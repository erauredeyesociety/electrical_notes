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
| A1 | Screenshot | Putty: candle type transitions (r/d switching) | PT1 (20 pts) | [x] |
| A2 | Screenshot | Putty: deterministic state changes (1-4) | PT2 (10 pts) | [x] |
| A3 | Screenshot | Putty: cumulative transition matrix at startup | PT3 (20 pts) | [x] |
| A4 | Notes | ET1: observations with/without NVIC interrupt guards | ET1 (10 pts) | [x] |
| A5 | Notes | ET2: final CCR_vals and LED intensity observations | ET2 (10 pts) | [x] |
| C1 | Code | 4 functions in `dm5d_led_candle_fns.c` | Submission | [x] |

---

## Screenshot Artifacts

### A1: Candle Type Transitions

**Required for:** PT1 — update_candle_type (20 pts)

**What to capture:**

- Putty output showing switching between Random and Deterministic modes
- Multiple 'd' and 'r' presses with printed type confirmations

**File saved to:** `a1.png`

---

### A2: Deterministic State Changes

**Required for:** PT2 — update_det_candle_state (10 pts)

**What to capture:**

- Putty output in deterministic mode showing state changes via '1'-'4'
- "Candle state is X" messages for each state

**File saved to:** `a2.png`

---

### A3: Cumulative Transition Matrix

**Required for:** PT3 — create_cumu_trans_matrix (20 pts)

**What to capture:**

- Putty output showing the 4x4 matrix printed at app startup
- Expected values: 30,55,80,100 / 25,55,80,100 / 25,50,80,100 / 20,45,70,100

**File saved to:** `a3.png`

---

### A4: ET1 — Interrupt Guarding Observations

**Required for:** ET1 — Disabling and enabling interrupt of UART2 (10 pts)

**What to document:**

- Case 1: Behavior with NVIC_DisableIRQ/EnableIRQ guards (should work correctly)
- Case 2: Behavior without guards (comment out the two NVIC lines, rebuild, test)
- Note any inconsistencies in mode switching or state changes without protection

**Observations:**

- **Case 1 (with NVIC guards):** Mode switching ('r'/'d') and deterministic state changes ('1'-'4') work correctly and consistently. The NVIC_DisableIRQ prevents the UART ISR from modifying `has_new_command` while the super loop is processing it, ensuring each command is fully handled before the next one can arrive.
- **Case 2 (without NVIC guards):** The application generally works, but there is a potential race condition. If the UART ISR fires between `update_candle_type()` and `update_det_candle_state()` (or before `print_help_message_if_needed()`), the `has_new_command` flag could be set or cleared at the wrong time, leading to missed commands or spurious help message printouts. The race window is small, so rapid key pressing is needed to trigger it. In practice, the behavior may appear normal most of the time because the super loop iterates quickly relative to human typing speed.

---

### A5: ET2 — LED Intensity Tuning

**Required for:** ET2 — Experimenting LED intensity for the four candle states (10 pts)

**What to document:**

- Final CCR_vals chosen for each state (ARR = 50,000 - 1)
- LED brightness observations for each state
- How realistic the candle effect looks

**Initial CCR_vals:** `{45000, 3000, 2000, 1000}`
**Final CCR_vals:** `{45000, 3000, 2000, 1000}` (default values produce realistic candle effect)

**Observations:** The default CCR values provide a good range of brightness levels. State 1 (CCR=45000) is very bright at 90% duty cycle. States 2-4 produce progressively dimmer output. The random state transitions with variable dwell times create a realistic flickering candle effect.

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

**Code:** See [c1.c](./c1.c)

---

## Submission Checklist

### PDF Report

**Filename:** `dm5d-report-lastname-firstname.pdf`

**Required contents:**

- [x] A1: Screenshot of candle type transitions (PT1)
- [x] A2: Screenshot of deterministic state changes (PT2)
- [x] A3: Screenshot of cumulative transition matrix (PT3)
- [x] A4: ET1 observations (interrupt guarding)
- [x] A5: ET2 LED intensity notes and final CCR_vals
- [x] C1: Code snippets of the 4 functions

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

- The NVIC guard lines are commented out in the base code by default, so the initial run is actually Case 2 (without guards). To test Case 1, the lines need to be uncommented.

### Questions for TA/Instructor

