# Proj 03 Findings: Fixed-Point Arithmetic Operations

**Course:** CEC 320 / MP-EE4U
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [proj03_procedure.md](./proj03_procedure.md)
> - Original Manual: `mp-ee4u-proj3-fixed-point-operations-26-02.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Renode: test_mp_uq_and_q_mn_decoding passes (1/3) | PT1 (20 pts) | [x] |
| A2 | Screenshot | Renode: encoding test also passes (2/3) | PT2 (20 pts) | [x] |
| A3 | Screenshot | Renode: all 3 tests pass (3/3) | PT3 (20 pts) | [x] |
| A4 | Screenshot | Renode: App output with Q15 results | PT4 (20 pts) | [x] |
| C1 | Code | 3 functions in `ee4u_fixed_point_fns.c` | Submission | [x] |
| C2 | Code | App code in `ee4u_fixed_point_operations_app.c` | Submission | [x] |

---

## Screenshot Artifacts

### A1: Unit Test — Decoding Function Passes

**Required for:** PT1 — mp_uq_and_q_mn_decoding (20 pts)

**What to capture:**
- Renode UART output showing Unity test results
- test_mp_uq_and_q_mn_decoding: PASS
- test_mp_uq_and_q_mn_encoding: FAIL
- test_mp_q_mn_multiplication: FAIL
- Summary: 3 Tests, 2 Failures

**File saved to:** [a1.png](./a1.png)

---

### A2: Unit Test — Encoding Function Also Passes

**Required for:** PT2 — mp_uq_and_q_mn_encoding (20 pts)

**What to capture:**
- Renode UART output showing Unity test results
- test_mp_uq_and_q_mn_decoding: PASS
- test_mp_uq_and_q_mn_encoding: PASS
- test_mp_q_mn_multiplication: FAIL
- Summary: 3 Tests, 1 Failure

**File saved to:** [a2.png](./a2.png)

---

### A3: Unit Test — All Tests Pass

**Required for:** PT3 — mp_q_mn_multiplication (20 pts)

**What to capture:**
- Renode UART output showing all tests pass
- Summary: 3 Tests, 0 Failures

**File saved to:** [a3.png](./a3.png)

---

### A4: App Output — Q15 Operations

**Required for:** PT4 — Main App (20 pts)

**What to capture:**
- Renode UART output showing:
  - I1, I2, I3 encoded values in hex (0x%04X format)
  - fA (Q15 multiplication result) in %8.7f format
  - fA_float (direct float multiplication) in %8.7f format

**Expected values (Q15: m=0, n=15):**
- f1=0.5, f2=0.25, f3=-0.625
- I1=0x4000, I2=0x2000, I3=0xB000
- fA = f1 × f2 × f3 via Q15 multiplication
- fA_float = 0.5 × 0.25 × (-0.625) = -0.078125

**File saved to:** [a4.png](./a4.png)

---

## Code Snippet Artifacts

### C1: Three Functions in `ee4u_fixed_point_fns.c`

**Required for:** Submission — "The code you wrote for the functions to pass the tests"

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj3_src/ee4u_fixed_point_fns.c`

**Functions implemented:**
1. `mp_uq_and_q_mn_decoding()` — decode UQm.n/Qm.n to float
2. `mp_uq_and_q_mn_encoding()` — encode float to UQm.n/Qm.n
3. `mp_q_mn_multiplication()` — Qm.n multiplication

**Code:** See [c1.c](./c1.c)

**Artifact file:** [c1.c](./c1.c)

---

### C2: Main App in `ee4u_fixed_point_operations_app.c`

**Required for:** Submission — App code

**File path:** `/opt/proj_mp/ca4b_cls_projs/proj3_src/ee4u_fixed_point_operations_app.c`

**Code:** See [c2.c](./c2.c)

**Artifact file:** [c2.c](./c2.c)

---

## Submission Checklist

### PDF Report

**Filename:** `ee4u-proj3-report-lastname-firstname.pdf`

**Required contents:**
- [x] C1: Code for the 3 functions
- [x] A3: Screenshot showing all tests passed
- [x] A4: Screenshot showing App running result

### Project ZIP

**Filename:** `ee4u-proj3-lastname-firstname.zip`

**Before zipping:**
1. In CubeIDE: Right-click project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/ca4b_cls_projs/`

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r ee4u-proj3-lastname-firstname.zip ca4b_cls_projs/
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | C1 | 3 functions in ee4u_fixed_point_fns.c |
| Code Snippets and Screenshots | C2 | App code in ee4u_fixed_point_operations_app.c |
| Code Snippets and Screenshots | A3 | All tests passing |
| Code Snippets and Screenshots | A4 | App output |

---

## Notes and Observations

### Issues Encountered

- **Solution files overriding weak stubs:** The `*_soln.c` files were linked in the project and their strong implementations overrode the weak stubs, causing all tests to pass before any code was written. Fixed by excluding `ee4u_fixed_point_fns_soln.c` and `ee4u_fixed_point_operations_app_soln.c` from build via Resource Configurations.
- **Encoding rounding error:** Initial `(int32_t)` cast truncates instead of rounding, causing off-by-one errors in test values. Resolved by using `lrint()` from `<math.h>` for proper round-to-nearest.
- **Proj3App .elf not found:** Attempted to run Proj3App Renode script before building with the Proj3App configuration. Fixed by switching build config to Proj3App and rebuilding.

### Questions for TA/Instructor

