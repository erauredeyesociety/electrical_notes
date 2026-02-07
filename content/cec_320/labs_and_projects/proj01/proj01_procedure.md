# Proj 01 Procedure: Pointers and Unit Test

**Course:** CEC 320 - Microprocessors
**Points:** 100 (PT1: 10, PT2: 30, PT3: 25, PT4: 25, Submission: 10)
**Instructor:** Jianhua Liu
**Semester:** Spring 2026

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-ci4u-proj1-ptr-tdd-2026-01.pdf`

---

## TLDR - Execution Sequence

| Step | Who | Task | Expected Test Results |
|------|-----|------|----------------------|
| 1 | LLM | Place provided source files in `proj1_src/` and `proj1_test/` | — |
| 2 | HUMAN | CubeIDE: Link `.c` files into `proj1_src_test/` folder | — |
| 3 | HUMAN | CubeIDE: Select `Proj1Unity` build config → Build | — |
| 4 | HUMAN | Renode: Run `s @proj1Unity_f412dsc.resc` — verify test harness runs | 0 pass, 3 fail |
| 5 | LLM | Implement PT1 ONLY: Fix `mp_swap` to use pointers | — |
| 6 | HUMAN | CubeIDE: Rebuild → Renode: Rerun | **1 pass, 2 fail** |
| → | **ARTIFACT** | **Artifact 1a:** Screenshot showing `test_mp_swap` PASSED, others FAIL | |
| → | **ARTIFACT** | **Artifact 1b:** Code of finished `mp_swap` function | |
| 7 | LLM | Implement PT2 ONLY: Write `mp_partial_sum` function | — |
| 8 | HUMAN | CubeIDE: Rebuild → Renode: Rerun | **2 pass, 1 fail** |
| → | **ARTIFACT** | **Artifact 2a:** Screenshot showing `test_mp_partial_sum` PASSED, reverse_str FAIL | |
| → | **ARTIFACT** | **Artifact 2b:** Code of finished `mp_partial_sum` function | |
| 9 | LLM | Implement PT4: Write `test_mp_reverse_str` test function | — |
| 10 | LLM | Implement PT3: Write `mp_reverse_str` function | — |
| 11 | HUMAN | CubeIDE: Rebuild → Renode: Rerun | **3 pass, 0 fail** |
| → | **ARTIFACT** | **Artifact 3a:** Screenshot showing ALL 3 tests PASSED | |
| → | **ARTIFACT** | **Artifact 3b:** Code of finished `mp_reverse_str` function | |
| → | **ARTIFACT** | **Artifact 4a:** Screenshot showing all tests PASSED | |
| → | **ARTIFACT** | **Artifact 4b:** Code of finished `test_mp_reverse_str` function | |
| 12 | HUMAN | Create PDF report, clean builds, zip project, submit | — |

> **Incremental testing:** Each artifact screenshot must show progressive test results. Implement ONLY the current task before taking the screenshot. Do NOT implement all tasks at once.

---

## Project Overview

This project uses the **existing `ca4b_cls_projs` base project** at `/opt/proj_mp/ca4b_cls_projs/`. Unlike previous labs, there is **no CubeMX step** — the project infrastructure is already set up. You only need to:

1. Place source files in the correct folders
2. Link them in CubeIDE
3. Build and run using the `Proj1Unity` build configuration
4. Implement 4 programming tasks (PTs)

### Project Structure (relevant paths)

```
/opt/proj_mp/ca4b_cls_projs/
├── proj1_src/                          ← PUT SOURCE FILES HERE (currently empty)
│   ├── _mp_main.c
│   ├── proj1_app.c
│   ├── proj1_cfns.c
│   └── proj1_fns.h
├── proj1_test/                         ← PUT TEST FILES HERE (currently empty)
│   └── test_proj1.c
├── lib/                                ← Shared libs (Unity framework, utilities)
├── ca4b_cls_projs_f412dsc/
│   └── STM32CubeIDE/
│       └── proj1_src_test/             ← LINK .c FILES HERE IN CubeIDE
├── renode/
│   ├── proj1App_f412dsc.resc
│   └── proj1Unity_f412dsc.resc         ← Renode script for testing
└── ...
```

### Programming Tasks Summary

| PT | Description | Points | Key Requirement |
|----|-------------|--------|-----------------|
| PT1 | Fix `mp_swap` to use pointers | 10 | Change pass-by-value to pass-by-pointer |
| PT2 | Implement `mp_partial_sum` | 30 | Even-index via pointer, odd-index via array index |
| PT3 | Implement `mp_reverse_str` | 25 | Reverse string without `strlen`, return char count |
| PT4 | Write `test_mp_reverse_str` | 25 | Test "Hello." → ".olleH", verify return value = 6 |

> **Important:** PT4 (write test) should be done BEFORE PT3 (write function). This is TDD methodology.

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Place source files in `proj1_src/` and `proj1_test/` | CLAUDE CODE |
| Link `.c` files in CubeIDE `proj1_src_test/` | HUMAN |
| Build `Proj1Unity` configuration | HUMAN |
| Run Renode simulation | HUMAN |
| Implement `mp_swap` (PT1) | CLAUDE CODE |
| Implement `mp_partial_sum` (PT2) | CLAUDE CODE |
| Write `test_mp_reverse_str` (PT4) | CLAUDE CODE |
| Implement `mp_reverse_str` (PT3) | CLAUDE CODE |
| Take screenshots of test results | HUMAN |
| Create report PDF | HUMAN |
| Clean builds and zip project | HUMAN |

---

## Part A: Claude Code Automated Tasks

> These tasks are performed by Claude Code. Human verifies completion.

### A.1 Place Provided Source Files

Create the following files in `/opt/proj_mp/ca4b_cls_projs/proj1_src/`:

| File | Description |
|------|-------------|
| `_mp_main.c` | Entry point — dispatches to `mp_app()` or `mp_unity()` based on `UNIT_TEST` define |
| `proj1_app.c` | Main application (prints header, infinite loop) |
| `proj1_cfns.c` | C functions to implement: `mp_swap`, `mp_partial_sum`, `mp_reverse_str` |
| `proj1_fns.h` | Header with function prototypes |

Create the following file in `/opt/proj_mp/ca4b_cls_projs/proj1_test/`:

| File | Description |
|------|-------------|
| `test_proj1.c` | Unity test functions: `test_mp_swap`, `test_mp_partial_sum`, `test_mp_reverse_str`, `mp_unity` |

**Source code is provided in [`mp-ci4u--ptr-tdd-code.md`](./mp-ci4u--ptr-tdd-code.md)** (also in the PDF manual, Section 1.3, pages 3-5). The files should be created with the starter code exactly as shown.

### A.2 Implement PT1: Fix `mp_swap` (10 pts)

**File to modify:** `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_cfns.c`
**Also update:** `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_fns.h`

**What to change:**
- Change `mp_swap(int a, int b)` to `mp_swap(int *a, int *b)` (pass-by-pointer)
- Swap using dereferenced pointers: `*a`, `*b`
- Update prototype in header to match

**Also update the test call in:** `/opt/proj_mp/ca4b_cls_projs/proj1_test/test_proj1.c`
- Change `mp_swap(act[0], act[1])` to `mp_swap(&act[0], &act[1])`

### A.3 Implement PT2: `mp_partial_sum` (30 pts)

**File to modify:** `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_cfns.c`

**Requirements:**
- Prototype: `void mp_partial_sum(int *arr, int arr_size, int *result)`
- `result[0]` = sum of even-indexed elements (indices 0, 2, 4, ...) — **use pointer arithmetic**
- `result[1]` = sum of odd-indexed elements (indices 1, 3, 5, ...) — **use array indexing**
- Initialize both result elements to 0 before summing

### A.4 Implement PT4: Write `test_mp_reverse_str` (25 pts) — DO THIS BEFORE PT3

**File to modify:** `/opt/proj_mp/ca4b_cls_projs/proj1_test/test_proj1.c`

**Requirements:**
- Replace the placeholder `TEST_ASSERT_TRUE(1 > 2)` in `test_mp_reverse_str`
- Test case: `"Hello."` → `".olleH"`
- Use `TEST_ASSERT_EQUAL_INT(6, result)` to verify return value (number of chars reversed)
- Use `TEST_ASSERT_EQUAL_UINT8_ARRAY(expected, dst, 7)` to verify reversed string (7 = 6 chars + null terminator)

### A.5 Implement PT3: `mp_reverse_str` (25 pts)

**File to modify:** `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_cfns.c`

**Requirements:**
- Prototype: `int mp_reverse_str(char *src, char *dst)`
- Reverse characters of `src` into `dst`
- Do NOT use `strlen` or any built-in string functions
- Determine string length manually (walk to null terminator)
- Null-terminate `dst`
- Return the number of characters reversed (not counting null terminator)
- Reference examples in `/opt/proj_mp/ca4b_cls_projs/lib/mp_binary_str.c`

---

## Part B: Human Tasks (GUI Required)

> Follow steps exactly. Copy-paste commands where provided.

### B.1 Verify Base Project Builds (Prerequisite)

Before starting proj1, verify the base project is working:

1. Open **CubeIDE** (workspace: `/opt/proj_mp/`)
2. If `ca4b_cls_projs_f412dsc` is not imported:
   - **File → Import → General → Existing Projects into Workspace**
   - Browse to `/opt/proj_mp/ca4b_cls_projs/ca4b_cls_projs_f412dsc/STM32CubeIDE/`
   - Click **Finish**
3. Select build configuration **Proj0App**: Right-click project → **Build Configurations → Set Active → Proj0App**
4. Build: **Ctrl+B** (or click hammer icon)
5. If it builds successfully, you're ready for proj1

### B.2 Link Source Files in CubeIDE

After Claude Code places source files (Part A, Step A.1):

**In CubeIDE Project Explorer**, navigate to:
`ca4b_cls_projs_f412dsc` → `STM32CubeIDE` → `proj1_src_test`

Link each `.c` file using **New → File → Advanced → Link to file system**:

1. Right-click `proj1_src_test` folder
2. Select **New → File**
3. Click **Advanced >>**
4. Check **Link to file in the file system**
5. Click **Browse...** and navigate to the source file
6. Click **Open**, then **Finish**
7. Repeat for each file

**Files to link (5 total):**

| Source File (full path) | From Folder |
|-------------------------|-------------|
| `/opt/proj_mp/ca4b_cls_projs/proj1_src/_mp_main.c` | proj1_src |
| `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_app.c` | proj1_src |
| `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_cfns.c` | proj1_src |
| `/opt/proj_mp/ca4b_cls_projs/proj1_test/test_proj1.c` | proj1_test |

> **Note:** Do NOT link `proj1_fns.h` — header files are found via include paths, not linked into source folders.

### B.3 Build Proj1Unity

1. In CubeIDE, right-click `ca4b_cls_projs_f412dsc`
2. Select **Build Configurations → Set Active → Proj1Unity**
3. Build: **Ctrl+B**
4. Verify build succeeds (check Console output for errors)

> **Note:** Include paths for `proj1_src` (and all other projN_src folders) are already pre-configured in the `ca4b_cls_projs` base project. You should NOT need to add them manually. See [known_base_projects.md](../known_base_projects.md) for details.

### B.4 Run on Renode

**Terminal command to start Renode:**
```bash
cd /opt/proj_mp/ca4b_cls_projs/renode/
renode
```

**In Renode Monitor window, type:**
```
s @proj1Unity_f412dsc.resc
```

**Expected output in UART2 window:**
```
Running Proj1 unit test:
...
```

The Unity test framework will show PASS/FAIL for each test function.

### B.5 Iterative Build-Test Cycle

After each PT implementation by Claude Code:

1. **CubeIDE:** Rebuild (**Ctrl+B**)
2. **Renode:** Reset and rerun:
   - In Renode Monitor: `machine Reset` then `start`
   - OR close Renode and restart from terminal
3. Check UART2 output for test results
4. Take screenshot when test(s) pass

### B.6 Capture Artifacts

Take screenshots at each milestone:

| Artifact | When | What to Capture |
|----------|------|-----------------|
| A1a | PT1 passes | Renode/PuTTY showing `test_mp_swap` PASSED |
| A2a | PT2 passes | Renode/PuTTY showing `test_mp_partial_sum` PASSED |
| A3a | PT3+PT4 pass | Renode/PuTTY showing ALL 3 tests PASSED |
| A4a | PT3+PT4 pass | Same screenshot as A3a (or separate if preferred) |

**Save screenshots to:** `~/electrical_notes/content/cec_320/labs_and_projects/proj01/`

Suggested filenames: `a1a.png`, `a2a.png`, `a3a.png`, `a4a.png`

### B.7 Submission

**Report filename:** `ci4u-report-lastname-firstname.pdf`

**Report contents:** Brief narrative tying together Artifacts 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b.

**Project ZIP preparation:**

1. In CubeIDE: Right-click `ca4b_cls_projs_f412dsc` → **Build Configurations → Clean All**
2. Zip the project:

```bash
cd /opt/proj_mp/
zip -r ci4u-proj-lastname-firstname.zip ca4b_cls_projs/
```

**Zip filename:** `ci4u-proj-lastname-firstname.zip`

---

## Submission Checklist

- [ ] A1a: Screenshot — `test_mp_swap` PASSED
- [ ] A1b: Code — `mp_swap` function (in report)
- [ ] A2a: Screenshot — `test_mp_partial_sum` PASSED
- [ ] A2b: Code — `mp_partial_sum` function (in report)
- [ ] A3a: Screenshot — all tests PASSED (PT3 + PT4)
- [ ] A3b: Code — `mp_reverse_str` function (in report)
- [ ] A4a: Screenshot — all tests PASSED (can reuse A3a)
- [ ] A4b: Code — `test_mp_reverse_str` function (in report)
- [ ] PDF report: `ci4u-report-lastname-firstname.pdf`
- [ ] ZIP project: `ci4u-proj-lastname-firstname.zip` (builds cleaned)

