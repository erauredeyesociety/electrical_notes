# Claude entry point — CESC 410 homework

**Trigger:** *"`hwNN/` now exists with the assignment in it, work it."*

Read this, then the docs it points at, then work. Stop only for [Human-only](#human-only).

Sibling setup for the lab course: [`../labs_and_projects/prompt.md`](../labs_and_projects/prompt.md). Same instructor, same conventions — but **homework is LaTeX, not Markdown**, and usually involves no code and no zip.

---

## Read first

1. This file.
2. [`reference_docs/findings.md`](reference_docs/findings.md) — **what silently produces wrong answers.** Read before transcribing anything.
3. [`reference_docs/hw_workflow.md`](reference_docs/hw_workflow.md) — the two-document rule, and how a problem file is built.
4. The assignment PDF in `hwNN/`.
5. [`../../../docs/latex/coursework_preamble.tex`](../../../docs/latex/coursework_preamble.tex) — the SHARED preamble: `\answerbox`, `trap`, `\srcref`, `\extref`, `\problemheader` / `\problemheaderlo`, page style, packages.
6. [`reference_docs/cesc410_macros.tex`](reference_docs/cesc410_macros.tex) — the CESC 410 half: DSP notation and `\stemplot`. Do not redefine either set per problem.

---

## ⚠ Never transcribe an equation from a PDF text layer

`pdftotext` flattens stacked fractions into valid-looking text that means
something else. On HW1 it turned $\cos(\frac{\pi}{6}n)$ into `cos( 6π n)` — a
constant signal — and dropped a $\sqrt{\ }$ onto the wrong line, which would have
flipped an aperiodic signal into a periodic one. Neither raises an error.

**Render the region and look at it:**

```python
import fitz
d = fitz.open("hwNN/assignment.pdf")
d[0].get_pixmap(clip=fitz.Rect(180, 270, 420, 320), dpi=400).save("/tmp/x.png")
```

`course_text.py --grep` reads that same broken layer. It is for finding *which
document* covers a topic — never for reading the maths inside one.
Full detail: [HW-01](reference_docs/findings.md#hw-01--pdftotext-silently-corrupts-fractions--wrong-answers-no-error).

---

## The two-document rule

This is the whole shape of the work, and it is not negotiable:

| | Per-problem files | Solutions document |
| --- | --- | --- |
| `hwNN/pNN_<slug>.tex` | one per problem | `hwNN/hwNN_solutions.tex` |
| **Every step, shown** | ✅ full working | ❌ **answers only** |
| Audience | someone learning it | someone checking it |
| Length | as long as it takes | as short as possible |

**Detailed work lives in the per-problem files. The solutions document is the condensed version — final answers, nothing else.** Do not put derivations in the solutions document; do not omit them from the problem files.

Each problem file is **standalone** — it inputs the shared repo preamble and the
CESC 410 macros, then builds by itself, so a broken problem is found where it broke:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}
\input{../reference_docs/cesc410_macros.tex}
\begin{document}
```

```sh
# from the repo root; paths are REPO-RELATIVE
docs/latex/build_tex.sh content/cesc_410/hw/hw01/p01_phasor_form.tex
```

---

## Procedure

### 1. Inventory

List `hwNN/`. Read the assignment PDF. **Extract every problem, its stated LO, and its points.** Record them in `hwNN/README.md` before writing any LaTeX.

**Sum the points and compare against the handout's stated total.** It is the only cheap check that catches a dropped problem — HW1 states 130, and $20+10+20+20+40+20=130$ confirms it.

Watch for handout numbering errors. HW1 labels two different problems "Prob 1" and has no Prob 6; files use a continuous internal index and state the discrepancy on the face of the document.

### 2. Ground it in the course materials — do not guess

The lectures and labs are the authority on notation and method. **Search them before searching the internet:**

```sh
tools/course_text.py --grep "periodic"      # find where the course covers it
tools/course_text.py --list                 # what is available
```

⚠ **4 of 25 documents have no usable text layer** — the handwritten lecture PDFs. `--list` flags them `NO-TEXT`. They are not searchable this way, and inventing what they contain is worse than admitting the gap. Use [`../../../ocr_handler`](../../../ocr_handler) or read the PDF directly.

If the course materials genuinely do not cover something, say so in the problem file rather than silently importing a convention from elsewhere.

### 3. Write one file per problem

Copy [`reference_docs/problem_template.tex`](reference_docs/problem_template.tex). Fill in the header, restate the problem, then work it.

**Show every step.** The reader is someone learning the method, not someone confirming an answer they already have. State which lecture or LO a technique comes from where it is not obvious.

End with the result in an `answerbox`. That is what the solutions document lifts.

### 4. Assemble the solutions document

`hwNN/hwNN_solutions.tex` — one entry per problem, the final answer only. If it takes more than a few lines per problem, it is the wrong document.

### 5. Build-check everything — then *look* at it

```sh
docs/latex/build_tex.sh content/cesc_410/hw/hwNN
```

**A document that compiles is not a document that is correct.** `OK` says
nothing about layout: it did not catch the y-label being drawn straight through
the tallest stem, or `\angle -75°` rendering as a subtraction. Render to PNG and
actually look, at least once per new visual element:

```python
import fitz
d = fitz.open("hwNN/pNN_slug.pdf"); d[0].get_pixmap(dpi=110).save("/tmp/p.png")
```

### 5b. Verify the numbers computationally

Do not submit an answer that was only re-read. Check it by an independent route —
and for any "not periodic" / "no solution" claim, **run the search** rather than
asserting it. Evaluating at a single point is usually too weak: $x(0)=A\cos\phi$
agrees for both $+\phi$ and $-\phi$. See [HW-04](reference_docs/findings.md#hw-04--verify-numerics-computationally-and-prefer-two-independent-routes).

### 6. Report

What is done, what is blocked, and everything from [Human-only](#human-only).

---

## Human-only

| Task | Why |
| --- | --- |
| **Confirming what to submit** | Varies per assignment and is usually unconfirmed — [`reference_docs/submission.md`](reference_docs/submission.md) |
| **Canvas submission** | Login |
| **Deciding whether an answer is right** | Where the course materials are silent and two conventions are defensible, flag it; do not pick silently |
| **Anything needing the handwritten lectures** | Until `ocr_handler` lands, those PDFs are human-read |

---

## Rules

- **LaTeX only for homework content.** No Markdown solutions, no Markdown working. `README.md` per assignment is tracking metadata, not homework.
- **One problem, one file.** A file covering two problems cannot be build-checked independently.
- **Use the existing macros** rather than redefining notation per file. `\answerbox`, `\problemheaderlo`, `\srcref` come from the shared repo preamble; `\stemplot`, `\phasor` and the rest of the DSP notation from `reference_docs/cesc410_macros.tex`. A macro another course would also want belongs in the shared preamble, not in the course macros.
- **Never cite a lecture you have not read.** `course_text.py --grep` first; `NO-TEXT` documents are not searchable.
- **Homework rarely ships code or a zip** — unlike the labs. Check before assuming.
- PDFs are build products: gitignored, rebuilt by `docs/latex/build_tex.sh`.

---

**Related:** [`reference_docs/findings.md`](reference_docs/findings.md) · [`reference_docs/hw_workflow.md`](reference_docs/hw_workflow.md) · [`reference_docs/submission.md`](reference_docs/submission.md) · [`../labs_and_projects/prompt.md`](../labs_and_projects/prompt.md)
