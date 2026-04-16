# Lab 10 Findings: Debug Practices

**Course:** CEC 322 / MP-GE4
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab10_procedure.md](./lab10_procedure.md)
> - Original Manual: `mp-ge4-lab10-debug-practices-26-04.pdf`

> **Note:** Manual §10.1 says **"this lab is only for practice purposes. It
> is not graded."** Treat the per-task "10 pts" labels as illustrative.

---

## Blocker cleared (2026-04-15)

Base zip received, extracted to `/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/`
with a single-level layout (no flattening needed). All Task 8 code edits
are applied and verified with `arm-none-eabi-as`.

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Debug build running in PuTTY (real G431) | Task 1 | [ ] |
| A2 | Screenshot | Debugger halted at `_app.c` line 18 | Task 2 | [ ] |
| A3 | Screenshot | Memory view at `0x20000200` before init | Task 3 | [ ] |
| A4 | Screenshot | Same memory after init (line 22) | Task 4 | [ ] |
| A5 | Screenshot | R0–R6 inside `mp_initialize_r1_to_r6_s` | Task 5 | [ ] |
| A6 | Screenshot | Variable view: `p32, var32 (hex), i` | Task 6 | [ ] |
| A7 | Screenshot | Expression view: `regs` + first 10 of `reservation` | Task 7 | [ ] |
| A8 | Screenshot | Unity test pass with new `_pos_sum` test included | Task 8 | [ ] |
| A9 | Screenshot | Editor view of new asm function | Task 8 | [ ] |
| C1 | Code | New `mp_array_pos_sum_cst_ptr_s` in `_sfns.s` | Task 8 | [x] |

All 9 screenshots are required for the (optional) submission PDF.

---

## Resume State (as of 2026-04-15)

**LLM work done:**

- Zip extracted to `/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/` (single-level, no flattening required)
- Read the real `mp_array_abs_sum_cst_ptr_s` and mirrored its style for the new function
- Applied Task 8 edits to all three files:
  - [`src/ge1s_more_ldr_n_str_n_mov_fns.h`](/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/src/ge1s_more_ldr_n_str_n_mov_fns.h): added `int mp_array_pos_sum_cst_ptr_s(int *const pArr, int n);` prototype
  - [`src/ge1s_more_ldr_n_str_n_mov_sfns.s`](/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/src/ge1s_more_ldr_n_str_n_mov_sfns.s): added `.global`/`.type` block and full function body using `blt` skip-on-negative pattern
  - [`test/test_ge1s_more_ldr_n_str_n_mov.c`](/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/test/test_ge1s_more_ldr_n_str_n_mov.c): added `test_mp_array_pos_sum_cst_ptr_s` with `exp = {0, 9}` (first 3 elements all negative → 0; full 7 elements → 0+1+3+5 = 9) and `RUN_TEST` line
- Verified with `arm-none-eabi-as -mcpu=cortex-m4 -mthumb` — assembles cleanly; objdump shows the expected instruction stream
- Code artifact saved to [c1.s](./c1.s)

**Human work — debugger walkthrough (Tasks 1–7):**

This is unavoidably manual; the debugger views (Memory, Registers,
Variables, Expressions, Breakpoints) are interactive CubeIDE GUI features
that an LLM cannot drive. Step-by-step instructions are in
[lab10_procedure.md](./lab10_procedure.md) §B.1–B.7.

**Human work — Task 8 build/run:**

After the LLM finishes the file edits:

1. CubeIDE → switch project to **Unity** build config → Ctrl+B
2. Right-click → **Run As → STM32 C/C++ Application**
3. Watch serial terminal for the new `test_mp_array_pos_sum_cst_ptr_s`
   among the existing tests
4. Capture A8 (test pass) and A9 (asm source)

**Human work — submission (only if instructor grades it despite §10.1):**

Compile A1–A9 into a single PDF.

---

## Notes and Observations

### Issues Encountered

- **Base project zip missing.** The ge1s base project is not on disk and
  must be obtained from the course materials. This is the critical blocker.
- **Lab is not graded** per §10.1, so treat point values as informational.
- Tasks 1–7 are CubeIDE debugger UI exercises. They cannot be automated —
  the LLM cannot click buttons in CubeIDE, set breakpoints in the GUI, or
  capture memory/register views. The procedure document lists exact menu
  paths and expected views.

### Questions for TA/Instructor

- Is a submission PDF actually required, given §10.1's "not graded"?
- The two-level-folder warning in Task 1 ("you cannot have two levels") —
  on Linux, does `unzip` produce a single level here, or do we need to
  flatten? (Will be answered when the LLM extracts the zip.)
