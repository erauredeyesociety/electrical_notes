# Proj 02 Findings: Mocking GPIO and BSRR

**Course:** CEC 320 / MP-DE4U
**Student:** ____________________
**Date:** 2026-02-10

> **Related Documents:**
> - Procedure: [proj02_procedure.md](./proj02_procedure.md)
> - Original Manual: `mp-de4u-proj2-mocking-gpio-n-bsrr-26-02.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Tests 1,2 PASS after PT 1 (4 failures) | Incremental verification | [x] |
| A3 | Screenshot | All 8 tests PASS after PT 3 | **Submission** (10 pts) | [x] |
| C1 | Code | `mp_mock_write_idr()` function | PT 1 (15 pts) | [x] |
| C2 | Code | `mp_mock_odr_update_with_bsrr()` function | PT 2 (45 pts) | [x] |
| C3 | Code | `test_mp_gpio_toggle_pins_func()` function | PT 3 (25 pts) | [x] |

**Note:** A2 (after PT 2) was skipped — the weak empty Test 8 stub passes vacuously with no assertions, making the output identical to A3 (8 Tests 0 Failures). A2 was incremental verification only, not required for submission.

---

## Screenshot Artifacts

### A1: Tests 1,2 PASS After PT 1

**Required for:** PT 1 — Mocking the updating of the IDR (15 pts) — incremental verification

**What to capture:**
- UART2 window in Renode showing Unity test output
- Tests 1 (test_read_idr_via_hal_func) and 2 (test_read_idr_directly) PASS
- 4 failures from tests requiring PT 2 implementation

**File saved to:** [a1.png](./a1.png)

---

### A3: All 8 Tests PASS (Submission Required)

**Required for:** Submission (10 pts) — must show all tests passing including the newly created Test 8

**What to capture:**
- UART2 window in Renode showing Unity test output
- ALL 8 tests PASS
- Summary line: "8 Tests 0 Failures 0 Ignored"

**File saved to:** [a3.png](./a3.png)

---

## Code Snippet Artifacts

### C1: `mp_mock_write_idr()`

**Required for:** PT 1 — Mocking the updating of the IDR (15 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_utils_4_gpio_regs.c`

**Code:**
```c
void mp_mock_write_idr(GPIO_TypeDef *GPIOx, uint32_t idr) {
    GPIOx->IDR = idr;
}
```

**Artifact file:** [c1.c](./c1.c)

---

### C2: `mp_mock_odr_update_with_bsrr()`

**Required for:** PT 2 — Mocking the updating of ODR using BSRR (45 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_odr_update_with_bsrr_brr.c`

**Code:**
```c
void mp_mock_odr_update_with_bsrr(GPIO_TypeDef *GPIOx) {
    if (GPIOx->BSRR != 0) {
        GPIOx->ODR |= (GPIOx->BSRR & 0xFFFF);
        GPIOx->ODR &= ~(GPIOx->BSRR >> 16);
        GPIOx->BSRR = 0;
    }
}
```

**Artifact file:** [c2.c](./c2.c)

---

### C3: `test_mp_gpio_toggle_pins_func()`

**Required for:** PT 3 — Testing a revised GPIO toggle function (25 pts)

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj2_test/test_de4u_mocking_gpio_n_bsrr.c`

**Code:**
```c
void test_mp_gpio_toggle_pins_func(void) {
    uint32_t act, exp = 0xABCD, odr = 0xAB3D;
    GPIOx->ODR = odr;
    mp_GPIO_TogglePinS(GPIOx, (15U<<4));
    act = mp_mock_read_odr(GPIOx);
    TEST_ASSERT_EQUAL_UINT32(exp, act);
}
```

**Artifact file:** [c3.c](./c3.c)

---

## Submission Checklist

### PDF Report

**Filename:** `de4u-report-lastname-firstname.pdf`

**Required contents:**
- [x] C1: `mp_mock_write_idr()` code
- [x] C2: `mp_mock_odr_update_with_bsrr()` code
- [x] C3: `test_mp_gpio_toggle_pins_func()` code
- [x] A3: Screenshot of all 8 tests passing

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

- A2 screenshot (after PT 2) was indistinguishable from A3 because the weak empty Test 8 stub has no assertions, so Unity counts it as a pass. Both show "8 Tests 0 Failures."

### Solutions Applied

- Skipped A2 as it was incremental verification only. A1 (4 failures) and A3 (0 failures) sufficiently demonstrate incremental progress.
