# Research — external teardowns

Studied before building. Numbers marked **measured** were run on this machine's
RTX 3060 Laptop (6144 MiB, ~4.3 GB free); everything else is from primary
sources. Anything a source could not settle is marked UNVERIFIED in its file.

⚠ **The deployment target is not this machine.** It is the skytracker
**Quadro RTX 5000 — 16 GB, and Turing (sm_75)**, which is a *larger* card on
*older* silicon. Every VRAM verdict below was reached at 6 GB on Ampere and at
least three of them change.
[stage2-slate-and-head-to-head-2026-09-06.md](stage2-slate-and-head-to-head-2026-09-06.md)
re-derives them and gives the protocol.

---

## Verdict

**The corpus splits into three problems with three different answers, and only
one of them needs a model.**

| Corpus | Right tool | Cost | Status |
| --- | --- | --- | --- |
| **Born-digital LaTeX** (2,594 pages) | mechanical reconstruction from vector rects — **no model** | free, CPU | path proven, precision unfinished |
| **Scanned prose** (ps160, ~400 pages) | OCRmyPDF / RapidOCR — **no GPU** | ~10 s/page, CPU | works; math does not survive |
| **Handwritten mathematics** | a model — the only place one is needed | see below | **open** |

**This is the day's main structural result.** Earlier framing treated the whole
corpus as one OCR problem; it is not, and two thirds of it never needed a GPU.

### The largest accuracy win is not a model

Feeding `ink.py`'s **existing binary mask** instead of raw pixels produced the
best of 84 measured UniMERNet outputs — recovering `|\alpha|^n` and the
`\omega_0` subscripts, and deleting a hallucinated `\frac{1}{2}` that was **the
slide's graph-paper grid read as a fraction bar**. Free, deterministic, uses
code already in the project. See [equation-ocr-specialists.md](equation-ocr-specialists.md).

### Stage 2 — handwritten maths, still open

| Candidate | Peak (measured) | Verdict |
| --- | --- | --- |
| **UniMERNet-Base** | **686 MiB alloc / 1290 MiB reserved** | incumbent; survives, weakly |
| **PaddleOCR-VL-1.6** | steady ~3.0–3.5 GiB; **loading peaks 3.6–4.6 GiB** | recommended page engine; **loading is the binding constraint**. ⚠ **True at 6 GB and on the Paddle path only.** At 16 GB it stops binding; on **Turing** a larger constraint replaces it — PaddleX gates bf16 *and* SDPA at capability ≥ 8.0, so sm_75 gets **fp32 + eager O(N²)**. The torch path has no such gate |
| TrOCR-large-handwritten | **2347 MiB** | prose near-perfect, **every equation garbage** |
| Unlimited-OCR | 4199 MiB | **demoted to baseline** — no handwriting metric, never independently reproduced |
| dots.mocr | 5,797 MiB of weights | **ruled out** — exceeds the card. ⚠ **VRAM reason void on the RTX 5000** (5,797 MiB reproduces exactly, and fits 16 GB); it stays out on its **licence rider** alone |
| GLM-OCR | n/a | **not a local model** — the repo is a cloud-API client. ⚠ **Imprecise:** the *weights* are MIT, 2.469 GiB, ~2M downloads/month. The blocker is that they ship no modeling code, so they need **native transformers-5 support** |
| MinerU | 4 GB tier scores 86.47 | **wrong tier** — its 93–95 belongs to the 8 GB config |

Resolve with ADR-0004's head-to-head — now with the **mask variants in the
slate**, and more than two equations. **The slate and the protocol are settled**
in [stage2-slate-and-head-to-head-2026-09-06.md](stage2-slate-and-head-to-head-2026-09-06.md):
five arms, 24 hand-transcribed equations across **three** strata of handwriting,
84 inferences per arm, and a win condition fixed before the run. Two UniMERNet
checkpoints newer than the one measured here (`unimernet_base_2501`,
`unimernet_hf_small_2503` — MinerU's actual default) are in it at **zero VRAM
cost**, and `Uni-MuMER-Qwen3-VL-2B` is in it because the objection that kept it
out — 4.4 GB of weights and a vLLM-only path — **fails on both halves**.

---

## Read these first

| File | What it settles |
| --- | --- |
| [classical-ocr-and-pipelines.md](classical-ocr-and-pipelines.md) | **The no-VLM path.** Fraction bars are vector rects; born-digital math is mechanically recoverable. Also: OCRmyPDF flips scanned pages to `text-layer-sufficient` at ~10 s/page, CPU-only — but 2-D math does not survive. |
| [handwriting-ocr-systems.md](handwriting-ocr-systems.md) | **Classical HTR is structurally ruled out.** The best open handwriting model's output codec has **81 classes and no `=` sign**. Kraken and docTR carry no Greek and no `√ ∫ π Σ`. Not a quality gap — a vocabulary that cannot express the answer. |
| [equation-ocr-specialists.md](equation-ocr-specialists.md) | **Compile-checking is dead** (83/84 garbage outputs compiled). Padding is a cliff at the *neighbour distance*, not a gradient. ⚠ Its token-variety headline (<0.20, 8/10, 0 FP) **does not survive re-measurement** — it was scored with space-counting tokenisation and only against other model outputs; spacing-invariant it drops to 2/10. The real winner is `length-vs-crop` (tokens ÷ crop dimension ≥ 18): 8/10, zero FP, gap 13.7 vs 521. |
| [paddleocr-vl-teardown.md](paddleocr-vl-teardown.md) | The recommendation, verified from source. **Loading peaks ≈2× weights** because `no_init_weights()` exists and is never called. Three silent CPU fallbacks, all closed by passing `device="gpu:0"` explicitly. |
| [engine-landscape-2026-09.md](engine-landscape-2026-09.md) | The survey that reopened the engine choice. ⚠ Superseded in three places by the teardown above — see its § corrections. |
| [stage2-slate-and-head-to-head-2026-09-06.md](stage2-slate-and-head-to-head-2026-09-06.md) | **The slate and the protocol, re-derived for the 16 GB Turing target.** PaddleX gates **both bf16 and SDPA at compute capability ≥ 8.0** — verified in `place.cc` and `_siglip.py` — so on sm_75 the Paddle path runs **fp32 with eager O(N²) attention**, and the torch `trust_remote_code` path (no capability gate) is the one-line escape. Also: the win condition, and why `ocr-handler check` is a **screen, not a score**. |

## Teardowns

| File | Verdict |
| --- | --- |
| [mineru-teardown.md](mineru-teardown.md) | VRAM floors are **advisory**, nothing enforces them. Handwriting 17th of 18 on WildHandBench. ⚠ Its "worth vendoring: `mfr/utils.py`" verdict is **withdrawn** — an 11-bug audit reversed it; see the landmines below. |
| [dots-mocr-teardown.md](dots-mocr-teardown.md) | Ruled out. Also carries a licence rider barring *"unauthorized digitization of publications/document scanning"* — arguably this project's use case. |
| [glm-ocr-teardown.md](glm-ocr-teardown.md) | The repo contains **no model code**; ships pointing at a cloud API. An OOM turns a page into **zero regions** while reporting success. |
| [unlimited-ocr.md](unlimited-ocr.md) | The original inspiration, now baseline. ⚠ Its NF4 "no measurable loss" came from **n=1 page**; a controlled ladder shows Q4_K_M at 15.64% CER vs bf16's 0.78%. |

---

## ⚠ Landmines found in code we nearly adopted

**The audit is done, and the answer is worse than the bug that prompted it.**
`mineru/model/mfr/utils.py` carries **11 defects**, and `\Bar` → `\hat`
(x̄ a mean becoming x̂ an estimate) ranks only **#5**. Worse:

- **`\rightarrow` is deleted outright.** `RIGHT_PATTERN` matches the `\right`
  prefix of `\rightarrow`, rewrites it to `\right.`, the delimiter counts then
  disagree, and the strip-all branch removes it. `x[n] \rightarrow X(z)` becomes
  `x[n]  X(z)`. Same for `\leftarrow`, `\leftrightarrow`, `\rightharpoonup`,
  `\lefteqn`. It is **asymmetric** — `\Rightarrow` survives untouched, so the
  corruption is invisible in any sample that happens to use the capitalised form.
- **Any compact `\left…\right` group is annihilated:** `\left(x+1\right)` → `` .
- The 21-entry delimiter whitelist omits `\langle` / `\rangle`, so an inner
  product `\left\langle x,y \right\rangle` flattens to `\left. x, y \right.`.
- `\left. y \right|_{x=0}` loses the evaluation bar **and** its subscript.
- `\textsubscript` is deleted: `H\textsubscript{2}O` → `H{2}O`.

**Measured on our own recorded outputs, both engines. Every single change is
damage; there is not one improvement in either set.**

*UniMERNet, `tmp/eqocr/sweep.json`, 44 records — 4 changed:*

| case | what upstream did |
| --- | --- |
| `eqline/pad+96` | **`\rightarrow` deleted** — `{ \rightarrow \chi[n] = ...` → `{  \chi[n] = ...` |
| `eqline/pad+300` | `\;` → `\ ;` — a spacing command split into a space and a **semicolon** |
| `expo/pad+300` | `\left(` → `(` — the delimiter dropped from a nested `array` |
| `patho/merged_two_equations` | `\slash` → `/` |

The first is the arrow bug firing on genuine model output, not a constructed case.

*PaddleOCR-VL-1.6 (the recommended page engine), `tmp/eval/out_*/` — **6 of 6
changed**, because it emits `\[ … \]` and upstream breaks that delimiter every
time (`\[` → `\ [`). The worst:*

```
in:  \[=|\alpha|^{n}\left(\cos(\omega n)+j\sin(\omega n)\right).\]
out: \ [=|\alpha|^{n}\left. n)+j\sin(\omega n)\right.
```

The entire `\cos(\omega` term is gone and the display math is broken — it no
longer compiles. That input is a **correct** reading of the crop; UniMERNet never
managed it, degenerating across all 44 sweep records to `\cos ( \cos n )` and
`\sin ( w \sin )`. So upstream's single most destructive edit lands on the best
reading either engine produced of that equation.

A latent bug came out with them: the `align*` pattern is assembled by string
concatenation, so the `*` is a **regex quantifier** and `\begin{align*}` can
never match.

**Verdict: do not vendor.** We ship our own `latex_repair.py` — see
[../plans/latex-repair-and-validity.md](../plans/latex-repair-and-validity.md).

**MinerU is Apache-2.0 *plus additional terms*** — $20M/month revenue cap,
attribution obligation, auto-termination. An earlier teardown called this file
"licence-clean"; it is not.

---

## Method notes worth keeping

**Ranked evidence, not blogs.** A GPU-recommender page whose VRAM table is pure
arithmetic on parameter count would have said "6 GB is fine" — and been wrong,
because the real peak is dominated by vision-attention scratch a parameter count
cannot model. Two other sources returned 403 or were derivative SEO content.

**Where numbers disagree, the disagreement is the finding.** `pdftotext`
extracting *more* than PyMuPDF is what exposed a false "equations were dropped"
claim; a `-layout` delta that *inverts* on clean documents is what rejected a
proposed detector.

**A claim by a peer is a hypothesis.** Two arrived today — "equations dropped"
and "PyMuPDF layout mode beats poppler". Both failed verification.

---

**Related:** [`../findings/INDEX.md`](../findings/INDEX.md) ·
[`../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md`](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md) ·
[`../directives/gpu-discipline.md`](../directives/gpu-discipline.md)
