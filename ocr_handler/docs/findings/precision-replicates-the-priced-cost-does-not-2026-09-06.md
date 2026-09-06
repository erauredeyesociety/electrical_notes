# Precision replicates on unseen documents. The priced cost does not.

**Type: FINDING (internal).** Measured 2026-09-06 against `content/` — **459 documents / 7,198 pages**,
independently of the session that made the change.
**Audits:** [recall-was-a-symbol-test-not-a-run-length.md](./recall-was-a-symbol-test-not-a-run-length.md)
(the 2026-09-06 `_SHRED_MIN_RUN` 4 → 2 + `_is_strong` change) ·
[ground-truth-sample.md](./ground-truth-sample.md) § 5 (the `-plw` census it asked for) ·
[../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) § 3.2 (the "control corpus").
**New hand labels: 115 pages**, all read as 100–110 dpi renders against their own extracted text —
50 + 45 flagged pages drawn from documents in **neither** existing label set, 20 pages the change
silently dropped, and 67 pages read to build a control corpus that is actually a control.
**Changes no code.** `src/` belongs to another agent this session; nothing here was fixed, only measured.

Nothing ran a model or touched the GPU. Four `nice -n 19` CPU passes: 43 s (text cache), 22 s, 25 s, 31 s.

---

## 0 · The headline

| claim under audit | shipped figure | measured here | verdict |
| --- | ---: | ---: | --- |
| strict precision | **93.1%** | **90.0%** [79, 96], n = 50 / 35 docs | **replicates** |
| …on content never labelled before | — | **88.9%** [77, 95], n = 45 / 31 docs | **replicates** |
| broad precision | 95.2% | 96.0% [87, 99] and 93.3% [82, 98] | **replicates** |
| corpus pages the change gives up | "**~46**, non-mathematical" | **66 pages**, enumerated | **understated by 43%** |
| …and they are non-mathematical | "traceability matrices, decision trees" | **~35% of them are flattened mathematics** [18, 57] | **wrong** |
| "No strict true positive … was lost" | true of the 161-row sample | **false corpus-wide** — ~23 pages [12, 37] | **wrong** |
| the `-plw` population | "22 pages in 2 documents, 5 flagged suspect" | 22 pages in 2 documents, **7** flagged | count moved with the change |
| `-plw` = the ink-annotated documents | implied by the census | **neither has a single `/Ink` annotation** | **wrong** |
| suspect pages, all four detectors | 959 (13.3%) | **963** (13.4%) | small arithmetic slip |

**The change is sound and the precision claim is real.** The part that does not survive is the *price*:
the paragraph that says the loss is 46 pages of non-mathematical 2-D structure is wrong on both the
number and the kind. Roughly a third of what was given up is exactly what the detector exists for —
a Σ with limits, a ∫ with limits, `v_rms = √(3kT/m)`, `1/s + 1/s′ = 1/f`, a 3×3 matrix product.

---

## 1 · How the samples were drawn, and why the obvious draw is not honest

Every flagged page in the corpus was enumerated at the shipped setting (732 pages / 162 documents —
reproduces exactly). Two nested populations were then defined:

| population | definition | size |
| --- | --- | ---: |
| **U** | flagged pages in documents whose **path** appears in neither `sample.csv` nor `shred_sweep_labels.csv` | **278 pages / 83 docs** |
| **F** | the subset of U whose document's **content** is also absent — no byte-identical and no text-layer-identical twin among the 128 labelled documents | **150 pages / 62 docs** |

**F exists because U is not what it looks like.** `content/` files the same lecture PDF under
`all_lectures/`, `exam2/lectures/` and `homework/hw4/`; **21 of U's 83 "unseen" documents are exact
content duplicates of a document that has already been labelled**, and they carry 128 of U's 278 pages.
A draw from U alone would report a number partly re-measured on pages the original reader had seen.

- **Sample A** — simple random sample of 50 from U, `random.Random("unseen-validation-2026-09-06")`,
  drawn over the enumeration sorted by `(pdf, page)`. No per-document cap: a cap makes the estimator
  biased for a page-level rate unless it is reweighted, and the concentration is reported below instead.
- **Sample B** — simple random sample of 45 from F, `random.Random("content-fresh-validation-2026-09-06")`.
  Six of B's pages were already in A and reuse their labels.

**Both draws are favourable to the detector and that is worth saying plainly.** U is dominated by
`cec_315` (a signals-and-systems course whose lecture notes are LaTeX-set and wall-to-wall integrals):
29 of A's 50 pages come from it. If the flagged population outside `cec_315` were much worse, these
samples would understate it. Against that, sample B spans 31 documents across **8** courses and only 9 of its 45 pages are `cec_315`.

Every page was **rendered and read**, then checked against its own extracted text, using the label
vocabulary of [ground-truth-sample.md](./ground-truth-sample.md) § 0 — `genuine`,
`genuine-wrong-evidence` (both strict hits), `partial` (broad only), `misfire`. Calls were calibrated
against the 75 existing rows of
[`shred_sweep_labels.csv`](../../tests/fixtures/ground_truth/shred_sweep_labels.csv): where this reader
met a run the earlier reader had already judged (`√ / …`, `Z +∞ / −∞`, `9 / ˆ`, `∆S = / kJ/K`,
`B / s −3`), the same call was made.

---

## 2 · Strict precision, independently

| | n | docs | strict | Wilson 95% | document-clustered bootstrap 95% |
| --- | ---: | ---: | ---: | --- | --- |
| **A** — unseen by path (pop. 278) | 50 | 35 | **90.0%** | [78.6%, 95.7%] | [81.1%, 97.8%] |
| **B** — unseen by content (pop. 150) | 45 | 31 | **88.9%** | [76.5%, 95.2%] | [77.5%, 97.9%] |

| | A | B |
| --- | ---: | ---: |
| `genuine` | 38 | 39 |
| `genuine-wrong-evidence` | 7 | 1 |
| `partial` | 3 | 2 |
| `misfire` | 2 | 3 |
| **strict** | **45/50 = 90.0%** | **40/45 = 88.9%** |
| **broad** | 48/50 = 96.0% [86.5, 98.9] | 42/45 = 93.3% [82.1, 97.7] |
| **evidence also correct** | 38/50 = 76.0% [62.6, 85.7] | 39/45 = 86.7% [73.8, 93.7] |

**93.1% sits inside both intervals.** The point estimates land 3 and 4 points below it, which is what
two samples of this size should do around a true value near 90%; nothing here says the shipped number
is wrong, and nothing says it is precisely right either. The clustered bootstrap — resampling
*documents*, not pages, because a lecture PDF's pages are not independent draws — widens the lower
bound to 81% and 78%. **Read the honest floor as "at least about 80%", not "93%".**

The strict misses across the two samples — **nine distinct pages**, all read:

| page | run | why it fires, and why it is not mathematics |
| --- | --- | --- |
| `cec_315/exam2/lectures/…lctr14…` p11 | `ωp / ωc / ωs / 0 / −δp` | a filter-spec **figure's axis labels**; every equation on the page is inline (`partial`) |
| `cec_315/homework/hw4/…lctr14… (2)` p5 | `−4 / −2 / 2 / 4 / −π / −π/2 / π/2 / π` | two phase plots' **axis ticks**; no display maths anywhere on the page (`partial`) |
| `cec_320/lectures/mp-de-lctr7…` p5 | `9 / ˆ` | a C **operator-precedence table** (`partial`; the earlier reader called the same run the same way) |
| `ps160/midterm_02/Midterm_2_sp_24.pdf` p9 | `∆S / J/K` | an **exam answer blank** — `∆S ▢ J/K`. Nothing lost (`misfire`) |
| `syse_301/Systems-Eng-Guidebook…-slp.pdf` p26 | `18 / U+F0A7` | a **page number and a Wingdings square bullet**. Pure prose page (`misfire`) |
| `sys_304/…07 Simulation Approaches 1.pdf` p6 | `U+F06D / U+F073` | Symbol-font `μ` and `σ`, two **underbrace labels** under an Excel formula. The brace-to-argument mapping is lost, but it is not mathematics (`partial`) |
| `ae318/…AE318 8 Apr 2026 lecture slides.pdf` p4 | `U+F050 / U+F050` | two Symbol-font glyphs; the page's maths is **in images**, so it is a `sparse` page, not a shredded one (`misfire`) |
| `ps160/midterm_03/test_finalexam_DRAFT…fall.pdf` pp. 9, 11 | `∆L = / mm`, `∆S = / kJ/K` | **exam answer blanks** again (`misfire`) |

**Two of the five misfires are the same mechanism and it is a hole in `_is_strong`** — see § 6.2.
**Three more are one shape: an exam answer blank.** `∆S ▢ J/K` extracts as `∆S` / `J/K`, a two-line run
whose first line carries a genuine mathematical character. There is no 2-D structure and nothing is
lost. At `_SHRED_MIN_RUN = 4` this class could not fire; at 2 it is the commonest false positive this
audit saw, and it will grow with `_SHRED_MAX_CHARS`.

### 2.1 Every label, so any call can be re-checked

The rows below are this document's data. They cannot go in `tests/fixtures/ground_truth/` — that tree
was gitignored on 2026-09-06 — so they live here, one row per page, naming the run that was judged.

### SAMPLE A

| # | document | p | run | label |
| ---: | --- | ---: | --- | --- |
| 0 | `ae318/AE318_export/AE318 23 Mar 2026 lecture slides.pdf` | 3 | `𝐼𝑦𝐼𝑧 / •` | genuine |
| 1 | `cec_315/all_lectures/cec315-lctr03-complex-nums-exp-n-sinusoidal-sigs.pdf` | 3 | `√ / −1.` | genuine |
| 2 | `cec_315/all_lectures/cec315-lctr03-complex-nums-exp-n-sinusoidal-sigs.pdf` | 4 | `𝑟= / √` | genuine |
| 3 | `cec_315/all_lectures/cec315-lctr15-systems-bode-examples.pdf` | 8 | ` / −πζ / √ / 1−ζ2 / ` | genuine |
| 4 | `cec_315/all_lectures/cec315-lctr20-inverse-z-transform-properties.pdf` | 4 | `×0.5 / × / 2` | genuine-wrong-evidence |
| 5 | `cec_315/exam1/lectures/cec315-lctr08-diff-eqns-singularity.pdf` | 6 | `2 / 1 / 2 / ` | genuine |
| 6 | `cec_315/exam1/lectures/cec315-lctr08-diff-eqns-singularity.pdf` | 10 | `Z t / −∞` | genuine |
| 7 | `cec_315/exam2/lectures/cec315-lctr09-ct-fourier-series.pdf` | 3 | `Z ∞ / 0` | genuine |
| 8 | `cec_315/exam2/lectures/cec315-lctr09-ct-fourier-series.pdf` | 17 | `+∞ / X / k=−∞` | genuine |
| 9 | `cec_315/exam2/lectures/cec315-lctr11-frequency-response-filtering.pdf` | 16 | `Z +∞ / −∞` | genuine |
| 10 | `cec_315/exam2/lectures/cec315-lctr12-fourier-transforms.pdf` | 3 | `def / = / Z +∞ / −∞` | genuine |
| 11 | `cec_315/exam2/lectures/cec315-lctr14-magnitude-phase-filters.pdf` | 3 | `Z +∞ / −∞` | genuine |
| 12 | `cec_315/exam2/lectures/cec315-lctr14-magnitude-phase-filters.pdf` | 7 | `dω / U+0002` | genuine |
| 13 | `cec_315/exam2/lectures/cec315-lctr14-magnitude-phase-filters.pdf` | 11 | `ωp / ωc / ωs / 0 / −δp` | partial |
| 14 | `cec_315/exam3/lectures/cec315-lctr16-laplace-transform-roc.pdf` | 6 | `σ / jω / ×` | genuine-wrong-evidence |
| 15 | `cec_315/exam3/lectures/cec315-lctr16-laplace-transform-roc.pdf` | 8 | `σ / jω / ×` | genuine-wrong-evidence |
| 16 | `cec_315/exam3/lectures/cec315-lctr17-inverse-laplace-properties.pdf` | 4 | `B / s −3` | genuine |
| 17 | `cec_315/exam3/lectures/cec315-lctr17-inverse-laplace-properties.pdf` | 7 | `σ / jω / × / p1 / × / p∗ / 1 / z1` | genuine-wrong-evidence |
| 18 | `cec_315/exam3/lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf` | 3 | `σ / jω / × / −2 / × / −3 / −1/2` | genuine-wrong-evidence |
| 19 | `cec_315/exam3/lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf` | 4 | `Z +∞ / −∞` | genuine |
| 20 | `cec_315/exam3/lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf` | 5 | `σ / jω / × / × / × / ROC` | genuine-wrong-evidence |
| 21 | `cec_315/exam3/lectures/cec315-lctr19-z-transform-roc.pdf` | 10 | `Z ∞ / −∞` | genuine |
| 22 | `cec_315/exam3/lectures/cec315-lctr22-sampling.pdf` | 3 | `−ωM / ωM / 0 / −ωs / ωs / 1 / T / gap` | genuine-wrong-evidence |
| 23 | `cec_315/exam3/lectures/cec315-lctr22-sampling.pdf` | 5 | `πt / .` | genuine |
| 24 | `cec_315/homework/hw4/cec315-hw-lctr12-15.pdf` | 2 | `= / Z +∞ / −∞` | genuine |
| 25 | `cec_315/homework/hw4/cec315-lctr14-magnitude-phase-filters (2).pdf` | 3 | `Z +∞ / −∞` | genuine |
| 26 | `cec_315/homework/hw4/cec315-lctr14-magnitude-phase-filters (2).pdf` | 5 | `−4 / −2 / 2 / 4 / −π / −π/2 / π/2 / π` | partial |
| 27 | `cec_315/homework/hw4/cec315-lctr15-systems-bode-examples.pdf` | 8 | ` / −πζ / √ / 1−ζ2 / ` | genuine |
| 28 | `cec_315/homework/hw4/cec315-lctr15-systems-bode-examples.pdf` | 12 | `ωn = / p` | genuine |
| 29 | `cec_315/hw_practice_problems/lctr07-convolution-problems.pdf` | 1 | `Z ∞ / −∞` | genuine |
| 30 | `cec_320/lectures/mp-de-lctr7-bitwise-ops-n-gpio-reg-access-slides-2026-01 (1).pdf` | 5 | `9 / ˆ` | partial |
| 31 | `cesc_410/hw/hw01/overleaf/p04_periodicity.pdf` | 1 | `√ / 8)` | genuine |
| 32 | `cesc_410/hw/hw01/p06_convolution.pdf` | 2 | `1−aN / 1−a` | genuine |
| 33 | `cesc_410/hw/hw01/p06_convolution.pdf` | 3 | `n ≥0 / 0,` | genuine |
| 34 | `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 12 | `𝑁−1 / ∑︁ / 𝑛=0` | genuine |
| 35 | `cesc_470/hw/hw01/hw01_solutions.pdf` | 3 | `=⇒ / S = / 1` | genuine |
| 36 | `ee_300/exam_final/final_cheatsheet.pdf` | 5 | `𝑘𝑓 / ,` | genuine |
| 37 | `ee_300/exam_final/final_quiz_examples.pdf` | 4 | `2000 / √` | genuine |
| 38 | `ee_300/exam_final/final_quiz_examples.pdf` | 5 | `𝛼 / 𝑠+𝛼` | genuine |
| 39 | `ee_300/exam_final/final_quiz_examples.pdf` | 9 | `𝑅= / 1` | genuine |
| 40 | `ps160/m15/chapter_15.pdf` | 5 | `x / v −t / ` | genuine |
| 41 | `ps160/m18/CH18_ADA_PPT_LectureOutline.pdf` | 9 | `( / ) / 2 / 2 / an / p / V / nb / nRT / V /  /  / + / − / ` | genuine |
| 42 | `ps160/m20/CH20_ADA_PPT_LectureOutline.pdf` | 22 | `H / C / \| / \| / Q / Q / −` | genuine |
| 43 | `ps160/midterm_01/knowledge_ps160_mid01.pdf` | 1 | `ω = / r / k / m / ω = / rg / ℓ / ω = / r / mgd / I` | genuine |
| 44 | `ps160/midterm_02/Midterm_2_sp_24.pdf` | 9 | `∆S / J/K` | misfire |
| 45 | `stat_412/HW07/solutions/q04.pdf` | 1 | `3.4/ / √` | genuine |
| 46 | `stat_412/HW08/solutions/q09.pdf` | 1 | `SE = / √ / 1572` | genuine |
| 47 | `stat_412/QZ08/solutions/q06.pdf` | 1 | `4.4 / 11.6 / Then / χ2 =` | genuine |
| 48 | `stat_412/QZ08/solutions/q09.pdf` | 1 | `SE = / √` | genuine |
| 49 | `syse_301/Systems-Eng-Guidebook_Feb2022-Cleared-slp.pdf` | 26 | `18 / U+F0A7` | misfire |

### SAMPLE B

| # | document | p | run | label |
| ---: | --- | ---: | --- | --- |
| B00 | `ae318/AE318_export/AE318 13 Mar 2026 lecture slides.pdf` | 10 | `𝑑𝜎𝑥 / 𝑑𝑥𝑑𝑥` | genuine |
| B01 | `ae318/AE318_export/AE318 8 Apr 2026 lecture slides.pdf` | 4 | `U+F050 / U+F050` | misfire |
| B02 | `cec_315/all_lectures/cec315-lctr20-inverse-z-transform-properties.pdf` | 8 | `n / X / k=−∞ / x[k] / 1` | genuine |
| B03 | `cec_315/exam1/CEC_315_exam_1.pdf` | 2 | `∞ / X / k=−∞` | genuine |
| B04 | `cec_315/exam1/lectures/cec315-lctr03-complex-nums-exp-n-sinusoidal-sigs.pdf` | 3 | `√ / −1.` | genuine |
| B05 | `cec_315/exam2/cec315-EXAM2-1.pdf` | 6 | `ω2 / n` | genuine |
| B06 | `cec_315/exam3/lectures/cec315-lctr20-inverse-z-transform-properties.pdf` | 8 | `n / X / k=−∞ / x[k] / 1` | genuine |
| B07 | `cec_315/exam3/lectures/cec315-lctr21-system-analysis-unilateral-z.pdf` | 4 | `Re / Im / × / × ×` | genuine-wrong-evidence |
| B08 | `cec_315/exam3/lectures/cec315-lctr21-system-analysis-unilateral-z.pdf` | 6 | `∞ / X / n=0` | genuine |
| B09 | `cec_315/hw_practice_problems/lctr06-convolution-problems.pdf` | 2 | `U+F8F1 / U+F8F4 / U+F8F4 / U+F8F4 / U+F8F2 / U+F8F4 / U+F8F4` | genuine |
| B10 | `cec_315/hw_practice_problems/lctr22-exercise-solutions.pdf` | 2 | `T = / 2π` | genuine |
| B11 | `cec_320/homework/hw11-hche--if-based-flow-control-soln-26-04.pdf` | 3 | `10, / 𝑥≥5, / 2𝑥,` | genuine |
| B12 | `cec_320/lectures/mp-cg--lctr4-data-representation-slides-26-01 (1).pdf` | 4 | `¯𝛼5 / -1` | genuine |
| B13 | `cec_320/lectures/mp-de-lctr7-bitwise-ops-n-gpio-reg-access-slides-2026-01 (1).pdf` | 5 | `9 / ˆ` | partial |
| B14 | `cesc_410/hw/hw01/dsphw26-hw1.pdf` | 1 | `√ / 8).` | genuine |
| B15 | `cesc_410/hw/hw01/p06_convolution.pdf` | 1 | `∞ / X / k=−∞` | genuine |
| B16 | `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 9 | `( / 0, / 𝑡≠0, / ∞,` | genuine |
| B17 | `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 10 | `𝑇 / ∞ / ∑︁ / 𝑘=−∞` | genuine |
| B18 | `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 11 | `𝑁−1 / ∑︁ / 𝑛=0` | genuine |
| B19 | `ee_300/exam_final/final_cheatsheet.pdf` | 2 | `𝑄𝑘= / 1 / 2𝜁𝑘` | genuine |
| B20 | `ee_300/exam_final/final_cheatsheet.pdf` | 3 | `𝑅= / 1 / 𝜔0𝐶` | genuine |
| B21 | `ee_300/exam_final/final_cheatsheet.pdf` | 5 | `𝑘𝑓 / ,` | genuine |
| B22 | `ee_300/exam_final/final_quiz_examples.pdf` | 1 | `1 / 𝑠𝐶 / 𝑅𝑓+ / 1 / 𝑠𝐶 / = / 𝑅𝑓` | genuine |
| B23 | `ee_300/exam_final/final_quiz_examples.pdf` | 4 | `2000 / √` | genuine |
| B24 | `ee_300/exam_final/final_quiz_examples.pdf` | 10 | `𝑅= / 1` | genuine |
| B25 | `ps160/m15/chapter_15.pdf` | 5 | `x / v −t / ` | genuine |
| B26 | `ps160/m15/chapter_15.pdf` | 9 | `Area / = / P / 4πR2` | genuine |
| B27 | `ps160/m15/chapter_15.pdf` | 14 | `t / U+0003` | genuine |
| B28 | `ps160/m17/CH17_ADA_PPT_LectureOutline.pdf` | 15 | `U+F061 / − / U+F0B0 / 5` | genuine |
| B29 | `ps160/m17/chapter_17.pdf` | 8 | `∆L / Lo / ` | genuine |
| B30 | `ps160/m18/M18_Review-1.pdf` | 9 | `CV = / Q / n∆T` | genuine |
| B31 | `ps160/m19/chapter_19.pdf` | 3 | `V2 / V1 / ` | genuine |
| B32 | `ps160/m33,34,35,36/CH34_ADA_PPT_LectureOutline-1.pdf` | 6 | `s / s / = −` | genuine |
| B33 | `ps160/m33,34,35,36/CH34_ADA_PPT_LectureOutline-1.pdf` | 10 | `1 / 1 / 2 / s / s / R / + / = / ` | genuine |
| B34 | `ps160/m33,34,35,36/CH34_ADA_PPT_LectureOutline-1.pdf` | 24 | `0 / a / b / n / n / s / s / + / = / ` | genuine |
| B35 | `ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` | 3 | `1 / 2m /  v2` | genuine |
| B36 | `ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` | 9 | `∆L = / mm` | misfire |
| B37 | `ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` | 11 | `∆S = / kJ/K` | misfire |
| B38 | `stat_412/HW07/solutions/q12.pdf` | 1 | `√ / 110 / .` | genuine |
| B39 | `stat_412/HW07/solutions/q13.pdf` | 1 | `ˆp = / 99` | genuine |
| B40 | `stat_412/HW08/solutions/q09.pdf` | 1 | `SE = / √ / 1572` | genuine |
| B41 | `stat_412/QZ08/solutions/q06.pdf` | 1 | `4.4 / 11.6 / Then / χ2 =` | genuine |
| B42 | `stat_412/QZ08/solutions/q08.pdf` | 1 | `sp = / √` | genuine |
| B43 | `sys_304/class_materials/07 Simulation Approaches 1.pdf` | 6 | `U+F06D / U+F073` | partial |
| B44 | `sys_304/class_materials/07 Simulation Approaches 1.pdf` | 11 | `)) / ( / 1( / 2 / )) / ( / ( / ) / ( / ) / ( / 2 / i / i / i` | genuine |


---

## 3 · The `-plw` population, enumerated

[ground-truth-sample.md](./ground-truth-sample.md) § 5 asked for this and said why: "22 pages in 2
documents is not a population to sample; it is a population to enumerate." Both documents, every page:

### 3.1 `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` — 12 pages

pdfTeX / "LaTeX via pandoc with the Eisvogel template". Density `ocr-partial`, structure
`structure-suspect-partial`. `redpx` = pixels passing `ink.red_mask` at 110 dpi, beside the same count
on its **un-annotated twin** `…-26-08-26.pdf` (same 12 pages, 0 annotations).

| p | chars | density | annots | redpx (plw) | redpx (twin) | detectors, and the run |
| ---: | ---: | --- | --- | ---: | ---: | --- |
| 1 | 3224 | ok | — | 0 | 0 | — |
| 2 | 1554 | ok | — | 0 | 0 | — |
| 3 | 922 | ok | 1 FreeText | 5 | 0 | — |
| 4 | 961 | ok | — | 0 | 0 | `shredded-lines` — `𝑗= / √ / −1.` |
| 5 | 2145 | ok | 3 FreeText | 345 | 0 | `shredded-lines` — `C(𝑡) / 2 / , / = 𝐴` |
| 6 | 128 | **sparse** | — | 448 | **448** | — |
| 7 | 726 | ok | 1 Highlight, 1 Line | 796 | **448** | — |
| 8 | 1799 | ok | 2 FreeText, 2 Line | 833 | 0 | `shredded-lines` — `𝑃 / ∫ / 𝑃` |
| 9 | 1234 | ok | 5 FreeText, 1 Line | 117 | 0 | `shredded-lines` — `( / 0, / 𝑡≠0, / ∞,` (a `cases` brace) |
| 10 | 1614 | ok | 3 FreeText, 2 Line | 583 | 0 | `shredded-lines` — `𝑇 / ∞ / ∑︁ / 𝑘=−∞` |
| 11 | 1342 | ok | — | 891 | **891** | `shredded-lines` — `𝑁−1 / ∑︁ / 𝑛=0` |
| 12 | 693 | ok | — | 0 | 0 | `shredded-lines` + `unmapped-glyphs` — `𝑁−1 / ∑︁ / 𝑛=0`; `U+F8F4×4, U+F8F1, U+F8F2, U+F8F3` |

All 7 `shredded-lines` calls were read and all 7 are **genuine** (three of them appear in sample B as
B16, B17, B18). The annotations are **14 FreeText ("Typewriter"), 6 Line, 1 Highlight, by author `jhl`**.

### 3.2 `cesc_410/lectures/f26_lctr02_DT signals and systems-plw.pdf` — 10 pages

"PDF Annotator 10.0.0.1011 [GPL Ghostscript 9.06]" over "PScript5.dll". Density **`ocr-required`**,
structure **`structure-intact` — no detector fires on any page**.

| p | chars | density | images | drawings | annots | redpx (plw) | redpx (twin) |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 295 | sparse | 0 | 119 | 0 | 0 | 0 |
| 2 | 132 | sparse | 4 | 114 | 0 | 2101 | 0 |
| 3 | 73 | sparse | 3 | 114 | 0 | 1585 | 0 |
| 4 | 41 | sparse | 5 | 117 | 0 | 3705 | 0 |
| 5 | 41 | sparse | 3 | 114 | 0 | 3095 | 0 |
| 6 | 164 | sparse | 6 | 114 | 0 | 4685 | 0 |
| 7 | 109 | sparse | 4 | 114 | 0 | 4674 | 0 |
| 8 | 156 | sparse | 4 | 114 | 0 | 0 | 0 |
| 9 | 212 | sparse | 6 | 114 | 0 | 315 | 0 |
| 10 | 116 | sparse | 1 | 114 | 0 | 0 | 0 |

### 3.3 What the census says, and one inherited claim it kills

1. **22 pages / 2 documents confirmed**, and **11 pages under 400 chars** as recorded — but **7 pages
   flagged suspect, not 5.** The 2026-09-06 change added two (`dsp-lctr1` pp. 4 and 12); the census
   figure was taken before it and is not wrong, only stale. Worth pinning because this is a fixed,
   fully-enumerated population, so it is the cheapest regression check in the repo.

2. **Neither `-plw` document contains a single `/Ink` annotation.** Scanning every annotation object in
   all 459 corpus documents:

   | document | annotations |
   | --- | --- |
   | `cec_300/exam1/nelsongatlin_446926_46576077_cec300_hw02.pdf` | **Ink × 14** |
   | `cesc_410/lectures/dsp-lctr1-…-plw.pdf` | FreeText × 14, Line × 6, Highlight × 1 |
   | `cesc_470/Module 01 Introduction to computer technology & ISA (1).pdf` | FreeText × 3 |
   | `sys_304/class_materials/SYS 304 Test 1 Fall 2026 - Key.pdf` | Stamp × 9 |

   Four documents carry annotations at all; **the only one with `/Ink` objects is a student homework
   submission that nobody has looked at.** The corpus census's "only 2 documents in the whole repo are
   ink-annotated" (quoted in [INDEX.md](./INDEX.md)) is not true of `/Ink`: the two `-plw` files are one
   set of *typed* comments and arrows, and one file whose annotations Ghostscript **flattened into page
   content** — which is why doc 2 has no annotation objects, 114 vector paths per page, and 2,000–4,700
   red pixels on 7 of its 10 pages. This does not break `ink.py`, which works on rendered pixels rather
   than annotation objects, but it does mean the two documents are two *different* problems and the
   second one is a `sparse` document, not a `suspect` one.

3. **`ink.py`'s red mask cannot separate ink from content on document 1.** On pages 6 and 11 the
   un-annotated twin carries **exactly the same** red pixel count (448 and 891) — the red is prepared
   slide content. On page 7, 448 of 796 red pixels are the twin's. Doc 2 is clean: 0 red on the twin
   everywhere. **The difference method works; the colour method does not, on this document.**

4. **`page.get_text()` splices FreeText annotation text into the body stream with no marker.**
   Diffing `dsp-lctr1-…-plw.pdf` p10 against its twin, the extraction gains exactly
   `-`, `the chance to`, `recover the`, `original`, `that` — the instructor's typed marginal comments,
   now indistinguishable from the lecture text. That is a *faithfulness* fault of a fifth kind: the text
   layer gains content that was never prepared content, and none of the four detectors can see it.
   Small here (42 characters on one page, ~115 across the document) but it is a silent corruption of the
   one document class the ink pipeline exists for.

---

## 4 · The priced cost, enumerated instead of reweighted

The change was accepted with this price, from
[recall-was-a-symbol-test-not-a-run-length.md](./recall-was-a-symbol-test-not-a-run-length.md) § 3.1:

> **This is a real loss and it is not mathematics.** Broad precision falls 98% → 95%, and the ~46 corpus
> pages of that class … now fire on nothing.

and this, from § 3.2: **"No strict true positive in the sample was lost."**

The 46 is a reweighting of 5 `partial` rows out of 46 labelled onto 416 corpus pages. It does not need
to be estimated — the dropped set is a pure function of the corpus and can be listed:

| | pages | documents |
| --- | ---: | ---: |
| flagged at the old setting (`max_chars 4, min_run 4`, no `_is_strong`) | 416 | 115 |
| flagged at the shipped setting (`min_run 2` + `_is_strong`) | 732 | 162 |
| **gained** by the change | **390** | |
| **dropped** by the change | **74** | |
| …still suspect via `unmapped-glyphs` (4) or `vertical-letter-spaced` (4) | 8 | |
| **orphaned — now fire on nothing at all** | **66** | 27 |

**66, not ~46.** The reweighted estimate was 43% low, because the 46 labelled rows it was projected from
contained no `cec_315`, no `ps160` chapter and no `ae318` slide of the kind that dominates the real
dropped set.

### 4.1 And a third of them are mathematics

A simple random sample of 20 of the 66 (`random.Random("orphan-cost-2026-09-06")`) was rendered and read:

| what the page is | n | rate | 95% CI | extrapolated to 66 |
| --- | ---: | ---: | --- | ---: |
| **flattened mathematics — a strict true positive, now invisible** | **7** | **35%** | [18%, 57%] | **23 pages** [12, 37] |
| non-mathematical 2-D loss — the class that was priced | 10 | 50% | [30%, 70%] | 33 pages [20, 46] |
| misfire correctly removed — a **gain**, not a cost | 3 | 15% | [5%, 36%] | 10 pages [3, 24] |

The seven mathematical losses, read:

| page | run | what is on the page |
| --- | --- | --- |
| `ae318/…AE318 25 Mar 2026 lecture slides.pdf` p10 | `= 0 / q / q / q` | three nested fractions filling the slide, `q = […]/(I_y I_z − I_yz²)` — the whole page is the equation |
| `cec_315/…lctr18-system-analysis-unilateral-laplace.pdf` p2 | `N / X / k=0 / ak / dky` | `Σ_{k=0}^{N} a_k dᵏy/dtᵏ = Σ_{k=0}^{M} b_k dᵏx/dtᵏ` — a summation with limits **and** a derivative fraction (also present as an exact duplicate under `exam3/lectures/`) |
| `ps160/m18/chapter_18.pdf` p8 | `r / 3kT / m / = / r / 3RT / M` | `v_rms = √(3kT/m) = √(3RT/M)`; `√` extracted as `r` |
| `ps160/m19/chapter_19.pdf` p2 | `W = / Z V2 / V1 / p dV` | `W = ∫_{V₁}^{V₂} p dV`; `∫` extracted as `Z` |
| `ps160/m20/CH20_ADA_PPT_LectureOutline.pdf` p16 | `C / \| / \| / \| / \| / Q / W` | `K = \|Q_C\|/\|W\| = \|Q_C\|/(\|Q_H\| − \|Q_C\|)`, a MathType equation in fragments |
| `sys_304/…03 Analytic Hierarchy Process_Handout.pdf` p9 | `CR / CI / RI / = / = / =` | `CR = CI/RI = 0.0270/0.58 = 0.0466` |
| `sys_304/…03 The Analytic Hierarchy Process.pdf` p24 | `3 / 1 / 2 / x / 0.55 / =` | a 3×3 **matrix product** `[A][B] = [C]` plus a row of quotients — the canonical target |

Ten more of the 66 that were *not* drawn have runs of the same shape and are very likely the same class:
`ps160/m19/chapter_19.pdf` p12 (`CV / dV / V / = 0 / R / CV`), `ps160/m20/CH20…` pp. 11, 25, 31
(`dQ / dS / T / =` — that is `dS = dQ/T`), `ps160/m33,34,35,36/M33-36_Review.pdf` p16
(`s′ / 1 / f = / 1` — the lens equation), `ps160/m14/YF15e_CH14…` p26
(`2 / 2 / 2 / x / E / mv / kx / kA / = / + / = / =` — `E = ½mv² + ½kx² = ½kA²`),
`cec_315/…lctr14…` p10 ×3, `cesc_470/hw/hw01/p09_cpi_and_execution_time.pdf` p1.

**"No strict true positive in the sample was lost" was true of the 161-page sample and is false of the
corpus.** The sample simply had none of these pages in it — which is the same structural weakness this
audit was asked to look for, appearing one level down.

### 4.2 The other two halves of the price do verify

- **Broad precision.** Claimed 97.8% → 95.2%. Measured on unseen documents: **96.0%** [86.5, 98.9]
  (sample A) and **93.3%** [82.1, 97.7] (sample B). 95.2% is inside both. **Verified.**
- **The `partial` class is real and is the plurality of the loss.** 10 of 20, extrapolating to ~33 pages:
  seven `sys_304` decision trees, nine `A / B / C / D` matrix headers, the INCOSE Figure 2.28 risk
  matrix, the INCOSE 34-row traceability matrix (`EXT / X / X ×18 / CTL / …`), NASA FFBD block diagrams,
  a `cpsc_462` protocol-encapsulation diagram, a DME channel-timing table. **Exactly as described —
  there is just half again as much of it as was stated, and it is not the whole story.**
- **Dropping 3 of 20 was a gain.** The `cec_320` C-listing gutters (`232 / // / 233 / v`, the twin of the
  ground-truth sample's one hard false positive at idx 90) and the NASA handbook's Wingdings `z / z`
  bullets are correctly gone.


### 4.3 What that means for the decision, and what it does not

**It does not reverse the change.** Strict precision still rises and recall still nearly doubles; the
390 pages gained are overwhelmingly real (that is what § 2 measures). What it changes is the *sign of the
open question*: [recall-was-a-symbol-test-not-a-run-length.md](./recall-was-a-symbol-test-not-a-run-length.md)
§ 7 item 2 files the loss as "**the `partial` class has no home** … if that matters it is a *separate named
detector*". About a third of it is not the `partial` class at all — it is `shredded-lines`' own job,
lost to a qualifier that asks for a mathematical *character* on a page where the mathematics arrived as
`Z`, `r`, `X` and bare digits. `∫` → `Z`, `√` → `r`, `Σ` → `X`, `∏` → `Q` are precisely the extraction
faults the detector exists to catch, and they are precisely the ones that leave no mathematical
character behind. **`_is_strong` is blind in exactly the direction of its own target.**

The long-run escape that § 3.1 measured and rejected would not have recovered these either: five of the
seven have runs of 3–7 lines. What would recover them is a rule about the *shape* of the run
(a lone `Z`/`X`/`r`/`Q` line adjacent to a limit-looking line) rather than about its characters —
which is a new measurement, not a knob.

---

## 5 · An honest control corpus for `_SHRED_MAX_CHARS`

[../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) § 3.2 swept that constant
against "all of `cesc_470`, `cec_320`, `stat_412`: 156 documents, 1,475 pages, none of which should
fire". [recall-was-a-symbol-test-not-a-run-length.md](./recall-was-a-symbol-test-not-a-run-length.md)
§ 4.1 showed 44 of the 49 pages it flags there are real. So the sweep has no control. This section
builds one, by reading.

**Selection was deliberately not done with the detector.** Candidates were screened on properties the
detector does not use — median chars/page ≥ 300, and a count of runs of ≥ 2 lines of ≤ 10 characters
(a deliberately over-permissive superset of any setting a sweep would test) — and then **every page of
every candidate was rendered and read**. A control verified by sampling is not a control: one unread
page with a flattened equation poisons it.

### 5.1 Tier 1 — 13 documents / 47 pages, no mathematical character anywhere

| pages | document | what it is |
| ---: | --- | --- |
| 4 | `cpsc_462/class_materials/CS 462 Syllabus_Fall26.pdf` | syllabus; grading table; 39-row schedule table |
| 2 | `cec_320/homework/hw8-fmfo--nzcv-ccs-branch-prob-26-03.pdf` | ARM assembly homework, `lstlisting` gutters |
| 3 | `cec_320/homework/hw9-gcge--ldr-str-prob-25-03.pdf` | ditto + memory-map tables |
| 3 | `cec_320/homework/hw10-gggm--c-ptr-n-ldr-str-n-fn-call-prob-26-04.pdf` | ditto |
| 2 | `cec_320/quizes/quiz4/qz-25b-qz5-ccs-n-cond-branch-ldr-str-wkst.pdf` | assembly worksheet |
| 2 | `cec_320/quizes/quiz4/qz-25b-qz6a-ptr-flow-ctrl-in-asm-wkst.pdf` | assembly worksheet |
| 2 | `cesc_420/canvas_materials/poster rubric.pdf` | a 4-column rubric table |
| 7 | `cesc_410/labs_and_projects/lab00/dsp-ba--lab0-getting-started-26.pdf` | 100+ lines of numbered Python listings, ToC dot leaders |
| 2 | `cesc_470/hw/hw01/p01_five_components.pdf` | LaTeX prose + a 5-row table |
| 8 | `syse_301/homework/hw2/12 Systems Engineering Roles.pdf` | two-column paper; **Table 2 is a 22 × 11 ✓/▲ matrix** |
| 3 | `cec_315/CEC315_2026_Syllabus.pdf` | syllabus; grading tables |
| 6 | `cesc_410/senior_design/cesc410-course-info-fall2026.pdf` | course info; 40-row schedule table; a code listing |
| 3 | `sys_304/class_materials/07 Simulation Approaches 2.pdf` | 15-row numeric simulation tables; costing arithmetic, all inline |

Six further byte-identical copies of the `cec_320` files exist elsewhere in `content/`, giving
**19 documents / 62 corpus pages** at no extra reading cost.

**Tier 1 fires 0 pages at `_SHRED_MAX_CHARS` ∈ {4, 5, 6, 7, 8, 10, 12}** — and that result is itself the
finding. These documents contain no character in `_SYMBOLIC_RANGES` at all, so **`_is_strong` can never
pass, and no `max_chars` can ever make them fire.** A control corpus built the obvious way — "documents
with no mathematics" — is *vacuous* against the shipped detector. It bounds nothing. Tier 1's real value
is as a floor for a future sweep of `_is_strong` itself, or of the ratio gate, and as proof that code
gutters and rubric tables are no longer a risk.

### 5.2 Tier 2 — 2 documents / 20 pages that carry mathematical characters but no 2-D mathematics

This is the tier that discriminates, and it is much harder to find. It needs pages with `∆`, `ω`, `π`,
`σ` and PUA glyphs on them and **no displayed 2-D layout at all**:

| pages | document | what it is |
| ---: | --- | --- |
| 10 | `ps160/midterm_02/Midterm_2_sp_24.pdf` | PS 160 Test #2 — one question per page, boxed statement, `▢` answer field, every formula inline |
| 10 | `ps160/midterm_01/MT1_make_up.pdf` | PS 160 Test #1 make-up, same format, plus two pages of "write the formula for…" prompts with blank space |

All 20 pages read. **No formula sheet, no displayed fraction, no matrix, no `cases` brace.**

| `_SHRED_MAX_CHARS` | tier 1 (47p) | tier 2 (20p) | pooled (67p) | 95% CI on the pooled FP rate |
| ---: | ---: | ---: | ---: | --- |
| **4 (shipped)** | 0 | **3** | 3/67 = 4.5% | [1.5%, 12.4%] |
| 5 | 0 | 4 | 4/67 = 6.0% | [2.3%, 14.4%] |
| 6 | 0 | 4 | 4/67 = 6.0% | [2.3%, 14.4%] |
| 8 | 0 | 4 | 4/67 = 6.0% | [2.3%, 14.4%] |
| 10 | 0 | 4 | 4/67 = 6.0% | [2.3%, 14.4%] |
| 12 | 0 | 4 | 4/67 = 6.0% | [2.3%, 14.4%] |

The four false positives, all the same shape — **an exam answer blank**:
`∆L / mm` (p1), `∆S / J/K` (p9), `∆f = / Hz` (p9), and at `max_chars ≥ 5` one more, `ω = / rad/s` (p6).

**The signal in that table is the plateau.** Raising `_SHRED_MAX_CHARS` from 4 costs this control
exactly **one** extra page and then nothing more up to 12. On a 67-page control that is weak evidence,
but it is real evidence, which the 1,475-page "control" never was.

### 5.3 The trap, demonstrated

`ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` passed the same screen — 13 pages, an exam
paper by the same instructor, and two of its six flagged pages (pp. 9, 11) are the same harmless
`∆S = / kJ/K` answer blank. **It is not a control document.** Its pages 2 and 3 are two full
**formula sheets** — forty stacked fractions, `√(k/m)`, `∫p dV`, `∮dQ/T` — and they flatten completely.
Nothing short of opening them says so. `ps160/midterm_03/test_finalexam_ps160_2024_spring.pdf` is the
same document family and is excluded for the same reason.

**The recipe, so the next session can grow this set:** screen on median chars/page and permissive
short-line-run density, exclude nothing on the detector's own output, then **read every page**, and
reject the whole document the moment one page carries a displayed fraction, radical, summation,
integral, matrix or `cases` brace. Roughly one candidate in three fails on a page nobody would have
predicted.


---

## 6 · Three things found on the way

### 6.1 The suspect count is 963, not 959

Running the roll-call exactly as
[recall-was-a-symbol-test-not-a-run-length.md](./recall-was-a-symbol-test-not-a-run-length.md) § 8
prints it: `459 docs / 7198 pages -- 963 suspect; {'unmapped-glyphs': 505, 'shredded-lines': 732,
'letter-spaced': 9, 'vertical-letter-spaced': 4}`. Every per-detector count in that document reproduces
exactly; the total in its § 0 table reads **959 (10.8% → 13.3%)** and should read **963 (13.4%)**.
A transcription slip, recorded so the next reader does not re-derive it.

### 6.2 `_is_strong` accepts the very glyphs `unmapped-glyphs` calls furniture

`_is_strong` treats the **entire Private Use Area** (`0xE000–0xF8FF`) as "an actual mathematical
character". Detector 4, forty lines further down the same file, declares `U+F0B7`, `U+F070` and `U+F06C`
**benign** — "the Office dingbat block, 92% of its corpus volume … a bullet reaching the reader as a box
costs nothing". Both statements are in `src/ocr_handler/structure.py` and they contradict each other.

Measured over the 732 flagged pages:

| pages whose *only* strong evidence is… | count | share |
| --- | ---: | ---: |
| a code point on detector 4's **benign list** | 3 | 0.4% |
| anywhere in the Office dingbat block `U+F020–F0FF` | **29** | **4.0%**, in 13 documents |

Both of this audit's hard misfires are in that 29: `syse_301/Systems-Eng-Guidebook…-slp.pdf` p26
(`18 / U+F0A7`, a page number and a square bullet on a page of pure prose) and
`ae318/…8 Apr 2026 lecture slides.pdf` p4 (`U+F050 / U+F050`).

**It is not a clean fix, and that is the point.** The same block is Symbol font's Greek: `U+F070` is π
*and* a Wingdings square, `U+F06C` is λ *and* a round bullet, `U+F077` is ω, `U+F044` is Δ, `U+F061` is
α. Nine of the 29 pages are `sys_304`'s fuzzy-set slides where the PUA characters are genuine
membership-function Greek. **The text cannot separate them; only the font can**, and `signals()` takes a
string — the exact constraint § 5.1 of the earlier finding already named on the other detector. So this
is a **contract** question, not a threshold one: it belongs with the superscript detector in the
"needs a `page`, not a `str`" bucket. Recorded, not fixed.

### 6.3 The corpus is duplicated, and the flagged set is the most duplicated part of it

Hashing every document's concatenated text layer, and every page's:

| | count | distinct | ratio |
| --- | ---: | ---: | ---: |
| documents | 459 | **355** | 1.29× |
| pages ≥ 200 chars | 5,784 | 4,931 | 1.17× |
| **`shredded-lines` flagged pages** | **732** | **513** | **1.43×** |

Whole `cec_315` lecture PDFs exist three times over (`all_lectures/`, `exam*/lectures/`,
`homework/hw4/`); `cesc_410/hw/hw01/` is mirrored under `overleaf/`; 21 of the 83 "unseen" documents are
content-identical to an already-labelled one, and 4 of the 13 tier-1 control documents have 6
byte-identical twins between them.

**Every corpus-wide count in this repo's findings — 7,198 pages, 732 flagged, 505 unmapped — counts
duplicates as independent pages**, and the flagged set is duplicated *more* than the corpus average
(1.43× against 1.17×), because the duplicated documents are LaTeX lecture notes full of integrals.
**732 flagged pages are 513 distinct pages.** That is fine for "how much work is there", wrong for "how
many distinct problems are there", and it silently narrows the effective sample size of any precision
estimate drawn page-uniformly. Sample B exists because of it; nothing else in the repo accounts for it.

---

## 7 · What is now open

1. **`_is_strong` has a blind spot shaped like its own target** (§ 4.1). `∫`→`Z`, `√`→`r`, `Σ`→`X`,
   `∏`→`Q` leave no mathematical character behind, and ~23 corpus pages of exactly that are now
   invisible. A shape rule — a lone capital `Z`/`X`/`Q`/`r` line adjacent to a limit-looking line —
   is the obvious candidate and has **not** been measured.
2. **`_SHRED_MAX_CHARS` is still open, and now has a control** (§ 5). 67 verified pages, false-positive
   rate 4.5% at 4 and 6.0% flat from 5 to 12. It needs the drawn-and-read *increment* the earlier
   finding asked for as well; the control bounds the wrong-way error, not the right-way gain.
3. **The exam-answer-blank false positive** (`∆S ▢ J/K`) is a named, cheap class: a run of exactly two
   lines whose second is a bare unit. 3 of this audit's 5 misfires, and 4 of the control's 4. It did not
   exist at `_SHRED_MIN_RUN = 4`.
4. **`_is_strong` vs the benign-glyph list** (§ 6.2) — a contract question, 29 pages.
5. **`page.get_text()` splices annotation text into the body** (§ 3.3 item 4) — a fifth faithfulness
   fault, unmeasured beyond the one document.
6. **The `-plw` pair is two different problems**, not one (§ 3). Doc 1 is a `suspect` LaTeX document with
   typed comments; doc 2 is a fully `sparse` document whose ink Ghostscript flattened into page content
   and which no detector sees. `ink.py`'s difference method works on both; its colour method fails on
   doc 1.

---

## 8 · Reproducing this

```bash
cd ~/electrical_notes/ocr_handler

# the roll-call this document is built on -- 459 docs / 7,198 pages, 963 suspect, 22 s
nice -n 19 .venv/bin/python - <<'PY'
import sys, collections; sys.path.insert(0, "src")
from pathlib import Path
from ocr_handler import textlayer
pages = docs = suspect = 0; per = collections.Counter()
for pdf in sorted(Path("../content").rglob("*.pdf")):
    try: d = textlayer.extract(pdf)
    except Exception: continue
    docs += 1; pages += len(d.pages); suspect += len(d.suspect_pages)
    per.update({k: v for k, v in d.signal_counts.items() if v})
print(docs, "docs /", pages, "pages --", suspect, "suspect;", dict(per))
PY
```

Everything else is a pure function of `content/` plus one cached pass: each page's `page.get_text()` is
written once to a JSONL cache (43 s), and the enumerations replay over the cache.

- **The 66 orphans** = pages where a parameterised `shredded_run(max_chars=4, min_run=4, strong=False)`
  fires and the shipped `shredded_run` does not, minus pages any other detector still flags.
- **The draws** are `random.Random(seed).sample(enumeration_sorted_by_(pdf, page), n)` with the seeds
  named in § 1 and § 4.1.
- **The 115 hand labels cannot be regenerated.** They are one reader's judgements on 100–110 dpi renders
  read against each page's own extracted text. Samples A and B are tabulated in § 2.1 and the orphan
  sample in the appendix; the control set is listed in full in § 5.

**One reader, no answer key**, the same caveat the two prior samples state. Where a call was arguable it
is flagged in the tables. The sensitivity that matters: moving the three most arguable strict hits in
sample A (idx 15, 22 — pole-zero and figure-axis runs on pages whose only flattening is a subscript
pushed onto its own line) from `genuine-wrong-evidence` to `partial` takes A's strict precision from
90.0% to **84.0%** [71.5, 91.7], which is below the shipped 93.1% but still inside its interval. The
direction of § 4 is not sensitive to any single call: five of the seven mathematical losses there are
unambiguous.

---

## 9 · Decision status

| # | Question | Answer | Status |
| --- | --- | --- | --- |
| 1 | Does 93.1% strict precision hold on documents nobody labelled? | **Yes.** 90.0% [79, 96] on 50 pages / 35 docs; 88.9% [77, 95] on 45 pages / 31 docs of never-labelled content. 93.1% is inside both. Clustered on documents the floor is ~80%. | **Replicated.** |
| 2 | Does broad precision 95.2% hold? | **Yes.** 96.0% and 93.3%. | **Verified.** |
| 3 | Is the priced cost "~46 non-mathematical pages"? | **No, twice over.** It is **66** pages, and ~35% of them [18, 57] are flattened mathematics — Σ and ∫ with limits, `√(3kT/m)`, `1/s + 1/s′ = 1/f`, a 3×3 matrix product. "No strict true positive was lost" is true of the sample, false of the corpus. | **Refuted; ~23 pages of real loss now named.** |
| 4 | The `-plw` census? | **22 pages / 2 documents confirmed; 7 flagged, not 5.** All 7 calls genuine. **Neither document has an `/Ink` annotation** — the only one in the corpus is an unlooked-at student homework. The two files are two different problems. | **Closed by enumeration.** |
| 5 | Is there an honest control for `_SHRED_MAX_CHARS`? | **Yes, 15 documents / 67 pages, every page read.** FP rate 4.5% at 4, 6.0% flat to 12. Also: a control with no mathematical characters is **vacuous** against `_is_strong` — it cannot fire at any setting. | **Built. Small but real.** |
| 6 | Anything the shipped code contradicts itself about? | `_is_strong` treats the whole Private Use Area as a genuine mathematical character, including the three glyphs `unmapped-glyphs` explicitly calls benign. **3** flagged pages rest on those three; **29 (4.0%)** rest somewhere in the Office dingbat block that contains them, and 2 of this audit's 5 misfires are among the 29. Not cleanly fixable from a string — the font separates π from a bullet and the text does not. | **Open, § 6.2.** |

---

**See also:** [recall-was-a-symbol-test-not-a-run-length.md](./recall-was-a-symbol-test-not-a-run-length.md) ·
[ground-truth-sample.md](./ground-truth-sample.md) ·
[../plans/structural-faithfulness.md](../plans/structural-faithfulness.md) ·
[corpus-census-2026-09-04.md](./corpus-census-2026-09-04.md) ·
`src/ocr_handler/structure.py`, `src/ocr_handler/ink.py`

---

## Appendix · The remaining hand labels


### A.1 · Sample B — the 45 content-fresh pages (`B13/B21/B23/B25/B40/B41` reuse a sample-A label)

| # | document | p | run | label |
| ---: | --- | ---: | --- | --- |
| B00 | `ae318/AE318_export/AE318 13 Mar 2026 lecture slides.pdf` | 10 | `𝑑𝜎𝑥 / 𝑑𝑥𝑑𝑥` | genuine |
| B01 | `ae318/AE318_export/AE318 8 Apr 2026 lecture slides.pdf` | 4 | `U+F050 / U+F050` | misfire |
| B02 | `cec_315/all_lectures/cec315-lctr20-inverse-z-transform-properties.pdf` | 8 | `n / X / k=−∞ / x[k] / 1` | genuine |
| B03 | `cec_315/exam1/CEC_315_exam_1.pdf` | 2 | `∞ / X / k=−∞` | genuine |
| B04 | `cec_315/exam1/lectures/cec315-lctr03-complex-nums-exp-n-sinusoidal-sigs.pdf` | 3 | `√ / −1.` | genuine |
| B05 | `cec_315/exam2/cec315-EXAM2-1.pdf` | 6 | `ω2 / n` | genuine |
| B06 | `cec_315/exam3/lectures/cec315-lctr20-inverse-z-transform-properties.pdf` | 8 | `n / X / k=−∞ / x[k] / 1` | genuine |
| B07 | `cec_315/exam3/lectures/cec315-lctr21-system-analysis-unilateral-z.pdf` | 4 | `Re / Im / × / × ×` | genuine-wrong-evidence |
| B08 | `cec_315/exam3/lectures/cec315-lctr21-system-analysis-unilateral-z.pdf` | 6 | `∞ / X / n=0` | genuine |
| B09 | `cec_315/hw_practice_problems/lctr06-convolution-problems.pdf` | 2 | `U+F8F1 / U+F8F4 / U+F8F4 / U+F8F4 / U+F8F2 / U+F8F4 / U+F8F4` | genuine |
| B10 | `cec_315/hw_practice_problems/lctr22-exercise-solutions.pdf` | 2 | `T = / 2π` | genuine |
| B11 | `cec_320/homework/hw11-hche--if-based-flow-control-soln-26-04.pdf` | 3 | `10, / 𝑥≥5, / 2𝑥,` | genuine |
| B12 | `cec_320/lectures/mp-cg--lctr4-data-representation-slides-26-01 (1).pdf` | 4 | `¯𝛼5 / -1` | genuine |
| B13 | `cec_320/lectures/mp-de-lctr7-bitwise-ops-n-gpio-reg-access-slides-2026-01 (1).pdf` | 5 | `9 / ˆ` | partial |
| B14 | `cesc_410/hw/hw01/dsphw26-hw1.pdf` | 1 | `√ / 8).` | genuine |
| B15 | `cesc_410/hw/hw01/p06_convolution.pdf` | 1 | `∞ / X / k=−∞` | genuine |
| B16 | `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 9 | `( / 0, / 𝑡≠0, / ∞,` | genuine |
| B17 | `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 10 | `𝑇 / ∞ / ∑︁ / 𝑘=−∞` | genuine |
| B18 | `cesc_410/lectures/dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 11 | `𝑁−1 / ∑︁ / 𝑛=0` | genuine |
| B19 | `ee_300/exam_final/final_cheatsheet.pdf` | 2 | `𝑄𝑘= / 1 / 2𝜁𝑘` | genuine |
| B20 | `ee_300/exam_final/final_cheatsheet.pdf` | 3 | `𝑅= / 1 / 𝜔0𝐶` | genuine |
| B21 | `ee_300/exam_final/final_cheatsheet.pdf` | 5 | `𝑘𝑓 / ,` | genuine |
| B22 | `ee_300/exam_final/final_quiz_examples.pdf` | 1 | `1 / 𝑠𝐶 / 𝑅𝑓+ / 1 / 𝑠𝐶 / = / 𝑅𝑓` | genuine |
| B23 | `ee_300/exam_final/final_quiz_examples.pdf` | 4 | `2000 / √` | genuine |
| B24 | `ee_300/exam_final/final_quiz_examples.pdf` | 10 | `𝑅= / 1` | genuine |
| B25 | `ps160/m15/chapter_15.pdf` | 5 | `x / v −t / ` | genuine |
| B26 | `ps160/m15/chapter_15.pdf` | 9 | `Area / = / P / 4πR2` | genuine |
| B27 | `ps160/m15/chapter_15.pdf` | 14 | `t / U+0003` | genuine |
| B28 | `ps160/m17/CH17_ADA_PPT_LectureOutline.pdf` | 15 | `U+F061 / − / U+F0B0 / 5` | genuine |
| B29 | `ps160/m17/chapter_17.pdf` | 8 | `∆L / Lo / ` | genuine |
| B30 | `ps160/m18/M18_Review-1.pdf` | 9 | `CV = / Q / n∆T` | genuine |
| B31 | `ps160/m19/chapter_19.pdf` | 3 | `V2 / V1 / ` | genuine |
| B32 | `ps160/m33,34,35,36/CH34_ADA_PPT_LectureOutline-1.pdf` | 6 | `s / s / = −` | genuine |
| B33 | `ps160/m33,34,35,36/CH34_ADA_PPT_LectureOutline-1.pdf` | 10 | `1 / 1 / 2 / s / s / R / + / = / ` | genuine |
| B34 | `ps160/m33,34,35,36/CH34_ADA_PPT_LectureOutline-1.pdf` | 24 | `0 / a / b / n / n / s / s / + / = / ` | genuine |
| B35 | `ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` | 3 | `1 / 2m /  v2` | genuine |
| B36 | `ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` | 9 | `∆L = / mm` | misfire |
| B37 | `ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` | 11 | `∆S = / kJ/K` | misfire |
| B38 | `stat_412/HW07/solutions/q12.pdf` | 1 | `√ / 110 / .` | genuine |
| B39 | `stat_412/HW07/solutions/q13.pdf` | 1 | `ˆp = / 99` | genuine |
| B40 | `stat_412/HW08/solutions/q09.pdf` | 1 | `SE = / √ / 1572` | genuine |
| B41 | `stat_412/QZ08/solutions/q06.pdf` | 1 | `4.4 / 11.6 / Then / χ2 =` | genuine |
| B42 | `stat_412/QZ08/solutions/q08.pdf` | 1 | `sp = / √` | genuine |
| B43 | `sys_304/class_materials/07 Simulation Approaches 1.pdf` | 6 | `U+F06D / U+F073` | partial |
| B44 | `sys_304/class_materials/07 Simulation Approaches 1.pdf` | 11 | `)) / ( / 1( / 2 / )) / ( / ( / ) / ( / ) / ( / 2 / i / i / i` | genuine |


### A.2 · The 20-page orphan sample of § 4.1

`maths` = a strict true positive the change made invisible · `not-maths` = the `partial` class
that was priced · `misfire` = a false positive correctly removed.

| # | document | p | run | verdict |
| ---: | --- | ---: | --- | --- |
| O00 | `ae318/AE318_export/AE318 25 Mar 2026 lecture slides.pdf` | 10 | `= 0 / q / q / q` | maths |
| O01 | `cec_300/course_content/module 2a - Navigation Systems.pdf` | 30 | `X / 12us / 12us / Y / 30us / 36us / W / 24us / 24us / Z / 15` | not-maths |
| O02 | `cec_315/all_lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf` | 2 | `N / X / k=0 / ak / dky` | maths |
| O03 | `cec_320/summaries/cec32x-companion (2).pdf` | 19 | `L / 4 / 76 / V / G / T` | not-maths |
| O04 | `cec_320/summaries/cec32x-companion (2).pdf` | 206 | `232 / // / 233 / v` | misfire |
| O05 | `cesc_470/hw/hw01/p09_cpi_and_execution_time.pdf` | 1 | `A / 40% / 1 / B / 40% / 2 / C / 20% / 3` | not-maths |
| O06 | `cpsc_462/class_materials/Application Layer.pdf` | 36 | `time / time / X / X / X’ / X’’ / X’’ / t’` | not-maths |
| O07 | `cpsc_462/class_materials/Introduction CPSC 462.pdf` | 77 | `Ht / Hn / Hl / M / Ht / Hn / M / Ht / M / M / Ht / Hn / Hl /` | not-maths |
| O08 | `ps160/m18/chapter_18.pdf` | 8 | `r / 3kT / m / = / r / 3RT / M` | maths |
| O09 | `ps160/m19/chapter_19.pdf` | 2 | `W = / Z V2 / V1 / p dV` | maths |
| O10 | `ps160/m20/CH20_ADA_PPT_LectureOutline.pdf` | 16 | `C / \| / \| / \| / \| / Q / W` | maths |
| O11 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 51 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry ` | not-maths |
| O12 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 21 | `A / B / C / D` | not-maths |
| O13 | `sys_304/class_materials/03 Analytic Hierarchy Process_Handout.pdf` | 9 | `CR / CI / RI / = / = / =` | maths |
| O14 | `sys_304/class_materials/03 The Analytic Hierarchy Process.pdf` | 24 | `3 / 1 / 2 / x / 0.55 / =` | maths |
| O15 | `syse_301/INCOSE SYS ENG HANDBOOK 5th EDITION.pdf` | 110 | `IV / V / c / 1 / 5 / 2` | not-maths |
| O16 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 35 | `B / C / A / Cost` | not-maths |
| O17 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 103 | `z / z / Drop / z / z` | misfire |
| O18 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 211 | `z / z / Iz / z` | misfire |
| O19 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 305 | `OR / G / G / _ / OR` | not-maths |


### A.3 · All 66 orphaned pages, enumerated

Pages that fired `shredded-lines` at `max_chars 4 / min_run 4` with no `_is_strong`, fire nothing
at the shipped setting, and are not picked up by any other detector. Twenty were drawn and read
(A.2); the rest are listed so the next session can extend the read without re-deriving the set.

| # | document | p | run |
| ---: | --- | ---: | --- |
| 0 | `ae318/AE318_export/AE 318 take-home assignment.pdf` | 3 | `C.S. / a / b / c / c` |
| 1 | `ae318/AE318_export/AE318 25 Mar 2026 lecture slides.pdf` | 10 | `= 0 / q / q / q` |
| 2 | `cec_300/course_content/Module 6a - State Parameters and Sensor Fusion.pdf` | 27 | `o / E.g. / • / F = / •` |
| 3 | `cec_300/course_content/module 2a - Navigation Systems.pdf` | 30 | `X / 12us / 12us / Y / 30us / 36us / W / 24us / 24us / Z / 15us / 21us` |
| 4 | `cec_300/exam1/module 2a - Navigation Systems.pdf` | 30 | `X / 12us / 12us / Y / 30us / 36us / W / 24us / 24us / Z / 15us / 21us` |
| 5 | `cec_315/all_lectures/cec315-lctr14-magnitude-phase-filters.pdf` | 10 | `t / / / ( / )` |
| 6 | `cec_315/all_lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf` | 2 | `N / X / k=0 / ak / dky` |
| 7 | `cec_315/exam2/lectures/cec315-lctr14-magnitude-phase-filters.pdf` | 10 | `t / / / ( / )` |
| 8 | `cec_315/exam3/lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf` | 2 | `N / X / k=0 / ak / dky` |
| 9 | `cec_315/homework/hw4/cec315-lctr14-magnitude-phase-filters (2).pdf` | 10 | `t / / / ( / )` |
| 10 | `cec_320/summaries/cec32x-companion (2).pdf` | 19 | `L / 4 / 76 / V / G / T` |
| 11 | `cec_320/summaries/cec32x-companion (2).pdf` | 199 | `195 / // / 196 / v` |
| 12 | `cec_320/summaries/cec32x-companion (2).pdf` | 206 | `232 / // / 233 / v` |
| 13 | `cec_320/summaries/cec32x-companion (2).pdf` | 211 | `252 / // / 253 / v` |
| 14 | `cesc_470/hw/hw01/p09_cpi_and_execution_time.pdf` | 1 | `A / 40% / 1 / B / 40% / 2 / C / 20% / 3` |
| 15 | `cpsc_462/class_materials/Application Layer.pdf` | 36 | `time / time / X / X / X’ / X’’ / X’’ / t’` |
| 16 | `cpsc_462/class_materials/Introduction CPSC 462.pdf` | 75 | `M / Ht / Hn / Hl` |
| 17 | `cpsc_462/class_materials/Introduction CPSC 462.pdf` | 76 | `Ht / M / M / M / Ht / Hn / M / Ht / Hn / Hl / M / Ht / Hn / Ht / M / M` |
| 18 | `cpsc_462/class_materials/Introduction CPSC 462.pdf` | 77 | `Ht / Hn / Hl / M / Ht / Hn / M / Ht / M / M / Ht / Hn / Hl / M / Ht / ` |
| 19 | `ps160/m14/YF15e_CH14_ADA_PPT_LectureOutline.pdf` | 26 | `2 / 2 / 2 / x / E / mv / kx / kA / = / + / = / =` |
| 20 | `ps160/m18/chapter_18.pdf` | 8 | `r / 3kT / m / = / r / 3RT / M` |
| 21 | `ps160/m19/chapter_19.pdf` | 2 | `W = / Z V2 / V1 / p dV` |
| 22 | `ps160/m19/chapter_19.pdf` | 12 | `CV / dV / V / = 0 / R / CV` |
| 23 | `ps160/m20/CH20_ADA_PPT_LectureOutline.pdf` | 11 | `C / \| / \| / Q` |
| 24 | `ps160/m20/CH20_ADA_PPT_LectureOutline.pdf` | 16 | `C / \| / \| / \| / \| / Q / W` |
| 25 | `ps160/m20/CH20_ADA_PPT_LectureOutline.pdf` | 25 | `C / \| / \|. / Q / 4.` |
| 26 | `ps160/m20/CH20_ADA_PPT_LectureOutline.pdf` | 31 | `dQ / dS / T / =` |
| 27 | `ps160/m33,34,35,36/M33-36_Review.pdf` | 16 | `s′ / 1 / f = / 1` |
| 28 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 26 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry / Dry / 26` |
| 29 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 27 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry / Dry / $0` |
| 30 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 31 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry / Dry / $0` |
| 31 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 33 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry / Dry / $0` |
| 32 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 35 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry / Dry / $0` |
| 33 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 37 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry / Dry / $0` |
| 34 | `sys_304/class_materials/02 Decision Making Under Risk and Uncertainty 2 (1).pdf` | 51 | `a / b / c / d / e / f / g / h / Oil / Oil / Oil / Dry / Dry / Dry / $0` |
| 35 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 15 | `1 / - / P / P / = / 2+ / 2 / P / - / P / P / P / 4 / 3 / - / P / = / 1` |
| 36 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 17 | `A / B / C / D` |
| 37 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 18 | `A / B / C / D` |
| 38 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 19 | `A / B / C / D` |
| 39 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 21 | `A / B / C / D` |
| 40 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 22 | `A / B / C / D` |
| 41 | `sys_304/class_materials/02 Decision Making with Multiple Objectives 1.pdf` | 29 | `X / Y / Z / X / X / X / Y / Y / Y / Z / Z / Z / X / Y / Z / A / B / C` |
| 42 | `sys_304/class_materials/03 Analytic Hierarchy Process_Handout.pdf` | 9 | `CR / CI / RI / = / = / =` |
| 43 | `sys_304/class_materials/03 Analytic Hierarchy Process_Handout.pdf` | 13 | `CR / CI / RI / = / = / =` |
| 44 | `sys_304/class_materials/03 Analytic Hierarchy Process_Handout.pdf` | 15 | `A / B / C / Cost / 4 / 8 / 7` |
| 45 | `sys_304/class_materials/03 The Analytic Hierarchy Process.pdf` | 14 | `A / B / C / D / E` |
| 46 | `sys_304/class_materials/03 The Analytic Hierarchy Process.pdf` | 24 | `3 / 1 / 2 / x / 0.55 / =` |
| 47 | `sys_304/class_materials/03 The Analytic Hierarchy Process.pdf` | 26 | `A / B / C / D / E` |
| 48 | `sys_304/class_materials/03 The Analytic Hierarchy Process.pdf` | 32 | `A / B / C / D / E` |
| 49 | `sys_304/class_materials/04 Fuzzy Theory in Decision Analysis.pdf` | 18 | `T / Nate / Tall / T` |
| 50 | `sys_304/class_materials/05 Game Theory.pdf` | 37 | `Y1 / P / Y2 / 1-P` |
| 51 | `syse_301/INCOSE SYS ENG HANDBOOK 5th EDITION.pdf` | 110 | `IV / V / c / 1 / 5 / 2` |
| 52 | `syse_301/INCOSE SYS ENG HANDBOOK 5th EDITION.pdf` | 230 | `A / B / to / B / A / to / D / A` |
| 53 | `syse_301/INCOSE SYS ENG HANDBOOK 5th EDITION.pdf` | 241 | `Co / rr / ec / t / a / m / ou / nt / o / f / ta / il / o / ri / n / g ` |
| 54 | `syse_301/INCOSE SYS ENG HANDBOOK 5th EDITION.pdf` | 344 | `EXT / X / X / X / X / X / X / X / X / X / X / X / X / X / X / X / X / ` |
| 55 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 29 | `B / A / A / n / C / B / A / n / C / B / Ab / Aa / Bb / Ba / Ab / Aa / ` |
| 56 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 35 | `B / C / A / Cost` |
| 57 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 44 | `CDR / z / z / PRR / z / z / SIR / z / z` |
| 58 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 45 | `z / z / ORR / z / z / FRR / z / z` |
| 59 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 46 | `PLAR / z / z / CERR / z / z` |
| 60 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 72 | `A / B / C / D / E / F / G / H / SS / M / M / M / M / E / E / E / E` |
| 61 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 103 | `z / z / Drop / z / z` |
| 62 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 141 | `A / B / C / D` |
| 63 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 211 | `z / z / Iz / z` |
| 64 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 305 | `OR / G / G / _ / OR` |
| 65 | `syse_301/NASA-Systems-Engineering-Handbook-2007.pdf` | 316 | `X / X / X / X / X` |
