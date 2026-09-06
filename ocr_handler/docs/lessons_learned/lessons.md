# Lessons Learned

**PRESCRIPTIVE.** Each entry is a rule *plus the specific failure that earned it*. If an entry cannot
name its incident, it belongs in [../directives/INDEX.md](../directives/INDEX.md) instead.

Index and the directive/lesson boundary: [INDEX.md](./INDEX.md).

---

## Measurement

- **WHEN a source hands you a utility function to vendor, DON'T adopt it on inspection — run it over
  your own recorded outputs first — BECAUSE a function can be uniformly destructive and still look
  clean.** MinerU's `latex_rm_whitespace` was read, found to map `\Bar` → `\hat` (x̄ a mean becoming x̂
  an estimate), and recorded as "worth vendoring, mind the one landmine". A real audit found **11
  defects, and that one ranked fifth.** `\rightarrow` is *deleted outright*: the pattern matches the
  `\right` prefix, rewrites it to `\right.`, the delimiter counts then disagree, and a strip-all branch
  removes it. Measured over our own outputs: 4 of 44 UniMERNet readings changed, **6 of 6** PaddleOCR-VL
  readings changed, and **every single change was damage — not one improvement in either set.**
  (2026-09-06) Source: [../research/INDEX.md](../research/INDEX.md) § Landmines ·
  [../plans/latex-repair-and-validity.md](../plans/latex-repair-and-validity.md)

- **WHEN a bug is asymmetric, DON'T trust a sample to reveal it — construct the paired case —
  BECAUSE the surviving half makes the broken half invisible.** `\Rightarrow` passes through the above
  function untouched while `\rightarrow` is deleted. Any spot-check that happened to use the
  capitalised form would have reported the function clean. (2026-09-06)

- **WHEN you inherit a headline number, DON'T build on it — re-derive it — BECAUSE the measurement
  method is usually the finding.** Token-variety's "8/10 pathologies at zero false positives" was
  scored with space-counting tokenisation and only against other model outputs; under
  spacing-invariant tokenisation it is **2/10**. The genuine winner, `length-vs-crop`, was not in the
  original list at all. Separately, an inherited "235 pages / 54 documents" unmapped-glyph volume
  re-measured at **1,406 / 130** — off by ~6×, and no variant reproduced the original.
  (2026-09-06) Source: [../plans/latex-repair-and-validity.md](../plans/latex-repair-and-validity.md) § 3.8

- **WHEN a corpus is called a "control", DON'T assume it is one — label a sample of it — BECAUSE a
  control that is full of true positives prices recall as if it were cost.** The
  `cesc_470`/`cec_320`/`stat_412` control set was used to bound false positives while sweeping
  `_SHRED_MAX_CHARS`; **44 of its 49 hits are real flattened mathematics** (`cases` braces, summations,
  an `\underbrace`). That constant is therefore unsettled, not decided. (2026-09-06)
  Source: [../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md)

- **WHEN a peer or a prior session hands you a claim, DON'T act on it — treat it as a hypothesis —
  BECAUSE several have failed verification, and the failure is usually more informative than the
  claim.** "`pdftotext -layout` dropped all the equations" — it did not; `-layout` extracts 135,744
  chars against plain's 108,796, and the equations survive with their 2-D alignment. "PyMuPDF layout
  mode beats `pdftotext -layout`, 170,105 vs 135,744" — does not reproduce; there is no
  `get_text("layout")` mode, and the `blocks` mode being measured includes coordinate tuples in its
  character count. (2026-09-05) Source: [../findings/layout-mode-decides-whether-math-survives.md](../findings/layout-mode-decides-whether-math-survives.md)

---

## Detectors and classifiers

- **WHEN a detector exists but feeds no verdict, DON'T call it shipped — wire it in or delete it —
  BECAUSE an unwired detector is never wrong, so its bugs never surface.** `is_letter_spaced()` had
  shipped since M1, fired on **51 documents**, and fed nothing. Making it verdict-bearing immediately
  exposed that its pattern `(?:\b\w\s){6,}` used `\s`, **which matches a newline** — so a plot's tick
  labels extracted one-per-line scored as a corrupt text layer. Corrected to horizontal whitespace and
  letters only: **3 documents.** The published corpus census was an overcount of roughly 17×.
  (2026-09-05) Source: [../findings/layout-mode-decides-whether-math-survives.md](../findings/layout-mode-decides-whether-math-survives.md)

- **WHEN two questions have different repairs, DON'T merge them into one score — give them separate
  axes — BECAUSE the merged verdict routes the page to the wrong fix.** `inspect` reported
  **47 of 47 pages `ok`** on a PDF whose every displayed equation was rubble, because it classified on
  character count alone. Density (`ok`/`sparse`/`empty`, "is there text?") and faithfulness
  (`intact`/`suspect`, "is it right?") are now separate, and a `suspect` page is deliberately **never**
  sent to OCR — its glyphs are already present with correct coordinates, so a model would spend GPU
  recovering what is in the file and return a worse answer. (2026-09-05)
  Source: [../plans/structural-faithfulness.md](../plans/structural-faithfulness.md)

- **WHEN recall is short, DON'T reach for the threshold first — ask what the detector is actually
  testing — BECAUSE loosening the wrong constant buys misfires instead of coverage.** The standing
  hypothesis was that `_SHRED_MIN_RUN = 4` caused a 35% recall, since a flattened fraction makes only
  2–3 short lines. Of 12 labelled misses, lowering the run to 3 reached **1** and to 2 reached **5** —
  the other seven were blocked by a different constant entirely, and the case named as the sharpest
  argument for lowering does not fire at 4, 3 **or** 2. Lowering the run alone drops strict precision to
  **28%**, with 17 of 25 misfires being **Wingdings bullets that map to ASCII `z`** and assembly-listing
  gutters, both escaping through a "lone ASCII letter is a variable" fallback. The fix that paid was a
  *symbol* test — every run must contain a line symbolic by an actual mathematical character.
  Result: precision **84.8% → 93.1%** while recall went **35.3% → 68.2%**. (2026-09-06)
  Source: [../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md)

- **WHEN every individual detector is correct, DON'T conclude the set is complete — look for the
  content-free case — BECAUSE a reading can satisfy all of them and still carry nothing.**
  `\[\begin{aligned}\begin{aligned}\\ &\end{aligned}\\ \end{aligned}\]` — zero mathematics — passed all
  seven validity detectors as `plausible`. Each was individually right: 45 tokens (the tokeniser splits
  `{aligned}` into nine), variety 0.333, balanced braces, no repeated run. The gap needed an **eighth**
  detector counting *content* tokens, not a tuned threshold. (2026-09-06)
  Source: [../plans/latex-repair-and-validity.md](../plans/latex-repair-and-validity.md) § 3.8

- **WHEN a report lists what fired, DON'T stop there — list what ran and stayed quiet, and what could
  not run at all — BECAUSE a silent detector and an absent one are not the same, and only the report
  can tell them apart.** The `Signal(name, fired, detail)` roll-call exists for this; `check` prints
  `length-vs-crop  not evaluated: no crop size supplied` rather than omitting the row. (2026-09-06)

## Measuring a measurement

- **WHEN a control corpus is chosen for the absence of the thing you are testing, DON'T trust the
  bound it gives you — check that it CAN fire — BECAUSE a control that cannot fire bounds nothing.**
  Thirteen documents of syllabi, ARM assembly listings, Python code and rubrics were assembled as a
  false-positive control for `shredded-lines`. They fire **0 at every `_SHRED_MAX_CHARS` from 4 to
  12** — not because the detector is precise, but because with no character in `_SYMBOLIC_RANGES`
  its `_is_strong` gate can never pass on any setting. **The measurement was vacuous.** A useful
  control here must contain mathematics that is *not* flattened. Screening for it is also unreliable:
  one candidate exam paper passed and pages 2–3 turned out to be formula sheets — roughly one in
  three fails on a page nobody would predict. (2026-09-06)
  Source: [../findings/precision-replicates-the-priced-cost-does-not-2026-09-06.md](../findings/precision-replicates-the-priced-cost-does-not-2026-09-06.md)

- **WHEN you report a cost, DON'T reweight a sample to get it — enumerate the affected population —
  BECAUSE a sample tells you a rate and you are claiming a count.** A change was shipped priced at
  "~46 non-mathematical pages lost". Enumerated, it orphans **66**, and a seeded read of those found
  **35% are genuine flattened mathematics** — `W = ∫p dV`, `v_rms = √(3kT/m)`, a 3×3 matrix product.
  The published sentence *"no strict true positive was lost"* was true of the 161 labelled pages and
  **false corpus-wide**. (2026-09-06)

- **WHEN pages come from the same document, DON'T treat them as independent samples — cluster the
  bootstrap by document — BECAUSE the confidence interval is otherwise a fiction.** A replication that
  reported 90.0% [78.6, 95.7] on 50 pages found the honest floor was **~80%** once clustered, and
  flagged that 29 of its 50 pages came from a single LaTeX signals course. Related: this corpus is
  measurably duplicated — 459 documents carry **355 distinct text layers** — so a per-document draw
  over-weights whatever is filed three times. (2026-09-06)

- **WHEN a page has no text and no images, DON'T call it blank — check for vector content — BECAUSE
  a drawn page is content and skipping it discards the whole page silently.** The figure "482 blank
  pages" was quoted throughout this project's docs. Of 483 such pages, **406 carry vector drawings or
  XObject-painted images**; `lctr22-exercise.pdf` p1 is 0 chars, 0 images, **1,837 vector paths and
  8.9% non-white pixels**. The real skip set is **24**. (2026-09-06)
  Source: [../findings/one-classifier-2026-09-06.md](../findings/one-classifier-2026-09-06.md)

---

## Detectors, continued

- **WHEN a detector requires evidence of X, DON'T assume the evidence survives the corruption you are
  detecting — check the degraded case — BECAUSE a detector can be blind in exactly the direction of
  its own target.** `_is_strong` requires a genuine mathematical character in every flagged run. But
  when a fraction flattens, the font that flattened it often mangles the operator too: `∫`→`Z`,
  `√`→`r`, `Σ`→`X`, `∏`→`Q`. A run of `Z / p / dV` — a flattened integral, precisely the thing the
  detector exists to catch — fires **nothing**. Not fixable from a `str`: separating a mangled `∫`
  from a literal `Z` needs the font. (2026-09-06)

- **WHEN two detectors read the same evidence, DON'T let them disagree about what it means — BECAUSE
  one of them is wrong and neither will say so.** `unmapped_glyphs` declared U+F0B7 / U+F070 / U+F06C
  benign — Office bullets, 2,896 corpus occurrences — while `_is_strong`, forty lines away in the same
  file, counted those same glyphs as proof of mathematics. One detector calling a glyph a bullet while
  another calls it an integral sign. Fixed by filtering the declared-benign set before the strength
  test; measured 732 → 729 pages, all three removed non-mathematical. (2026-09-06)

- **WHEN a constant is swept on one corpus, DON'T carry it to another — re-sweep per stratum —
  BECAUSE a tuned constant encodes the data it was tuned on.** `RED_MARGIN = 55`, correct for red ink
  on P1's slides, transposed to blue ink on scanned exams destroys **67–77% of the handwriting**
  (18,995 ink px → 6,296), leaving a dotted skeleton. It is invisible at page scale and obvious at
  crop scale, so it would have reached the model and **scored as a model failure**. `merge_px = 64`'s
  plateau is likewise P1-only: on P2 it returns one region covering half the page. Corollary worth
  keeping: the **locator** dilates before labelling so it tolerates erosion and not contamination; the
  **paint** is reproduced pixel-for-pixel, so its tolerances are exactly reversed. One job, two
  constants. (2026-09-06)
  Source: [../findings/mask-separability-by-stratum-2026-09-06.md](../findings/mask-separability-by-stratum-2026-09-06.md)

---

## Code


- **WHEN a transformation changes text, DON'T let it return without naming the rule — BECAUSE a test
  asserting that invariant can exist and still not cover the one path that violates it.**
  `repair()`'s `_QQUAD_RE` used `re.sub` and appended no note, so a real recorded reading came back
  altered with an empty `notes` tuple — contradicting the spec, the docstring, and a test literally
  named `test_every_change_is_reported`. `\qquad` is load-bearing here: it is the token `ink.py` uses to
  mark a deliberately blank region. The test was widened from one string to an invariant over four.
  (2026-09-06)

- **WHEN a value is tuned, DON'T ship the number alone — ship the sweep that produced it, in the code —
  BECAUSE the next person cannot tell a measured constant from a guess.** `merge_px = 64` carries its
  16→96 sweep and the stable 56–80 plateau. `_MIN_CONTENT_TOKENS = 3` carries what pins it: `x = 1`, the
  shortest legitimate reading, is exactly three content tokens.

- **WHEN sorting spatial items, DON'T sort by `(y, x)` — band by vertical overlap first — BECAUSE two
  side-by-side equations whose tops differ by three pixels come back swapped**, silently reversing the
  reading. Source: [../directives/code-discipline.md](../directives/code-discipline.md)

- **WHEN a page already has a text layer, DON'T run a model over it — BECAUSE extraction is exact and
  recognition is lossy.** Measured: 67% of the corpus needs no model at all.

---

## Cost and hardware

- **WHEN a job is pinned to the GPU, DON'T assume it will not saturate the CPU — BECAUSE
  `from_pretrained` deserialises weights on the CPU before anything reaches the device.** A correctly
  CUDA-pinned evaluation script held 98% CPU and nearly took the machine down. Killing the process was
  not enough — the agent that owned it respawned it; the agent had to be stopped. Thread-pool
  environment variables are read **at import time**, so `cap_cpu_threads()` must run before torch or
  numpy are imported. (2026-09-06) Source: [../directives/gpu-discipline.md](../directives/gpu-discipline.md)

- **WHEN attributing load, DON'T assume it is yours — measure per-process first — BECAUSE stopping
  your own work on a wrong premise costs the work and does not fix the load.** Load hit 13.20; an agent
  was reniced and then stopped. `unattended-upgrades` was at 98% and two Firefox processes at ~90% —
  roughly 80% of the load was not ours. (2026-09-06)
