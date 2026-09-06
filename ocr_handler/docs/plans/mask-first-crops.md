# Mask-first crops — removing the background, and stopping at the neighbour

> **Type: ACTIVE-SPEC. Built 2026-09-05** as [`src/ocr_handler/crops.py`](../../src/ocr_handler/crops.py),
> floor at [`tests/persistent/test_crops.py`](../../tests/persistent/test_crops.py).
> Living document, named by concept per [../directives/roadmap-and-plans.md](../directives/roadmap-and-plans.md).
> Grounded in [../research/equation-ocr-specialists.md](../research/equation-ocr-specialists.md) §4.2 and §4.5;
> every number below marked *measured* was run on this machine through
> [`tools/gpu_lock.py`](../../tools/gpu_lock.py), UniMERNet-Base, fp16, greedy, one model at a time.
> Constrained by [ADR-0002](../decisions/0002-numpy-scipy-pillow-not-opencv.md) — numpy, scipy, Pillow, no OpenCV.
>
> ⚠ **[INDEX.md](./INDEX.md) was deliberately not touched** (other agents hold that file). It needs one
> row for this document.

---

## 1 · The principle

**The recogniser's accuracy is decided before the recogniser runs.** Two things about the *image
handed to it* moved the output further than any model or hyper-parameter measured on this project:
what is in the background, and where the crop stops.

Both are free. Both are deterministic. Both use masks `ink.py` already computes.

---

## 2 · Finding one — removing the background beats changing the model

The fixture handwriting sits on a slide's **light-blue graph-paper grid**. Grayscale conversion turns
that grid into mid-grey horizontal rules, and UniMERNet reads a horizontal rule as a fraction bar.

*Measured*, same box, same model, same padding — only the rendering differs:

| | output |
| --- | --- |
| `expo` / raw pixels | `e^{iwo})^{n}=e^{`**`\frac12`**`woh}` ← the grid, read as a fraction |
| `expo` / **composited** | `e^{iw_0})^{n}=e^{iw_0 r}` ← **`\frac12` gone, subscript recovered** |
| `eqline` / raw pixels | `= 1\alpha\vert^{n}(\cos(w_0 h)+j\sin(w_0 h)).` |
| `eqline` / **composited** | **`= \vert\alpha\vert^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).`** |

Ground truth for `eqline` is `= |\alpha|^{n}(\cos(\omega_0 n)+j\sin(\omega_0 n)).` — the composited
read is correct but for one `\omega` rendered `w`. The raw read has three errors.

**A composited crop is the page's ink painted flat black on clean paper, and nothing else.** The
hallucination is not suppressed, it is made impossible: the grid is not in the image.

### 2.1 What `paint` must contain — the counter-test

The obvious refinement is to paint only the *annotation* ink and drop the printed content, which
would erase neighbouring lines entirely and make the padding cliff of §3 disappear. It was tried.
**It is destructive**, because a lecture expression is routinely half printed and half handwritten:

| `eqline`, pad 12 | output |
| --- | --- |
| paint = red ∪ dark | `= \vert\alpha\vert^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).` |
| paint = **red only** | `\cos(w_1 r)\sin(w_1\varphi_h)` ← the printed `= \|α\|^n( … + j … )` is gone |

Same on the fragments: `r3` loses its parentheses, `r4` loses its `j`. **The background is the enemy;
the printed content is part of the equation.** `paint = red_mask | dark_mask`.

---

## 3 · Finding two — padding is a cliff, and the cliff is at the neighbour

Output is byte-identical across a wide plateau of padding — the model re-crops padding away itself,
in `crop_margin` — and then collapses outright into `\begin{array}` multi-line mode once the crop
reaches the next thing on the page. It does not degrade. It is lost.

*Measured*, composited rendering, `eqline`, whose nearest neighbour is a printed line **6 px above**:

| pad | output |
| ---: | --- |
| 0, 4 | `= \vert\alpha\vert^{n}(\cos(\cos n)+j\sin(w_0,w)).` |
| 8 | `= 1\alpha\vert^{n}(\cos(\cos n)+j\sin(w,n)).` |
| **12, 16, 20** | **`= \vert\alpha\vert^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).`** — identical, best |
| 24 | `= 1\times 1^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).` |
| **32** | **`\begin{array}{rl}{((n)-u)^{n}\cdots`** ← cliff |
| 40 | `\begin{array}{rl}&{\displaystyle \chi(n)=\alpha^{n}=…` |

Against `expo`, whose nearest neighbour is **141 px** away: held to pad 96, garbage at 160. Same
model, same page, same day — **8× the padding tolerance, because of where it sits.**

This is the small-scale reproduction of DocTron-Formula (`2508.00311` Table 3), where UniMERNet
scores 0.919 CDM on line-scoped crops, 0.644 on paragraph-scoped and **0.009** on page-scoped.

> **Crop tolerance is a property of the page, not of the model.** A tuned constant is therefore the
> wrong shape of answer.

### 3.1 The rule

For each region, measure the clear distance to the nearest **other content** — printed included —
and cap the padding just past it, **per side**:

```
pad_side = min(requested_pad, gap_side + INTRUSION)
```

- **`gap_side` is measured against all page content**, `red_mask | dark_mask`, not against other ink
  regions. The thing that killed `eqline` was a printed line no ink mask contains.
- **Per side, never one scalar.** *Measured* on the fixture equation: **6 px of clearance above,
  675 px below.** One number would either clip the room underneath or walk into the line overhead.
- **The scan band is widened by the requested pad**, because a crop that pads sideways can reach
  content that does not overlap the bare box.
- A side with nothing beyond it gets its distance to the page edge — which is all the padding that
  side could use anyway.

### 3.2 `INTRUSION = 8`, and why it is not zero

The first implementation clamped to `gap − 2`: stop *short* of the neighbour. It is the intuitive
rule and it is **wrong, measurably**. On `eqline` it cut pad 12 down to 4 and traded the correct read
for a worse one:

| `eqline`, composited | output |
| --- | --- |
| `gap − 2` guard → pad 4 | `= \vert\alpha\vert^{n}(\cos(\cos n)+j\sin(w_0,w)).` |
| `gap + 8` guard → pad 12 | `= \vert\alpha\vert^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).` ← correct |

Because the model re-crops its own input, clipping a few pixels of a neighbour's descenders is free.
The cliff arrives when *enough of the next line is legible* to switch the decoder into array mode.
Across the two targets the boundary is tight — **safe at `gap + 18`, broken at `gap + 19`** — so `8`
is a deliberate half-measure with n=2 behind it, not a fitted constant.

It has a useful consequence: **`gap + 8 ≥ 12` whenever `gap ≥ 4`, so the guard is invisible at the
default pad.** It exists to stop a large request from walking off the cliff, not to shave a safe one.
*Measured* on the fixture page it fires on 4 of 5 regions, all on sides whose gap is literally 0.

---

## 4 · The three judgement calls

### 4.1 Composite alongside raw, not instead of it

**Both are produced.** `Crop` carries `.raw` and `.composite`.

The composite is not a uniform win. *Measured*, end-to-end through `crops.prepare()`, on the five
regions `ink.regions()` actually returns plus the two research boxes:

| target | verdict |
| --- | --- |
| `eqline` | **composite clearly better** — recovers `\|\alpha\|^{n}` and `\omega_0` |
| `expo` / `r2` | **composite clearly better** — deletes the `\frac{1}{2}`, recovers `w_0` |
| `r3` (`cos` blank) | *raw marginally better* — `(\cos(won)+` vs `(\cos(w)n)+` |
| `r4` (`sin` blank) | *wash* — both wrong; raw keeps the trailing `.` |
| `r0`, `r1` | not equations (stem plots); garbage either way, see §6 |

Two decisive wins, two marginal losses, on the two crops that are fragments of a printed line rather
than whole expressions. That is not the evidence needed to delete the raw pixels. **Feed both,
compare, and revisit when the sample is bigger than one page.**

### 4.2 Background: white, with `median` available and currently a no-op

Default **white**. It is the rendering that won the measured sweep, and the honest reason to
consider the page's own median instead — that a model trained on scans expects paper texture —
turns out not to arise here. *Measured* median background:

| fixture | median | mean non-ink |
| --- | --- | --- |
| `F1_cesc410_plw_i04` (annotated slide) | **(255, 255, 255)** | 253.1 |
| `F1c_cesc410_base_i04` (unannotated) | **(255, 255, 255)** | 253.1 |
| `F2_ps160_m14_i08` (scanned) | **(255, 255, 255)** | 249.6 |

**All three are pure white, the scanned one included.** `background="median"` is implemented and
would change nothing on today's corpus; it earns its place only when a genuinely tinted scan appears,
and at that point it should be re-measured rather than assumed. Note the direction of the risk:
UniMERNet normalises around a mean of `0.7931·255 ≈ 202`, so pure white sits ~1.2σ light of its
training centre. That did not hurt in any measured run, but it is the reason the knob exists.

### 4.3 Overlapping regions — report, do not paper over

When two regions' boxes intersect, the neighbour distance is genuinely 0 and padding falls to
`INTRUSION`. But **no padding rule can help**: the crop already contains a second expression. That is
a *grouping* failure — `ink.regions(merge_px=…)` split one thing in two, or merged two into one — and
the honest response is to surface it, not to emit a crop that looks safe.

`Crop.contested` is `True` when another region's box overlaps this one. The caller can merge the two
regions, or route the crop to something that tolerates several expressions. It is deliberately not
"fixed" inside `crops.py`, because the fix belongs one stage upstream.

---

## 5 · The module

```python
from ocr_handler import crops, ink

page, red, dark = ink.page_and_masks(png)      # one decode, both masks
content = red | dark

for c in crops.prepare(png, ink.regions(red), paint=content, occupancy=content):
    c.raw          # the page as it is
    c.composite    # ink on clean paper -- the measured win
    c.padding      # per-side, with .gaps, .clamped and .note()
    c.contested    # another region's box overlaps this one
```

| Function | Does |
| --- | --- |
| `gaps(region, occupancy, reach)` | clear pixels to the nearest other content, `(top, right, bottom, left)` |
| `clamp(region, occupancy, pad, intrusion)` | → `Padding`, per side, cut where the neighbour is close |
| `composite(page, paint, box, background, binary)` | ink on clean paper; `binary=False` keeps true greys |
| `prepare(...)` | → `list[Crop]`, both renderings, guarded padding, overlap flagged |

`ink.page_and_masks` was added alongside, because `red_mask` and `dark_mask` each re-open the file
and `prepare` needs the pixels and both masks — three decodes of the same PNG otherwise.

**Validation of the gap rule.** `crops.gaps()` reproduces the two clearances the research measured by
hand, exactly: `eqline` **(6 above, 675 below)** and `expo` **(141 above, 216 below)**. It is not
approximating them.

---

## 6 · What this does not solve

- **`r0` and `r1` are stem plots, not equations.** `crops.py` prepares them faithfully and UniMERNet
  returns 100–200 tokens of `\frac{\int\limits_0^\infty …}` nonsense for both. Nothing here decides
  *whether a region is an equation at all*, and until something does, a formula recogniser will be
  handed figures. That is the next gap, and it is upstream.
- **Masking needs separable ink.** The whole §2 win is available on the annotated `-plw` lectures,
  where there is a red channel to key on. On the 430-document scanned corpus there is no annotation
  layer and the raw crop is all there is — `dark_mask` alone composites content onto white, which is
  a weaker version of the same idea and is unmeasured.
- **n is small.** One page, four equation-shaped targets, ~120 model outputs across all runs. The
  direction is consistent and reproduces a published curve; the constants are not settled.
- **Deskew is still nobody's job.** UniMERNet's augmentation used `rotate_limit=1` — one degree.
  A composited crop of skewed handwriting is a clean image of a skewed equation.
