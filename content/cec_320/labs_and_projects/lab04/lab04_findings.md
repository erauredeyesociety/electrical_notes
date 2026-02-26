# Lab 04 Findings: Logic Analyzer Based on Direct GPIO Register Access

**Course:** CEC 320 / MP-DE5D
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab04_procedure.md](./lab04_procedure.md)
> - Original Manual: `lab4-de5d-logic-analyzer-with-gpio-26-02.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | PuTTY output WITHOUT Fnc6 (CH1 all 0s) | Submission (10 pts) | [ ] |
| A2 | Screenshot | PuTTY output WITH Fnc6 (CH1 all 1s) | Submission (10 pts) | [ ] |
| A3 | Text/Code | Description of uint8_t sample packing | Submission (10 pts) | [ ] |
| C1 | Code | Modified `de5d_logic_analyzer_fns.c` | Submission (10 pts) | [ ] |

---

## Screenshot Artifacts

### A1: PuTTY Output Without Fnc6

**Required for:** Section 4.3.2.3 — Print out LA sample results (part of 20 pts)

**What to capture:**
- PuTTY terminal window showing full output
- "Sampling data for you...just a moment."
- CH1: all 0s (PA0 reads low due to pull-down, Fnc6 not pressed)
- CH2 and CH3: alternating patterns (opposite each other, toggling every 2 seconds)

**Expected output pattern:**
```
Sampling data for you...just a moment.
CH1: 00000000000000000000000000000000000000000000000000
CH2: 11111111111100000000000000000000011111111111111111
CH3: 00000000000001111111111111111111100000000000000000
```

**File saved to:** ____________________

---

### A2: PuTTY Output With Fnc6

**Required for:** Section 4.3.2.3 — Print out LA sample results (part of 20 pts)

**What to capture:**
- PuTTY terminal window showing full output
- CH1: all 1s (PA0 reads high because Fnc6 connects PA0 to PA10's output)
- CH2 and CH3: same alternating pattern as A1

**Expected output pattern:**
```
Sampling data for you...just a moment.
CH1: 11111111111111111111111111111111111111111111111111
CH2: 11111111111100000000000000000000011111111111111111
CH3: 00000000000001111111111111111111100000000000000000
```

**File saved to:** ____________________

---

## Text/Code Artifacts

### A3: Description of uint8_t Sample Packing

**Required for:** Section 4.3.2.2 — "provide a description about how you performed the saving of the samples" (part of 40 pts)

**Description:**
```
[To be filled — explain the bitwise packing approach:
- CH1 (PA0) → Bit 0: extracted via (GPIOA->IDR >> Pin0_pos) & 1
- CH2 (PA10) → Bit 1: extracted via (GPIOA->ODR >> Pin10_pos) & 1
- CH3 (PB8) → Bit 2: extracted via (GPIOB->ODR >> Pin8_pos) & 1
- Packed: logic_samples[i] = (bit2 << 2) | (bit1 << 1) | bit0
- Each uint8_t stores 3 channel states, using only bits [2:0]]
```

---

## Code Snippet Artifacts

### C1: Modified `de5d_logic_analyzer_fns.c`

**Required for:** Submission — "Include the code you modified in de5d_logic_analyzer_fns.c"

**File path:** `/opt/proj_mp/de5d_logic_analyzer/src/de5d_logic_analyzer_fns.c`

**Functions implemented:**
1. `mp_init_set_LED1_reset_LED4()` — sets LED1 on (PA10), LED4 off (PB8) via BSRR
2. `mp_read_logic_samples()` — samples 3 channels into uint8_t array
3. `mp_print_logic_samples()` — prints channel data as binary strings

**Code:**
```c
// To be filled after implementation
```

**Artifact file:** [c1.c](./c1.c)

---

## Submission Checklist

### PDF Report

**Filename:** `de5d-report-lastname-firstname.pdf`

**Required contents:**
- [ ] A1: Screenshot without Fnc6
- [ ] A2: Screenshot with Fnc6
- [ ] A3: Description of uint8_t sample packing
- [ ] C1: Modified `de5d_logic_analyzer_fns.c` code

### Project ZIP

**Filename:** `de5d-proj-lastname-firstname.zip`

**Before zipping:**
1. In CubeIDE: Right-click project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/de5d_logic_analyzer/`

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r de5d-proj-lastname-firstname.zip de5d_logic_analyzer/
```

**Note:** Team submission allowed — list both members' names on report.

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | A1 | PuTTY output without Fnc6 |
| Code Snippets and Screenshots | A2 | PuTTY output with Fnc6 |
| Code Snippets and Screenshots | A3 | uint8_t packing description |
| Code Snippets and Screenshots | C1 | Modified `de5d_logic_analyzer_fns.c` |

---

## Notes and Observations

### Issues Encountered

- Reference project `de2f_direct_gpio_reg_access` not found on system — needs to be obtained from instructor

### Solutions Applied


### Questions for TA/Instructor

