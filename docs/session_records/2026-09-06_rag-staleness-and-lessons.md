# 2026-09-06 — The RAG index only grows; lessons distilled

**Seat:** PM2 Project-Lead · **Mode:** maintenance · **Outcome:** a live correctness defect in docs-rag found and closed; `lessons_learned/` filled; M2 confirmed complete

---

## What was done

### A correctness defect in the live RAG, found by accident

While verifying that a re-ingest had landed, a scoped query returned a homework solution **that had
already been corrected**. Root cause: **the index only ever grows.**

A re-ingest *inserts* a new `documents` row when a file's content has changed and leaves the old row in
place. It also never removes rows for files since deleted or newly excluded. The stale chunks **keep
their embeddings**, so they stay live in search. Measured on one file:

| row | created | content_hash | chunks | embedded |
| --- | --- | --- | ---: | ---: |
| 152 | 2026-09-05 21:01 | `0dbdcfc5…` | 3 | 3 |
| 173 | 2026-09-06 15:33 | `df6081a2…` | 3 | 3 |

Same path, different hash, both retrievable, and **nothing in the response marks which is which.**

Two symptoms, one cause:

| Symptom | Count | Why |
| --- | ---: | --- |
| Same filepath indexed twice | 12 (cesc_410), 11 (cesc_470) | content changed between ingests; insert, not upsert |
| `overleaf/` files indexed despite the exclusion | 5 (cesc_410) | all created 09-05 21:03, **before** the pattern was added |

Confined to `cesc_410` and `cesc_470` — the only two courses with the `.tex` → `.md` prepare step and
the Overleaf flatten step, i.e. the only ones whose files get regenerated. The other 13 KBs measured
**zero**.

**Cleanup:** `pg_dump` both databases, then per KB in one transaction select the doomed ids (every row
but the newest per `filepath`, unioned with anything under `/overleaf/`), delete their `chunks`, then
the `documents`. Removed **28 documents / 145 chunks** — cesc_410 61 → 44 docs, cesc_470 28 → 17.
Post-checks: 0 duplicate filepaths, 0 overleaf rows, and a scoped `/api/v2/search` on each KB returns
only that course's files.

**Made executable, not just documented:** `docs-rag/purge_stale.sh` (with `--dry-run`, and a `pg_dump`
before every real run). Verified by restoring the pre-purge backup into a scratch database — it flagged
**exactly the 11 rows** removed by hand from cesc_470. Now a required step in `docs-rag/RUN.md`.

### `lessons_learned/` filled in both projects

Empty in both, and flagged as a doctrine gap since 2026-09-04. Now written:
[lessons_learned/lessons.md](../lessons_learned/lessons.md) (14 lessons — coursework/LaTeX, docs-rag,
shell/operations, repo governance) and the child project's
[`ocr_handler/docs/lessons_learned/lessons.md`](../../ocr_handler/docs/lessons_learned/lessons.md)
(15 lessons — measurement, detectors, code, cost/hardware). The three lessons each INDEX was *owing*
are among them, with their measurements.

### M2 confirmed complete

`content/cesc_470/hw/prompt.md`, `content/cpsc_462/hw/prompt.md` and `docs/latex/INDEX.md` all exist —
the milestone's remaining items, written by an earlier pass and never marked done.

---

### Later in the same session — one parent-repo change

`tmp_ocr_child.md` (root, awaiting the M3 operator move) carries a **disproven** claim: *"7 `/Ink`
objects … handwriting here is geometry, not pixels"* and `"Needs OCR? No — it is vector ink"`.
Measured across all three annotated lectures: **0 `/Subtype/Ink` objects**, 6 / 36 / 14 raster
XObjects. The `/Ink` keys are opaque base64 blobs in vendor `/Private` dicts.

This mattered — the contradiction between that note and a later measurement blocked `ocr_handler`
milestone M4 for days, because only one of the two could be the right extraction path. It is the raster
path.

A **correction banner** was prepended; the body is untouched, because it is a dated operator note
rather than a maintained document, and moving it is an [M3](../roadmap.md) operator action. Evidence:
[`ocr_handler/docs/findings/mask-separability-by-stratum-2026-09-06.md`](../../ocr_handler/docs/findings/mask-separability-by-stratum-2026-09-06.md).

## Decisions made

| Decision | Rationale |
| --- | --- |
| **Purge is a required step, not an optional cleanup** | Re-ingest is not idempotent. Any workflow rebuilding `corpus/` — every `prepare_corpus.py` run — must purge, or the KB serves two answers and prefers neither |
| **Delete stale rows rather than rebuild the KBs** | Targeted, cheap, verifiable, and avoids re-embedding 89 documents through the tunnel. Backed by `pg_dump` first |
| **Keep the 09-05 `overleaf/` exclusion as written** | The pattern is correct; `_is_excluded` documents `"name/"` as a path-component match and the 09-06 ingest honoured it. Only the pre-existing rows were wrong |

---

## Discoveries

### The obvious diagnosis was wrong twice

Both wrong readings are recorded because each looks exactly like a different, worse bug:

1. **Duplicate hits looked like `overleaf/` being triple-indexed.** They were chunk counts, not
   documents.
2. **Cross-course results looked like broken per-course routing** — the whole point of the 16-KB split.
   The parameter name differs by endpoint: `/api/search` and `/api/v1/search` take **`corpus`**,
   `/api/v2/search` takes **`kb`**. An unrecognised field is **silently ignored** and the query runs
   unscoped. `ragdb_cesc_410` contains only cesc_410 files, 61 of 61 — routing was never in question.

### An exclusion is not retroactive

Adding `"overleaf/"` to `config.yaml` stopped new ingestion and did nothing to the five rows already
indexed. Worth stating explicitly because the obvious diagnosis — a bad glob — sends you to edit a
config that is already correct.

---

## Blockers

- **ResearchHub is unavailable** — pwnstar is down (`No route to host`), not a VPN issue.
- **Chunk size 256/50 was inherited unexamined** and is likely wrong for LaTeX-derived content; a
  `.tex`-converted `.md` spends its first chunk on `\input` preamble boilerplate that matches nothing.
- **Six operator calls** remain in [scope.md](../scope.md) § Open questions, unchanged.
- **Uncommitted paths across the repo.** Git is human-only — reported, never resolved.

---

## Next

1. **Re-examine `chunk_size`** for LaTeX-derived content — the boilerplate-only first chunk is a
   measurable waste and the fix is cheap.
2. **Strip the `\input` preamble block in `prepare_corpus.py`** before conversion, so the first chunk
   carries content.
3. **M3** — the loose root `.md` files are operator moves; the proposals stand in
   [DRIFT_REPORT.md](../DRIFT_REPORT.md) § 3.
4. **M4** — `scripts/check.sh` and pinning `hugo-version`.

---

**See:** [../roadmap.md](../roadmap.md) · [../todo.md](../todo.md) ·
[`docs-rag/FINDINGS.md`](../../docs-rag/FINDINGS.md) F-06 ·
[../lessons_learned/lessons.md](../lessons_learned/lessons.md)
