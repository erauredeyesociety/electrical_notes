# TODO — single source of truth

> Last updated: 2026-09-06 · **MODE: maintenance**
> Index, not an essay. Detail lives behind the links.

## CURRENT STATE

**Governance exists and is now populated.** [scope.md](./scope.md), [roadmap.md](./roadmap.md), this
file, six directives, two ADRs in [decisions/](./decisions/INDEX.md), and — as of 2026-09-06 —
[lessons_learned/lessons.md](./lessons_learned/lessons.md), which had been an empty folder flagged as a
gap since bootstrap. Origin: [DRIFT_REPORT.md](./DRIFT_REPORT.md).

**M2 is complete.** `content/cesc_470/hw/prompt.md`, `content/cpsc_462/hw/prompt.md` and
`docs/latex/INDEX.md` all exist — written by an earlier pass and never marked done.

**The coursework doctrine is live across the three newest courses** (`cesc_410`, `cesc_470`,
`cpsc_462`) — [directives/coursework-solutions.md](./directives/coursework-solutions.md) plus
[`docs/latex/`](./latex/). Older courses are deliberately out of scope.

**docs-rag serves 16 per-course knowledge bases**, all healthy. A correctness defect was found and
closed 2026-09-06: **a re-ingest inserts rather than replaces**, so 28 stale documents / 145 chunks —
including superseded homework solutions — were live in search.
[`docs-rag/purge_stale.sh`](../docs-rag/purge_stale.sh) is now a required step in
[`docs-rag/RUN.md`](../docs-rag/RUN.md).

Last session: [session_records/2026-09-06_rag-staleness-and-lessons.md](./session_records/2026-09-06_rag-staleness-and-lessons.md).

## NEXT ACTION

**Make the RAG's LaTeX-derived chunks carry content — [`docs-rag/`](../docs-rag/).** Cheap, measurable,
and it degrades every answer sourced from coursework today:

1. **Strip the `\input` preamble block in `prepare_corpus.py`** before conversion. A converted `.md`
   currently spends its first chunk on `\input{../../../../docs/latex/coursework_preamble.tex}`
   boilerplate that matches nothing.
2. **Re-examine `chunk_size` 256/50** — inherited unexamined, and LaTeX tables and `aligned`
   environments exceed it.
3. Then purge and re-ingest — in that order ([`docs-rag/RUN.md`](../docs-rag/RUN.md)).

Then [roadmap.md](./roadmap.md) § M3 (loose root `.md`, operator moves) and § M4 (`scripts/check.sh`,
pin `hugo-version`).

## Blocked / awaiting operator

Six named calls, all in [scope.md](./scope.md) § Open questions. Batch them; none should be guessed.
Highest-impact first:

- **#1 — are worked solutions published publicly?** `content/cesc_410/hw/hw01/` tracks six solution `.tex`
  files that Hugo publishes to a site under the institution's GitHub org. This also gates § M7.
- **#2 — where do the four loose root `.md` files go?** Recommendations in
  [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 3. `tmp_ocr_child.md` is the urgent one.
- **#4 — pin `hugo-version` in CI?** It is `latest`, so an upstream release can break the public site.

## Known issues

- **`scripts/refactor_standard_equations.sh` is a destructive, undocumented, repo-wide in-place rewrite.**
  Running it today would rewrite twelve frozen course folders. § 5.
- **docs-rag re-ingest is not idempotent** — it inserts rather than replaces, and exclusions are not
  retroactive, so the index only grows ([`docs-rag/FINDINGS.md`](../docs-rag/FINDINGS.md) F-06).
  `purge_stale.sh` closes it, but it must actually be run.
- **LaTeX-derived chunks open with `\input` boilerplate** that matches nothing — a wasted chunk per
  converted problem file at `chunk_size` 256.
- **Four `ocr_handler` modules are untracked** — `crops.py`, `latex_repair.py`, `structure.py`,
  `validity.py`, plus `tools/` and `tests/fixtures/`. `textlayer.py` is now tracked. Repeated here
  because they are one `git clean` from gone. **Git is human-only** — reported, never resolved.
- **Many uncommitted paths across the repo.** Git is human-only — the state is reported, never resolved.
  Git is human-only — the count is reported, never resolved.
- **`.github/workflows/pages.yml` runs `git submodule update`** against a repo with no `.gitmodules`.
  Harmless no-op, misleading to read.

## Doctrine gaps

- `docs-rag/` is a child project with no bootstrap and no git tracking. [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 9.
  It now carries `FINDINGS.md`, `RUN.md` and `purge_stale.sh`, but not the doctrine tree.

**Closed 2026-09-06:** ~~`docs/latex/` has no `INDEX.md`~~ · ~~`lessons_learned/` is empty~~ (14 lessons
written) · ~~`decisions/` is empty~~ (two ADRs) · ~~the `session_records/` vs `archives/` convention is
unsettled~~ ([session_records/INDEX.md](./session_records/INDEX.md) — the contradiction was in the
bootstrap, not here).

---

**See:** [roadmap.md](./roadmap.md) · [scope.md](./scope.md) · [DRIFT_REPORT.md](./DRIFT_REPORT.md) · [directives/INDEX.md](./directives/INDEX.md)
