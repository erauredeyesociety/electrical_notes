# Homework workflow

## Two documents, different jobs

The single rule that shapes everything:

| | `pNN_<slug>.tex` | `hwNN_solutions.tex` |
| --- | --- | --- |
| One per | problem | assignment |
| Contains | **every step** | **answers only** |
| For | learning the method | checking the result |
| Built | standalone | once, at the end |

Mixing them ruins both. A solutions document with derivations is unusable for checking; a problem file without them is unusable for learning.

## Why one file per problem

- **It build-checks alone.** A LaTeX error is located at the problem, not somewhere in a 12-problem document.
- **Problems are independent.** They can be written, revised, and reviewed without touching each other.
- **The assignment can be partially done** without a broken document.

Each file inputs two preamble fragments — neither has a `\begin{document}`, which is what lets a fragment be a complete document:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}   % shared, every course
\input{../reference_docs/cesc410_macros.tex}             % CESC 410 only
\begin{document}
```

The shared half carries the document class, the packages, `\answerbox`, the
`trap` callout, `\srcref` / `\extref`, `\problemheader` / `\problemheaderlo`
and the page style. The CESC 410 half carries `\coursename`, the DSP notation
and `\stemplot` — things that mean nothing outside a signals course. Four `..`
levels reach the repo root from `content/<course>/hw/hwNN/`.

## Naming

```text
hw01/
├── dsphw26-hw1.pdf              the assignment
├── README.md                    tracking: problems, LOs, points, status
├── p01_phasor_form.tex          one per problem
├── p02_phasor_arithmetic.tex
├── ...
└── hw01_solutions.tex           condensed answers
```

`pNN` is a **continuous internal index**, not necessarily the handout's label. HW1 numbers two different problems "Prob 1"; the file names run p01–p06 and each file states the handout's own label in its header.

## Grounding work in the course

```sh
tools/course_text.py --grep "convolution"
tools/course_text.py --list
tools/course_text.py --dump /tmp/coursetext
```

Searches lectures, labs, and handouts in one command. **21 of 25 documents have a usable text layer; 4 do not** — the handwritten lecture PDFs, flagged `NO-TEXT`.

> Not being able to search a document is not permission to guess what it says. Read the PDF, or use `ocr_handler`, or state the gap in the problem file.

## Notation

Use the existing macros so every problem writes the same symbols:

| Macro | From | For |
| --- | --- | --- |
| `\answerbox` | shared | final answer — what the solutions document lifts |
| `\problemheaderlo{n}{LO}{pts}{title}` | shared | problem header; CESC 410 states an LO, so use the 4-arg `lo` form |
| `\problemheader{n}{pts}{title}` | shared | 3-arg form, for courses with no LO |
| `\srcref{...}` `\extref{...}` | shared | cite the slide a step came from / mark an outside step |
| `trap` environment | shared | callout for the trap in a problem |
| `\stemplot{xmin}{xmax}{coords}` | cesc410 | DT stem plot in the lecture's format |
| `\phasor{mag}{angle}` | cesc410 | phasor notation |
| `\conv` `\ustep` `\Real` `\Imag` `\dtft` `\ztr` `\sinc` | cesc410 | DSP notation |

Add a macro rather than redefining notation in one file — DSP notation to
`cesc410_macros.tex`, anything another course would also want to
`docs/latex/coursework_preamble.tex`.

## Building

The shared build-checker takes **repo-relative** paths and is run from the repo root:

```sh
docs/latex/build_tex.sh content/cesc_410/hw/hw01/p01_phasor_form.tex   # one
docs/latex/build_tex.sh content/cesc_410/hw/hw01                        # all
docs/latex/build_tex.sh content/cesc_410/hw/hw01 --keep                 # keep PDFs
```

`tools/build_tex.sh` still works for this folder and takes paths relative to
`content/cesc_410/hw/`, but `docs/latex/build_tex.sh` is the shared one — prefer it.

PDFs are deleted by default and gitignored — they are build products.

---

**Related:** [`findings.md`](findings.md) · [`../prompt.md`](../prompt.md) · [`submission.md`](submission.md) · [`problem_template.tex`](problem_template.tex)
