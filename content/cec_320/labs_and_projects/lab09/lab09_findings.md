# Lab 09 Findings: Condition Code Suffices and Conditional Branch

**Course:** CEC 322 / MP-FO4B
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab09_procedure.md](./lab09_procedure.md)
> - Original Manual: `mp-fo4b-lab9-ccs-n-cond-branch-26-04.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Renode UART — all 5 tests pass (F412dsc Unity) | PT1-PT3 (80 pts) | [ ] |
| A2 | Screenshot | Serial — all 5 tests pass on real G431 Nucleo-32 | Submission | [ ] |
| C1 | Code | `mp_apsr_to_ccs` body in `fo4b_ccs_n_cond_branch_cfns.c` | PT1 (30 pts) | [ ] |
| C2 | Code | `mp_max_ab_i_s` + `mp_range_square_sum_standard_while_s` in `_sfns.s` | PT2+PT3 (50 pts) | [ ] |

---

## Screenshot Artifacts

### A1: Unit Tests — All Pass (F412dsc via Renode)

**Required for:** PT1 (30), PT2 (15), PT3 (35) = 80 pts of programming tasks

**What to capture:**

- Renode USART2 analyzer window
- `5 Tests 0 Failures 0 Ignored / OK`
- Tests: `test_mp_val_apsr_to_apsr`, `test_mp_apsr_to_ccs_case1`,
  `test_mp_apsr_to_ccs_case2`, `test_mp_max_ab_i_s`,
  `test_mp_range_square_sum_standard_while_s`

**File to save:** [a1.png](./a1.png)

---

### A2: Unit Tests — All Pass (G431n32 Real Board)

**Required for:** Submission — running Unity on both boards is required by the
course workflow (even when the manual only says "a screenshot showing tests pass").

**What to capture:**

- Serial terminal output from real G431 Nucleo-32
- Same 5-test summary

**File to save:** [a2.png](./a2.png)

---

## Code Snippet Artifacts

### C1: `mp_apsr_to_ccs` in `fo4b_ccs_n_cond_branch_cfns.c`

**Required for:** PT1 (30 pts)

**File path:** `/opt/proj_mp/fo4b_ccs_n_cond_branch/src/fo4b_ccs_n_cond_branch_cfns.c`

**What was added:** body of the weak `mp_apsr_to_ccs` stub — 10 assignments
translating APSR flag fields (`N, Z, C, V`) into the 10 CCS struct members per
the ARM condition-code table.

**Artifact file:** [c1.c](./c1.c)

### C2: `fo4b_ccs_n_cond_branch_sfns.s` (PT2 + PT3)

**Required for:** PT2 (15 pts) + PT3 (35 pts)

**File path:** `/opt/proj_mp/fo4b_ccs_n_cond_branch/src/fo4b_ccs_n_cond_branch_sfns.s`

**Functions written:**

1. `mp_max_ab_i_s` — 3-instruction signed max using `cmp` + `bge` + `mov`.
2. `mp_range_square_sum_standard_while_s` — `while (i <= e) sum += i*i; i++;`
   loop using `smull` for the 64-bit square and `adds/adc` for the 64-bit
   accumulator. Callee-saved r4/r5 are pushed/popped.

**Artifact file:** [c2.s](./c2.s)

---

## Submission Checklist

### PDF Report

**Filename:** `fo4b-report-lastname-firstname.pdf`

**Required contents (per §9.4 of the manual):**

- [ ] **CET explanation (10 pts):** written paragraphs answering the two
  questions in §9.3.1 (see `lab09_procedure.md` §B.4 for a sketch)
- [ ] **C1:** code snippet of `mp_apsr_to_ccs` with clear comments (PT1)
- [ ] **C2:** code snippets of `mp_max_ab_i_s` and
  `mp_range_square_sum_standard_while_s` with clear comments (PT2, PT3)
- [ ] **A1:** Screenshot showing tests pass in Renode (F412dsc)
- [ ] **A2:** Screenshot showing tests pass on real G431n32 board (recommended)

### Project ZIP

**Filename:** `fo4b-proj-lastname-firstname.zip`

**Before zipping:**

1. In CubeIDE: right-click each project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/fo4b_ccs_n_cond_branch/`

```bash
cd /opt/proj_mp/
zip -r fo4b-proj-lastname-firstname.zip fo4b_ccs_n_cond_branch/ \
    -x 'fo4b_ccs_n_cond_branch/*/STM32CubeIDE/Debug/*' \
    -x 'fo4b_ccs_n_cond_branch/*/STM32CubeIDE/Unity/*' \
    -x 'fo4b_ccs_n_cond_branch/*/STM32CubeIDE/UnitySoln/*'
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| CET discussion | (written) | Explanation of type-cast trick + val_apsr1 shift |
| Code Snippets and Screenshots | C1 | `mp_apsr_to_ccs` (C) |
| Code Snippets and Screenshots | C2 | `mp_max_ab_i_s` + `mp_range_square_sum_standard_while_s` (asm) |
| Code Snippets and Screenshots | A1 | 5/5 tests pass — Renode F412dsc |
| Code Snippets and Screenshots | A2 | 5/5 tests pass — G431n32 real board |

---

## Resume State (as of 2026-04-14)

**LLM work done:**

- Project deployed to `/opt/proj_mp/fo4b_ccs_n_cond_branch/` (from `lab09/fo4b_ccs_n_cond_branch.zip`)
- PT1 body filled in at
  [`src/fo4b_ccs_n_cond_branch_cfns.c`](/opt/proj_mp/fo4b_ccs_n_cond_branch/src/fo4b_ccs_n_cond_branch_cfns.c)
  (replacing the empty weak `mp_apsr_to_ccs` stub)
- PT2 + PT3 bodies filled in at
  [`src/fo4b_ccs_n_cond_branch_sfns.s`](/opt/proj_mp/fo4b_ccs_n_cond_branch/src/fo4b_ccs_n_cond_branch_sfns.s)
- Assembly assembles cleanly with `arm-none-eabi-as -mcpu=cortex-m4 -mthumb`
- CCS logic host-compiled and verified against both `mp_apsr_to_ccs` test cases
- Sum-of-squares logic Python-simulated against all 4 test cases
- Code artifacts saved to [c1.c](./c1.c) and [c2.s](./c2.s)

**Human work remaining:**

1. **Import** in CubeIDE: File → Open Projects from File System → both
   `/opt/proj_mp/fo4b_ccs_n_cond_branch/fo4b_ccs_n_cond_branch_{f412dsc,g431n32}/STM32CubeIDE`
   - Ignore the warning about missing `fo4b_ccs_n_cond_branch_soln/` linked resource
2. **F412dsc Unity** → Ctrl+B → run in Renode:

   ```bash
   cd /opt/proj_mp/fo4b_ccs_n_cond_branch/renode
   renode
   # in monitor: s @unity_fo4b_ccs_n_cond_branch_f412dsc.resc
   ```

   Capture → `lab09/a1.png`
3. **G431n32 Unity** → Ctrl+B → Run As → STM32 C/C++ Application → capture
   serial terminal → `lab09/a2.png`
4. **Write the CET paragraph** in the report (see procedure §B.4 for a sketch)
5. Clean All in CubeIDE
6. Tell the LLM: *"lab09 is done, please make the submission zip"*

---

## Notes and Observations

### Issues Encountered

- Same pattern as lab08: the zip contains a pre-packaged CubeIDE project
  with linked resources, so no CubeMX "Generate Code" step is needed.
- `UnitySoln` build config references a non-existent
  `fo4b_ccs_n_cond_branch_soln/` sibling. Ignore the linked-resource
  warning, use the `Unity` config.

### Questions for TA/Instructor

