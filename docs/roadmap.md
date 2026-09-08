# Roadmap v1

> Lean index only: milestone bullets + path refs. Detail lives in [plans/](./plans/INDEX.md), never here.
> Boundaries: [scope.md](./scope.md) · Rules: [directives/INDEX.md](./directives/INDEX.md) · Tasks: [todo.md](./todo.md)
> This tracks the **repo**, not the coursework. Assignment progress lives in each assignment's `README.md`.

**Mode: BOOTSTRAP → MAINTENANCE.** The corpus and the publishing pipeline have worked for a year;
what was missing was governance. Started 2026-09-04 — [DRIFT_REPORT.md](./DRIFT_REPORT.md).

## M1 — Root docs skeleton ✓ done (2026-09-04)
- [x] `scope.md` with a tiered Out-of-Scope blacklist and six named open questions
- [x] Five project-local directives + `INDEX.md` — [directives/INDEX.md](./directives/INDEX.md)
- [x] `INDEX.md` in every `docs/` subfolder except [`latex/`](./latex/) (owned elsewhere — [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 1)
- [x] Drift report and session record — [session_records/2026-09-04_catch-up.md](./session_records/2026-09-04_catch-up.md)

## M2 — Give the two newest doctrine courses an entry point ✓ done (confirmed 2026-09-06)
The preamble/duplication half of this milestone was **closed during the 2026-09-04 pass by another
writer** — all 7 `cesc_410` and 11 `cesc_470` problem files now input the shared preamble, and the old
course-local preamble is a documented tombstone. What is left is documentation, not migration.
Detail: [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 2.
- [x] `content/cesc_470/hw/prompt.md` — it has **11 written problem files** and no entry point
- [x] `content/cpsc_462/hw/prompt.md` — has macros, nothing else
- [ ] Both point at [directives/coursework-solutions.md](./directives/coursework-solutions.md) as the authority. **Do not clone `cesc_410`'s 149-line file** — most of it is now shared, and a copy will drift
- [ ] A `submission.md` per doctrine course. `content/cesc_410/hw/reference_docs/submission.md` carries four unanswered instructor questions; `cesc_470` and `cpsc_462` have not asked them
- [x] `docs/latex/INDEX.md` — the one folder this pass could not write into
- **Must-not-break:** `docs/latex/build_tex.sh content/cesc_410/hw/hw01` and `… content/cesc_470/hw/hw01` both build

## M2b — Coursework delivery standard ✓ done (2026-09-08)
Driven by two live failures: an operator sent to Canvas for a file that was not there, and a source
`.tex` uploaded to Overleaf that cannot build there.
- [x] [directives/human-task-instructions.md](./directives/human-task-instructions.md) — reason-coded human tasks, absolute paths, WHERE/WHAT/VERIFY/IF-ABSENT/BLOCKS, do-the-homework-first
- [x] All **19** source `.tex` across cesc_410/cesc_470 carry an Overleaf marker in their own first six lines; `new_tex.sh` writes it, `flatten_tex.sh` warns without it
- [x] `flatten_tex.sh --check` — content-compare, not timestamps; catches STALE / MISSING / ORPHAN; run automatically by `build_tex.sh`
- [x] `make_submission.sh` prints an archive **composition** report — a "code" zip that is 93% lockfile now says so
- [x] Repo-wide rule: **read the handout's own deliverables section**; over-submitting is a default for silence, not a policy
- [x] CESC 410L Lab 1 delivered and demoed — one file to upload
- **Must-not-break:** every flattened copy builds standalone; comment-only markers never change rendered output (both checked by measurement)
## M3 — File the loose root `.md`  (operator moves; agent proposes)
Per-file destinations and reasons: [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 3 · [scope.md](./scope.md) § Open questions #2
- [ ] `tmp_ocr_child.md` → `ocr_handler/docs/findings/` — holds the `/Ink`-object measurement that one side of an open `ocr_handler` contradiction depends on
- [ ] `tmp.md` → [`archives/operator-notes/`](./archives/operator-notes/INDEX.md)
- [ ] `note.md` → split into two runbooks; drop the stale `tree` listing
- [ ] `make_study_guide_master_prompt.md` → `runbooks/make-study-guide.md`
- [ ] `content/cesc_410/tmp.md` → `archives/operator-notes/` (doctrine course, so in bounds)


## M3b — docs-rag correctness  ← **next**
The index only grows: a re-ingest inserts rather than replaces, and exclusions are not retroactive —
[`docs-rag/FINDINGS.md`](../docs-rag/FINDINGS.md) F-06
- [x] Purge the 28 stale documents / 145 chunks live in search (2026-09-06)
- [x] [`docs-rag/purge_stale.sh`](../docs-rag/purge_stale.sh), verified against a restored pre-purge backup; required step in [`docs-rag/RUN.md`](../docs-rag/RUN.md)
- [ ] **Strip the `\input` preamble block in `prepare_corpus.py`** — every converted problem file wastes its first chunk on boilerplate that matches nothing
- [ ] **Re-examine `chunk_size` 256/50** — inherited unexamined; LaTeX tables and `aligned` environments exceed it
- **Must-not-break:** all 16 KBs healthy; a scoped `/api/v2/search` returns only its own course

## M4 — Make the build checkable
- [ ] `scripts/check.sh` — `hugo --minify` plus a known-correct assertion, not just exit 0 — [directives/testing-discipline.md](./directives/testing-discipline.md)
- [ ] Pin `hugo-version` in [`.github/workflows/pages.yml`](../.github/workflows/pages.yml); drop the no-op `git submodule update` step (there is no `.gitmodules`)
- [ ] Add a LaTeX build-check job for the doctrine courses
- **Must-not-break:** a push to `main` publishes the site

## M5 — Adopt the orphaned scripts, or archive them
Six scripts, zero references anywhere — [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 5
- [ ] `runbooks/scripts.md`, or archive the dead ones
- [ ] `scripts/refactor_standard_equations.sh` gets a `--dry-run` and a provenance header, or is archived — it rewrites **every `.md` in the repo** in place
- [ ] Rename `scripts/latex_to_pdf.sh` — it builds a résumé, and the name collides with the two real coursework builders

## M6 — Distil the repo-wide lessons ✓ done (2026-09-06)
All three owed lessons written, plus eleven more — [lessons_learned/lessons.md](./lessons_learned/lessons.md)
- [x] KI-09 — tooling references must never reach a submitted document
- [x] docs-rag F-01 — a silent-success ingest is worse than a failure
- [x] HW-01 — never read maths out of a PDF text layer
- [x] Eleven further lessons earned since, incl. docs-rag F-06 (re-ingest is not idempotent), the
      `grep -q`/pipefail SIGPIPE race (18 of 40 false negatives), and Overleaf's inability to resolve
      paths above its project root

## M7 — Site navigation  (blocked on an operator answer)
- [ ] Decide whether solutions are published publicly — [scope.md](./scope.md) § Open questions #1
- [ ] Then: `_index.md` per course, or `ignoreFiles` — [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 7

## Child projects — linked, never summarised here
- [`ocr_handler/docs/roadmap.md`](../ocr_handler/docs/roadmap.md) — M1 done, M2 (one extractor) next
- [`docs-rag/`](../docs-rag/) — **not bootstrapped and untracked in git.** Candidate for `## Bootstrap Existing` — [scope.md](./scope.md) § Open questions #5

## Scripts
- Build the site `hugo --minify` · Build-check a `.tex` [`docs/latex/build_tex.sh <path>`](./latex/build_tex.sh) · Deploy: CI on push to `main`
- No install script and none needed (Hugo + tectonic + `uv` are system tools). No root test suite — see [directives/testing-discipline.md](./directives/testing-discipline.md) for why.
