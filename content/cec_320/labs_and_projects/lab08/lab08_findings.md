# Lab 08 Findings: Bit Reversal in C and Assembly

**Course:** CEC 322 / MP-FI4B
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab08_procedure.md](./lab08_procedure.md)
> - Original Manual: `mp-fi4b-lab8-bit-reversal-26-03.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Renode UART — all 14 tests pass (F412dsc Unity) | PT1 + PT2 (90 pts) | [ ] |
| A2 | Screenshot | Putty/tio — all 14 tests pass on real G431n32 Nucleo-32 | Submission | [ ] |
| C1 | Code | Edited `fi4b_bit_reversal_sfns.s` (PT1 fix + PT2 body) | Submission | [ ] |

---

## Screenshot Artifacts

### A1: Unit Tests — All Pass (F412dsc via Renode)

**Required for:** PT1 (30 pts) + PT2 (60 pts)

**What to capture:**

- Renode USART2 analyzer output
- Should end with: `14 Tests 0 Failures 0 Ignored / OK`
- Tests include both `_n_bit_naive_s` and `_16_bit_fast_s` cases

**File to save:** [a1.png](./a1.png)

---

### A2: Unit Tests — All Pass (G431n32 Real Board)

**Required for:** Submission — Unity build on both boards

**What to capture:**

- Serial terminal (Putty / minicom / tio) output from real G431 Nucleo-32
- Same 14-test summary

**File to save:** [a2.png](./a2.png)

---

## Code Snippet Artifacts

### C1: `fi4b_bit_reversal_sfns.s` (PT1 + PT2 edits)

**Required for:** Submission — "Code snippets of all your own code"

**File path:** `/opt/proj_mp/fi4b_bit_reversal/src/fi4b_bit_reversal_sfns.s`

**What was changed:**

1. **PT1** — two register fixes inside `mp_bit_reverse_n_bit_naive_s`:
   - `lsl r6, r2, r4` → `lsl r6, r2, r3`  (`mask_j = 1 << j`)
   - `lsr r7, r0, r3` → `lsr r7, r0, r4`  (`b_i = (x >> i) & 1U`)

2. **PT2** — full body of `mp_bit_reverse_16_bit_fast_s` written by extending
   the given 8-bit fast pattern: four swap stages (distance 1, 2, 4, 8) with
   masks `0x5555 / 0x3333 / 0x0f0f`, final `0xFFFF` clamp.

**Artifact file:** [c1.s](./c1.s)

---

## Submission Checklist

### PDF Report

**Filename:** `fi4b-report-lastname-firstname.pdf`

**Required contents:**

- [ ] C1: Code snippet of the edited `fi4b_bit_reversal_sfns.s` with clear comments
- [ ] A1: Screenshot showing all tests pass in Renode (F412dsc)
- [ ] A2: Screenshot showing all tests pass on G431n32 real board (recommended but not strictly required by manual)

### Project ZIP

**Filename:** `fi4b-proj-lastname-firstname.zip`

**Before zipping:**

1. In CubeIDE: right-click each project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/fi4b_bit_reversal/`

```bash
cd /opt/proj_mp/
zip -r fi4b-proj-lastname-firstname.zip fi4b_bit_reversal/ \
    -x 'fi4b_bit_reversal/*/STM32CubeIDE/Debug/*' \
    -x 'fi4b_bit_reversal/*/STM32CubeIDE/Unity/*' \
    -x 'fi4b_bit_reversal/*/STM32CubeIDE/UnitySoln/*'
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | C1 | Edited `fi4b_bit_reversal_sfns.s` |
| Code Snippets and Screenshots | A1 | 14/14 tests pass — Renode F412dsc |
| Code Snippets and Screenshots | A2 | 14/14 tests pass — G431n32 real board |

---

## Resume State (as of 2026-04-14)

**LLM work done:**

- Project deployed to `/opt/proj_mp/fi4b_bit_reversal/` (from `lab08/fi4b_bit_reversal.zip`)
- PT1 fix applied: two register corrections in `mp_bit_reverse_n_bit_naive_s`
  at [`src/fi4b_bit_reversal_sfns.s`](/opt/proj_mp/fi4b_bit_reversal/src/fi4b_bit_reversal_sfns.s), lines ~46–47
- PT2 body written: full `mp_bit_reverse_16_bit_fast_s` in the same file
- Edited file assembles cleanly with `arm-none-eabi-as -mcpu=cortex-m4 -mthumb`
- Python hand-sim against test inputs: all match
- Code artifact saved to [c1.s](./c1.s)

**Human work remaining — exactly these steps:**

1. **Import** in CubeIDE: File → Open Projects from File System → both
   `/opt/proj_mp/fi4b_bit_reversal/fi4b_bit_reversal_{f412dsc,g431n32}/STM32CubeIDE`
   - Expect a warning about a missing linked resource under
     `UnitySoln/soln/fi4b_bit_reversal_sfns_soln.s` → **ignore**, use `Unity` config
2. **F412dsc Unity** → Ctrl+B → in a new terminal:

   ```bash
   cd /opt/proj_mp/fi4b_bit_reversal/renode
   renode
   # in Renode monitor:
   #   s @unity_fi4b_bit_reversal_f412dsc.resc
   ```

   Expect `14 Tests 0 Failures 0 Ignored / OK` → capture → `lab08/a1.png`
3. **G431n32 Unity** → Ctrl+B → Run As → STM32 C/C++ Application (use the
   packaged `fi4b_bit_reversal_g431n32 Unity.launch`) → capture serial
   terminal output → `lab08/a2.png`
4. Clean All in CubeIDE for both projects
5. Tell the LLM: *"lab08 is done, screenshots are saved, please make the
   submission zip"* → LLM creates `fi4b-proj-lastname-firstname.zip`

**If a test unexpectedly fails:** the PT1 fix and PT2 body are at
[/opt/proj_mp/fi4b_bit_reversal/src/fi4b_bit_reversal_sfns.s](/opt/proj_mp/fi4b_bit_reversal/src/fi4b_bit_reversal_sfns.s)
— diff against [c1.s](./c1.s) in this folder to confirm no drift, and against
the original pristine copy inside `lab08/fi4b_bit_reversal.zip`.

---

## Notes and Observations

### Issues Encountered

- The packaged zip already contains CubeIDE `.project` / `.cproject` with
  linked resources using `PARENT-N-PROJECT_LOC`, so no CubeMX "Generate Code"
  step is needed — just **Open Projects from File System**.
- A `UnitySoln` build config references a non-existent
  `fi4b_bit_reversal_soln/` sibling folder. CubeIDE shows a warning about the
  missing linked resource; ignore it and use the `Unity` config.

### Questions for TA/Instructor

