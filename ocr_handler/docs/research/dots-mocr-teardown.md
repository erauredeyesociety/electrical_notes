# dots.mocr — static teardown

**Scope.** Source read of `rednote-hilab/dots.mocr` (clone at `~/tmp/ocr_repos/dots.mocr`,
single squashed commit `23f3e56 update`, 111 MB, weights **not** downloaded), plus the HF
metadata API, the arXiv paper (2603.13032v1), and upstream vLLM/llama.cpp support.

**Nothing was executed.** No weights fetched, no inference, no GPU, no `pip install`. Every
claim below is either a file:line citation, a metadata field, or is marked **UNVERIFIED** with
the experiment that would settle it.

---

## Verdict up front

**At bf16 — the only dtype the repo can load — it does not fit. Not on 4.3 GB free, and not
on a completely idle 6144 MiB card either.**

The weights alone are **5,797 MiB** (3,039,179,264 params × 2 B). The card is 6,144 MiB
total. That leaves 347 MiB for the CUDA context (~300–500 MiB on its own), the vision
encoder's activation peak, and the KV cache. The margin is negative before a single pixel is
processed. The repo ships **no quantization support of any kind** (§1) and the default
transformers path is `device_map="auto"`, which responds to this shortfall by silently moving
half the model to system RAM and running it there (§4).

There is one path that does fit, and it is entirely outside this repo: **llama.cpp**, whose
`mtmd: support dots.ocr` PR (#17575, merged 2026-04-09) covers this exact architecture
*including the vision tower*, and for which community GGUFs exist at 2.4–2.6 GB total. That
route abandons `dots_mocr/parser.py` — the coordinate rescaling, the JSON→Markdown transform,
the malformed-output salvage — and you would reimplement all of it. It also lands in the 4-bit
band this project has already measured a cliff in (`engine-landscape-2026-09.md` §1.7:
Q4_K_M → 45% CER on dense text for a comparable model).

**Recommendation: rule it out.** The two flags from the landscape review both resolve
against it — the handwriting claim is qualitative-only and its predecessor scores 71.7 where
PaddleOCR-VL-1.5 scores 87.4 (§7), and the MIT card *does* carry an acceptable-use rider that
restricts the exact activity this project performs (§8). Combined with a 2× VRAM
disadvantage against every other candidate under review, the 83.9 olmOCR-Bench headline is
not reachable on this hardware.

---

## 0. What the model actually is

`config.json` for **dots.mocr** and for its predecessor **dots.ocr** are **byte-identical**.
Same architecture, same shapes, same `model_type`, same `max_pixels`. dots.mocr is a
retrained dots.ocr, not a redesigned one.

| Field | Value | Source |
| --- | --- | --- |
| `architectures` | `["DotsOCRForCausalLM"]` | `config.json` |
| `model_type` | `dots_ocr` | `config.json` |
| Decoder | 28 layers, hidden 1536, 12 heads, **2 KV heads** (GQA), MLP 8960, vocab 151936, `tie_word_embeddings: false` | `config.json` — this is Qwen2.5-1.5B's shape |
| Vision tower | 42 layers, hidden 1536, MLP 4224, patch 14, `spatial_merge_size` 2, `is_causal: false` | `config.json.vision_config` |
| `torch_dtype` | `bfloat16` | `config.json` |
| `attn_implementation` | `flash_attention_2`, **baked into the vision config** | `config.json.vision_config` |
| Total params | **3,039,179,264**, all BF16 | HF API `safetensors.total` |
| Shards | `model-0000{1,2}-of-00002.safetensors` | HF API siblings |
| Native transformers support | **No** — `auto_map` + `trust_remote_code`, remote code in `modeling_dots_ocr.py` / `modeling_dots_vision.py` | HF API siblings; README:558 *"pending our integration with Transformers"* |

Independent cross-check on the parameter count, from the community GGUF split
(`lodrick-the-lafted/dots.mocr-gguf`): text decoder BF16 = 3,560,414,496 B, vision mmproj
BF16 = 2,526,297,024 B. Sum = **6,086,711,520 B ≈ 6.09 GB**, matching 3.039 B × 2 B =
6,078,358,528 B to within GGUF metadata overhead. The 1.2B-vision / 1.5B-decoder split the
paper advertises is really **~1.26B vision + ~1.78B decoder** (the decoder figure includes
2 × 151936 × 1536 = 467 M params of untied embeddings).

The repo has been moved to a `dots-studio` org; `rednote-hilab/dots.mocr` redirects there
(HF API returns `"id": "dots-studio/dots.mocr"`). Cosmetic, but it will surprise anything
that pins the org string.

---

## 1. Does 3B fit ~4.3 GB free? — No.

### 1.1 dtype: bf16, hardcoded in three places, with no override

```
dots_mocr/parser.py:72        torch_dtype=torch.bfloat16,
demo/demo_hf.py:61            torch_dtype=torch.bfloat16,
README.md:606                 torch_dtype=torch.bfloat16,
```

There is no `--dtype` flag, no fp16 option, no config file. `DotsMOCRParser.__init__`
(`parser.py:23-61`) exposes 14 knobs; dtype is not one of them.

### 1.2 quantization: absent from the repository

```sh
grep -rn -iE "quantiz|bitsandbytes|bnb|gptq|awq|int8|int4|fp8|load_in_" --include=*.py --include=*.md --include=*.sh --include=*.txt .
```

returns **three hits, all of them the `torch.bfloat16` line above**. No
`BitsAndBytesConfig`, no `quantization_config=`, no `max_memory=`, no `offload_folder`, no
`load_in_4bit`. `requirements.txt` does not list `bitsandbytes`, `autoawq`, `optimum`, or
`accelerate`-adjacent quantization extras.

`_load_hf_model` (`parser.py:63-77`) is 15 lines with no injection point. Quantizing means
patching that function.

### 1.3 The arithmetic

| Item | bf16 | Notes |
| --- | ---: | --- |
| Weights | **5,797 MiB** | 3,039,179,264 × 2 B |
| CUDA context + allocator | ~300–500 MiB | vLLM docs put framework overhead at 0.5–2 GB |
| KV cache, A4 @ 200 dpi page (4,931 visual tokens) | 138 MiB | 28 KB/token, see below |
| KV cache, + repo-default 24,000 generated tokens | +658 MiB | `parser.py:111` |
| Vision encoder activation peak, A4 @ 200 dpi | ~0.4–0.8 GB **UNVERIFIED** | see §2.3 |
| **Total** | **≈ 7.3–7.9 GB** | |
| **Card** | **6,144 MiB total / ~4,300 MiB free** | |

KV per token: 28 layers × 2 (K,V) × 2 KV heads × 128 head_dim × 2 B = **28,672 B/token**.
GQA with only 2 KV heads makes the cache genuinely cheap — it is *not* the binding
constraint. The weights are.

The ≈7.9 GB estimate lands on top of the one measured figure this project already has:
`engine-landscape-2026-09.md` records **dots.ocr 3B at 7.9 GB VRAM, 48 s/page** on an RTX
4070 Laptop 8 GB — the slowest entry in that table by 4×. Since the configs are identical
(§0), that measurement transfers directly. It was made on a card with **1.8 GB more VRAM
than this one has in total**, and it was the tightest fit in the comparison.

### 1.4 Quantized routes — all out-of-repo

Six community derivatives exist. None are from rednote-hilab; none carry an OCR eval.

| Repo | Scheme | Weights on disk | Viable on 4.3 GB free? |
| --- | --- | ---: | --- |
| `Durgaram/dots.mocr-4bit` | bitsandbytes NF4, fp16 compute | ~2.0–3.4 GB **UNVERIFIED** | Maybe. Needs patching `parser.py:63-77`. |
| `binedge/dots.mocr-FP8` | FP8 | ~3.0 GB | **Unlikely** — RTX 3060 is Ampere SM 8.6; native FP8 needs SM 8.9+. Would depend on vLLM's fp8-Marlin weight-only path. **UNVERIFIED**. |
| `lodrick-the-lafted/dots.mocr-gguf` | GGUF Q5_K_M + Q8_0 mmproj | 1.29 + 1.34 = **2.63 GB** | **Yes**, with ~1.7 GB headroom |
| `enginil/dots.mocr-IQ4_NL-GGUF` | GGUF IQ4_NL + Q8_0 mmproj | 1.07 + 1.34 = **2.41 GB** | Yes, but 4-bit — see cliff warning |
| `enginil/dots.mocr-gguf`, `anujkosambi/dots.mocr-Q8_0-GGUF` | GGUF | — | — |

The NF4 uncertainty that matters: vision-LM NF4 recipes commonly **exclude the vision
tower**, which here is 1.26 B params. Excluded → 2.53 GB (fp16 tower) + ~0.9 GB (NF4
decoder) = **~3.4 GB**, which on a 4.3 GB budget leaves under 1 GB for context + activations
and is marginal. Included → **~2.0 GB** and comfortable. The card does not say.
*Settled by: reading `quantization_config.llm_int8_skip_modules` in that repo's config.json —
a metadata fetch, no download.*

The GGUF route is the only unambiguous fit, and it is a different program: llama.cpp
`mtmd`, not `dots_mocr/parser.py`. You would reimplement `post_process_cells`
(`layout_utils.py:147-194`), `layoutjson2md` (`format_transformer.py:145-180`), and the
`OutputCleaner` salvage path. And `engine-landscape-2026-09.md` §1.7's own 24-page
quantization ladder — *"below Q5_K_M, quality falls off a cliff"*, 45% CER on dense text at
Q4_K_M — makes `IQ4_NL` a bad default and `Q5_K_M` the floor, costing the headroom back.

---

## 2. Input resolution — 11.29 Mpx is real, and the CLI default does not cap it

### 2.1 The ceiling is model-side, not just client-side

```
dots_mocr/utils/consts.py:1-3   MIN_PIXELS=3136 / MAX_PIXELS=11289600 / IMAGE_FACTOR=28
```

and the same numbers in the model's own `preprocessor_config.json`
(`min_pixels: 3136`, `max_pixels: 11289600`, `patch_size: 14`, `merge_size: 2`). Because it
lives in the preprocessor, this ceiling applies to **both** the transformers path and the
vLLM path regardless of what the client does.

`IMAGE_FACTOR = 28 = patch_size 14 × spatial_merge_size 2` → **one visual token per 28×28
pixels**. So 11,289,600 px = **14,400 visual tokens** for a single page.

### 2.2 What the default path actually sends

This is the part that surprised me. The CLI defaults `--min_pixels`/`--max_pixels` to `None`
(`parser.py:479-485`), which propagates to `self.min_pixels = self.max_pixels = None`
(`parser.py:51-52`), which reaches `fetch_image(image, min_pixels=None, max_pixels=None)`
(`parser.py:179,181`), where the resize branch is:

```
dots_mocr/utils/image_utils.py:124    elif min_pixels or max_pixels:
```

Both `None` → **the branch is skipped and no client-side resize happens at all.**
`smart_resize` is still called at `parser.py:182`, but only to compute `input_height` /
`input_width` for the bbox rescaling — it does not touch the image.

So the actual resolution is set upstream of that, by the PyMuPDF rasteriser:

- **PDF input:** `load_images_from_pdf(dpi=200)` (`parser.py:347`) → `fitz_doc_to_image`
  → `get_matrix` (`doc_utils.py:20-27`). For A4 (595 × 842 pt) the cap does not engage and
  factor = 200/72, giving **1653 × 2339 = 3.87 Mpx ≈ 4,931 visual tokens**. US Letter:
  1700 × 2200 = 3.74 Mpx ≈ 4,770 tokens.
- **Image input:** `fitz_preprocess` is on by default (`parser.py:512`), routing through
  `get_image_by_fitz_doc(target_dpi=200)` (`parser.py:178`) and the same matrix logic.
- Two guards exist: any raster dimension > 4500 px falls back to 72 dpi
  (`doc_utils.py:89-91`), and pages containing an embedded image over 30 Mpx are **skipped
  entirely** (`doc_utils.py:29-69`, `doc_utils.py:113-116`) — note that this `return []`
  aborts the *whole PDF*, not just the page, which is a bug worth knowing about if you ever
  do use this.

A latent unit bug in `get_matrix` (`doc_utils.py:22`): it compares `rect.width * rect.height`
— in **PDF points** — against a **pixel** budget of 11,289,600. The cap therefore only
engages for pages larger than ~46 × 46 inches. Harmless for lecture PDFs; the >4500 px guard
catches the pathological case anyway.

- **Gradio demo:** defaults `max_pixels` to the full `MAX_PIXELS`
  (`demo/demo_gradio.py:36-37`), i.e. the demo pushes 11.29 Mpx by default. If you judge
  this model from the demo you are judging its most expensive configuration.

### 2.3 Is it configurable down? Yes

`--max_pixels` (`parser.py:482-485`) and `--dpi` (`parser.py:462-465`) both work, asserted
against the ceiling at `parser.py:174-175`. Setting `--max_pixels 1000000` re-enables the
resize branch at `image_utils.py:124` and cuts to ~1,275 visual tokens. So resolution is a
real, working lever.

**But it does not rescue the memory question**, because the weights are the binding
constraint, not the activations. Dropping to 1 Mpx saves a few hundred MB of activation and
~110 MB of KV against a **5,797 MiB** weight footprint on a 4,300 MiB budget. You cannot
resolution-tune your way into a 1.5 GB deficit.

**UNVERIFIED — the vision activation peak.** 42 non-causal layers over N = pixels/196
patches (19,740 patches for an A4 page at 200 dpi). Per-layer hidden tensor is
19,740 × 1536 × 2 B = 60.6 MiB, the MLP intermediate 19,740 × 4224 × 2 B = 159 MiB, so the
transient peak is plausibly 0.4–0.8 GB — but that depends on whether the remote code
processes patches in windows, which is in `modeling_dots_vision.py` (not in this repo; it
ships with the weights). *Settled by: fetching that single file from HF — ~30 KB, no weights
— and reading the attention block.*

One hard consequence of the non-causal tower: **flash-attn is not optional at these
resolutions.** An eager 19,740² × 12-head score matrix is 9.3 TB. That is why
`attn_implementation="flash_attention_2"` is hardcoded at `parser.py:71`, `demo_hf.py:60`,
*and* in the model's own `vision_config`. `requirements.txt:11` has flash-attn commented out,
so the shipped install will fail at load unless you build it separately (~20 min compile,
Ampere SM 8.6 is supported).

---

## 3. Model loading cost — no guards whatsoever

This is the question the `gpu-discipline` directive exists because of, so: **the repo does
nothing about any of it.**

```sh
grep -rn -E "set_num_threads|OMP_NUM_THREADS|MKL_NUM_THREADS|PYTORCH_CUDA_ALLOC_CONF|empty_cache|memory_allocated" --include=*.py .
```

→ **zero hits.** No thread cap, no allocator config, no pre-flight VRAM check, no lock, no
cache clearing. The only `os.environ` writes in the whole repo are
`demo_hf.py:2-3` setting `LOCAL_RANK=0` and `inference.py:21` reading `API_KEY`.

The load itself:

```
dots_mocr/parser.py:68-75
    model_path = "./weights/DotsMOCR"
    self.model = AutoModelForCausalLM.from_pretrained(
        model_path,
        attn_implementation="flash_attention_2",
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
```

Four things about this:

1. **`model_path` is hardcoded** and relative. Not a constructor argument, not a CLI flag.
   The weights must live at `./weights/DotsMOCR` relative to cwd, matching
   `tools/download_model.py:12`. Any other location requires editing source.
2. **`trust_remote_code=True`** — `modeling_dots_ocr.py`, `modeling_dots_vision.py` and
   `configuration_dots.py` are executed from the downloaded weight directory. Arbitrary code
   from a third party, run at import.
3. **`device_map="auto"`** — worse than `.to("cuda")` here, for the reason in §4.
4. `from_pretrained` with `device_map` implies `low_cpu_mem_usage=True` in modern
   transformers, so shards are streamed rather than fully materialised in RAM. That mitigates
   the peak-RSS half of the 2026-09-05 failure, but **not** the CPU-saturation half: dtype
   conversion and tensor materialisation still run on the CPU with `torch.get_num_threads()`
   threads, uncapped, exactly as the directive describes. Nothing in this repo calls
   `cap_cpu_threads()`'s equivalent.

Relevant second-order load: `parser.py:370` spawns `ThreadPool(num_thread)` with
`num_thread` defaulting to **64** in the class (`parser.py:31`) and 16 on the CLI
(`parser.py:471`). For the HF path this is correctly forced to 1 (`parser.py:363-364`), but
for the vLLM path it means up to 64 concurrent page requests at a server that has one GPU.

And: `max_new_tokens=24000` is **hardcoded** at `parser.py:111` (and `demo_hf.py:44`). The
`--max_completion_tokens` flag only reaches the vLLM path (`parser.py:133`). On the
transformers path you cannot lower the generation budget — 24,000 decode steps, 658 MiB of
KV growth — without editing the file.

---

## 4. Silent CPU fallback — **yes, present, and quiet**

`device_map="auto"` (`parser.py:73`, `demo_hf.py:62`) hands placement to `accelerate`. When
5,797 MiB of weights meet ~4,300 MiB of free VRAM, `infer_auto_device_map` fills the GPU,
then assigns the remaining layers to `"cpu"`. **That placement is silent** — no warning, no
exception. (Only *disk* offload raises, and only because it demands an `offload_folder`.)

The line that would normally catch it does not:

```
dots_mocr/parser.py:108    inputs = inputs.to("cuda")
```

This still succeeds — the *inputs* go to CUDA fine. Accelerate's `AlignDevicesHook` then
moves each CPU-resident module's weights onto the GPU and back **per forward call**, i.e.
per decode step, up to 24,000 times. The output is correct. The run is one to two orders of
magnitude slower and pins every core for the duration.

There is no `max_memory=` to bound it, no post-load assertion that
`model.hf_device_map` is GPU-only, and nothing prints the device map.

**This is disqualifying on its own terms.** The 2026-09-05 incident involved a script that
was written correctly with `.to("cuda")` and still took the desktop down. `device_map="auto"`
is the version of that script that *never even OOMs to tell you something is wrong* — it
just quietly becomes a CPU job. On this hardware, with 5,797 MiB of weights, that is not an
edge case; it is the guaranteed outcome of running `demo/demo_hf.py` as shipped.

Minor related defect: `--use_hf` is declared `type=bool` (`parser.py:487`). argparse applies
`bool()` to the string, so `--use_hf false` evaluates to `True`. Only omitting the flag
yields `False`.

---

## 5. vLLM — not required, but it is the blessed path, and it is fatal here

**Not required.** `dots_mocr/model/inference.py` is a 49-line OpenAI HTTP client with no
vLLM import; the transformers path is real and reachable via `--use_hf`
(`parser.py:36,55-56,187-188`). `vllm` does not appear in `requirements.txt`. So on paper
there is a plain-transformers escape.

**But it is second-class.** README:563 — *"We highly recommend using vLLM"*; README:700 —
*"transformers is slower than vllm"*; README:548 offers the vLLM Docker image as the fix for
install trouble. The measured penalty in `engine-landscape-2026-09.md`'s comparison table is
brutal for this family of models: PaddleOCR-VL goes **273 s → 3.6 s/page** purely by
switching transformers → vLLM. The transformers path exists; it is not the path the 83.9
score was produced on.

**`gpu_memory_utilization`: handled nowhere in Python, and the shipped value is 0.9.**

```
demo/launch_model_vllm.sh:1  CUDA_VISIBLE_DEVICES=0 nohup vllm serve dots.mocr --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --chat-template-content-format string --served-model-name ${model_name} --trust-remote-code
README.md:568                (same, with --gpu-memory-utilization 0.9)
```

`grep -rn gpu_memory_utilization --include=*.py` → **zero hits.** It is a server flag only;
`inference.py` has no memory awareness at all.

On this card, `0.9 × 6144 MiB = 5,530 MiB` budget against **5,797 MiB** of weights. vLLM
fails during weight loading, before it ever reaches KV-cache allocation. Raising it to 1.0
gives 6,144 MiB against 5,797 MiB of weights plus a ~400 MiB CUDA context — still short, and
with a zero-byte KV pool it would refuse to start regardless. **The shipped vLLM command is
a guaranteed OOM on 6 GB, and no amount of `gpu_memory_utilization` tuning fixes it,**
because the deficit is in the weights.

Support status, for the record: dots.ocr was integrated in-tree in vLLM (PR #24645,
improved by #25466), and the README claims verified performance since v0.11.0. Since
dots.mocr shares `model_type: dots_ocr` and `DotsOCRForCausalLM`, the in-tree module should
load it — **UNVERIFIED**; note that dots.ocr's HF repo ships a `modeling_dots_ocr_vllm.py`
shim and **dots.mocr's does not**, so it depends entirely on the in-tree path being current.
*Settled by: `vllm serve` on any machine with ≥16 GB — not this one.*

---

## 6. Output format — JSON with pixel-space boxes, and native Markdown. This part is good.

**Not DocTags.** The granite-docling problem does not apply here.

`prompt_layout_all_en` (`prompts.py:3-20`) asks for **a single JSON object**, a list of
elements each carrying:

- `bbox`: `[x1, y1, x2, y2]`
- `category`: one of `Caption, Footnote, Formula, List-item, Page-footer, Page-header,
  Picture, Section-header, Table, Text, Title` (`prompts.py:7`)
- `text`, formatted per category (`prompts.py:10-13`):
  - **Formula → LaTeX**
  - **Table → HTML**
  - **Picture → text omitted** (bbox only)
  - everything else → **Markdown**
- sorted in human reading order (`prompts.py:17`)

**Coordinate space.** The model emits boxes in the `smart_resize`d input space;
`post_process_cells` (`layout_utils.py:147-194`) divides by `input/original` scale factors
and returns boxes in **original image pixel coordinates**. That is the space the saved
`.json` is in — directly usable, no further transform.

**Markdown.** `layoutjson2md` (`format_transformer.py:145-180`) is a plain concatenation with
per-category handling: formulas go through `get_formula_in_markdown`
(`format_transformer.py:69-119`), which normalises `\[...\]` and bare LaTeX into `$$...$$`
blocks. Two files are written: `<name>.md` and `<name>_nohf.md` with page headers/footers
stripped (`parser.py:245-252`).

**Figures.** `Picture` cells give you a bbox and no text — which is what this project wants.
Beware `format_transformer.py:169-172`: `layoutjson2md` crops each Picture and inlines it as
a **base64 data-URI** directly in the Markdown. For a figure-heavy lecture PDF that produces
enormous `.md` files. Use the JSON bboxes and crop from the source yourself.

**Other modes**, all in `prompts.py`: `prompt_layout_only_en` (boxes, no text),
`prompt_ocr` (plain text, no boxes), `prompt_grounding_ocr` (text within a supplied box —
note the box must be pre-transformed into input space by `pre_process_bboxes`,
`layout_utils.py:116-145`), `prompt_scene_spotting` (4-point polygons as
`(x1,y1),(x2,y2),(x3,y3),(x4,y4) text`, parsed by regex at `layout_utils.py:233-251`),
`prompt_image_to_svg`, `prompt_general`.

**Failure handling is honest, and you must check for it.** If the model's JSON does not
parse, `post_process_output` (`layout_utils.py:203-229`) catches it, runs the 622-line
`OutputCleaner` regex salvage, and returns `filtered=True`. `parser.py:206-226` then writes
**the raw response string** into the `.json` file instead of a cell list, and sets
`'filtered': True` in the result record. Any consumer must branch on that flag or it will
try to iterate a string. README's own Limitations section concedes *"parsing failures … may
still occur occasionally."*

Undeclared dependency, since it would bite immediately: `layout_utils.py:279` does
`import cv2`, and **opencv is not in `requirements.txt`**. `prompt_scene_spotting`
visualisation crashes on a clean install. (Also note ADR 0002 in this project: numpy/scipy/
Pillow, *not* opencv.)

---

## 7. Handwriting — the flag is confirmed. There is no number, anywhere.

```sh
grep -rn -i -E "handwrit|cursive|scrawl" --include=*.py --include=*.md .
```

over the clone returns **zero**. The two phrases the marketing rests on are:

```
README.md:23                Designed for comprehensive parsing, dots.mocr seamlessly recognizes
                            both diverse human scripts and structured graphical content.
demo/demo_gradio.py:710     <em>Recognize Any Human Scripts and Symbols</em>
```

**"Human scripts" means writing *systems*, not handwriting.** The showcase gallery settles
it — `assets/showcase/result/` contains `Tibetan.png`, `kannada.png`, `russian.png`,
`tradition_zh.png`, `nl.png`. Multilingual, every one. **There is no handwriting sample in
the repository.**

The HF model card contains no mention of handwriting. The arXiv abstract contains no mention
of handwriting. The paper body mentions it exactly twice, both purely qualitative:

> §4.1 — *"The model identifies and partitions structural elements such as titles,
> paragraphs, multi-column regions, dense tables, mathematical formulas, scanned text, and
> **handwritten content**, demonstrating robust document-level structural understanding…"*
>
> Appendix A.2 — *"…handling multilingual pages, complex multi-column layouts, dense tables,
> mathematical formulas, scanned materials, and **handwritten notes**."*

**No table, no metric, no benchmark subset.** olmOCR-Bench — the benchmark carrying the 83.9
headline — has no handwriting category; its eight subsets are ArXiv, Old-scans-math, Tables,
Old-scans, Headers&footers, Multi-column, Long-tiny-text, Base. `Old scans` (48.2, the
model's *weakest* subset by 33 points) is degraded print, not handwriting.

**The one quantitative datum for this family is third-party and unfavourable.** From GLM-OCR's
Table 5, already recorded in `engine-landscape-2026-09.md` §1.6:

| Model on handwritten text | Score |
| --- | ---: |
| PaddleOCR-VL-1.5 | **87.4** |
| DeepSeek-OCR2 | 73.8 |
| **dots.ocr** | **71.7** |
| MinerU2.5 | 54.2 |

dots.mocr is architecturally identical to dots.ocr (§0) and retrained, so 71.7 is a floor,
not a ceiling — the retrain may well have improved it. **But it was not measured, and
rednote chose not to measure it while publishing eleven other benchmark tables.** On a
project whose corpus is handwritten lecture notes, adopting a 3B model on the strength of a
printed-document Elo score, against a 0.9B model with a published 87.4, is the exact error
§2(a) of the landscape review warns against.

---

## 8. Licence — MIT card, plus a rider that restricts this project's activity

**The predecessor's pattern repeats. It is not cleanly MIT.**

Both the GitHub clone and the HF repo carry two files:

- `LICENSE` — verbatim MIT, "Copyright (c) 2025 rednote-hilab"
- `dots.mocr LICENSE AGREEMENT` — 10 sections, effective 2025-08-08, copyright holder
  **Xingyin Information Technology (Shanghai) Co., Ltd**

The HF API `siblings` list for **both** `dots.mocr` and `dots.mocr-svg` includes
`"dots.mocr LICENSE AGREEMENT"` while `cardData.license` reads `mit`. So the HF licence
badge understates the terms in exactly the way the landscape review flagged.

§1.6 of the Agreement subordinates itself to MIT on conflict — *"the terms of the MIT License
shall prevail"* — but adds that where MIT is *"ambiguous or silent"*, the Agreement
*"shall apply and supplement"*. MIT is silent on essentially everything below, so in practice
the Agreement governs.

Clauses that touch this project directly:

- **§3.3(c) Copyright Restrictions** — *"Licensees shall not use the tool for unauthorized
  digitization of publications/document scanning or bulk scraping of content. Any use
  involving publications or other copyright-protected materials must first obtain relevant
  permissions."* Lecture slides and course PDFs are copyright-protected materials owned by
  the instructor or publisher. Read literally, batch-OCRing them requires prior permission.
- **§3.3(b) Privacy** — bars extracting personal data or protected characteristics without
  authorisation. Names on assignment headers are arguably in scope.
- **§5.2(a)** — bars processing sensitive personal data under GDPR/HIPAA absent consent and
  *"adequate anonymization, pseudonymization, or other privacy-enhancing technologies."*
- **§5.4 Further Training** — user input or outputs may only be used to train or fine-tune
  other models with *"specific and informed consent of data subjects."*
- **§7.1** — redistributing requires shipping a copy of the Agreement.
- **§7.3** — modified or fine-tuned weights must display *"Built with dots.mocr."*
- **§8** — governed by PRC law; disputes to the **Hangzhou Arbitration Commission**.
- **§9** — the Licensor may revise the Agreement, and rights **terminate automatically** if
  you do not migrate within 90 days.
- **§3.3 preamble** — any breach *"will result in the automatic termination of all licenses."*

**For a private, local, personal-coursework tool the practical risk is low.** But this is
not the "clean MIT" the HF badge suggests, and §9's unilateral-revision-plus-auto-termination
is a term MIT does not contain and cannot be said to be "silent" in a way that favours the
licensee. Compare PaddleOCR-VL (Apache-2.0, no rider) and GLM-OCR (MIT, no rider).

---

## 9. `dots.mocr-svg` — separate weights, same architecture, same footprint

Not shared weights: `dots.mocr-svg` is its own 2-shard checkpoint with an **identical
parameter count** (3,039,179,264 BF16) and identical file layout — a separately fine-tuned
copy of the same base, so running both means 12 GB of weights, not 6. Irrelevant to this
project (image→SVG for charts and UI layouts), and the README concedes the base model needed
it because *"due to the capacity constraints of a 3B-parameter VLM, dots.mocr may not excel
in all tasks yet like svg."*

---

## 10. Verdict

**Can this run on a 6 GB card at all?**

| Path | Weights | Fits 4.3 GB free? | Fits 6144 MiB total? |
| --- | ---: | --- | --- |
| **transformers, as shipped (bf16)** | 5,797 MiB | **No** — 1.5 GB short before activations | **No** — 347 MiB left for context + KV + activations |
| **vLLM, as shipped (`--gpu-memory-utilization 0.9`)** | 5,797 MiB vs 5,530 MiB budget | **No** — OOM during weight load | **No** |
| bitsandbytes NF4 (out-of-repo, needs source patch) | ~2.0–3.4 GB **UNVERIFIED** | Marginal to plausible | Yes |
| **llama.cpp GGUF Q5_K_M + Q8_0 mmproj** (out-of-repo, abandons the repo's pipeline) | 2.63 GB | **Yes**, ~1.7 GB headroom | Yes |
| GGUF IQ4_NL | 2.41 GB | Yes, but in the measured 4-bit quality-cliff band | Yes |
| FP8 | ~3.0 GB | Ampere SM 8.6 has no native FP8 — **UNVERIFIED** | — |

**As distributed: no.** Every code path in this repository loads bf16 and every one of them
exceeds the card. The repo contains no quantization, no dtype option, no memory guard, no
VRAM pre-flight, and no thread cap; its default `device_map="auto"` responds to the shortfall
by silently relocating the model to system RAM and running it there — the failure mode this
project wrote `docs/directives/gpu-discipline.md` about, in its quietest possible form.

**Via llama.cpp: technically yes, and it is still the wrong choice.** That route costs a
full reimplementation of the parsing pipeline, lands in a quantization band this project has
already measured a 45%-CER cliff in, and buys a model whose only handwriting evidence is a
third-party 71.7 against PaddleOCR-VL-1.5's 87.4 — while consuming 2.4–2.6 GB where a 0.9B
alternative fits comfortably at bf16 and scores higher on the dimension that actually matters
here.

**Rule it out.** The olmOCR-Bench 83.9 and OmniDocBench TextEdit 0.031 are genuine and
class-leading, but they are printed-document scores, they were produced on hardware with 4×
this VRAM, and they are unreachable on a 6 GB card in any configuration that preserves them.
The 3B parameter count that makes those scores possible is precisely what makes the model
unusable here. Both landscape-review flags resolve against it: handwriting is unsubstantiated
by any number, and the MIT badge conceals an acceptable-use rider covering document
digitisation.

---

## Open items (would need execution — deliberately not run)

| # | Question | Cheapest experiment |
| --- | --- | --- |
| 1 | Does `Durgaram/dots.mocr-4bit` quantize the vision tower or skip it? | Fetch that repo's `config.json` and read `quantization_config.llm_int8_skip_modules`. Metadata only, ~2 KB. |
| 2 | Vision-encoder activation peak at 3.87 Mpx | Fetch `modeling_dots_vision.py` from HF (~30 KB, no weights) and read the attention block for windowing. Static. |
| 3 | Does vLLM's in-tree `dots_ocr` module load dots.mocr (no `modeling_dots_ocr_vllm.py` shim)? | `vllm serve` on a ≥16 GB machine. **Not this one.** |
| 4 | Does the llama.cpp GGUF route reproduce layout JSON at all, and at what CER? | `llama-server` with mmproj on a 6 GB card. Feasible here **under `tools/gpu_lock.py`**, but only worth doing if §10's verdict is being contested. |
| 5 | Is FP8 usable on Ampere SM 8.6 via vLLM's fp8-Marlin path for this arch? | vLLM startup log on a 3060. Low value given #10. |

---

## Sources

- Clone: `~/tmp/ocr_repos/dots.mocr` @ `23f3e56` — all file:line citations above
- [rednote-hilab/dots.mocr](https://huggingface.co/rednote-hilab/dots.mocr) — card, `config.json`, `preprocessor_config.json`, HF metadata API (`safetensors.total`, `siblings`)
- [rednote-hilab/dots.ocr `config.json`](https://huggingface.co/rednote-hilab/dots.ocr/raw/main/config.json) — byte-identical comparison
- [arXiv 2603.13032v1](https://arxiv.org/abs/2603.13032v1) — abstract and §4.1 / Appendix A.2 handwriting mentions
- [llama.cpp PR #17575 — "mtmd: support dots.ocr"](https://github.com/ggml-org/llama.cpp/pull/17575) — merged 2026-04-09, includes vision encoder
- [vLLM PR #24645 — "[Model] Support Dots OCR"](https://github.com/vllm-project/vllm/pull/24645), [PR #25466](https://github.com/vllm-project/vllm/pull/25466)
- [lodrick-the-lafted/dots.mocr-gguf](https://huggingface.co/lodrick-the-lafted/dots.mocr-gguf), [enginil/dots.mocr-IQ4_NL-GGUF](https://huggingface.co/enginil/dots.mocr-IQ4_NL-GGUF), [Durgaram/dots.mocr-4bit](https://huggingface.co/Durgaram/dots.mocr-4bit) — quantized derivative file manifests
- Internal: `docs/research/engine-landscape-2026-09.md` §1.6, §1.7, §2(a) · `docs/directives/gpu-discipline.md` · `docs/decisions/0002-numpy-scipy-pillow-not-opencv.md`
