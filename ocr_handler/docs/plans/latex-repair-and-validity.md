# LaTeX repair, and the validity axis that replaces compile-checking

> **Type: ACTIVE-SPEC.** Living document, named by concept (no date in the filename) per
> [../directives/roadmap-and-plans.md](../directives/roadmap-and-plans.md). Written 2026-09-06.
> Ships `src/ocr_handler/latex_repair.py`, `src/ocr_handler/validity.py` and the
> `ocr-handler check` verb in `src/ocr_handler/cli.py` (§ 7, added 2026-09-06).
> Every constant below names the measurement that produced it, per
> [../directives/code-discipline.md](../directives/code-discipline.md).
>
> Sources: [../research/mineru-teardown.md](../research/mineru-teardown.md) § 6, § 7.1 ·
> [../research/equation-ocr-specialists.md](../research/equation-ocr-specialists.md) § 5 ·
> [./structural-faithfulness.md](./structural-faithfulness.md) (the `Signal` roll-call contract) ·
> [../decisions/0002-numpy-scipy-pillow-not-opencv.md](../decisions/0002-numpy-scipy-pillow-not-opencv.md).
> Neither source document is edited by this work; where this contradicts them, § 5 says so.
>
> ⚠ **No GPU, no model, no `tectonic`.** Both modules are `import re` plus the standard library.
> The whole-corpus pass in § 3.7 is 0.11 s for 2,967 expressions; § 3.8's re-sweep is 0.11 s
> for 2,508.

---

## 1 · Two claims this closes

1. **MinerU's LaTeX repair suite cannot be vendored as-is.** It was nominated for adoption as
   "licence-clean, dependency-free" and "reproducing this list by observation would cost days".
   The list is real; the implementation destroys mathematics. **Applied to this repo's own 44
   recorded UniMERNet outputs, it changed 4 — and all four changes were damage.**
2. **Compile-checking is not a weak validity signal, it is no signal.** 83 of 84 recorded outputs
   compiled under tectonic, including 1,113 tokens of array garbage read off a whole page,
   matching the CDM authors' published 99.71% render rate. Planning around it stops here.

---

## 2 · The audit — every rule in `mineru/model/mfr/utils.py`

Verified by executing the upstream file directly (`~/tmp/ocr_repos/MinerU`, `import re` only) over
hand-built probes and over this repo's `tmp/eqocr/sweep.json`. Every ⚠ row below is reproduced.

### 2.1 Meaning-changing defects, worst first

| # | Upstream | What it does | Why it is a meaning change |
| --- | --- | --- | --- |
| 1 ⚠ | `RIGHT_PATTERN = (\\right)(\S*)`, `:5` | **Deletes `\rightarrow`, `\leftarrow`, `\leftrightarrow`, `\rightharpoonup`, `\lefteqn`.** `a \rightarrow b` → `a  b` | `\S*` after `\right` grabs `arrow`, which is not a delimiter, so the token is rewritten to `\right.`; the counts then disagree and the strip-all branch removes it. `x[n] \rightarrow X(z)` loses the transform-pair arrow. Asymmetric and therefore invisible: `\Rightarrow` survives, `\rightarrow` does not |
| 2 ⚠ | same | **Annihilates any compact `\left…\right` group.** `\left(x+1\right)` → `''` | `\S*` is greedy to the first space, so it swallows the whole expression; the replacement is `\left.` and the rest is gone. Only survives because UniMERNet happens to emit spaces between tokens |
| 3 ⚠ | `valid_delims_list`, `:22` | **Deletes `\langle`, `\rangle`, `\vert`, `\Vert`, `\lbrace`, `\rbrace`, `<`, `>`.** `\left\langle x \right\rangle` → `\left. x \right.` | 21-entry whitelist; anything off it is *replaced* by `.`. Inner products and expectations lose their brackets |
| 4 ⚠ | same | `\left. y \right\|_{x=0}` → `\left. y \right.` | The evaluation bar **and its subscript** are deleted. "Evaluated at x=0" becomes nothing |
| 5 ⚠ | `re.compile(r'\\Bar'): r'\\hat'`, **line 282** | `\Bar{x}` → `\hat{x}` | x̄ is a **mean**; x̂ is an **estimate**. Confirmed: `\Bar{x} = \frac{1}{n}\sum x_i` → `\hat{x} = \frac{1}{n}\sum x_i`. Exactly the statistics and DSP material this project serves |
| 6 ⚠ | `process_latex`, `:210` | `\,` → `\ ,`; `\;` → `\ ;`; `\!` → `\ !`; `\:` → `\ :` | TeX's one-character **spacing** commands are not in its keep-set, so a thin space becomes a space **plus a literal punctuation glyph inside the mathematics**. `\int f(x)\,dx` → `\int f(x)\ ,dx`. Measured firing on 2 of 44 recorded outputs |
| 7 ⚠ | no word boundary on any of the 15 substitutions | `\slashed{D}` → `/ed{D}`; `\Barbell` → `\hatbell` | `\slashed` is the Feynman slash, an operator |
| 8 ⚠ | `remove_unsupported_commands`, `:309` | `\textsubscript` deleted: `H\textsubscript{2}O` → `H{2}O` | A different molecule. Also deletes `\textcent`, a currency symbol |
| 9 ⚠ | `remove_up_commands`, `:300` | `\upharpoonright` → `\harpoonright`; `\upuparrows` → `\uparrows` | The keep-list `{"arrow","downarrow","lus","silon"}` is a suffix guess. Both results are **undefined commands** |
| 10 ⚠ | `re.compile(r'\\vline = '): r'\\models '` | `\vline` in an array cell becomes ⊨ | `\vline` draws a table rule. Semantic entailment is a different object |
| 11 | `fix_latex_left_right`, `:45-49` | counts differ → **strip every** `\left`/`\right` | Restyles every delimiter in the expression to fix one. Fires on a real output: `expo/pad+300`'s `\left(` → `(` |

### 2.2 Latent defects — wrong, but not yet observed corrupting output

| # | Upstream | Defect |
| --- | --- | --- |
| 12 | `ENV_*_PATTERNS`, `:271-273` | Built as `r'\\begin\{' + env + r'\}'`, so for **`align*` the `*` is a regex quantifier**: the pattern is `\begin{alig n*}` and can never match `\begin{align*}`. The environment upstream most wants to pad is the one it silently cannot |
| 13 | `fix_left_right_pairs`, `:52-133` | `adjustments.append((i, i + 7, target_pos))` assumes `\right` + a **one-character** delimiter. With `\right\}` or `\right\rangle` it slices mid-token and moves the fragment. **Not ported** |

### 2.3 Rules audited and kept

`\Hat`→`\hat`, `\Tilde`→`\tilde`, `\Dot`→`\dot`, `\underbar`→`\underline`, `\slash`→`/`,
`\textunderscore`→`\_`, `\vDash`→`\models`, `\sq \sqcup`→`\square`, `\up `→`\ ` — all
formatting-equivalent, all given the `(?![a-zA-Z])` boundary they lacked.
`\textperthousand`→‰, `\copyright`→©, `\sun`→☉, `\fint`→⨏ — kept; **noted** as raw-Unicode
injection, which is fine for a Markdown target and would need a math font under pdflatex.
`fix_unbalanced_braces` is upstream's algorithm, kept whole; the escape test is rewritten as a
two-character skip, which is equivalent and legible.

`\upalpha`→`\alpha` is kept as the one deliberate **formatting** change: upright→italic Greek,
taken because `upgreek` is rarely loaded downstream and the alternative is a build failure.

### 2.4 What shipped instead

| Upstream behaviour | Here |
| --- | --- |
| `\left`/`\right` delimiter fix by `\S*` | match `\\(?:left\|right)(?![a-zA-Z])`, then test the *next* token against a delimiter alternation; **insert** a `.` only when nothing follows |
| counts differ → strip all | **pad the short side** with `\left.`/`\right.`. `drop_unmatched_delimiters=True` reproduces upstream's branch, off by default |
| `\Bar` → `\hat` | `\Bar` → `\bar` |
| `\textsubscript` deleted | `\textsubscript` → `_` |
| `\up<suffix guess>` | explicit upright-Greek name list |
| space after any lone backslash | space **only before a digit** |
| `\begin{align*}` regex | `re.escape(env)` |
| `fix_left_right_pairs` | not ported (§ 2.2 #13) |
| silent | every change returns a note in `Repair.notes` |

**Measured on the 44 recorded raw outputs:** upstream changes 4 (`eqline/pad+96` — an arrow
deleted; `eqline/pad+300` — `\;`→`\ ;` twice; `expo/pad+300` — `\left(`→`(`;
`patho/merged_two_equations` — `\!`→`\ !` four times, `\,`→`\ ,`). **This module changes 1**
(`\slash`→`/`, formatting). It is idempotent on 2,000 corpus expressions and never returns an
empty string for a non-empty input.

---

## 3 · The validity axis

### 3.1 Contract

`Signal(name, fired, detail)`, imported from `structure.py` rather than redefined, so one renderer
serves both axes. **One `Signal` per detector on every reading, fired or not.** Verdict is
`plausible` / `suspect`, and `suspect` **iff any detector fired** — an OR, never an average, for
the reason [structural-faithfulness.md](./structural-faithfulness.md) § 2 gives: these detectors
catch unrelated failures, so a blended score would hide the only actionable fact, which is *which*
one fired. A detector that could not run (no crop size) says so in `detail` with `fired=False`.

**Signals run BEFORE repair.** A string that needs heavy repair is evidence about the reading.

### 3.2 Tokenisation — the definition the numbers depend on

`\\[a-zA-Z]+|\\.|\S` — a control word is one token, an escape (`\\`, `\{`, `\,`) is one, every
other **non-space** character is one.

⚠ **Whitespace is excluded, changing the research doc's definition** (`\\[a-zA-Z]+|.`, which
counts spaces). UniMERNet emits a space between every token; hand-typed LaTeX emits almost none.
Under the old definition the same expression scores twice as varied when a human typed it, so no
threshold survives crossing from the model corpus to a known-good corpus — which is precisely what
validating both directions requires.

### 3.3 The eight detectors and their constants

| Detector | Fires when | Constant, and the sweep behind it |
| --- | --- | --- |
| `token-variety` | types/tokens `< 0.20` and tokens `> 40` | § 3.4 |
| `empty-reading` | `< 5` tokens | research doc's rule. Costs **0/2,967** corpus display rows |
| `content-free` | `< 3` **content** tokens | § 3.8, added 2026-09-06. Costs **0/2,508** corpus display rows |
| `repeat-loop` | surya tail check, **or** an identical-token run ≥ 4 (≥ 10 for a digit) | § 3.5 |
| `unbalanced-braces` | escape-aware `{`/`}` counts disagree | § 3.6 |
| `unmatched-delimiters` | `\left` vs `\right` counts disagree | § 3.6 |
| `unmatched-environments` | any `\begin{X}` / `\end{X}` count disagrees | § 3.6 |
| `length-vs-crop` | tokens ÷ (crop width/height) `≥ 18` | § 3.5 |

### 3.4 `token-variety` — re-measured, and it does not reproduce

| ratio < | pathologies | non-patho model outputs | corpus display rows (2,967) |
| ---: | ---: | ---: | ---: |
| **0.20** | **2/10** | **0/74** | **28 (0.94%)** |
| 0.22 | 3/10 | 0/74 | 42 (1.42%) |
| 0.25 | 4/10 | 0/74 | 71 (2.39%) |
| 0.30 | 5/10 | 0/74 | 197 (6.64%) |

⚠ **The research doc's headline — "8 of 10 pathologies caught with zero false positives in 76" —
does not reproduce**, and the reason is not a coding error. It was measured with the
space-counting tokenisation of § 3.2 and **only against other model outputs**. Adding a
known-good corpus is what moves the number; the "zero false positives" was never tested against
LaTeX a human wrote.

**0.20 is chosen because of the roll-call, not the ratio.** Every pathology that 0.25 would add is
already caught by `length-vs-crop` and `repeat-loop`, so the 43 extra flagged coursework equations
buy nothing. Hand-checking the 28 at 0.20: about a third are artefacts of the measurement's own
LaTeX extractor grabbing preamble; the rest are genuine misfires on long partial-fraction
derivations where `z^{-1}` recurs a dozen times. That is this detector's floor, stated rather than
tuned away.

### 3.5 `length-vs-crop` — the actual winner, and it was not in the plan

1,113 tokens from one equation crop is absurd on its face, but a bare token cap cannot say so:
long correct equations and short looping ones overlap completely. **The crop separates them.** An
equation crop is one line, so `width / height` is how many glyph-heights fit across it, and a
faithful reading spends about one token per glyph-height.

| | tokens per line-width |
| --- | ---: |
| highest **good** reading (`expo/pad+96`, a 96 px over-pad that still read correctly) | 13.7 |
| lowest **degenerate** one (`eqline/pad+48`) | 21.6 |
| worst (`patho/whole_page`) | 521.0 |

**18** is the midpoint of that gap. **8 of 10 pathologies, 0 false positives** — the best single
detector here, and the only one needing anything beyond the string. It assumes one line per crop,
which is what `crops.py` produces; pass no crop rather than a wrong one.

**`repeat-loop`, and why surya's constants find nothing.** Implemented faithfully —
`base_max_repeats=4, window_size=500, scaling_factor=3.0`, tail-anchored. surya's source is not in
`~/tmp/ocr_repos`, so the scaling law is *reconstructed* from the two documented data points (a
1-char loop needs > 16 repeats, a 100-char loop > 4): `base * (1 + scaling / len(unit))` gives
16.0 and 4.12, reproducing both. The cap it implies — no unit longer than 100 chars can repeat
often enough in a 500-char window — is derived, not hardcoded.

⚠ **It fires on 0 of the 10 recorded pathologies.** UniMERNet does not run off the end: it loops
in the *middle* of a `\begin{array}` and then closes the array properly, so the tail reads
`… \end{array}` and looks healthy. `patho/whole_page` ends
`\cosh \cosh \cosh \cosh \cosh \cosh } \right) } \end{array} }` — the loop is six tokens back. A
**token-run arm** was added for that shape: an identical token repeated ≥ 4 times, or ≥ 10 for a
digit. Sweeps: coursework maximum run is 3 (`}`) symbolic and 8 (`0.3888888889`) numeric; the
pathologies reach 6 (`\cosh`) and 13 (`1`). An `array` column spec (`\begin{array} { c c c c }`)
is stripped first — it is layout, not content, and it accounts for **every one** of the 6 corpus
rows the raw run test flagged. Same move `structure.py` makes when it refuses to call a bare
numeral symbolic.

This arm is what catches `patho/blank_paper_pad96` — the confident, well-formed, compilable
hallucination off blank paper that the research doc records as caught by nothing.

### 3.6 Structural counts — free, correct, and silent

`\left`/`\right`, `\begin`/`\end`, and brace balance fire on **0 of 44 raw model outputs** and
**0 of 2,967 corpus display rows**. That silence *is* the finding: it is the same fact that kills
compile-checking — UniMERNet emits balanced LaTeX whether or not it read anything — arrived at for
one regex each. They stay because they make `latex_repair`'s work visible instead of silent, and
because a detector that has never fired is not the same thing as one that is absent.

*(The 12 corpus rows reported as `unbalanced-braces` in § 3.7 were hand-checked: all are `tabular`
fragments the measurement's extractor mis-sliced, not detector misfires.)*

### 3.7 Measured, both directions

**Recall — the 10 recorded pathologies: 10/10.**

| Detector | pathologies it caught |
| --- | ---: |
| `length-vs-crop` | 8 |
| `repeat-loop` | 4 |
| `token-variety` | 2 |
| `empty-reading` | 1 |

Nothing is caught by only `token-variety`; `repeat-loop` uniquely holds `patho/blank_paper_pad96`
and `empty-reading` uniquely holds `patho/blank_paper`.

**False positives — 74 non-pathological model outputs: 1 (1.35%).** `control/expo_base_twin`
returned the single token `\mp` and is flagged `empty-reading`. That is arguably a *true* positive
— it is the deliberately-degraded un-annotated twin whose reading the research doc already records
as wrong — and it is counted against us anyway.

**False positives — 2,967 display-maths rows extracted from all 394 `.tex` files in `content/`:
42 (1.42%), in 0.11 s.**

| Detector | rows | note |
| --- | ---: | --- |
| `token-variety` | 28 (0.94%) | ~⅓ extractor artefacts; the rest genuine, see § 3.4 |
| `unbalanced-braces` | 12 (0.40%) | all `tabular` fragments the extractor mis-sliced |
| `empty-reading` | 6 (0.20%) | all `\bottomrule`, same cause |
| `repeat-loop`, `unmatched-delimiters`, `unmatched-environments` | **0** | |
| `content-free` | **0** | added 2026-09-06 and re-swept; § 3.8 |

⚠ **The one corpus this detector set does badly on, stated plainly.** Over *inline* `$…$`
expressions — 23,324 of them — `empty-reading` flags 47%, because a great deal of inline
"mathematics" is `$n$`. That is a granularity mismatch, not a detector fault: nothing sends `$n$`
to an equation model, and `ink.regions(merge_px=64)` merges a lone glyph into its line rather than
cropping it. It is recorded because a future caller that *does* pass short crops will hit it.

**Cost.** Whole-corpus pass, `nice -n 10`: 0.11 s for 2,967 expressions. Load average unchanged
(1.44 → 1.44). No GPU, no model, no `tectonic`.

### 3.8 `content-free` — the eighth, and the hole § 7.4 (b) recorded

> Added 2026-09-06, closing § 8 item 2. Swept `nice -n 19`, CPU only: 0.11 s for 2,508 corpus
> rows, 9 ms for 146 model readings, all eight detectors.

**The reading, verbatim** — `crop_expo_base` read as `formula` in
`tmp/eval/out_crops/results.json`, PaddleOCR-VL over a 500×160 crop of the un-annotated twin:

```latex
\[\begin{aligned}\begin{aligned}\\ &\end{aligned}\\ \end{aligned}\]
```

**The definition.** *Content tokens* are `tokens()` after removing what carries no mathematics on
its own: whole `\begin{…}` / `\end{…}` constructs including the environment name, `array` column
specs (the strip `repeat-loop` already makes), grouping braces, `&` and `\\`, the math-mode
delimiters `\[ \] \( \) $`, the spacing commands, the delimiter-size prefixes `\left`/`\right`/
`\big…`, and the style selectors `\displaystyle`/`\limits`/`\nonumber`. Font selectors
(`\mathrm`, `\text`) are deliberately **kept** — they wrap content that is already counted, so
dropping them would narrow the margin against short readings and buy nothing. The reading above
scores **0**.

**The constant is pinned by `x = 1`,** the shortest expression anyone would call a legitimate
reading, which is exactly three content tokens. So `< 3` is the largest floor that leaves it alone.

| content < | corpus rows (2,508) | model readings (146) |
| ---: | ---: | ---: |
| **3** | **0** | **4** |
| 4 | 1 | 4 |
| 5 | 2 | 4 |
| 6 | 4 | 4 |

Raising it buys nothing — the same four readings are caught at every value — and only the corpus
cost moves. The corpus minimum is 3 (`\boxed{#1}`, an artefact of the extractor); the shortest
**genuine** row is `\Omega = \omega T` at 4.

**Both directions, over every recorded reading in the repo** — 44 UniMERNet crops
(`tmp/eqocr/sweep.json`), 40 background variants (`tmp/eqocr/bg.json`, post-repair text), 54 more
(`tmp/crops_check/*.json`), 8 PaddleOCR-VL records (`tmp/eval/out_*/results.json`), and 2,508
display-maths rows from all 394 `.tex` files in `content/`:

| | fires | of | note |
| --- | ---: | ---: | --- |
| content-free readings (hand-labelled) | **4** | **4** | recall 1.00 |
| everything else | **0** | 2,650 | precision 1.00 |
| known-good corpus rows | **0** | 2,508 | 0.00% |
| non-pathological model readings | **0** | 142 | 0.00% |

The four: `crop_expo_base[formula]` (0 content of 45 tokens — **the only one the other seven
miss**, and the only reading in the repo whose verdict this changes), `crop_expo_base[ocr]` (the
empty string), `patho/blank_paper` (`-`) and `control/expo_base_twin` (`\mp`). The last three
`empty-reading` already held. Counting `control/expo_base_twin` the other way — § 3.7 counts it as
a false positive while noting it is arguably a true one — moves precision to 3/4 on that one row
and changes nothing else.

⚠ **The corpus is a reconstruction, and that is worth stating.** The extractor behind § 3.7's
2,967 rows was never committed — `tmp/` is gitignored and the script is gone — so it was rebuilt:
`\[…\]`, `$$…$$` and the display environments from all 394 `.tex` files, split into rows on
top-level `\\` only. It yields **2,508**, and it reproduces § 3.7's numbers once that extractor's
*own* recorded artefacts are excluded: `repeat-loop` 0, `unmatched-delimiters` 0,
`unmatched-environments` 0 and `length-vs-crop` 0 match exactly; `token-variety` is 21 against 28,
and § 3.4 already records ~⅓ of its 28 as preamble the extractor grabbed (the cause is
`\\[2pt]` — a row break with optional spacing — being read as a display-maths open, which this
rebuild guards with a lookbehind); `unbalanced-braces` 3 against 12 and `empty-reading` 1 against
6, and § 3.6/§ 3.7 record all 12 and all 6 as `tabular` fragments, which this rebuild does not
extract. It is the same corpus measured more cleanly, not a different one.

**Its floor, stated rather than tuned away.** A lone two-entry row vector
(`\begin{pmatrix} 1 & 2 \end{pmatrix}`) is two content tokens and would fire. 0 of the 2,508
corpus rows and 0 of the 146 readings are that short, so it is a hypothetical — but it is the
shape a false positive would take, and it is why the floor is 3 and not 5.

**Two alternatives measured and rejected**, in the same spirit as the `-layout` delta and the
tight-stacking signal:

1. **A ratio arm** (`content / total < R`). The corpus minimum ratio is **0.367**, so an FP-free
   `R` is ≤ 0.36. It would add only `expo/pad+300` (0.242), which `length-vs-crop`, `repeat-loop`
   and `token-variety` already hold — and it fires on `\[\begin{aligned}x &= 1\end{aligned}\]`,
   3 content in 26 tokens = **0.115**. A model that wraps three real tokens in an environment has
   still read something. Rejected.
2. **Gating a higher floor on total tokens** (`total ≥ T and content < K`). The corpus floor does
   rise with length — min content is 6 at `total ≥ 10`, 8 at `≥ 12`, 12 at `≥ 20` — but every such
   gate fires on the same wrapped `x = 1` above (total 26, content 3), because `total` is inflated
   by exactly the scaffolding being excluded. Rejected, same counterexample.

⚠ **And a correction to § 7.4 (b), which this sweep found.** That table said the reading's 14.4
tokens per line-width was "just under § 3.5's highest recorded good reading, 13.7". **14.4 is
above 13.7**, so `length-vs-crop` at a limit of 14 *would* catch it — the claim that the threshold
"cannot be lowered" was not established by that number. It is still the wrong repair, for three
measured reasons: the margin collapses from ±4 (13.7 … 18 … 21.6) to 0.35; the detector needs a
crop, and the file-input path that surfaced the defect supplies none; and it is the wrong axis —
the identical string off a 1000×160 crop scores **7.2** and passes at any limit, while the content
count still reads 0. Re-measured 2026-09-06.

---

## 4 · Licence — the determination

`~/tmp/ocr_repos/MinerU/LICENSE.md`, read in full 2026-09-06. MinerU is **Apache-2.0 plus four
additional terms**: (1) a separate commercial licence required above 100 M MAU or USD 20 M monthly
revenue, consolidated with affiliates; (2) prominent attribution if you provide **online services
to third parties** based on MinerU; (3) **automatic, no-notice termination** on breach of 1 or 2;
(4) definitions.

**Vendoring is permitted for this project.** One person's coursework: term 1's thresholds are not
in play, no online service is provided, so term 2 does not attach. Owed under Apache-2.0 § 4 and
discharged in the module header: the `Copyright (c) Opendatalab` notice, a statement that the file
was changed and how, and a pointer to the licence.

⚠ **The teardown's summary is wrong and § 4 of it is right.**
[../research/mineru-teardown.md](../research/mineru-teardown.md) § 7.4 calls the file
"licence-clean"; § 6.1 of the same document lays out all four terms correctly. The additional
terms **travel with the file** and with anything derived from it — this is Apache-2.0-plus-riders,
not Apache-2.0 — and term 3 is self-executing. That document is not edited by this work, per its
own front-matter; the correction lives here and in the module header.

**Not done, and it should be if this repo is ever distributed:** a verbatim copy of MinerU's
`LICENSE.md` under `docs/licences/`. Apache-2.0 § 4(a) asks recipients be given the licence text,
and a URL is thinner than a file. Not created here because this work owns only the two modules,
their tests, and this document.

---

## 5 · Where this contradicts the source documents

| Source | Claim | This document |
| --- | --- | --- |
| `mineru-teardown.md` § 7.1 | "Reproducing this list by observation would cost days" | The *list* is worth having; the *implementation* corrupts output in 11 measured ways. Port the rules, not the file |
| `mineru-teardown.md` § 7.1 adoption note | only the strip-all branch needs a flag | That branch is #11 of 11. The delimiter-matching regex above it is the worse bug |
| `mineru-teardown.md` § 7.4 | "licence-clean" | Apache-2.0 **plus** four terms that travel with the code (§ 4) |
| `equation-ocr-specialists.md` § 5 | token-variety < 0.20: 8/10 caught, 0 FP in 76 | 2/10 under a spacing-invariant tokenisation; "0 FP" was never tested against human-written LaTeX (§ 3.4) |
| `equation-ocr-specialists.md` § 5.1 | surya's repeat detector is "the one to lift" | Lifted, and it fires on 0/10 — wrong shape for a decoder that closes its own array (§ 3.5) |
| `equation-ocr-specialists.md` § 5 | `patho/blank_paper_pad96` is caught by nothing | Caught by the token-run arm: 13 consecutive `1`s (§ 3.5) |

---

## 6 · Regression floor

`tests/persistent/test_latex_repair.py` (25) and `tests/persistent/test_validity.py` (40 — 34
before § 3.8's eighth detector, which added 6), in the existing style — self-contained, no course material, no model, no PDF. Every repair test names the
upstream behaviour it exists to keep out.

**11 of those cover the CLI surface itself**, at the bottom of `test_validity.py`, following the
convention `test_textlayer.py` set for `inspect` — CLI tests live in the test file of the axis the
command reports. They assert on the *report*, not on the detectors: the roll-call is complete, a
detector that could not run says so, the input file is byte-identical after both a plain run and a
`--repair` run, every shown change names a rule, and both recorded harness JSON shapes are read.
`test_cli_exposes_the_documented_commands` in `test_textlayer.py` gained `check`.

Every fixture string in those tests is a **verbatim transcription** of a recorded output — the
testing directive's rule that a fixture outside the repository is not a fixture, and `tmp/` is
gitignored.

**120 pass, none skipped:** `PYTHONPATH=src python3 -m pytest tests/ -q`
(114 before § 3.8's eighth detector; 6 new, and no existing test changed except the one asserting
the CLI's evidence string).

⚠ **The "111 pass" recorded here on 2026-09-06 does not reproduce** — the working tree collected
**114** before this change (backbone 7, crops 5, latex_repair 25, textlayer 43, validity 34). The
count was stale, not the tests; every one of the 114 passed.

---

## 7 · The delivered CLI contract

> Added 2026-09-06, when the two modules were wired. Until then § 8 item 1 read *"Neither module is
> wired to anything"* — no CLI verb, no call site. That is now closed.

### 7.1 The verb

```
ocr-handler check READINGS [--crop WxH] [--repair]
```

`READINGS` is one of three things, and nothing else:

| Input | Becomes | Crop |
| --- | --- | --- |
| a harness `results.json` | one reading per record | from the record |
| any other file | **one** reading, the whole file | `--crop`, or none |
| `-` | one reading, read from stdin | `--crop`, or none |

⚠ **This is a fourth verb, and that is a scope call the operator should confirm.**
[../scope.md](../scope.md) caps the CLI at five verbs and enumerates three (`inspect`, `extract`,
`version`), adding that *"a new capability that needs a new verb is a scope question, not a coding
task."* `check` is not a `--mode` of `extract` because it does not take a PDF — it reads a recorded
model output — and folding it in would mean `extract` accepted two unrelated input types. It joins
the free, no-GPU, writes-nothing family with `inspect`. Count is now four of five.

**Two flags, against [../directives/code-discipline.md](../directives/code-discipline.md)'s
*"WHEN tempted to add a CLI flag → DON'T"*.** Each is named here with what it buys:

- **`--crop WxH`** — `length-vs-crop` is the measured winner (§ 3.5: 8/10 pathologies, 0 false
  positives) and is the one detector that needs more than the string. Without it the detector
  reports `not evaluated: no crop size supplied` rather than passing, so the flag is the difference
  between a strong check and a weak one that does not say it is weak. Refused on a `results.json`,
  loudly: one crop cannot be true of every record, and a wrong crop poisons the best detector.
- **`--repair`** — emits repaired LaTeX on **stdout** and moves the report to **stderr**, so
  `check x.tex --repair > fixed.tex` still tells the reader what changed. Off by default: report is
  the safe thing you get by not thinking, exactly as `--mode text` is in
  [./text-layer-first.md](./text-layer-first.md) § 3.

`drop_unmatched_delimiters` — upstream's strip-every-delimiter branch, § 2.1 #11 — is **not**
exposed. It is reachable from `repair()` for anyone reproducing upstream and has no business on a
surface a user reaches for.

### 7.2 What it prints

The shape is `inspect`'s, so a reader who has run one recognises the other: a headline count, a
`verdict:` line, a band of per-item counts, then evidence only where something fired.

**One reading — the whole roll-call, including the detectors that stayed quiet.** A report that
lists only what fired cannot be checked for what it failed to look at, which is § 3.1's contract
rendered rather than restated.

```
$ ocr-handler check tmp/eval/out_crops/crop_eqline_base.formula.txt --crop 720x130
crop_eqline_base.formula.txt: 1 reading, 18 tokens (18/reading)
verdict: readings-plausible
  plausible 1   suspect 0
  · token-variety
  · empty-reading
  · content-free
  · repeat-loop
  · unbalanced-braces
  · unmatched-delimiters
  · unmatched-environments
  · length-vs-crop
  repair would change 1/1 reading — shown, not applied (--repair to emit)
    crop_eqline_base.formula.txt
      · spaced 3 \qquad
      @16 '\\qquad\\qquad+j\\qquad).\\]' -> '\\qquad \\qquad +j\\qquad ).\\]'
```

Drop the `--crop` and the last roll-call line becomes
`· length-vs-crop           not evaluated: no crop size supplied` — a detector that could not run
and one that ran and passed are different facts.

**Many readings — counts, then the evidence for each suspect one**, capped at 10 with the remainder
counted (`_SHOW`, the same trade `inspect` makes at 30 pages; the largest recorded reading set here
is 44).

```
$ ocr-handler check tmp/eqocr/sweep.json
sweep.json: 44 readings, 2,600 tokens (59/reading)
verdict: readings-suspect-partial
  plausible 33   suspect 11
  ! 11/44 readings  (token-variety 2  empty-reading 2  content-free 2  repeat-loop 4  length-vs-crop 8)
    eqline/pad+48 — length-vs-crop: 78 tokens from a 816x226 crop = 21.6 per line-width (limit 18)
    ...
    patho/blank_paper_pad96 — repeat-loop: token '1' repeated x13 consecutively
    (+1 more)
    length-vs-crop: far more tokens than one line of mathematics can hold
    nothing here was rewritten — a suspect reading is re-cropped or re-read, never
    silently patched; --repair fixes SYNTAX, not a bad reading
  repair would change 1/44 readings — shown, not applied (--repair to emit)
    patho/merged_two_equations
      · 1x \slash
      @103 '\\! \\! \\slash / ( e' -> '\\! \\! / / ( e'
```

`readings-plausible` / `readings-suspect-partial` / `readings-suspect` bands none/some/all, mirroring
`textlayer.DocText.structure_verdict` rather than inventing a third vocabulary.

### 7.3 The rules the surface enforces

1. **Never silently rewrite.** Without `--repair` nothing is emitted but a report, and the input
   file is byte-identical after either invocation. This is [../scope.md](../scope.md)'s permanent
   blacklist entry and [./structural-faithfulness.md](./structural-faithfulness.md)'s rule for a
   suspect page, held for a suspect reading.
2. **Every change names a rule and shows its span.** `Repair.notes` is the per-rule roll-call;
   `difflib.SequenceMatcher.get_grouped_opcodes(6)` gives the changed spans with six characters of
   context — enough to carry a whole control word into view, and enough to merge three adjacent
   `\qquad` insertions into one legible span instead of three unreadable `'' -> ' '` lines. A
   whole-string before/after is unreadable at 500 tokens, and that is precisely how a silent
   post-processor stays silent: upstream changed 4 of 44 and nobody would have seen it.
3. **If the text changed and no rule was named, the report says so** — `! changed with no rule
   named`. A tripwire for the class of defect § 7.4 found, not decoration.
4. **Repair fixes syntax; it does not fix a bad reading.** `--repair` prefixes each emitted
   expression with a `%` comment carrying the label and, where a detector fired,
   `[suspect: <names>]`. `%` is LaTeX's comment character, so the stream is still LaTeX and the
   suspicion travels with the text instead of staying in a terminal nobody opens again.
5. **Both recorded harness shapes are read.** `tmp/eval/*/results.json` writes
   `{name, task, size:[w,h], text}`; `tmp/eqocr/sweep.json` writes `{case, w, h, raw}`. Four
   aliases. Refusing one of them would be the per-caller divergence this project exists to end.

### 7.4 Two things the wiring found

**(a) `repair()` was changing text silently — fixed.** `_QQUAD_RE` was applied with `re.sub` and
appended no note, so `\[=|\alpha|^{n}(\qquad\qquad+j\qquad).\]` — a real recorded reading, in
`tmp/eval/out_crops/` — came back altered with an empty `notes` tuple. That contradicts § 2.4's last
row (*"silent → every change returns a note"*), the `Repair` docstring, and
`test_every_change_is_reported`, which existed and did not cover it. Now `subn` plus a note;
`test_every_change_is_reported` was widened from one string to an invariant over four, and
`test_qquad_spacing_names_its_rule` was added. **`\qquad` is load-bearing here** — it is the token
`ink.py` uses to mark a deliberately blank region — so a silent edit to it is not cosmetic.

**(b) A content-free reading passed all seven detectors — CLOSED 2026-09-06 by § 3.8's
`content-free`, the eighth detector.** `crop_expo_base` in
`tmp/eval/out_crops/results.json` (PaddleOCR-VL, 500x160 crop of the *un-annotated* twin) returned:

```latex
\[\begin{aligned}\begin{aligned}\\ &\end{aligned}\\ \end{aligned}\]
```

Nested empty `aligned` environments and nothing else — zero mathematical content. It is called
`plausible`. Every detector is individually right and the set is collectively wrong:

| Detector | Why it does not fire |
| --- | --- |
| `empty-reading` | **45 tokens**, far above the 5-token floor — but every one is scaffolding. The tokeniser of § 3.2 splits `{aligned}` into seven letter tokens plus braces, so an environment name alone costs nine |
| `token-variety` | 15 types / 45 tokens = **0.333**, well above 0.20 |
| `length-vs-crop` | 45 tokens ÷ (500/160) = **14.4**, under the limit of 18. ⚠ **Corrected 2026-09-06:** this row originally read "just under § 3.5's highest recorded good reading, 13.7". 14.4 is *above* 13.7. § 3.8 re-measures what that does and does not license |
| `repeat-loop` | the `aligned`/`\\`/`&` alternation contains no run of 4 |
| the three structural counts | perfectly balanced, which is § 3.6's whole point |

**The gap was that `empty-reading` counts *tokens*, not *content*.** § 3.8 ships the content-token
count as `content-free`, the eighth entry on the roll-call: this reading scores **0** and fires, at
**0 false positives** over 2,508 corpus rows and 146 recorded model readings. It is the only
reading in the repo whose verdict it changes, and `--repair` now carries `[suspect: content-free]`
on it instead of emitting it unflagged.

Neither of these was reachable before there was a CLI to run over the recorded output — which is the
argument for wiring a module the day it is built rather than the release after.

### 7.5 Reproduced against the recorded fixtures

Everything below was re-run through the shipped verb on 2026-09-06, CPU only, `nice -n 10`.

| Claim (§) | Source | Reproduces? |
| --- | --- | --- |
| repair changes **1 of 44** recorded outputs, and it is `\slash`→`/` | `tmp/eqocr/sweep.json` | ✅ `patho/merged_two_equations`, the only one |
| **10/10** pathologies flagged | same | ✅ `eqline/pad+{48,96,160,300}`, `expo/pad+{160,300}`, all four `patho/*` |
| `length-vs-crop` **8/10** | same | ✅ misses only `blank_paper` and `blank_paper_pad96`, which `empty-reading` and `repeat-loop` hold |
| `repeat-loop` 4, `token-variety` 2, `empty-reading` 1 | same | ✅ exactly |
| the gap: best good **13.7**, worst degenerate **521.0** | same | ✅ `expo/pad+96` = 13.7, `patho/whole_page` = 521.0, lowest degenerate `eqline/pad+48` = 21.6 |
| **1 false positive** in the 34 non-pathological sweep rows | same | ✅ `control/expo_base_twin`, `\mp`, `empty-reading` |
| `token-variety` does **not** carry its inherited 8/10 headline | same | ✅ 2/10 — it is never presented as a primary signal on this surface |

**Re-run 2026-09-06 with the eighth detector, `nice -n 19`.** Every row above still holds; the
verdict of exactly **one** reading in the whole repository changes, and it is the recorded defect.

| Claim (§) | Source | Reproduces? |
| --- | --- | --- |
| `crop_expo_base` is called `plausible` on 45 tokens of nested empty `aligned` (§ 7.4 b) | `tmp/eval/out_crops/` | ✅ before the change; now `readings-suspect`, `content-free` |
| its 14.4 tokens per line-width is "just under" the best good reading, 13.7 | `tmp/eqocr/sweep.json` | ❌ **14.4 is above 13.7.** § 3.8 re-measures. The rest of § 7.4 (b)'s table reproduces exactly |
| `content-free` costs 0 false positives | 2,508 corpus rows + 146 model readings | ✅ 4 fire, all four content-free |
| the sweep JSON verdict band is unchanged | `tmp/eqocr/sweep.json` | ✅ still 11/44 suspect — `content-free`'s 2 were already suspect |
| "111 tests pass" (§ 6) | `tests/` | ❌ the tree collected **114** before this change, all passing. Stale count, corrected in § 6 |

⚠ **`tmp/eval/out_crops/` and `tmp/eval/out_smoke/` are PaddleOCR-VL, not UniMERNet.** They come from
`tmp/eval/pvl.py` (`PaddlePaddle/PaddleOCR-VL-1.6`); the 44 recorded UniMERNet outputs this document's
measurements are drawn from are in `tmp/eqocr/sweep.json`. Both were exercised, and both are useful —
the PaddleOCR-VL set is what surfaced § 7.4 (a) and (b) — but they are different engines and the
numbers above belong to the UniMERNet set. All of it is under gitignored `tmp/`, so none of it is a
fixture in the [../directives/testing-discipline.md](../directives/testing-discipline.md) sense; the
test suite carries verbatim transcriptions instead.

---

## 8 · Open, and deliberately not done

1. ~~**Neither module is wired to anything.**~~ **Closed 2026-09-06** — `ocr-handler check`,
   § 7. `repair()` and `signals()` remain the API; the CLI is a reader over recorded output and
   still has no inference path in front of it.
2. ~~**A content-free reading passes all seven detectors.**~~ **Closed 2026-09-06** — § 3.8's
   `content-free`, the eighth detector, on the roll-call with the other seven. It fires on 4 of
   the repo's 146 recorded model readings and **0** of 2,508 known-good corpus rows; the floor of
   3 content tokens is pinned by `x = 1`. A ratio arm and a length-gated floor were measured and
   rejected — both fire on `\[\begin{aligned}x &= 1\end{aligned}\]`. The sweep also **corrected**
   § 7.4 (b): its 14.4 tokens per line-width is *above* the highest recorded good reading, not
   below it.

3. **`length-vs-crop` assumes one line per crop.** A crop holding a stacked `aligned` block fires
   legitimately. Reconsider when `crops.py` starts emitting multi-line regions.
4. **The pre-inference blank guard is still the right answer for hallucinations.** The research
   doc's cascade puts `ink.regions(min_pixels=120)` and surya's `BLANK_WHITE_THRESHOLD = 245` /
   `BLANK_PIXEL_FRACTION = 0.99` *before* the model. `repeat-loop` catches the one recorded
   instance; it is a backstop, not a substitute.
5. **`eos_reached` and the generation budget are free and unused.** The budget is VRAM-dependent
   (1152 on ≤ 6 GB, 1344 above), so a length rule must be relative to it. That needs the inference
   wrapper, which does not exist.
6. **A KaTeX parse is the better syntax gate than a compile** — the CDM paper's pix2tex row shows
   it catching ~4× more bad output. Not added: it is a Node dependency, and this module is `re`.
7. **Three files sit over the ~300-line guidance:** `latex_repair.py` 327, `validity.py` 428
   (321 before § 3.8's eighth detector, whose scaffolding list and sweep table are ~100 lines of
   the increase), `cli.py` 359. 46 of `latex_repair.py`'s are the licence determination § 4 requires in the header;
   `cli.py`'s growth is § 7's report renderer, kept in the CLI because that is where `inspect`
   renders its own roll-call and splitting one of the two would invent a convention the other does
   not follow. Recorded rather than trimmed to hit a number — `structure.py` (388) and `crops.py`
   (308) were already over it.

8. **`--repair` will not survive the `extract` rename unchanged.** When
   [./text-layer-first.md](./text-layer-first.md) § 3's `extract` verb lands, repair becomes
   something the inference path applies per crop, and `check --repair` is then a second way to do
   it. Decide there, not here.
