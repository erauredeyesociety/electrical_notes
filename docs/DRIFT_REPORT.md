# Drift Report — 2026-09-04

> **This is not a drift catch-up. It is a first bootstrap.**
> `electrical_notes` has **never been bootstrapped**. `docs/` at the repo root was created empty minutes
> before this pass — eleven folders, three files, all of them written today. There is no prior structure
> to have drifted *from*, so "drift" here means **the gap between what is on disk and what current
> standards require**, not decay of a previous bootstrap.
>
> The `## Catch Up` prune passes (prune-docs / prune-tests / folder reshuffle) were **not run**: there is
> nothing accreted at the root to prune, and the accretion that *does* exist is inside course folders the
> operator has ruled out of bounds.
>
> **Nothing under `content/`, `ocr_handler/`, `docs-rag/` or `docs/latex/` was created, moved, edited or
> deleted.** Every recommendation below is a proposal for the operator.

Ordered by impact. Every path is real and was checked.

---

## 1 — Structure: the root repo had no boundary contract at all  ·  **fixed this pass**

**Was:** no `scope.md`, no `roadmap.md`, no `todo.md`, no `README.md`, no directives, no `INDEX.md`
anywhere. The only root-level orientation was `README.md` — 130 bytes, *"Notes for classes, mostly AI
generated"* plus a link to the hextra theme docs. A session starting cold had nothing to read.

Meanwhile the repo is **2,089 git-tracked files across 15 course folders**, a public publishing pipeline,
two child projects, and a coursework doctrine that was written today and had nowhere to be referenced
from.

**Now:**

| File | Purpose |
| --- | --- |
| [scope.md](./scope.md) | Boundary contract + the Out-of-Scope blacklist + six open operator questions |
| [roadmap.md](./roadmap.md) | Lean milestone index |
| [todo.md](./todo.md) | CURRENT STATE / NEXT ACTION |
| [README.md](./README.md) | What this repo is, how it builds, where to read next |
| [directives/INDEX.md](./directives/INDEX.md) | Six project-local rules (§ 6) |
| `INDEX.md` in all ten remaining `docs/` subfolders | Navigation, per the mandatory INDEX rule |

**Still open:** [`docs/latex/`](./latex/) has **no `INDEX.md`**, which the standard requires of every docs
folder. That folder is owned by another writer this session and was deliberately left alone. It needs
one line describing `coursework_preamble.tex` and `build_tex.sh` and a pointer to
[coursework-solutions.md](./directives/coursework-solutions.md).

---

## 2 — The doctrine seam: **mostly closed during this pass**, one real gap left

> ⚠ **This section was rewritten at 16:26 after re-verification.** Another writer was migrating
> `content/` concurrently with this pass. The duplication originally found here — two live definitions of
> `answerbox`, a course-local `prompt.md` that never mentioned the shared directive — **was fixed while
> this report was being written.** What follows is the state on disk now, re-checked, not what was true
> at 16:16.

**What is now correct** (verified 2026-09-04 16:26):

| Check | Result |
| --- | --- |
| `content/cesc_410/hw/hw01/*.tex` inputs the shared preamble | **7 of 7** — `\input{../../../../docs/latex/coursework_preamble.tex}` + `../reference_docs/cesc410_macros.tex` |
| `content/cesc_470/hw/hw01/*.tex` inputs the shared preamble | **11 of 11**, same two lines with `cesc470_macros.tex` |
| `content/cesc_410/hw/prompt.md` points at the shared toolchain | Yes — it now names `docs/latex/coursework_preamble.tex` in its read-first list and `docs/latex/build_tex.sh` in its build commands |
| The old course-local preamble | `content/cesc_410/hw/reference_docs/cesc410_preamble.tex` is now an explicit **tombstone** — its first line reads *"SUPERSEDED — do not `\input` this file"* and explains the split. A repo-wide grep finds **zero** remaining references to it. That is the right way to retire a file. |
| `content/cesc_410/hw/tools/build_tex.sh` | Still present, still works, and its header now defers: *"the SHARED build-checker is now `docs/latex/build_tex.sh` … Prefer it."* A deliberate deprecated alias, not an undocumented duplicate. |
| `content/cpsc_462/hw/reference_docs/cpsc462_macros.tex` | Created — the third doctrine course now has its notation file |

**The one gap that remains, and it is real:**

**Neither `content/cesc_470/hw/` nor `content/cpsc_462/hw/` has a `prompt.md` or any prose reference
docs.** Both have macros. `cesc_470/hw/hw01/` has **eleven written problem files and a solutions
document**. `content/cesc_410/hw/` has a 149-line `prompt.md`, a `findings.md` with seven damage-ordered
findings, an `hw_workflow.md` and a `submission.md`.

So an agent entering through `content/cesc_470/hw/` — the way `cesc_410`'s own `prompt.md` is designed
to be entered — finds nothing. The two most-recently-started doctrine courses are the least documented.

**Recommend:**
1. A short `content/cesc_470/hw/prompt.md` and `content/cpsc_462/hw/prompt.md`, each pointing at
   [coursework-solutions.md](./directives/coursework-solutions.md) as the authority and naming only what
   is course-specific. **Do not clone `cesc_410`'s 149 lines** — most of it is now in the shared
   directive, and a copy will drift.
2. A `submission.md` per doctrine course. `content/cesc_410/hw/reference_docs/submission.md` is
   explicitly marked unconfirmed with four questions for the instructor; `cesc_470` and `cpsc_462` have
   not even asked them.

**Not a defect, worth knowing:** `content/cesc_410/hw/tools/course_text.py` (PDF text extraction for
citation grepping) and `content/cpsc_462/tools/extract_notes.py` (`.docx`/`.pptx` → Markdown) are two of
the three per-course extractors that `ocr_handler` exists to replace — its scope names both by path
([`ocr_handler/docs/scope.md`](../ocr_handler/docs/scope.md) § Overview). They stay until `ocr_handler`
reaches parity; retiring them is on that project's roadmap, not this one.

---

## 3 — Loose `.md` in the repository root  ·  **reported, nothing moved**

Four files sit at the root. The hub guide tolerates `tmp*.md` at a root as *scratch*; two of these hold
durable knowledge that exists nowhere else, which is the anti-pattern `ocr_handler`'s own directive
already names by filename
([`ocr_handler/docs/directives/documentation-discipline.md`](../ocr_handler/docs/directives/documentation-discipline.md)).

| File | What it actually is | Belongs at | Priority |
| --- | --- | --- | --- |
| [`tmp_ocr_child.md`](../tmp_ocr_child.md) (10.3 KB) | **A findings document.** Written 2026-09-02 from real measurements: the Type A/B/C lecture-PDF taxonomy, the **7 `/Ink` vector stroke objects** on the annotated page, and the warning that two unrelated kinds of file share the `-plw` suffix so the Producer string is the only reliable discriminator. `ocr_handler/docs/findings/INDEX.md` **already cites it by its root path** as a known misplacement. | `ocr_handler/docs/findings/lecture-pdf-taxonomy.md` | **High** — the `/Ink` count contradicts a later measurement, and `ocr_handler/docs/todo.md` lists resolving that contradiction as an M4 blocker. Losing this file loses one side of the contradiction. |
| [`tmp.md`](../tmp.md) (4.7 KB) | Verbatim operator prompts — the requirement history that produced `tmp_ocr_child.md` and `ocr_handler/`. Immutable record. | `docs/archives/operator-notes/2026-09-02_ocr-handler-request.md` | Medium |
| [`note.md`](../note.md) (1.5 KB) | Two runbooks welded together: the Hugo/`hugo mod` site bootstrap, and the pandoc+xelatex cheat-sheet incantation. Plus a `tree` listing from when the repo had 11 files — **stale, delete that part**. | Split → `docs/runbooks/hugo-site.md` and `docs/runbooks/cheat-sheet-pdf.md` | Medium — the cheat-sheet half is the live half of `scripts/gen_cheat_sheet.sh` (§ 5) |
| [`make_study_guide_master_prompt.md`](../make_study_guide_master_prompt.md) (3.7 KB) | A reusable, course-agnostic prompt template. A repeatable operator procedure. | `docs/runbooks/make-study-guide.md` | Low |

An empty [`docs/archives/operator-notes/`](./archives/operator-notes/INDEX.md) was created to receive the
second row, following the exemplar at `~/sys301_minesweeper/docs/archives/operator-notes/`.

**Seven more `tmp*.md` sit under `content/`:** `cec_320/homework/tmp_03_13_2026.md`,
`cec_320/labs_and_projects/tmp.md`, `cec_320/labs_and_projects/lab10/tmp.md`, `cesc_410/tmp.md`,
`cesc_420/tmp.md`, `ee_300/tmp.md`, `sys_304/exam3/tmp.md`. `cesc_410/tmp.md` (94 lines) is the operator
prompt log that produced the entire `labs_and_projects/` workflow — the same class of record as root
`tmp.md`. **The other six are in frozen courses and are out of bounds** ([scope.md](./scope.md) § blacklist).

---

## 4 — Project knowledge lives outside `docs/`, in five separate conventions

Content that the standard routes to `docs/findings/` and `docs/lessons_learned/` already exists, written
well, in five different in-tree shapes. **None of it is wrong where it is** — course-local material ships
with the coursework it serves — but nothing at the root points to any of it, so it is invisible to a
session that starts at `docs/`.

| Where | What | Under new doctrine? |
| --- | --- | --- |
| `content/cesc_410/hw/reference_docs/findings.md` | 7 findings ordered by damage — HW-01 `pdftotext` corrupts fractions; HW-03 `\angle` makes a following minus binary; HW-06 `axis lines=middle` draws the y-label through the data | **Yes** |
| `content/cesc_410/labs_and_projects/reference_docs/known_issues.md` | **KI-01…KI-09** — repeated `plt.figure(N)` overplots · `plt.show()` no-ops headless · `myID` is a per-student seed · `uv` is not in the package manager · ImageMagick renders matplotlib SVG blank · setting the ERAU ID may not change figures · `splitlines()`/`tokenize` desync corrupted stripped output · stripping docstrings removes Typer `--help` · **tooling references leaked into a submitted report** | **Yes** |
| `content/cec_320/labs_and_projects/` | `known_issues.md`, `findings/cubeide_*.md`, `SYSTEM_ANALYSIS.md`, `LAB_PROJECT_ANALYSIS_PROCEDURE.md` — the ancestor of the cesc_410 system | Frozen |
| `content/cesc_420/docs/findings/F01…F10` + `INDEX.md` | A capstone-proposal doc set that already follows the taxonomy, inside a course folder | Frozen |
| `content/cec_315/*.md` (8 loose files) | `latex_layout_tips.md`, `html_pagination_tips.md`, `js_screenshot_alternatives.md`, … — de-facto findings predating the `reference_docs/` convention | Frozen |
| `content/stat_412/findings.md` | Course-level findings file | Frozen |
| [`docs-rag/FINDINGS.md`](../docs-rag/FINDINGS.md) | **F-01 is repo-wide and load-bearing:** the ingester has no `.tex` handler and **fails silently** — it warns, indexes zero files, and reports success. The pandoc workaround must use `-f latex+raw_tex`, because plain `-f latex` discards custom-macro content, which is exactly where the answers are (`\finalanswer` in stat_412, `answerbox` in cesc_410). | Child project |

**Recommend:** do **not** move any of it. Instead the root [`findings/INDEX.md`](./findings/INDEX.md) and
[`lessons_learned/INDEX.md`](./lessons_learned/INDEX.md) **cite them by path** — done this pass — and any
lesson that generalises past its course gets *distilled* (one WHEN→DON'T→BECAUSE line) into
`docs/lessons_learned/`, never copied. Two are already repo-wide in effect and are the obvious first
candidates: **KI-09** (tooling references must never reach a submitted document — already promoted into
[coursework-solutions.md](./directives/coursework-solutions.md) § Repo hygiene) and **docs-rag F-01**
(a silent-success ingest is worse than a failure).

---

## 5 — Testing and scripts: nothing is scripted, nothing is checked, one script is destructive

**There is no test layout at the repo root, and there should not be a `tests/persistent/` unit suite** —
the root ships no application code. What it ships is artifacts that either build or do not. See
[directives/testing-discipline.md](./directives/testing-discipline.md).

**What is missing:**

| Gap | Evidence |
| --- | --- |
| **No local build check** | Nothing runs `hugo --minify` before a push. The first place a broken site is discovered is CI, after `main` already moved. |
| **CI checks nothing but the build** | [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) is checkout → submodule → `actions-hugo` → `hugo --minify` → deploy. No lint, no link check, no LaTeX build. |
| **`hugo-version: latest` is unpinned** | An upstream Hugo release can break the **public site** with no local change. → [scope.md](./scope.md) § Open questions #4. |
| **No LaTeX build check in CI** | [`docs/latex/build_tex.sh`](./latex/build_tex.sh) exists and works, but a `.tex` that stops compiling is only caught when someone runs it by hand. |
| **`.github/workflows/pages.yml` runs `git submodule update`** | There is **no `.gitmodules`** in this repo — the theme comes in as a Hugo *module* (`hugo.yaml` → `module.imports`), not a submodule. The step is a no-op left from an older setup. Harmless, misleading. |

**`scripts/` — six files, and a repo-wide grep for all six names returns zero references outside the
files themselves** (and, now, this `docs/` tree). They are orphaned: not in the root `README.md`, not in
`note.md`, not in any course doc, not in CI.

| Script | What it does | Note |
| --- | --- | --- |
| `refactor_standard_equations.sh` | Bulk `perl -i` rewrite across **every `.md` in the repo** — strips nested `$` around `\geq`/`\leq`/`\times`/`\pm`/`\approx`, converts Unicode maths to LaTeX | ⚠ **Destructive, in-place, repo-wide, and undocumented.** Running it today would rewrite twelve frozen course folders. It needs a header saying what it did, when it was last run, and a `--dry-run`, or it needs to be archived. |
| `gen_cheat_sheet.sh` | Shrinks font size and re-runs pandoc until a `.md` fits a target page count | Live capability; its procedure is documented only in root `note.md` (§ 3) |
| `latex_to_pdf.sh` | Unzips `Resume___CV.zip` and compiles it to `static/pdfs/` | **Not coursework.** Name collides with `docs/latex/build_tex.sh` and `content/cesc_410/hw/tools/build_tex.sh`, which *are* the coursework builders. Rename or archive. |
| `chunker_1MB.py` | Splits a large `.md` into ~1 MB chunks for upload limits | |
| `get_yt_transcripts.py` | Selenium scraper against `youtubetotranscript.com` | External-service dependent; likely already stale |
| `merge_playlist_transcripts.py` | Merges per-video transcripts into one file | |

**Recommend:** a `docs/runbooks/scripts.md` describing all six, or archive the dead ones. Neither was done
— deciding which are dead is an operator call ([question-discipline](./directives/question-discipline.md)).

---

## 6 — Directives: none existed  ·  **fixed this pass**

`docs/directives/` was empty except for `coursework-solutions.md`, written today by another writer.
Five project-local directives were back-filled, distilled from `~/llm-project-bootstrap/directives/` and
phrased for *this* repo:

| File | The rule it exists to prevent breaking |
| --- | --- |
| [scope-discipline.md](./directives/scope-discipline.md) | A consistency pass over the twelve frozen courses |
| [documentation-discipline.md](./directives/documentation-discipline.md) | Durable knowledge landing in a root `tmp*.md` again |
| [testing-discipline.md](./directives/testing-discipline.md) | Building a root unit-test suite that protects nothing |
| [roadmap-and-plans.md](./directives/roadmap-and-plans.md) | A roadmap that tracks assignment due dates |
| [question-discipline.md](./directives/question-discipline.md) | Guessing a publish/retrofit/move call, or running git |

Seven hub directives were **deliberately not distilled** — `code-discipline` (no root application code;
`ocr_handler` has its own), `automation-first`, `wiki`, `plan-first`, `map-before-act`,
`knowledge-retrieval`, `honest-instrumentation`, `research-docs`. Listed in
[directives/INDEX.md](./directives/INDEX.md); add one when it starts costing something.

---

## 7 — The published site indexes 3 of 15 courses

[`content/_index.md`](../content/_index.md) — the site's landing page — links **`ee_300`, `ee_302` and
`cs_420` only**, and only `content/ee_300/` has an `_index.md` (plus two under `ee_300/exam1/` and
`exam2/`). The other **fourteen course folders have no `_index.md`**, so twelve courses are effectively
unnavigable on the published site even though their files are pushed to it.

Two readings, and they demand opposite actions:

- **Stale landing page** → add cards and `_index.md` files. But that would *newly surface* worked
  solutions on a public site, which is [scope.md](./scope.md) § Open questions #1.
- **Deliberate** → then `hugo.yaml`'s `ignoreFiles` should say so, because "not linked" is not "not
  published": the pages are still built and still reachable by URL and by search engines.

**Nothing was changed.** Answering #1 answers this. → [scope.md](./scope.md) § Open questions #3.

---

## 8 — Git working tree: 48 uncommitted paths

Reported, not acted on — **git is human-only**. `git status --porcelain | wc -l` → **49** at 16:26
(17 modified, 32 untracked; the number moves as other writers work).

- Modified — `ocr_handler/docs/*` and two `ocr_handler/src/` modules, plus `content/cesc_410/tmp.md`
- Untracked — including the whole of `docs/`, the whole of `docs-rag/` (**417 files, 0 tracked**),
  `content/cesc_470/hw/`, `content/cesc_410/hw/`, `content/cpsc_462/md_notes/` and `content/cpsc_462/hw/`,
  and 15 new `ocr_handler/docs/` files
- `ocr_handler/src/ocr_handler/textlayer.py` is **untracked** — the module the shipped CLI depends on
  exists on disk only, and `ocr_handler/docs/todo.md` already flags it

Everything this pass produced is new and additive; no commit is proposed here, per
[SESSION_CONDUCT](file:///home/devel/llm-project-bootstrap/guides/SESSION_CONDUCT.md) § Git — commits are
milestone-gated and the operator's alone.

---

## 9 — `docs-rag/` is a child project with no bootstrap and no git

[`docs-rag/`](../docs-rag/) is 417 files: a Docker-composed retrieval deployment with one knowledge base
per course, a 12 KB `rag` CLI dispatcher, a stdlib-only query client, ops scripts, port-forward tunnels,
and a `corpus/` already populated for seven courses (stat_412 203 docs, cec_315 56, ps160 53, cec_320 28,
cesc_410 11, ae318 3, cec_300 1). It carries [`README.md`](../docs-rag/README.md),
[`RUN.md`](../docs-rag/RUN.md), [`FINDINGS.md`](../docs-rag/FINDINGS.md) and
`agent_hints/HOW_TO_QUERY.md`.

It has **no `docs/` taxonomy** and is **entirely untracked in git** (§ 8). Its `FINDINGS.md` F-01 (§ 4)
is a repo-wide fact currently readable only from inside an untracked folder.

**Recommend:** run `## Bootstrap Existing` on it as its own child project — the same treatment
`ocr_handler/` already has. Not done here: it is a separate project and outside this pass's write zone.
→ [scope.md](./scope.md) § Open questions #5.

---

## 10 — Smaller items, recorded so they are not rediscovered

- **`ocr_handler/docs/` is current and needs nothing.** It is the in-repo reference for what these
  standards look like: 11 folders, all indexed, five ADRs, a corpus census, a research teardown, two
  runbooks, a `tests/persistent/` floor, and its own doctrine-compliance plan. This pass modelled the
  root `docs/` on it and on `~/sys301_minesweeper/docs/`.
- **Disk size is not repo size.** ~11,980 files on disk, **2,089 tracked**. The 5,287-file difference is one
  280 MB gitignored `.venv` at `content/cesc_410/labs_and_projects/dsp26/.venv/`, correctly excluded by a
  folder-scoped `.gitignore` with a comment explaining exactly that. The `.gitignore` hygiene in this
  repo is genuinely good — four folder-scoped files, each with negations preserving instructor source
  PDFs, each with a comment saying why.
- **`content/cesc_420/` is a documentation project living inside a course folder** — `INDEX.md`,
  `docs/00…06_*.md`, `docs/findings/F01…F10`. It is a frozen course, so it stays, but it is the closest
  thing in the repo to a second bootstrapped sub-project.
- **`content/cec_320/labs_and_projects/` is the ancestor** of the cesc_410 lab system (same instructor).
  Frozen, but it is where a `cesc_410` question is most likely to already be answered.
- **`ocr_handler/docs/session_records/` is empty while its one record sits in `archives/session_records/`.**
  That project's own INDEX flags the inconsistency and asks the operator to settle the convention. This
  root `docs/` follows the guide (live records in `session_records/`, rotate to `archives/`), which makes
  the two trees disagree. Worth settling once, for both.

---

## What this pass changed

**Created — all under `docs/`, all new files:**

```
docs/DRIFT_REPORT.md          this file
docs/README.md   scope.md   roadmap.md   todo.md
docs/directives/  INDEX.md + scope-discipline · documentation-discipline
                             testing-discipline · roadmap-and-plans · question-discipline
docs/{findings,research,lessons_learned,decisions,plans,features,runbooks,session_records}/INDEX.md
docs/archives/INDEX.md  +  archives/{session_records,plans,operator-notes}/INDEX.md
docs/session_records/2026-09-04_catch-up.md
```

**Not touched, by instruction:** `docs/directives/coursework-solutions.md` · `docs/latex/**` ·
`content/**` · `ocr_handler/**` · `docs-rag/**`.

**Deleted or moved:** nothing.

---

**See:** [scope.md](./scope.md) · [roadmap.md](./roadmap.md) · [todo.md](./todo.md) ·
[directives/INDEX.md](./directives/INDEX.md) ·
[session_records/2026-09-04_catch-up.md](./session_records/2026-09-04_catch-up.md)
