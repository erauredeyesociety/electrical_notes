# The labelled ground-truth sample — what 161 read pages say about four open decisions

**Type: FINDING (internal).** Measured 2026-09-05 → 2026-09-06 against `content/`.
**Data:** [`tests/fixtures/ground_truth/sample.csv`](../../tests/fixtures/ground_truth/sample.csv) (the draw,
161 pages) · [`tests/fixtures/ground_truth/labels.csv`](../../tests/fixtures/ground_truth/labels.csv)
(the labels, 161 rows) · [`tests/fixtures/ground_truth/sample.py`](../../tests/fixtures/ground_truth/sample.py)
(build / draw / render).
**Answers:** [../scope.md](../scope.md) § Open decisions #3 · [../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) § 6, § 8
**Closes:** the "no labelled sample exists" half of S1 in [../scope.md](../scope.md) § Success.

> ⚠ [INDEX.md](./INDEX.md) was deliberately **not** touched — another agent holds that file. It needs one
> row for this document.

Nothing here ran a model, touched the GPU, or wrote to a source PDF. Two corpus passes, both `nice -n 10`,
17 s and 60 s.

---

## 0 · What was actually done, and how far to trust it

161 pages were rendered at 110 dpi and **read, one at a time, against the page's own extracted text layer
and the detector evidence for that page**. Every row carries a note that names the specific fragment that
was checked, so any call here can be re-checked without re-reading the page.

**One reader, no answer key.** These are one person's judgements. Where a call is genuinely arguable the
row says so in its note (idx 155 is the clearest), and § 3.1 reports the sensitivity. Every proportion
below carries a **Wilson 95% interval** — a precision estimate on 45 pages is a range, not a number, and
this document is written so that it cannot be read as a point value by accident.

### The label vocabulary

`labels.csv` columns, and the values the 161 rows actually use:

| Column | Values | Means |
| --- | --- | --- |
| `content` | 37 tags, e.g. `latex-math`, `slide-prose+figure`, `scan-prose`, `handwritten-math`, `vector-outlined-math` | what is physically on the page |
| `display_math` | `y` / `n` | is there a *displayed* equation (not just inline) |
| `text_verdict` | `all` / `most` / `some` / `none` | how much of the page's information the text layer holds |
| `needs_ocr` | `no` / `marginal` / `yes` | **the human call the density gate is scored against** |
| `math_state` | `none` / `intact` / `degraded` / `destroyed` / `absent` | `absent` = the maths is pixels; `destroyed` = present but the statement now reads false |
| `shred` | `genuine` / `genuine-wrong-evidence` / `partial` / `misfire` / `genuine-letter-spaced` / `na` | the precision call on a flagged page |
| `recall` | `ok` / `miss` / `miss-other` / `na` | the recall call on an unflagged page |

`shred` in detail — this is the load-bearing vocabulary for § 3:

- **`genuine`** — a flattened equation or symbolic table, and the *reported run is that equation*. Strict hit.
- **`genuine-wrong-evidence`** — the page really does carry flattened mathematics, but the run the detector
  printed is plot furniture or block-diagram labels. Strict hit, evidence wrong.
- **`partial`** — 2-D structure genuinely lost, and it is genuinely **not** mathematics: a decision tree, a
  traceability matrix, a figure axis. Broad hit, strict miss.
- **`misfire`** — nothing was lost; the run is a code gutter or similar. False positive.
- **`genuine-letter-spaced`** — the page was flagged by `letter-spaced`, not `shredded-lines`. Excluded
  from every `shredded-lines` figure below.

`recall`: **`ok`** = structure was at risk and survived (true negative); **`miss`** = flattened 2-D
mathematics the detector did not fire on (false negative); **`miss-other`** = structure lost in a way
*neither* shipped detector can see (an inline superscript flattened to a wrong number, a dropped
ligature); **`na`** = the question does not arise.

### Sample-wide shape

| | |
| --- | ---: |
| `needs_ocr` | no **115** · marginal **19** · yes **27** |
| `text_verdict` | all **40** · most **58** · some **45** · none **18** |
| `math_state` | none 90 · intact 7 · degraded 18 · **destroyed 36** · absent 10 |

**36 of 161 pages carry mathematics that the text layer turned into a false statement.** All 36 score
`ok` on the density axis. That is the defect `structure.py` exists for, and it is not rare.

### The frame these estimates are reweighted onto

Regenerated 2026-09-05: **7,187 pages / 448 documents** (the 2026-09-04 census counted 7,146 / 430; the
corpus grew).

| band | chars | pages | share |
| --- | --- | ---: | ---: |
| `d0_empty` | < 30 | 620 | 8.6% |
| `d1_thin` | 30–199 | 783 | 10.9% |
| `d2_below_gate` | 200–399 | 950 | 13.2% |
| `d3_above_gate` | 400–799 | 1,341 | 18.7% |
| `d4_dense` | ≥ 800 | 3,493 | 48.6% |

`verdict != ok` therefore routes **2,353 pages, 32.7% of the corpus** (1,733 `sparse` + 620 `empty`).
The 1,736 figure in [../scope.md](../scope.md) is the `sparse` band alone.

---

## 1 · Q1 — is 400 chars/page the right `sparse` gate?

**Estimator:** the 70 `Q1/d*` rows, drawn by simple random sample within band from the whole corpus, then
reweighted by the band populations above. `marginal` counts as half a page in the sweep.

### 1.1 The bands, read

| band | n | needs OCR | P(needs OCR) | 95% CI |
| --- | ---: | --- | ---: | --- |
| `d0_empty` (<30) | 8 | 7 yes, 0 marginal | **88%** | [53%, 98%] |
| `d1_thin` (30–199) | 10 | 4 yes, 1 marginal | **40%** | [17%, 69%] |
| `d2_below_gate` (200–399) | 22 | 3 yes, 4 marginal | **14%** | [5%, 33%] |
| `d3_above_gate` (400–799) | 22 | **0 yes**, 5 marginal | **0%** | [0%, 15%] |
| `d4_dense` (≥800) | 8 | 0 yes, 1 marginal | **0%** | [0%, 32%] |

### 1.2 The sweep

| gate | routed | % of corpus | wasted | missed | precision | recall |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 30 | 620 | 8.6% | 78 | 939 | 88% | 37% |
| 200 | 1,403 | 19.5% | 508 | 587 | 64% | 60% |
| **400 (today)** | **2,353** | **32.7%** | **1,242** | **371** | **47%** | **75%** |
| 800 | 3,694 | 51.4% | 2,431 | 218 | 34% | 85% |

### 1.3 What the sample actually settles

**Do not raise the gate.** `d3` is **0 of 22**, CI [0%, 15%]. Between 400 and 800 chars there is not one
page in the sample whose content is in pixels. Going to 800 would double the routed volume for a band the
sample says is empty of targets. **This is decided.**

**400 is defensible and expensive.** It buys 75% recall at 47% precision — a little over half of what it
routes is wasted. That is a real cost (1,242 pages of pointless model time) but not a wrong call.

**Moving the number *inside* [200, 400] is not supported, because character count carries no signal in
that band.** The 22 `d2` rows, sorted by density, with Y = needs OCR, m = marginal, . = no:

```
209.  218.  237.  238.  240.  249.  265.  267m 282m 286.  287.
296Y 311Y 319Y 327.  329m 350m 356.  358.  380.  382.  392.
```

The three genuine targets sit at **296, 311 and 319** — the middle of the band. The bottom of the band
(209, 218, 237) is three false alarms. Whatever separates a genuine target from a false alarm below 400
chars, it is not the char count, so a threshold move inside this band trades volume for recall along an
axis that does not exist.

### 1.4 The axis that does work — and it is nearly free

The variable that separates them is **how much of the page is pixels**. Over the 40 `Q1` rows below the
gate:

| sub-gate rows | n | needs OCR | P | 95% CI |
| --- | ---: | ---: | ---: | --- |
| image area ≥ 20% of the page | 22 | 12 yes, 5 marginal | **55%** | [35%, 73%] |
| image area < 20% | 18 | 2 yes, 0 marginal | **11%** | [3%, 33%] |

By `doc_class` it is the same story: `scanned` 8/10 yes, `slides` 6/26, `born-digital-latex` **0/4** — and
across the *whole* 161-row sample, `born-digital-latex` is **0 of 69** and `prose-pdf` **0 of 8**.

The image-area rule misses one class, and the sample contains it: **text converted to vector outlines**
has no image at all (idx 115, a full textbook page, image area 0.00, **502 drawings**). Adding a
drawings term catches it:

> **route a sub-gate page only if `image_area ≥ 0.20 × page_area` OR `len(page.get_cdrawings()) ≥ 40`**

| sub-gate rows | n | needs OCR | P | 95% CI |
| --- | ---: | ---: | ---: | --- |
| `Q1` rows, predicate says route | 25 | 13 yes, 5 marginal | 52% | [33%, 70%] |
| `Q1` rows, predicate says don't | 15 | **1** yes | **7%** | [1%, 30%] |
| all 62 sub-gate rows, route | 43 | 26 yes, 6 marginal | 60% | [46%, 74%] |
| all 62 sub-gate rows, don't | 19 | **1** yes | **5%** | [1%, 25%] |

Corpus effect, measured over all 7,187 pages: **2,353 routed → 1,689 (23.5%)**. It stops routing **664
pages** — 28% of the current OCR budget — while releasing one true target in roughly fourteen. Both
predicates are already computed by `sample.py`'s frame builder and cost no extra PDF read.

**Honesty about that last row:** 1/19 has a 95% upper bound of 25%. Nineteen pages cannot demonstrate a
false-negative rate below about 5%; they can only show it is not 50%. The single escape is idx 117, a
slide whose four bullets end "the average power is:" and whose answer is a 13%-area image.

### 1.5 Verdict on Q1

| | |
| --- | --- |
| **Is 400 right?** | It is not *wrong*, and it must not be raised. As a pure density threshold anything in [200, 400] is inside this sample's resolution. |
| **What it should be** | Keep 400 as the density axis. **Add a pixel-coverage predicate under it**, § 1.4. That is a bigger win (−664 pages, precision 35% → 52–60%) than any threshold move, and it is not a threshold question. |
| **Decision status** | **Unblocked in one direction** (do not raise; evidence is clean). **Open** on lowering to 200 — it saves 950 pages and costs ~130 true targets, and this sample cannot say whether that is the right trade; that is an operator preference, not a measurement. |

One thing the density axis cannot fix in either direction: **five of the 22 `d3` rows are `marginal`**
(idx 13, 14, 84, 122, 159) — pages whose prose is exact and whose *figures* carry twenty-plus labels that
exist only as pixels. Moving a char threshold cannot reach them; they need a figure-region test.

---

## 2 · Q2a — `shredded-lines` precision

**Estimator:** the 46 `Q2a/flagged` rows, a simple random sample of the 424 flagged pages in the corpus
(cap 3/document, which did not bind).

One of the 46 was flagged by `letter-spaced`, not `shredded-lines` (idx 101, the documented
`C o m p u t e r  O r g a n i z a t i o n` title slide — a true positive for its own detector). It is
excluded, leaving **45**.

| measure | count | rate | 95% CI |
| --- | ---: | ---: | --- |
| **strict precision** — flattened equation or symbolic table | 38/45 | **84%** | [71%, 92%] |
| **broad precision** — any real 2-D structural loss | 44/45 | **98%** | [88%, 100%] |
| **evidence also correct** — the reported run *is* the maths | 29/45 | **64%** | [50%, 77%] |
| **hard misfire** | 1/45 | **2%** | [0%, 12%] |

### 2.1 This confirms the plan's prior, on an independent draw

[../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) § 6 hand-labelled a *different*
40-page draw and reported **83% strict / 95% broad / 5% hard FP**. This draw lands at **84% / 98% / 2%**.
Two independent samples, same answer. The plan's number is no longer an estimate from one reader on one
draw; it now has a confirming replicate and an interval.

The single hard misfire is **idx 90**, `cec_320/summaries/cec32x-companion (2).pdf` p211 — a page of pure C
source with no mathematics anywhere. The run is `252 / // / 253 / v`: two `lstlisting` gutter numbers, a
comment marker, and the C variable `v`, which `_is_symbolic` accepts as "a lone variable". Symbolic ratio
exactly **0.25**, right on the threshold. Three larger runs on the same page (`201 / } / 202 / } …`) score
0.00 and were correctly rejected — the numeral rejection is doing its job, and the escape is the
single-ASCII-letter clause, not the numeral clause.

### 2.2 The finding the plan does not have — evidence correctness

**On 9 of 45 flagged pages the verdict is right and the printed evidence is wrong** (idx 45, 47, 52, 53,
57, 59, 62, 64, 66). The page genuinely carries destroyed mathematics, but the run `shredded_run()`
returns — the *first* run to clear 25% symbolic — is a plot's axis ticks (`−π / −π/2 / π/2 / π`) or a
pole-zero diagram's labels, while the flattened equation is elsewhere on the page.

This matters more than its size suggests, because the plan's central design argument is *"a reader who
cannot see the evidence cannot check the call."* **One reviewer in three who checks the detail will see a
run that looks like a misfire and conclude the detector is wrong when it is right.** Reported here, not
fixed — the obvious remedy (return the *most* symbolic run rather than the first) is a code change, and
`src/` is not this document's to touch.

### 2.3 The six `partial` rows — what "broad" is buying

idx 65 (a rectangular-pulse figure's axis labels), 139 and 141 (a decision tree flattened to a bag of node
names), 153 (INCOSE Figure D.1, a 34×34 traceability matrix arriving as **123 consecutive lines of `X`**),
157 (NASA Figure G-6, the TRL assessment matrix), and 155.

**idx 155 is the arguable one and is flagged as such in its row.** Its run is `C / o / n / t / r / o / l` —
the vertically rotated label on the NASA CRM cycle wheel, one glyph per line, exactly the case
[the plan](../plans/structural-faithfulness.md) § 3.1 names as its known cost and § 8 lists as open
question 3. The corruption is real (the word is unusable and unsearchable) but it is rotated text, not a
flattened 2-D layout, and the page carries no mathematics. Counted as a broad hit here. **Counting it as a
misfire instead moves hard-FP from 1/45 to 2/45 (2% → 4%) and broad precision from 98% to 96%** — neither
changes any decision.

---

## 3 · Q2b — `shredded-lines` recall, measured for the first time

**Estimator:** the 30 `Q2b/unflagged-math` rows — a simple random sample of the **3,230** corpus pages
that are *unflagged*, in a mathematics-bearing course, and carry ≥ 200 chars (enough text to have held an
equation). This stratum exists because the prior 40-page sample was drawn from flagged pages only and
therefore **could not see a miss**.

| | count | rate | 95% CI |
| --- | ---: | ---: | --- |
| unflagged math-course pages that carry flattened display mathematics | 6/30 | **20%** | [10%, 37%] |
| …of the 7 such pages that carry **any** display mathematics | **6/7** | **86%** | [49%, 97%] |

The six: idx 1, 4 (AE318 slides — inline fractions flattened *and* spliced mid-sentence), 44
(Euler identities), 50 (partial fractions), 54 (`dx/dt`, `d²x/dt²`), 94 (fourteen displayed trig
identities, every `π/2` split). The one hit, idx 124, is a page whose display maths is all single-line —
there was nothing to flatten.

**Reweighted onto the corpus:**

```
TP  ≈ 424 flagged  × 0.84 strict precision  ≈ 358
FN  ≈ 3,230 eligible × 0.20 miss rate       ≈ 646
recall ≈ 358 / (358 + 646) ≈ 36%     crude interval from the two CIs: [20%, 56%]
```

**Read 36% as an upper bound.** The `Q2b` frame excludes non-mathematics courses and every page under 200
chars, and both certainly contain further misses — idx 67 is one, a `d1_thin` page whose entire content is
one boxed Z-transform pair with its fraction bar gone. Counting every `recall = miss` row anywhere in the
161 (12 rows: idx 1, 2, 4, 40, 44, 48, 50, 54, 67, 68, 94, 133) corroborates the direction but is not a
clean estimator, because those rows come from a density-banded draw.

### 3.1 Why recall is this low, mechanically

It is the design, not a bug, and the misses share one shape: **a flattened fraction produces two or three
short lines, and `_SHRED_MIN_RUN = 4` needs four.** `Σ` extracted as `X` with `k=0` beneath it is a run of
three.

> ⚠ **Half of this was wrong, measured 2026-09-06** —
> [recall-was-a-symbol-test-not-a-run-length.md](./recall-was-a-symbol-test-not-a-run-length.md) § 1.
> Taking these 12 `miss` rows mechanically, lowering `_SHRED_MIN_RUN` to 3 reaches **one** of them and to
> 2 reaches **five**. The other seven are blocked by `_SHRED_MAX_CHARS`, not by the run length — including
> **idx 133 below**, which has no run of ≤4-character lines longer than *one* and does not fire at 4, 3
> **or 2**. The paragraph after this one is therefore right about the shape and wrong about the constant.
> `_SHRED_MIN_RUN` is now 2, behind a rule that every run carry a genuine mathematical character; the
> resulting precision/recall is 93% / 68%, and three of these twelve rows (idx 1, 50, 68) are closed. `3 / s + 2 ,` is a run of one, because the denominator line carries the ROC and is seven characters.

The sharpest single case is **idx 133**, `stat_412/HW08/solutions/q16.pdf`: `χ² = Σ(O−E)²/E = 22.22`
arrives as `chi2 =` / `sum(O -E)2` / `E` / `= 22.22,` and **does not fire** — while the plan's § 3.2 sweep
cites `stat_412/QZ08/solutions/q06.pdf` firing on the *same formula* as the true positive that justified
`_SHRED_MAX_CHARS = 4`. Whether that formula is caught depends on how long the neighbouring line happens
to be.

### 3.2 Verdict on Q2

| | |
| --- | --- |
| **Precision** | **84% strict [71, 92]**, **98% broad [88, 100]**, hard FP **2% [0, 12]**. Confirmed against an independent prior draw. **Unblocked.** |
| **Recall** | **≈ 36%, interval [20%, 56%], and that is an upper bound.** Conditional on an unflagged maths page actually carrying displayed mathematics, the detector misses it about **six times in seven**. **Now measured; previously only estimated.** |
| **What it means** | `shredded-lines` is a high-precision *sampler* of broken pages, not a *census* of them. Anything that reads `structure-intact` as "this document's maths is fine" is wrong: the sample says roughly two thirds of the broken pages are not flagged. Whether to trade precision for recall is now a real decision with numbers behind it, and it is **open** — it is a product call, not a measurement. |

---

## 4 · Q3 — RapidOCR vs OCRmyPDF on scanned pages

### 4.1 This session cannot settle it, and says so

No OCR engine was run. The task forbids models and inference; the ERAU VPN and `pwnstar` are down. This
document therefore has **nothing to say about which engine is more accurate**, and any number it invented
would be worse than the two that already disagree.

### 4.2 But it explains why the two prior agents disagreed

They measured **different single pages**, and the sample shows that `Q3/scanned` is not one population. Its
16 rows are at least five physically different things:

| what the page actually is | rows | can a printed-OCR engine read it? |
| --- | ---: | --- |
| **raster scan or pasted raster screenshot** | 5 (idx 7, 15, 111, 114, 121) | yes — this is the case the head-to-head is about |
| **born-digital slide whose whole content is one raster diagram** | 2 (idx 19, 31 — byte-identical duplicates) | yes |
| **born-digital text converted to vector outlines** | 2 (idx 112, 116) | yes, and it is the *easiest possible input* — see below |
| **handwriting** | 3 (idx 97, 98, 129) | **no.** Neither RapidOCR nor OCRmyPDF/Tesseract does handwriting |
| **ordinary born-digital slide, text layer fine** | 4 (idx 16, 18, 30, 32) | not an OCR page at all — `_doc_class` misfiled the document |

**A head-to-head that draws its pages from `doc_class == "scanned"` is measuring a mixture.** Score it on
idx 121 (a crisp 1076×513 Canvas screenshot) and both engines will look excellent; score it on idx 129 (a
3300×2550 flatbed scan of an exam a student wrote on in blue biro) and both will look terrible, because
half that page is handwriting. That is enough to produce two contradictory conclusions from two honest
agents, with no disagreement about the engines at all.

### 4.3 The finding that reshapes the question: ps160's "scans" are not scans

`ps160/m14/M14_textbook_chapter.pdf` and `ps160/m15/M15_Textbook_chapter.pdf` are classified `scanned` and
report 0–27 chars per page. They are **born-digital pages whose glyphs were converted to vector outlines**.
Measured directly:

| page | fonts | images | drawings | line/curve items |
| --- | --- | ---: | ---: | ---: |
| idx 112 · M14 p27 | `CIDFont+F1/F2`, Identity-H, no usable ToUnicode | 6 (rules and icons) | 535 | 155,776 |
| idx 115 · M15 p22 | **none** | **0** | 502 | 100,884 |
| idx 116 · M15 p23 | one | 1 (a rule) | 713 | 117,885 |

There is no scanner noise, no skew, no JPEG artefact and no resolution ceiling. Rendering these at any DPI
gives **pristine synthetic printed type** — the best input either engine will ever be handed. Any
head-to-head that includes them and calls the result "scanned-page accuracy" is reporting a number about a
population that does not exist elsewhere in the corpus.

### 4.4 What the sample contributes to the eventual head-to-head

**A written answer key for 14 pages**, recorded verbatim in the `note` column and prefixed `Q3 KEY`:

idx 7, 15, 17, 19, 24, 111, 112, 114, 115, 116, 121, 123, 129, 130.

They span the range deliberately: two clean screenshots (114, 121), two full vector-outlined textbook
pages with display equations (115, 116), two real flatbed scans with handwriting (129, 130 — and **idx 128
is 129's born-digital twin**, the same exam page before a student wrote on it, which isolates exactly what
a printed-OCR engine can and cannot add), a CamScanner textbook page (7), a labelled slant-range diagram
with no text layer at all (19), and a callout-heavy map (24).

Two traps a fair evaluation must not skip: **idx 116's boxed ANSWER paragraph is printed upside down**, and
**idx 121's whole difficulty is superscripts** (`10⁻⁵`, `m³`, `K⁻¹`, `(kC°)⁻¹`).

### 4.5 Verdict on Q3

| | |
| --- | --- |
| **Which engine wins?** | **Not settled here, and not settleable here.** No engine was run. |
| **What changed** | The evaluation *set* is now defined and keyed. The head-to-head must be scored **per page class**, not over `doc_class == "scanned"`, and must exclude the three handwriting pages or report them separately. |
| **Decision status** | **Still open**, but no longer blocked on "which pages do we test?" — it is blocked only on running the two engines, which needs a session that is allowed to. |

---

## 5 · Q4 — does the `ink.py` mask improve equation OCR?

**Out of scope for this session, as the task anticipated:** answering it requires running UniMERNet (or a
peer) twice per crop, which is model inference on a GPU.

It is also **already partly answered elsewhere, by measurement**, and this document should not be read as
re-opening it: [../plans/mask-first-crops.md](../plans/mask-first-crops.md) § 2 records the same model, same
box, same padding, raw pixels vs composited — `expo` `e^{iwo})^{n}=e^{\frac12 woh}` → `e^{iw_0})^{n}=e^{iw_0 r}`
(a hallucinated fraction bar, read off the slide's graph-paper grid, disappears), and `eqline` three errors
→ one. § 2.1 records the counter-test that `paint = red only` is destructive.

**What this sample can add, and it is mostly a warning about scope:**

- **The sample contains 5 pages with handwriting** (idx 96, 97, 98, 129, 130); **4 of them carry displayed
  mathematics**. So the ink + equation combination is 3.1% of a 161-page corpus-wide draw.
- **It contains zero `-plw` pages.** The two annotated-lecture documents `ink.py` was built for —
  `content/cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` and
  `f26_lctr02_DT signals and systems-plw.pdf` — hold **22 pages between them** (5 flagged `suspect`,
  11 under 400 chars). At 22/7,187 the probability that a 161-page stratified draw hits one is small, and
  it did not.
- **Therefore a corpus-wide sample is the wrong instrument for this question.** 22 pages in 2 documents is
  not a population to sample; it is a population to enumerate. The right next step is a 22-page census of
  those two files, not another draw.
- The 3 handwriting pages that *are* here (`cesc_410/lectures/f26_lctr03_LTI_systems_conv.pdf` pp. 3, 4, 8)
  are a **different** artefact: OneNote exports where the typed bullets are in the text layer and all the
  mathematics is ink on graph paper. If a second ink fixture is ever wanted, that is where one is.

**Decision status: still open, correctly.** The sample contributes the population count (22 pages, 2
documents) and the observation that this question does not belong to the corpus sample at all.

---

## 6 · Three things nobody asked about, found by reading the pages

Recorded because they are cheap to lose and expensive to re-find.

### 6.1 A whole document silently loses its `ti` ligature — invisible to both detectors

`syse_301/homework/hw3/letters_to_my_younger_self.pdf` (idx 159, 160) scores `ok` and `intact`. The page
renders **"Letters"**, **"often"**, **"anticipate"**, **"appreciation"**, **"situations"**, **"executive"**.
The text layer says **`Le(ers`**, **`o$en`**, **`ancipate`**, **`appreciaon`**, **`situaons`**, **`execuve`**.

Roughly one word in twenty-five is silently wrong. No run forms, no letter spacing, and the damage is
*inside* words, so `structure.py` cannot see it and neither can a character count. It is also the one case
in the sample where **the pixels are more faithful than the bytes** — a rendered OCR pass would beat the
text layer here — which cuts against the otherwise-sound rule that OCR is never the repair for a present
text layer. Labelled `recall = miss-other`, `needs_ocr = marginal`.

### 6.2 Rotated PowerPoint text can be absent from the text layer entirely

`sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` pp. 31 and 35 (idx 139,
141). Verified with `get_text("dict")`: **all 40 extracted lines have direction `(1.0, 0.0)`.** Every
rotated label on the decision tree — `Do seismic survey`, `Unfavorable`, `Favorable`, `No seismic survey`,
`Drill`, `Sell`, `-$30,000`, `0.70`, `0.30`, `-$100,000`, `$90,000` — exists only as vector outlines and is
simply not there.

These are the **only two slide pages in the whole sample where `sparse` is unambiguously the right call and
OCR is unambiguously the right repair.** Every other sub-gate slide page was a false alarm.

### 6.3 Inline superscript flattening is a silent numeric error class

Six rows (idx 21, 63, 104, 122, 159, 160) are `recall = miss-other`. Two are arithmetic:
`2.35 × 10⁴ chips` → `2.35 𝑥 104` (wrong by 10³, idx 21) and `7.50 × 10³ Pa` → `103 Pa` (wrong by 10², idx
122). No line break, no run, no letter spacing — **neither shipped detector can see any of them**, and a
third detector for this class would be a different shape from both.

---

## 7 · Decision status, in one table

| # | Question | Answer | Confidence | Status |
| --- | --- | --- | --- | --- |
| **Q1** | Is 400 the right `sparse` gate? | Do **not** raise it: `d3` is 0/22 [0, 15%]. 400 gives 47% precision / 75% recall over 32.7% of the corpus. Inside [200, 400] the char count carries no signal. The real win is a pixel-coverage predicate under the gate: **−664 pages (−28%), precision 35% → 52–60%**. | Bands n = 8–22; every rate has a CI. The predicate's escape rate (1/19) is bounded only to 25%. | **Partly unblocked** — "do not raise" is decided; lowering to 200 remains an operator preference. |
| **Q2a** | `shredded-lines` precision? | **84% strict [71, 92]**, **98% broad [88, 100]**, hard FP **2% [0, 12]**. Independently confirms the plan's 83/95/5. New: **evidence is correct on only 64% [50, 77]**. | n = 45, two independent samples agreeing. | **Unblocked.** |
| **Q2b** | `shredded-lines` recall? | **≈ 36%, [20%, 56%], upper bound.** Conditional on displayed mathematics being present on an unflagged page, **6 misses in 7**. | n = 30 (7 with display maths). Wide, and directionally certain. | **Measured for the first time.** Whether to trade precision for recall is now a real, open product decision. |
| **Q3** | RapidOCR vs OCRmyPDF? | **Cannot be settled here — no engine was run.** But the disagreement is explained: `Q3/scanned` is ≥ 5 different page kinds, including 3 handwriting pages neither engine can read and 2 vector-outlined pages that are not scans at all. 14 pages now carry a written key. | The taxonomy is verified page by page; the engine question is untouched. | **Open**, but the evaluation set is defined. |
| **Q4** | Does the `ink.py` mask help equation OCR? | **Out of scope — needs a model run.** Partly answered already in [mask-first-crops.md](../plans/mask-first-crops.md) § 2. The sample adds: 5 handwriting pages (4 with display maths), **0 `-plw` pages**, and the observation that the `-plw` population is 22 pages in 2 documents and should be **enumerated, not sampled**. | n/a | **Open**, correctly, and not a sampling question. |

---

## 8 · Reproducing this

```bash
cd ~/electrical_notes/ocr_handler
# frame is regenerated, never committed (~7,200 rows, a pure function of the corpus)
nice -n 10 .venv/bin/python tests/fixtures/ground_truth/sample.py build-frame
nice -n 10 .venv/bin/python tests/fixtures/ground_truth/sample.py draw --seed 20260905   # -> sample.csv
nice -n 10 .venv/bin/python tests/fixtures/ground_truth/sample.py render                 # -> tmp/ground_truth/renders/
```

`labels.csv` is the human half and cannot be regenerated. Every row's `note` names the exact fragment that
was checked, so any single call can be re-verified by opening that page's render and its extracted text —
that is the point of writing the evidence down rather than the verdict alone.

---

**See also:** [../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) ·
[../plans/mask-first-crops.md](../plans/mask-first-crops.md) ·
[corpus-census-2026-09-04.md](./corpus-census-2026-09-04.md) ·
[layout-mode-decides-whether-math-survives.md](./layout-mode-decides-whether-math-survives.md) ·
[../scope.md](../scope.md) § Open decisions
