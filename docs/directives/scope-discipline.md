# Scope Discipline

**WHEN** you are about to change a course folder → **DON'T** act until you know whether that course is
under the new doctrine → **BECAUSE** the operator has explicitly ruled that **older courses are not to be
retrofitted**, and a well-intentioned "consistency" pass over `content/stat_412/` or `content/cec_320/`
would be a scope violation, not a cleanup.

- **One file: [../scope.md](../scope.md).** It carries what this repo is, the in-scope list, and the
  mandatory Out-of-Scope blacklist tiered *permanent* / *not now* / *maybe later*. Read it before acting.
- **The doctrine boundary is the load-bearing rule.** The coursework-solutions workflow
  (`docs/latex/`, [coursework-solutions.md](./coursework-solutions.md)) applies to **`cesc_470`,
  `cesc_410`, `cpsc_462`, and courses started after them** — nothing else. The other twelve course
  folders are frozen as-is. Retrofitting one requires the operator to say so, in the current session.
- **Child projects own their own scope.** `ocr_handler/` and `docs-rag/` each have their own
  `docs/` (or `README.md`+`FINDINGS.md`) tree and their own boundaries. This repo's `docs/scope.md`
  does not govern their internals; do not write into their trees from a root-level session.
- **Course content is the operator's coursework, not a codebase to refactor.** Notes, solutions and
  lab reports are graded artifacts. Reorganising them for tidiness changes what gets submitted.
  Structure changes to a course folder are an operator decision.
- **Per-course workflows already exist and are the local authority.** `content/cesc_410/hw/prompt.md`
  and `content/cesc_410/labs_and_projects/{prompt.md,README.md,reference_docs/}` are the contract for
  those two folders. Where they disagree with a root directive, the per-course doc wins **for that
  folder**, and the disagreement gets written into `docs/findings/` rather than silently resolved.
- **Publishing is a scope fact, not an implementation detail.** Everything under `content/` is pushed
  to a **public** GitHub Pages site (`.github/workflows/pages.yml` → `hugo --minify` → the `published`
  branch of `erauredeyesociety/electrical_notes`). "Add a file to `content/`" means "publish it".
- **Uncertain about the operator's intent → write it into [../scope.md](../scope.md) § Open questions**,
  don't invent an answer.

Hub: `~/llm-project-bootstrap/directives/scope-discipline.md` → guide `PROJECT_SETUP.md`
