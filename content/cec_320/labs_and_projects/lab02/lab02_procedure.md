# Lab 02 Procedure: Debugging with CubeIDE for Fibonacci Number Generation

**Course:** CEC 320 / MP-CE5D
**Points:** 100 total (PT 30 + PC/MT 20 + DT 40 + Submission 10)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - [known_issues.md](../known_issues.md) - Check here if stuck
> - Original PDF: `mp-ce5d-lab2-cubeide-debug-4-fib-26-02.pdf`

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | **DONE** - Extracted zip to `/opt/proj_mp/ce5d_debug_fib/`, created `ce5d_debug_fib_g431n32/` with `.ioc` |
| 3 | HUMAN | CubeMX: Open `.ioc` in `ce5d_debug_fib_g431n32`, Save Project As, Generate Code, Open in CubeIDE |
| 4 | HUMAN | CubeIDE: Add hook to `main.c`, create `lib_src`, add include path `../../lib`, link 3 files, Build |
| 5 | HUMAN | Connect NUCLEO-G431KB board, open PuTTY for serial output |
| 6 | HUMAN | CubeIDE: Open `ce5d_debug_fib_app.c` in `lib_src`, set breakpoints BP1-BP4 |
| 7 | HUMAN | Enter Debug perspective, Run to BP1 |
| -> | **ARTIFACT** | **A1:** Screenshot of halted program at BP1 |
| 8 | HUMAN | Resume to BP2, inspect `N[]` in Variables view |
| -> | **ARTIFACT** | **A2:** Screenshot of `N[]` values at BP2 |
| 9 | LLM | Write `mp_update_fib_array` code (PT 1, 20 pts) |
| 10 | HUMAN | Rebuild, Debug, Run to BP3. Verify "5 Fibonacci numbers" output in PuTTY |
| 11 | HUMAN | At BP3: Add `fibonacci_arr1` to Expression view |
| -> | **ARTIFACT** | **A3:** Screenshot of `fibonacci_arr1` in Expression view |
| 12 | LLM | Write `mp_app` for-loop code (PT 2, 10 pts) |
| 13 | HUMAN | Rebuild, Debug, Run to BP4. Verify full printed output in PuTTY |
| -> | **ARTIFACT** | **A4:** Screenshot of full printed output (arrays 1 and 2) |
| 14 | HUMAN | Get array addresses from Expressions view, open Memory view with lower address, Unsigned Integer format |
| -> | **ARTIFACT** | **A5:** Screenshot of Memory view |
| 15 | LLM | Fix the array size bug (DT 6, 6 pts) |
| 16 | HUMAN | Rebuild, Debug, verify correct 10th Fibonacci number |
| -> | **ARTIFACT** | **A6:** Screenshot of corrected output |
| 17 | HUMAN | Clean build, zip project, write report PDF |

---

## Task Classification Summary

| Section | Task | Points | Who |
|---------|------|--------|-----|
| PC 0 | Create project folders and copy files | 0 | LLM |
| PC 1 | Generate C code from CubeMX | 5 | HUMAN |
| MT 1 | Manage project in CubeIDE | 15 | HUMAN |
| PT 1 | Program `mp_update_fib_array` | 20 | LLM |
| PT 2 | Program `mp_app` for loops | 10 | LLM |
| DT 1 | Set up breakpoints | 5 | HUMAN |
| DT 2 | Debug perspective, run to BP1 | 5 | HUMAN |
| DT 3 | Inspect local variables | 8 | HUMAN |
| DT 4 | Inspect global variables | 8 | HUMAN |
| DT 5 | Inspect memory | 8 | HUMAN |
| DT 6 | Fix the bug | 6 | LLM (code) + HUMAN (verify) |
| Sub | Submission (report + zip) | 10 | HUMAN |

---

## Prerequisites

Before starting, ensure you have:

1. **Base project zip:** `ce5d_debug_fib-f412.zip` (in `./lab02/` folder)
2. **Reference project:** `ce1s_print_in_diff_formats` zip (in `./lab02/` folder)
   - **STATUS: DONE** - G431n32 `.ioc` extracted and copied to project
3. **NUCLEO-G431KB board** connected via Micro-USB
4. **PuTTY** configured for serial communication with the board

---

## Zip Contents Analysis

The provided `ce5d_debug_fib-f412.zip` extracts as `ce5d_debug_fib-f412/` with:

```
ce5d_debug_fib-f412/
├── ce5d_debug_fib_f412dsc/        # F412 version (fully set up with STM32CubeIDE/)
│   ├── ce5d_debug_fib_f412dsc.ioc
│   ├── STM32CubeIDE/              # Has .cproject, .project, Debug/ makefiles
│   ├── Drivers/                   # HAL drivers
│   ├── Inc/                       # Generated headers
│   └── Src/                       # Generated sources (main.c with mp_main hook)
├── lib/                           # mp_bin_str_printing.c/.h, mp_supported_mcu.h, mp_uart_redirect.c/.h
├── renode/                        # debug_ce5d_debug_fib_f412dsc.resc (correctly named)
└── src/                           # ce5d_debug_fib_app.c (skeleton), _mp_main.c
```

**What the zip provides (no copying needed):**
- All `lib/` files (mp_bin_str_printing, mp_supported_mcu, mp_uart_redirect)
- All `src/` files (ce5d_debug_fib_app.c skeleton, _mp_main.c)
- All `renode/` scripts (already correctly named)
- Complete F412 CubeIDE project with correct include paths (`../../lib`)

**What's missing (must be created):**
- `ce5d_debug_fib_g431n32/` folder with a G431n32 `.ioc` file (from `ce1s_print_in_diff_formats`)

**Note:** The F412 `.cproject` already has correct include paths (`../../../lib`), no folder-level override issue.

---

## Part A: Claude Code Automated Tasks

> These tasks are performed by Claude Code. Human verifies completion.

### A.1 PC 0: Extract and Set Up Project (0 pts)

**Step 1: Extract zip and rename**

```bash
cd /opt/proj_mp/
unzip ~/electrical_notes/content/cec_320/labs_and_projects/lab02/ce5d_debug_fib-f412.zip
mv ce5d_debug_fib-f412 ce5d_debug_fib
```

Resulting structure:

```
/opt/proj_mp/ce5d_debug_fib/
├── ce5d_debug_fib_f412dsc/   # F412 (provided, complete)
├── lib/                       # Library files (provided)
├── renode/                    # Renode scripts (provided)
└── src/                       # Source code skeleton (provided)
```

**Step 2: Create G431n32 folder**

```bash
mkdir -p /opt/proj_mp/ce5d_debug_fib/ce5d_debug_fib_g431n32/
```

**Step 3: Copy G431n32 .ioc file from reference project**

**DONE** - Copied `ce1s_print_in_diff_formats_g431n32.ioc` to `ce5d_debug_fib_g431n32/`.

PC 0 is complete. The project is ready for CubeMX.

---

### A.2 PT 1: Program `mp_update_fib_array` Function (20 pts)

**File:** `/opt/proj_mp/ce5d_debug_fib/src/ce5d_debug_fib_app.c`

**Location:** Line 18, replace `// Add your code here` inside the `else if (N <= 20)` block.

**Existing skeleton:**

```c
    } else if (N <= 20) {
// Add your code here       // <-- REPLACE THIS
    } else {
```

**Code to insert:**

```c
        fib_arr[0] = 0;
        fib_arr[1] = 1;
        int i = 2;
        while (i <= N) {
            fib_arr[i] = fib_arr[i-1] + fib_arr[i-2];
            i = i + 1;
        }
```

This implements Algorithm 1 from the lab manual - Fibonacci computation from index 2 through N.

---

### A.3 PT 2: Program `mp_app` For Loops (10 pts)

**File:** `/opt/proj_mp/ce5d_debug_fib/src/ce5d_debug_fib_app.c`

**Context:** The first for-loop (lines 43-47, printing 5 Fibonacci numbers) already has the complete code as an example:

```c
    for (int i = 1; i <= 5; i++) {
        dec_int = fibonacci_arr1[i];
        mp_bin_num_2_n_bit_vrbs_bin_str(bin_str, dec_int, 8);
        printf(result_info, i, dec_int, bin_str, dec_int);
    }
```

The two remaining loops need the same pattern.

**Replace line 55** (`// Add your code here` in array 1 for-loop):

```c
        mp_bin_num_2_n_bit_vrbs_bin_str(bin_str, dec_int, 8);
        printf(result_info, i, dec_int, bin_str, dec_int);
```

**Replace line 61** (`// Add your code here` in array 2 for-loop):

```c
        mp_bin_num_2_n_bit_vrbs_bin_str(bin_str, dec_int, 8);
        printf(result_info, i, dec_int, bin_str, dec_int);
```

---

### A.4 DT 6: Fix the Bug (6 pts)

**The bug:** Array sizes are too small for the indices being used.

| Array | Declared Size | Called With N= | Indices Written | Out of Bounds? |
|-------|--------------|----------------|-----------------|----------------|
| `fibonacci_arr1[10]` | 10 (indices 0-9) | 10 | 0-10 | Yes, index 10 |
| `fibonacci_arr2[13]` | 13 (indices 0-12) | 13 | 0-13 | Yes, index 13 |

**Symptom:** Fibonacci number 10 from array 1 prints as `0` (out-of-bounds read).

**Fix in** `/opt/proj_mp/ce5d_debug_fib/src/ce5d_debug_fib_app.c` **line 6:**

```c
// BEFORE (buggy):
static uint32_t fibonacci_arr1[10], fibonacci_arr2[13];

// AFTER (fixed):
static uint32_t fibonacci_arr1[11], fibonacci_arr2[14];
```

**Hint from manual (Section 2.6):** "The index of the array in C starts at 0, and hence the size of the array is the maximum index number plus 1."

---

## Part B: Human Tasks (GUI Required)

> Follow steps exactly. Copy-paste commands where provided.

### B.1 PC 1: Generate C Code from CubeMX (5 pts)

1. Double-click the `.ioc` file in `/opt/proj_mp/ce5d_debug_fib/ce5d_debug_fib_g431n32/`
2. **File -> Save Project as** - verify folder is correct, click **OK**
3. Click **Generate Code**
4. Click **Open project** - CubeIDE will open
5. Click **OK** on import success message

### B.2 MT 1: Manage Project in CubeIDE (15 pts)

**Step 1:** Add hook to `main.c`

Open `main.c` under `Application/User` of `ce5d_debug_fib_g431n32`. Add between `/* USER CODE BEGIN 2 */` and `/* USER CODE END 2 */`:

```c
void mp_main(void);   // <-- Prototype of the HOOK
mp_main();             // <-- The HOOK function
```

**Step 2:** Create folder `lib_src`

- Right-click project title -> **New -> Folder** -> name `lib_src` -> **Finish**

**Step 3:** Add include paths

- Right-click **project title** (NOT lib_src!) -> **Properties**
- **C/C++ General -> Paths and Symbols** -> **Includes** tab -> **GNU C**
- Click **Add...** -> type `../../lib` -> check **Add to all configurations** -> **OK**

> **WARNING:** Verify `lib_src` does NOT have its own include paths. See [known_issues.md](../known_issues.md).

**Step 4:** Link files to `lib_src`

Use **New -> File -> Advanced -> Link to file in the file system** (see [known_issues.md](../known_issues.md)):

| Source File (full path) | Destination |
|-------------------------|-------------|
| `/opt/proj_mp/ce5d_debug_fib/lib/mp_bin_str_printing.c` | `lib_src` |
| `/opt/proj_mp/ce5d_debug_fib/lib/mp_uart_redirect.c` | `lib_src` |
| `/opt/proj_mp/ce5d_debug_fib/src/ce5d_debug_fib_app.c` | `lib_src` |
| `/opt/proj_mp/ce5d_debug_fib/src/_mp_main.c` | `lib_src` |

**Step 5:** Build (**Ctrl+B**)

- Warning `unused variable 'bin_str'` is expected at this stage
- If include errors occur, check [known_issues.md](../known_issues.md)

### B.3 Hardware Setup

1. Get **NUCLEO-G431KB board** from TA
2. Connect via **Micro-USB**
3. Upgrade firmware if prompted
4. Open **PuTTY** for serial (see VCP chapter of Companion)

### B.4 DT 1: Set Up Breakpoints (5 pts)

1. **Editor perspective** (click **C/C++** icon at upper right)
2. Open `ce5d_debug_fib_app.c` from `lib_src`
3. Double-click **Gutter** (left margin) at:

| BP | Line of Code |
|----|-------------|
| **BP1** | `printf("\n\nRunning ce5d_debug_fib App ---\n");` |
| **BP2** | `mp_update_fib_array(fibonacci_arr1, 5);` |
| **BP3** | `mp_update_fib_array(fibonacci_arr1, 10);` |
| **BP4** | `while (1) {` |

4. Remove leftover breakpoints from other projects

### B.5 DT 2: Run to BP1 (5 pts)

1. Click **Debug** icon (bug) -> Debug perspective
2. Click **Run** -> halts at **BP1**

> **ARTIFACT A1:** Screenshot of halted program at BP1. Describe how you know it stopped.

### B.6 DT 3: Inspect Local Variables at BP2 (8 pts)

1. **Variables** view -> expand `N` (values are random/uninitialized)
2. Click **Run** -> stops at **BP2**
3. Expand `N` -> values: `{-1, 0, 1, 5, 21}`
4. PuTTY shows status messages for each N value

> **ARTIFACT A2:** Screenshot of `N[]` in Variables view. Determine size of `N`.

### B.7 After PT 1: Verify at BP3

1. Rebuild after `mp_update_fib_array` is written
2. Debug -> Run to BP3
3. PuTTY shows 5 Fibonacci numbers (1, 1, 2, 3, 5)

### B.8 DT 4: Global Variables at BP3 (8 pts)

1. **Expression** view -> **Add new expression** -> `fibonacci_arr1`
2. Expand: `{0, 1, 1, 2, 3, 5, 0, 0, 0, 0}`

> **ARTIFACT A3:** Screenshot of `fibonacci_arr1` in Expression view. Determine size.

### B.9 After PT 2: Full Output at BP4

1. Rebuild after for-loop code is written
2. Debug -> Run to BP4
3. **Note:** Fibonacci number 10 shows **0** (intentional bug)

> **ARTIFACT A4:** Screenshot of full output (both arrays).

### B.10 DT 5: Memory Inspection (8 pts)

1. Note addresses of `fibonacci_arr1` and `fibonacci_arr2` from Expression view
2. **Memory** view (lower pane) -> **[+]** -> enter lower hex address
3. Set rendering to **Unsigned Integer**

> **ARTIFACT A5:** Screenshot of Memory view. Estimate size of `fibonacci_arr2`.

### B.11 After Bug Fix: Verify (DT 6)

1. Rebuild after array size fix
2. Debug -> Run to BP4
3. Fibonacci number 10 is now **55**

> **ARTIFACT A6:** Screenshot of corrected output.

---

## Submission Checklist

### PDF Report: `ce5d-report-lastname-firstname.pdf`

- [ ] **A1:** Screenshot at BP1 + describe how you know it stopped
- [ ] **A2:** Screenshot of `N[]` at BP2 + determine size of `N`
- [ ] **A3:** Screenshot of `fibonacci_arr1` + determine size
- [ ] **A4:** Screenshot of full output at BP4
- [ ] **A5:** Screenshot of Memory view + estimate size of `fibonacci_arr2`
- [ ] **A6:** Screenshot of corrected output

### Project ZIP: `ce5d-proj-lastname-firstname.zip`

```bash
# Clean builds first in CubeIDE: Project -> Clean
cd /opt/proj_mp/
zip -r ce5d-proj-lastname-firstname.zip ce5d_debug_fib/
```

---

## Important Notes

- This lab uses **physical hardware** (NUCLEO-G431KB + PuTTY), NOT Renode
- Workflow is **iterative**: debug -> code -> debug -> code -> fix bug
- **Intentional bug:** array sizes too small (`[10]` should be `[11]`, `[13]` should be `[14]`)
- The F412 `.cproject` has correct include paths - no Lab 01 include path issue
- The first for-loop (5 Fibonacci numbers) already has complete code as a PT 2 example
