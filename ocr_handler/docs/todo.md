# TODO — single source of truth

**CURRENT STATE:** M1 complete, 7/7 tests passing, 23 files ready to commit. Two research efforts done. Engine choice deliberately reopened after Unlimited-OCR was measured running here.

Last session: [`archives/session_records/2026-09-02_initialize-and-teardown.md`](archives/session_records/2026-09-02_initialize-and-teardown.md)

**NEXT ACTION:** Rewrite `pdfops.py` on PyMuPDF (replacing poppler subprocess calls) and add structural ink extraction. See [`research/INDEX.md`](research/INDEX.md).

**MODE:** development

---

## Next, in order

1. **`pdfops.py` → PyMuPDF.** Drops three subprocess calls, ~10x faster, and unlocks structural ink extraction. Keep the `PageInfo`/`kind` interface so the tests and router are unchanged.
2. **`ink.py` — add `structural_regions()`.** Extract annotation images by count-difference against the base PDF, with exact page coordinates. Keep colour separation as the no-base fallback; keep region grouping to subdivide into one-expression crops.
3. **`emit.py` + `cli.py`** — M2 as planned.
4. **`recognize.py`** — UniMERNet-Base fp16 behind one swappable interface.

## Reopened by the teardown

**Unlimited-OCR runs on this GPU** at NF4 (4199 MiB peak, 8.5 s/page) and met the success criterion on the fixture page. The earlier "does not fit / wrong shape" verdict was wrong on the first half. [`research/unlimited-ocr.md`](research/unlimited-ocr.md)

**Decide stage 2 by head-to-head** on the fixture page — UniMERNet-Base (681 MiB) vs SmolDocling-256M (960 MiB) vs Unlimited-OCR NF4 (4199 MiB). Do this before writing `recognize.py`.

**Adopt regardless of which wins:**
- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` — worth ~1.1 GiB of peak
- `temperature=0` — deterministic output is what makes regression tests possible
- **Always run the un-annotated twin as a control** — it is what proved ink was being read rather than guessed
- Serialise GPU work; a concurrent 1318 MiB process caused an OOM mid-session

**Switch the renderer to PyMuPDF — it changes answers, not just speed.** poppler at 200 dpi produced `c o s (w o n)`; PyMuPDF at 150/200/300 all produced `\cos(\omega_0 n)`. The renders differ on 6.66% of pixels from antialiasing alone. Supersedes the old "re-test at 300 dpi" item: DPI is free in cost and irrelevant between 150-300 once the renderer is right.

**If Unlimited-OCR is chosen:** `crop_mode` (gundam) is mandatory — `base` drops our red ink to a 0.62 px stroke, and their multi-page/PDF path is forced to base. Put `model.projector` in `llm_int8_skip_modules` or it dies on a dtype mismatch.

## Decided

- **Equation engine: UniMERNet-Base fp16** (Apache-2.0). 681 MiB peak measured on this GPU — 11% of VRAM. `unimernet_tiny` kept as a second opinion; the two fail on different symbols.
- **PDF library: PyMuPDF only.** No pdfplumber/pypdf/pdfminer/Camelot.
- **No OpenCV, no scikit-image.** Benchmarked and beaten by numpy + scipy + Pillow.
- **No single general VLM.** ~38% on handwritten math; the specialist gains +41.79 points.

## Blocked / awaiting operator

- Confirm [`scope.md`](scope.md), especially the Out-of-Scope blacklist.
- Output destination (currently `tmp/`).
- Bootstrap child project vs subfolder.

## Known issues

- `diff_mask` untested against a *recompiled* twin, where the whole page shifts. Guard: check the changed fraction and refuse if implausibly large.
- `merge_px=64` is calibrated for 200 dpi only — a pixel distance, so re-sweep if dpi changes.
- Structural extraction gave 2 ink images on page 5 where pixel grouping gave 5 logical items. Expected; they compose. Do not treat either count as canonical.
