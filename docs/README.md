# electrical_notes — docs

**Governance for the repository.** Not the coursework itself — that lives under
[`content/`](../content/), and each course folder documents itself.

`electrical_notes` holds one student's coursework for **15 courses** and publishes it as a static Hugo
site at <https://erauredeyesociety.github.io/electrical_notes/>. Everything under `content/` is on that
public site.

**Status:** the corpus and the publishing pipeline have worked for a year. This `docs/` tree is new —
created 2026-09-04, the repo's first bootstrap. What it fixes and what it found:
[`DRIFT_REPORT.md`](./DRIFT_REPORT.md).

---

## Start here

| Read | For |
| --- | --- |
| [`scope.md`](./scope.md) | What this repo is and is not. The blacklist, and six open operator questions. |
| [`directives/coursework-solutions.md`](./directives/coursework-solutions.md) | **The coursework workflow.** How a homework, quiz or exam solution gets written. |
| [`directives/INDEX.md`](./directives/INDEX.md) | How to work in this repo — six condensed rules. |
| [`roadmap.md`](./roadmap.md) | Milestones for the *repo*. Lean index only. |
| [`todo.md`](./todo.md) | Current state and next action. |
| [`DRIFT_REPORT.md`](./DRIFT_REPORT.md) | What is out of date, ordered by impact, with paths. |

## The one rule most likely to be broken

The coursework doctrine applies to **`cesc_470`, `cesc_410`, `cpsc_462`, and courses started after
2026-09-04**. The other twelve course folders are **frozen and are not to be retrofitted** — an explicit
operator decision. "It would be more consistent" is not a reason; it is the thing the rule forbids.
→ [`scope.md`](./scope.md) · [`directives/scope-discipline.md`](./directives/scope-discipline.md)

## Layout

```
content/          15 course folders — the coursework, published by Hugo
  cesc_410/         hw/ and labs_and_projects/, each with prompt.md + reference_docs/ + tools/
  cesc_470/         newest doctrine course
  cpsc_462/         notes generated from .pptx/.docx by tools/extract_notes.py
docs/             ← you are here. Governance for the repo.
  latex/            shared coursework toolchain: coursework_preamble.tex + build_tex.sh
  directives/       standing rules
  findings/ research/ lessons_learned/ decisions/ plans/ runbooks/ features/
  session_records/  dated narrative → archives/session_records/ when stale
  archives/         superseded material, incl. operator-notes/
ocr_handler/      CHILD PROJECT — one text extractor for every course. Own docs/, own tests/.
docs-rag/         CHILD PROJECT — retrieval over the corpus, one knowledge base per course.
scripts/          six utility scripts, currently unreferenced from anywhere
.github/          the only CI: build the site and publish it
```

## Building

```sh
hugo --minify                                          # the site; what CI runs
docs/latex/build_tex.sh content/cesc_470/hw/hw01       # build-check an assignment
docs/latex/build_tex.sh content/cesc_470/hw/hw01/p01_five_components.tex
docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep   # keep the PDFs
```

Paths are repo-relative. `build_tex.sh` deletes the PDF unless `--keep` — the question it answers is
"does it compile", not "does it look right".

## Conventions

- **Git is human-only.** Agents propose commands; the operator runs them.
- **Nothing under `content/` is moved or deleted by an agent.** Say where it should go; let the operator
  move it.
- **PDFs, figures, zips and `.venv` are build products** — gitignored, rebuilt from tracked sources.
  Instructor source PDFs are the exception and are kept by explicit negation in each `.gitignore`.
- **Never read maths out of a PDF text layer.** Render the region and look at it — `pdftotext` turns
  $\cos(\tfrac{\pi}{6}n)$ into `cos( 6π n)` without raising an error.
- **No tooling references in a submitted document** — no script names, flags or repo paths.
- **Child projects are reached by path, never restated.** [`ocr_handler/docs/`](../ocr_handler/docs/README.md)
  is the in-repo reference for what these standards look like when fully applied.

## Documentation folders

| Folder | Holds |
| --- | --- |
| [`findings/`](./findings/INDEX.md) | INTERNAL — what we discovered about **this repo** |
| [`research/`](./research/INDEX.md) | EXTERNAL — teardowns of tools outside this repo |
| [`lessons_learned/`](./lessons_learned/INDEX.md) | PRESCRIPTIVE — WHEN → DON'T → BECAUSE |
| [`decisions/`](./decisions/INDEX.md) | ADRs — immutable; supersede, never edit |
| [`plans/`](./plans/INDEX.md) | Tactical *how* for work not yet done |
| [`runbooks/`](./runbooks/INDEX.md) | Repeatable operator procedures |
| [`features/`](./features/INDEX.md) | Specs for shipped-stable capabilities |
| [`session_records/`](./session_records/INDEX.md) | Dated per-session narrative |
| [`archives/`](./archives/INDEX.md) | Superseded material — archive, never erase |
