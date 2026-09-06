#!/usr/bin/env bash
# Remove stale rows from the per-course knowledge bases.
#
# WHY THIS EXISTS: a re-ingest INSERTS a new `documents` row when a file's
# content has changed and leaves the old one in place, and it never removes rows
# for files that have since been deleted or newly excluded. The stale chunks keep
# their embeddings, so they stay live in search -- a corrected homework solution
# competes with the version it corrected. See FINDINGS.md § F-06.
#
# Re-ingest is therefore NOT idempotent. Run this after anything that regenerates
# corpus/ (i.e. after every prepare_corpus.py run).
#
# Removes, per KB:
#   - every `documents` row but the newest for a given filepath
#   - anything under a path component excluded AFTER it was first indexed
#     (listed in RETRO_EXCLUDE -- adding a pattern to config.yaml does not
#     retroactively remove what is already in the index)
set -euo pipefail
cd "$(dirname "$0")"

# Path fragments that config.yaml excludes but that predate the exclusion.
# Keep in sync with the `exclude:` block for patterns added after first ingest.
RETRO_EXCLUDE=('%/overleaf/%')

DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

psql_kb() {
    docker compose exec -T postgres \
        sh -c "psql -U \$POSTGRES_USER -d $1 -tAc \"$2\"" 2>/dev/null
}

# Build the OR-list once so the two branches below cannot drift apart.
retro_sql=""
for frag in "${RETRO_EXCLUDE[@]}"; do
    retro_sql+=" OR filepath LIKE '${frag}'"
done
doomed_cte="WITH ranked AS (
      SELECT id, row_number() OVER (PARTITION BY filepath ORDER BY created_at DESC) rn
      FROM documents)
    SELECT id FROM ranked WHERE rn > 1
    UNION SELECT id FROM documents WHERE false ${retro_sql}"

total=0
for db in $(psql_kb ragdb "SELECT datname FROM pg_database WHERE datname LIKE 'ragdb_%' ORDER BY 1;"); do
    n=$(psql_kb "$db" "SELECT count(*) FROM ($doomed_cte) d;")
    [[ -z "$n" || "$n" == "0" ]] && continue
    total=$(( total + n ))
    if (( DRY_RUN )); then
        printf '  %-22s would remove %s document(s)\n' "$db" "$n"
        continue
    fi
    # pg_dump before touching anything -- these deletes are not recoverable.
    mkdir -p .purge_backups
    docker compose exec -T postgres sh -c "pg_dump -U \$POSTGRES_USER -d $db" \
        > ".purge_backups/${db}-$(date +%Y%m%d-%H%M%S).sql" 2>/dev/null
    psql_kb "$db" "
      BEGIN;
      CREATE TEMP TABLE doomed AS $doomed_cte;
      DELETE FROM chunks    WHERE document_id IN (SELECT id FROM doomed);
      DELETE FROM documents WHERE id          IN (SELECT id FROM doomed);
      COMMIT;" >/dev/null
    left=$(psql_kb "$db" "SELECT count(*) FROM (SELECT filepath FROM documents GROUP BY filepath HAVING count(*)>1) t;")
    printf '  %-22s removed %-4s document(s), %s duplicate filepath(s) left\n' "$db" "$n" "$left"
done

(( total == 0 )) && echo "  nothing stale -- index is consistent with config"
exit 0
