# Engine backends — one interface, many engines, and none of them chosen yet

> **Type: ACTIVE-SPEC. Not built.** Living document, named by concept per
> [../directives/roadmap-and-plans.md](../directives/roadmap-and-plans.md).
> Answers the operator's question — *"there might be multiple OCR methods perhaps you want a module
> for each or something?"* — as a **design**, so the next session implements it without re-deciding.
>
> **Constrained by [ADR-0004](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md)
> and its 2026-09-06 addendum.** That ADR mandates *"`recognize.py` behind one swappable interface,
> so the loser is cheap to replace"* and forbids naming a model until the head-to-head runs. This
> plan is the shape of that interface. **It names no model, sets no default, and ships no backend.**
>
> Serves the protocol in
> [../research/stage2-slate-and-head-to-head-2026-09-06.md](../research/stage2-slate-and-head-to-head-2026-09-06.md).
> Nothing under `src/` or `tests/` was modified writing it; the two source files below were read only.

---

## 1 · The answer, in one paragraph

**Yes — a module per engine, but they are not peers of `recognize.py`; they are behind it.**
`recognize.py` stays the single façade every caller talks to, and its public signature does not
change when a backend appears. Each engine is one file under `src/ocr_handler/engines/`, declaring
as *data* what it needs — weights, free VRAM, dtype, attention implementation, compute capability,
packages — so the host can be checked **before** anything loads. Selection is a table lookup on a
default that is currently `None` for every problem kind, because ADR-0004 has not chosen one. There
are no parallel entry points and there is no `--engine` flag.

**What this buys, concretely:** the loser of the head-to-head is deleted by removing one file and
one table row; the winner arrives as one file and one table row; `cli.py` never changes; and the
sm_75 trap in the addendum — *"each must be loaded with an explicit `float16`, or torch honours the
config and runs an emulated path"* — becomes a **declared field with a contract test** instead of a
line in a research document that somebody has to remember.

---

## 2 · What must not break

Today's honest failure is the thing this design most easily destroys, so it is stated as a
constraint before anything else. From [`recognize.py`](../../src/ocr_handler/recognize.py)'s own
docstring and [text-layer-first.md § 7](./text-layer-first.md):

1. **`available()` is `False` and `recognize()` raises `EngineUnavailable`** while no engine is
   chosen, and the message names ADR-0004 by path.
2. **Never an empty string.** `--mode ocr` returning `""` is indistinguishable from a blank page.
   This is the founding rule of § 7's three-case split and it holds *after* a backend ships, not
   just before — a loaded model that returns nothing is a defect report, not a blank page.
   [../research/glm-ocr-teardown.md](../research/glm-ocr-teardown.md) is the standing example: *an
   OOM turns a page into zero regions while reporting success.*
3. **`pdfops`, `ink`, `crops`, `textlayer`, `emit`, `structure`, `validity`, `latex_repair` keep
   working with no GPU, no torch, and no `engines/` import** — [../directives/code-discipline.md](../directives/code-discipline.md)'s
   *"`pdfops` and `ink` must keep working with no GPU."* `torch` is not in `pyproject.toml` today
   and this design does not put it there.
4. **~300 lines per module**, so one file holding five engines was never an option — which is the
   structural half of the operator's question, independent of ADR-0004.

---

## 3 · The interface `recognize.py` exposes

The façade. Everything public today survives; three things are added.

```python
# ---- errors -------------------------------------------------------------
class RecognitionError(RuntimeError):        # the base a caller catches
class EngineUnavailable(RecognitionError):   # pre-flight: nothing to run, or a requirement unmet
class EngineFailed(RecognitionError):        # ran and blew up; __cause__ carries the original
class EmptyReading(RecognitionError):        # ran, returned nothing printable

UNAVAILABLE: str                             # unchanged, byte for byte

# ---- discovery ----------------------------------------------------------
def engines() -> tuple[str, ...]             # registered names, stable order. () today
def available(kind: str = "math-crop", *, engine: str | None = None) -> bool
def describe(name: str) -> Requirement       # what it needs, without importing it
def preflight(name: str) -> Preflight        # what this host can actually give it

# ---- recognition --------------------------------------------------------
def read_image(image, *, engine=None, kind="math-crop") -> str
def recognize(pdf: Path, page: int, *, dpi: int = 200, engine: str | None = None) -> str
```

### 3.1 The signature that does not change

`recognize(pdf, page, *, dpi=200, engine=None) -> str` is preserved exactly as shipped, including
the `engine` keyword, which is **already in the stub**. That keyword is a *library* parameter, not a
CLI flag, and ADR-0004's prohibition is on the flag (*"naming a model in the CLI would bake in the
choice"*). Keeping it means the head-to-head harness can drive a named arm without any new surface
existing anywhere.

### 3.2 `read_image` is the atom, `recognize` is built on it

[`crops.prepare()`](../../src/ocr_handler/crops.py) already returns `Crop.raw` and `Crop.composite`
— the `raw` / `inkmask` / `flatten` renderings the protocol's § 4.3 needs — as PIL images. The
protocol feeds **crops**, the CLI feeds **pages**. One atom serves both:

- `read_image(img)` — a `PIL.Image` in, LaTeX or text out. This is what a backend implements.
- `recognize(pdf, page, dpi=200)` — renders the page via `pdfops.render` and calls `read_image`
  with `kind="page-any"`. It is the only place in the package that turns a PDF into pixels for a
  model, and `dpi=200` keeps its swept justification unchanged.

`read_image` takes no sampling parameters. **Determinism is a property of the interface, not of the
call site** — ADR-0004's *"`temperature=0` — determinism is what makes a regression test possible"*
is a backend obligation (§ 4.4), not a kwarg a caller can get wrong.

### 3.3 The empty guard, and why it is in the façade

```
text = backend.read_image(img)
if not text.strip():                 # whitespace and control characters only == empty
    raise EmptyReading(engine=..., crop=(w, h))
return text
```

**In the façade, not in each backend**, because a rule enforced in five places is enforced in four.
`EmptyReading` carries the engine name and the crop size so the caller can write
text-layer-first § 7's **case 2** record — `{"chars": 0, "error": null}` plus the loud
`⚠ N pages: OCR returned empty` line — without guessing. That is the reconciliation between "never
return an empty string" and "§ 7 case 2 must be *recorded*, not fatal": the **function** raises, the
**document pipeline** catches and records. A raise cannot be mistaken for a blank page; a `""`
return can.

`recognize()` returns the model's text **unrepaired and unscreened**. It does not call
`latex_repair.repair()` and it does not call `validity.classify()`. Silently repairing extracted
text is a permanent blacklist row in [../scope.md](../scope.md), and
[latex-repair-and-validity.md](./latex-repair-and-validity.md) is explicit that the validity gate is
*a screen, not a score*. The caller builds `validity.Reading(text=..., crop=(w, h))` itself. The
dependency arrow is one-way: `recognize` never imports `validity`.

### 3.4 The exact contract a backend must satisfy

A backend is **a module**, not a class hierarchy. It exposes exactly three names:

| Name | Type | Rule |
| --- | --- | --- |
| `NAME` | `str` | Matches the filename stem and the registry key. Lowercase, hyphenated. |
| `REQUIRES` | `Requirement` | Frozen dataclass, § 4. **Pure data, readable without importing torch.** |
| `open()` | `() -> Engine` | Loads weights and returns the live object. Called inside the lock. |

and the object `open()` returns satisfies:

```python
class Engine(Protocol):
    def read_image(self, image: Image.Image) -> str: ...
    def close(self) -> None: ...
```

Five obligations, each with the evidence behind it:

1. **Top-level imports are stdlib + `engines.base` only.** `import torch` goes *inside* `open()`.
   Without this rule, reading `REQUIRES` to decide whether a backend can run would require importing
   the thing you are deciding about — and `cli.py` imports `recognize` unconditionally, so
   `ocr-handler inspect` on a box with no torch would die. Testable by AST; see § 8.
2. **`read_image` returns text or raises.** Framework errors are translated to `EngineFailed` with
   `__cause__` set — a `torch.cuda.OutOfMemoryError` must never surface as a short string. The
   façade cannot do this translation because it cannot import torch.
3. **Greedy decoding, no sampling.** ADR-0004.
4. **Honour `REQUIRES.dtype` explicitly at load.** Never `dtype="auto"`, never the config default.
   § 5 is why.
5. **Do not acquire the GPU lock.** The façade holds it (§ 4.5) so a backend cannot forget it.

---

## 4 · The registry and the layout

```
src/ocr_handler/
  recognize.py            façade: errors, discovery, the empty guard, selection   (~170 lines)
  gpulock.py              MOVED from tools/gpu_lock.py, re-exported there         (~140 lines)
  engines/
    __init__.py           the table, DEFAULTS, lazy load(), session()             (~90 lines)
    base.py               Requirement · Host · probe() · check() · Engine         (~160 lines)
    <name>.py             one backend. NONE SHIP TODAY                            (<300 each)
```

Every file is inside the ~300-line cap with room, which was the structural argument for splitting in
the first place. `engines/` is the first subpackage under `src/ocr_handler/` — see § 9, Q1.

### 4.1 Registration is an explicit table, not discovery

```python
# engines/__init__.py
_TABLE: dict[str, str] = {}          # name -> module in this package. EMPTY until ADR-0004 closes.

DEFAULTS: dict[str, str | None] = {  # problem kind -> engine name
    "math-crop": None,               # handwritten mathematics — the ADR-0004 question
    "page-prose": None,              # scanned prose — NOT an ADR-0004 question, see § 9 Q2
    "page-any":   None,              # a whole page, any content
}
```

**No entry-point scanning, no directory globbing, no plugin protocol.** Three reasons, and the third
is the one that matters: ordering stays deterministic so `engines()` and any report built from it are
stable; nothing is imported as a side effect of installing something; and an engine cannot become
the default by being the only one that happened to import successfully. *That last failure mode is
ADR-0004's exact prohibition arriving through the back door* — a choice made by install order rather
than by measurement.

`load(name)` does `importlib.import_module(f".{_TABLE[name]}", __package__)`. Lazy, so the table can
list a backend whose dependencies are absent and `engines()` still answers.

### 4.2 Selection — and the refusal that protects the ADR

```
engine given explicitly ─────────────────────────► use it (library callers, the h2h harness)
engine is None ──► DEFAULTS[kind] is a name ─────► use it
              └──► DEFAULTS[kind] is None ──┬── table empty ──► EngineUnavailable(UNAVAILABLE)
                                            └── table non-empty ──► EngineUnavailable(
                                                 "N engine(s) are registered but none is the default
                                                  for kind '<kind>' — the head-to-head in ADR-0004
                                                  has not selected one. Name one explicitly.")
```

**There is no "first usable engine" fallback and no fallback between engines, ever.** If the selected
backend is unusable, `recognize` raises; it does not quietly try another. The concrete harm is in the
three-problems verdict: [../research/INDEX.md](../research/INDEX.md) records that the scanned-prose
path works at ~10 s/page on CPU *and that "math does not survive"* it. An automatic fallback from an
unavailable maths engine to a prose engine would return plausible-looking text with the mathematics
silently destroyed — the single worst failure this project can produce, and worse than returning
nothing, which is the thing § 2 already forbids.

### 4.3 What a backend declares

```python
@dataclass(frozen=True)
class Requirement:
    kind: str                       # "math-crop" | "page-prose" | "page-any"
    repo: str                       # HF id or local path — provenance, not a download instruction
    weights_bytes: int              # from the safetensors manifest, so headroom is arithmetic on fact
    dtype: str                      # REQUIRED. No default. "float16" | "float32" | ...
    packages: tuple[str, ...]       # import names, e.g. ("torch", "transformers")
    min_free_mib: int               # peak, load included
    peak_is_measured: bool          # False ==> min_free_mib is arithmetic, and reports must say so
    attn: str | None = None         # "sdpa" | "eager" | "flash_attention_2" | None
    min_compute: tuple[int,int] | None = None      # below this it CANNOT run
    degrades_below: tuple[int,int] | None = None   # below this it RUNS, worse — see § 5
    degradation: str = ""           # required iff degrades_below is set; one line, plain English
    transformers: str | None = None # version specifier, when the backend needs one
    licence: str = "unknown"        # "Apache-2.0" | "unlicensed" | ...
    notes: tuple[str, ...] = ()
```

Four of these fields exist only because a specific thing went wrong or nearly did:

- **`dtype` has no default.** Every model on the slate ships `dtype: bfloat16` in `config.json`, and
  Turing has no bf16 tensor cores. The addendum: *"a one-line change per engine and a silent 2–5× if
  forgotten."* A field with no default cannot be forgotten; a comment can.
- **`peak_is_measured`** separates the two measured numbers in the slate (UniMERNet-Base at
  686 MiB alloc, PaddleOCR-VL at 1767 MiB) from the estimated ones, so no report ever presents
  arithmetic as a measurement. This project has already caught one external source doing exactly
  that, and one internal one (`SAHI-INTEGRATION.md`'s 24 GB).
- **`degrades_below` + `degradation`** are § 5, the whole point.
- **`licence`** because two of the five slate arms live in a repo whose `cardData.license` is
  **null**. A licence never blocks a run — it is an operator call, not a runtime one — but it must be
  visible in `describe()` rather than living only in a research file.

### 4.4 Preflight — three verdicts, not two

```python
@dataclass(frozen=True)
class Preflight:
    engine: str
    verdict: str                 # "usable" | "degraded" | "unusable"
    unmet: tuple[str, ...]       # why it cannot run
    notes: tuple[str, ...]       # why it will run badly, or what could not be checked
    host: Host
```

| Verdict | `available()` | Behaviour |
| --- | --- | --- |
| `usable` | True | runs |
| `degraded` | **True** | runs, **and every note is surfaced to the caller and the report**. Never silent. |
| `unusable` | False | `EngineUnavailable`, naming the specific unmet requirement, not just the ADR |

`degraded` exists because the alternatives are both wrong. Refusing to run on sm_75 makes the tool
useless on the actual deployment target. Running silently is what PaddleX does, and it is precisely
the defect the addendum spent a source audit finding. **Run, and say what you gave up.**

### 4.5 The façade holds the GPU lock

```python
with engines.session(name) as eng:      # gpu_session() when REQUIRES needs a device, else a no-op
    text = eng.read_image(img)
```

ADR-0004's *"serialise GPU work"* and [../directives/gpu-discipline.md](../directives/gpu-discipline.md)
are enforced structurally: a backend never touches the lock, so it cannot forget it, and one engine
is resident at a time — the protocol's § 4.5 rule 1. This requires
[`tools/gpu_lock.py`](../../tools/gpu_lock.py) to be importable from the package, hence the move to
`src/ocr_handler/gpulock.py` with `tools/gpu_lock.py` kept as a thin re-export so both the directive's
documented usage and `python3 tools/gpu_lock.py` as a status command keep working unchanged.

---

## 5 · Hardware declaration — the sm_75 problem, made structural

**The deployment target is the skytracker Quadro RTX 5000: TU104, Turing, compute capability 7.5,
16 GB, shared with other processes.** Confirmed by PCI device ID `10de:1eb0`, not inferred from a
part number (stage2 § 7b).

### 5.1 The two gates that fire, and how a backend says so

PaddleX gates bf16 at `cap >= 80` (`paddle/fluid/pybind/place.cc:492-499`) and PaddleOCR-VL sets
`_supports_sdpa` only at `cap >= (8, 0)` (`paddlex/…/_siglip.py:144-158`). **75 < 80, so both fire**,
and that path silently takes fp32 with eager O(N²) vision attention. The HF torch implementation has
no such gate.

Two hypothetical declarations — hypothetical because **no backend ships** (§ 7):

```python
# a Paddle-path backend WOULD declare:
degrades_below = (8, 0)
degradation    = ("PaddleX gates bf16 and SDPA at compute capability >= 8.0, so on sm_75 this "
                  "runs fp32 with eager O(N^2) vision attention: ~2x weights, ~4x attention "
                  "scratch. Not an error — a price. Verified in place.cc:492-499 and _siglip.py:144-158.")

# an HF-torch-path backend WOULD declare:
min_compute = None                # torch SDPA's memory-efficient backend runs on sm_75
dtype       = "float16"           # NOT the config's bfloat16
attn        = "sdpa"
```

On the target, `preflight()` returns `degraded` for the first with that exact sentence in `notes`.
The difference between this design and the status quo is not that the penalty goes away — it is that
**it is announced instead of discovered**, and announced by a check that costs no GPU and loads no
weights.

### 5.2 Two consistency rules `check()` enforces

- **`attn == "flash_attention_2"` requires `min_compute >= (8, 0)`.** FlashAttention-2's own README
  excludes Turing. A backend declaring FA2 with no capability floor is a bug in the *declaration*,
  caught at import, not an OOM at 3 a.m.
- **`degrades_below` set without `degradation` is a declaration error.** A silent degradation flag
  is worse than none, because it looks like the problem was handled.

### 5.3 `nvidia-smi` is broken on the target, and the design degrades honestly

```
Failed to initialize NVML: Driver/library version mismatch
NVML library version: 580.173   vs   NVRM 580.159.03 (loaded kernel module)
```

Userspace-only: `/dev/nvidia{0,ctl,uvm}` are present and the CUDA path is unaffected — Ollama is
100% GPU-resident on that box. **Not our machine to fix; that is a request to the skytracker
developers.** So the probe must not depend on the broken tool:

```python
@dataclass(frozen=True)
class Host:
    cuda: bool | None
    name: str | None
    capability: tuple[int, int] | None
    total_mib: int | None
    free_mib: int | None
    source: str                  # "torch" | "nvidia-smi" | "procfs" | "none"
    notes: tuple[str, ...]
```

Probe order, cheapest and most reliable first:

| # | Source | Gives | Survives the NVML mismatch? |
| --- | --- | --- | --- |
| 1 | `torch.cuda.get_device_capability()`, `torch.cuda.mem_get_info()`, `get_device_name()` | all four fields | **Expected yes** — these are CUDA driver/runtime calls, not NVML |
| 2 | `nvidia-smi --query-gpu=name,memory.total,memory.free,compute_cap --format=csv` | all four | **No** — this is the broken path |
| 3 | `/proc/driver/nvidia/gpus/*/information` | `name` only | Yes — it is how the card was identified |
| 4 | nothing | every field `None`, `source="none"` | — |

⚠ **Row 1 is reasoned, not measured.** Nothing was executed writing this plan. It is the single
assumption the first implementer must verify on the target, and it is one line:
`python3 -c "import torch; print(torch.cuda.get_device_capability(), torch.cuda.mem_get_info())"`.
If it fails too, the design still works — every field is `None` and § 5.4 takes over — but the
free-VRAM guard cannot be re-armed and that must be said in the result.

**`None` means "not known" and is never coerced to a number.** No defaulting an unknown capability
to 7.5 because the docs say so; no defaulting unknown free VRAM to 16 GB or to 7.9 GB. The GPU is
shared with a YOLO watcher and the skytracker application itself, so free VRAM is not a constant to
look up even when it *can* be read.

### 5.4 What happens when a requirement cannot be checked

| Requirement | Host says | Verdict | Why |
| --- | --- | --- | --- |
| `packages`, `transformers` | — | `unusable` if missing | Deterministic, needs no probe. Hard refusal. |
| `min_compute` | a number below it | `unusable` | It cannot run. |
| `min_compute` | `None` (unknown) | `unusable` | Capability is cheap and reliable *if torch works at all*; failing to read it means torch is not working, so nothing was going to run. |
| `degrades_below` | a number below it | `degraded` + the `degradation` note | § 5.1. This is the sm_75 case. |
| `degrades_below` | `None` | `degraded` + *"compute capability unknown; the sm_75 degradation could not be ruled out"* | Unknown is not "met". |
| `min_free_mib` | below it | `unusable` | Refusing beats OOMing after paying the CPU load cost. |
| `min_free_mib` | `None` (unknown) | `degraded` + *"free VRAM unknown (NVML mismatch on this host); the N MiB requirement was not verified"* | **Proceed.** Refusing here would make the tool unusable on the deployment target in its current state, and the failure mode of proceeding is an OOM, which is loud. Compare a silent wrong answer, which is not. |
| `licence` not clean | — | never blocks | Operator call. Surfaced in `describe()`. |

### 5.5 A guard that is already disarmed on the target

Read while designing this, and worth fixing whatever else happens:
[`tools/gpu_lock.py`](../../tools/gpu_lock.py) pre-flights free VRAM through
`free_vram_mib()`, which shells out to `nvidia-smi` and returns `None` on failure — and
`gpu_session` only refuses when `free is not None and free < MIN_FREE_MIB`. **On the deployment
target the third of gpu-discipline's three guards is therefore a no-op right now**, and the session
banner prints `? MiB free` without saying why.

Two changes, both small, both engine-agnostic, both in the ships-now list:

1. `free_vram_mib()` tries **torch's `mem_get_info` first**, `nvidia-smi` second. That re-arms the
   guard on the target without waiting for the driver fix.
2. When it is still unknown, say so in the banner — *"free VRAM unknown (NVML mismatch?); the
   pre-flight guard is disarmed for this run"* — rather than printing a question mark.

---

## 6 · The three-problems split, and exactly where routing lives

[../research/INDEX.md](../research/INDEX.md)'s verdict: **the corpus is three problems and only one
of them needs a model.**

| Corpus | Tool | Reaches `recognize`? |
| --- | --- | --- |
| Born-digital LaTeX — 2,594 pages | mechanical reconstruction from vector rects, `structure.py` | **No. Never.** |
| Scanned prose — ~400 pages | OCRmyPDF / RapidOCR, CPU, ~10 s/page | only as `kind="page-prose"`, and § 9 Q2 |
| Handwritten mathematics | a model | yes, `kind="math-crop"` |

There are three routing decisions in this project at three altitudes, and **conflating them is how
the ML path would come to own the deterministic one.** They live in three different places:

| # | Decision | Lives in | GPU? |
| --- | --- | --- | --- |
| **R1** | *Does this page need recognition at all?* | `textlayer.py` classification + `cli.extract`'s mode logic — `doc.ocr_candidates`, already built | no |
| **R2** | *Which of the three problems is this page?* | the **classifier**, upstream — text layer present, vector drawings, images, colour ink. **Not `recognize.py`.** | no |
| **R3** | *Which backend reads this image?* | `engines.DEFAULTS[kind]`, one table lookup | n/a until a backend exists |

**R1 and R2 are deterministic, CPU-only, and answered before `recognize` is imported for anything
but its `UNAVAILABLE` string.** R3 is the only decision inside `engines/`, and it is a dictionary
lookup, not an inference.

### 6.1 The invariant that keeps this true, and its test

> **`recognize.py` is the only module in the package that may import `engines/`, and no module
> other than `cli.py` may import `recognize`.**

One AST test in `tests/persistent/` walks every module's imports and asserts it. Today the graph is
already `cli → recognize` and nothing else (verified: `cli.py:39` and
`tests/persistent/test_extract.py:23` are the only references in the repo). The test does not
describe an aspiration; it pins a property that currently holds, which is the only kind of
invariant worth writing.

That single test is what makes objective **O5 — stay runnable with no GPU** checkable rather than
asserted, and it is what stops a future session importing `recognize` into `emit.py` for one
convenient helper and quietly making the 430-document path depend on torch.

### 6.2 `kind` is not decoration

`kind` is why the "no fallback" rule of § 4.2 can be enforced mechanically: `read_image(img,
kind="math-crop")` will not select a backend whose `REQUIRES.kind` is `"page-prose"`, so the
mathematics-destroying substitution cannot happen by configuration accident. It also gives the
addendum's **"if (i) holds and (iii) fails, the answer is 'route', not 'swap'"** outcome a home —
see § 7.3.

---

## 7 · What ships now, and what waits

ADR-0004: *"No `--engine` flag ships until this is closed."* The line this design draws is between
**the shape** and **the choice**. The shape is engine-agnostic and can be built today; anything that
names a model waits.

### 7.1 Ships now — no model named anywhere

- `recognize.py` façade: the four-error hierarchy, `engines()`, `available()`, `describe()`,
  `preflight()`, `read_image()`, `recognize()`, the empty guard, the selection rule **including the
  "registered but no default" refusal**.
- `engines/__init__.py`: **empty** `_TABLE`, `DEFAULTS` all `None`, `load()`, `session()`.
- `engines/base.py`: `Requirement`, `Host`, `probe()`, `check()`, the `Engine` protocol, the two
  consistency rules of § 5.2.
- `gpulock.py` moved into the package; `free_vram_mib()` prefers torch; the disarmed-guard banner.
- Tests (§ 8).

`UNAVAILABLE` keeps its current text so `cli.py`'s message does not move, and `available()` keeps
returning `False` — because the table is empty, not because it is hard-coded. **That is the only
behavioural difference on day one: the same answer, reached by the real mechanism.**

### 7.2 Waits — every one of these names or presupposes a model

- **Any `engines/<name>.py`.** All five arms.
- **`DEFAULTS[...]` being set to a string.** This *is* the ADR-0004 decision; setting it is what
  "closing the head-to-head" means in code.
- **The `--engine` CLI flag.** Forbidden by name. It may never be needed at all — see § 7.3.
- **A `[project.optional-dependencies]` block in `pyproject.toml`.** Its contents are decided by
  which arm wins: `Uni-MuMER-Qwen3-VL-2B` needs `transformers >= 5`, on which
  `handwriting-ocr-systems.md` § 3.2 recorded that TrOCR *breaks* and on which the vendored
  UniMERNet path is unverified. **A dependency pin is a model choice wearing a different hat.**
- **Replacing `cli._refuse_ocr` with a real call.** It is already gated on `available()` in spirit;
  making it so in fact is one branch, added when the first backend lands.

### 7.3 How the first real backend changes no caller

The whole diff:

1. one new file `src/ocr_handler/engines/<winner>.py`;
2. one row in `_TABLE`;
3. one `DEFAULTS["math-crop"] = "<winner>"`;
4. one optional-dependency block in `pyproject.toml`;
5. one branch in `cli.extract` so the OCR modes call instead of refusing.

`recognize.recognize(pdf, page, *, dpi, engine)` is byte-identical before and after. `available()`
flips from `False` to `True` **because the table stopped being empty**, which is what the stub's
docstring already promises: *"When M3 lands, `available()` starts returning True and `recognize()`
starts returning text. No caller changes."*

**And if the head-to-head ends in "route" rather than "swap"** — the addendum's condition (iii),
*"it loses no symbol the incumbent recovered"* — then two backends ship and `DEFAULTS` grows a
sibling: `select(kind, crop) -> str`, one documented function in `engines/__init__.py` keyed on the
stratum or the aspect ratio (UniMERNet's input is 1:3.5 and wastes ~90% of its canvas on a stacked
derivation; PP-FormulaNet's is square). **Still no CLI flag, still no caller change.** The routing
outcome the addendum anticipates is the case this design is *shaped for*, not a case it survives.

### 7.4 Where the head-to-head's five arms live in the meantime

The chicken-and-egg is real: the protocol needs five arms to run, and no arm may ship. The answer is
that **the arms are the harness, not the product.**

```
tools/h2h/arms/<arm>.py        # imports ocr_handler.engines.base, satisfies the Engine protocol
```

Outside `src/`, outside the package, not on the install path, not reachable from the CLI. They
satisfy the § 3.4 contract because that costs nothing and buys everything: **promoting the winner is
a `git mv` plus a table row, not a rewrite.** This is also what makes shipping `base.py` today
load-bearing rather than speculative — the harness is its first consumer, and it consumes it before
any product code does.

---

## 8 · The test floor

Per [../directives/testing-discipline.md](../directives/testing-discipline.md), everything here is
CPU-only and runs on a box with no GPU and no torch.

| Test | Pins |
| --- | --- |
| `available()` is False, `recognize()` raises `EngineUnavailable`, message contains `0004-engine-choice` | § 2.1 — the current test at `tests/persistent/test_extract.py:172` extended by one assertion on the ADR pointer |
| `read_image` raises `EmptyReading`, never returns `""`, for a stub backend returning `""`, `"  "`, `"\n\t"` | § 2.2 |
| Import-graph AST test: only `cli` imports `recognize`; only `recognize` imports `engines` | § 6.1 — the invariant behind O5 |
| Every registered backend's module imports nothing outside stdlib + `engines.base` at top level | § 3.4 rule 1. Vacuously true today, and that is fine — it starts failing the moment it matters |
| Every registered backend declares a `dtype` and it is not `"auto"` | § 4.3, the bf16 trap |
| `check()` on a synthetic `Host(capability=(7,5))` against `degrades_below=(8,0)` → `degraded`, note non-empty | § 5.1, without a GPU |
| `check()` on `Host(free_mib=None)` → `degraded`, not `usable` and not `unusable` | § 5.4, the broken-`nvidia-smi` row |
| `attn="flash_attention_2"` with `min_compute=None` is a declaration error | § 5.2 |
| `probe()` returns all-`None` and `source="none"` without raising, with no GPU and no `nvidia-smi` | § 5.3 |
| Non-empty `_TABLE` with `DEFAULTS[kind] is None` raises, and the message says the head-to-head has not chosen | § 4.2 — this is the ADR guard in executable form |

---

## 9 · The scope cost — two questions for the operator, and one that is not one

### The CLI verb count does not move: **four of five, unchanged.**

[../scope.md](../scope.md) caps the CLI at five verbs and lists four today — `inspect`, `extract`,
`check`, `version`. **This design adds none.** Recognition arrives as behaviour behind
`extract --mode ocr|both|auto`, which already exists and already refuses; `--engine` is a flag, not
a verb, and it does not ship. If the head-to-head ends in "route", it still does not ship (§ 7.3).

Two genuine questions, named rather than answered, per
[../directives/scope-discipline.md](../directives/scope-discipline.md)'s *"uncertain about the
operator's intent → write it into scope.md § Open decisions, don't invent an answer."*

### Q1 — `engines/` is the first subpackage under `src/ocr_handler/`. Confirm?

Everything today is flat modules. [../directives/code-discipline.md](../directives/code-discipline.md)
caps *module size*, not directory depth, so nothing is violated — and the ~300-line cap is precisely
what forces the split, since one file holding five engines is not an option. But a subpackage is a
structural precedent and it is cheap to say no to now and expensive later. **The alternative** is
flat `engine_<name>.py` files with the table in `recognize.py`, which costs one level of nesting and
buys a `recognize.py` that is doing façade *and* registry work — closer to the cap and doing two
jobs. **Recommend the subpackage. Low stakes, but it should be said out loud rather than assumed.**

### Q2 — is a CPU **prose** backend in scope, or out? ⚠ This is the real one.

[../scope.md](../scope.md) § In scope #7 is *"Recognise handwritten **mathematics** into LaTeX"*, and
the blacklist has *"Handwriting recognition for prose"* at tier **yes** (out). But the research
verdict names **scanned prose (~400 ps160 pages) as one of the three problems**, solvable by
OCRmyPDF/RapidOCR on CPU at ~10 s/page — no GPU, no ADR-0004, no model choice, and it would make
`extract --mode ocr` do real work on the corpus that carries most of the value.

**ADR-0004 does not block this.** It defers *the handwritten-maths engine* and nothing else. So the
`page-prose` slot in `DEFAULTS` could be filled long before `math-crop` is.

The question is scope, and it is a real one in both directions: the blacklist row excludes prose
*annotation* on lecture slides (fair — those can stay images), but the ps160 scans are printed prose
that the corpus census counts and that no other path recovers. **Is `page-prose` in?** If yes, it
costs one backend file, two CPU dependencies, zero verbs and zero GPU, and it should get its own row
in scope.md § In scope. If no, `DEFAULTS["page-prose"]` stays `None` permanently and the `kind`
field still earns its place by making the no-fallback rule enforceable.

### Not a question: `--engine`

Recorded so it is not re-litigated. ADR-0004 forbids it now; § 7.3 shows that even the "route"
outcome does not need it; the `engine=` keyword already in `recognize()`'s shipped signature covers
every library and harness caller. **It should never ship.**

---

## 10 · Does this force a change to ADR-0004?

**No.** Checked consequence by consequence, and the ADR is immutable, so this is the place to record
the check rather than the ADR.

| ADR-0004 says | This design |
| --- | --- |
| *"`recognize.py` behind one swappable interface, so the loser is cheap to replace"* | ✅ Exactly this. Losing costs one file and one table row. |
| *"No `--engine` flag ships until this is closed"* | ✅ No flag. The `engine=` **keyword** is in the stub's shipped signature already and is not a CLI surface. |
| *"`PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`"* | ✅ Already set by `cap_cpu_threads()`, which the façade's `session()` runs. |
| *"`temperature=0`"* | ✅ § 3.4 obligation 3 — the interface exposes no sampling parameter, so it cannot be got wrong. |
| *"Always run the un-annotated twin as a control"* | ✅ Protocol-level, unchanged. `read_image` takes an image, so a twin crop is just another call. |
| *"Serialise GPU work"* | ✅ § 4.5 — the façade holds the lock, backends cannot forget it. |
| Addendum: *"measure `max_memory_allocated` around `from_pretrained` separately"* | ✅ `peak_is_measured` carries which numbers came from that and which are arithmetic. |
| Addendum: *"if (i) holds and (iii) fails, the answer is 'route', not 'swap'"* | ✅ § 7.3 — `DEFAULTS` per kind, plus `select()` if it comes to that. No caller change either way. |

**One tension, and it is not an ADR change.** The ADR's *"serialise GPU work"* consequence is
implemented by `gpu_lock`, whose free-VRAM guard is currently a **no-op on the deployment target**
because it depends on the broken `nvidia-smi` (§ 5.5). That is an implementation gap in a
consequence, not a defect in the decision, and § 7.1 fixes it. Worth writing down because it is the
kind of thing that reads as "already handled" for exactly as long as nobody checks.

---

## 11 · Open questions this plan does not answer

1. **Does `torch.cuda.mem_get_info()` actually work on the target with NVML broken?** § 5.3's row 1
   is reasoned from the CUDA-path-is-unaffected evidence, not measured. One line settles it, and
   nothing here was executed.
2. **Q2 above — is `page-prose` in scope?** The only question that changes what gets built.
3. **Does `page-any` earn its place?** It exists because `recognize(pdf, page)` needs a kind, and
   `crops.prepare` is the only thing producing `math-crop` inputs today. If the answer to Q2 is no
   and no page-level engine ever ships, `page-any` is dead weight and should be removed rather than
   kept "in case".
4. **Where does the `Crop.contested` flag surface?** The protocol excludes a contested crop from
   scoring rather than counting it as a model error ([mask-first-crops.md](./mask-first-crops.md)).
   That is a *caller* concern and this plan deliberately leaves it there — but somebody has to own
   it before the head-to-head scores anything.
5. **Does a degraded run get recorded in the JSONL intermediate?** § 4.4 says notes reach the
   caller; [text-layer-first.md § 4](./text-layer-first.md) does not yet have a field for them, and
   ADR-0005 has the intermediate's shape reopened.

---

**Related:** [INDEX.md](./INDEX.md) ·
[../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md) ·
[../research/stage2-slate-and-head-to-head-2026-09-06.md](../research/stage2-slate-and-head-to-head-2026-09-06.md) ·
[../research/INDEX.md](../research/INDEX.md) ·
[./text-layer-first.md](./text-layer-first.md) ·
[./mask-first-crops.md](./mask-first-crops.md) ·
[./latex-repair-and-validity.md](./latex-repair-and-validity.md) ·
[../directives/gpu-discipline.md](../directives/gpu-discipline.md) ·
[../directives/code-discipline.md](../directives/code-discipline.md) ·
[../scope.md](../scope.md) · [../roadmap.md](../roadmap.md)
