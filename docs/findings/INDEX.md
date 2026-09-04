# Findings — INDEX

**INTERNAL** discoveries about *this* repository — its layout, its build, its own scripts, its Hugo
configuration. External teardowns of other people's tools go in [../research/INDEX.md](../research/INDEX.md).

**EMPTY as a folder — but the repo is not without findings.** They exist, written well, in five
in-tree conventions that predate this `docs/` tree. **None of them should move**: course-local material
ships with the coursework it serves. They are cited here so a session starting at `docs/` can find them.

| Where it lives | What it holds | Course status |
| --- | --- | --- |
| [`content/cesc_410/hw/reference_docs/findings.md`](../../content/cesc_410/hw/reference_docs/findings.md) | HW-01…HW-07, ordered by damage. **HW-01: `pdftotext` silently corrupts fractions** — $\cos(\tfrac{\pi}{6}n)$ became `cos( 6π n)`, a constant signal, and a stray $\sqrt{\ }$ landed on the wrong line. HW-02: the handout labels two different problems "Prob 1". HW-03: `\angle` makes a following minus sign binary. HW-06: `axis lines=middle` draws the y-label through the data. | doctrine |
| [`content/cesc_410/labs_and_projects/reference_docs/known_issues.md`](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md) | **KI-01…KI-09** — repeated `plt.figure(N)` overplots · `plt.show()` no-ops headless · `myID` is a per-student seed · `uv` is not in the package manager · ImageMagick renders matplotlib SVG blank · setting the ERAU ID may not change the figures · `splitlines()`/`tokenize` desync corrupted stripped output · stripping docstrings removes Typer `--help` · **KI-09 tooling references leaked into a submitted report** | doctrine |
| [`docs-rag/FINDINGS.md`](../../docs-rag/FINDINGS.md) | **F-01 is repo-wide:** the ingester has no `.tex` handler and **fails silently** — warns, indexes zero files, reports success. The pandoc workaround must use `-f latex+raw_tex`; plain `-f latex` discards custom-macro content, which is exactly where the answers are (`\finalanswer` in stat_412, `answerbox` in cesc_410). | child project |
| [`ocr_handler/docs/findings/INDEX.md`](../../ocr_handler/docs/findings/INDEX.md) | The corpus census — **430 PDFs / 7,146 pages** measured across `content/`. 67% of pages and 50% of documents need no OCR; 51 documents carry a *corrupt* text layer; only 2 documents in the repo are ink-annotated. | child project |
| [`content/cec_320/labs_and_projects/`](../../content/cec_320/labs_and_projects/) — `known_issues.md`, `findings/`, `SYSTEM_ANALYSIS.md` | The ancestor of the cesc_410 lab system, same instructor. Where a cesc_410 question is most likely already answered. | **frozen** |
| [`content/stat_412/findings.md`](../../content/stat_412/findings.md) · [`content/cesc_420/docs/findings/`](../../content/cesc_420/docs/) · 8 loose `*_tips.md` at `content/cec_315/` | Course-level findings predating any convention | **frozen** |

> **Frozen** means the operator has ruled the course out of bounds — read it, cite it, never edit it
> ([../scope.md](../scope.md) § blacklist).

## What belongs *here* rather than in a course folder

A finding about the **repo**: the Hugo build, `.gitignore` behaviour, CI, the shared LaTeX toolchain, the
`scripts/` folder, or something true across several courses. First candidates are recorded in
[../DRIFT_REPORT.md](../DRIFT_REPORT.md) and should graduate into named files here when one is
investigated properly rather than merely observed.
