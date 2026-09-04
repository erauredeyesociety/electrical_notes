# Scope

> **Status: first pass, 2026-09-04.** This repo had never been bootstrapped; `docs/` was created empty
> and this file is the first boundary contract it has had. Everything here is derived from what is on
> disk plus the operator's stated rulings — where neither settles a question it is named in
> § Open questions rather than invented.
> Rules that govern work here: [directives/INDEX.md](./directives/INDEX.md)

**Kind:** Coursework corpus + publishing pipeline. The deliverable is **documents** — notes, worked
solutions, lab reports — not an application. Two child projects inside it *are* implementation projects
and are scoped separately.

---

## Overview

`electrical_notes` holds one university student's coursework for **15 courses** and publishes it as a
static site.

| | |
| --- | --- |
| Site | <https://erauredeyesociety.github.io/electrical_notes/> — **public** |
| Generator | Hugo + the [hextra](https://github.com/imfing/hextra) theme, pulled as a Hugo module ([`hugo.yaml`](../hugo.yaml)) |
| Maths | KaTeX, with `$…$` / `$$…$$` passthrough enabled |
| Deploy | [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) — every push to `main` runs `hugo --minify` and publishes to the `published` branch |
| Size | **2,089 git-tracked files.** ~11,980 exist on disk; the difference is almost entirely one 280 MB gitignored `.venv` (5,287 files) under `content/cesc_410/labs_and_projects/dsp26/` |

Everything under `content/` is on a public website. **"Add a file to `content/`" means "publish it."**

### The 15 course folders

| Under the new coursework doctrine | Frozen as-is |
| --- | --- |
| `cesc_470` · `cesc_410` · `cpsc_462` | `ae318` · `cec_300` · `cec_315` · `cec_320` · `cesc_420` · `cs_420` · `ee_300` · `ee_302` · `ps160` · `stat_412` · `sys_304` · `syse_301` |

Plus every course started after 2026-09-04. The boundary is stated authoritatively in
[directives/coursework-solutions.md](./directives/coursework-solutions.md) and is repeated here because
it is the single rule most likely to be violated by a well-meaning consistency pass.

---

## Objectives

- **O1 — A durable, searchable record of the coursework.** Notes survive the semester and stay greppable.
- **O2 — Worked solutions that teach the method**, per
  [directives/coursework-solutions.md](./directives/coursework-solutions.md): derivations in per-problem
  `.tex`, final answers in a condensed solutions document, every non-obvious step cited to the course
  material.
- **O3 — One shared LaTeX toolchain**, not one per course — [`docs/latex/`](./latex/).
- **O4 — Reproducible artifacts.** PDFs, figures and zips are build products, rebuilt from tracked
  sources. Git holds the source, not the output.
- **O5 — The published site keeps working.** A push that breaks `hugo --minify` breaks a public site.

---

## In scope

1. **Course notes** — Markdown under `content/<course>/`, rendered by Hugo.
2. **Worked solutions** for homework, quizzes and exams, under the two-document rule, for the doctrine
   courses only.
3. **Lab reports and lab automation**, where a course has labs — today only
   `content/cesc_410/labs_and_projects/`, which carries its own workflow
   ([`README.md`](../content/cesc_410/labs_and_projects/README.md),
   [`reference_docs/`](../content/cesc_410/labs_and_projects/reference_docs/),
   [`tools/`](../content/cesc_410/labs_and_projects/tools/)).
4. **The shared LaTeX toolchain** — [`docs/latex/coursework_preamble.tex`](./latex/coursework_preamble.tex)
   and [`docs/latex/build_tex.sh`](./latex/build_tex.sh). Course-specific notation stays in a per-course
   `reference_docs/<course>_macros.tex`.
5. **Course-material extraction** — turning instructor PDFs, `.pptx` and `.docx` into Markdown notes.
   Centralising this is [`ocr_handler`](../ocr_handler/docs/scope.md)'s job.
6. **The Hugo site** — configuration, navigation, and keeping the build green.
7. **This `docs/` tree** — the repo's own governance, findings and history.

---

## Out of scope — the blacklist

Deliberate exclusions. Re-opening a **permanent** row requires an ADR in
[decisions/](./decisions/INDEX.md), not a commit message.

| Excluded | Tier | Why |
| --- | --- | --- |
| **Retrofitting the twelve frozen courses** to the new doctrine | **permanent** | Explicit operator ruling. Re-doing settled coursework is wasted effort, and those folders are already submitted. Consistency is not a reason. |
| **Moving or deleting anything under `content/`** without the operator asking | **permanent** | Paths are referenced from submission scripts, per-course READMEs and the Hugo site. Report where a file should go; do not move it. |
| **Git mutations by an agent** | **permanent** | `add` / `commit` / `push` / `checkout` / `reset` are proposed as commands, never run. `.gitignore` may be edited. |
| **Committing build products** — rendered PDFs, generated figures, zips, `.venv`, `__pycache__` | **permanent** | Regenerable and large. `.gitignore` files at `content/cesc_410/hw/`, `content/cesc_410/labs_and_projects/` and `content/cpsc_462/md_notes/` encode this, each with the negation that keeps the instructor's source PDFs. |
| **Tooling references inside a submitted document** | **permanent** | Script names, flags and repo paths must not appear in anything handed in — [coursework-solutions.md](./directives/coursework-solutions.md) § Repo hygiene. |
| **Transcribing an equation from a PDF text layer** | **permanent** | Measured failure: `pdftotext` turned $\cos(\tfrac{\pi}{6}n)$ into `cos( 6π n)` and silently dropped a radical. Render the region and look at it. |
| **A per-course PDF extractor** | permanent | Three already diverged. One extractor: [`ocr_handler`](../ocr_handler/docs/scope.md). |
| **A per-course LaTeX preamble** | permanent | Shared setup duplicated per course is how three preambles drift apart. Course files hold *notation only*. |
| **A root-level unit-test suite** | not now | The root repo ships no application code. The floor is three build checks — [testing-discipline.md](./directives/testing-discipline.md). |
| **Rewriting git history to shrink the repo** | not now | Raised by the operator in `tmp.md`. It is destructive, it invalidates every existing clone, and nothing currently depends on it. Needs its own decision. |
| **A search index, database, or custom web viewer** | maybe later | Hugo's built-in search covers it. `docs-rag/` already exists for retrieval and is a separate project. |
| **Anything inside `ocr_handler/` or `docs-rag/`** | n/a | Child projects. They have their own scope; a root session does not write into them. |

### Distractions to name explicitly

Attractive mid-session, and not the job:

- **Tidying the twelve frozen course folders.** The single most likely scope violation in this repo.
- **Generalising a per-course workflow before a second course needs it.** `cesc_410`'s lab tooling exists
  because `cesc_410` has labs. No other course does yet.
- **Perfecting the Hugo site's appearance.** It is a notes site. Green build, readable maths, done.
- **Documenting a workflow that is still being invented.** During active development: findings, ADRs and
  session records only.
- **Making `docs/` mirror the coursework.** This tree governs the *repo*. Assignment tracking lives in the
  assignment's own `README.md`.

---

## Child projects — separately scoped

Neither is governed by this file. Both are reached by path, never restated.

| Project | What it is | Its scope |
| --- | --- | --- |
| [`ocr_handler/`](../ocr_handler/) | The one text extractor for every course. Python 3.12 + `uv` + PyMuPDF; classifies each PDF page and extracts the text layer before spending anything on recognition. Fully bootstrapped, with its own ADRs, findings, runbooks and a `tests/persistent/` floor. | [`ocr_handler/docs/scope.md`](../ocr_handler/docs/scope.md) |
| [`docs-rag/`](../docs-rag/) | A retrieval deployment over the documentation corpus. Docker-composed, with its own `README.md`, `RUN.md` and `FINDINGS.md`. **Not bootstrapped to the standard `docs/` taxonomy** — see [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 2. | `docs-rag/README.md` |

---

## Constraints

| | |
| --- | --- |
| Publication | Everything in `content/` is public. There is no private area. |
| Build | Hugo extended + the hextra module. CI uses `hugo-version: latest` — **unpinned**, so an upstream release can break the site without a local change. |
| LaTeX | `tectonic`, invoked by [`docs/latex/build_tex.sh`](./latex/build_tex.sh). PDFs are deleted after the build check unless `--keep`. |
| Python | `uv`. The system `PYTHONPATH` carries ROS 2, whose pytest plugins break collection — run as `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH= uv run pytest`. |
| Academic integrity | Worked solutions are published on a public site under the operator's institution's org. **Settled: not a concern** — [decision 0001](./decisions/0001-publishing-and-git-are-not-a-concern.md). Do not re-raise. |
| Git | **Human-only.** Agents propose commands; the operator runs them. |

---

## Success

**S1 — the site builds and publishes.** A push to `main` completes `hugo --minify` and updates the
published branch. *Currently unverified from this repo: no local build check is scripted.*

**S2 — a doctrine assignment is reproducible from source.** `docs/latex/build_tex.sh content/<course>/<kind>NN`
builds every problem file and the solutions document from tracked `.tex` alone, with no PDF in git.
*Met for `content/cesc_410/hw/hw01` (six problem files + a solutions document, all `.tex` tracked, PDFs
gitignored).*

**S3 — a new session can orient from `docs/` without reading the whole repo.** This file,
[roadmap.md](./roadmap.md), [todo.md](./todo.md) and [directives/INDEX.md](./directives/INDEX.md) answer
"what is this, what is the rule, what is next" in four files. *Met as of this pass; untested by a real
session.*

---

## Open questions — operator input needed

Named rather than invented. Each blocks or re-shapes something concrete.

1. ~~**Should worked solutions be published publicly at all?**~~ — **CLOSED.** Settled by the
   operator on 2026-09-01 and re-affirmed 2026-09-04: publishing and the git remote are **not a
   concern** for coursework under `content/`. Do not re-raise.
   See [decisions/0001-publishing-and-git-are-not-a-concern.md](./decisions/0001-publishing-and-git-are-not-a-concern.md).

2. **Where do the four loose root `.md` files go?** `tmp.md`, `tmp_ocr_child.md`, `note.md` and
   `make_study_guide_master_prompt.md`. Recommendations with reasons are in
   [DRIFT_REPORT.md](./DRIFT_REPORT.md) § 3. **Nothing was moved** — the operator moves files under
   version control.
3. **Does the site index all 15 courses, or 3 on purpose?** [`content/_index.md`](../content/_index.md)
   links `ee_300`, `ee_302` and `cs_420` only, and only `content/ee_300/` has an `_index.md`. Twelve
   course folders are effectively unnavigable on the published site. Is that a deliberate privacy
   position or a stale landing page?
4. **Should `hugo-version` in CI be pinned?** It is `latest` today, so the public site can break with no
   local change. **Recommend: pin it**, and bump deliberately.
5. **Does `docs-rag/` become a bootstrapped child project, stay as-is, or move out of this repo?** It is
   untracked in git today — 417 files, none tracked.
6. **Is `ocr_handler` staying inside this repo?** Its own scope carries this as an open decision — its
   tests reach into `../content/` for fixtures, and this parent repo is large. Answering it here settles
   it in one place.

---

**See:** [README.md](./README.md) · [roadmap.md](./roadmap.md) · [todo.md](./todo.md) · [DRIFT_REPORT.md](./DRIFT_REPORT.md) · [directives/INDEX.md](./directives/INDEX.md)
