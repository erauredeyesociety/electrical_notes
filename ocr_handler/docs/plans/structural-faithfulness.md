# The structural faithfulness axis — "is the text present?" is not "is the text right?"

> **Type: ACTIVE-SPEC.** Living document, named by concept (no date in the filename) per
> [../directives/roadmap-and-plans.md](../directives/roadmap-and-plans.md).
> Written 2026-09-05; **amended 2026-09-06** — two more detectors shipped (§ 4.3, § 4.4) and
> `shredded-lines` re-swept, `_SHRED_MIN_RUN` 4 → 2 behind a new strong-symbolic rule
> ([../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md)).
> Two claims made here were re-measured and are marked ⚠ where they stand: the `cec_320`/`stat_412`
> "control corpus" (§ 3.2, § 6) and the raw unmapped-glyph volume (§ 4.3).
> Closes the false negative recorded in
> [../findings/layout-mode-decides-whether-math-survives.md](../findings/layout-mode-decides-whether-math-survives.md).
> Constants below are swept, not guessed; each names its measurement per
> [../directives/code-discipline.md](../directives/code-discipline.md).

---

## 1 · The defect, in one line

`textlayer.py` classifies on characters per page. On a 47-page born-digital LaTeX PDF whose prose is
intact but whose rendered equations are shredded into unordered fragments, it returns **`ok` on all 47
pages** and a document verdict of `text-layer-sufficient`. The load-bearing content is unusable and the
tool reports health.

Character count answers *"is there text?"*. This project exists to answer *"is the text faithful?"*.

---

## 2 · The output contract

**Two orthogonal axes, never merged.** Each page and each document carries both.

| | Axis 1 — **density** (existing) | Axis 2 — **faithfulness** (new) |
| --- | --- | --- |
| Question | is there text? | is the text a faithful rendering of the page? |
| Evidence | characters per page | named structural detectors |
| Page field | `verdict` — `ok` / `sparse` / `empty` | `structure` — `intact` / `suspect` |
| Doc property | `verdict` — `text-layer-sufficient` / `ocr-partial` / `ocr-required` | `structure_verdict` — `structure-intact` / `structure-suspect-partial` / `structure-suspect` |
| Remedy | **OCR** — render the pixels, run a model | **not OCR** — layout-aware re-extraction, or read the page image |

### Why they must not merge — the load-bearing decision

A structurally-suspect page **must not** change `doc.verdict`, and a `suspect` page **must not** set
`needs_ocr`. The finding this plan closes says why: the glyphs on that fixture are *already present with
correct coordinates*. Sending it to a VLM would spend GPU recovering information that is already in the
file, and would return a worse answer than the bytes already there — the exact waste
[../decisions/0003-text-layer-first-and-one-extractor.md](../decisions/0003-text-layer-first-and-one-extractor.md)
forbids. **Two different failures, two different repairs.** Routing them down one pipe is how the cheap
fix ends up waiting on the expensive one.

It also keeps a promise: `doc.verdict`, `PageText.verdict` and `needs_ocr` are consumed by `pdfops`, by
the `auto`-mode gate in [text-layer-first.md](./text-layer-first.md) § 2, by an external caller in
`content/cesc_470/md_notes/README.md`, and by 15 tests. The new axis is **additive**.

### Evidence, not a boolean

A bolted-on `is_suspect: bool` would age badly — the third detector has nowhere to go, and a reader who
sees `suspect` cannot tell *what* was detected or check it. Every page therefore carries the full
detector roll-call:

```python
@dataclass(frozen=True)
class Signal:
    name: str      # "letter-spaced" | "shredded-lines"
    fired: bool
    detail: str    # the evidence, verbatim, so a human can check the call
```

`PageText.signals` holds one `Signal` per detector, fired or not. Adding a detector means appending to
`_DETECTORS`; it does not touch `PageText`, `DocText`, the CLI, or any existing test. Each entry carries
its own one-line explanation, so a report never has to guess which corruption it is describing.

**Where it lives.** The detectors are a new module, `src/ocr_handler/structure.py`; `textlayer.py`
imports it and re-exports `is_letter_spaced` so its existing callers and tests are untouched. "Is there
text?" and "is the text right?" are two jobs, and one file doing both is what the ~300-line ceiling in
[../directives/code-discipline.md](../directives/code-discipline.md) is for.

> ⚠ **That ceiling is now breached.** This section was written when the module was ~200 lines and two
> detectors. With four detectors and the sweeps that justify their constants it is **461 lines**. The
> registry, the `Signal` contract and the four detectors are arguably two jobs, and the split — contract
> here, detectors beside it — is overdue. Recorded rather than quietly accepted.

### The combining rule, and what happens when signals disagree

**`structure == "suspect"` iff ANY signal fired.** An OR, never an average, never an AND.

Disagreement is the *normal* case, not an error. Measured over 442 documents / 7,202 pages when there
were two detectors: they both fired on the same page **49 times out of 463 flagged pages (11%)**. Now
four, over 459 documents / 7,198 pages: **959 suspect pages**, of which **673 carry exactly one signal**.
⚠ **Remeasured 2026-09-06: 956** over 7,187 pages / 141 documents (`shredded-lines` 729,
`unmapped-glyphs` 505, `letter-spaced` 4, `vertical-letter-spaced` 4). The published 959 was a
headline slip — every *per-detector* count reproduced exactly — and 3 of the remaining difference is
the benign-glyph guard added to `_is_strong` the same day.
They detect unrelated corruptions — a font-encoding fault, a reading-order fault, a rotated label, an
unmapped glyph — so:

- an **AND** would find almost nothing;
- a **weighted score** would blur two independent failures into one uninterpretable number and lose the
  only thing a reviewer can act on, which is *which* corruption occurred.

So both are always reported by name, and the page is suspect if either fires. Where they disagree, the
report shows the disagreement rather than resolving it — the same rule
[../directives/documentation-discipline.md](../directives/documentation-discipline.md) applies to
contradictory measurements.

### Document banding — 21% suspect is not 100% suspect

Mirrors the density axis exactly, so there is one rule to remember:

| suspect pages | `structure_verdict` |
| --- | --- |
| none | `structure-intact` |
| some | `structure-suspect-partial` |
| all | `structure-suspect` |

The count and the page list are always reported alongside, because the band alone cannot distinguish a
paper with ten broken equations from a document that is broken throughout.

---

## 3 · The detectors

### 3.1 `letter-spaced` — promoted, not new

`is_letter_spaced()` already existed. It fired on 51 documents and fed **nothing**: a footnote at the
bottom of the Markdown header and one line of `inspect` output, attached to no verdict and to no page.
It *is* a faithfulness signal — "a dense text layer can still be corrupt" — and it is exactly the
bolted-on boolean this design replaces. It becomes the first entry in `_DETECTORS`, per page.

Promoting it is what exposed its own bug. Its pattern, `(?:\b\w\s){6,}`, was measured at exactly the
census's 51 documents / 154 pages — and **`\s` matches a newline**, so a plot's tick labels extracted one
per line (`1\n2\n3\n4\n5\n6`) scored as a corrupt text layer. **46 of the 51 documents fired on nothing
else.**

| Pattern | Documents | Pages |
| --- | ---: | ---: |
| `(?:\b\w\s){6,}` | 51 | 154 |
| `(?:\b\w[^\S\n]){6,}` — horizontal whitespace only | 5 | 11 |
| `(?:\b[^\W\d_][^\S\n]){6,}` — six consecutive **letters** | **3** | **9** |

Tightened to the last row; all nine surviving pages are genuine, and all three of the detector's existing
regression tests pass unchanged. A detector at ~10% precision was tolerable as a footnote and is not
tolerable as a verdict — that is the whole argument for promoting it rather than leaving it dangling.
Cost, stated plainly: a *vertically* extracted rotated axis label (`C\no\nn\nt\nr\no\nl`, real in the
NASA SE handbook) is no longer caught; separating that from a tick sequence needs a detector that can tell
a word from a number, which is open question 3 below, not a wider regex.

### 3.2 `shredded-lines` — new

> A run of **≥ 2 consecutive lines of ≤ 4 characters**, of which **≥ 25% carry symbolic content** and
> **at least one carries a genuine mathematical character**.
>
> *Was: ≥ 4 lines, with no strong-character requirement. Re-swept 2026-09-06 —
> [../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md).*

That is the signature of a two-dimensional layout — a matrix, a stacked fraction, a `cases` brace, a
summation with limits — flattened into a column of fragments by reading-order extraction. On fixture
page 7 a 3×3 intrinsic-matrix equation becomes 32 consecutive one- and two-character lines.

**The symbolic-content qualifier is what makes it usable.** Without it the raw run test has a 21% hit
rate on the fixture *and* fires on assembly-listing line-number gutters (`5 . 6 . 7 . 8 .`), on a Lego
ruler's number scale, and on plot axis ticks — 97 documents, mostly wrong. A line counts as symbolic if,
after rejecting bare numerals, it contains a Greek letter, a mathematical operator, a sub/superscript, a
Private-Use-Area glyph (Computer Modern's big delimiters land there), a control character (an unmapped
math glyph), an `=`, or is a single ASCII letter (a variable).

**Rejecting bare numerals is load-bearing**, and was added on measurement: without it, plot axis ticks
(`0.2 0.4 0.6 0.8 −2`) and `\lstlisting` line numbers pass as "symbolic" because U+2212 MINUS is a math
character. With it, `content/syse_301/LegoRulerV1.1.pdf` stops firing and the cec_320 hit count drops
from 3 documents to 1.

#### Constants, and the sweeps that set them

| Constant | Value | Measurement |
| --- | ---: | --- |
| `_SHRED_MAX_CHARS` | 4 | Sweep over `{3,4,5,6,8}`, below. 4 is the knee **on the sweep as run** — see the correction under it. |
| `_SHRED_MIN_RUN` | **2** *(was 4)* | Re-swept 2026-09-06 over `{4,3,2}` against 236 hand-labelled pages. 4 → 2 alone costs 26 points of precision; with the strong rule below it gains 8. [../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md) § 2. |
| **`_is_strong`** | **new, 2026-09-06** | Every run must contain one line that is symbolic *by a character*, not by the "lone ASCII letter" or "contains `=`" fallbacks. Those two fallbacks are what a Wingdings bullet that maps to `z` and an assembly `b` opcode look like. This is what pays for the run length. |
| `_SHRED_MIN_SYMBOLIC` | 0.25 | `{0, 0.1, 0.25, 0.3, 0.4, 0.5}` on the fixture: 0.25 keeps all 10 originally-measured pages, 0.3 loses 3 of them. Below 0.25 the ruler and axis-tick false positives return. At a run length of 2 this gate is nearly vacuous on its own — one symbolic line of two already clears it — which is why `_is_strong` had to exist before the run length could move. |

> **The run length was the wrong lever, and that is the headline of the re-sweep.** Of the 12 hand-labelled
> `recall = miss` pages, lowering the run to 3 reaches **one** and to 2 reaches **five**; the other seven
> are blocked by `_SHRED_MAX_CHARS`, because their denominator line carries a ROC or a unit and runs to
> 5–8 characters. That includes `stat_412/HW08/solutions/q16.pdf`, which
> [../findings/ground-truth-sample.md](../findings/ground-truth-sample.md) § 3.1 names as the sharpest
> case for lowering the run: it has no run of ≤4-character lines longer than **one**, and does not fire at
> 4, 3 or 2. Shipped result: **416 → 732 pages, strict precision 84.8% → 93.1%, estimated true positives
> 353 → 681.** Cost, priced: 5 of the 6 `partial` pages in the labelled sample — non-mathematical 2-D
> loss such as a 34×34 traceability matrix arriving as 123 lines of `X` — lose their only signal, and
> broad precision falls 98% → 95%.

Line-length sweep — fixture recall against control-corpus false positives (controls = all of `cesc_470`,
`cec_320`, `stat_412`: 156 documents, 1,475 pages, none of which should fire):

| `≤ N` chars | fixture pages flagged | recall over its 18 numbered-equation pages | control pages firing | control docs firing |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 10 / 47 | 10 / 18 | 4 (0.27%) | 1 / 156 |
| **4** | **12 / 47** | **12 / 18** | **5 (0.34%)** | **2 / 156** |
| 5 | 14 / 47 | 14 / 18 | 20 (1.36%) | 14 / 156 |
| 6 | 17 / 47 | 16 / 18 | 49 (3.32%) | 20 / 156 |
| 8 | 19 / 47 | 16 / 18 | 71 (4.81%) | 38 / 156 |

**4 is the knee.** Going 3 → 4 buys two more true positives on the fixture (pages 10 and 12, both
destroyed numbered equations) for one extra control page — and that page, `stat_412/QZ08/solutions/q06.pdf`,
turns out on inspection to be a genuine hit (`χ² = Σ(O−E)²/E` flattened). Going 4 → 5 multiplies control
documents by 7 for two more true positives. The finding's original ≤3 measurement is preserved as the
lower bound of this sweep, not overwritten.

> ⚠ **Correction, 2026-09-06 — the last two columns of that table are not false positives.** "Controls =
> all of `cesc_470`, `cec_320`, `stat_412` … none of which should fire" is the premise, and it is wrong.
> `cec_320` is a mixed C-and-assembly course whose lecture notes are set in LaTeX; `stat_412`'s solutions
> are worked algebra. At the shipped setting those courses produce 49 flagged pages and **44 of them are
> real** — `cases` braces (`10, / 𝑥≥5, / 2𝑥,`), summations (`𝑛 / ∑︁ / 𝑖=1`), an `\underbrace`
> (`| / {z / } / IC`), flattened fractions. The five that are not are one C operator-precedence table in
> five duplicate PDFs. This sweep therefore counted recall as cost, and its conclusion about
> `_SHRED_MAX_CHARS` is **not settled**: raising it 4 → 8 costs +232 corpus pages and recovers 4 more of
> the 12 known recall misses. That increment has not been drawn and read, so the constant stays at 4 —
> but it is the next lever, not a closed question.
> [../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md) § 4.1.

---

## 4 · Detectors evaluated and deliberately NOT shipped

Recorded rather than silently dropped, so the next session does not re-measure them.

### 4.1 The `-layout` character-count delta — **rejected, it does not discriminate**

The finding offers it as the second cheap signal (27k / 25% on the fixture). Measured against controls it
**inverts**:

| Document | `-layout` delta | truth |
| --- | ---: | --- |
| `content/cesc_470/cesc_470.pdf` — prose-only syllabus, no mathematics at all | **+44%** | clean |
| `content/cesc_470/Module 01 …ISA (1).pdf` — slide deck | **+51%** | clean |
| the fixture — equations destroyed | **+25%** | broken |

It ranks two clean documents as *worse than* the broken one. It measures how much horizontal whitespace a
page has — tables, indentation, headers, two-column layouts — which is not structural loss. Shipping it
would have raised the false-positive rate above the false-negative rate it was meant to fix.

Two further reasons it should not sit in the classifier even if it worked: it costs a second full
extraction on every page, and its faithful implementation is `pdftotext`, which
[../decisions/0001-pymupdf-is-the-only-pdf-library.md](../decisions/0001-pymupdf-is-the-only-pdf-library.md)
excludes as a dependency (poppler stays a terminal diagnostic). PyMuPDF's own layout renderer is a
private CLI helper, `pymupdf.__main__.page_layout`.

**Verdict: not in the classifier, and not behind an opt-in flag either.** An opt-in flag for a signal
that ranks clean documents worse than broken ones is a trap, not an option — and
[../directives/code-discipline.md](../directives/code-discipline.md) says a new flag needs a better
reason than "it was cheap to compute". It stays what it always was: a diagnostic you run at a terminal
when you already suspect a document, documented here so nobody re-derives it.

### 4.2 Geometric tight-stacking — **rejected, fires on code**

*"Fraction of consecutive line pairs whose vertical gap is under half the page's median baseline pitch"* —
the direct geometric read of "this page has 2-D structure", PyMuPDF-native and free. It fires on **100%
of pages** in five separate cec_320 assembly-listing homework sets and 27% of a computer-architecture
slide deck, because a monospaced listing has a tighter pitch than the surrounding prose. Unusable.

### 4.3 Unmapped glyphs — ~~promising, deferred~~ **SHIPPED 2026-09-06**

Count of Private-Use-Area and C0-control characters, i.e. glyphs the extractor could not map to Unicode.
Fires on 54 documents / 235 pages, and its hits are real: U+F8F1–F8F4 are Computer Modern's `\left\{`
pieces, so a `cases` environment reaches the reader as `` — unreadable. It is genuinely independent of
both shipped detectors (it fires alone on 18 documents).

It was **not shipped** because its single commonest corpus-wide trigger is **U+F0B7, the Symbol-font
bullet, 1,514 occurrences** — every PowerPoint bullet in the corpus. A benign-glyph list had to be built
and swept before the detector could be trusted.

**That list exists and the detector ships.** All 89 unmapped code points in the corpus were ranked by
frequency and each one's glyph bbox rendered to see what it is on the page. The cut falls after three,
and nowhere else — `_BENIGN_GLYPHS = {U+F0B7, U+F070, U+F06C}`, the Office dingbat block, 92% of its
corpus volume. Below them the ranking is mathematics: U+F8F4 is CMEX10's `\left\{` extension, U+0001 its
big `\left(`. U+0007 and U+0008 are deliberately **not** benign even though they are tab leaders in two
handbooks, because in CMEX10's encoding they are `\rceil` and `\{`.

Effect, re-verified 2026-09-06: raw **1,406 pages / 130 documents** → **505 pages / 118 documents**, 901
silenced, of which 99.0% is furniture. It fires alone on 219 pages.

> ⚠ **Correction:** the "54 documents / 235 pages" above is wrong by roughly 6×. Re-counted over the
> shipped definition — Private-Use Area plus C0 controls, tab and newline excluded — the raw signal is
> **1,406 pages / 130 documents**, and no obvious variant reproduces 235/54 (PUA alone 1,053/70; C0 alone
> 374/69; a ≥5-per-page threshold 361/76). Every *code-point* count in the ranking reproduces exactly.

**And it closes a defect nobody had assigned to it.**
[../findings/ground-truth-sample.md](../findings/ground-truth-sample.md) § 6.1 reports a document
"silently losing its `ti` ligature — invisible to both detectors". The ligature is not dropped: it is
extracted as **U+0017**, and this detector fires on **89 of that document's 92 pages**. What was true of
two detectors is not true of four.

### 4.4 Vertical letter spacing — **SHIPPED 2026-09-06**, and it is now independent

Open question 3 below, answered: a rotated label extracted downwards (`C\no\nn\nt\nr\no\nl`) is
separable from a plot's tick column by asking whether the letters spell a *word*. Three tests, each paid
for by a measured false positive among the 26 pages a bare run test flags — case shape, "not an A–Z run",
"no four consecutive consonants" — leave 4 pages in 1 document: `Control`, `Identify`, `Analyze`,
`Sustaining`, `System`, `Management`, `Operation`, `Enginee`. Run-length sweep over {4,5,6,7,8,10} gives
6/5/4/4/4/2 pages; 6 is the first value where all of them are real.

It was described as adding naming rather than pages, because a column of single letters was also a
`shredded-lines` run. **The `_is_strong` rule of § 3.2 changed that**: a column of lone ASCII letters
carries no mathematical character, so `shredded-lines` declines it and all four of this detector's pages
are now pages it is the *only* signal on. It became independent evidence without being touched.

### 4.5 Flattened superscripts — **measured, specified, NOT shipped**

`7.50 × 10³ Pa` extracting as `103 Pa` is a silent numeric error: no line break, no run, no unmapped
glyph, and six rows of the labelled sample are this class with no detector able to see any of them.

It *is* cheaply detectable — geometrically, not from the string. A superscript span is smaller than its
line's body size and sits higher; when extraction glues it to the preceding digits the value becomes
false. Prototyped at `size ≤ 0.85 × body` and `rise ≥ 0.15 × body`: **156 pages / 71 documents**, catching
3 of the 4 superscript rows in the labelled sample with the right evidence.

**Not shipped for two reasons that are about the contract, not the signal.** Every entry in `_DETECTORS`
is `str -> str | None`, and this one needs a `page`; and `get_text("dict")` takes the corpus pass from
22 s to 58 s, where the whole second axis currently costs nothing measurable. Both are decisions for this
plan, not for a detector. Constants and numbers:
[../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md) § 6.3.

### 4.6 A mid-word-punctuation ligature test — **rejected, subsumed**

`tt → (` and `ft → $` corrupt words in place (`Le(ers`, `so$ware`). `[a-z]\$[a-z]` is perfectly precise —
38 pages, **one document** — and worthless, because `unmapped-glyphs` already flags 89 pages of that same
document through its `ti` ligature. `[a-z]\([a-z]` fires on 1,208 pages: every `x(t)` in the corpus.

---

## 5 · Surfaces

`inspect` gains **one line, printed only when something fired** — it must not add noise to the 214
documents that are genuinely clean:

```text
  ! structure-suspect-partial: 12/47 pages (shredded-lines 12, letter-spaced 0)
    pages: 7, 8, 10, 11, 12, 16, 19, 26, 27, 28, 40, 41
    text layer is present but its 2-D structure was flattened; OCR is NOT the fix
```

`to_markdown()` gains a matching block in the existing honesty header, and the existing letter-spacing
footnote is folded into it — one warning about faithfulness, not two. Per-page headings gain a `suspect`
tag next to the density tag.

**No new CLI verb and no new flag**, per [../scope.md](./../scope.md) § A note on the CLI.

---

## 6 · Measured performance

> **Re-measured 2026-09-06 after the `_SHRED_MIN_RUN` re-sweep and with all four detectors shipped.**
> Whole corpus, **459 documents / 7,198 pages**, one `nice -n 19` pass in **22 s**, no model, no GPU.
> **959 pages (13.3%) suspect** — `shredded-lines` 732 (162 docs), `unmapped-glyphs` 505 (118),
> `letter-spaced` 4 (3), `vertical-letter-spaced` 4 (1). 673 of the 959 carry exactly one signal.
>
> | | before | after |
> | --- | ---: | ---: |
> | `shredded-lines` pages / documents | 416 / 115 | **732 / 162** |
> | strict precision | 84.8% [72, 92] | **93.1% [85, 96]** |
> | broad precision | 97.8% | 95.2% |
> | estimated corpus true positives | 353 | **681** |
> | recall against a fixed pool of 999 broken pages | 35.3% | **68.2%** |
>
> Fixture: **17 of 47 pages**, up from 12 — its 18 equation-bearing pages are now nearly all reached.
> Per course: `ee_300` 84.5%, `cec_315` 52.4%, `cesc_410` 21.9%, `stat_412` 16.4%, `ps160` 11.3%,
> `ae318` 5.4%, `sys_304` / `cesc_470` 3.9%, `cec_320` 2.4%, `cec_300` 1.5%, `syse_301` 0.3%,
> `cesc_420` and `cpsc_462` 0.0%. It still fires where the mathematics is.
> [../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md).

The 2026-09-05 measurement, kept because the sections below reason from it:

Whole corpus, **460 documents / 7,245 pages**, one `nice -n 10` pass in **17 s**, no model, no GPU.
**436 pages (6.0%) flagged across 118 documents** — `shredded-lines` 428, `letter-spaced` 9.

**False negative closed.** Fixture: `structure-suspect-partial`, **12 of 47 pages**. Precision on the
fixture is **12/12** — every flagged page carries a numbered display equation. Recall over its 18
equation-bearing pages is 12/18; the six misses are fractions whose numerator is long enough
(`x = f Xc` / `Zc ,`) that no run of ≤4-character lines forms. That is the deliberate precision/recall
setting from § 3.2, not an oversight.

**False positives, the direction that matters more.** The four control documents:

| Document | pages | flagged |
| --- | ---: | --- |
| `content/cesc_470/hw/hw01/HW1.pdf` (LaTeX we generated) | 3 | **0** |
| `content/cesc_470/cesc_470.pdf` (born-digital syllabus, prose only) | 12 | **0** |
| `content/cesc_470/Module 01 …ISA (1).pdf` | 88 | 1 — the *documented* `C o m p u t e r` artefact |
| `content/cec_320/cec320-course-info-spring2026.pdf` | 9 | **0** |

Widened to **1,559 control pages** (all of `cesc_470`, `cec_320`, `stat_412`): **4 hard false positives,
0.26%**, all four inside one 248-page code-companion PDF (a `//` comment gutter and a table of contents).

> ⚠ **These "controls" are not controls** — see the correction in § 3.2. At the current setting the same
> 1,559 pages produce 49 hits and 44 of them are genuine flattened mathematics. The one 248-page
> code-companion misfire is gone: `_is_strong` rejects the `252 / // / 253 / v` gutter that produced it.

Where it fires, it fires on mathematics: `ee_300` 29.3% of pages, `cec_315` 27.6%, `cesc_410` 10.7%,
`sys_304` 9.3%, `ps160` 7.2%, `cesc_470` 2.3%, `cec_320` 0.3%, `cesc_420` 0.0%. It independently
rediscovered the already-documented HW-01 defect in
`content/cesc_410/hw/hw01/overleaf/p03_signal_transformations.pdf`: the run
`` / `` / `` / `cos` / `(π` / `6 n` / `)` is the stacked `π/6` that flattened to `cos( 6π n)`.

**Hand-labelled sample.** 40 flagged pages drawn at random, weighted by flagged-page count:

| Label | n |
| --- | ---: |
| flattened equation or symbolic table (Σ, ∫, `cases`, partial fractions, transform table) | 32 |
| letter-spacing (`C o m p u t e r`) | 1 |
| flattened figure axis, block diagram or traceability matrix — 2-D structure genuinely lost, not an equation | 5 |
| **hard misfire** — a table of contents and a code gutter, both in 700+ page SE handbooks | **2** |

**Strict precision 83%, broad precision 95%, hard false-positive rate 5%.**

**Cost.** The whole second axis is two regexes and a character-range test over a string that has already
been extracted. It adds no PDF read, no second extraction, no render, and no model — 17 s for the corpus
against 24 s for the same pass before it existed, i.e. inside the noise.

## 7 · Regression floor

Added to `tests/persistent/test_textlayer.py`, in the existing style — every fixture PDF is built
in-process so the tests run on a machine with no course material.

| Test | Direction it guards |
| --- | --- |
| `test_flattened_matrix_page_is_structurally_suspect` | the false negative itself |
| `test_unicode_and_pua_math_glyphs_count_as_symbolic` | Computer Modern's unmapped big delimiters |
| `test_prose_page_is_not_structurally_suspect` | false positives |
| `test_numeric_gutter_is_not_structurally_suspect` | the measured axis-tick / line-number class |
| `test_suspect_page_is_not_routed_to_ocr` | a suspect page never sets `needs_ocr` — OCR is the wrong repair |
| `test_structural_suspicion_does_not_change_the_density_verdict` | the two axes stay orthogonal |
| `test_every_page_carries_every_signal` | the contract: evidence, not a boolean |
| `test_suspect_signal_carries_checkable_evidence` | a verdict a reader cannot check is one they must trust |
| `test_document_structure_verdict_bands_none_some_all` | 21% ≠ 100% |
| `test_letter_spacing_is_a_structural_signal` | the promotion, without loosening the old behaviour |
| `test_letter_spacing_ignores_a_column_of_tick_labels` | the `\s`-matches-newline bug, so it cannot return |
| `test_signal_counts_lists_silent_detectors_too` | a silent detector and an absent one differ |
| `test_markdown_warns_that_ocr_is_not_the_repair` | it reaches a reader who never opens the JSONL |
| `test_cli_inspect_reports_the_structural_axis` | it reaches the operator |
| `test_cli_inspect_stays_quiet_on_a_clean_document` | the 214 clean documents gain no noise |

Added with the detectors of § 4.3–4.4 and the 2026-09-06 re-sweep:

| Test | Direction it guards |
| --- | --- |
| `test_vertical_letter_spacing_is_a_structural_signal` | the rotated label, and that it stays the ONLY signal on those pages |
| `test_vertical_letter_spacing_ignores_labels_that_are_not_words` | six real corpus columns that are not words |
| `test_vertical_detection_does_not_widen_the_horizontal_regex` | `is_letter_spaced` is public API with its own regressions |
| `test_unmapped_big_delimiter_is_a_structural_signal` | a `cases` brace reaching the reader as empty boxes |
| `test_symbol_font_bullets_are_benign`, `test_measured_bullets_are_benign_and_the_mathematics_is_not` | the benign list, and its limit |
| `test_cmex_brace_code_points_stay_off_the_benign_list` | U+0007 / U+0008 are `\rceil` and `\{`, not tab leaders |
| **`test_two_line_flattened_fraction_is_suspect`** | **the recall gap — a fraction makes TWO short lines, not four** |
| **`test_lone_letter_column_is_not_structurally_suspect`** | **what pays for it: a Wingdings `z` bullet and an assembly `b` gutter** |
| **`test_a_bare_equals_line_is_not_strong_enough_on_its_own`** | the rejected third tier — a C operator-precedence table |

`FLATTENED_MATRIX` gained one `×` when the strong rule shipped, and the reason is written beside it: the
real page's mathematical characters are the PUA bracket pieces, base-14 Helvetica cannot draw them (only
the Latin-1 block `°±²³µ·×÷` survives a synthetic round trip, measured), and a column of lone ASCII
letters is now deliberately not suspect.

**120 tests pass, none skipped:** `PYTHONPATH=src python3 -m pytest tests/ -q`.

---

## 8 · Open questions this plan does not answer

1. **Should `extract --mode auto` route suspect pages anywhere?** Not to OCR. The right target is a
   layout-aware re-extraction that does not exist yet ([text-layer-first.md](./text-layer-first.md) § 2).
   Until it does, `suspect` is a report, not a route.
2. ~~**What is the benign-glyph list for § 4.3?**~~ **Answered 2026-09-06** — `{U+F0B7, U+F070, U+F06C}`,
   and the detector ships. § 4.3.
3. ~~**Is there a vertical letter-spacing detector?**~~ **Answered 2026-09-06** — yes, and it is a
   separate detector rather than a wider regex, because the separating question is *word versus label*,
   which a regex cannot ask. § 4.4.
4. **Does the sparse gate interact?** A `sparse` page that is also `suspect` is currently reported as
   both. No evidence yet that this is wrong; noted so it is not decided by accident.
5. **`_SHRED_MAX_CHARS` is the next lever, and its original sweep is not trustworthy.** It blocks 7 of the
   12 known recall misses; 4 → 8 costs +232 corpus pages and recovers 4 of them. The sweep that set it
   counted a corpus full of LaTeX-set mathematics as a control (§ 3.2 correction), so it needs a drawn and
   hand-read increment of ~25 pages before the constant moves.
6. **The `partial` class has no home.** `_is_strong` gives up ~46 corpus pages of non-mathematical 2-D
   loss — traceability matrices, decision trees, figure axes. If that matters it is a *separate named
   detector*; every loosening measured buys the wrong pages (§ 3.2, and the finding § 3.1).
7. **Does the superscript detector justify a `page` in the detector signature?** § 4.5. It is the first
   measured signal that cannot be computed from the extracted string.

---

**Sources:** [../findings/layout-mode-decides-whether-math-survives.md](../findings/layout-mode-decides-whether-math-survives.md) ·
[../findings/ground-truth-sample.md](../findings/ground-truth-sample.md) ·
[../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md) ·
[../findings/corpus-census-2026-09-04.md](../findings/corpus-census-2026-09-04.md) ·
[./text-layer-first.md](./text-layer-first.md) ·
`src/ocr_handler/structure.py`, `src/ocr_handler/textlayer.py`, `src/ocr_handler/cli.py`
