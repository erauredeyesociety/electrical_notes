# Recall was a symbol test, not a run length — `shredded-lines` at 93% / 68%

**Type: FINDING (internal).** Measured 2026-09-06 against `content/` —
**459 documents / 7,198 pages** (the 2026-09-05 frame counted 448 / 7,187; the corpus grew).
**Answers:** [ground-truth-sample.md](./ground-truth-sample.md) § 3.2 "whether to trade precision for
recall … is **open**" · [../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) § 8
open questions 2 and 3.
**Changes:** `src/ocr_handler/structure.py` — `_SHRED_MIN_RUN` 4 → 2, and a new `_is_strong` gate.
**New hand labels:** [`tests/fixtures/ground_truth/shred_sweep_labels.csv`](../../tests/fixtures/ground_truth/shred_sweep_labels.csv)
— 75 pages, drawn at random from the corpus increment each sweep step adds, read at 110 dpi against
their own extracted text. Every row names the page and the run that was judged, so any call here can be
re-checked without re-drawing.

Nothing here ran a model or touched the GPU. Three `nice -n 19` corpus passes: 19 s, 22 s, 58 s.

---

## 0 · The headline

|  | before | after |
| --- | ---: | ---: |
| `shredded-lines` pages / documents | 416 / 115 | **732 / 162** |
| strict precision — a flattened equation or symbolic table | 84.8% [72, 92] | **93.1% [85, 96]** |
| broad precision — any real 2-D structural loss | 97.8% | 95.2% |
| estimated true positives corpus-wide | 353 | **681** |
| recall against a fixed broken-page pool of 999 | 35.3% | **68.2%** |
| suspect pages, all four detectors | 774 (10.8%) | 959 (13.3%) ⚠ **remeasured 956** — see note below |
| whole-corpus pass | 22 s | 22 s |

**Recall nearly doubled and precision went up.** That is not the trade the task expected, and the reason
is the second half of the change: **the run length was never the binding constraint — the symbol test
was.** Lowering `_SHRED_MIN_RUN` to 2 on its own takes strict precision from 85% to 59%. Requiring that
every run carry at least one genuine *mathematical character* pays for the whole reduction and then some.

---

## 1 · The hypothesis, and where it was wrong

Inherited from [ground-truth-sample.md](./ground-truth-sample.md) § 3.1:

> It is the design, not a bug, and the misses share one shape: **a flattened fraction produces two or
> three short lines, and `_SHRED_MIN_RUN = 4` needs four.**

**Half true, and the half that is false matters.** Taking the 12 hand-labelled `recall = miss` rows and
asking, mechanically, what blocks each:

| lowering `_SHRED_MIN_RUN` to | of the 12 misses, now caught |
| ---: | ---: |
| 3 | **1** (idx 48) |
| 2 | **5** (idx 1, 40, 48, 50, 68) |

Seven of the twelve are not reachable by any run length, because their longest run of ≤4-character lines
is **one or two lines** and the qualifying run is often zero. The blocker on those is `_SHRED_MAX_CHARS`,
not `_SHRED_MIN_RUN`: the denominator carries the ROC or a unit and is 5–8 characters long.

**The sharpest case the finding names is the clearest example of this.** idx 133,
`stat_412/HW08/solutions/q16.pdf`, `χ² = Σ(O−E)²/E = 22.22` arrives as

```
χ2 =            4 chars
∑(O −E)2        8 chars   <-- breaks the run here, and at every run length
E               1 char
= 22.22,        8 chars
```

No run of ≤4-character lines longer than **one** exists on that page. It does not fire at
`_SHRED_MIN_RUN` of 4, 3 **or 2**, with or without any qualifier tested here. It was cited as the case
that lowering the run length would reach; it is not.

Priced so nobody re-derives it: with the strong rule of § 3, `_SHRED_MAX_CHARS` 4 → 8 costs **+232
corpus pages** and recovers **4 more of the 12 misses**. That increment has not been hand-labelled and
so is **not** shipped — see § 7.

---

## 2 · The sweep, and how the increment was measured

The labelled sample cannot score a sweep on its own: 46 of its 161 rows were drawn *because* they were
flagged at `_SHRED_MIN_RUN = 4`, and only 30 rows sample the unflagged-mathematics stratum. Lowering the
constant creates a **new population** the sample has almost no rows in. So each step's increment was
enumerated corpus-wide and then sampled and read:

| stratum | what it is | size | drawn and read |
| --- | --- | ---: | ---: |
| **A** | pages the shipped setting flags | 416 | 46 (the `Q2a` rows of the ground-truth sample) |
| **B** | pages `_SHRED_MIN_RUN` 4 → 3 adds | 261 | **30** |
| **C** | pages `_SHRED_MIN_RUN` 3 → 2 adds | 536 | **25**, plus **20** more inside C ∩ strong |

Precision at a setting is the population-weighted mean of the three strata's hit rates, over whichever
strata that setting actually flags. Recall is `TP / 999`, where 999 = 353 + 646 is the ground-truth
sample's own estimate of the broken-page pool (`TP` + `FN` at the shipped setting), **held fixed** so
every row of the table below is comparable. It inherits that sample's caveat exactly: 999 is a lower
bound on the true population, so every recall figure here is an upper bound.

### 2.1 The increments, read

| increment | n | strict | 95% CI | what the misses are |
| --- | ---: | ---: | --- | --- |
| **B**, `_SHRED_MIN_RUN` 4 → 3 | 30 | **83%** | [66, 93] | 5 misfires: 3 Wingdings bullet columns, 1 assembly gutter, 1 map legend |
| **C**, `_SHRED_MIN_RUN` 3 → 2 | 25 | **28%** | [14, 48] | 17 misfires: **10** Wingdings bullet columns, 5 code gutters, 1 exam answer blank, 1 page whose maths is pixels |
| **C ∩ strong** | 20 | **85%** | [64, 95] | 2 misfires, both the same map legend |

Going 4 → 3 costs essentially nothing: the pages it adds are `∞ / X / k=−∞` (a summation whose Σ arrived
as `X`), `B1 / s−p, / B2` (partial fractions), `10, / 𝑥≥5, / 2𝑥,` (a `cases` brace), `𝑡𝑛 / 𝑛! / 𝑠𝑛+1` (a
Laplace-transform table row). Going 3 → 2 without a qualifier is exactly the trade the plan warned about.

### 2.2 The full table

Corpus-wide volume, reweighted precision, and estimated true positives:

| setting | pages | A/B/C | labelled | strict P | broad P | TP | recall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `min_run` 4 — **the shipped setting** | 416 | 416/0/0 | 46 | 84.8% | 97.8% | 353 | 35.3% |
| `min_run` 3 | 677 | 416/261/0 | 76 | 84.2% | 92.2% | 570 | 57.1% |
| `min_run` 2 | 1,213 | 416/261/536 | 101 | **59.4%** | 65.6% | 720 | 72.1% |
| `min_run` 4 + strong | 319 | 319/0/0 | 40 | 97.5% | 100% | 311 | 31.1% |
| `min_run` 3 + strong | 527 | 337/190/0 | 65 | 97.0% | 98.6% | 511 | 51.1% |
| **`min_run` 2 + strong — shipped** | **732** | 342/199/191 | **93** | **93.1%** | 95.2% | **681** | **68.2%** |
| `min_run` 2 + strong + distinct | 570 | 321/168/81 | 70 | 98.6% | 100% | 562 | 56.2% |
| `min_run` 2 + distinct only | 681 | 372/192/117 | 67 | 94.8% | 100% | 646 | 64.6% |

The CI column is dropped here because it would be misread: the Wilson interval is computed on the
*unweighted pooled* labelled rows and the point estimate is stratum-reweighted, so the two are not the
same quantity. For the shipped setting they are 93.1% (weighted) and [85%, 96%] (pooled, n = 93); read
the interval as a width, not as a confidence set for the point.

**`min_run 2 + strong` is the only row that beats the shipped setting on both axes.** `strong&distinct`
buys 5 more points of precision for 119 fewer true positives; `distinct` alone is dominated.

---

## 3 · What `_is_strong` is, and why it is the load-bearing half

`_is_symbolic` accepts a line three ways: it contains a character from a mathematical range; **or** it is
a single ASCII letter ("a lone variable: u, v, X, i"); **or** it contains an `=`. The last two are
fallbacks, and they are exactly what the two commonest false-positive classes look like:

```
z / z                 a Wingdings list bullet that maps to ASCII `z`, twice per wrapped
                      bullet -- 10 of the 25 sampled C-stratum pages, all one document
16 / 17 / b           an assembly listing's line-number gutter and the `b` branch opcode
14 / =                a C operator-precedence table
```

The rule shipped is: **every run must contain at least one line that is symbolic by a *character*.** The
ratio gate is unchanged and still does its own job — at `_SHRED_MIN_RUN = 2` a 25% threshold means "at
least one line of two", which is nearly vacuous, so without `_is_strong` the run length could not have
been lowered at all. Two gates, two different false-positive classes: the ratio rejects a long numeric
gutter, `_is_strong` rejects a short column of bare letters.

### 3.1 What it costs, measured rather than asserted

Of the 46 labelled pages the shipped detector flags, `_is_strong` drops **6**, and the composition is the
whole argument: **5 `partial` and 1 `misfire`, and no strict hit at all.**

| dropped | what it was |
| --- | --- |
| idx 90 | the ground-truth sample's single **hard false positive** — `252 / // / 253 / v`, a C listing's gutter |
| idx 139, 141 | a PowerPoint decision tree flattened to a bag of node names |
| idx 153, 157 | INCOSE Figure D.1 and NASA Figure G-6 — traceability matrices arriving as 123 consecutive lines of `X` |
| idx 155 | the rotated `C / o / n / t / r / o / l` label — **still suspect**, now under `vertical-letter-spaced` |

**This is a real loss and it is not mathematics.** Broad precision falls 98% → 95%, and the ~46 corpus
pages of that class (13% of 416, less the one the vertical detector keeps) now fire on nothing. The
`partial` class was never what the detector is for — [the plan](../plans/structural-faithfulness.md)
§ 3.2 describes it as "a matrix, a stacked fraction, a `cases` brace" — but a 34×34 traceability matrix
flattened to 123 lines of `X` is a genuine flattening and it is now invisible. Recorded, not hidden.

A **long-run escape** was measured as a way to keep it — "admit any run of ≥ N lines regardless of
`_is_strong`" — and **rejected**: over N ∈ {8, 10, 12, 16, 20, 24, 32} it recovers at most 6 corpus pages
and *lowers* strict precision to 92.0%. It buys the wrong pages.

A **third tier for `=`** was measured and rejected: admitting a bare `=` line as strong takes precision
93.1% → 85.4% for two estimated true positives, because a C operator-precedence table is a column of
`13` / `? :` / `14` / `=`.

### 3.2 On the labelled sample, page by page

Running the shipped code over all 161 ground-truth rows, exactly three pages gain the signal and six lose
it:

- **gained:** idx 1, 50, 68 — **all three are `recall = miss`**, i.e. three of the twelve known false
  negatives closed. idx 50 is `X(s) = 3/(s+2) − 2/(s+5)`; idx 68 is `H(j3) = 4/25 − j(3/25)` arriving as
  `= 4` / `25 −j 3` / `25`, an arithmetic statement that now reads false.
- **lost:** the six of § 3.1 — one hard misfire and five broad-only hits.

**No strict true positive in the sample was lost.**

> ### ⚠ CORRECTED 2026-09-06 — true of the sample, **false corpus-wide**
>
> An independent replication enumerated the drop rather than reweighting the sample: the change
> orphans **66 pages** (74 dropped, 8 retained by another detector), not the ~46 estimated here. A
> seeded 20-page read of those 66 found **35% [18, 57] are flattened mathematics** — `Σ_{k=0}^{N} a_k dᵏy/dtᵏ`,
> `v_rms = √(3kT/m)`, `W = ∫p dV`, a 3×3 matrix product. Extrapolated: **~23 corpus pages of real
> loss** [12, 37]. The sentence above is a statement about 161 labelled pages and does not generalise.
>
> **Root cause, and it is structural:** `_is_strong` is blind in the direction of its own target. When
> a fraction flattens, the font often mangles the operator too — `∫`→`Z`, `√`→`r`, `Σ`→`X`, `∏`→`Q` —
> leaving **no mathematical character on the page at all**, so the rule that pays for `min_run 2`
> cannot fire on exactly the pages it most wants. Verified: a run of `Z / p / dV` fires nothing.
>
> The change still stands on net — ~328 true positives gained against ~23 lost — but "no cost" is not
> the claim to carry forward.
> Full audit: [precision-replicates-the-priced-cost-does-not-2026-09-06.md](./precision-replicates-the-priced-cost-does-not-2026-09-06.md)

---

## 4 · Two inherited claims that do not survive re-measurement

### 4.1 The "control corpus" is not a control corpus

[The plan](../plans/structural-faithfulness.md) § 3.2 sweeps `_SHRED_MAX_CHARS` against "all of
`cesc_470`, `cec_320`, `stat_412`: 156 documents, 1,475 pages, **none of which should fire**".

That premise is false, and it biased the sweep it decided. At the shipped setting those courses now
produce 49 flagged pages, and **44 of them are real**:

```
cec_320  hw11        10, / 𝑥≥5, / 2𝑥,        a `cases` brace
cec_320  lab09       𝑛 / ∑︁ / 𝑖=1             a summation with limits
cec_320  summaries   𝑓S = / 𝑓CNT             a flattened fraction
cesc_470 hw01 p09    | / {z / } / IC / × / h  an `\underbrace`
cesc_470 hw01 p10    n→∞ / 1                  a limit
```

`cec_320` is a mixed C-and-assembly course whose lecture notes are set in LaTeX and full of summations
and `cases`; `stat_412`'s solutions are worked algebra. The five that are not real are one C
operator-precedence table (appearing in five duplicate PDFs) and one page-number glyph. Counting these
as false positives is what made `_SHRED_MAX_CHARS = 5` look like it "multiplies control documents by 7".
**Any future sweep of that constant needs a drawn-and-read increment, not this corpus.**

### 4.2 The unmapped-glyph detector's raw volume is 6× what the plan records

[The plan](../plans/structural-faithfulness.md) § 4.3 records the raw signal as firing on "54 documents /
235 pages". Re-measured over the same definition the shipped code uses — Private-Use Area plus C0
controls, excluding tab and newline — it is **1,406 pages / 130 documents**. No obvious variant
reproduces 235/54 (PUA alone gives 1,053/70; C0 alone 374/69; a ≥5-per-page threshold 361/76). The
benign list silences **901 pages**, leaving **505 pages / 118 documents**, which is what ships.

---

## 5 · The three items the task asked about, verified rather than assumed

Detectors 3 and 4 were **already shipped** in `structure.py` when this session started, by a concurrent
session. Their headline measurements were re-derived here independently; all of the following reproduce
**exactly**.

### 5.1 `unmapped-glyphs` and its benign list — verified, and it closes a fifth defect

89 distinct unmapped code points in the corpus. The top of the frequency ranking, re-counted:

| code point | count | pages | the shipped call |
| --- | ---: | ---: | --- |
| U+F0B7 | 1,514 | 164 | benign — SymbolMT bullet |
| U+0017 | 1,437 | 89 | signal — the `ti` ligature |
| U+F070 | 1,016 | 424 | benign — Wingdings square/triangle |
| U+F06C | 366 | 357 | benign — Wingdings round bullet |
| U+F8F4 | 344 | 37 | signal — CMEX10 `\left\{` extension |
| U+0001 | 186 | 103 | signal — CMEX10 big `\left(` |

Every count matches the shipped comment. The one claim **not** independently verified here is the font
attribution ("28 Symbol-font λ and π occurrences against 2,868 Wingdings bullets"), which needs per-span
font inspection; it is taken on the peer session's measurement.

**And it closes the `ti`-ligature defect.** [ground-truth-sample.md](./ground-truth-sample.md) § 6.1
reports `syse_301/homework/hw3/letters_to_my_younger_self.pdf` losing its `ti` ligature invisibly —
"`anticipate` → `ancipate` … `structure.py` cannot see it". The ligature is **not dropped**: it is
extracted as **U+0017**, and `unmapped-glyphs` fires on **89 of that document's 92 pages**, including
both hand-labelled rows (idx 159, 160). What was true of two detectors is not true of four.

### 5.2 `vertical-letter-spaced` — verified, and it became independent this session

The run-length sweep in its comment reproduces exactly: over `_VERT_MIN_RUN` ∈ {4, 5, 6, 7, 8, 10} the
detector flags **6 / 5 / 4 / 4 / 4 / 2** pages, and at 6 the surviving words are precisely `Analyze`,
`Control`, `Enginee`, `Identify`, `Management`, `Operation`, `Sustaining`, `System` — one document, four
pages. The raw run test with no word filter flags 26 pages, 22 of them not words, as recorded.

Its docstring said it "adds NO page … a strict subset of `shredded-lines`". **That is no longer true, and
this session's change is what made it untrue.** A column of lone ASCII letters carries no strong
character, so `shredded-lines` now correctly declines it, and all **four** of the vertical detector's
pages are pages it is the only signal on. It went from naming to evidence without being touched. A
regression test asserts this, because if `shredded-lines` ever reclaims those pages the lone-letter
escape has come back.

---

## 6 · The three extraction defects — assessed, one closed, one specified, one out of scope

### 6.1 The dropped `ti` ligature — **already caught**, see § 5.1

The residual damage on that document is a *different* class and is not caught: `tt` → `(` and `ft` → `$`
(`Le(ers`, `so$ware`, `unfe(ered`). A mid-word-punctuation regex was measured as a candidate:

| pattern | pages | documents |
| --- | ---: | ---: |
| `[a-z]\$[a-z]` | 38 | **1** — that document, and nothing else |
| `[a-z]\([a-z]` | 1,208 | 199 — every `x(t)`, `H(jω)`, `f(x)` in the corpus |

The `$` form is perfectly precise and **not worth shipping**: it reaches 38 pages of a document that
`unmapped-glyphs` already flags on 89. The `(` form is unusable. **Rejected as subsumed.**

### 6.2 Rotated PowerPoint text absent from the text layer — **not a faithfulness signal at all**

`sys_304/…/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` pp. 31, 35: every rotated label on
the decision tree exists only as vector outlines. **The evidence a text-layer detector would need is
precisely what is missing.** Nothing in the string says a label was there. This is a *density*-axis
question and the ground-truth sample already answers it: those two pages are "the only two slide pages in
the whole sample where `sparse` is unambiguously the right call", and the sub-gate predicate
`image_area ≥ 0.20 × page_area OR len(page.get_cdrawings()) ≥ 40`
([ground-truth-sample.md](./ground-truth-sample.md) § 1.4) is the mechanism that routes them. **Not a
detector. Closed as mis-filed.**

### 6.3 Superscript flattened into a false number — **detectable, specified, deliberately not shipped**

`7.50 × 10³ Pa` → `103 Pa` (wrong by 10²) and `2.35 × 10⁴ chips` → `2.35 𝑥 104` (wrong by 10³). Six rows
of the labelled sample are this class and no shipped detector sees any of them.

It **is** cheaply detectable, geometrically. A superscript span is smaller than its line's body size and
sits higher; when extraction glues it to the preceding digits the value becomes false. Prototyped:

```python
SIZE_RATIO, RISE_RATIO = 0.85, 0.15          # of the line's largest span size
for line in page.get_text("dict") ... :
    body = max(s["size"] for s in spans);  base = max(s["origin"][1] for s in spans)
    for prev, s in zip(spans, spans[1:]):
        if re.fullmatch(r"\d+", s["text"].strip()) \
           and re.search(r"\d\s*$|[×x∗*]\s*10\s*$", prev["text"]) \
           and s["size"] <= SIZE_RATIO * body \
           and base - s["origin"][1] >= RISE_RATIO * body:
            yield prev["text"][-14:], s["text"]
```

Measured over all 7,198 pages: **156 pages / 71 documents in 58 s**. It catches **3 of the 4** superscript
rows in the labelled sample with the right evidence — `(' 10', '3')` on `ps160/m18/chapter_18.pdf` p2 and
`('2.35 𝑥 10', '4')` on the GNSS module — and its other hits read correctly (`3.95 × 10⁸`, `2¹⁶`, `2³²`).
Visible false positives are footnote and figure references (`Fig. 7` + `23`).

**Not shipped, for two reasons that are about the contract, not the signal.** It needs a `page`, not a
string, and every entry in `_DETECTORS` today is `str -> str | None`; and it costs `get_text("dict")`,
which takes the corpus pass from 22 s to 58 s — 2.6×, where the whole second axis currently costs nothing
measurable. Both are plan-level decisions. Recorded here with its constants and its numbers so that work
starts from data, exactly as § 4.3 of the plan did for `unmapped-glyphs`.

---

## 7 · What is now open

1. **`_SHRED_MAX_CHARS`.** It, not the run length, blocks 7 of the 12 known misses. Raising it 4 → 8
   with the strong rule costs +232 corpus pages and recovers 4 of them. **The increment is unlabelled**,
   and § 4.1 shows the corpus the original sweep used as a control is not one. Needs a drawn-and-read
   increment of ~25 pages, which is one session's work with the method in § 2.
2. **The `partial` class has no home.** § 3.1 gives up ~46 pages of non-mathematical 2-D loss —
   traceability matrices, decision trees, figure axes. If that matters it is a *separate named detector*,
   not a loosening of this one; every loosening measured here buys the wrong pages.
3. **The superscript detector needs a contract decision** — § 6.3.
4. **Evidence correctness is still 64%.** [ground-truth-sample.md](./ground-truth-sample.md) § 2.2 found
   the printed run is the wrong run on 9 of 45 flagged pages. `shredded_run()` still returns the *first*
   qualifying run, not the most symbolic one. `_is_strong` improves this incidentally — plot furniture
   with no mathematical character is now skipped — but it was not measured and is not claimed.
5. **`structure.py` is 461 lines**, against the ~300 ceiling in
   [../directives/code-discipline.md](../directives/code-discipline.md). Four detectors plus the registry
   is arguably two jobs. A split (registry and contract here, the detectors beside it) is overdue.

---

## 8 · Reproducing this

The three corpus passes are pure functions of `content/` and of `structure.py`:

```bash
cd ~/electrical_notes/ocr_handler

# the corpus roll-call the tables above are built on -- 459 docs / 7,198 pages, 22 s
nice -n 19 python3 - <<'PY'
import sys, collections; sys.path.insert(0, "src")
from pathlib import Path
from ocr_handler import textlayer
pages = docs = suspect = 0
per = collections.Counter()
for pdf in sorted(Path("../content").rglob("*.pdf")):
    try: d = textlayer.extract(pdf)
    except Exception: continue
    docs += 1; pages += len(d.pages); suspect += len(d.suspect_pages)
    per.update({k: v for k, v in d.signal_counts.items() if v})
print(docs, "docs /", pages, "pages --", suspect, "suspect;", dict(per))
PY

# the regression floor
PYTHONPATH=src nice -n 19 python3 -m pytest tests/ -q       # 120 pass
```

The sweep itself replays by caching each page's `page.get_text()` once (19 s) and re-running a
parameterised copy of `shredded_run` over the cache at each `(max_chars, min_run, min_symbolic,
qualifier)` — no PDF is re-opened per setting, which is what makes an 18-cell sweep cost seconds.

**The 75 new hand labels cannot be regenerated** — they are one reader's judgements, made on 110-dpi
renders read against each page's own extracted text, using the label vocabulary of
[ground-truth-sample.md](./ground-truth-sample.md) § 0. They are committed as
[`shred_sweep_labels.csv`](../../tests/fixtures/ground_truth/shred_sweep_labels.csv), one row per page
with the run that was judged, so a single call can be re-checked by opening that page. The draws were
seeded — `random.seed(20260906)` for strata B and C over the enumerated increments, `20260913` for the
20-page redraw inside C ∩ strong — and re-drawing them is a `random.sample` over the same enumeration.

**One reader, no answer key**, and the same caveat the ground-truth sample states applies: n = 30, 25 and
20 give wide intervals. The direction is not in doubt — 83% versus 28% is not a sampling artefact — but a
point estimate on 20 pages is a range.

---

## 9 · Decision status

| # | Question | Answer | Status |
| --- | --- | --- | --- |
| 1 | Lower `_SHRED_MIN_RUN`? | **Yes, to 2 — but only with `_is_strong`.** Alone, 2 costs 26 points of precision. With it: precision 84.8% → **93.1%**, recall 35.3% → **68.2%**, 416 → 732 pages. | **Shipped.** |
| 2 | What does it cost? | 5 of 6 `partial` pages — non-mathematical 2-D loss. Broad precision 98% → 95%. No strict true positive in the labelled sample. | **Priced, § 3.1.** |
| 3 | Is the benign-glyph list right? | Every count reproduces. 1,406 → 505 pages, 901 silenced. Plan § 4.3's "235 pages / 54 docs" is wrong by 6×. | **Verified; plan corrected.** |
| 4 | Is vertical letter-spacing catchable? | Yes, and it is shipped. The sweep reproduces exactly. It became *independent* evidence this session. | **Verified.** |
| 5 | The `ti` ligature? | Not dropped — extracted as U+0017 and already caught on 89 of 92 pages. | **Closed.** |
| 6 | Rotated PowerPoint text? | Undetectable from the string, and it is a density question, not a faithfulness one. | **Closed as mis-filed.** |
| 7 | Flattened superscripts? | Detectable geometrically — 156 pages / 71 docs, prototype in § 6.3 — but needs a `page` in the detector signature and 2.6× the pass cost. | **Open, specified.** |

---

**See also:** [ground-truth-sample.md](./ground-truth-sample.md) ·
[../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) ·
[layout-mode-decides-whether-math-survives.md](./layout-mode-decides-whether-math-survives.md) ·
`src/ocr_handler/structure.py`, `tests/persistent/test_textlayer.py`
