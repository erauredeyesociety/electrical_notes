# Lab 06 Findings: LED Candle Based on PWM

**Course:** CEC 320 / MP-DM5D
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab06_procedure.md](./lab06_procedure.md)
> - Original Manual: `mp-dm5d-lab6-led-candle-26-03.pdf`

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Putty: candle type transitions (r/d switching) | PT1 (20 pts) | [ ] |
| A2 | Screenshot | Putty: deterministic state changes (1-4) | PT2 (10 pts) | [ ] |
| A3 | Screenshot | Putty: cumulative transition matrix at startup | PT3 (20 pts) | [ ] |
| A4 | Notes | ET1: observations with/without NVIC interrupt guards | ET1 (10 pts) | [ ] |
| A5 | Notes | ET2: final CCR_vals and LED intensity observations | ET2 (10 pts) | [ ] |
| C1 | Code | 4 functions in `dm5d_led_candle_fns.c` | Submission | [ ] |

---

## Screenshot Artifacts

### A1: Candle Type Transitions

**Required for:** PT1 — update_candle_type (20 pts)

**What to capture:**

- Putty output showing switching between Random and Deterministic modes
- Multiple 'd' and 'r' presses with printed type confirmations

**File saved to:** ____________________

---

### A2: Deterministic State Changes

**Required for:** PT2 — update_det_candle_state (10 pts)

**What to capture:**

- Putty output in deterministic mode showing state changes via '1'-'4'
- "Candle state is X" messages for each state

**File saved to:** ____________________

---

### A3: Cumulative Transition Matrix

**Required for:** PT3 — create_cumu_trans_matrix (20 pts)

**What to capture:**

- Putty output showing the 4x4 matrix printed at app startup
- Expected values: 30,55,80,100 / 25,55,80,100 / 25,50,80,100 / 20,45,70,100

**File saved to:** ____________________

---

### A4: ET1 — Interrupt Guarding Observations

**Required for:** ET1 — Disabling and enabling interrupt of UART2 (10 pts)

**What to document:**

- Case 1: Behavior with NVIC_DisableIRQ/EnableIRQ guards (should work correctly)
- Case 2: Behavior without guards (comment out the two NVIC lines, rebuild, test)
- Note any inconsistencies in mode switching or state changes without protection

**Observations:** ____________________

---

### A5: ET2 — LED Intensity Tuning

**Required for:** ET2 — Experimenting LED intensity for the four candle states (10 pts)

**What to document:**

- Final CCR_vals chosen for each state (ARR = 50,000 - 1)
- LED brightness observations for each state
- How realistic the candle effect looks

**Initial CCR_vals:** `{45000, 3000, 2000, 1000}`
**Final CCR_vals:** ____________________

---

## Code Snippet Artifacts

### C1: Four Functions in `dm5d_led_candle_fns.c`

**Required for:** Submission — "Code snippets of the functions you have modified or created"

**File path:** `/opt/proj_mp/dm5d_led_candle/src/dm5d_led_candle_fns.c`

**Functions implemented:**

1. `update_candle_type()` — toggle random/deterministic mode
2. `update_det_candle_state()` — set state from UART command '1'-'4'
3. `create_cumu_trans_matrix()` — cumulative probability distribution
4. `update_random_candle_state()` — random state transitions with random dwell time

**Code:** See [c1.c](./c1.c) (to be created after testing)

---

## Submission Checklist

### PDF Report

**Filename:** `dm5d-report-lastname-firstname.pdf`

**Required contents:**

- [ ] A1: Screenshot of candle type transitions (PT1)
- [ ] A2: Screenshot of deterministic state changes (PT2)
- [ ] A3: Screenshot of cumulative transition matrix (PT3)
- [ ] A4: ET1 observations (interrupt guarding)
- [ ] A5: ET2 LED intensity notes and final CCR_vals
- [ ] C1: Code snippets of the 4 functions

### Project ZIP

**Filename:** `dm5d-proj-lastname-firstname.zip`

**Before zipping:**

1. In CubeIDE: Right-click project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/dm5d_led_candle/`

**Note:** Team submission allowed (2 students). List both names.

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Code Snippets and Screenshots | C1 | 4 functions in dm5d_led_candle_fns.c |
| Code Snippets and Screenshots | A1 | Candle type transitions |
| Code Snippets and Screenshots | A2 | Deterministic state changes |
| Code Snippets and Screenshots | A3 | Cumulative transition matrix |
| Discussions and Results | A4 | ET1 interrupt guarding observations |
| Discussions and Results | A5 | ET2 LED intensity tuning |

---

## Notes and Observations

### Issues Encountered


### Questions for TA/Instructor

