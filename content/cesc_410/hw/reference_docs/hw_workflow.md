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
\input{../../reference_docs/cesc410_macros.tex}             % CESC 410 only
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
It is the same script every course runs, so a fix to it lands everywhere.

PDFs are deleted by default and gitignored — they are build products.

### ⚠ Pointing it at `reference_docs/` reports two failures, by design

`build_tex.sh` builds **every** `.tex` in a folder, and two of the three files
in `reference_docs/` are **fragments, not documents**:

| File | Standalone build | Why |
| --- | --- | --- |
| `problem_template.tex` | ✅ OK | a real document — it is the skeleton you copy |
| `cesc410_macros.tex` | ❌ `Command \coursename undefined` | preamble fragment; `\renewcommand{\coursename}` needs the shared preamble loaded first, and there is no `\begin{document}` |
| `cesc410_preamble.tex` | ❌ `no legal \end found` | comment-only tombstone; superseded, do not `\input` it |

That is correct behaviour, not a bug to fix — a fragment without
`\begin{document}` **cannot** compile, and that is exactly what lets it be
`\input` by a file that has one. Build the template by name instead:

```sh
docs/latex/build_tex.sh content/cesc_410/hw/reference_docs/problem_template.tex
```

## Overleaf

**A source file cannot be pasted into Overleaf.** Its `\input` climbs above the
project root, which an Overleaf project cannot resolve — the compile dies with
`File '../../../../docs/latex/coursework_preamble.tex' not found`. Flatten to a
self-contained copy first:

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
#   -> content/cesc_410/hw/hw01/overleaf/*.tex   (gitignored, regenerable)
```

The flattened copy also has tooling-naming comments stripped, which is what the
no-tooling-references rule requires of anything submitted. **Edit the source, not
the copy.**

**Flattening successfully is not the same as the output compiling.** The script
only guarantees no `\input` survived; it does not build what it wrote. Check it:

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
cd content/cesc_410/hw/hw01/overleaf && for f in *.tex; do tectonic "$f"; done
```

Status: **all seven HW1 files flatten and compile standalone**, and so does
`reference_docs/problem_template.tex`.

Two caveats:

- The flattener stamps a two-line header into every output naming the **source
  path**. Harmless here — a LaTeX comment never reaches the PDF — but delete
  those lines if the `.tex` itself is what gets handed in.
- `overleaf/` is gitignored at any depth, so `hw01/overleaf/` and
  `reference_docs/overleaf/` are both covered by the one rule.

## Starting a new file

Do not hand-write the two `\input` lines — the `../` count depends on depth:

```sh
docs/latex/new_tex.sh content/cesc_410/hw/hw02 1 phasors --pts "20 pts" --lo LO01
docs/latex/new_tex.sh content/cesc_410/hw/hw02 --solutions
```

CESC 410 states learning outcomes, so use `--lo`; the scaffold then emits
`\problemheaderlo`.

## Quizzes and exams

The doctrine covers `hw`, `qz` and `exam` with **identical** structure — same
two-document rule, same five-section problem file, same `answerbox`. Nothing
exists for quizzes yet; when a `qz01` appears it goes at
`content/cesc_410/qz/qz01/` alongside `hw/`.

**There is one macros file for CESC 410 and it is shared across all three
kinds.** Do *not* create `qz/reference_docs/cesc410_macros.tex`: a second
`*_macros.tex` for one course is the drift the doctrine exists to prevent, and
`new_tex.sh` warns about it explicitly —

```text
WARNING: 2 macros files for course 'cesc_410':
         Doctrine is ONE per course.
         Two files means hw/ and qz/ can silently diverge.
```

A quiz file therefore reaches across to `hw/`:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}   % 4 up: qz/qz01 -> root
\input{../../reference_docs/cesc410_macros.tex}          % course level
\begin{document}
```

### ⚠ `new_tex.sh` cannot scaffold that line — copy the template instead

The scaffolder walks **up** from the target folder looking for
`*/reference_docs/*_macros.tex`, two levels deep at each step. From
`content/cesc_410/qz/qz01` that reaches `qz/reference_docs/` and
`content/cesc_410/reference_docs/`, but **not** `hw/reference_docs/` — a
sibling kind is three levels down from the common ancestor. It exits before
writing anything:

```text
error: no reference_docs/*_macros.tex found at or above content/cesc_410/qz/qz01.
```

So for a quiz or an exam, copy the template and correct the one line:

```sh
mkdir -p content/cesc_410/qz/qz01
cp content/cesc_410/hw/reference_docs/problem_template.tex \
   content/cesc_410/qz/qz01/p01_<slug>.tex
# the macros \input is ../../reference_docs/cesc410_macros.tex, same as hw
docs/latex/build_tex.sh   content/cesc_410/qz/qz01
docs/latex/flatten_tex.sh content/cesc_410/qz/qz01
```

**Verified end to end** on a throwaway `qz99/` (since deleted): a problem file
and a solutions document both built, both flattened, and both flattened copies
compiled standalone with the DSP macros correctly inlined.

`qz/` will also need its own `.gitignore`, or the `hw/` one copied — the
existing rules are scoped to `hw/` and do not reach a sibling folder.

> **Open question for the human.** The directive puts the macros file at
> `content/<course>/<kind>/reference_docs/`, and that is where CESC 410's is.
> `new_tex.sh` names `content/<course>/reference_docs/` instead. Moving it up
> one level would let the scaffolder serve `hw/`, `qz/` and `exam/` alike — but
> it is a layout change across three courses, and the shared docs point at the
> current path. Flagged, not decided.

---

**Related:** [`findings.md`](findings.md) · [`../prompt.md`](../prompt.md) · [`submission.md`](submission.md) · [`problem_template.tex`](problem_template.tex) · [`../hw01/README.md`](../hw01/README.md)
