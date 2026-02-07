# Proj 01 Findings: Pointers and Unit Test

**Course:** CEC 320 - Microprocessors
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [proj01_procedure.md](./proj01_procedure.md)
> - Original Manual: `mp-ci4u-proj1-ptr-tdd-2026-01.pdf`
> - Source Code: [`mp-ci4u--ptr-tdd-code.md`](./mp-ci4u--ptr-tdd-code.md)

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1a | Screenshot | `test_mp_swap` PASSED output | PT1 (10 pts) | [x] |
| A1b | Code | Finished `mp_swap` function | PT1 (10 pts) | [x] |
| A2a | Screenshot | `test_mp_partial_sum` PASSED output | PT2 (30 pts) | [x] |
| A2b | Code | Finished `mp_partial_sum` function | PT2 (30 pts) | [x] |
| A3a | Screenshot | All 3 tests PASSED (PT3+PT4 complete) | PT3 (25 pts) | [x] |
| A3b | Code | Finished `mp_reverse_str` function | PT3 (25 pts) | [x] |
| A4a | Screenshot | All tests PASSED (same run as A3a) | PT4 (25 pts) | [x] |
| A4b | Code | Finished `test_mp_reverse_str` function | PT4 (25 pts) | [x] |

---

## Screenshot Artifacts

### A1a: test_mp_swap PASSED

**Required for:** PT1 - Swapping variables using pointers (10 pts)

**What to capture:**
- Renode UART2 window (or PuTTY) showing Unity test output
- `test_mp_swap` should show PASS
- Other tests may still show FAIL at this stage

**Screenshot:** `a1a.png` — Shows 1 pass, 2 fail (only mp_swap implemented at this stage)

**File saved to:** `./a1a.png`

**Notes:** Progressive result confirming PT1 complete before moving to PT2.


---

### A2a: test_mp_partial_sum PASSED

**Required for:** PT2 - Summing odd and even-indexed elements (30 pts)

**What to capture:**
- Renode UART2 window showing Unity test output
- `test_mp_partial_sum` should show PASS
- `test_mp_swap` should also show PASS

**Screenshot:** `a2a.png` — Shows 2 pass, 1 fail (mp_swap + mp_partial_sum implemented)

**File saved to:** `./a2a.png`

**Notes:** Progressive result confirming PT2 complete before moving to PT4/PT3.


---

### A3a: All Tests PASSED (PT3 + PT4)

**Required for:** PT3 - Reversing a string (25 pts)

**What to capture:**
- Renode UART2 window showing Unity test output
- ALL 3 tests should show PASS: `test_mp_swap`, `test_mp_partial_sum`, `test_mp_reverse_str`
- Unity summary should show "3 Tests 0 Failures 0 Ignored"

**Screenshot:** `a3a_a4a.png` — Shows 3 pass, 0 fail (all functions implemented)

**File saved to:** `./a3a_a4a.png`

**Notes:** All 3 Unity tests passing. Confirms mp_reverse_str works correctly.


---

### A4a: All Tests PASSED (PT4 verification)

**Required for:** PT4 - Test the string-reversing function (25 pts)

**What to capture:**
- Same test run as A3a (can reuse the same screenshot)
- Shows that the test function written in PT4 correctly validates PT3's implementation

**Screenshot:** `a3a_a4a.png` — Same run as A3a (PT4 test validates PT3 implementation)

**File saved to:** `./a3a_a4a.png`

**Notes:** Same screenshot as A3a. The test_mp_reverse_str function (PT4) correctly validates the mp_reverse_str function (PT3).


---

## Code Snippet Artifacts

### A1b: mp_swap function

**Required for:** PT1 - Swapping variables (10 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_cfns.c`

**Code:**
```c
void mp_swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

**Notes:** Modified from pass-by-value to pass-by-reference using int pointers.


---

### A2b: mp_partial_sum function

**Required for:** PT2 - Summing odd and even-indexed elements (30 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_cfns.c`

**Code:**
```c
void mp_partial_sum(int *arr, int arr_size, int *result) {
    result[0] = 0;
    result[1] = 0;

    for (int i = 0; i < arr_size; i++) {
        if (i % 2 == 0) {
            result[0] += *(arr + i);
        } else {
            result[1] += arr[i];
        }
    }
}
```

**Notes:** Uses pointer arithmetic `*(arr + i)` for even-indexed and array indexing `arr[i]` for odd-indexed as required.


---

### A3b: mp_reverse_str function

**Required for:** PT3 - Reversing a string (25 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj1_src/proj1_cfns.c`

**Code:**
```c
int mp_reverse_str(char *src, char *dst) {
    int len = 0;
    char *p = src;

    while (*p != '\0') {
        len++;
        p++;
    }

    for (int i = 0; i < len; i++) {
        dst[i] = src[len - 1 - i];
    }
    dst[len] = '\0';

    return len;
}
```

**Notes:** Determines string length without strlen, reverses into dst, null-terminates, returns character count.


---

### A4b: test_mp_reverse_str function

**Required for:** PT4 - Test the string-reversing function (25 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj1_test/test_proj1.c`

**Code:**
```c
void test_mp_reverse_str(void) {
    char src[] = "Hello.";
    char dst[7];
    char exp[] = ".olleH";

    int result = mp_reverse_str(src, dst);

    TEST_ASSERT_EQUAL_INT(6, result);
    TEST_ASSERT_EQUAL_UINT8_ARRAY(exp, dst, 7);
}
```

**Notes:** TDD — test written before mp_reverse_str implementation. Verifies both reversed string content and character count.


---

## Submission Checklist

### PDF Report

**Filename:** `ci4u-report-lastname-firstname.pdf`

**Required contents:**
- [x] A1a: Screenshot of `test_mp_swap` PASSED
- [x] A1b: Code of `mp_swap` function
- [x] A2a: Screenshot of `test_mp_partial_sum` PASSED
- [x] A2b: Code of `mp_partial_sum` function
- [x] A3a: Screenshot of all tests PASSED
- [x] A3b: Code of `mp_reverse_str` function
- [x] A4a: Screenshot of all tests PASSED (same as A3a)
- [x] A4b: Code of `test_mp_reverse_str` function
- [x] Brief narrative tying all artifacts together

### Project ZIP

**Filename:** `ci4u-proj-lastname-firstname.zip`

**Before zipping:**
1. In CubeIDE: Right-click `ca4b_cls_projs_f412dsc` → **Build Configurations → Clean All**
2. Verify no build artifact folders remain (Proj1Unity/, Proj1App/, etc.)

**Project location:** `/opt/proj_mp/ca4b_cls_projs/`

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r ci4u-proj-lastname-firstname.zip ca4b_cls_projs/
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | A1a | Screenshot: `test_mp_swap` PASSED |
| Code Snippets and Screenshots | A1b | Code: `mp_swap` function |
| Code Snippets and Screenshots | A2a | Screenshot: `test_mp_partial_sum` PASSED |
| Code Snippets and Screenshots | A2b | Code: `mp_partial_sum` function |
| Code Snippets and Screenshots | A3a | Screenshot: all tests PASSED |
| Code Snippets and Screenshots | A3b | Code: `mp_reverse_str` function |
| Code Snippets and Screenshots | A4a | Screenshot: all tests PASSED |
| Code Snippets and Screenshots | A4b | Code: `test_mp_reverse_str` function |

---

## Notes and Observations

### Issues Encountered

- CubeIDE "Clean All" fails with: `proj0_src_test/subdir.mk:34: *** target pattern contains no '%'. Stop.` — pre-existing makefile issue in ca4b_cls_projs.

### Solutions Applied

- Manually removed build artifacts (`*.o`, `*.d`, `*.elf`, `*.map`, `*.list`, `*.su`) before zipping the project.



### Questions for TA/Instructor


