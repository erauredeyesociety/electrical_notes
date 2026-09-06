# Findings — CESC 410 homework

Things learned by doing the work, in the form that would have saved the time.
Ordered by how badly each one bites. **HW-01 through HW-04 are the dangerous
ones: they produce confidently wrong answers, not errors.**

Sibling: [`../../labs_and_projects/reference_docs/known_issues.md`](../../labs_and_projects/reference_docs/known_issues.md) (KI-01…KI-09).

---

## HW-01 — `pdftotext` silently corrupts fractions ⚠ **wrong answers, no error**

**Found:** HW1, Problems 3 and 4, 2026-09-04.

`pdftotext -layout` flattens a stacked fraction by emitting numerator and
denominator in visual order, with no delimiter. The result is valid-looking
text that means something else entirely.

| Text layer says | Actually is | Consequence if believed |
| --- | --- | --- |
| `cos( 6π n)` | $\cos\!\big(\frac{\pi}{6}n\big)$ | $\cos(6\pi n) = 1\ \forall n \in \mathbb{Z}$ — the signal becomes a constant, and all four plots are wrong |
| `e^{j(πn/ 8)}` + stray `√` on its own line | $e^{j(\pi n/\sqrt{8})}$ | The $\sqrt{\ }$ is the entire point of the part: with it the signal is **aperiodic**, without it $N_0 = 16$ |

Both misreadings are *plausible*. Neither raises an error. The second is worse:
the stray `√` lands on the wrong line, so it looks like it belongs to part 3.

**Fix — render the region and look at it:**

```python
import fitz
d = fitz.open("hw01/dsphw26-hw1.pdf")
d[0].get_pixmap(clip=fitz.Rect(180, 270, 420, 320), dpi=400).save("/tmp/x.png")
```

Then read the PNG. 400 dpi is enough to resolve a $\sqrt{\ }$ from a `/`.

**Rule: never transcribe an equation from a text layer.** `--grep` is for
*finding* which document discusses a topic, never for reading the maths in it.
This applies to `tools/course_text.py` too — it reads the same broken layer.

---

## HW-02 — The handout numbers two different problems "Prob 1"

**Found:** HW1, 2026-09-04.

`dsphw26-hw1.pdf` has Prob 1 (LO01, phasors) and then, after Prob 5, a second
**Prob 1** (LO05, convolution). There is no Prob 6.

**Fix:** files use a continuous internal index (`p06_convolution.tex`) so they
sort correctly, and **the discrepancy is stated on the face of the document** —
both in `p06` and in the solutions document — so a grader is never left
wondering whether a problem was skipped or duplicated.

**Check the point total against the handout's stated total.** HW1 says 130;
$20+10+20+20+40+20 = 130$ confirms nothing was missed. Do this every assignment;
it is the only cheap check that catches a dropped problem.

---

## HW-03 — `\angle` makes a following minus sign *binary*

**Found:** while rendering the HW1 solutions, 2026-09-04.

`\angle` is a `\mathord`, so TeX parses the `-` in `\angle -75^\circ` as a
**binary** operator and typesets it with space on both sides:

```
  10 ∠ − 75°      wrong — reads as a subtraction
  10 ∠ −75°       right
```

**Fixed in `../reference_docs/cesc410_macros.tex`.** `\phasor` wraps its second
argument in `\mathord{}`, which starts a fresh math list so the sign is unary.
Use `\phasor{10}{-75^\circ}` and it comes out right; do not hand-write `\angle`
in problem files.

---

## HW-04 — Verify numerics computationally, and prefer two independent routes

**Found:** HW1 throughout.

A derivation that is internally consistent can still be wrong. Every numeric
answer in HW1 was checked by an independent computation, and two checks caught
things a re-read would not have:

- **Evaluating at a single point proves almost nothing.** $x(0) = A\cos\phi$
  agrees for both $+\phi$ and $-\phi$, since cosine is even. A full-sweep
  comparison over $\omega t$ is the real check (max error $\approx 10^{-14}$).
- **Exact forms beat decimals.** P2's magnitudes are $\sqrt{325} = 5\sqrt{13}$
  and $\sqrt{189} = 3\sqrt{21}$ exactly — confirmed independently by geometry
  (the phasors are $90°$ apart; then the law of cosines). Two routes agreeing on
  a closed form is much stronger evidence than one decimal matching.

**Rule:** for any claim of the form "not periodic" or "no solution exists",
**run the search**. P4 parts 3 and 4 were confirmed by brute-forcing
$N \le 10{,}000$ and finding nothing, which is what makes "aperiodic" a result
rather than an assertion.

---

## HW-05 — `plt`-free plotting: stem plots come from the `.tex`

**Found:** HW1 Problem 3.

The stem plots are drawn by pgfplots from coordinates written directly in the
`.tex` (`\stemplot`), not rendered to image files. Consequences:

- No image files to gitignore, no figure pipeline, nothing to regenerate.
- The plot and the numbers cannot drift apart — they are the same source.
- Zero-valued samples must be listed explicitly to draw the baseline circles
  that the class plotting format uses.

`\stemplot` takes an optional first argument passed straight to the pgfplots
`axis`, so a compact side-by-side version is
`\stemplot[width=\textwidth,height=3.4cm]{...}`.

---

## HW-06 — `axis lines=middle` puts the y-label through the data

**Found:** while rendering HW1 Problem 3, 2026-09-04.

With `axis lines=middle`, pgfplots centres the y-label at mid-height **on the
y-axis**, which is exactly where a full-height stem at $n = 0$ is drawn. The
label and the tallest sample overlap.

**Fixed in `../reference_docs/cesc410_macros.tex`** by anchoring the label to the
axis box corner:

```latex
ylabel style={at={(current axis.north west)}, anchor=south west}
```

**General lesson: a document that compiles is not a document that is correct.**
`docs/latex/build_tex.sh` returning OK says nothing about layout. Render to PNG
and look at it at least once per new visual element.

---

## HW-07 — Build products vs. source material in one folder

**Found:** setting up `hw/.gitignore`, 2026-09-04.

`hwNN/` holds both generated PDFs (regenerable) and the instructor's assignment
PDF (not regenerable, and the source of truth). A blanket `*.pdf` loses the one
that matters.

**Fixed** with a negation, verified by rule number rather than assumed:

```
$ git check-ignore -v hw01/p01_phasor_form.pdf hw01/dsphw26-hw1.pdf
  .gitignore:5:*.pdf        hw01/p01_phasor_form.pdf      <- ignored
  .gitignore:28:!dsphw*.pdf hw01/dsphw26-hw1.pdf          <- kept
```

`git check-ignore -v` names the exact rule that matched. Use it whenever a
gitignore has a negation; "it looks right" is not a check.

---

## HW-08 — `build_tex.sh <folder>` also tries to build the preamble fragments

**Found:** auditing every `.tex` in the course, 2026-09-05.

`build_tex.sh` builds **every** `.tex` in a folder it is pointed at. Pointed at
`reference_docs/`, that includes two files that are not documents:

```
reference_docs/cesc410_macros.tex     FAIL  Command \coursename undefined
reference_docs/cesc410_preamble.tex   FAIL  no legal \end found
reference_docs/problem_template.tex   OK
```

Both failures are **correct**. `cesc410_macros.tex` `\renewcommand`s
`\coursename`, which the shared preamble must have `\providecommand`ed first,
and it has no `\begin{document}`; `cesc410_preamble.tex` is a comment-only
tombstone. A fragment that compiled alone would not be a fragment.

**Rule: do not "fix" a fragment by making it build.** Build the template by
name, and read a folder-level FAIL against the list above before believing it.

---

## HW-09 — A flattened file that flattens is not a flattened file that compiles

**Found:** auditing the Overleaf outputs, 2026-09-05.

`flatten_tex.sh` guarantees exactly one thing: no `\input` survived. It never
builds what it wrote, so "flattened OK" and "compiles in Overleaf" are separate
claims and only one of them was being checked.

**Check both:**

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
cd content/cesc_410/hw/hw01/overleaf && for f in *.tex; do tectonic "$f"; done
```

Result on 2026-09-05: all 7 HW1 outputs compiled, plus
`reference_docs/problem_template.tex`. Nothing needed fixing — but nothing had
been *verified* either.

**Generalises past LaTeX:** a generator that validates its own output against a
weaker property than the one you care about will pass forever while shipping
broken artifacts.

---

## HW-10 — The flattener used to stamp a repo path into its output ✅ FIXED

**Found:** grepping the flattened copies for tooling references, 2026-09-05.
**Fixed:** same day, in `docs/latex/flatten_tex.sh`.

Flattened files used to open with a second line naming the full source path
(`content/cesc_410/labs_and_projects/lab00/report.tex`) — a repository path in a
document that might be submitted, emitted by the tool that enforces the
no-tooling-references rule everywhere else. The header now carries only the
**basename**, which locates the source without naming a path.

**⚠ The original write-up of this finding overstated the consequence**, and the
correction is the useful part:

> "Lab reports: blocking. The lab packaging guard scans `.tex` for tooling
> references and refuses to build the zip."

**That was wrong on two independent counts.** Both were tested, not reasoned
about:

1. **The strip runs BEFORE the guard.** `make_submission.sh` pipes the staged
   `report.tex` through `strip_comments.py` (which removes comment-only lines),
   and only *then* runs `find_tooling_refs` on the result. The header was a
   comment-only line, so it never reached the guard. Verified by running the
   project's own `strip_tex` + `find_tooling_refs` in that order: **CLEAN**.
2. **The packager never sees the flattened copy anyway.** It copies
   `$LAB/report.tex` — the source — into the staging folder. `overleaf/` is not
   in the packaged set.

So packaging was never blocked. The path in the header was still worth removing,
which is why it was, but the finding as first written would have sent a future
session chasing a failure that could not occur.

**The transferable lesson: check the ORDER of a pipeline's stages before
concluding one of them rejects your input.** "A guard matches this pattern" is
not the same as "the guard sees this text."

---

## HW-11 — `new_tex.sh` cannot reach a sibling kind's macros file

**Found:** working out how a `qz01/` would be scaffolded, 2026-09-05.

The scaffolder walks up from the target folder running
`find <ancestor> -maxdepth 2 -path '*/reference_docs/*_macros.tex'`. From
`content/cesc_410/qz/qz01` that sees `qz/reference_docs/` and
`content/cesc_410/reference_docs/` — but **not** `hw/reference_docs/`, which
sits three levels below the common ancestor. It exits 1 before writing a file:

```text
error: no reference_docs/*_macros.tex found at or above content/cesc_410/qz/qz01.
```

**The tempting fix is the wrong one.** Creating
`qz/reference_docs/cesc410_macros.tex` makes the scaffolder work and triggers
this, correctly:

```text
WARNING: 2 macros files for course 'cesc_410':
         Two files means hw/ and qz/ can silently diverge.
```

Two macros files for one course is a silent-wrong-answer bug: `hw/` and `qz/`
compile against different notation and nothing errors.

**So: one macros file per course, and a quiz reaches across to it** —
`\input{../../reference_docs/cesc410_macros.tex}` — copying
`problem_template.tex` rather than scaffolding. Verified end to end on a
throwaway `qz99/`: built, flattened, and the flattened copies compiled with the
DSP macros inlined. Detail: [`hw_workflow.md`](hw_workflow.md#quizzes-and-exams).

---

**Related:** [`hw_workflow.md`](hw_workflow.md) · [`../prompt.md`](../prompt.md) · [`submission.md`](submission.md) · [`../hw01/README.md`](../hw01/README.md)
