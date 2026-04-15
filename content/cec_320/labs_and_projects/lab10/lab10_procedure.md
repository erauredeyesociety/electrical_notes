# Lab 10 Procedure: Debug Practices

**Course:** CEC 322 / MP-GE4
**Points:** **NOT GRADED** — the PDF (§10.1) explicitly says
*"this lab is only for practice purposes. It is not graded."* The "10 pts"
labels in the task headers are vestigial; submit only if your instructor
overrides the not-graded note.

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-ge4-lab10-debug-practices-26-04.pdf`
> - [known_issues.md](../known_issues.md)

---

## ⚠️ Blocker — base project zip not on disk

This lab uses `ge1s_more_ldr_n_str_n_mov.zip`, which the manual tells you
to **download from the course materials** (Canvas/instructor). It is **not
in `lab10/`** and is **not in `/opt/proj_mp/`**. Before any of the steps
below can run, you (the human) need to:

1. Download `ge1s_more_ldr_n_str_n_mov.zip` from Canvas (or wherever your
   instructor posts base projects).
2. Drop it into `~/electrical_notes/content/cec_320/labs_and_projects/lab10/`
3. Tell the LLM: *"the ge1s zip is in lab10 now, please extract and continue"*

Once the zip is there, the LLM can:

- Extract it to `/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/`
- Read `ge1s_more_ldr_n_str_n_mov_sfns.s` to confirm the actual signature
  of `mp_array_abs_sum_cst_ptr_s`
- Verify / refine the Task 8 draft (see `task8_draft.s` in this folder)
- Apply the edit and assemble-check it

---

## TLDR - Execution Sequence

Lab 10 is mostly a **debugger UI walkthrough** on real hardware (G431 Nucleo-32),
plus one small assembly write task at the end. There's no Renode and no
unit test for tasks 1–7.

| Step | Who | Task |
|------|-----|------|
| 0 | HUMAN | Download `ge1s_more_ldr_n_str_n_mov.zip`, place in `lab10/` |
| 1 | LLM | Extract zip to `/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/` |
| 2 | HUMAN | CubeIDE: import `ge1s_more_ldr_n_str_n_mov_g431n32`, build **Debug** |
| 3 | HUMAN | Run on real G431 Nucleo-32 → PuTTY screenshot → **A1** (Task 1) |
| 4 | HUMAN | Set breakpoint at `ge1s_more_ldr_n_str_n_mov_app.c` line 18 → run → halt screenshot → **A2** (Task 2) |
| 5 | HUMAN | Memory view at `0x20000200`, format Row=8 Col=1 → screenshot → **A3** (Task 3) |
| 6 | HUMAN | Step over until line 22, re-screenshot memory → **A4** (Task 4) |
| 7 | HUMAN | Step into `mp_initialize_r1_to_r6_s` on line 22, step over to `store_r1_to_r6_local_0`, screenshot R0–R6 → **A5** (Task 5) |
| 8 | HUMAN | Step Return, step over to line 31, Variable view of `p32, var32, i` (var32 in hex) → **A6** (Task 6) |
| 9 | HUMAN | Expression view of `regs` and first 10 of `reservation` → **A7** (Task 7) |
| 10 | LLM | Task 8 plan: copy `mp_array_abs_sum_cst_ptr_s` → `mp_array_pos_sum_cst_ptr_s` in 3 files (header, asm, test) |
| 11 | LLM | Apply Task 8 edits to header, asm, and test files; verify asm |
| 12 | HUMAN | CubeIDE: build **Unity**, Run As on real board → screenshot test pass → **A8** |
| 13 | HUMAN | Screenshot of the new asm function → **A9** |
| 14 | LLM | Save code artifact, update findings/report |
| 15 | HUMAN | Compile screenshots into a single PDF if your instructor wants a submission |

---

## Point Breakdown (per the PDF, but lab is NOT graded)

| Section | Points | Description |
|---------|--------|-------------|
| Task 1 | 10 | Build Debug, run on real board, PuTTY screenshot |
| Task 2 | 10 | Breakpoints — halt at line 18 |
| Task 3 | 10 | Memory view at `0x20000200` before init |
| Task 4 | 10 | Step over, observe memory change after init |
| Task 5 | 10 | Step into `mp_initialize_r1_to_r6_s`, register view |
| Task 6 | 10 | Variable view: `p32, var32, i` (var32 in hex) |
| Task 7 | 10 | Expression view: `regs` and first 10 of `reservation` |
| Task 8 | 20 | Write `mp_array_pos_sum_cst_ptr_s` asm + test, run Unity |
| §10.3 Submission | 10 | Single-PDF submission of all screenshots |

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Download base zip | HUMAN |
| Extract zip to `/opt/proj_mp/` | CLAUDE CODE |
| Import project, build Debug | HUMAN |
| Run on real G431 (PuTTY/tio) | HUMAN |
| All debugger GUI tasks (1–7) | HUMAN — debugger work cannot be automated |
| Task 8 — write `mp_array_pos_sum_cst_ptr_s` asm | CLAUDE CODE |
| Task 8 — add header proto + Unity test case + RUN_TEST line | CLAUDE CODE |
| Build Unity, run on real board, capture screenshots | HUMAN |
| Save code artifact, update docs | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks (post-zip)

### A.1 Extract Base Files

```bash
cd /opt/proj_mp
unzip ~/electrical_notes/content/cec_320/labs_and_projects/lab10/ge1s_more_ldr_n_str_n_mov.zip
# verify expected layout:
ls /opt/proj_mp/ge1s_more_ldr_n_str_n_mov/
```

The PDF warns: **do not have two levels of `ge1s_more_ldr_n_str_n_mov`**.
If `unzip` produces `ge1s_more_ldr_n_str_n_mov/ge1s_more_ldr_n_str_n_mov/...`,
the LLM should flatten it before continuing.

### A.2 Read existing `mp_array_abs_sum_cst_ptr_s`

Once the zip is extracted, the LLM reads
`/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/src/ge1s_more_ldr_n_str_n_mov_sfns.s`
to confirm the actual function signature, register usage, and label naming
conventions. The Task 8 draft (`task8_draft.s` in this folder) is a
*placeholder template* that must be reconciled with the real `_abs` function
before being applied.

### A.3 Apply Task 8 edits in three files

1. **`src/ge1s_more_ldr_n_str_n_mov_fns.h`** — copy the prototype of
   `mp_array_abs_sum_cst_ptr_s` and rename to `mp_array_pos_sum_cst_ptr_s`.
2. **`src/ge1s_more_ldr_n_str_n_mov_sfns.s`** — copy both the prototype
   declaration block at the top and the function body at the bottom; rename;
   replace the abs-value step with a conditional skip for negative elements.
3. **`test/test_ge1s_more_ldr_n_str_n_mov.c`** — copy
   `test_mp_array_abs_sum_cst_ptr_s`, rename to `test_mp_array_pos_sum_cst_ptr_s`,
   recompute `exp[]` to be the sum of the positive elements only, and add a
   `RUN_TEST(test_mp_array_pos_sum_cst_ptr_s);` line in `mp_unity()`.

### A.4 Verify with `arm-none-eabi-as`

After the edit, the LLM runs:

```bash
arm-none-eabi-as -mcpu=cortex-m4 -mthumb \
    -o /tmp/ge1s_sfns.o \
    /opt/proj_mp/ge1s_more_ldr_n_str_n_mov/src/ge1s_more_ldr_n_str_n_mov_sfns.s
arm-none-eabi-objdump -d /tmp/ge1s_sfns.o
```

…to confirm the new function assembles cleanly. (This is the same
sanity-check pattern used for lab08 and lab09.)

### A.5 Save Code Artifact

After tests pass, save the edited `_sfns.s` snippet (or the diff hunk) to
`lab10/c1.s` for inclusion in any submission PDF.

---

## Part B: Human Tasks (GUI Required)

### B.1 Task 1 — Build & Run (Debug, Real Board) — Artifact A1

1. CubeIDE → **File → Open Projects from File System** → directory
   `/opt/proj_mp/ge1s_more_ldr_n_str_n_mov/ge1s_more_ldr_n_str_n_mov_g431n32/STM32CubeIDE`
2. Open `ge1s_more_ldr_n_str_n_mov_app.c` in the editor (you'll need it
   visible for the breakpoint in Task 2).
3. Switch to build config **Debug** → Ctrl+B (should build with no errors).
4. Connect the G431 Nucleo-32 board via USB. Open PuTTY (or
   `tio /dev/ttyACM0 -b 115200`).
5. Right-click project → **Run As → STM32 C/C++ Application**.
6. Capture the PuTTY/serial window showing the running app → **`a1.png`**.

### B.2 Task 2 — Breakpoints — Artifact A2

1. In `ge1s_more_ldr_n_str_n_mov_app.c`, double-click the gutter on **line 18**
   to set a breakpoint.
2. Switch to the **Debug perspective** (Window → Perspective → Open Perspective
   → Debug, or click the bug icon).
3. Right-click project → **Debug As → STM32 C/C++ Application**.
4. If it doesn't halt, open the **Breakpoints** view, **Remove All**
   (left-over breakpoints from other projects can prevent new ones from
   firing if the limit is exceeded), then re-set the breakpoint at line 18
   and Resume.
5. Capture the halted editor showing the green arrow at line 18 → **`a2.png`**.

### B.3 Task 3 — Memory view before init — Artifact A3

1. **Window → Show View → Memory** (or Other... → Debug → Memory).
2. Click the green **[+]** in the Memory view → enter `0x20000200` → OK.
3. Right-click any cell → **Format...** → set **Row Size: 8**, **Column Size: 1**.
4. Capture the memory view → **`a3.png`**.

### B.4 Task 4 — Step over to line 22 — Artifact A4

1. Press **Step Over (F6)** until the green PC arrow is on **line 22**.
   This passes line 21 (the memory init), so the memory contents you
   captured in A3 should now be different.
2. Re-capture the same Memory view → **`a4.png`**.

### B.5 Task 5 — Step into + Register view — Artifact A5

1. With the PC on line 22, press **Step Into (F5)** to enter
   `mp_initialize_r1_to_r6_s`. Do **not** execute any instructions yet.
2. **Window → Show View → Registers** (or Debug → Registers).
3. **Step Over (F6)** until the PC is on the line labeled
   `store_r1_to_r6_local_0`.
4. Capture the Registers view showing R0–R6 → **`a5.png`**.

### B.6 Task 6 — Variable view — Artifact A6

1. Press **Step Return (F7)** to leave `mp_initialize_r1_to_r6_s` and
   come back to the C caller.
2. **Step Over (F6)** until the PC is on **line 31**.
3. Open the **Variables** view. You should see `p32`, `var32`, `i`.
4. Right-click the `var32` row → **Number Format → Hex**.
5. Capture the Variables view → **`a6.png`**.

### B.7 Task 7 — Expression view (globals) — Artifact A7

1. Open the **Expressions** view.
2. Add a new expression `regs`.
3. Add a second expression `reservation`.
4. Expand both, scroll so all of `regs` and the first 10 elements of
   `reservation` are visible.
5. Capture → **`a7.png`**.

### B.8 Task 8 — Build Unity, run on board — Artifacts A8 & A9

After the LLM has finished Part A.3:

1. Switch to build config **Unity** → Ctrl+B.
2. Right-click project → **Run As → STM32 C/C++ Application** (use the
   Unity launch config).
3. In the serial terminal, watch for the new test
   `test_mp_array_pos_sum_cst_ptr_s` — it should pass alongside the
   existing tests.
4. Capture the serial output → **`a8.png`**.
5. Capture the editor view of the new asm function → **`a9.png`**.

### B.9 Submission

If your instructor decides to override the "not graded" note, paste the 9
screenshots into a single PDF and submit per Canvas instructions. The
manual just says "Submit a single pdf file with all the above screenshots."
There's no naming convention given.

---

## Programming Task Details

### Task 8: `mp_array_pos_sum_cst_ptr_s`

**Goal:** Sum only the **positive** elements of an int array (skip negatives).
The starting point is the existing `mp_array_abs_sum_cst_ptr_s`, which sums
the **absolute values** of every element.

**Difference:**

- `_abs_sum`: for negative elements, negate (`rsb`/`neg`) and then add.
- `_pos_sum`: for negative elements, **skip the add entirely**.

**Three file edits required:**

1. **Header** (`ge1s_more_ldr_n_str_n_mov_fns.h`) — add the prototype copy.
2. **Assembly** (`ge1s_more_ldr_n_str_n_mov_sfns.s`) — add a `.global` /
   `.type` declaration block matching the existing one for `_abs_sum`, and
   add the function body at the bottom.
3. **Test** (`test_ge1s_more_ldr_n_str_n_mov.c`) — duplicate the test, rename,
   recompute `exp[]` (sum of positive elements only), add a `RUN_TEST` line.

**Asm template (placeholder — must be reconciled with the real `_abs_sum`
function once the zip is in place):** see [task8_draft.s](./task8_draft.s).

---

## Submission Checklist

- [ ] (Blocker) Base project zip downloaded and placed in `lab10/`
- [ ] A1: Screenshot — Debug build running on G431 (PuTTY)
- [ ] A2: Screenshot — halted at line 18
- [ ] A3: Screenshot — memory at `0x20000200`, before init
- [ ] A4: Screenshot — same memory after init (line 22)
- [ ] A5: Screenshot — R0–R6 inside `mp_initialize_r1_to_r6_s`
- [ ] A6: Screenshot — `p32, var32 (hex), i` in Variables view
- [ ] A7: Screenshot — `regs` + first 10 of `reservation` in Expressions view
- [ ] A8: Screenshot — Unity test pass with new test included
- [ ] A9: Screenshot — new asm function source
- [ ] C1: Edited `ge1s_more_ldr_n_str_n_mov_sfns.s`
- [ ] (only if instructor requires) Single PDF of all 9 screenshots
