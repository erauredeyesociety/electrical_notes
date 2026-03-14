# Proj 04 Findings: Half Precision IEEE 754 Numbers

**Course:** CEC 320
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [proj04_procedure.md](./proj04_procedure.md)
> - Original Manual: `mp-ee4u--proj4-half-precision-ieee754-26-03.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | All 5 Unity tests passing | Programming tasks (80 pts) | [x] |
| A2 | Screenshot | App running result | Running the main App (10 pts) | [x] |
| C1 | Code | `ee4u_half_precision_ieee754_fns.c` — encoding + decoding functions | Programming tasks (80 pts) | [x] |

---

## Screenshot Artifacts

### A1: Unity Test Results — All 5 Tests Passing

**Required for:** Section 4.2 - Programming tasks (80 pts)

**What to capture:**
- Renode UART2 window showing Unity test output
- All 5 tests PASS with 0 failures
- Tests: encoding_a_too_big_num, encoding_a_normal_num, encoding_a_tiny_num, decoding_a_normal_num, decoding_a_tiny_num

**File saved to:** `./a1.png`

---

### A2: App Running Result

**Required for:** Section 4.3 - Running the main App (10 pts)

**What to capture:**
- Renode UART2 window showing App output
- Encoded field printouts (Sign, Expt, Frac) for 3 numbers
- Decoded value printouts for 2 numbers

**Expected output:**
```
ee4u Half Precision IEEE 754 App-----------
Sign = 0, Expt =  31, Frac = 0x000000
Sign = 1, Expt =  19, Frac = 0x0003F8
Sign = 0, Expt =   0, Frac = 0x000040
Value = -31.875000
Value = 1.000000
```

**File saved to:** `./a2.png`

---

## Code Snippet Artifacts

### C1: ee4u_half_precision_ieee754_fns.c

**Required for:** Section 4.2 - Programming tasks (80 pts)

**File path:** `/opt/proj_mp/ee4u_half_precision_ieee754/src/ee4u_half_precision_ieee754_fns.c`

**Code:** [c1.c](./c1.c)

---

## Submission Checklist

### PDF Report

**Filename:** `ee4u-proj4-report-lastname-firstname.pdf`

**Required contents:**
- [ ] C1: Code for both encoding and decoding functions
- [ ] A1: Screenshot of all 5 tests passing
- [ ] A2: Screenshot of App running result

### Project ZIP

**Filename:** `ee4u-proj4-lastname-firstname.zip`

**Before zipping:**
1. In CubeIDE: Right-click project → **Build Configurations → Clean All**
2. Verify no Debug/Unity/Application build artifacts remain

**Project location:** `/opt/proj_mp/ee4u_half_precision_ieee754/`

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r ee4u-proj4-lastname-firstname.zip ee4u_half_precision_ieee754/
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | C1 | Encoding + decoding functions |
| Code Snippets and Screenshots | A1 | All 5 Unity tests passing |
| Code Snippets and Screenshots | A2 | App running result |

---

## Notes and Observations

### Issues Encountered

- `DebugSoln` config produces makefile error during Clean All (`target pattern contains no '%'`). This is the instructor's solution config — does not affect student builds.
- No "Application" build config exists in the project. The App is built using the **Debug** config (which has no `UNIT_TEST` define).

### Solutions Applied

- Used **Debug** config for App mode and **Unity** config for test mode.
- Ignored `DebugSoln` clean error — Debug and Unity cleaned successfully.
