# docs/latex — shared LaTeX toolchain

The **one** preamble and the **one** build-checker used by every course under the
coursework doctrine. Nothing course-specific lives here.

| File | Purpose |
| --- | --- |
| [`coursework_preamble.tex`](coursework_preamble.tex) | Shared preamble — packages, `answerbox`, `trap`, `\srcref`, `\extref`, `\problemheader` / `\problemheaderlo`, `\coursename`, page style. **Preamble only**: no `\begin{document}`. |
| [`new_tex.sh`](new_tex.sh) | Scaffold a new problem file with the `\input` lines **computed**, not counted by hand. |
| [`build_tex.sh`](build_tex.sh) | Build-check one `.tex` or a whole assignment. Deletes the PDF unless `--keep`. |
| [`flatten_tex.sh`](flatten_tex.sh) | Inline the preamble to make a file **self-contained for Overleaf**. |

All take **repo-relative** paths and run from the repo root.

```sh
docs/latex/new_tex.sh content/cesc_470/hw/hw02 3 clock-rate --pts "15 pts"
docs/latex/build_tex.sh content/cesc_470/hw/hw01                    # whole assignment
docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep             # keep the PDFs
docs/latex/flatten_tex.sh content/cesc_470/hw/hw01                  # Overleaf copies
```

---

## ⚠ Overleaf cannot resolve the shared `\input` — flatten first

An Overleaf project is **self-contained**. A path climbing above the project
root cannot resolve there, so pasting a file straight in fails with exactly the
error a wrong depth gives locally:

```text
LaTeX Error: File `../../../../docs/latex/coursework_preamble.tex' not found.
```

Uploading the preamble by hand works but must be redone per project and
re-synced whenever the shared file changes. Instead:

```sh
docs/latex/flatten_tex.sh content/cesc_470/hw/hw01
#   -> content/cesc_470/hw/hw01/overleaf/*.tex   (gitignored, regenerable)
```

Each output file is standalone — paste or upload one, and it needs nothing else.
The script:

- recursively inlines `\input` / `\include`,
- **strips comment-only lines naming tooling** (script names, repo paths), because
  the doctrine forbids tooling references in a submitted document,
- drops the inlined preamble's comments wholesale — they are all about this
  repo's toolchain and mean nothing in Overleaf,
- **fails loudly if any `\input` survives**, rather than shipping a file that
  will break in Overleaf the same way the original did.

**Keep editing the source file, not the flattened copy.** Re-flatten after
changes; the `overleaf/` folder is generated output.

---

## Scaffolding a new file

The two `\input` lines are the only fiddly part, and both are easy to get wrong:
the number of `../` depends on nesting depth, and the macros file is named per
course. `new_tex.sh` derives both from the target path:

```sh
docs/latex/new_tex.sh content/cesc_470/hw/hw02 3 clock-rate --pts "15 pts"
docs/latex/new_tex.sh content/cesc_410/hw/hw02 1 phasors --pts "20 pts" --lo LO01
docs/latex/new_tex.sh content/cesc_470/hw/hw02 --solutions
```

It counts the depth rather than assuming four, and walks **up** the tree for
`reference_docs/*_macros.tex`, so an assignment nested deeper still resolves
(verified at five levels: `../../../../../docs/latex/…` with
`../../reference_docs/…`). It refuses to overwrite an existing file, and the
scaffolded file **builds immediately** — the skeleton is valid LaTeX with TODOs
in the prose.

Use `--lo` only for courses that state learning outcomes (CESC 410 does; CESC
470 does not).

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

| Course | Carries |
| --- | --- |
| CESC 410 | DSP notation, `\stemplot` |
| CESC 470 | performance-equation notation, `\amdahl` |
| CPSC 462 | delay notation, `\field` |

**One macros file per COURSE**, shared by `hw`, `qz` and `exam` — notation is a
property of the subject, not of the assignment kind. It belongs at
`content/<course>/reference_docs/<course>_macros.tex`.

> ⚠ **Never have two.** `new_tex.sh` resolves macros by walking **up** from the
> assignment folder and taking the first hit, so a nearer
> `content/<course>/hw/reference_docs/` silently shadows the course-level file —
> and `hw` and `qz` would compile against different macros with no error at all.
> Some courses still have theirs under `hw/` from before this rule; that is fine
> while the course has only homework, but must be moved up before a `qz/` or
> `exam/` folder is added. See the
> [directive](../directives/coursework-solutions.md#one-macros-file-per-course-not-per-kind).

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
