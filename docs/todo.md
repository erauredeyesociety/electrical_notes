# TODO — single source of truth

> Last updated: 2026-09-04 · **MODE: bootstrap → maintenance**
> Index, not an essay. Detail lives behind the links.

## CURRENT STATE

**The root `docs/` tree exists for the first time.** `electrical_notes` had never been bootstrapped;
`docs/` was an empty eleven-folder skeleton this morning. It now carries [scope.md](./scope.md),
[roadmap.md](./roadmap.md), this file, [README.md](./README.md), six directives and an `INDEX.md` in every
subfolder but [`latex/`](./latex/). Full account: [DRIFT_REPORT.md](./DRIFT_REPORT.md).

**Nothing outside `docs/` was touched.** No file under `content/`, `ocr_handler/`, `docs-rag/` or
`docs/latex/` was created, moved, edited or deleted. Everything the drift report recommends is a
proposal awaiting the operator.

**The coursework doctrine landed today too** —
[directives/coursework-solutions.md](./directives/coursework-solutions.md) plus
[`docs/latex/`](./latex/). Another writer migrated `content/` to it **concurrently with this pass**:
all 7 `cesc_410` and 11 `cesc_470` problem files now input the shared preamble, and the superseded
course-local preamble is a documented tombstone. [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 2 was rewritten
at 16:26 to match what is actually on disk.

## NEXT ACTION

**Give `cesc_470` and `cpsc_462` an entry point — [roadmap.md](./roadmap.md) § M2, detail in
[DRIFT_REPORT.md](./DRIFT_REPORT.md) § 2.**

`content/cesc_470/hw/hw01/` holds **eleven written problem files and a solutions document**, and
`content/cesc_470/hw/` has no `prompt.md`, no `findings.md`, no `submission.md` — only
`reference_docs/cesc470_macros.tex`. `content/cpsc_462/hw/` is the same, with nothing written yet. An
agent entering through the course folder, which is exactly how `content/cesc_410/hw/prompt.md` is
designed to be entered, finds nothing.

1. **Write `content/cesc_470/hw/prompt.md`** — short. Point at
   [directives/coursework-solutions.md](./directives/coursework-solutions.md) as the authority; name only
   what is course-specific. **Do not clone `cesc_410`'s 149 lines**; most of it is now shared and a copy
   will drift.
2. **Same for `content/cpsc_462/hw/`.**
3. **A `submission.md` per doctrine course.**
   `content/cesc_410/hw/reference_docs/submission.md` is marked unconfirmed and carries four questions
   for the instructor. The other two courses have not asked them.

## Blocked / awaiting operator

Six named calls, all in [scope.md](./scope.md) § Open questions. Batch them; none should be guessed.
Highest-impact first:

- **#1 — are worked solutions published publicly?** `content/cesc_410/hw/hw01/` tracks six solution `.tex`
  files that Hugo publishes to a site under the institution's GitHub org. This also gates § M7.
- **#2 — where do the four loose root `.md` files go?** Recommendations in
  [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 3. `tmp_ocr_child.md` is the urgent one.
- **#4 — pin `hugo-version` in CI?** It is `latest`, so an upstream release can break the public site.

## Known issues

- **`content/cesc_470/hw/` and `content/cpsc_462/hw/` have no `prompt.md`.** The two newest doctrine
  courses are the least documented; `cesc_470` already has eleven written problem files.
  [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 2.
- **`scripts/refactor_standard_equations.sh` is a destructive, undocumented, repo-wide in-place rewrite.**
  Running it today would rewrite twelve frozen course folders. § 5.
- **`docs-rag` cannot ingest `.tex` and fails silently** — it warns, indexes zero files, and reports
  success ([`docs-rag/FINDINGS.md`](../docs-rag/FINDINGS.md) F-01). Any RAG answer sourced from LaTeX
  coursework is unreliable until this is fixed. The workaround needs `pandoc -f latex+raw_tex`; plain
  `-f latex` discards exactly the custom-macro content the answers live in.
- **`ocr_handler/src/ocr_handler/textlayer.py` is untracked** — the module its shipped CLI depends on
  exists on disk only. Flagged in that project's own todo; repeated here because it is one `git clean`
  from gone.
- **49 uncommitted paths** at 16:26, including all of `docs/` and all 417 files of `docs-rag/`.
  Git is human-only — the count is reported, never resolved.
- **`.github/workflows/pages.yml` runs `git submodule update`** against a repo with no `.gitmodules`.
  Harmless no-op, misleading to read.

## Doctrine gaps

- [`docs/latex/`](./latex/) has no `INDEX.md` — the one folder this pass could not write into.
- `docs/lessons_learned/` is empty. Three lessons are already earned and only need distilling —
  [lessons_learned/INDEX.md](./lessons_learned/INDEX.md), [roadmap.md](./roadmap.md) § M6.
- `docs/decisions/` is empty. The retrofit boundary and the shared-toolchain choice were both real
  decisions made today and are recorded only in prose —
  [decisions/INDEX.md](./decisions/INDEX.md).
- `docs-rag/` is a child project with no bootstrap and no git tracking. § 9.

---

**See:** [roadmap.md](./roadmap.md) · [scope.md](./scope.md) · [DRIFT_REPORT.md](./DRIFT_REPORT.md) · [directives/INDEX.md](./directives/INDEX.md)
