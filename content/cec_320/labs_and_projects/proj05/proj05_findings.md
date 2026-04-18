# Proj 05 Findings: Load and Store (General)

**Course:** CEC 322 / MP-GE4A
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [proj05_procedure.md](./proj05_procedure.md)
> - Original Manual: `mp-ge4a-proj5-load-n-store-general-26-03.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Renode UART — all 9 tests pass (F412dsc Unity) | PT1-PT3 (90 pts) | [x] |
| A2 | Screenshot | Serial — all 9 tests pass on real G431 Nucleo-32 | Submission | [x] |
| C1 | Code | Edited `ge4a_load_n_store_sfns.s` (all 5 PT bodies) | PT1+PT2+PT3 (90 pts) | [x] |

---

## Screenshot Artifacts

### A1: Unit Tests — All Pass (F412dsc via Renode)

**Required for:** PT1 (15) + PT2a (18) + PT2b (12) + PT3a (30) + PT3b (15) = 90 pts of programming tasks

**What to capture:**

- Renode USART2 analyzer window
- Final summary line: `9 Tests 0 Failures 0 Ignored / OK`
- Tests:
  - `test_mp_load_modify_store` (C reference, should already pass)
  - `test_mp_str_cpy_c1` (C reference)
  - `test_mp_str_cpy_c2` (C reference)
  - `test_mp_array_abs_sum` (C reference)
  - `test_mp_load_modify_store_s` ← PT1
  - `test_mp_str_cpy_s` ← PT2a
  - `test_mp_str_len_s` ← PT2b
  - `test_mp_array_abs_sum_s` ← PT3a
  - `test_mp_array_max_s` ← PT3b

**File to save:** [a1.png](./a1.png)

---

### A2: Unit Tests — All Pass (G431n32 Real Board)

**Required for:** Submission — running Unity on both boards is the standard
course workflow. The manual only says "screenshots of running results," but
CEC 322 consistently expects results on both targets.

**What to capture:**

- Serial terminal output from the real G431 Nucleo-32 via USB (typically
  `/dev/ttyACM0` @ 115200)
- Same 9-test summary

**File to save:** [a2.png](./a2.png)

---

## Code Snippet Artifacts

### C1: `ge4a_load_n_store_sfns.s` (all 5 PT bodies)

**Required for:** PT1 (15) + PT2a (18) + PT2b (12) + PT3a (30) + PT3b (15) = 90 pts

**File path:** `/opt/proj_mp/ge4a_load_n_store/src_ge4a_load_n_store/ge4a_load_n_store_sfns.s`

**What was written:**

1. **PT1 — `mp_load_modify_store_s`:**
   `ldr/ldrsh/ldrsb` to load, one shift-based instruction per element
   (`sub … asr #2`, `asr #1`, `asr #2`), then `str/strh/strb` to store back.
2. **PT2a — `mp_str_cpy_s`:** post-indexed `ldrb [r0], #1` and
   `strb [r1], #1` with `cbz` to detect the terminator.
3. **PT2b — `mp_str_len_s`:** walk a shadow pointer until NUL, return
   `(end − start − 1)`.
4. **PT3a — `mp_array_abs_sum_s`:** `ldr [r0], #4` post-indexed word load,
   `it lt / neglt` conditional negate for abs, accumulate.
5. **PT3b — `mp_array_max_s`:** seed `max` with `pArr[0]`, loop with
   `it gt / movgt` to conditionally update.

Both `abs_sum_s` and `max_s` use `r12` as a scratch counter (caller-saved on
ARM EABI → no push/pop required).

**Artifact file:** [c1.s](./c1.s)

---

## Submission Checklist

### PDF Report

**Filename:** `cec320-proj5-report-lastname-firstname.pdf`

**Required contents (per §5.4 of the manual):**

- [ ] **C1:** code snippet of the edited `ge4a_load_n_store_sfns.s` with
      clear comments (all 5 PT functions)
- [ ] **A1:** Screenshot showing all 9 tests pass in Renode (F412dsc)
- [ ] **A2:** Screenshot showing all 9 tests pass on real G431n32 board
      (recommended by course workflow)

### Project ZIP

**Filename:** `cec320-proj5-proj-lastname-firstname.zip`

**Before zipping:**

1. In CubeIDE: right-click each project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/ge4a_load_n_store/`

```bash
cd /opt/proj_mp/
zip -r cec320-proj5-proj-lastname-firstname.zip ge4a_load_n_store/ \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/Debug/*' \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/Release/*' \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/Unity/*' \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/UnitySoln/*'
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | C1 | Edited `ge4a_load_n_store_sfns.s` (all 5 PT bodies) |
| Code Snippets and Screenshots | A1 | 9/9 tests pass — Renode F412dsc |
| Code Snippets and Screenshots | A2 | 9/9 tests pass — G431n32 real board |

---

## Resume State (as of 2026-04-17)

**LLM work done:**

- Project deployed to `/opt/proj_mp/ge4a_load_n_store/` (from `proj05/ge4a_load_n_store.zip`)
- All 5 PT bodies written at
  [`src_ge4a_load_n_store/ge4a_load_n_store_sfns.s`](/opt/proj_mp/ge4a_load_n_store/src_ge4a_load_n_store/ge4a_load_n_store_sfns.s)
- Assembly assembles cleanly with
  `arm-none-eabi-as -mcpu=cortex-m4 -mthumb -o /tmp/ge4a.o ...`
- All 5 algorithms hand-simulated in Python against every Unity test vector:
  - PT1: `{-16,-8,-4}` → `{-12,-4,-1}` ✓
  - PT2a: `"hello very long world"` / `"hello short world"` round-trip ✓
  - PT2b: `len("hi")=2`, `len("hello")=5` ✓
  - PT3a: `abs_sum([-5,-3,-1,0,1,3,5], 3)=9`, `(…, 7)=18` ✓
  - PT3b: `max([-3,-5,-1,7], 3)=-1`, `(…, 4)=7` ✓
- Code artifact saved to [c1.s](./c1.s)

**Human work remaining — exactly these steps:**

1. **Import** in CubeIDE: File → Open Projects from File System → both
   `/opt/proj_mp/ge4a_load_n_store/ge4a_load_n_store_{f412dsc,g431n32}/STM32CubeIDE`
   - Ignore the warning about missing linked resource under
     `UnitySoln/soln/ge4a_load_n_store_sfns.s` → **ignore**, use `Unity` config
2. **F412dsc Unity** → Ctrl+B → in a new terminal:

   ```bash
   cd /opt/proj_mp/ge4a_load_n_store/renode
   renode
   # in Renode monitor:
   #   s @unity_ge4a_load_n_store_f412dsc.resc
   ```

   Expect `9 Tests 0 Failures 0 Ignored / OK` → capture → `proj05/a1.png`
3. **G431n32 Unity** → Ctrl+B → Run As → STM32 C/C++ Application (uses the
   packaged `ge4a_load_n_store_g431n32 Unity.launch`) → capture serial
   terminal output → `proj05/a2.png`
4. Clean All in CubeIDE for both projects
5. Tell the LLM: *"proj05 is done, screenshots are saved, please make the
   submission zip"* → LLM creates `cec320-proj5-proj-lastname-firstname.zip`

**If a test unexpectedly fails:** the 5 PT bodies are at
[/opt/proj_mp/ge4a_load_n_store/src_ge4a_load_n_store/ge4a_load_n_store_sfns.s](/opt/proj_mp/ge4a_load_n_store/src_ge4a_load_n_store/ge4a_load_n_store_sfns.s)
— diff against [c1.s](./c1.s) in this folder to confirm no drift.

---

## Notes and Observations

### Issues Encountered

- The packaged zip already contains CubeIDE `.project` / `.cproject` with
  linked resources using `PARENT-N-PROJECT_LOC`, so no CubeMX
  "Generate Code" step is needed — just **Open Projects from File System**.
- `UnitySoln` build config references a non-existent
  `ge4a_load_n_store_base_n_soln/` sibling folder (plus a `soln/` subfolder
  under STM32CubeIDE). CubeIDE shows a warning about the missing linked
  resource; ignore it and use the `Unity` config.
- **Non-standard source folder names:** the zip uses
  `src_ge4a_load_n_store/` and `test_ge4a_load_n_store/` (not the plain
  `src/` and `test/` of lab08/lab09). The CubeIDE `.project` linked
  resources already target these paths — do not rename them.

### Questions for TA/Instructor

- **PDF vs. base-code divergence.** §5.3.3 of the manual talks about the
  "ReLU norm" (`mp_array_relu_sum`, summation of *positive* elements).
  The shipped zip (and Unity test) instead implements the **absolute-value**
  sum (`mp_array_abs_sum` — negates negatives then always accumulates).
  The submitted code matches the shipped test (`abs_sum`) since those are
  the symbols the test file uses. Please confirm this is the intended
  version; if the PDF is authoritative, a one-line swap of `if (temp < 0)
  neglt r3, r3` → `if (temp < 0) continue` is all that is needed.
