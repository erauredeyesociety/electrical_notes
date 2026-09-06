# 2026-09-06 — The repair audit, the recall fix, and the validity gate

**Seat:** PM2 Project-Lead · **Mode:** development · **Outcome:** M3's acceptance gate shipped and reachable; recall nearly doubled; a vendoring decision reversed

---

## What was done

Three parallel agents, each verified independently before acceptance. All work CPU-only; **no GPU, no
model, no ollama** — the machine had nearly been taken down by a runaway process the previous day, and
every sweep ran `nice -n 19` and single-threaded.

### 1. MinerU's repair suite was audited and rejected

`docs/research/INDEX.md` carried a note that `mineru/model/mfr/utils.py` maps `\Bar` → `\hat` — x̄ (a
mean) becoming x̂ (an estimate) — recorded as "worth vendoring, mind the one landmine". A real audit
found **11 defects, and that one ranks fifth**:

| # | Defect | Effect |
| --- | --- | --- |
| 1 | `RIGHT_PATTERN` matches the `\right` prefix of `\rightarrow` | **`\rightarrow` deleted outright.** Rewritten to `\right.`, delimiter counts then disagree, strip-all branch removes it. Same for `\leftarrow`, `\leftrightarrow`, `\rightharpoonup`, `\lefteqn`. **Asymmetric — `\Rightarrow` survives**, so a spot-check using the capitalised form reports it clean |
| 2 | Compact groups | `\left(x+1\right)` → `` (annihilated) |
| 3 | 21-entry delimiter whitelist omits `\langle`/`\rangle` | `\left\langle x,y \right\rangle` → `\left. x, y \right.` |
| 4 | Evaluation bars | `\left. y \right\|_{x=0}` loses the bar **and** its subscript |
| 5 | `\Bar` → `\hat` | the originally-noted semantic corruption |
| … | `\,` → `\ ,`; no word boundaries (`\slashed{D}` → `/ed{D}`); `\textsubscript` deleted (`H\textsubscript{2}O` → `H{2}O`); `\upharpoonright` → `\harpoonright` (undefined); `\vline` → `\models` (a table rule becomes semantic entailment) | |

Plus a latent bug: the `align*` pattern is assembled by string concatenation, so the `*` is a **regex
quantifier** and `\begin{align*}` can never match.

**Measured on our own recorded outputs — 4 of 44 UniMERNet readings changed, 6 of 6 PaddleOCR-VL
readings changed, and every single change is damage. Not one improvement in either set.** PaddleOCR-VL
loses 6/6 because it emits `\[ … \]` and upstream breaks that delimiter every time. The worst case
destroys a *correct* reading:

```
in:  \[=|\alpha|^{n}\left(\cos(\omega n)+j\sin(\omega n)\right).\]
out: \ [=|\alpha|^{n}\left. n)+j\sin(\omega n)\right.
```

The `\cos(\omega` term is gone and the display math no longer compiles. UniMERNet never read that
equation correctly at all — across all 44 sweep records it degenerates to `\cos(\cos n)` and
`\sin(w \sin)` — so upstream's most destructive edit lands on the best reading either engine produced.

**Verdict: do not vendor.** We ship our own `latex_repair.py`.

### 2. `ocr-handler check` — the acceptance gate, engine-agnostic

`latex_repair.py` and `validity.py` were complete and tested but **reachable by nobody** — no CLI verb,
no call site. Now wired as a fourth verb, in the same free / no-GPU / writes-nothing family as `inspect`.

Compile-checking is dead (83 of 84 garbage outputs compiled). Eight detectors on the `Signal` roll-call
replace it. The report shows the **whole** roll-call — what fired, what ran and stayed quiet, and what
*could not run* (`length-vs-crop  not evaluated: no crop size supplied`) — because a report listing only
what fired cannot be checked for what it failed to look at. Repair is never applied without `--repair`,
and reports a per-rule roll-call plus the changed spans.

### 3. Recall: the hypothesis was wrong, and the real fix is better

The standing hypothesis — carried from the ground-truth sample — was that `_SHRED_MIN_RUN = 4` caused
the 35% recall, since a flattened fraction makes only 2–3 short lines. **Half wrong.** Of 12 labelled
misses, lowering the run to 3 reaches **1** and to 2 reaches **5**; the other seven are blocked by
`_SHRED_MAX_CHARS`. The case the ground-truth sample named as the sharpest argument for lowering does
not fire at 4, 3 **or** 2.

Lowering the run alone is the bad trade: strict precision collapses to **28%**, and 17 of 25 misfires
are **Wingdings bullets that map to ASCII `z`** plus assembly-listing gutters — both escaping through
`_is_symbolic`'s "a lone ASCII letter is a variable" clause. What paid for it was a *symbol* test
(`_is_strong`): every run must contain a line symbolic by an actual mathematical **character**, not by
the lone-letter or bare-`=` fallbacks.

| | before | after |
| --- | ---: | ---: |
| pages / documents flagged | 416 / 115 | **732 / 162** |
| strict precision | 84.8% [72, 92] | **93.1% [85, 96]** |
| broad precision | 97.8% | 95.2% |
| recall (fixed 999-page pool) | 35.3% | **68.2%** |
| corpus pass | 22 s | 22 s |

Priced, not hidden: ~46 corpus pages of non-mathematical 2-D loss (traceability matrices, decision
trees) now fire on nothing, and broad precision drops 98% → 95%.

### 4. `content-free` — the eighth detector

The new CLI immediately exposed a hole in its own spec. `\[\begin{aligned}\begin{aligned}\\ &\end{aligned}\\ \end{aligned}\]`
— **zero mathematics** — passed all seven detectors as `plausible`. Each was individually correct: 45
tokens (the tokeniser splits `{aligned}` into nine), variety 0.333, balanced structure, no repeated run.
It needed an eighth detector counting *content* tokens, floor pinned at 3 by `x = 1` (the shortest
legitimate reading is exactly three content tokens). Swept **2,654 readings** including 2,508 human
display-maths rows from every `.tex` file in `content/`: recall 1.00, precision 1.00.

Two alternatives were measured and rejected on the same counterexample — `\[\begin{aligned}x &= 1\end{aligned}\]`,
a legitimate short equation the model wrapped in scaffolding.

---

## Decisions made

| Decision | Rationale |
| --- | --- |
| **Do not vendor MinerU's `latex_rm_whitespace`** | 11 defects; over our own outputs every change it makes is damage. Verdict in [../research/INDEX.md](../research/INDEX.md) § Landmines is now *withdrawn* from the teardown's "worth vendoring" line |
| **`check` becomes a fourth CLI verb** | Its input is a recorded model output, not a PDF, so it cannot be a `--mode` of `extract`. [../scope.md](../scope.md) caps the CLI at five verbs and calls a new verb a scope question — flagged for the operator, at four of five |
| **Ship `_is_strong`, accept the broad-precision cost** | Recall 35% → 68% with strict precision *rising*; the cost is non-mathematical 2-D loss, priced above |
| **Do not lower `length-vs-crop`'s limit to catch content-free readings** | Margin collapses from ±4 to 0.35, the file-input path supplies no crop, and it is the wrong axis — the same string off a larger crop passes at any limit |
| **`_SHRED_MAX_CHARS` is unsettled, not decided** | Its sweep used a "control corpus" in which 44 of 49 hits are real mathematics, so recall was priced as cost |

---

## Discoveries

### The best reading in the project belongs to PaddleOCR-VL, not UniMERNet

A brief in this session asserted `tmp/eval/out_crops/` and `out_smoke/` were recorded UniMERNet outputs.
They are **PaddleOCR-VL-1.6**, from `tmp/eval/pvl.py`; the 44 UniMERNet records are in
`tmp/eqocr/sweep.json`. This propagated into a claim in `docs/research/INDEX.md` that the destroyed
`|\alpha|^n` string was "the mask-fed result … best of 84 [UniMERNet outputs]". It is not — that exact
string appears **only** in the two PaddleOCR-VL files. Corrected in place, and the corrected version is
stronger because both engines are now measured separately.

### `repair()` was changing text silently

`_QQUAD_RE` used `re.sub` and appended no note, so a real recorded reading came back altered with an
empty `notes` tuple — contradicting the spec, the docstring, **and a test named
`test_every_change_is_reported` that existed and did not cover it.** `\qquad` is load-bearing: it is the
token `ink.py` uses to mark a deliberately blank region. Fixed with `subn` + a note; the test was
widened from one string to an invariant over four; the CLI carries a tripwire for the class.

### Three inherited numbers did not reproduce

| Claim | Re-measured |
| --- | --- |
| token-variety catches 8/10 at zero FP | **2/10** under spacing-invariant tokenisation; it was scored with space-counting and only against other model outputs. The real winner is `length-vs-crop` (8/10, zero FP), which was not in the original list |
| unmapped-glyph volume 235 pages / 54 docs | **1,406 / 130** — off ~6×; no variant reproduces the original |
| "14.4 is under the highest good reading, 13.7" | **14.4 is above 13.7.** A limit of 14 *would* have caught the content-free reading. Lowering it is still wrong, for three different measured reasons |
| test suite is 111 | **114** before the change |

### The `ti` ligature is not dropped

Recorded as an open extraction defect (`anticipate` → `ancipate`). It extracts as **U+0017**, and the
`unmapped-glyphs` detector already catches it on **89 of 92 pages**. Closed. Rotated PowerPoint text is
undetectable from the string and is a density question, not a faithfulness one — closed as mis-filed.
Flattened superscripts (`7.50 × 10³ Pa` → `103 Pa`) **are** cheaply detectable geometrically; a
prototype catches 3 of 4 labelled rows, but it needs a `page` rather than a `str` in the `_DETECTORS`
signature and takes the corpus pass 22 s → 58 s. Specified, not shipped.

---

## Blockers

- **Engine choice is still open** — M3's head-to-head has not run. The acceptance gate is now built and
  engine-agnostic, so the head-to-head has something to score against.
- **`_SHRED_MAX_CHARS` needs a real control corpus** before it can be swept honestly.
- **Four new modules are untracked** — `crops.py`, `latex_repair.py`, `structure.py`, `validity.py`,
  plus `tools/` and `tests/fixtures/`. Git is human-only; reported, not resolved.

---

## Next

1. **M2 remains the leverage.** The extractor serves 430 documents; everything shipped this session
   serves the acceptance gate. Converge the two 400-char classifiers, then `extract --mode`.
2. **A `page`-aware detector signature** would unlock the flattened-superscript detector already
   prototyped, at a 22 s → 58 s corpus cost.
3. **Enumerate the `-plw` population** (22 pages, 2 documents) rather than sampling it.
4. **Operator call owed:** `check` puts the CLI at four verbs of five.

---

**See:** [../roadmap.md](../roadmap.md) · [../todo.md](../todo.md) ·
[../plans/latex-repair-and-validity.md](../plans/latex-repair-and-validity.md) ·
[../findings/recall-was-a-symbol-test-not-a-run-length.md](../findings/recall-was-a-symbol-test-not-a-run-length.md) ·
[../lessons_learned/lessons.md](../lessons_learned/lessons.md)

---
---

# Part 2 — same session, later: M2 converged, the mask question closed, the recall result audited

> **Appended, not revised.** Records here are immutable; Part 1 above is exactly as written. This
> session continued past it, and four more agents landed. Nothing in Part 1 is edited — where Part 2
> contradicts it, Part 2 says so explicitly.

## What was done

Four agents, scoped so none shared a file: one on `src/`, one on `docs/plans/`, two read-only on `src/`
writing `docs/findings/`. Every result verified independently before acceptance. No GPU, no model, no
ollama, no commits.

### 1. M2 delivered — and the "482 blank pages" figure was wrong everywhere

`pdfops` is now a view over `textlayer`; no poppler on the classification path. `extract --mode` and
`emit.py` ship. **142 tests** (was 120).

**The finding:** the `482 blank pages` figure quoted throughout these docs counted pages with no text
**and no images** — and never checked for vector content. Reproduced independently: **483 pages** under
the original rule, of which **406 carry vector drawings or XObject-painted images**. `lctr22-exercise.pdf`
p1 is 0 chars, 0 images, **1,837 vector paths and 8.9% non-white pixels**. The real skip set is **24**.
Those 406 pages were on track to be silently discarded as blank.

Two judgment calls worth recording because they went the harder way: `text` was **removed, not
aliased** (the agent grepped all of `electrical_notes` first and confirmed no external caller), and
`--dpi` / `--engine` / `--force` were **not shipped** because all three parameterise a path that does
not exist — a flag that silently does nothing is the dishonesty this project is built against.

### 2. The mask question — the premise of my own brief was wrong

I briefed that `ink.py`'s mask could not be built on P2/P3 because they lack a colour key and a twin.
**Both halves were wrong.** P3's ink is blue ballpoint over black print — a colour key, exactly
complementary to `dark_mask`. A usable mask is constructible on all three strata.

What does **not** transfer is the constants, and missing it would have been expensive:

| margin | `Worked Problems.pdf` p2 | `M17 Review.pdf` p2 |
| --- | ---: | ---: |
| 25 | 18,995 ink px | 20,893 |
| 55 — P1's `RED_MARGIN` | 6,296 | 4,766 |

**67–77% of the handwriting destroyed**, leaving a dotted skeleton. Invisible at page scale, obvious at
crop scale — so it would have been fed to a model and **scored as a model failure**. The structure
behind the fix: the locator dilates before labelling so it tolerates erosion but not contamination; the
paint is reproduced pixel-for-pixel, so its tolerances are exactly reversed. Two jobs, two margins.

**The `/Ink`-vs-raster contradiction is CLOSED — it is rasters.** Verified across all three annotated
lectures: **0 `/Subtype/Ink` objects**, 6 / 36 / 14 raster XObjects. The "7 `/Ink` objects" an early
note counted are opaque base64 blobs in vendor `/Private` dicts. This had blocked M4 for days because
only one of two recorded measurements could be right. `tmp_ocr_child.md` in the parent repo carries a
correction banner; its body is untouched (operator-owned note).

Also: **P1 is one document, not two** — `dsp-lctr1-…-plw.pdf` has 21 annotations (14 FreeText, 1
Highlight, 6 Line) and **no handwriting**; its red pixels are an arrow. And `diff_mask` needs no twin.

### 3. The engine backend design, and a live safety hole it found

`docs/plans/engine-backends.md`: `recognize.py` as the façade, `engines/<name>.py` as backends,
**explicit dict registration rather than discovery** — auto-discovery lets an engine become the default
by being the only one that imported successfully, which is ADR-0004's prohibition arriving through the
back door. Verb count does not move.

While reading `gpu_lock.py` for unrelated reasons it found that **the VRAM pre-flight guard was a no-op
on the deployment target**:

```python
free = free_vram_mib()                            # None when nvidia-smi fails
if free is not None and free < MIN_FREE_MIB: ...  # so: skipped, silently
```

`nvidia-smi` is broken on that host (kernel `580.159.03` vs userspace `580.173.02`), so the guard its
own docstring promised did not run and nothing said so — the silent-success failure this project exists
to catch, inside its own safety code. Fixed: `torch.cuda.mem_get_info` is tried **first** (unaffected by
broken NVML, so the guard now actually works there), and unknown is loud — it cannot say "unknown"
without saying why.

### 4. The recall result audited — precision replicates, the cost claim does not

Deliberately adversarial, and it worked.

**Precision replicates:** 90.0% [78.6, 95.7] and 88.9% [76.5, 95.2] on two fresh samples from unseen
documents; 93.1% sits inside both. With a **document-clustered bootstrap** — pages within one lecture
PDF are not independent — the honest floor is **~80%, not 93%**. It flagged its own draw as favourable.

**The priced cost was understated by 43% and misdescribed.** Enumerated rather than reweighted: **66
orphaned pages**, not ~46, and a seeded read found **35% [18, 57] are flattened mathematics** —
`W = ∫p dV`, `v_rms = √(3kT/m)`, a 3×3 matrix product. ~23 corpus pages of **real** loss.

**Root cause, verified here:** `_is_strong` is blind in the direction of its own target. A run of
`Z / p / dV` fires **nothing**, because when a fraction flattens the font often mangles the operator
with it — `∫`→`Z`, `√`→`r`, `Σ`→`X` — leaving no mathematical character at all.

**⚠ This corrects Part 1.** Part 1 records *"No strict true positive lost."* That is true of the
161-page sample and **false corpus-wide**. The change still stands on net — ~328 gained against ~23
lost — but "no cost" is not the claim to carry forward.

## Decisions made

| Decision | Rationale |
| --- | --- |
| **Exclude the declared-benign glyphs from `_is_strong`** | `unmapped-glyphs` calls U+F0B7/F070/F06C decorative while `_is_strong` counted them as proof of mathematics — an internal contradiction. Measured before applying: 732 → 729 pages, all three removed non-mathematical. Precision gain, no recall cost |
| **Keep `min_run 2` + `_is_strong` despite the real loss** | ~328 true positives gained against ~23 lost. Net strongly positive; the claim was wrong, not the change |
| **Guard proceeds on unmeasurable VRAM, loudly** | Refusing would make the tool useless on the exact machine the head-to-head runs on. An unguarded run must announce itself |
| **Drop the twin control from the head-to-head** | `diff_mask` reproduces it at IoU 1.0000 from the optional content group, and P1's second document has no handwriting |
| **State `paint` and locator per stratum** | P1's constants erode P3's ink by 67–77% |

## Discoveries

- **A maths-free control corpus is vacuous against this detector.** 13 documents / 47 pages of syllabi,
  assembly listings and rubrics fire **0 at every `_SHRED_MAX_CHARS` from 4 to 12** — with no character
  in `_SYMBOLIC_RANGES`, `_is_strong` can never pass. Such a corpus **bounds nothing**. A useful control
  must contain mathematics that is *not* flattened, and screening is unreliable: one candidate exam
  paper passed the screen and pages 2–3 were formula sheets.
- **`page.get_text()` splices FreeText annotation text into the body stream** — a fifth faithfulness
  fault no detector sees.
- **The corpus is measurably duplicated:** 459 documents carry **355 distinct text layers**; the 732
  flagged pages are **513 distinct pages**. Any per-document sample over-weights what is filed thrice.
- **The suspect total was a slip** — documented 959, remeasured **956**; every per-detector count
  reproduced exactly.
- **Six malformed Markdown table rows** repo-wide, from unescaped `|` inside inline code
  (`blue(25)|dark`, `\left. y \right|_{x=0}`). Two were written in Part 1 of this session. All fixed.

## Blockers

- **`nvidia-smi` is broken on the skytracker GPU host** — reported to that team; the fix is their
  operator's call. Per-arm VRAM cannot be measured on the target until then. Workaround: measure peaks
  on err0r's RTX 3060 and treat the target as a headroom check, saying which was done.
- **`_is_strong`'s mojibake blindness is not fixable from a `str`** — telling a mangled `∫` from a
  literal `Z` needs the **font**. It joins the flattened-superscript detector in the "needs a `page`,
  not a `str`" bucket.
- **Five modules exceed the ~300-line cap**, `cli.py` now 432. The seams are real but the axis is an
  operator call.

## Next

1. **Close M2 by retiring the three per-course scripts**, once parity is proven. That is what the
   milestone is actually for.
2. **Operator call: is a CPU `page-prose` backend in scope?** ADR-0004 defers only the handwritten-maths
   engine; OCRmyPDF/RapidOCR over ~400 `ps160` pages is zero verbs and zero GPU.
3. **M4 is unblocked** — build `structural_regions()` against the raster path, re-sweeping `RED_MARGIN`
   and `merge_px` per stratum.
4. **Build an honest control corpus** that contains unflattened mathematics, so `_SHRED_MAX_CHARS` can
   be swept against something that can actually fire.

---

**See:** [../findings/one-classifier-2026-09-06.md](../findings/one-classifier-2026-09-06.md) ·
[../findings/mask-separability-by-stratum-2026-09-06.md](../findings/mask-separability-by-stratum-2026-09-06.md) ·
[../findings/precision-replicates-the-priced-cost-does-not-2026-09-06.md](../findings/precision-replicates-the-priced-cost-does-not-2026-09-06.md) ·
[../plans/engine-backends.md](../plans/engine-backends.md) ·
[../research/stage2-slate-and-head-to-head-2026-09-06.md](../research/stage2-slate-and-head-to-head-2026-09-06.md)
