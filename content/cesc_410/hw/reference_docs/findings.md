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

**Fixed in `reference_docs/cesc410_macros.tex`.** `\phasor` wraps its second
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

**Fixed in `reference_docs/cesc410_macros.tex`** by anchoring the label to the
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

**Related:** [`hw_workflow.md`](hw_workflow.md) · [`../prompt.md`](../prompt.md) · [`submission.md`](submission.md)
