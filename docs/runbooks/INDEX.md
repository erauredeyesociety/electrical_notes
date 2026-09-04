# Runbooks — INDEX

Repeatable operator procedures. Written to be **followed**, not read — step, then how to verify the step
worked. Assume the reader does not know the system.

**EMPTY as a folder.** Three procedures exist and are executable today; two of them are documented only
in a loose root file, which is why filing them is [../roadmap.md](../roadmap.md) § M3.

| Procedure | Where it is today | Should be |
| --- | --- | --- |
| **Build-check a `.tex`** — `docs/latex/build_tex.sh content/<course>/<kind>NN` for a whole assignment, or one file, `--keep` to retain the PDFs | Documented in the script's own header ([`../latex/build_tex.sh`](../latex/build_tex.sh)) and in [../directives/coursework-solutions.md](../directives/coursework-solutions.md) | Fine where it is |
| **Bootstrap / rebuild the Hugo site** — the `hugo mod init` / `hugo mod get` sequence, mounting layouts and static, enabling maths in `hugo.yaml` | [`note.md`](../../note.md) in the repository root, mixed with a stale `tree` listing | `runbooks/hugo-site.md` |
| **Turn a Markdown note into a printable cheat sheet** — the pandoc + xelatex incantation, plus the caveat that pandoc will not execute a Vega `<script>` chart (export a PNG/SVG and embed it) | [`note.md`](../../note.md), root. The automated form is `scripts/gen_cheat_sheet.sh`, which shrinks the font until the document fits a page count — **and is referenced from nowhere** | `runbooks/cheat-sheet-pdf.md` |
| **Generate a study guide from a topic** — a course-agnostic prompt template | [`make_study_guide_master_prompt.md`](../../make_study_guide_master_prompt.md), root | `runbooks/make-study-guide.md` |
| **The other five `scripts/`** | Undocumented anywhere. One of them rewrites every `.md` in the repo in place. | `runbooks/scripts.md`, or archived — [../DRIFT_REPORT.md](../DRIFT_REPORT.md) § 5 |

Nothing was moved: files under version control are moved by the operator
([../directives/question-discipline.md](../directives/question-discipline.md)).

**Child-project runbooks:** [`ocr_handler/docs/runbooks/INDEX.md`](../../ocr_handler/docs/runbooks/INDEX.md)
— extracting course text, and the ROS 2 `PYTHONPATH` gotcha that breaks pytest collection on this machine.
`docs-rag/RUN.md` covers bringing the retrieval stack up.
