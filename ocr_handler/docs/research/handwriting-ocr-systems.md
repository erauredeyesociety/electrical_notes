# Handwritten text recognition (HTR) systems — survey, 2026-09-05

The four VLMs torn down so far all published weak or absent handwriting evidence. This document
asks the obvious next question: **is there a classical/specialist HTR system — a plain Python
package, no model server — that does better on the two things this corpus actually needs?**

The two needs, from [`../findings/corpus-census-2026-09-04.md`](../findings/corpus-census-2026-09-04.md):

- **(a) handwritten instructor annotations** on `content/cesc_410/lectures/*-plw*.pdf` — 2 documents
- **(b) scanned textbook chapters** in `content/ps160/` — 15 `ocr-required` documents, ~202 MB of pure scans

**Constraint set:** no ollama, no vLLM, no serving stack. Ordinary `pip`-installable packages
(fetching weights from the HF hub is fine). RTX 3060 Laptop, 6144 MiB, ~4.3 GB typically free.
Fine-tuning is blacklisted by [`../scope.md`](../scope.md).

**Method.** Four parallel web surveys against primary sources (GitHub/PyPI/HuggingFace/Zenodo JSON
APIs, not blog posts), plus **two systems actually installed and run on this machine today** under
[`../directives/gpu-discipline.md`](../directives/gpu-discipline.md). Numbers marked **measured**
were produced here. Claims I could not settle are marked **UNVERIFIED**.

> **Companion documents, written in parallel today.** Three sessions covered adjacent ground and
> none edits another. [`classical-ocr-and-pipelines.md`](classical-ocr-and-pipelines.md) covers
> Tesseract/OCRmyPDF and born-digital geometry extraction — **it measured a competing answer for
> the same 400 scanned pages this document's §8.2 recommends for**; the two are compared in
> [§8.2](#82-adopt-rapidocr-pp-ocrv6_small-as-the-no-gpu-classical-path-for-scanned-printed-pages).
> [`equation-ocr-specialists.md`](equation-ocr-specialists.md) covers the cropped-equation tier
> (UniMERNet and its challengers) in depth; **§4 here is a summary and defers to it.** This
> document's own lane is the **HTR family** — the systems built for handwriting.

---

## Verdict up front

| # | Question | Answer |
| --- | --- | --- |
| 1 | Does Kraken handle modern handwritten *mathematics*? | **No — and the refutation is not architectural hand-waving, it is the alphabet.** Its best general handwriting model has 116 output classes containing `+ - = ^ _ * /` and **no Greek, no `√ ∫ π Σ`, no super/subscript digits** |
| 2 | Is TrOCR usable? What does it need upstream? | Line-level only, needs an external segmenter. **Measured here: perfect on a handwritten prose line, total garbage on every handwritten equation on the same page** |
| 3 | Can PP-OCRv5 — the handwriting model MinerU declined to ship — be used directly? | **Yes, trivially. `pip install rapidocr onnxruntime`, 48 MB, no paddlepaddle, no torch, no server, CPU-only.** Measured here. It also cannot do maths |
| 4 | Anything else that targets HTR? | Calamari (GPL-3, frozen at TF 2.15/py3.11), PyLaia (frozen at torch 1.13/py3.10), Loghi, Pero-OCR, Transkribus (SaaS), eScriptorium (6 containers). **All line→string. None does maths. Zero published maths results across the whole family** |
| 5 | Do the CROHME specialists really have no LICENSE file? | **Verified true for CoMER, TAMER, ICAL and PosFormer.** One correction: **BTTR, their common ancestor, *is* MIT** |

**The finding that decides everything:** the entire HTR family is a **line → flat string**
transducer, and the constraint is enforced in the *output layer*, not just the architecture.
Four independent codecs inspected directly today:

| System | Model | Output classes | `=` | Greek | `√ ∫ π Σ` | super/subscript |
| --- | --- | ---: | --- | --- | --- | --- |
| PyLaia | `Teklia/pylaia-iam` (best open modern-English HTR) | **81** | **NO** | no | no | no |
| Kraken | `McCATMuS` (best general handwriting) | **116** | yes | **no** | **no** | **no** |
| docTR | every pretrained recogniser (`VOCABS["french"]`) | **126** | yes | **no** | **no** | **no** |
| docTR | the unused `VOCABS["latex"]` | 81 | yes | **no** | **no** | **no** |

**The best modern-English handwriting recogniser in the open-source HTR world physically cannot
output an equals sign.** No amount of better weights fixes a softmax with no class for `α`. With
fine-tuning blacklisted there is not even a theoretical escape.

**Recommendation** in [§8](#8-recommendation). **The strongest argument against it** is in
[§9](#9-the-strongest-argument-against-my-own-recommendation) and it is not weak.

---

## 1. What was actually run here, and what it cost

Two systems installed into `ocr_handler/tmp/htr/` (gitignored) and run against this project's own
fixture crops — the same crops [`paddleocr-vl-teardown.md`](paddleocr-vl-teardown.md) used, so the
numbers are directly comparable. Load average before/after every run; it never exceeded 5.5 and
the GPU run left it unchanged at 3.10.

### 1.1 TrOCR-large-handwritten — **measured**

`microsoft/trocr-large-handwritten`, 557,238,851 params, fp32, run under
`tools.gpu_lock.gpu_session`. Script and raw JSON: `tmp/htr/run_trocr.py`, `tmp/htr/trocr_results.json`.

| | |
| --- | --- |
| Weights on GPU | **2129 MiB** (fp32) |
| torch peak allocated / reserved | **2169 / 2186 MiB** |
| `nvidia-smi` process peak | **2347 MiB of 6144** |
| Load time | **3.3 s** (from mmapped safetensors) |
| Per line | **0.13 – 0.65 s** |
| Load average | 3.10 before → 3.10 after |

**It fits with room to spare.** Now the results:

| Input | What it is | Truth | TrOCR output |
| --- | --- | --- | --- |
| `ctrl_prose` | **positive control** — handwritten English prose | `− When α is complex` | **`-When a is complex`** ✅ |
| `eq_alpha_polar` | handwritten maths, black ink | `α = \|α\| e^{jω₀}` | `dark # also` |
| `eq_expo_ann` | handwritten maths, red ink | `(e^{jω₀})^n = e^{jω₀n}` | `( cino ) " eimon ,` |
| `eq_line_ann` | printed + handwritten maths | `=\|α\|^n(cos(ω₀n)+j sin(ω₀n)).` | `# # # ( uslwon ) # j simultaneously .` |
| `eq_line_base` | control twin, blanks where the ink went | `=\|α\|^n(  +j  ).` | `e (at ( tj. ) .` |
| `ink178` | structural red-ink extract | `cos(ω₀n)  sin(ω₀n)` | `evalwyn ) . Sir Lwyn )` |
| **`blank_base`** | **empty graph paper, no ink at all** | *(nothing)* | **`0 0`** ← hallucination |

**The positive control is the load-bearing part of this experiment.** It rules out "the harness is
broken": the same model, the same code path, the same page, one line lower — and it reads the prose
essentially perfectly. (`α → a` is expected: the decoder's vocabulary is English BPE and has no `α`.)

Three things to take from it:

1. **`\sin` decoded as the word "simultaneously".** That is a language prior beating the pixels, in
   the purest form available. WildHandBench traces 87–98% of model formula errors to exactly this
   mechanism; here it is, reproducible in 0.27 s on a 558M model.
2. **No LaTeX, ever.** `^n` came back as `"` or `#`. There is no superscript in the output space.
3. **It hallucinated `0 0` from blank paper.** This independently reproduces
   [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) §4.3, where `qwen3.5:9b` invented
   `\frac{1}{\sqrt x}` from the same empty crop. **Two unrelated architectures, same failure.**
   The blank-region guard that document asked for is now supported by two data points, not one.

**Why it fails is checkable, not speculative.** The decoder is RoBERTa-large over a 50,265-token
English BPE vocabulary. `\frac`, `\int`, `\alpha`, `\sum`, `\sqrt`, `\omega`, `\pi` are **absent as
tokens**; 93.3% of the vocabulary is pure alphabetic word tokens; the only backslash tokens are the
32 JSON escapes. Byte-level BPE means LaTeX is *representable* (2–3 tokens per command) but nothing
in 684M synthetic printed text lines plus the LOB-corpus prose of IAM ever taught it to emit one.

> **Precision correction to the obvious framing:** it is wrong to say TrOCR "cannot emit LaTeX."
> It can represent any byte string. It has simply never learned one, and its prior overwhelmingly
> prefers English words. The observable consequence is identical; the reason matters because it
> means a *fine-tune* would work — which is precisely what scope.md forbids.

### 1.2 RapidOCR = PP-OCR v4/v5/v6 as ONNX — **measured**

This is the direct answer to question 3, and the install cost is the headline.

```sh
uv venv tmp/htr/rovenv && uv pip install rapidocr onnxruntime
```

**14 seconds. 399 MB venv, 373 MB excluding models. No paddlepaddle. No torch. No CUDA. No server.**
Apache-2.0 throughout. Models download on first use from ModelScope. Script and raw JSON:
`tmp/htr/run_rapidocr.py`, `tmp/htr/rapidocr_results.json`.

`rapidocr` 3.9.2 ships **197 models** spanning PP-OCRv4, **PP-OCRv5** and **PP-OCRv6**, including
`ch_PP-OCRv5_rec_server` — *the exact model MinerU benchmarked as better on handwriting and then
declined to ship as its default.* Downloaded here: 84.04 MB det + 80.66 MB rec.

Three configurations, all CPU, threads pinned to 3:

| Fixture | v6-small (default) | v5-server-ch | v5-mobile-en |
| --- | ---: | ---: | ---: |
| Engine load | **0.2 s** | 24.2 s | 3.9 s |
| handwritten prose line | 2.01 s | 15.51 s | 12.70 s |
| handwritten equation | 1.09 s | 17.62 s | 8.92 s |
| whole handwritten slide (715×860) | **0.62 s** | 15.87 s | 2.75 s |
| **`ps160` scanned textbook page** | **10.32 s / 112 lines** | 216.57 s / 121 lines | 24.16 s / 117 lines |

**On the scanned textbook page — problem (b) — it works.** First lines from PP-OCRv6_small,
verbatim:

```text
'14.2 Simple Harmonic Motion'
'437'
'period from the graph of acceleration versus time (Fig. 14.12c). Figure 14.13 shows why'
'Figure 14.13 How x-velocity vx and'
'this is so. When the object is passing through the equilibrium position so that x = 0,'
```

That is correct, including the `vx` subscript variable that both older models rendered as `Ux`.
**10 seconds a page, on CPU, with the GPU untouched.**

**Two findings that were not expected:**

- **The "handwriting" model is the wrong choice for this corpus.** `ch_PP-OCRv5_rec_server` is
  **21× slower** than PP-OCRv6_small on the textbook page and *worse on English*, mangling word
  spacing: `'period fromthe graphof acceleration versus time(Fig.14.12c)'`. MinerU's decision to
  keep a different default looks better from here, not worse.
- **PP-OCR does not hallucinate.** Fed the blank graph-paper crop it returned
  `WARNING: The text detection result is empty` and **nothing at all** — where TrOCR emitted `0 0`
  and qwen3.5:9b emitted `\frac{1}{\sqrt x}`. This is architectural: recognition is gated behind
  detection, so a page with no detected text boxes produces no text. **Detection-gated recognition
  is intrinsically hallucination-resistant, and every generative VLM in this project's slate is not.**

**On handwritten mathematics it fails like everything else** — but interestingly, less badly:

| Fixture | PP-OCRv6_small output |
| --- | --- |
| `ink178` (`cos(ω₀n) sin(ω₀n)`) | `'(3(won)'`, `'Sin(wsn)'` |
| whole handwritten slide | `'—When α is complex'`, `'x[n]=xn=1x1nejwon'`, `'=1x1^('`, `'+j'`, `').'` |

It recovered the literal `α`, and it read `x[n] = αⁿ = |α|ⁿe^{jω₀n}` as the flat string
`x[n]=xn=1x1nejwon`. **Every character is roughly there and every structural relationship is gone.**
That is the 1-D CTC ceiling made visible on this project's own page. Note also that the base twin's
deliberate blanks emit as *separate detected boxes* (`'=1x1^('`, `'+j'`, `').'`), so the
un-annotated-twin control works at the detection layer too.

---

## 2. The structural finding: why none of this family does mathematics

Every system in §3–§5 is a **line-to-string transducer**. The assumption is baked in at five levels:

1. **Network topology.** Kraken's default recognition VGSL spec contains `S1(1x0)1,3` — a reshape
   that folds the *height* dimension into the channel dimension before three 1-D BLSTMs run over
   *x* only. `kraken/lib/models.py` confirms the output is a `(classes, width)` tensor. **The y
   coordinate does not exist downstream.** A superscript has nowhere to go.
2. **Decoder.** CTC greedy/beam over a 1-D lattice. Calamari's `token_passing` and
   `word_beam_search` decoders are *lexicon*-driven — actively hostile to notation.
3. **Output schema.** ALTO/PAGE-XML `<String CONTENT="…">`. docTR's `Line.render()` is `" ".join(...)`.
4. **Segmentation taxonomy.** Kraken's shipped `blla` model merged all region and line types into
   single classes. **No formula region class exists anywhere in the HTR family.**
5. **The codec.** The one that actually settles it — verified today, per the table in the verdict.

Codec evidence, fetched and parsed directly (not quoted from a paper):

- **`Teklia/pylaia-iam`** `syms.txt`, fetched from HF: exactly **81 symbols** —
  `<ctc> ! " # & ' ( ) * + , - . / 0-9 : ; ? A-Z a-z <unk> <space>`.
  **No `=`, no `< >`, no `^ _`, no brackets or braces, no `\`, no `|`, no Greek, no operators.**
  This is the best modern-English handwriting model in the open HTR world (CER 8.44% / 7.50% with LM
  on IAM, 42.67 MB, MIT).
- **Kraken `McCATMuS`** (Zenodo 13788177, CC-BY-4.0, accuracy 92.80), `metadata.json` fetched from
  Zenodo: **116 graphemes**. Contains `= ^ _ + - * /` — *(a correction to my own sub-agent, which
  reported `+ - =` only)* — but **no Greek at all**, no `< >`, no `\`, no `|`, no `√ ∫ π Σ`, no
  super/subscript digits. `α`, the single most common symbol on this project's fixture page, is
  absent from the output layer.
- **docTR**, `doctr/datasets/vocabs.py` fetched from GitHub and executed: all nine pretrained
  recognisers use `VOCABS["french"]`, **126 characters**, of which **zero** are mathematical.
  There *is* a `VOCABS["latex"]` (81 chars, ASCII + `\{}^_=+-<>()[]/.,|`) — but no pretrained
  checkpoint references it and it too has no Greek and no operators. *(My sub-agent called it "dead
  code exposed in none of the public vocabs"; it is in fact one of 215 public vocabs. It is still
  unusable — it would require training, which is blacklisted.)*
- **Kraken's richest codec**, `german_print` (Zenodo 10519596, **CC0**), has 283 characters
  *including* super- and subscript digits `⁰¹²³⁴⁵⁶⁷⁸⁹ ₀₁₂₃₄₅₆₇₈₉` and lowercase Greek — the only
  model in the repository that does. It is a German Fraktur/antiqua **print** model, 15th–20th c.
  Wrong material entirely, and it still has no `√ ∫ ∑ ∂ ∇ ≤ ≥ ≠`.

### The search evidence

A sub-agent ran the negative searches and they are stark:

| Search | Hits |
| --- | ---: |
| Kraken issues: `mathematic` / `LaTeX` | **0 / 0** |
| eScriptorium GitLab issues: `latex` | **0** |
| Zenodo `ocr_models` community (79 records), `q=math` | **0** |
| Zenodo full-text: `kraken AND mathematical AND handwriting` | **0** |
| Calamari issues: `equation` / `LaTeX` | **0 / 0** |
| HTR-United catalogue: 138 datasets searched for `math\|equat\|formul\|scien\|physic\|student\|notebook` | **0** |

**There is no published evaluation of Kraken, Calamari, PyLaia, Pero-OCR or classical PaddleOCR on
handwritten mathematics. Not "few" — none.** This is not an accident of the literature; it is what
happens when the output space cannot express the answer.

---

## 3. System by system — the HTR core

### 3.1 Kraken — the best-engineered thing here, and the wrong tool

| | |
| --- | --- |
| Licence | **Apache-2.0** (LICENSE file, 11,324 B, verified) |
| Version | **7.1.1, uploaded 2026-09-04** — yesterday |
| Wheel | 5,079,921 B — ~99% of it is the bundled `blla.mlmodel` segmenter (5,047,020 B) |
| Python | `>=3.10,<3.14` |
| **torch** | **`>=2.9.0,<=2.14`** ← this project runs **torch 2.7.0+cu126** |
| Models | 79 Zenodo records, 2.9–63.8 MB (Party VLM 518–858 MB) |
| Model licences | mixed: CC-BY-4.0 mostly, some CC0/Apache/MIT, **one CC-BY-NC-SA** (MiDRASH Geniza) |
| Fits 6 GB | **Yes, easily.** Segmenter peaks ~1.5–2 GB on a page; recogniser is ~16 MB fp32 |
| Does maths | **No** — §2 |

Architecture: `blla` baseline segmenter (a real page-level network, 1800 px input) + CTC line
recogniser. `ketos train --spec` help text: *"CTC layer will be added automatically."* Not optional.
Kraken 7.1 added a second recogniser architecture — confusingly, also called **PP-OCRv6** — whose
own model card describes it as *"a conventional CTC-based line recognizer."* Still CTC.

**Two blockers I expected and that turned out to be false:** `coremltools~=9.0` is unconditional but
ships manylinux wheels (2.3 MB); `pyvips` is a `[pdf]`-extra only. **The real install cost is torch.**
Kraken's floor is torch 2.9.0 (released 2025-10-15) against this project's 2.7.0, so adopting it
means a second CUDA stack — ≈4.5–6 GB of wheels for the GPU path, ≈1.2–1.5 GB CPU-only.
*(Wheel-size arithmetic, not a measured install — UNVERIFIED as a disk number.)*

**Modern handwriting is nearly absent from the model repository.** Of 79 records the only English
handwriting model is **RevCity** — *18th century*. `en_best`, the only modern English model, is a
**2019 print** model with an 89-character alphabet lacking `* ^ _ | \`. The one genuinely modern,
genuinely capable entry is **PP-OCRv6 medium** (Zenodo 21788410, 63.78 MB, Apache-2.0, 15.92M
params, 44 languages, **IAM in training**, English **CER 5.90% / WER 20.35%**) — which is the same
Baidu model family §1.2 already runs more cheaply through RapidOCR.

**Documentation/code discrepancy worth recording:** `docs/user_guide/inference.rst` says the device
default is `cpu`; `kraken/configs/base.py:67` sets `device='auto'`, which Lightning resolves to CUDA
when available. Assume it will take the GPU unless told otherwise.

### 3.2 TrOCR — measured in §1.1; here is the rest of the story

| Model | Params | Weight file | Licence on the hub |
| --- | ---: | ---: | --- |
| `trocr-small-handwritten` | 62M | 245.9 MB | **none declared** |
| `trocr-base-handwritten` | 333,331,200 | 1333.4 MB | **MIT** |
| `trocr-large-handwritten` | 557,238,851 | **2229.0 MB** | **none declared** |

**Licence finding, verified myself against the HF API:** only `trocr-base-handwritten` carries a
licence tag. The other ten TrOCR checkpoints — **including the `-large-handwritten` measured in
§1.1** — declare nothing. Upstream `microsoft/unilm` is MIT and `trocr/README.md` points at it, so
the intent is clear, but the artefacts carry no grant. Discussion #10 "Add License" has been open
since 2024-11-07. **For this project (personal coursework) that is fine; it is not fine for anything
distributed.**

**Line-level only, from the paper itself:** *"we focus on the text recognition task for document
images and leave text detection as the future work."* `preprocessor_config.json` sets
`{"size": 384}` — an **int**, so images are resized to a **square, not aspect-preserving**. A
1000×80 line is stretched ~5× vertically. A wide equation is badly distorted; a full page is destroyed.

**Upstream is unmaintained.** Last code commit under `unilm/trocr` was **2023-01-07**.

**It is broken on `transformers` v5.** None of the Microsoft checkpoints ship `tokenizer.json`, and
v5 requires a fast tokenizer — the model card's own example raises `ValueError: Couldn't instantiate
the backend tokenizer`. Workaround: pin `transformers<5`, or install `sentencepiece`. *(This machine
runs 4.52.3 in the user site, which is why §1.1 ran clean; the `evalvenv` next door has 5.16.1 and
would fail.)* Also: `decoder.max_length = 20` — always pass `max_new_tokens` explicitly.

**What it needs upstream.** A line segmenter. The practical options, in order of how little they
cost: **docTR's `detection_predictor(arch="fast_base")`** (62.77 MB, Apache-2.0, maintainer-endorsed
for exactly this handoff in discussion #1734 — but word boxes, not lines); **Kraken's `blla`**
(bundled in the 5.1 MB wheel, real baseline detection, but drags in torch ≥2.9); **PP-OCR's DB
detector** via RapidOCR (already installed here, 9.47 MB, gives line boxes). Note that CRAFT and
`craft-text-detector` are **archived and pin `opencv-python<4.5.4.62`** — dead ends.

**Published TrOCR-on-maths results exist and are poor:** `Azu/trocr-handwritten-math` reports
**CER 0.508** on CROHME-2014; `win5923/TrOCR-HMER` reports **ExpRate 0.306** on CROHME-2016 with the
author's own note *"the Accuracy is worst."* Dedicated HMER models reach 55–60% ExpRate. There is one
credible maths fine-tune, `fhswf/TrOCR_Math_handwritten` (609M, 2437 MB, **AFL-3.0**, raises
`max_length` to 256, ships `tokenizer.json`), claiming 77.8% exact match on MathWriting — but that
would beat Google's own PaLIGemma baseline (69%) on the dataset's home benchmark, the card says only
*"a part of"* the dataset with no stated split, and there is no independent reproduction.
**Treat 77.8% as UNVERIFIED and probably not comparable.**

### 3.3 PaddleOCR classic (PP-OCRv5 / v6) — usable, and question 3 is answered

Measured install and runtime in §1.2. The remaining facts:

**The handwriting claim has real numbers behind it.** PaddleOCR's own PP-OCRv5 docs, in-house
recognition eval:

| Model | Handwritten CN | **Handwritten EN** | Printed CN | Printed EN |
| --- | ---: | ---: | ---: | ---: |
| PP-OCRv4_server_rec | 0.3626 | 0.2661 | 0.8486 | 0.6677 |
| **PP-OCRv5_server_rec** | 0.5807 | **0.5806** | 0.9013 | 0.8679 |

Handwritten English **more than doubled**, v4 → v5. That is what MinerU's changelog note meant.
*(The metric is never defined in the docs or in arXiv 2507.05595 — read 0.58 as "roughly 58% of
handwritten English lines come out right by some line-level measure." UNVERIFIED.)*

**PP-OCRv6 exists and resolves the MinerU teardown's open question.** Released 2026-06-11
(arXiv 2606.13108). It **kept and improved** handwriting: PP-OCRv6_medium (34.5M) scores **67.8**
on handwritten English vs PP-OCRv5_server's 59.6, at half the size and faster.
→ this supersedes [`mineru-teardown.md`](mineru-teardown.md) §5.3's *"Whether PP-OCRv6 retained
PP-OCRv5's handwriting training is stated nowhere in the repo — UNVERIFIED."* **It did.**

**The honest detail Baidu left in their own table:** on handwritten English, Qwen3-VL-235B (73.2)
and Gemini-3.1-Pro (73.0) still beat every PP-OCR model (67.8). PP-OCR wins the weighted average by
being far better everywhere else.

**Correction to my own sub-agents, recorded.** One reported that PaddleOCR should be skipped because
*"its GPU wheel is stuck at 2.6.2 from 2024-09-13 and can't be installed from PyPI at all."* The
first half is true — PyPI's `paddlepaddle-gpu` is frozen at 2.6.2, a 723.8 MB wheel — but the
conclusion is wrong three times over: Baidu ships current 3.3.1 GPU wheels from their own index
(cu118/123/**126**/128/129/130 all live); the CPU wheel is 185.8 MB and fine; and **none of that is
needed**, because RapidOCR runs the same models as ONNX in a 48 MB install, which is what §1.2
measured. *(One genuine warning survives: `paddlepaddle-gpu` and `torch` in one venv collide —
`"_CudaDeviceProperties" is already registered!`, PaddleOCR issue #12046, closed with no fix.)*

**On the dictionary question — my own prior was wrong.** I expected PP-OCR's character dictionary to
lack Greek and operators. It does not: `PP-OCRv5_server_rec` has **18,383 characters** including all
48 Greek letters, 182 characters from the Math Operators block (`∀∂∃∇∈∏∑√∝∞∠∫≈≠≤≥⊂⊕⊗⊥⋅`…), and
**all ten super- and subscript digits**. The dictionary is not the problem. The problem is
`CTCLabelDecode` emitting one flat string per line — §2 — which §1.2 then demonstrated empirically
on this project's own page. *(Dictionary inventory ≠ trained capability; the dict also contains
`⌘⌥⎋⏰`, so it looks unioned from Unicode blocks. Whether the maths classes ever fire is UNVERIFIED
— though `α` did.)*

**Licence:** PaddleOCR code Apache-2.0 (LICENSE file verified); **all** PP-OCRv5/v6, PP-FormulaNet,
PP-DocLayout and UniMERNet weight repos return `license: apache-2.0` from the HF API; RapidOCR
Apache-2.0. This is the cleanest licence story of any family in this document.

### 3.4 The rest of the classical family — dead, dying, or not for this

| System | Licence | Status | Verdict |
| --- | --- | --- | --- |
| **Calamari** 2.3.1 | **GPL-3.0** (models MIT) | last release **2024-11-12**; ~3 commits since | Capped at **py3.11 / TF 2.15 / numpy 1.x**. TF wheel 475 MB. `tensorflow-addons` is dead (last release 2023-11). Cannot share a venv with kraken. **All 9 shipped models are historical print; zero handwriting models.** TF may grab the whole GPU unless `set_memory_growth` is called (UNVERIFIED whether tfaip does) |
| **PyLaia** 1.1.2 | MIT (models MIT) | 2024-10-16 | **Worst install of all**: `python >=3.9,<3.11`, `torch>=1.13,<1.14` (Oct 2022), `pytorch-lightning==1.4.2` (Aug 2021), hard `==` pins throughout. A frozen 2022 stack in its own quarantined venv. Ships the best modern-English HTR model that exists — with the 81-symbol alphabet of §2 |
| **ocropy / OCRopus** | Apache-2.0 | **archived 2026-04-27, read-only, Python 2.7** | Dead. Kraken is its living successor |
| **OCR-D** 3.13.2 | Apache-2.0 | alive (2026-07-20) | A METS/PAGE workflow *framework*, not a model. Docker-recommended because installing several processors means installing TF **and** PyTorch. German historical-print mass digitisation. **No formula processor exists** |
| **Loghi** | **MIT** | alive (2026-08-05) | KNAW-HuC/Dutch National Archives. Laypa segmenter + CNN-LSTM/CTC recogniser + PageXML tooling, Docker-first. ICDAR 2024 paper. Pretrained model targets **17th–18th c. Dutch**. Zero maths |
| **Pero-OCR** | BSD-3-Clause | alive (2026-07-16) | Brno. Good pipeline, but the README says it is tuned for **European printed** documents and that for handwriting you should *contact the authors* — the handwriting models are not in the public release |
| **eScriptorium** | MIT text (no SPDX tag) | alive (2026-09-05) | A Django web app over Kraken. **6 containers** to wrap a package you can `pip install`. Not a library. Zero maths |
| **Transkribus** | proprietary SaaS | alive | 50 free credits/month, then €99–399/yr; **1 credit ≈ 1 page**. On-prem exists but is enterprise-priced, contact-sales (**UNVERIFIED** figures). Its PyLaia models are **not downloadable as weights**. Open-source components are a REST client, not the engine. Also: cloud, which `scope.md` blacklists on the shipped path |
| **HTR-United / CATMuS** | catalogue CC0; datasets mostly CC-BY | alive | 138 datasets, 2,099,146 lines, dates **−250 to 2024**. Overwhelmingly French/Latin historical manuscript. **Zero maths, zero science-notes, zero modern-student handwriting** |
| **docTR** 1.1.0 | Apache-2.0 | **very** alive (2026-08-21, commit 2026-09-01) | **PyTorch-only since v1.0.0 — the TF backend is deleted, not deprecated.** Maintained by t2k GmbH, not Mindee. Handwriting is issue #1049, **open since 2022-09-07**, maintainer: *"still not solved… lack of training data."* No IAM loader, no IAM CER, zero handwriting checkpoints on the hub. **Real value: `detection_predictor`, 62.77 MB, as a line/word finder** |
| **htrflow** (Riksarkivet) | **EUPL-1.2** | stale (2025-06-24) | Supports TrOCR, which is nice. But `ultralytics` (**AGPL-3.0**) is an unconditional eager import, the YOLO weights carry *"License: [More Information Needed]"* — no grant at all — and the models are 17th–19th c. Swedish court archives. Avoid |
| **EasyOCR** | Apache-2.0 | stale (2024-09-24, 530 open issues) | Handwriting appears in the README **twice, both under "What's coming next."** It is a roadmap item, not a feature |
| **mmocr** | Apache-2.0 | dead (last commit 2024-11-27) | `mmcv` has no wheels for torch ≥2.4 → **effectively uninstallable in 2026** |
| **Tesseract** | Apache-2.0 | alive | **Does not do handwriting.** No handwriting `traineddata` ships; upstream position is that it was never designed for it. Treat contrary claims as marketing |
| **OpenOCR** (Fudan) | Apache-2.0 | alive (2026-02) | Claims strong handwriting generalisation. **No published handwriting benchmark found — UNVERIFIED** |
| **Surya** | **code Apache-2.0, weights are not** | very alive | Weights are *modified* AI-Pubs OpenRAIL-M: free under **$5M funding or revenue**, commercial licence above. Not OSI. Surya 2 (650M) claims inline maths in `<math>` tags — but **handwriting appears only as one qualitative example image; there is no handwriting number**, and olmOCR-bench (its headline 83.3%) **has no handwriting category at all** ("Old scans math" is *typeset* maths in degraded scans) |

---

## 4. The maths tier — where the answer actually lives

None of §3 does mathematics. These do. Included because the question "can an HTR system read
handwritten maths" is answered "no, and here is what does instead."

| System | Licence | Size | Handwritten-maths evidence | Full page? |
| --- | --- | ---: | --- | --- |
| **UniMERNet-B** | Apache-2.0 (code + weights) | 1530 MB / **681 MiB measured peak here** | **UniMER-Test HWE: BLEU 0.895, edit 0.072; CDM 0.953** | ✗ cropped only |
| **Texo** (`alephpi/FormulaNet`) | **AGPL-3.0** (verified) | **76.5 MB** safetensors | **UniMER-Test HWE CDM 0.902** — beats PP-FormulaNet-S on all four subsets at 35% the size | ✗ cropped only |
| PP-FormulaNet_plus-S/M/L | Apache-2.0 | 245 / 589 / 694 MB | **None. The paper reports SPE and CPE only — it omits the HWE subset that UniMERNet reports.** Training corpus is entirely printed | ✗ |
| pix2tex / LaTeX-OCR | MIT | ~300 MB | **HWE CDM 0.245 / BLEU 0.012.** README TODO literally reads `- [ ] support handwritten formulae` — an *unchecked* box | ✗ |
| RapidLaTeXOCR | MIT | — | ONNX repackaging of pix2tex → same weights, same failure | ✗ |
| texify | GPL-3.0 | — | HWE CDM 0.527. **Archived 2025-01-29** | ✗ |
| **Pix2Text** | **MIT** | ~1 GB with deps | The **only MIT full-page maths pipeline** (layout → MFD → MFR + OCR → Markdown). MFR is TrOCR-architecture retrained on formulas. **Its detector is trained on printed layouts; no handwritten-page recall number exists — UNVERIFIED, and it is the load-bearing risk** | **✓** |
| Nougat | MIT | 1.4 GB (cached here) | **No** — arXiv papers. NoTeS-Bank: *"struggles to extract even the textual content"* on handwritten pages | ✓ |
| Mathpix | commercial API | — | HWE CDM 0.932 — **beaten by UniMERNet** | ✓ |

**For finding *where* the equations are on a handwritten page**, the field is thin:
**ScanSSD** (MIT, last push 2023) is designed for 600 dpi *typeset* PDF images; **MathSeer**
depends on extracting characters from *born-digital* PDFs; **DocLayout-YOLO** is **AGPL-3.0** and is
reported to misclassify handwritten content as "figure". **PP-DocLayout_plus-L** (123.3 MB,
Apache-2.0, RT-DETR-L, 20 classes including `formula` and `formula_number`) is the only credible
option — and its mAP figures are all on printed benchmarks. **No handwritten-page mAP exists
anywhere. UNVERIFIED.**

**This project does not need any of them.** `ink.py` plus structural image-difference extraction
already locates the ink *exactly*, which is better than any detector here.

### WildHandBench — the operator's question, answered

The benchmark that put MinerU 17th of 18 contains **no classical or specialist OCR system at all.
All 18 entries are VLMs.** Its formula subset is **52 images / 278 regions** scored with CDM:

| | Formula CDM |
| --- | ---: |
| **Human baseline** | **86.56** |
| Gemini 3.1 Pro | 79.42 |
| Claude Opus 4.8 | 74.11 |
| MinerU2.5-Pro | 61.79 |
| GLM-OCR | 59.01 |
| **PaddleOCR-VL-1.6** | **51.75** |
| Unlimited-OCR | 51.62 |
| MinerU-2.5 | 36.56 |
| DeepSeek-OCR2 | 18.33 |

**Note that PaddleOCR-VL-1.6 — the current recommendation in
[`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) §5 — sits at 51.75 on wild handwritten
formulas, 35 points below a human.** That does not overturn the recommendation (nothing open scores
better at that size), but it calibrates it. 87–98% of model formula errors on this benchmark are
**prior-driven** vs 46.36% for humans — the same mechanism §1.1 measured as `\sin → "simultaneously"`.

*Caveat kept in view: the paper concludes "formula recognition in current MLLMs is relatively
mature" from a 52-image subset. That conclusion is doing more work than 52 images can support.*

**Corroborating negative — NoTeS-Bank** (arXiv 2504.09249): QA over handwritten scientific notes.
**OCR-based pipelines scored 1.73%–12.46% ANLS** (Google OCR, Textract, Nougat, GOT 2.0, olmOCR,
each + an LLM) against a best VLM of 28.21% and a human at 61.11%. Everything is bad; **OCR
pipelines are catastrophically bad.**

---

## 5. The CROHME licence question — verified, with one correction

The landscape review recorded that the CROHME specialists have **no LICENSE file at all**, a harder
exclusion than "no usable path." **Checked directly against the GitHub API today** — repository
contents listing, not the `license` field alone, because a non-standard filename would show as null:

| Repo | Licence-like files in root | `license` field | Status |
| --- | --- | --- | --- |
| `Green-Wood/CoMER` | **NONE** | null | **archived 2022-09-12** |
| `qingzhenduyu/TAMER` | **NONE** | null | active (2025-07-28) |
| `qingzhenduyu/ICAL` | **NONE** | null | 2024-08-16 |
| `SJTU-DeepVisionLab/PosFormer` | **NONE** | null | active (2025-04-10) |
| **`Green-Wood/BTTR`** | **`LICENSE`** | **MIT** | archived 2024-01-22 |

**Verified: CoMER, TAMER, ICAL and PosFormer have no licence of any kind.** Default is
all-rights-reserved. The exclusion stands and is final.

**One correction to record:** [`INDEX.md`](INDEX.md) groups *"CROHME specialists (CoMER, BTTR,
PosFormer)"* in a single row. **BTTR — the common ancestor of the whole line — is MIT.** It is also
archived, four years old, and the weakest model in the family, so nothing changes practically; but
the blanket statement is not accurate and should not be repeated.

*(Note the repository paths: TAMER and ICAL live under `qingzhenduyu/`, not `SJTU-DeepVisionLab/`.
All four ship `lightning_logs/` in the repository root — research code, not a distributable.)*

---

## 6. Measured vs claimed — the table the brief asked for

Ordered by strength of evidence on **handwritten mathematics** specifically.

| System | Handwritten-**maths** evidence | Kind |
| --- | --- | --- |
| **TrOCR-large** | **Total failure on 5 equation crops from this corpus; correct on the prose control on the same page** | **measured here, today** |
| **PP-OCRv6 / v5** | **Characters recovered, all structure lost, on this corpus's own page** | **measured here, today** |
| UniMERNet | UniMER-Test HWE BLEU 0.895 / edit 0.072 / CDM 0.953 | published, vendor's own test set |
| Texo | UniMER-Test HWE CDM 0.902 | published, third-party comparison |
| Mathpix | HWE CDM 0.932 | published (by the UniMERNet authors) |
| pix2tex | HWE CDM 0.245 | published, third-party |
| texify | HWE CDM 0.527 | published, third-party |
| TrOCR fine-tunes | CROHME-14 CER 0.508; CROHME-16 ExpRate 0.306 | published, community, self-reported |
| `fhswf/TrOCR_Math` | 77.8% exact match | self-reported, **implausible vs PaLIGemma's 69% — UNVERIFIED** |
| PP-OCRv5/v6 rec | Handwritten-English **prose** 0.5806 / 67.8 | published, vendor in-house, **metric undefined** |
| Kraken PP-OCRv6 | English **prose** CER 5.90% (IAM in training) | published, Zenodo model card |
| PyLaia-IAM | English **prose** CER 8.44% / 7.50% w/ LM | published, model card |
| TrOCR (stock) | IAM CER 2.89 — **English cursive prose from the LOB corpus** | published, paper, no independent reproduction found |
| PP-FormulaNet | **absent — the paper omits the HWE subset it could have reported** | — |
| **Kraken, Calamari, PyLaia, Pero-OCR, docTR, Loghi, OCR-D, Transkribus, EasyOCR, Tesseract** | **NONE. Zero published results on handwritten mathematics for any of them.** | — |

---

## 7. Where this touches the existing research

**Strengthens:**
- The blank-region guard from [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) §4.3.
  A second, unrelated architecture (TrOCR, 558M encoder-decoder) hallucinated from the same empty
  crop. Two families, same failure — this is now a property of generative recognisers, not of one model.
- The un-annotated-twin control. It reproduced a third time, at the *detection* layer: PP-OCR emits
  the base twin's blanks as separate empty boxes.
- The methodological rule that leaderboard rank does not transfer to handwriting. §4's WildHandBench
  table extends it: PaddleOCR-VL-1.6 is #1 on OmniDocBench and **51.75** on wild handwritten formulas.
- **The CROHME licence exclusion** — verified from repository contents, §5.

**Resolves an open UNVERIFIED:**
- [`mineru-teardown.md`](mineru-teardown.md) §5.3 asked whether PP-OCRv6 retained PP-OCRv5's
  handwriting training. **It did, and improved on it** (handwritten English 59.6 → 67.8), per
  arXiv 2606.13108 and the PP-OCRv6 docs. §3.3.

**Contradicts / corrects:**

| Earlier claim | This document |
| --- | --- |
| `INDEX.md`: *"CROHME specialists (CoMER, BTTR, PosFormer)"* ruled out as a group | **BTTR is MIT.** The other four have no licence. The group statement is wrong even though the conclusion is right |
| `INDEX.md`: PaddleOCR-VL *"fits conditionally; the vendor's floor exceeds 6 GB"* — and the landscape review's rebuttal | Neither is refuted here, but note the **PP-OCR classic** path sidesteps the whole argument: 48 MB, CPU-only, no GPU at all |
| A sub-agent: *"PaddleOCR — its GPU wheel can't be installed from PyPI at all, skip it"* | **Wrong conclusion from a true fact.** RapidOCR runs the same models as ONNX; measured, 14-second install. §3.3 |
| A sub-agent: McCATMuS contains *"`+ - =` only"* | Also `^ _ * /`. Still no Greek and no operators; conclusion unchanged. §2 |
| A sub-agent: docTR's `latex` vocab is *"dead code exposed in none of the public vocabs"* | It **is** one of 215 public vocabs. Still unusable — no pretrained model uses it, and it has no Greek or operators. §2 |

**Unchallenged and untouched:** PyMuPDF routing, structural ink extraction by image-count
difference, text-layer-first. Nothing here bears on them.

---

## 8. Recommendation

**Three parts, and the second is the one that matters.**

### 8.1 Close questions 1, 2 and 4. No HTR system enters this project for the handwriting problem.

Kraken, TrOCR, Calamari, PyLaia, docTR-recognition, Loghi, Pero-OCR, eScriptorium, Transkribus,
EasyOCR and Tesseract are all excluded on the same ground, which is checkable rather than
judgemental: **their output layers have no classes for the symbols on the page.** Verified in four
codecs; the best modern-English handwriting model in the field cannot emit `=`. With fine-tuning
blacklisted, there is no path. This should become a one-line entry in the blacklist rather than a
question that gets re-asked.

### 8.2 Adopt **RapidOCR (PP-OCRv6_small)** as the no-GPU classical path for scanned printed pages.

This is the finding worth acting on, and it serves the larger half of the corpus:

- **48 MB install, 14 seconds, no torch, no paddlepaddle, no CUDA, no server, Apache-2.0** — measured.
- **10.3 s/page CPU-only** on a `ps160` scanned textbook page, 112 lines, correct text including the
  `vx` subscript variable that older models got wrong — measured.
- **Cannot hallucinate.** Detection-gated: no detected boxes → no output. Verified on a blank crop
  where two generative models invented content.
- It touches the GPU **never**, which means the 400 `ocr-required` pages can be processed while the
  operator is using the machine — the thing `gpu-discipline.md` exists to protect.
- It satisfies `scope.md` **O5** ("stay runnable with no GPU") for the first time on the recognition
  side, and it is small enough to be a dependency rather than a project.

Use `PP-OCRv6_small` (the RapidOCR default). **Do not** use `ch_PP-OCRv5_rec_server` despite its
handwriting reputation — measured here at 21× slower and *worse* on English word spacing.

> ⚠ **A competing answer was measured today, in parallel, on the same pages.**
> [`classical-ocr-and-pipelines.md`](classical-ocr-and-pipelines.md) §5 measured **OCRmyPDF 16.13.0**
> (MPL-2.0, Tesseract backend) flipping the verdict `ocr-required` → `text-layer-sufficient` on
> **6/6 ps160 pages at 3,729 chars/page**, at **10.2 s/page** (`--redo-ocr`) or **3.5 s/page**
> (`--force-ocr`). That is the same order as this document's 10.3 s/page. **Neither result was
> scored against ground truth, so neither is an accuracy claim.** What separates them today:
>
> | | RapidOCR / PP-OCRv6 (here) | OCRmyPDF / Tesseract (sibling doc) |
> | --- | --- | --- |
> | Install | **pure pip, 48 MB, 14 s** | pip + **`apt install tesseract-ocr`** — a system binary, outside the venv |
> | Output | boxes + text, as a library | **writes a text layer back into the PDF** — which is what `textlayer.py` already reads |
> | On 2-D maths | characters kept, structure lost | *"destroys every 2-D expression and emits confident Latin garbage"* — measured there |
> | On blank input | **emits nothing** (detection-gated) | UNVERIFIED |
>
> **They are composable, not rivals:** an `ocrmypdf-rapidocr` plugin exists. The honest state is
> that two engines have been timed and neither has been scored. Settle it with the labelled sample
> in [§9](#9-the-strongest-argument-against-my-own-recommendation), not by argument.

### 8.3 Leave the handwritten-maths engine question exactly where it is.

Nothing in this survey displaces
[`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) §5: a page VLM plus UniMERNet-B on
crops. Two things to add to that slate:

- **Texo** (`alephpi/FormulaNet`, 76.5 MB, HWE CDM **0.902**) — a 20M-param distillation that beats
  PP-FormulaNet-S on all four UniMER-Test subsets at 35% the size. **Licence AGPL-3.0** (verified),
  which is a real difference from everything else on the slate and needs an operator call.
- **PP-FormulaNet should be dropped from consideration.** Its paper reports SPE and CPE and silently
  omits the HWE subset its own comparison table has room for. An absent number in a paper that
  reports its siblings is evidence.

---

## 9. The strongest argument against my own recommendation

**It is that I measured one page, and I have no ground truth for it.**

`F2_ps160_m14_i08.png` is from a document classified `ocr-required` — which means it has no text
layer, which means my claim that PP-OCRv6 "reads it correctly" is *me looking at 112 output lines
and judging them plausible*. That is exactly the epistemic move this project's own research
documents keep flagging in other people's work. There is no CER here. There is no labelled sample.
The 10.3 s/page figure is solid; the accuracy figure does not exist.

Five more things that cut against me:

1. **`§8.1` generalises from four codecs to a whole field.** I inspected PyLaia-IAM, McCATMuS,
   docTR-french and docTR-latex. Kraken's Zenodo community has **79 records** and I checked three.
   `german_print` (283 chars, CC0, with super- and subscript digits) shows the family *can* carry
   more mathematical inventory than I claimed — and Kraken 7.1's PP-OCRv6 model has 44 languages
   whose codec I never pulled. The structural argument (§2) does not depend on the codecs, but the
   codec argument is the one I called decisive, and it is a sample.
2. **A sibling document measured a different engine on the same pages and it also worked.**
   OCRmyPDF flipped 6/6 ps160 pages at a comparable speed and — decisively for this project's
   architecture — **writes its result back as a PDF text layer**, which `textlayer.py` already
   knows how to read. RapidOCR returns boxes and strings that something would have to assemble.
   On integration cost alone, the sibling's answer is ahead; my advantage is a pure-pip install
   and a hallucination guard, and neither has been priced against a real accuracy number.
3. **Adopting RapidOCR adds a second recognition stack** to a project whose modules must stay under
   300 lines and whose dependency list is deliberately minimal. `ocr_handler` would then have a
   CPU/ONNX path *and* a GPU/torch path, with two sets of failure modes and two model caches. The
   simpler answer — one VLM for every page that needs recognition — is worse per page and better
   per unit of complexity, and `scope.md`'s success criteria are about honesty and coverage, not
   throughput.
4. **The problem it solves may not be the problem.** 400 `ocr-required` pages is real, but §4's
   NoTeS-Bank result (OCR pipelines at 1.73–12.46% ANLS on handwritten scientific notes) is a
   reminder that OCR-then-assemble is a weak architecture for anything but clean printed scans.
   If the eventual answer for `ps160` is "the same VLM that does everything else, just slower,"
   then RapidOCR is a detour that acquires a dependency and a runbook and then gets deleted.
5. **`§8.1` is a recommendation to stop looking, and those age badly.** Kraken shipped 7.1.1
   *yesterday* and added a whole new recogniser architecture in 7.1. The HTR world is not static.
   The right form of the blacklist entry is therefore *"line→string CTC recognisers cannot express
   2-D notation"* — a property that would have to be architecturally abandoned to change — and not
   *"Kraken is excluded,"* which could be falsified by one release.

**What would settle it:** a labelled sample. Transcribe five `ps160` pages by hand, score
PP-OCRv6_small and PaddleOCR-VL on them, and the recommendation in §8.2 becomes a measurement
instead of an impression. That is the same labelled-sample debt `scope.md` § Open decisions #3
already records for the `sparse` threshold, and it is now blocking two decisions instead of one.

---

## Sources

**Measured on this machine, 2026-09-05** — scripts and raw JSON under `ocr_handler/tmp/htr/`
(gitignored; re-run to reproduce):
- `run_trocr.py` → `trocr_results.json` — TrOCR-large-handwritten, fp32, under `tools/gpu_lock.py`
- `run_rapidocr.py` → `rapidocr_results.json` — PP-OCRv6_small / PP-OCRv5_server_ch / PP-OCRv5_mobile_en, ONNX, CPU
- Fixtures: `tmp/eval/fixtures/crop_{eqline,expo}_{ann,base}.png`, `tmp/eval/fixtures/F2_ps160_m14_i08.png`,
  `tmp/structural/ink_{80,178}.png` (plus two crops cut today: `ctrl_prose_when_alpha.png`, `eq_alpha_polar.png`)
- Comparison baseline: `tmp/eval/out_crops/results.json` (PaddleOCR-VL on the same crops, 1727 MiB weights, 2.4–4.0 s/crop)

**Verified directly against APIs today**
- GitHub contents API: `Green-Wood/{CoMER,BTTR}`, `qingzhenduyu/{TAMER,ICAL}`, `SJTU-DeepVisionLab/PosFormer`
- HuggingFace API: `microsoft/trocr-{small,base,large}-handwritten`, `alephpi/FormulaNet`,
  `PaddlePaddle/PP-OCRv{5,6}_*`, `wanderkid/unimernet_base`, `Teklia/pylaia-iam` (`syms.txt`)
- Zenodo API: record 13788177 (McCATMuS) + its `metadata.json`
- `raw.githubusercontent.com/mindee/doctr/main/doctr/datasets/vocabs.py`
- PyPI JSON API: `kraken` 7.1.1, `calamari-ocr` 2.3.1, `python-doctr` 1.1.0, `rapidocr` 3.9.2,
  `paddleocr` 3.7.0, `paddlepaddle-gpu` 2.6.2, `pylaia` 1.1.2, `htrflow` 0.2.6, `surya-ocr` 0.22.1,
  `pix2text` 1.1.7

**Papers**
- TrOCR `2109.10282` · UniMERNet `2404.15254` · CDM metric `2409.03643` · MathWriting `2404.10690`
- PaddleOCR 3.0 `2507.05595` · PP-OCRv6 `2606.13108` · PP-FormulaNet `2503.18382` · PP-DocLayout `2503.17213`
- Texo `2602.17189` · WildHandBench `2608.22959` · OmniHandwritingOCR `2608.18586` · NoTeS-Bank `2504.09249`
- Loghi, ICDAR 2024 Workshops (doi 10.1007/978-3-031-70645-5_6) · CATMuS Medieval, ICDAR 2024

**Repositories and model cards**
- `github.com/mittagessen/kraken` · `zenodo.org/communities/ocr_models` (79 records enumerated)
- `github.com/Calamari-OCR/calamari` · `github.com/jpuigcerver/PyLaia` · `huggingface.co/Teklia/pylaia-iam`
- `github.com/mindee/doctr` (issue #1049 open since 2022-09-07; discussion #1734) · `github.com/knaw-huc/loghi`
- `github.com/DCGM/pero-ocr` · `gitlab.com/scripta/escriptorium` · `github.com/HTR-United/htr-united`
- `github.com/RapidAI/RapidOCR` · `github.com/PaddlePaddle/PaddleOCR` (issue #12046)
- `github.com/datalab-to/surya` · `github.com/breezedeus/Pix2Text` · `github.com/lukas-blecher/LaTeX-OCR`
- `transkribus.org/{pricing,credits,onprem/details}`
- `huggingface.co/microsoft/trocr-base-handwritten/discussions/{5,10,11,20}`

**Not done, deliberately:** no git operations of any kind; no Kraken, Calamari, PyLaia, docTR,
paddlepaddle or Pix2Text installation (dependency conflicts and install cost assessed from published
wheel metadata, marked UNVERIFIED where it is arithmetic rather than measurement); no fine-tuning;
no cloud API calls; nothing written outside `docs/research/handwriting-ocr-systems.md` and the
gitignored `tmp/htr/`.

---

**See:** [`INDEX.md`](INDEX.md) · [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) ·
[`mineru-teardown.md`](mineru-teardown.md) · [`paddleocr-vl-teardown.md`](paddleocr-vl-teardown.md) ·
[`../scope.md`](../scope.md) · [`../findings/corpus-census-2026-09-04.md`](../findings/corpus-census-2026-09-04.md) ·
[`../directives/gpu-discipline.md`](../directives/gpu-discipline.md)
