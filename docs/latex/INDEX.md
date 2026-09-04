# docs/latex — shared LaTeX toolchain

The **one** preamble and the **one** build-checker used by every course under the
coursework doctrine. Nothing course-specific lives here.

| File | Purpose |
| --- | --- |
| [`coursework_preamble.tex`](coursework_preamble.tex) | Shared preamble — packages, `answerbox`, `trap`, `\srcref`, `\extref`, `\problemheader` / `\problemheaderlo`, `\coursename`, page style. **Preamble only**: no `\begin{document}`. |
| [`build_tex.sh`](build_tex.sh) | Build-check one `.tex` or a whole assignment. Takes **repo-relative** paths. Deletes the PDF unless `--keep`. |

```sh
docs/latex/build_tex.sh content/cesc_470/hw/hw01                    # whole assignment
docs/latex/build_tex.sh content/cesc_470/hw/hw01/p08_target_clock_rate.tex
docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep             # keep the PDFs
```

---

## The split, and why it exists

A per-problem file inputs **two** fragments, in this order:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}   % shared — every course
\input{../reference_docs/<course>_macros.tex}            % this course only
\begin{document}
```

Four `../` reaches the repo root from `content/<course>/<kind>/<kind>NN/`.

| | Belongs in the shared preamble | Belongs in a course macros file |
| --- | --- | --- |
| Test | *Would another course want this?* | *Does this mean anything outside this subject?* |
| Examples | `answerbox`, `\srcref`, page style, packages | `\conv`, `\ustep`, `\stemplot` (DSP); `\dnodal`, `\dprop` (networks); `\CPI`, `\clockrate` (architecture) |

**Adding shared setup to a course file is how three preambles drift apart.** The
CESC 410 preamble was originally standalone and duplicated ~60 lines of this
file before being split on 2026-09-04.

### Current course macros files

| Course | File | Carries |
| --- | --- | --- |
| CESC 410 | [`../../content/cesc_410/hw/reference_docs/cesc410_macros.tex`](../../content/cesc_410/hw/reference_docs/cesc410_macros.tex) | DSP notation, `\stemplot` |
| CESC 470 | [`../../content/cesc_470/hw/reference_docs/cesc470_macros.tex`](../../content/cesc_470/hw/reference_docs/cesc470_macros.tex) | performance-equation notation, `\amdahl` |
| CPSC 462 | [`../../content/cpsc_462/hw/reference_docs/cpsc462_macros.tex`](../../content/cpsc_462/hw/reference_docs/cpsc462_macros.tex) | delay notation, `\field` |

---

## Two traps this toolchain has already hit

**`\problemheader` takes three arguments; `\problemheaderlo` takes four.** The
four-argument form carries a learning outcome, which CESC 410 states and CESC
470 does not. Calling the three-argument form with four arguments fails at build
time — loudly, which is the intent.

**A build that succeeds is not a document that is correct.** `build_tex.sh`
returning `OK` says nothing about layout. It did not catch a y-label drawn
through the tallest stem, or `\angle -75°` rendering as a subtraction with
binary-minus spacing. **Render to PNG and look**, at least once per new visual
element:

```python
import pymupdf
d = pymupdf.open("content/cesc_470/hw/hw01/p08_target_clock_rate.pdf")
d[0].get_pixmap(dpi=110).save("/tmp/p.png")
```

---

## Requirements

`tectonic` — self-contained, fetches its own packages on first run. Already
installed on this host. `build_tex.sh` exits 1 with a clear message if it is
absent.

---

**Governed by:** [`../directives/coursework-solutions.md`](../directives/coursework-solutions.md)
