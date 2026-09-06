# Whether the mask trick survives P2 and P3 — measured, per stratum

> Date: 2026-09-06 · Status: **Reference** (re-run when the corpus changes)
> Keywords: ink separability, colour key, diff_mask, optional content group, OCG, graph paper grid,
> OneNote, flatbed scan, blue ballpoint, RED_MARGIN, head-to-head strata, mask-first crops

**Answers** the single biggest unknown in
[../research/stage2-slate-and-head-to-head-2026-09-06.md](../research/stage2-slate-and-head-to-head-2026-09-06.md)
§ Verdict row 6 and § 4.1 — *"the best of 84 measured outputs came from `ink.py`'s binary mask, which
needs separable ink, and two thirds of this corpus's handwriting has none."*

**Corrects** § 4.1's stratum table in four places, and
[../plans/mask-first-crops.md](../plans/mask-first-crops.md) § 6 in one.

No model ran. No GPU. Everything below is CPU pixel arithmetic at 200 dpi via PyMuPDF
([ADR-0001](../decisions/0001-pymupdf-is-the-only-pdf-library.md)) with numpy/Pillow
([ADR-0002](../decisions/0002-numpy-scipy-pillow-not-opencv.md)), `nice -n 19`. Every page named below
was **rendered and looked at** before any statistic was believed — twice that changed the conclusion,
and both are recorded in § 6.

---

## Summary

**The premise of the question is wrong, and the answer is better than feared.** A usable mask is
constructible on **both** P2 and P3, by two routes neither of which is `colour_mask` or `diff_mask`
as `ink.py` ships them. What does *not* survive is `ink.py`'s **constants**.

| | What it really is | Ink separable from background? | Handwriting separable from print? | Twin needed? |
| --- | --- | --- | --- | --- |
| **P1** | PDF Annotator **red** ink over a Ghostscript slide deck | yes — `red_mask` | yes | **no** — the annotations are an **optional content group**; rendering it off is a pixel-exact synthetic twin (IoU **1.0000**) |
| **P2** | a **OneNote page** printed via *Microsoft Print To PDF*; handwriting is **opaque white-backed JPEG rasters** pasted over a light-blue vector grid | **yes, with a 62-grey-level margin** — `dark_mask` catches **0 of 2,739,777** grid pixels | not photometrically (both are black) — but **exactly**, via `page.get_image_rects()` | no |
| **P3** | **two** LANIER MP 6503 flatbed scans, blue ballpoint over print | yes | **document-dependent**: unbounded on one, 9 : 1 on the other (whose *print* is navy) — resolved by using a **different margin for the locator than for the paint** | no |

Three corrections that change the head-to-head:

1. **`RED_MARGIN = 55` transposed to blue destroys P3's handwriting *as paint*.** At the shipped
   margin the equation `f' = f_s (v ± v_L)/(v ± v_s)` composites to a broken dotted skeleton (§ 3.2).
   At margin 25 it is complete and legible, at **zero** measured cost in printed-text contamination —
   0 false positives on 256,100 labelled printed pixels at *every* margin from 10 to 55. The same
   constant is the **right** one for the *locator* (§ 3.4), which is why one number cannot serve.
2. **P1 is one document, not two.** `dsp-lctr1-…-plw.pdf` contains **no handwriting at all** — its
   "annotations" are 14 `FreeText`, 1 `Highlight` and 6 `Line` PDF annotations. The red pixels
   `red_mask` finds there are a **red arrow**. § 4.1 allocates 12 of 24 crops to a two-document P1;
   the handwriting is in **7 pages of one file**.
3. **`ink.regions`' `merge_px = 64` does not transfer.** It was swept on sparse red marginalia. On P2's
   dense handwriting it merges a whole page of derivation into **one 1294 × 1498 crop**; on P3's thin
   ballpoint it fragments (§ 5).

---

## 1 · What P2 and P3 actually are

Both files named in § 4.1 exist. Neither description is quite right.

### 1.1 P2 — `content/cesc_410/lectures/f26_lctr03_LTI_systems_conv.pdf`

8 pages. Producer **`PDF Annotator 6.1.0.620 [Microsoft: Print To PDF]`**, title
`LTI systems^J conv^J and LCCDES`, author `jhl`, created 2017-08-30.

*"OneNote export"* is right in substance, though the file never says so — the string `OneNote` does
not appear anywhere in it. The evidence that it is one anyway is the page furniture — a per-page footer
`LTI systems^J conv^J and LCCDES Page N` (OneNote's section-name + page-number print footer), a
`LO5 p.N` typed header, and OneNote's **Grid** page background. It was printed to PDF by *Microsoft
Print To PDF* and then re-saved by PDF Annotator 6.1, which flattened everything.

**What that flattening did, and it is the whole answer for P2:**

- The graph-paper grid is **vector**, exactly **114 path objects per page**, one flat colour.
- The handwriting is **14 JPEG image XObjects** across 8 pages (7 pages carry one or more), each
  drawn on an **opaque white background**. No `SMask` anywhere in the file — checked.
- Consequently the grid does **not** pass under the strokes. Inside the pasted rectangles, 91.6% of
  pixels are pure white (p5, measured).
- **Every dark pixel on every page lies either inside a pasted image rectangle or inside a text-layer
  block bbox.** There is no handwriting drawn directly onto the grid.

`red_mask` returns **0.0000%** on all 8 pages. There is no colour key and no twin — § 4.1 is right
about that, and it does not matter.

### 1.2 P3 — `content/ps160/midterm_01/Worked Problems.pdf`, **and a second file § 4.1 missed**

10 pages, producer/creator **`LANIER MP 6503`** (a Ricoh-family MFP), one 3300 × 2550 JPEG per page
(300 dpi letter), `rotation = 270`, zero text characters. A genuine flatbed/ADF scan of a worked exam
key: **black printed exam, blue ballpoint working**. 9 of 10 pages carry ink.

A corpus pass (459 documents, 7,198 pages, metadata + a full-page-image signature) finds **one other
document from the same scanner**: `content/ps160/m17/M17 Review.pdf`, 6 pages, 6 of 6 with blue
ballpoint. It belongs in P3 and it is **not the same problem** — see § 3.3.

> ⚠ § 4.1 labels P3's pages "idx 129, 130". The `p4` / `p5` in those `labels.csv` row ids are
> **1-indexed** page numbers — PyMuPDF page indices **3 and 4**. Verified by matching each row's note
> to the rendered page (idx 129's *"sound intensity level … Doppler shifted frequency"* is index 3).

---

## 2 · P2 — the mask is constructible, and it is `dark_mask` unchanged

### 2.1 The grid is a single flat colour, and it is nowhere near the threshold

Measured over the grid alone — every pixel outside a pasted image rectangle and outside a text-layer
block bbox, all 8 pages:

| | value |
| --- | --- |
| grid-only pixels examined | **2,739,777** (5.4–13.1% of each page) |
| grid mean RGB | **(214.8, 239.7, 253.2)** — the flat colour is **(202, 232, 252)**, antialiased toward white |
| grid **red** channel, min / p0.1 / p1, every page | **202 / 202 / 202** |
| smallest max-channel over all grid pixels | **253** (248 on p4) |
| `dark_mask` (`all channels < 140`) hits on grid | **0** |

The grid's darkest channel is **202**; `dark_mask` cuts at **140**. **Margin: 62 grey levels, zero
false positives on 2.74 million pixels.** This is not a threshold that needs tuning; it is not close.

Handwriting for comparison (p5): mean RGB **(59, 59, 59)**, max-channel p50 **54**, p95 **130**,
p99 **138**.

### 2.2 The composite still has a job — 15.4% of the crop foreground is grid

The grid is not *behind* the strokes, but it *is* inside the crop, because `crops.clamp` pads past the
edge of the pasted white rectangle. Over the **26 crops** the pipeline cuts from P2's 7 handwriting
pages (locator = `dark_mask & image rects`, `pad = 12`):

| class of crop foreground | pixels | share |
| --- | ---: | ---: |
| ink (`max < 140`) | 354,149 | 38.8% |
| neutral JPEG stroke halo | 418,516 | 45.8% |
| **blue grid** (`min < 250 & max ≥ 200 & b − r > 20`) | **140,233** | **15.4%** |

`Crop.composite` deletes both the grid and the halo. Looked at side by side, the composite of the
`x[n] → h₁[n] → h₂[n] → y[n]` block diagram is stroke-for-stroke identical to the raw crop with the
grid strip on its left edge removed. **No visible erosion.**

### 2.3 The handwriting *locator* on P2 is structural, not photometric

`dark_mask` is the right **paint** but the wrong **locator**: it also lights the typed slide bullets and
the OneNote footer, which are the same black. There is no colour to key on.

There is an exact route anyway. **The handwriting is precisely the set of pasted image XObjects**, and
PyMuPDF hands their page rectangles over for free:

```python
rects = [r for xref, *_ in page.get_images(full=True) for r in page.get_image_rects(xref)]
```

`ink.regions(dark_mask & image_rects)` drops the footer and the typed bullets and keeps every
handwritten block. This is the P2 analogue of `red_mask` and it costs no pixels.

> This is a **document-class** route, not a corpus-wide one: it works because a OneNote print puts
> handwriting in rasters and typed text in the text layer. It would fail on a page whose *figures* are
> also rasters. On P2, all 14 images are handwriting — checked by rendering all 8 pages.

---

## 3 · P3 — the mask is constructible, and the shipped constant is wrong

### 3.1 Separability, on 631,100 hand-labelled pixels

Label boxes were cut by hand from `Worked Problems.pdf` pages 3 and 4, **rendered and inspected
individually** to confirm each contains only printed text or only handwriting (three boxes were
discarded for contamination first; see § 6). Statistic: **chroma = b − max(r, g)**.

| rule | printed pixels lit (of **256,100**) | handwriting pixels lit (of **375,000**) |
| --- | ---: | ---: |
| `b > 100 & chroma > 55` (`ink.py`'s RED constants, transposed) | **0** (0.000%) | 7,694 |
| `b > 100 & chroma > 40` | **0** | 10,798 |
| `b > 100 & chroma > 30` | **0** | 12,872 |
| `b > 100 & chroma > 25` | **0** | 14,017 |
| `b > 100 & chroma > 10` | **0** | 18,275 |
| `dark_mask` (`max < 140`) | 10,405 | **0** (0.000%) |

**The two masks are exactly complementary and the separation is exhaustive.** Printed text on this
document has chroma p99 = **0** — literally no blue excess. Sweeping the decision threshold over 0–120,
the balanced error bottoms out at **0.00%** (threshold ≈ 4) counting only stroke cores, and **0.05%**
counting every pixel out to the antialiased edge.

Whole-document check, all 10 pages: `dark_mask ∩ blue_mask(margin 25)` is **≤ 0.109% of `dark_mask`**
on every page, and 0 on five of them.

So P3 **does** have a colour key, and § 4.1's *"neither `red_mask` nor a twin"* is wrong on the first
half. The analogue is one line:

```python
blue = (b > 100) & (b - r > MARGIN) & (b - g > MARGIN)      # locator: handwriting only
paint = blue | dark_mask                                    # the red|dark analogue
```

### 3.2 …but as *paint*, `MARGIN = 55` destroys the handwriting, invisibly at page scale

The 55 row above lights 7,694 handwriting pixels; the 25 row lights 14,017 — **1.8× more ink for the
same zero contamination**. That is not a rounding difference. Ballpoint on a 300-dpi scan is a light,
thin stroke; margin 55 keeps only the saturated core.

Run through the shipped `crops.prepare(paint=blue|dark, binary=True)` on P3 p3, the equation
`f' = f_s (v ± v_L)/(v ± v_s)`:

| margin | composite |
| ---: | --- |
| **55** (shipped constant) | a **broken dotted skeleton** — every glyph fragmented, `f_s` reduced to two dots |
| 40 | legible, strokes still thin and pitted |
| **25–30** | **complete, clean, indistinguishable from the raw crop minus the paper** |
| plain `min-channel < 190` (no colour key at all) | also complete and clean |

The raw crop of that equation is perfectly legible. **At the shipped constant the composite arm is
strictly worse than the raw arm on P3, and would have been scored as a model failure.**

> **This is the finding that needed a picture.** At whole-page scale the margin-55 mask looks fine.
> The erosion only shows at the scale a recogniser sees. `save_mask` on a page is not the check.

### 3.3 The second P3 document does *not* separate, and this is the honest limit

`ps160/m17/M17 Review.pdf` is the same scanner, same course, same kind of page — and its **printed
body text is dark navy blue, not black**. Two blues.

Labelled boxes on p1 (609,300 printed px, 328,000 handwriting px):

| | min-channel p5 / p50 / p95 | chroma p5 / p50 / p95 |
| --- | --- | --- |
| printed (navy) | 16 / **63** / 168 | −19 / **8** / 35 |
| handwriting (pale ballpoint) | 122 / **152** / 176 | 31 / **56** / 85 |

| rule | printed lit | handwriting lit | ratio |
| --- | ---: | ---: | ---: |
| `chroma > 55 & b > 100` | 316 | 2,846 | **9 : 1** |
| `chroma > 25 & b > 100` | 5,859 | 7,480 | 1.3 : 1 |
| `chroma > 25 & 100 < min < 210` | 2,776 | 7,277 | 3 : 1 |
| `chroma > 30 & 110 < min < 215` | 1,455 | 6,559 | 5 : 1 |
| `dark_mask` | 45,278 | **0** | — |

At margin 25 the blue mask **ghosts the entire printed paragraph** — confirmed by rendering the
intersection, which reads as legible text. Whole-document: 2.5–4.8% of `dark_mask` is claimed by
`blue_mask(25)` on every page, and that leak is **3.8–9.0% of the blue mask itself**.

**Two documents in one stratum, from one scanner, and no single margin serves both jobs on either
of them.** Margin 55 keeps M17's print out (9 : 1) but — checked at crop scale — erodes M17's ink the
same way it erodes Worked Problems'. Margin 30 composites M17 cleanly but leaks 6.6% of the printed
pixels into the mask.

### 3.4 The fix: the locator and the paint are two jobs with opposite tolerances

The mask does two things and they want different constants, which is why one number cannot be right:

- the **locator** feeds `ink.regions`, which **dilates by `merge_px` before labelling**. It only needs
  enough stroke core to place a box. It tolerates erosion and it does **not** tolerate contamination —
  one leaked printed paragraph swallows the region.
- the **paint** feeds `crops.composite`, which reproduces exactly the pixels it is given. It tolerates
  contamination — printed content is *supposed* to be in the paint,
  [../plans/mask-first-crops.md](../plans/mask-first-crops.md) § 2.1 — and it does **not** tolerate erosion.

Measured on M17 p1, `merge_px = 48`:

| | locator margin **30** | locator margin **55** |
| --- | --- | --- |
| regions | 11, of which four are **1251×235, 1339×353, 968×425, 834×335** — printed paragraphs pulled in | **12, every one handwriting-sized** (max 839×421, median ~200×120) |

Running `locator = blue(55)` with `paint = blue(25) | dark`, both crops inspected: `ΔT = 46 °C` and
`= 2.63 mm` come out **complete, clean, and free of printed text**. The split resolves M17.

What holds on both documents without any fitting: **`dark_mask` lights zero handwriting pixels on
either.** The paint mask `blue | dark` is safe everywhere; only the locator margin needs a number, and
it wants the **high** one.

---

## 4 · The route § 4.1 assumes is unnecessary on P1 — `diff_mask` needs no twin

While checking what P1 is, a cheaper route turned up and it removes the "twin control" column from the
protocol.

`f26_lctr02_DT signals and systems-plw.pdf` declares an **optional content group** named
`PDF Annotator` (`145 0 obj /Type /OCG`), and its 12 annotation XObjects each carry an `/OC` reference.
Rendering with the layer switched off is a synthetic un-annotated twin:

```python
doc = pymupdf.open(annotated)
doc.set_layer_ui_config(0, action=2)      # 2 = OFF.  NOT doc.set_layer(), which silently does nothing here
```

| page | `red_mask` | **OCG-off diff** | real-twin diff | IoU(OCG, twin) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 6,590 | 7,497 | 7,497 | **1.0000** |
| 2 | 4,939 | 5,651 | 5,651 | **1.0000** |
| 3 | 11,799 | 13,259 | 13,259 | **1.0000** |
| 4 | 9,636 | 10,988 | 10,988 | **1.0000** |
| 5 | 14,753 | 16,674 | 16,674 | **1.0000** |
| 6 | 14,748 | 16,669 | 16,669 | **1.0000** |
| 8 | 989 | 1,109 | 1,109 | **1.0000** |

**Pixel-identical to the companion file, from one PDF.** `red_mask` recovers 87–89% of the layer (IoU
0.873–0.892) — it misses the antialiased stroke edge, which is the same erosion as § 3.2 in a milder
form.

⚠ `doc.set_layer(-1, off=[145])` produces **no change at all** on this file and returns no error. Only
`set_layer_ui_config` works. That is a silent-no-op trap.

### 4.1 The `/Ink` contradiction, resolved

[../directives/documentation-discipline.md](../directives/documentation-discipline.md) records an open
contradiction: *"Two measurements disagree about whether the annotation ink is embedded images or
vector `/Ink` objects."* Measured today:

- `/Subtype /Ink` occurrences: **0**. PyMuPDF `page.annots()`: **none, on any page**.
- The 7 `/Ink` byte hits are keys inside `/Private` dictionaries hanging off `/PDFAnnotator` piece-info
  objects — vendor base64 stroke blobs kept for re-editing, e.g.
  `151 0 obj << /Ink (base64:AL4bHAOAgAQdBKIQ…`.
- The annotated file has **36 images to the base's 24**. The 12 extra are the ink.

**The rendered ink is raster, not vector.** `tmp_ocr_child.md`'s *"it is vector ink … handwriting here
is geometry, not pixels"* is **wrong as stated**; the file does carry `/Ink` keys, but they are opaque
private data and nothing on the page is a stroke path. **Contradiction closed.**

---

## 5 · What does *not* transfer: `ink.regions`' constants

`merge_px = 64` came from a sweep on P1's sparse red marginalia at 200 dpi, whose signature was a
**stable plateau of 5 regions across 56–80**. Re-running that sweep on the other strata, same dpi,
region count over largest-region area in thousands of pixels (page = 3,740 kpx):

| merge_px | 16 | 24 | 32 | 40 | 48 | **64** | 80 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **P1a p4** red *(control)* | 19 / 28k | 14 / 50k | 10 / 116k | 8 / 139k | **6 / 231k** | **5 / 251k** | **5 / 267k** |
| P2 p2 `dark & imgrects` | 52 / 513k | 28 / 526k | 11 / 539k | 9 / 551k | 8 / 564k | 5 / 591k | 4 / 889k |
| P2 p5 `dark & imgrects` | 101 / 187k | 63 / 261k | 29 / 344k | 14 / 640k | 6 / 819k | **2 / 1,871k** | 1 / 2,368k |
| P2 p7 `dark & imgrects` | 53 / 66k | 35 / 85k | 23 / 116k | 10 / 288k | 9 / 299k | 5 / 694k | 4 / 887k |
| P3a p3 `blue(25)` | 16 / 15k | 12 / 35k | 11 / 38k | 7 / 49k | 6 / 72k | 6 / 82k | 3 / 194k |
| P3a p4 `blue(25)` | 39 / 92k | 26 / 206k | 19 / 383k | 16 / 391k | 13 / 448k | 11 / 465k | 8 / 483k |

**The plateau is a property of P1, not of the method.** Neither P2 nor P3 has one — both collapse
monotonically, so there is no value the sweep *chooses*; it has to be picked against the page's logical
content.

- **P2** at `merge_px = 64` merges a whole page of derivation into **one region**: p5 returns **2**
  regions for 8 lines of prose plus 4 stem plots plus 3 equations, the larger of them **1,871 kpx —
  half the page**. That is a page-scoped crop, and DocTron-Formula's published curve
  (0.919 line → 0.644 paragraph → **0.009 page** CDM) says exactly what a recogniser does with one.
  P2's line-scoped range is nearer **24–32**.
- **P3** fragments instead: p4 returns 11 regions at margin 25, five of them under 400 ink pixels, and
  5 of 11 flagged `contested`. `min_pixels = 120` is strained here too — whole small equations arrive
  at **145–370** ink pixels, uncomfortably close to the blank-crop guard that catches the one
  hallucination no output-side test does.

**Re-sweep per stratum before cutting the head-to-head crops, and pick against the page's logical
content rather than against a plateau that is not there.** The sweep is free; the procedure is already
written down in `ink.regions`' docstring.

---

## 6 · Method, and the two places looking changed the answer

Pages rendered at 200 dpi (the protocol's dpi) with `page.get_pixmap(matrix=Matrix(200/72, 200/72),
colorspace=csRGB, alpha=False)`. Label boxes were cut by hand and **each one rendered and viewed**
before its pixels were counted.

Two statistics were wrong until the picture was looked at:

1. **Three of the first eight label boxes were contaminated** — a "blank paper" box on P3 p4 contained
   a faint `ρ = 413/(π·(0.17)²)`, a "white box background" box on P2 p5 contained `h[n−k] is`, and a
   "printed only" box contained a blue pen underline. All three produced plausible, wrong percentiles.
   They were re-cut against the rendered crop.
2. **The first P2 crop measurement said 54.5% of crop foreground was grid.** It was 15.4%; the
   classifier was counting the neutral JPEG halo around every stroke as "grid" because it only tested
   luminance. Adding the chroma term fixed it. Nothing about the page had changed.

Scripts are in the session scratchpad, not in `src/` — nothing under `src/` or `tests/` was touched.

---

## 7 · What this means for the head-to-head protocol

`stage2-slate-and-head-to-head-2026-09-06.md` § 4.3 says all three rendering arms come free from
`crops.prepare` and need no new code. **On P1 that is true. On P2 and P3 it is not** — `paint` and the
locator have to be built differently per stratum, and one shipped constant is actively harmful.

**Recommended, with the measurement behind each:**

| # | Change to § 4.1 / § 4.3 | Because |
| --- | --- | --- |
| 1 | **Keep all three arms on all three strata.** Do not add "the mask result does not generalise" — it does. | § 2.1 (62-level margin, 0/2.74 M), § 3.1 (0 FP on 256,100 px) |
| 2 | **Per-stratum `paint` and locator, stated in the protocol.** P1: `locator=red`, `paint=red\|dark`. P2: `locator=dark & image_rects`, `paint=dark`. P3: `locator=blue(55)`, `paint=blue(25)\|dark`. | § 2.3, § 3.1, § 3.4 |
| 3 | **Split the blue margin into two: a high one for the locator, a low one for the paint.** `locator = blue(55)`, `paint = blue(25) \| dark` works on **both** P3 documents. A single constant is measurably wrong in both directions. | § 3.2, § 3.3, § 3.4 |
| 4 | **Re-cut P1 as one document, 7 pages.** `dsp-lctr1-…-plw.pdf` has no handwriting; its red pixels are an arrow. Re-allocate its share of the 12 P1 crops — the corpus has more P3 pages than P1 pages. | § 1, § 4 |
| 5 | **Drop the "twin control" requirement.** The 12 P1 twin re-runs can come from the OCG toggle on the single annotated file, IoU 1.0000 — and the standing control is then reproducible from one file. | § 4 |
| 6 | **Re-sweep `merge_px` and `min_pixels` per stratum** and log the chosen value with each crop, next to the gap. | § 5 |
| 7 | **Add a per-crop "ink retained" check to step 2** — composite ink pixels ÷ raw non-paper pixels — and eyeball any crop below ~0.5. It catches § 3.2 before 84 inferences are spent on eroded input. | § 3.2 |

**The honest residual risk.** The mask arm is constructible on every stratum, but P3's
handwriting-only *locator* rests on a chroma gap that one of its two documents nearly closes — 9 : 1 on
M17, unbounded on `Worked Problems`. The locator/paint split (§ 3.4) covers both files measured here;
it is **not** a demonstration that it covers a third. A P3 document written in *black* ballpoint would
defeat the colour route entirely, and P3's fallback is then P2's — geometry — which a flatbed scan does
not have. **If a P3 crop comes back suspect, check the region box before blaming the model.**

### Corpus scale, for sizing

459 documents / 7,198 pages scanned today (the corpus grew again from the 448 / 7,187 frame in
[./ground-truth-sample.md](./ground-truth-sample.md)). Pages carrying actual handwriting:

| Stratum | Document | Pages with ink |
| --- | --- | ---: |
| P1 | `cesc_410/lectures/f26_lctr02_DT signals and systems-plw.pdf` (red) | 7 of 10 |
| P1 | `cec_320/activities/pm-1-26-01.pdf` (**blue** PDF Annotator ink, also an OCG) | 1 of 1 |
| P2 | `cesc_410/lectures/f26_lctr03_LTI_systems_conv.pdf` | 7 of 8 |
| P3 | `ps160/midterm_01/Worked Problems.pdf` | 9 of 10 |
| P3 | `ps160/m17/M17 Review.pdf` | 6 of 6 |

**30 pages of handwriting in the whole corpus; 22 of them (73%) are P2 or P3.** § 4.1's "roughly two
thirds" is right and slightly understated. Two further PDF Annotator files
(`cec_315/.../hw-chapter01.pdf` and its duplicate) carry a layer that paints **white** — an eraser, no
ink — and one `Adobe Fill & Sign` OCG is empty. Neither is handwriting.

`cec_320/activities/pm-1-26-01.pdf` is worth naming separately: it is P1-shaped (PDF Annotator over a
born-digital PDF, OCG present) but the ink is **blue**, red-excess p50 = **−119**. `red_mask` returns
nothing on it. **`ink.py`'s hard-coded red thresholds work on exactly one document in this corpus.**
