# Lab 05 Findings: Pseudo Random Number Generation in C

**Course:** CEC 320 / MP-DK5U
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab05_procedure.md](./lab05_procedure.md)
> - Original Manual: `mp-dk5u-lab5-prn-generation-in-c-26-03.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A3 | Screenshot | Renode: all 6 tests pass (F412dsc) | PT1-PT3 (65 pts) | [x] |
| A4 | Screenshot | Putty: all 6 tests pass on G431n32 real board | Submission | [x] |
| A5 | Screenshot | Putty: App running on G431n32 with PSC input | PT4 (5 pts) | [x] |
| C1 | Code | 3 functions in `mp_prn_c.c` | Submission | [x] |

---

## Screenshot Artifacts

### A3: Unit Test — All Tests Pass (F412dsc via Renode)

**Required for:** PT1-PT3 — all 3 functions (65 pts)

**What to capture:**

- Renode UART output showing all 6 tests pass on F412dsc
- Summary: 6 Tests, 0 Failures, 0 Ignored

**File saved to:** [a3.png](./a3.png)

---

### A4: Unit Test — All Tests Pass (G431n32 via Real Board)

**Required for:** Submission — Unity build on both boards

**What to capture:**

- Putty serial output showing all 6 tests pass on G431n32 real board
- Summary: 6 Tests, 0 Failures

**File saved to:** [a4.png](./a4.png)

---

### A5: App Output — PRN-Driven LED Blinking on G431n32

**Required for:** PT4 — App (5 pts)

**What to capture:**

- Putty serial output from G431n32 running Debug (App) build
- Shows app start message and PSC prompt
- At least one PSC value entered

**Note:** This App only works on real hardware, NOT Renode.

**File saved to:** [a5.png](./a5.png)

---

## Code Snippet Artifacts

### C1: Three Functions in `mp_prn_c.c`

**Required for:** Submission — "Code snippets of the three functions you have programmed"

**File path:** `/opt/proj_mp/dk5u_prn_generation_in_c/src/mp_prn_c.c`

**Functions implemented:**

1. `mp_prn_ini_c()` — initialize PRN register and reg_mask
2. `mp_prn_tap_mask_c()` — build tap mask from polynomial
3. `mp_prn_gen_c()` — generate PRN output bit and update register

**Code:** See [c1.c](./c1.c)

**Artifact file:** [c1.c](./c1.c)

---

## Submission Checklist

### PDF Report

**Filename:** `dk5u-report-lastname-firstname.pdf`

**Required contents:**

- [x] C1: Code snippets of the three functions
- [x] A3: Screenshot showing all tests passed (F412dsc)
- [x] A4: Screenshot showing all tests passed (G431n32)
- [x] A5: Screenshot of App running on G431n32

### Project ZIP

**Filename:** `dk5u-proj-lastname-firstname.zip`

**Before zipping:**

1. In CubeIDE: Right-click each project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/dk5u_prn_generation_in_c/`

**Zip command:**

```bash
cd /opt/proj_mp/
zip -r dk5u-proj-lastname-firstname.zip dk5u_prn_generation_in_c/
```

**Note:** Team submission allowed (2 students). List both names.

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | C1 | 3 functions in mp_prn_c.c |
| Code Snippets and Screenshots | A3 | All tests pass (F412dsc) |
| Code Snippets and Screenshots | A4 | All tests pass (G431n32) |
| Code Snippets and Screenshots | A5 | App on G431n32 |

---

## Notes and Observations

### Issues Encountered

- No Renode script exists for G431n32 — Unity tests for that board must run on real hardware via Run As / Debug As
- All 3 functions were implemented simultaneously, so incremental screenshots (A1, A2) were not captured; all tests passed on first run

### Questions for TA/Instructor

