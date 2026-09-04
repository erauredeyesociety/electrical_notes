# Engine landscape — re-examined, 2026-09-04

An adversarial re-open of the engine question. The prior session concluded Unlimited-OCR was
the model to beat, largely because the operator named it as this project's inspiration. The
operator has since questioned that. This document treats it as a hypothesis and tests it.

**Method:** three parallel web surveys against primary sources, plus new measurements taken
today on this machine, on the remote host, and against this project's own fixture page.
Numbers marked **measured** were run today; everything else is cited.

> This document **contradicts** parts of [`unlimited-ocr.md`](unlimited-ocr.md) and of
> [`INDEX.md`](INDEX.md). Contradictions are called out explicitly in
> [§7](#7-where-this-contradicts-the-earlier-findings). Those files are not edited.

---

## Verdict up front

**No. Unlimited-OCR is not the right choice, and the case against it is much stronger than
"there might be something better."**

1. It **loses on its own chosen benchmark** to four models that were already public when its
   paper was submitted — two of which are also Baidu's.
2. Its headline text metric has **never been independently reproduced**, including from
   Baidu's own prediction files.
3. It is **worst-in-class on degraded scans** among the models near it, and has an open issue
   titled *"handwritten text results aren't very good."*
4. Its one distinguishing feature — one-shot long-horizon parsing — is **structurally
   unusable for this project**, a fact the prior session already established and then
   did not act on.

**Recommendation: PaddleOCR-VL-1.6 (0.9B, Apache-2.0) as the page engine, UniMERNet-B (325M,
Apache-2.0) as the equation engine, both local.** The strongest argument against this is in
[§8](#8-the-strongest-argument-against-my-own-recommendation) and it is not weak.

**The remote host does not change the calculus. It is an RTX 2060 with 6144 MiB — the same
ceiling, older silicon, already two-thirds occupied.** See [§4](#4-the-remote-host-measured).

---

## 1. Is Unlimited-OCR actually the right choice?

### 1.1 It is not SOTA, and was not SOTA on the day it was published

The paper (`arXiv:2606.23050`, submitted 2026-06-22) claims *"end-to-end SOTA (93.92% on
overall metric)"* on OmniDocBench v1.6. Verified from the local PDF at
`~/tmp/Unlimited-OCR/Unlimited-OCR.pdf`, Table 1. Its comparison set stops at Qianfan-OCR
(93.90).

The **official leaderboard** (`github.com/opendatalab/OmniDocBench`, v1.6_full, fetched today):

| Model | Size | Overall ↑ | Public before 2026-06-22? |
| --- | --- | --- | --- |
| **PaddleOCR-VL-1.6** | **0.9–1.0B** | **96.34** | yes — arXiv 2606.03264, 2026-06-02 |
| MinerU2.5-Pro | 1.2B | 95.75 | yes — arXiv 2604.04771, 2026-04-06 |
| GLM-OCR | 0.9B | 95.22 | yes — arXiv 2603.10910, 2026-03-11 |
| PaddleOCR-VL-1.5 | 0.9B | 94.93 | yes — arXiv 2601.21957, 2026-01-29 |
| PaddleOCR-VL | 0.9B | 94.18 | yes |
| Qianfan-OCR | 4B | 93.90 | yes |
| *Unlimited-OCR* | *3B-A0.5B* | *93.92 (self-reported)* | **not listed on the leaderboard** |

The paper says *"all other models are selected from the OmniDocBench repository."* It compares
against exactly the six models it beats and none of the four it loses to. **It was fourth-best
at the moment of publication**, and the model that beats it by 2.42 points is Baidu's own
0.9B Apache-2.0 release from three weeks earlier.

*Caveat, stated fairly:* PaddleOCR-VL runs as layout-model + recogniser, so an "end-to-end"
table can legitimately exclude it. That defence does not cover **GLM-OCR**, which is a 0.9B
end-to-end encoder–decoder VLM published three months earlier and scoring 94.62 on v1.5
against Unlimited-OCR's 93.23 — a 1.39-point loss to a model **3.3× smaller**.

### 1.2 The headline number has not been reproduced

`github.com/baidu/Unlimited-OCR/issues/66`, open since 2026-07-12, unresolved. A third party
ran the official HF `model.infer` path and the official v1.6 scorer over all 1,651 pages:

| Metric | Independently measured | Paper |
| --- | --- | --- |
| Overall | **92.45** | 93.92 |
| Text EditDist ↓ | **0.0870** | 0.042 |
| Formula CDM | 0.9583 | matches |
| Table TEDS | 0.9022 | matches |

Formula and table reproduce exactly. **Text edit distance is ~2× worse and accounts for the
entire gap.** A Baidu maintainer then supplied Baidu's own `iter_0007500` prediction files plus
the masking procedure — scoring *Baidu's own outputs* still gave 0.085. Looping, prompt format
and ngram config were ruled out by the reporter.

### 1.3 On olmOCR-Bench it is mid-table, and worst-in-class where it matters here

From the Interfaze olmOCR-Bench leaderboard (`interfaze.ai/leaderboards/olmocr`). **Caveat:
Interfaze is a commercial OCR vendor that ranks itself #1 — discount the top row, not the
relative ordering below it.**

| Model | Overall | **Old Scans** |
| --- | --- | --- |
| Chandra OCR 2 | 84.3% | 49.2% |
| Claude-Sonnet-5 | 83.5% | 51.0% |
| olmOCR v0.4.0 | 82.4% | 47.7% |
| **Unlimited-OCR** | **80.5%** | **35.4%** |
| PaddleOCR-VL | 80.0% | 37.8% |
| Gemini-3-Flash | 75.3% | 33.9% |

**Old Scans is the degraded-photocopy category — the closest proxy on any public benchmark to
scanned lecture material. Unlimited-OCR's 35.4% is the worst of the top nine by 8.5 points.**
Its Old Scans Math is 74.2%, also bottom-tier. This is directly on point for `scope.md`'s
"scanned slide decks."

*Disagreement between sources, recorded:* one of my surveys reported a different olmOCR-Bench
ordering (Infinity-Parser2-Pro 87.6 leading, Chandra-2 85.8, Unlimited-OCR absent). The two
tables are not reconcilable and neither is the AllenAI-hosted official one. **Treat exact
olmOCR-Bench positions as UNVERIFIED; treat the Old Scans weakness as well-supported**, because
it agrees with independent qualitative reports (§1.5).

### 1.4 On ParseBench it is poor at exactly the thing this project emits

ParseBench (LlamaIndex, ~2,078 pages / 169,011 rules) scores five dimensions including
**Semantic Formatting** — heading hierarchy, sub/superscript, emphasis. From the Hugging Face
model cards:

| Model | ParseBench Mean | Text Content | Text Formatting |
| --- | --- | --- | --- |
| PaddleOCR-VL-1.6 | **67.43** | 82.71 | **54.64** |
| Unlimited-OCR | 46.17 | 86.81 | **0.97** |
| GLM-OCR | 29.6 | 78 | — |

A 0.97 on formatting is effectively zero. It is corroborated by LlamaIndex's own author
publicly noting Unlimited-OCR *"is a great model on table parsing and understanding proper
reading order, but it does struggle a little on semantic formatting."* **This project's
deliverable is Markdown or LaTeX. Structure is not a nice-to-have here.**

*(The Text Formatting 0.97 figure appears on the rendered HF model-card evaluation panel but
not in the raw README; I could not re-derive it from parsebench.ai, which is JS-rendered.
**Mark the exact value UNVERIFIED**; the direction is corroborated.)*

### 1.5 The failure modes are the wrong ones for this material

From the issue tracker (78 open issues, 27 open PRs, **zero code commits since release**;
last push 2026-07-29):

- **#45 — "手写的文字 效果不是特别好"** (handwritten text results not good). A commenter
  diagnoses it as *"training distribution mismatch — handwriting is out-of-distribution…
  the misidentification happens in the visual encoder."*
- **#58 — hallucination.** 3,000 images on a 3080Ti produced empty results plus outputs
  containing *totally unrelated* text; one output says *"The image contains no discernible
  text or characters"* and then keeps generating unrelated English boilerplate.
- **#55 — looping with no safe fix.** `no_repeat_ngram_size=35` mathematically cannot detect
  repeating units shorter than 35 tokens. 0.2–1.2% of pages loop; a looping page emits
  8K–32K tokens over **100–700 seconds**. The obvious fix (`ngram=5`) crashes Overall from
  91.97 to 64.56 because it bans legitimate `<|det|>` tags.
- **#3 / #25 — maintainer, verbatim:** *"In this version, we mainly support English and
  Chinese."*
- **#1 — the ablation is missing.** Unlimited-OCR = DeepSeek-OCR + R-SWA + 2M documents of
  continued training. The paper attributes the entire +6.22 to R-SWA. The control
  (DeepSeek-OCR + same data, standard attention) was never run; promised in June, still absent.

A community side-by-side on low-quality scans (HF discussion #4) ranked it **last** of five:
olmOCR-2 > Qianfan-OCR > PaddleOCR-VL > HunyuanOCR > Unlimited-OCR, with the comment *"on faint
or low quality scans it hallucinates — when it can't read the text it invents plausible content
instead of leaving it blank."*

### 1.6 Handwriting: confirmed absent, and there is an implicit number

`grep -ric handwrit` over the cloned repo returns **zero** — README, paper PDF, and HF card.
**This confirms the prior session's finding.** Training data is ~2M PDF-native samples
pseudo-labelled with PaddleOCR.

But there *is* an implicit handwriting number the paper does not label as such. OmniDocBench's
nine page types include `note`, defined in the CVPR 2025 benchmark paper as **handwritten
notes** (116 pages). Unlimited-OCR's Table 2 breaks results down by those types; the reading is
**text edit distance ≈ 0.066 on `note`, versus 0.008 on research reports — roughly 8× worse on
handwriting than on typeset text.** *(Column alignment inferred from flattened PDF text —
indicative, not exact. UNVERIFIED.)*

Contrast: PaddleOCR-VL-1.6 benchmarks handwriting as a **named dimension** —
Handwrite_ch 85.90, Handwrite_en 92.60 (arXiv 2606.03264). GLM-OCR's Table 5 gives
PaddleOCR-VL-1.5 **87.4** on handwritten text, best of its comparison set, against
DeepSeek-OCR2 73.8, dots.ocr 71.7, MinerU2.5 **54.2**.

> **The MinerU2.5 row is the single most useful fact in this document.** It sits 2nd–4th on
> OmniDocBench at 93–95.75 and scores **54.2 on handwriting** — 33 points below PaddleOCR-VL.
> Leaderboard rank on printed documents does not transfer to handwriting. For this project the
> OmniDocBench ordering is actively misleading, and any engine decision made from it alone is
> unsound.

### 1.7 Was 8.5 s/page NF4 good or mediocre?

**The latency was fine. The 4-bit was the mistake, and it is a serious one.**

Best like-for-like consumer normalisation available — 15 OCR systems, one RTX 4070 Laptop 8 GB,
same invoice:

| System | s/page | VRAM | Field recall |
| --- | ---: | ---: | ---: |
| PaddleOCR-VL 0.9B (vLLM, batched) | **0.23** | 7.9 GB | 100% |
| PaddleOCR-VL 0.9B (vLLM, single) | **3.6** | 7.9 GB | 100% |
| Surya-2 | 4–9 | 5.0 GB | 100% |
| **Unlimited-OCR (BF16)** | **10.9** | 7.74 GB | 100% |
| GLM-OCR | 11.8 | 4.67 GB | 100% |
| dots.ocr 3B | 48 | 7.9 GB | 100% |
| PaddleOCR-VL (raw transformers) | 273 | 7.9 GB | 100% |

Our 8.5 s/page at NF4 on a 3060 Laptop is *slightly faster* than 10.9 s/page BF16 on a
comparable card — exactly what quantisation buys. So: **unremarkable but adequate.** It is
~2.4× slower than PaddleOCR-VL on vLLM single-request on similar hardware. Note that the
runtime dominates the model: the same PaddleOCR-VL goes 273 s → 3.6 s purely by switching
transformers → vLLM.

**The 4-bit finding is the one that should change behaviour.** A measured GGUF quantisation
ladder for this exact model (`vimalnakrani/unlimited-ocr-gguf`, 24 pages, 3 difficulty tiers,
temp 0, repetition suppression off):

| Quant | Size | Overall CER | Dense-text CER | Loops |
| --- | ---: | ---: | ---: | ---: |
| BF16 | 5.47 GiB | 0.78% | 1.60% | 0/24 |
| Q6_K | 2.43 GiB | 0.78% | 1.60% | 0/24 |
| **Q5_K_M** | **2.07 GiB** | **0.74%** | **1.60%** | **0/24** |
| **Q4_K_M** | 1.82 GiB | **15.64%** | **45.23%** | 1/24 |
| Q4_0 | 1.59 GiB | 44.02% | 121.44% | 2/24 |

*"Below Q5_K_M, quality falls off a cliff."* **45% CER on dense text at Q4_K_M.**

This does **not** invalidate our own NF4 measurement — bitsandbytes NF4 and llama.cpp Q4_K_M
are different algorithms, and our run produced a correct answer on the fixture page. But
`unlimited-ocr.md` records *"no measurable accuracy loss"* from **n = 1 page**, and there now
exists a 24-page controlled ladder showing a ~20× CER increase at the neighbouring 4-bit
scheme. **The n=1 claim should be retired as evidence, whatever the true NF4 number is.**

### 1.8 The feature it exists for is unusable here

"Unlimited" does not mean unlimited pages. It means **constant KV cache during decode**;
prefill still grows linearly. The paper's own Limitations section: *"Our model cannot achieve
truly unlimited parsing under a finite context length (e.g., 32K), as it is also constrained by
the prefill length."* Quality degrades across the range it does support (in-house, unreleased
test set):

| Pages | 2 | 5 | 10 | 15 | 20 | 40+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Edit distance ↓ | 0.0362 | 0.0452 | 0.0526 | 0.0787 | 0.0572 | **0.1069** |

~10.7% character error at 40+ pages, and non-monotonic (15 worse than 20) — noisy.

And the prior session already found the decisive fact: **multi-page mode is forced to `base`
encoder mode, which is disqualified for our handwriting** (`base` drops our ink to 0.62 px
strokes — sub-pixel). That finding is correct and I am not disputing it. Its consequence was
under-drawn: **if the long-horizon path cannot be used, the only reason to prefer this model
over a smaller, better-scoring, better-maintained one has been removed.** What remains is a
3B model doing single-page work that 0.9B models do better.

---

## 2. The actual 2026 state of the art

### (a) Document OCR with layout

**The headline finding of 2026 is that the frontier lives at 0.9–1.2B parameters.**
OmniDocBench v1.6_full, verified against the official leaderboard today:

| Model | Type | Size | Overall | Licence |
| --- | --- | ---: | ---: | --- |
| **PaddleOCR-VL-1.6** | specialist | 0.9–1.0B | **96.34** | **Apache-2.0** (HF card) |
| MinerU2.5-Pro | specialist | 1.2B | 95.75 | open, UNVERIFIED |
| **GLM-OCR** | specialist | 0.9B | 95.22 | **MIT** (HF card) |
| PaddleOCR-VL-1.5 | specialist | 0.9B | 94.93 | Apache-2.0 |
| Qianfan-OCR | specialist | 4B | 93.90 | UNVERIFIED |
| dots.ocr | specialist | 3B | 90.77 | UNVERIFIED |
| DeepSeek-OCR-2 | specialist | 3B-A0.5B | 90.25 | UNVERIFIED (v1 was MIT) |
| Qwen3-VL-235B | general | 235B | 89.78 | — |
| GPT-5.2 | general | — | 86.59 | — |
| olmOCR | specialist | 7B | 85.74 | Apache-2.0, **12 GB floor** |
| Kimi K2.5 | general | 1T | 84.53 | — |
| Marker | pipeline | — | 78.44 | — |

**A 0.9B model beats a 1T model by 12 points.** Gemini 3 Pro is 92.91 — beaten by five open
models under 1.3B. GOT-OCR2.0 is obsolete (olmOCR-Bench 48.3, tables 0.2); do not consider it.

**Benchmark health warning.** LlamaIndex argued on 2026-02-24 that OmniDocBench is saturated:
~1,355–1,651 pages, overweighted to academic papers, exact-match metrics that punish harmless
formatting differences; above ~94 the gains are "edge case fixing." ParseBench spreads models
much further (Infinity-Parser2-Pro 74.3 → DeepSeek-OCR-2 41.2). **Use ParseBench and the
handwriting sub-scores, not the OmniDocBench overall, to choose an engine for this project.**

### (b) Handwritten mathematical expression recognition

**Metric warning that governs everything below.** `ExpRate` is exact string match on LaTeX
tokens; it punishes visually identical output written differently. The field is migrating to
**CDM** (arXiv 2409.03643, CVPR 2025), which renders both strings and matches spatially. CDM
runs 5–15 points above ExpRate and the two are **not interchangeable**.

**CROHME 2014/2016/2019 ExpRate**, all from one internally-consistent evaluation (Uni-MuMER,
NeurIPS 2025 Spotlight, arXiv 2505.23566):

| Model | C14 | C16 | C19 | Avg | Params | Licence |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| CoMER | 58.38 | 56.98 | 59.12 | 58.16 | 6.4M | **no LICENSE file** |
| TAMER | 61.36 | 59.54 | 60.13 | 60.34 | 8.2M | **no LICENSE file** |
| PosFormer | 60.45 | 60.94 | 62.22 | 61.20 | — | **no LICENSE file** |
| UniMERNet (ext. data) | 67.4 | 68.4 | 65.4 | 67.07 | 313–325M | Apache-2.0 |
| Uni-MuMER (CROHME only) | 75.36 | 70.79 | 73.73 | 73.29 | 3.75B | see below |
| **Uni-MuMER† (ext. data)** | **82.05** | **77.94** | **79.23** | **79.74** | 3.75B | see below |

The CROHME specialists (CoMER/TAMER/PosFormer/ICAL) have **no LICENSE file at all** — verified
via the GitHub API. Default is all-rights-reserved. This independently confirms the prior
session's decision to rule them out, for a *better reason* than the one recorded.

**CROHME is unrealistically clean.** The same Uni-MuMER model scores 79.74 on CROHME and
**72.66 on HME100K** (photographed, ~10k writers) — and the repo's own unfiltered full-test
number is **69.50**, a 9–13 point drop. On MathWriting it drops to **50.66–54.32**. Plan for the
low end.

**UniMERNet is stronger than the prior session credited, and there are two of them.** The
released weights (`wanderkid/unimernet_*`, Sept 2024) are the arXiv-v2 architecture. A **CVPR
2026** redesign (Raster-Scan Attention + ConvE, single 313M model) reports UniMER-Test in CDM:

| Model | Params | **HWE (handwritten) CDM/BLEU** |
| --- | ---: | ---: |
| pix2tex | 25M | **0.213 / 0.012** — unusable |
| Texify | 312M | 0.534 / 0.341 |
| **Mathpix** | API | 0.931 / 0.806 |
| Qwen2.5-VL-72B | 72B | 0.863 / 0.756 |
| GPT-4o | API | 0.836 / 0.532 |
| **UniMERNet (CVPR 2026)** | **313M** | **0.941 / 0.899** |
| UniMERNet† (2× res) | 313M | **0.954 / 0.922** |

**A 313M Apache-2.0 model beats Mathpix on handwritten expressions.** *(Whether the CVPR-2026
weights are downloadable is **UNVERIFIED** — the arXiv entry is still at v2 and the HF
checkpoints are the Sept-2024 ones. The released `unimernet_base` numbers are HWE BLEU 0.895 /
edit 0.072, which is what we would actually get.)*

**MinerU2.5-Pro's Table 5, UniMER-Test HWE in CDM**, is the cleanest cross-family comparison:

| Model | HWE CDM |
| --- | ---: |
| Qwen3.5-397B | **97.59** ← best |
| MinerU2.5-Pro (1.2B) | 95.38 |
| GLM-OCR (0.9B) | 95.10 |
| **PaddleOCR-VL (0.9B)** | **94.45** |
| MinerU2.5 (1.2B) | 94.42 |
| Qwen3-VL-235B | 94.23 |
| DeepSeek-OCR 2 | 81.67 |

**⚠ Licence trap on Uni-MuMER.** Repo and every HF card say Apache-2.0. But the flagship
checkpoint's base, `Qwen/Qwen2.5-VL-3B-Instruct`, is under the **qwen-research** licence:
*"…FOR NON-COMMERCIAL PURPOSES ONLY."* The Apache tag is a downstream relabel over a
non-commercial base. **Clean variants exist and score better:** `Uni-MuMER-Qwen3.5-2B`
(2.2B, avg ExpRate 73.09) and `Uni-MuMER-Qwen3-VL-2B` (2.1B, 72.49) — both Apache-2.0 base
*and* derivative, both beating the 3B (72.19). This sharpens `INDEX.md`'s note on the
Qwen research licence: it is right, and it extends to a model INDEX.md lists as clean.

**The "+41.79 points" claim — confirmed, with three caveats.** 41.79 = 79.74 − 37.95. The
baseline is **Qwen2.5-VL-3B-Instruct zero-shot**, which is *the model they fine-tuned* — a
self-improvement delta, not evidence about VLMs generally. The `†` means 1.6M extra training
samples; without them the gain is 35.34. Against realistically-sized stock VLMs the gap is
**+23.3** (Qwen2.5-VL-72B, 56.40) to **+27.6** (Qwen2.5-VL-7B, 52.17).

**The "~38% expression rate for stock generalist VLMs" claim — source found, and it is being
over-generalised.** It is Uni-MuMER Table 1, Qwen2.5-VL-**3B** zero-shot, avg 37.95%. Same
table: GPT-4o 48.81, Qwen2.5-VL-7B 52.17, Gemini 2.5 Flash 55.32, Qwen2.5-VL-72B 56.40. On the
harder CROHME-2023 the same models fall to 12–34%. **Honest statement: 12–56% depending on
model size and test set. ~38% is what a *small* VLM gets on the *easiest* benchmark.**
`INDEX.md` states it as a flat fact; that is too strong.

**Dead ends to record:** `pix2tex` unmaintained since Jan 2025 and HWE BLEU 0.012. `texify`
**archived and formally deprecated** 2025-01-29. Its successor `surya` has Apache-2.0 *code*
but **modified AI-Pubs OpenRAIL-M weights** (free under $5M revenue, commercial licence above)
— easy to misread as fully open. `Pix2Text` (MIT) is the most actively maintained permissive
option but publishes no handwritten numbers.

### (c) Figure / diagram extraction

Nothing in the open-model landscape does this as a separate task well. The practical options
are (i) the page parser emitting a figure bbox with empty content — which is what
Unlimited-OCR's `<|det|>` format does and what I measured qwen3.5:9b doing today
([§4.4](#44-it-can-emit-figure-boxes-when-told-to)) — or (ii) our own structural extraction,
which is already built and is *exact*. ParseBench's **Visual Grounding** dimension is the only
benchmark that scores bbox traceability at all; open-weight models cluster at 74–79 there,
below LlamaParse at 84.

---

## 3. Cloud / API options and their privacy implications

`scope.md` blacklists cloud OCR on the core path and permits it *to evaluate* a local model.
That line is correct and nothing below should move it. This section is about the evaluation
use, and about what it would cost if the blacklist were ever reopened.

### 3.1 Pricing

| Service | Price/page | Note |
| --- | ---: | --- |
| Mistral OCR | $0.001 | |
| Google Document AI OCR | $0.0015 | |
| Azure Document Intelligence (Read) | $0.0015 | |
| AWS Textract (DetectDocumentText) | $0.0015 | olmOCR-Bench 55.3 — last place |
| Mathpix async batch | $0.0015 | + **$19.99 one-time setup** |
| Mathpix PDF (fast) | $0.005 | **free tier is 2× with a .edu email** |
| Gemini 3 Flash (as OCR) | ~$0.0044 measured | |
| Datalab Convert | $0.004 | **$10/mo free on a personal email, no card** |
| LlamaParse Agentic | ~$0.0125 | |
| GPT-5.2 | ~$0.0353 measured | |
| Claude Opus 4.5 | ~$0.1108 measured | |

Measured per-page figures are from one benchmark on printed two-column math — order of
magnitude only.

### 3.2 Accuracy, honestly

**Small open specialists beat frontier general VLMs on structured document parsing, and both
crush the legacy cloud OCR APIs.** OmniDocBench v1.6: PaddleOCR-VL-1.6 96.34 > Gemini 3 Pro
92.91 > Mistral OCR 85.66. AWS Textract is last on olmOCR-Bench at 55.3.

**Handwritten math is the exception, and it cuts against Mathpix, not for it.** The one
published head-to-head on real student handwriting (arXiv 2603.00895, UC Irvine, ~800 students,
handwritten calculus quizzes, 2026-03-01): on a fixed challenging subset of 171 solutions,
**GPT-4.1-mini achieved 84% acceptable transcriptions versus Mathpix's 55%.** And directly
relevant to us: *"Mathpix did not reconstruct any diagrams from student work."*

That same paper names the two failure modes that matter most for preserving an instructor's
ink verbatim: **hallucination on blank or sparse regions**, and **silent autocorrection of
mathematical errors** (<2% of samples, reducible with an explicit "do not correct" instruction).
**I reproduced the first of these today** — see [§4.3](#43-it-hallucinates-on-a-blank-crop).

### 3.3 Privacy — the part that actually matters for coursework

The material is a university's copyrighted lecture PDFs plus an instructor's live annotations.

| Provider | Trains on your data by default? | Zero-retention without a sales contact? |
| --- | --- | --- |
| **Mathpix** | **Yes** — `improve_mathpix=true` is the **default** | Yes — set it `false` per request |
| **Gemini API — free / AI Studio** | **YES, plus human review** | No |
| Gemini API — paid | No | Per-project approval, sales needed |
| Google Document AI | No (in-memory, 1-day failsafe TTL) | Effectively default |
| Azure Document Intelligence | No | Yes — 24 h, or Delete Analyze Result |
| **AWS Textract** | **YES by default** | Needs AWS Organizations opt-out policy |
| Anthropic / OpenAI / Mistral | No | **ZDR is enterprise-gated** |
| LlamaParse | No | Yes — `do_not_cache=True` |
| **Datalab public Playground** | **YES — perpetual, irrevocable, no opt-out or deletion right** | **No** |

Three traps worth naming:

1. **Mathpix collection is opt-out, not opt-in.** *"By default, we collect information like
   requests and responses for QA purposes."* Setting `improve_mathpix=false` deletes the source
   immediately — but also disables dashboard history.
2. **The Gemini free/paid line is the single most consequential setting.** Unpaid terms:
   *"human reviewers may read, annotate, and process your API input and output."* Paid: they
   do not train on it. The trap is that *"Your access to Google AI Studio is a 'Paid Service'
   even when it is offered free of charge, as long as the account has access to a Cloud Project
   with an associated and active Cloud Billing account."* **A zero-spend billing account
   attached to the project is what flips it.**
3. **Datalab's Playground grant is the worst term in the set** — *"perpetual, irrevocable…
   license to use, reproduce, modify, create derivative works from, and otherwise exploit all
   Playground Data,"* with no opt-out or deletion right. Their paid API is fine. **Never paste
   course material into the Playground.**

**Conclusion for this project: the blacklist stands.** If a cloud model is ever used as an
*evaluator*, the only options that need no sales contact are LlamaParse with
`do_not_cache=True`, Mathpix with `improve_mathpix=false`, Google Document AI, and Azure DI.

---

## 4. The remote host — measured

**The premise that the SSH tunnel "removes the 6 GB ceiling entirely" is false.**

### 4.1 What the remote actually is

Read-only probe over SSH, 2026-09-04:

```
hostname                    pwnstar
GPU                         NVIDIA GeForce RTX 2060, 6144 MiB total, 4137 MiB already in use
compute capability          7.5 (Turing)
CPU                         16 cores
RAM                         31 GB, 293 MB free
swap                        20,388 MB of 20,388 MB used  ← fully exhausted
load average                46.58 / 164.30 / 94.39
ollama                      0.30.10
```

| | local RTX 3060 Laptop | remote RTX 2060 |
| --- | --- | --- |
| VRAM | 6144 MiB | **6144 MiB — identical** |
| Architecture | Ampere (sm86) | Turing (sm75) — older |
| Free at rest | ~6 GB (display on iGPU) | **~2 GB** (4137 already used) |
| Contention | ours alone | shared, load avg 46–164, swap exhausted |

**The remote is the same VRAM ceiling on older silicon with a third of it already gone, on a
thrashing multi-user box.** It is not an upgrade. On the specific axis that drove every prior
decision — VRAM — it is strictly worse.

### 4.2 What the model actually is, and how it runs

`/api/show`: `qwen3.5:9b` = **9,653,104,368 params, Apache-2.0**, Q4_K_M GGUF, hybrid
attention/SSM (`qwen35.ssm.*` keys present), vision tower 27 blocks, patch 16, merge 2.
Native context 262,144.

`/api/ps` while loaded:

```
size        6,274,049,635      (6.27 GB)
size_vram   1,399,230,299      (1.40 GB)   ← 22% resident
context_length  4096                       ← not 262144
```

**Only 22% of the model is on the GPU. The rest runs on CPU.** Confirmed by `top` during a
page request: `llama-server` at **775% CPU** with `nvidia-smi` reporting **0% GPU utilisation**.

Measured throughput: **~5 tok/s decode, ~22–42 tok/s prefill.** For reference a 9.7B Q4 model
fully resident on a 6 GB card would be an order of magnitude faster.

**And the loaded context is 4096 tokens.** A single 200 dpi page consumed **3,952 prompt
tokens** — 96% of the window before a single output token. There is no room for a long page,
and none at all for multi-page work.

### 4.3 What it produced — measured today

Fixture: this project's own page, `content/cesc_410/lectures/f26_lctr02_DT signals and
systems-plw.pdf` page index 4, PyMuPDF @ 200 dpi (1700×2200), plus its un-annotated twin as the
standing control. Plus `content/cesc_470/Module 01…pdf` page index 12 (born-digital diagram
slide, 2667×1500) with its text layer as ground truth.

| Test | Input | Prompt tok | Wall | Result |
| --- | --- | ---: | ---: | --- |
| Diagram slide → Markdown | 2667×1500 | 3952 | **222.3 s** | structure right, **transcript wrong** — see below |
| **Equation crop, annotated** | 800×150 | 158 | **14.9 s** | `= \|\alpha\|^{n}(\cos(w_0 n)+j\sin(w_0 n))` — **correct** |
| **Equation crop, base twin (control)** | 800×150 | 158 | 11.3 s | `= \|\alpha\|^{n}(\qquad + j \qquad).` — **control reproduces** |
| 2nd equation crop, annotated | 480×140 | 93 | 11.9 s | `(e^{i w_0})^n = e^{i w_0 n}` — **`i` substituted for the written `j`** |
| 2nd crop, base twin (blank) | 480×140 | 93 | 6.8 s | **`\frac{1}{\sqrt x}` — pure hallucination** |
| Full page, generic prompt | 1700×2200 | 3697 | **183.3 s** | equations perfect, **everything else omitted** |
| Full page, explicit OCR prompt | 1700×2200 | 3755 | **202.7 s** | **complete and correct, with figure bboxes** |

**The control experiment reproduces, on a completely different model family.** Annotated crop
→ filled content; base twin → `\qquad` exactly where the deliberately-left blanks are. This
independently validates the methodology `unlimited-ocr.md` established. Keep it.

*Nuance worth recording:* both models emit `\quad`/`\qquad` for blanks, which suggests it is a
shared training convention rather than a model-specific tell. The evidence is the **difference
between the two runs**, not the token itself — and that difference now holds across two
unrelated architectures.

**On the born-digital slide it is not a transcriber.** Against the PyMuPDF text layer it
omitted the caption *"The five classic components of a computer"*, the page number, and the
callout; and it **expanded `PC` to "PC (Program Counter)"** — a gloss that is not on the slide.
Plausible, correct as physics, and *not what the page says*. This is exactly the "hallucinate
plausible but visually unsupported corrections" failure OmniHandwritingOCR (arXiv 2608.18586,
CIKM 2026) reports across thirteen systems.

**It hallucinates on a blank crop.** The second crop region contains no ink at all on the base
twin — it is empty graph paper. The model returned `\frac{1}{\sqrt x}`. **For a pipeline that
crops regions and feeds them to a recogniser, a recogniser that invents an expression from
nothing is a correctness hazard, not a quality issue.** Any engine we adopt needs a
blank-region guard, and our `ink.py` pixel count is the obvious one.

**It substitutes `i` for `j`.** On the cropped `(e^{jw_0})^n`, the handwritten `j` came back as
`i` — the mathematical convention winning over the electrical-engineering one written on the
page. Language prior over pixels. WildHandBench (Aug 2026) traces **63–91% of model errors on
handwriting to language priors**; this is one.

### 4.4 It can emit figure boxes when told to

The generic prompt lost the header, both case labels, both plots and the footer. The explicit
prompt — *"You are a document OCR engine… transcribe EVERY element… emit each plot as
`FIGURE [x1,y1,x2,y2]` normalised 0–1000… do not summarise"* — returned all of it:

```
LO2. p.4
③ $-1 \leqslant \alpha \leqslant 0$
FIGURE [358,79,690,280]
④ $\alpha < -1$
FIGURE [358,290,690,491]
- When $\alpha$ is complex
$\begin{aligned} \alpha &= |\alpha| e^{j w_0} \\ &\rightarrow x[n] = \alpha^n = |\alpha|^n e^{jw_0 n} \\
 &= |\alpha|^n (\cos(w_0 n) + j \sin(w_0 n)). \end{aligned}$
$(e^{jw_0})^n = e^{jw_0 n}$
DT signals and systems Page 5
```

Every element, in reading order, equations correct (and `j` correct this time, at full-page
scale). **I cropped both predicted boxes and looked at them: they are approximately right but
systematically tight** — box 1 clips the left end of the *n*-axis, the right end of the dashed
envelope, and the `→n` label. Usable with ~5% padding; not usable raw.

So the omission was a prompting artefact, not a capability limit. **That distinction matters:
it means a general VLM *can* do the whole contract, and the earlier "no single general VLM"
decision was reasoning from the wrong evidence** (see §7).

### 4.5 Verdict on the remote

| | |
| --- | --- |
| VRAM ceiling removed? | **No.** Same 6144 MiB, older GPU, 4137 MiB already taken |
| Faster? | **No.** 183–222 s/page vs Unlimited-OCR's 8.5 s locally — **21–26× slower** |
| Bigger context? | **No.** Loaded at 4096; one page is 3,952 tokens |
| Reliable? | **No.** The tunnel dropped three times during this session; the host is at load 46–164 with swap exhausted |
| Useful at all? | **Yes — as a second opinion on cropped equations.** 15 s/crop is tolerable and it got them right |

**Genuine value: it is a free, Apache-2.0, architecturally-unrelated second reader for
cropped expressions, and it reproduced the ink control.** The prior session already wanted a
"cheap disagreement signal" between UniMERNet Base and Tiny; this is a much better one, because
it disagrees for different reasons. Use it for that. Do not build a page pipeline on it.

---

## 5. What I would actually recommend

### Stage 2a — page parsing: **PaddleOCR-VL-1.6**

0.9–1.0B, **Apache-2.0** (HF card), OmniDocBench v1.6 **96.34** (#1), ParseBench mean **67.43**
vs Unlimited-OCR's 46.17, and — decisively for us — the **strongest published handwriting
evidence of any open model**: Handwrite_en 92.60 / Handwrite_ch 85.90 (own paper), 87.4 on
GLM-OCR's independent comparison (best of that set), UniMER-Test HWE **94.45 CDM** on
MinerU2.5-Pro's independent table.

**It fits in 6 GB, and the prior session's refutation of that was based on the wrong path.**
A user on HF discussion #59 reported 45 GB → **3.3 GB** and 2 min → **19 s** purely by passing
`attn_implementation="flash_attention_2"` and wrapping in `torch.inference_mode()`. The 8 GB
figure in the prior research is FastDeploy's *serving* recommendation, not a transformers
single-image floor. Flash-attention-2 supports Ampere, so it applies to our 3060.
**UNVERIFIED on this machine — measure it before committing.**

### Stage 2b — cropped equations: **UniMERNet-B**, kept

325M, Apache-2.0, 681 MiB measured peak here, ~0.5 s/expression. Its released HWE numbers
(BLEU 0.895 / edit 0.072) hold up against everything published since, and the CVPR-2026 version
of the same architecture beats **Mathpix** on handwritten expressions at 313M. **The prior
session's choice was right and this survey strengthens it.**

Add **`Uni-MuMER-Qwen3-VL-2B`** (2.1B, Apache-2.0 *base and derivative*) as the second opinion,
**not** the 3B that INDEX.md names — that one sits on a non-commercial Qwen base. Or use the
remote qwen3.5:9b for free, which needs no local VRAM at all.

### Stages 0/1 — unchanged

PyMuPDF routing and structural ink extraction are the best findings in the project and nothing
in this survey touches them. Structural extraction is *exact*; every model here is approximate.

### The decision procedure, not just the answer

The single most important methodological finding is §1.6's MinerU2.5 row: **93–95.75 on
OmniDocBench, 54.2 on handwriting.** Rank on printed documents does not predict handwriting.
So:

1. **Do not choose by OmniDocBench overall.** Choose by handwriting sub-score, ParseBench
   semantic formatting, and olmOCR-Bench Old Scans.
2. **Run the head-to-head on our fixture page**, as INDEX.md already says. It is still right.
   Add PaddleOCR-VL-1.6 to the slate and drop Unlimited-OCR to a baseline.
3. **Always run the un-annotated twin as a control.** Now validated on two model families.
4. **Add a blank-region guard.** §4.3 shows a hallucinated expression from empty paper.
5. **Never trust n=1.** §1.7's quantisation ladder is the cautionary tale.

---

## 6. Corrections to my own sub-agents, for the record

- One survey reported *"I found no evidence Baidu Unlimited-OCR exists under that name."*
  **Wrong.** Verified locally: `~/tmp/Unlimited-OCR`, remote `github.com/baidu/Unlimited-OCR`,
  MIT, arXiv 2606.23050, 25,189 stars, 2.93M HF downloads/month.
- Two surveys returned **irreconcilable olmOCR-Bench tables**. Marked UNVERIFIED in §1.3.
- "OmniDocBench v2" does not exist. The line is v1.0 → v1.5 → v1.6 → v1.7.
- Unsiloed's "#1 at 88.0" and Nanonets "OCR-3 at 87.4" are **self-reported marketing on their
  own harness**. Discard.
- SEO claims of "GPT-5 achieves 95% handwriting accuracy" / "1.22% CER on IAM" have **no
  primary source**. Discard.
- TexTeller's claimed 88.0/85.9/85.8 CROHME is **self-inconsistent** (its own CROHME-2023 is
  61.8) and its released weights predate the paper by 14 months. Discard.

---

## 7. Where this contradicts the earlier findings

| Earlier claim | This document | Which evidence is stronger |
| --- | --- | --- |
| `unlimited-ocr.md`: *"It runs, and meets scope.md's success criterion in a single 8.5 s pass"* | **Both true and both beside the point.** It is 4th on its own benchmark, unreproduced, worst-in-class on degraded scans, 0.97 on ParseBench formatting, and its one distinguishing feature is unusable here | **This document.** The prior finding is a valid *measurement* generalised into a *choice*, from n=1 page. Leaderboards, an independent reproduction failure, and an issue tracker are broader evidence than one page |
| `unlimited-ocr.md`: NF4 has *"no measurable accuracy loss"* | A controlled 24-page quantisation ladder for this model shows **Q4_K_M at 15.64% CER vs BF16's 0.78%**, and 45.23% on dense text | **This document, with a caveat.** bnb-NF4 ≠ llama.cpp-Q4_K_M, so this does not disprove our number. But "no measurable loss" from **n=1** is not evidence either way and should be retired |
| `INDEX.md`: *"PaddleOCR-VL — 'fits comfortably' refuted… the vendor's own documented floor exceeds 6 GB"* | **The refutation repeats the exact error it corrected for Unlimited-OCR.** 8 GB is FastDeploy's *serving* recommendation; the transformers path with flash-attn-2 + `inference_mode` was measured by a third party at **3.3 GB** | **This document, provisionally.** `unlimited-ocr.md` correctly separated the sglang path from the transformers path for Baidu's model, then judged PaddleOCR-VL by its serving doc. Same mistake, uncorrected. **Verify on this GPU before acting** |
| `INDEX.md`: *"Stock generalist VLMs ~38% expression-rate on cropped handwritten math"* | Source found — Qwen2.5-VL-**3B** zero-shot on the *easiest* benchmark. The real range is **12–56%**, and Qwen3.5-397B now leads UniMER-Test HWE at **97.59 CDM**, beating every specialist | **This document.** The number was quoted accurately but generalised past what it supports |
| Session record: *"No single general VLM"* | **Overstated as a rule.** Measured today: a stock, Apache-2.0, general VLM produced a complete, correctly-ordered, LaTeX-correct transcription of our fixture page *with figure bounding boxes* (§4.4), and reproduced the ink control | **This document on the principle; the prior decision still stands on the practicalities.** It took 202.7 s on a 9.7B model 78% on CPU. The right conclusion is "not a general VLM *at this cost*", not "not a general VLM" |
| `INDEX.md`: CROHME specialists ruled out because *"no usable path for real lecture annotation"* | Correct, and there is a **harder** reason: CoMER, ICAL, TAMER and PosFormer have **no LICENSE file at all** — all rights reserved | **Both; this one is stronger.** A licence problem is checkable and final; a suitability judgement is arguable |
| Brief's premise: the remote host *"potentially removes the 6 GB ceiling entirely"* | **RTX 2060, 6144 MiB — identical ceiling, older GPU, 4137 MiB already in use, model 78% on CPU, context loaded at 4096, 21–26× slower** | **This document.** Directly measured today |

**Standing and unchallenged:** structural ink extraction by image-count difference; PyMuPDF over
poppler (the rasteriser changes answers); `expandable_segments:True` worth ~1.1 GiB; the SAM
attention-bias tensor as the real memory ceiling; gundam-over-base for handwriting; routing
born-digital pages away from any model; the un-annotated-twin control; serialise GPU work.
These are the project's best findings and this survey does not touch them.

---

## 8. The strongest argument against my own recommendation

**It is that I have not run PaddleOCR-VL-1.6 on this machine, and Unlimited-OCR has been run
on this machine, on this page, and it worked.**

Every number in §5 supporting PaddleOCR-VL is someone else's. Its 3.3 GB figure is one user's
comment in a GitHub discussion. Its handwriting scores are vendor-published, on vendor test
sets, in three of four cases. Its ParseBench and OmniDocBench leads are 2–20 points on
benchmarks that LlamaIndex itself argues are saturated and that OmniHandwritingOCR shows do not
predict handwriting performance. **Against that, `unlimited-ocr.md` has 4199 MiB measured,
8.5 s measured, six byte-identical repeat runs, and a correct answer on the page that is
literally this project's regression fixture — including the control run proving it read the
ink.** One verified measurement on the actual target beats a leaderboard.

Four more things that cut against me:

1. **PaddleOCR-VL is a two-model pipeline** (PP-DocLayoutV2 + the 0.9B recogniser). More
   moving parts, more VRAM, another dependency — against a project whose modules must stay
   under 300 lines and whose stack is deliberately minimal.
2. **Its handwriting evidence is thinner than it looks.** Handwrite_en 92.60 is Baidu's own
   in-house text-spotting benchmark. The independent-ish 87.4 is from GLM-OCR's paper — a
   competitor's table, which is *better* evidence, but still n=1 source. Its HF model card
   makes **no handwriting claim at all**.
3. **Switching costs are real and already sunk.** `<|det|>CATEGORY [bbox]<|/det|>CONTENT` was
   adopted as the intermediate representation *because* it is Unlimited-OCR's output format.
   Changing engines means either changing the IR or writing an adapter.
4. **Baidu is a shared upstream.** PaddleOCR-VL, Qianfan-OCR and Unlimited-OCR are all Baidu.
   Preferring one over another does not diversify anything.

**The honest resolution is not to overturn the choice on this document alone.** It is to run
the head-to-head `INDEX.md` already calls for, with the slate corrected:

| Candidate | Why on the slate |
| --- | --- |
| **PaddleOCR-VL-1.6** | #1 on OmniDocBench, best open handwriting evidence, 0.9B, Apache-2.0 |
| **UniMERNet-Base** | 681 MiB measured here, beats Mathpix on HWE, the cheapest thing that works |
| **SmolDocling-256M** | 960 MiB measured here, got the `ω₀` subscript UniMERNet-Tiny missed |
| **Unlimited-OCR NF4** | the incumbent — now a **baseline to beat**, not the front-runner |
| *qwen3.5:9b (remote)* | free second opinion on crops only; **not** a page engine |

If PaddleOCR-VL does not fit in 6 GB on this machine, or loses on the fixture page,
Unlimited-OCR keeps the job — but as a measured winner rather than an inherited assumption.
**That is the difference this document is trying to make.**

---

## Sources

**Primary, verified today**
- `github.com/opendatalab/OmniDocBench` — v1.6_full leaderboard
- `arxiv.org/abs/2606.23050` — Unlimited-OCR paper (read locally, `~/tmp/Unlimited-OCR/Unlimited-OCR.pdf`)
- `huggingface.co/baidu/Unlimited-OCR` · `huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6` · `huggingface.co/zai-org/GLM-OCR`
- `huggingface.co/PaddlePaddle/PaddleOCR-VL/discussions/59` — the 45 GB → 3.3 GB flash-attn result
- `paddlepaddle.github.io/FastDeploy/best_practices/PaddleOCR-VL-0.9B/` — "GPU Memory: 8GB or more"
- `github.com/baidu/Unlimited-OCR/issues/{1,16,45,53,55,58,66,79,90,95}`
- `github.com/run-llama/ParseBench` · `llamaindex.ai/blog/omnidocbench-is-saturated-what-s-next-for-ocr-benchmarks`

**Papers**
- PaddleOCR-VL `2510.14528` · -1.5 `2601.21957` · -1.6 `2606.03264`
- GLM-OCR `2603.10910` · MinerU2.5 `2509.22186` · MinerU2.5-Pro `2604.04771`
- olmOCR-2 `2510.19817` · LightOnOCR-2 `2601.14251` · Infinity-Parser2 `2607.07836`
- UniMERNet `2404.15254` + CVPR 2026 (openaccess) · Uni-MuMER `2505.23566` · CDM metric `2409.03643`
- OmniHandwritingOCR `2608.18586` · AI-grading / Mathpix head-to-head `2603.00895`
- Formula-parser benchmark `2512.09874` · MathWriting `2404.10690`

**Measured on this machine / this remote, 2026-09-04** — all runs under
`/tmp/claude-1000/-home-devel-electrical-notes/…/scratchpad/ocrtest/`. Not committed; re-run to
reproduce. Fixture: `content/cesc_410/lectures/f26_lctr02_DT signals and systems-plw.pdf` p.4
(0-indexed) and its twin; `content/cesc_470/Module 01 Introduction to computer technology &
ISA (1).pdf` p.12 (0-indexed).

---

**See:** [`INDEX.md`](INDEX.md) · [`unlimited-ocr.md`](unlimited-ocr.md) · [`../scope.md`](../scope.md)
