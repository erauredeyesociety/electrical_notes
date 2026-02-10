# Proj 02 Findings: Mocking GPIO and BSRR

**Course:** CEC 320 / MP-DE4U
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [proj02_procedure.md](./proj02_procedure.md)
> - Original Manual: `mp-de4u-proj2-mocking-gpio-n-bsrr-26-02.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Tests 1,2 PASS after PT 1 | Incremental verification | [ ] |
| A2 | Screenshot | Tests 1-7 PASS after PT 2 | Incremental verification | [ ] |
| A3 | Screenshot | All 8 tests PASS after PT 3 | **Submission** (10 pts) | [ ] |
| C1 | Code | `mp_mock_write_idr()` function | PT 1 (15 pts) | [ ] |
| C2 | Code | `mp_mock_odr_update_with_bsrr()` function | PT 2 (45 pts) | [ ] |
| C3 | Code | `test_mp_gpio_toggle_pins_func()` function | PT 3 (25 pts) | [ ] |

---

## Screenshot Artifacts

### A1: Tests 1,2 PASS After PT 1

**Required for:** PT 1 — Mocking the updating of the IDR (15 pts) — incremental verification

**What to capture:**
- UART2 window in Renode showing Unity test output
- Tests 1 (test_read_idr_via_hal_func) and 2 (test_read_idr_directly) PASS
- Remaining tests may FAIL (expected at this stage)

**Screenshot:**
```
[Paste screenshot or drag image file here]
```

**File saved to:** ____________________

**Notes:**


---

### A2: Tests 1-7 PASS After PT 2

**Required for:** PT 2 — Mocking the updating of ODR using BSRR (45 pts) — incremental verification

**What to capture:**
- UART2 window in Renode showing Unity test output
- Tests 1-7 all PASS
- Test 8 (test_mp_gpio_toggle_pins_func) may still FAIL

**Screenshot:**
```
[Paste screenshot or drag image file here]
```

**File saved to:** ____________________

**Notes:**


---

### A3: All 8 Tests PASS (Submission Required)

**Required for:** Submission (10 pts) — must show all tests passing including the newly created Test 8

**What to capture:**
- UART2 window in Renode showing Unity test output
- ALL 8 tests PASS
- Summary line: "8 Tests 0 Failures 0 Ignored"

**Screenshot:**
```
[Paste screenshot or drag image file here]
```

**File saved to:** ____________________

**Notes:**


---

## Code Snippet Artifacts

### C1: `mp_mock_write_idr()`

**Required for:** PT 1 — Mocking the updating of the IDR (15 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_utils_4_gpio_regs.c`

**Code:**
```c
// To be filled after implementation
```

**Notes:**


---

### C2: `mp_mock_odr_update_with_bsrr()`

**Required for:** PT 2 — Mocking the updating of ODR using BSRR (45 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_odr_update_with_bsrr_brr.c`

**Code:**
```c
// To be filled after implementation
```

**Notes:**


---

### C3: `test_mp_gpio_toggle_pins_func()`

**Required for:** PT 3 — Testing a revised GPIO toggle function (25 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj2_test/test_de4u_mocking_gpio_n_bsrr.c`

**Code:**
```c
// To be filled after implementation
```

**Notes:**


---

## Submission Checklist

### PDF Report

**Filename:** `de4u-report-lastname-firstname.pdf`

**Required contents:**
- [ ] C1: `mp_mock_write_idr()` code
- [ ] C2: `mp_mock_odr_update_with_bsrr()` code
- [ ] C3: `test_mp_gpio_toggle_pins_func()` code
- [ ] A3: Screenshot of all 8 tests passing

### Project ZIP

**Filename:** `de4u-lastname-firstname.zip`

**Before zipping:**
1. In CubeIDE: Right-click project → **Build Configurations → Clean All**
2. Verify no build artifacts remain (especially important since multiple project builds exist in ca4b_cls_projs)

**Project location:** `/opt/proj_mp/ca4b_cls_projs/`

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r de4u-lastname-firstname.zip ca4b_cls_projs/
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | C1 | `mp_mock_write_idr()` function |
| Code Snippets and Screenshots | C2 | `mp_mock_odr_update_with_bsrr()` function |
| Code Snippets and Screenshots | C3 | `test_mp_gpio_toggle_pins_func()` function |
| Code Snippets and Screenshots | A3 | All 8 tests passing screenshot |

---

## Notes and Observations

### Issues Encountered


### Solutions Applied


### Questions for TA/Instructor

