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

## ⚠️ Blocker on resume

The base project **`ge1s_more_ldr_n_str_n_mov.zip` is not on disk**. The
manual instructs the student to download it from the course materials. The
LLM searched `lab10/`, `/opt/proj_mp/`, `~`, and `/tmp` — not present.

**Action required from the human:** download the zip and drop it into
`lab10/`, then resume.

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
| C1 | Code | New `mp_array_pos_sum_cst_ptr_s` in `_sfns.s` | Task 8 | [ ] |

All 9 screenshots are required for the (optional) submission PDF.

---

## Resume State (as of 2026-04-14)

**LLM work done:**

- Read PDF and identified the structure (7 debug-GUI tasks + 1 small asm task)
- Confirmed `ge1s_more_ldr_n_str_n_mov` base zip is **not** on the system
- Drafted [task8_draft.s](./task8_draft.s) — a placeholder
  `mp_array_pos_sum_cst_ptr_s` template using a `blt skip_neg` to skip the
  add for negative elements. The draft assembles cleanly with
  `arm-none-eabi-as -mcpu=cortex-m4 -mthumb`.
- Created the procedure + findings + report skeletons noting the blocker

**LLM work remaining (after the human supplies the zip):**

1. Extract `lab10/ge1s_more_ldr_n_str_n_mov.zip` to
   `/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/`
2. Read the **real** `mp_array_abs_sum_cst_ptr_s` from
   `src/ge1s_more_ldr_n_str_n_mov_sfns.s` to confirm its register usage,
   label naming, and `.global`/`.type` declarations
3. Reconcile the draft with the real `_abs_sum` style (the manual is
   explicit: "copy and rename" — the new function should mirror the
   structure of the existing one)
4. Apply the edits to **three files**:
   - `src/ge1s_more_ldr_n_str_n_mov_fns.h` — add prototype
   - `src/ge1s_more_ldr_n_str_n_mov_sfns.s` — add `.global`/`.type` block + body
   - `test/test_ge1s_more_ldr_n_str_n_mov.c` — add new test function and
     `RUN_TEST(test_mp_array_pos_sum_cst_ptr_s);` in `mp_unity()`. Compute
     `exp[]` for the same `arr[]` used by the abs-sum test, but as the sum
     of positive elements only.
5. Re-verify with `arm-none-eabi-as` and (if possible) host-compile the new
   test logic to confirm `exp[]` is correct
6. Save the edited file as `lab10/c1.s`

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
