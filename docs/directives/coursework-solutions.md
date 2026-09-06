# Directive — worked solutions for homework, quizzes, and exams

**Applies to:** `cesc_470`, `cesc_410`, `cpsc_462`, **and every course added from
2026-09-04 onward.**

**Does NOT apply to:** `cec_320`, `cec_315`, `stat_412`, `ps160`, `cec_300`,
`ee_300`, `ee_302`, `sys_304`, `syse_301`, `ae318`, `cesc_420`, `cs_420`.
Those predate this directive and are **not** to be retrofitted — that was an
explicit operator decision, and re-doing settled coursework is wasted effort.
Leave them exactly as they are.

---

## The two-document rule

This is the whole shape of the work, and it is not negotiable.

| | Per-problem files | Solutions document |
| --- | --- | --- |
| Path | `<kind>NN/pNN_<slug>.tex` — **one per problem** | `<kind>NN/<kind>NN_solutions.tex` |
| Working | ✅ **every step, shown** | ❌ **final answers only** |
| Audience | someone learning the method | someone checking the result |
| Length | as long as it takes | as short as possible |

**Derivations live in the per-problem files. The solutions document is the
condensed version.** Do not put working in the solutions document; do not omit
it from the problem files. The solutions document is *assembled by lifting the
`answerbox` from each partial* — that is why every problem file ends with one.

`<kind>` is `hw`, `qz`, or `exam`. The rule is identical for all three.

### Why one file per problem

- A broken problem is found **where it broke** — `build_tex.sh` names the file.
- The assignment can be **partially done** without a broken document.
- Problems can be written in any order, and by parallel agents.

---

## Every file is standalone

A per-problem file inputs the shared preamble, then the course macros, then
opens the document:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}
\input{../../reference_docs/<course>_macros.tex}

\begin{document}
```

Four `../` reaches the repo root from `content/<course>/<kind>/<kind>NN/`; two
reach the course root, where the macros live (see below).

**Do not count those `../` by hand — scaffold with `new_tex.sh`**, which derives
both paths from the target folder.

| File | Holds | Rule |
| --- | --- | --- |
| [`docs/latex/coursework_preamble.tex`](../latex/coursework_preamble.tex) | packages, `answerbox`, `trap`, `\srcref`, `\extref`, `\problemheader`, page style | **shared by every course** |
| `content/<course>/reference_docs/<course>_macros.tex` | only course-specific notation | **one per course**, shared by `hw`, `qz` and `exam` |

**If another course would want a macro, it belongs in the shared preamble.**
Duplicating shared setup per course is how three preambles drift apart.

### One macros file per COURSE, not per kind

Notation is a property of the subject, not of the assignment kind: `\conv` means
the same thing on a homework, a quiz, and an exam. So the macros file lives at
**course level** and all three kinds reference it.

```text
content/<course>/
├── reference_docs/<course>_macros.tex     ← ONE, shared by all kinds
├── hw/hw01/pNN_*.tex                      → ../../reference_docs/<course>_macros.tex
├── qz/qz01/pNN_*.tex                      → ../../reference_docs/<course>_macros.tex
└── exam/exam01/pNN_*.tex                  → ../../reference_docs/<course>_macros.tex
```

> ⚠ **Macros under `hw/` are UNREACHABLE from a sibling kind — a quiz cannot be
> scaffolded at all.** This is a hard blocker, not untidiness.
>
> `new_tex.sh` walks up from the assignment folder running
> `find <probe> -maxdepth 2 -path '*/reference_docs/*_macros.tex'`. From
> `qz/qz01` the walk reaches the course root, where `hw/reference_docs/…` sits
> **three** levels down — past `-maxdepth 2`. The scaffolder exits with
> *"no reference_docs/\*_macros.tex found"* and writes nothing. Verified.
>
> At course level the file is two levels down, inside the limit, and all three
> kinds resolve `../../reference_docs/<course>_macros.tex`.
>
> **Two copies is worse than one in the wrong place.** The walk takes the
> *nearest*, so `hw/` and `qz/` would compile against different notation with no
> error anywhere. `new_tex.sh` warns if it finds more than one.
>
> Courses that predate this rule may still have macros under `hw/`. That is
> tolerable while a course has only homework; it **must** be moved up before a
> `qz/` or `exam/` folder is added.

### Don't write those two lines by hand

The `../` count depends on nesting depth and the macros file is named per
course. **Scaffold instead** — it computes both from the target path, and the
result builds immediately:

```sh
docs/latex/new_tex.sh content/cesc_470/hw/hw02 3 clock-rate --pts "15 pts"
docs/latex/new_tex.sh content/cesc_410/hw/hw02 1 phasors --pts "20 pts" --lo LO01
docs/latex/new_tex.sh content/cesc_470/hw/hw02 --solutions
```

`--lo` only for courses that state learning outcomes (CESC 410 does; CESC 470
does not).

### Build-check

```sh
docs/latex/build_tex.sh content/cesc_470/hw/hw01                # whole assignment
docs/latex/build_tex.sh content/cesc_470/hw/hw01/p08_clock.tex  # one problem
docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep         # keep the PDFs
```

---

## ⚠ Overleaf needs a flattened copy — never paste the source

An Overleaf project is **self-contained**, so a relative `\input` climbing above
the project root **cannot** resolve. Pasting a source file straight in fails:

```text
LaTeX Error: File `../../../../docs/latex/coursework_preamble.tex' not found.
```

Uploading the preamble by hand works, but must be redone per project and
re-synced whenever the shared file changes. Flatten instead:

```sh
docs/latex/flatten_tex.sh content/cesc_470/hw/hw01
#   -> content/cesc_470/hw/hw01/overleaf/*.tex   (gitignored, regenerable)
```

Each output is standalone. It also **strips comment-only lines naming tooling**,
satisfying the no-tooling-references rule below, and **fails loudly if any
`\input` survives** rather than shipping a file that breaks in Overleaf.

**Edit the source, never the flattened copy** — `overleaf/` is generated output
and is overwritten on the next run.

---

## Structure of a problem file

Five sections, in this order. Skip a section only when it is genuinely empty.

1. **Problem statement** — restate it. The solution must be readable without the
   assignment PDF beside it.
2. **Approach** — the governing formula or principle, **with a citation**, and
   why it applies here. One short paragraph.
3. **Work** — every step. See below.
4. **Check** — verify by an independent route. See below.
5. **Answer** — the result, in an `answerbox`. Nothing else.

### Show every step

The reader is someone **learning the method**, not someone confirming an answer
they already have. Concretely:

- Substitute numbers **before** simplifying, so the reader sees where each came from.
- Carry units through, and state them in the answer.
- Name the trap where a plausible shortcut gives the wrong answer, in a `trap` box.
- When a problem has an answer printed on a slide, compare against it explicitly.

---

## Citations

**Every non-obvious step cites the course material it came from**, by document
and page:

```latex
The performance equation \srcref{Module 01, PDF p55, slide 32}:
```

- Cite the **PDF page**, and the deck's own printed slide number where they
  differ — they usually do, because title slides are unnumbered.
- Cite where a **definition** comes from, not just formulas.
- A citation is a claim that the material actually says this. **Never cite a
  page you have not read.**

### When the course is silent

Some problems explicitly ask for outside research (CESC 470 HW1 Q7: *"Research
and compare ARM and x86…"*). Then, and only then, use `\extref{...}`:

```latex
\extref{ARM Ltd., ``Cortex-A Series Programmer's Guide'', 2024}
```

It renders in a different colour so an external claim is never mistaken for
lecture content. **Do not silently import an outside convention** where the
course teaches a different one — if the course covers it, cite the course.

---

## Verify the numbers, don't just re-read them

A derivation that is internally consistent can still be wrong. Before an answer
goes in an `answerbox`:

- **Recompute it independently** — a few lines of Python, not a re-read.
- **Prefer two routes.** Two methods agreeing is much stronger than one decimal
  matching.
- **Evaluating at a single point proves little.** $x(0)=A\cos\phi$ agrees for
  both $+\phi$ and $-\phi$.
- **For any "impossible" or "no solution" claim, run the search.** That is what
  makes it a result rather than an assertion.
- Where the assignment prints its own answer, state agreement explicitly.

Record what was verified and how, in the assignment `README.md`.

---

## ⚠ Never transcribe an equation from a PDF text layer

`pdftotext` flattens stacked fractions into valid-looking text that means
something else. On CESC 410 HW1 it turned $\cos(\tfrac{\pi}{6}n)$ into
`cos( 6π n)` — a constant signal — and dropped a $\sqrt{\ }$ that decided whether
a signal was periodic. **Neither raises an error.**

Render the region and look at it:

```sh
cd ocr_handler && uv run ocr-handler inspect ../content/<course>/<kind>/<file>.pdf
```

```python
import pymupdf
d = pymupdf.open("HW1.pdf")
d[0].get_pixmap(clip=pymupdf.Rect(180, 270, 420, 320), dpi=400).save("/tmp/x.png")
```

Grep tools read the same broken layer. They are for finding **which document**
covers a topic — never for reading the maths inside one.

---

## A build that succeeds is not a document that is correct

`build_tex.sh` returning `OK` says nothing about layout. It did not catch a
y-label drawn through the tallest stem, or `\angle -75°` rendering as a
subtraction. **Render to PNG and look**, at least once per new visual element:

```python
import pymupdf
d = pymupdf.open("hw01/p03.pdf"); d[0].get_pixmap(dpi=110).save("/tmp/p.png")
```

---

## Per-assignment checklist

1. **Inventory.** Read the assignment. Extract every problem and its points into
   `<kind>NN/README.md` *before* writing LaTeX.
2. **Sum the points and compare against the stated total.** The only cheap check
   that catches a dropped problem. Watch for handout numbering errors — CESC 410
   HW1 labels two different problems "Prob 1"; files use a continuous index and
   **state the discrepancy on the face of the document**.
3. **Ground it in the course materials** before searching the internet.
4. **Write one file per problem.**
5. **Assemble the solutions document** from the answer boxes.
6. **Build-check, then look at it.**
7. **Verify the numbers computationally.**
8. **Report** what is done, what is blocked, and anything Human-only.

---

## Human-only

| Task | Why |
| --- | --- |
| **Confirming what to submit** | Varies per assignment; usually unconfirmed |
| **Canvas submission** | Login |
| **Deciding between two defensible conventions** | Where the course is silent, flag it — do not pick silently |
| **All git mutations** | Human-only, always |

---

## Repo hygiene

- **LaTeX only for solution content.** No Markdown working. `README.md` per
  assignment is tracking metadata, not solutions.
- **PDFs are build products** — gitignored, rebuilt by `build_tex.sh`. The
  instructor's assignment PDF is *source material*: keep it.

  ⚠ **Ignore OUR OUTPUT by name; never blanket-ignore `*.pdf` and try to
  negate the handouts back.** A guessed negation fails silently and loses source
  material that cannot be regenerated:

  ```gitignore
  # WRONG — drops any handout whose name you did not predict
  *.pdf
  !HW*.pdf

  # RIGHT — ignore only what we generate; everything else is kept
  p[0-9][0-9]_*.pdf
  *_solutions.pdf
  overleaf/
  ```

  CPSC 462's handouts are named *"Lab 0"*, *"Introduction to Wireshark"*,
  *"Hands on"* — **none match `HW*`**, so the negation form would have untracked
  all of them without a word. Our build products have predictable names; the
  instructor's files do not. Verify with `git check-ignore -v <path>`, which
  names the exact rule that matched — "it looks right" is not a check.
- **No tooling references in submitted documents** — no script names, flags, or
  repo paths.
- Homework rarely ships code or a zip, unlike the labs. Check before assuming.

---

**Related:** [`../latex/coursework_preamble.tex`](../latex/coursework_preamble.tex) ·
[`../scope.md`](../scope.md) ·
[`../../content/cesc_410/hw/reference_docs/findings.md`](../../content/cesc_410/hw/reference_docs/findings.md)
