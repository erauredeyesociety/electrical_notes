# Lab 02 Findings: Debugging with CubeIDE for Fibonacci Number Generation

**Course:** CEC 320 / MP-CE5D
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab02_procedure.md](./lab02_procedure.md)
> - Original Manual: `mp-ce5d-lab2-cubeide-debug-4-fib-26-02.pdf`
> - Known Issues: [known_issues.md](../known_issues.md)

---

## Artifact Summary

| ID | Type | Description | Required For | File | Status |
|----|------|-------------|--------------|------|--------|
| A1 | Screenshot | Halted program at BP1 | DT 2 (5 pts) | `a1.png` | [ ] |
| A2 | Screenshot | `N[]` values in Variables view at BP2 | DT 3 (8 pts) | `a2.png` | [ ] |
| A3 | Screenshot | `fibonacci_arr1` in Expression view at BP3 | DT 4 (8 pts) | `a3.png` | [ ] |
| A4 | Screenshot | Full printed output (both arrays) at BP4 | PT 2 / DT output | `a4.png` | [ ] |
| A5 | Screenshot | Memory view of global arrays | DT 5 (8 pts) | `a5.png` | [ ] |
| A6 | Screenshot | Corrected output after bug fix | DT 6 (6 pts) | `a6.png` | [ ] |
| C1 | Code | `ce5d_debug_fib_app.c` (completed) | PT 1 + PT 2 + DT 6 | `c1.c` | [ ] |

---

## Screenshot Artifacts

### A1: Halted Program at BP1

**Required for:** DT 2 - Debugging in the Debug perspective (5 pts)

**What to capture:**

- CubeIDE Debug perspective with program halted at BP1
- The line `printf("\n\nRunning ce5d_debug_fib App ---\n");` should be highlighted
- Describe: How do you know the program has stopped at BP1?

**Screenshot:**

![A1 - Halted at BP1](./a1.png)

**File saved to:** `a1.png`

**Notes:**

---

### A2: Local Variable Inspection at BP2

**Required for:** DT 3 - Inspecting local variables (8 pts)

**What to capture:**

- Variables view showing `N[]` array values at BP2
- Values should show `{-1, 0, 1, 5, 21}` after initialization
- **Report must:** Determine the size of array `N` from the screenshot

**Screenshot:**

![A2 - N[] at BP2](./a2.png)

**File saved to:** `a2.png`

**Notes:**

---

### A3: Global Variable Inspection at BP3

**Required for:** DT 4 - Inspecting global variables (8 pts)

**What to capture:**

- Expression view showing `fibonacci_arr1` values at BP3
- After `mp_update_fib_array(fibonacci_arr1, 5)` has run
- Values should include first 6 Fibonacci numbers: `{0, 1, 1, 2, 3, 5, ...}`
- **Report must:** Determine the size of array `fibonacci_arr1` from the screenshot

**Screenshot:**

![A3 - fibonacci_arr1 at BP3](./a3.png)

**File saved to:** `a3.png`

**Notes:**

---

### A4: Full Printed Output at BP4

**Required for:** PT 2 + DT output verification

**What to capture:**

- PuTTY window showing full output: both array 1 (10 numbers) and array 2 (13 numbers)
- Note: Fibonacci number 10 will show **0** (this is the intentional bug)
- Output should match format: `Fibonacci number X: Y 0bBBBB_BBBB 0xHH`

**Screenshot:**

![A4 - Full output at BP4](./a4.png)

**File saved to:** `a4.png`

**Notes:**

---

### A5: Memory View Inspection

**Required for:** DT 5 - Inspecting the memory of global variables (8 pts)

**What to capture:**

- Memory view in Debug perspective
- Showing Unsigned Integer values at the address of `fibonacci_arr1`/`fibonacci_arr2`
- **Report must:** Estimate the size of `fibonacci_arr2` from the memory layout

**Screenshot:**

![A5 - Memory view](./a5.png)

**File saved to:** `a5.png`

**Notes:**

---

### A6: Corrected Output After Bug Fix

**Required for:** DT 6 - Fixing the bug(s) (6 pts)

**What to capture:**

- PuTTY output showing corrected Fibonacci numbers
- Fibonacci number 10 should now be **55** (was 0 before fix)
- All values should match expected Fibonacci sequence

**Screenshot:**

![A6 - Corrected output](./a6.png)

**File saved to:** `a6.png`

**Notes:**

---

## Code Snippet Artifacts

### C1: ce5d_debug_fib_app.c

**Required for:** PT 1 (20 pts) + PT 2 (10 pts) + DT 6 (6 pts)

**File path:** `/opt/proj_mp/ce5d_debug_fib/src/ce5d_debug_fib_app.c`

**Artifact file:** [c1.c](./c1.c)

**Key sections:**

- `mp_update_fib_array` function (PT 1)
- `mp_app` for-loop sections (PT 2)
- Array declarations with corrected sizes (DT 6 bug fix)

**Code:**

```c
// To be populated with final code after all tasks complete
```

**Notes:**

---

## Submission Checklist

### PDF Report

**Filename:** `ce5d-report-lastname-firstname.pdf`

**Required contents:**

- [ ] A1: Screenshot of halted program at BP1 + description of how you know it stopped
- [ ] A2: Screenshot of `N[]` at BP2 + determine size of array `N`
- [ ] A3: Screenshot of `fibonacci_arr1` at BP3 + determine size of `fibonacci_arr1`
- [ ] A4: Screenshot of full printed output
- [ ] A5: Screenshot of Memory view + estimate size of `fibonacci_arr2`
- [ ] A6: Screenshot of corrected output after bug fix

### Project ZIP

**Filename:** `ce5d-proj-lastname-firstname.zip`

**Before zipping:**

1. In CubeIDE: **Project -> Clean** to remove build artifacts
2. Verify no `Debug/` or `Release/` build artifacts remain

**Project location:** `/opt/proj_mp/ce5d_debug_fib/`

**Zip command:**

```bash
cd /opt/proj_mp/
zip -r ce5d-proj-lastname-firstname.zip ce5d_debug_fib/
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | File | Description | Analysis Required |
|----------------|-------------|------|-------------|-------------------|
| Screenshot 1 | A1 | `a1.png` | Halted at BP1 | Describe how you know it stopped |
| Screenshot 2 | A2 | `a2.png` | `N[]` at BP2 | Determine size of `N` |
| Screenshot 3 | A3 | `a3.png` | `fibonacci_arr1` at BP3 | Determine size of `fibonacci_arr1` |
| Screenshot 4 | A4 | `a4.png` | Full output at BP4 | - |
| Screenshot 5 | A5 | `a5.png` | Memory view | Estimate size of `fibonacci_arr2` |
| Screenshot 6 | A6 | `a6.png` | Corrected output | - |
| Source Code | C1 | `c1.c` | `ce5d_debug_fib_app.c` | - |

---

## Notes and Observations

### Issues Encountered

- **Missing `_mp_main.c` link:** Initial procedure omitted `_mp_main.c` from the file linking list, causing `undefined reference to 'mp_main'` linker error. Fixed by linking `/opt/proj_mp/ce5d_debug_fib/src/_mp_main.c` to `lib_src`. See [known_issues.md](../known_issues.md).

### Solutions Applied

### Questions for TA/Instructor
