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
| A1 | Screenshot | PuTTY output WITHOUT Fnc6 (CH1 all 0s) | Submission (10 pts) | [x] |
| A2 | Screenshot | PuTTY output WITH Fnc6 (CH1 all 1s) | Submission (10 pts) | [x] |
| A3 | Text/Code | Description of uint8_t sample packing | Submission (10 pts) | [x] |
| C1 | Code | Modified `de5d_logic_analyzer_fns.c` | Submission (10 pts) | [x] |

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

**File saved to:** `lab04/a1.png`

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

**File saved to:** `lab04/a2.png`

---

## Text/Code Artifacts

### A3: Description of uint8_t Sample Packing

**Required for:** Section 4.3.2.2 — "provide a description about how you performed the saving of the samples" (part of 40 pts)

**Description:**

Each sample captures 3 logic analyzer channels and packs them into a single `uint8_t` using bitwise operations. The 3 channels are read from GPIO registers and stored in bits [2:0]:

- **Bit 0 — CH1 (PA0):** Read from `GPIOA->IDR` (Input Data Register) since PA0 is configured as an input. Extracted via `(GPIOA->IDR >> Pin0_pos) & 1` where `Pin0_pos = 0`.
- **Bit 1 — CH2 (PA10):** Read from `GPIOA->ODR` (Output Data Register) since PA10 is an output driving LED1. Extracted via `(GPIOA->ODR >> Pin10_pos) & 1` where `Pin10_pos = 10`.
- **Bit 2 — CH3 (PB8):** Read from `GPIOB->ODR` since PB8 is an output driving LED4. Extracted via `(GPIOB->ODR >> Pin8_pos) & 1` where `Pin8_pos = 8`.

The three bits are packed into one byte: `logic_samples[i] = (bit2 << 2) | (bit1 << 1) | bit0`

This stores 3 channel states per `uint8_t`, using only the 3 least significant bits. Bits [7:3] remain 0. During printing, each channel is unpacked by shifting and masking: `(logic_samples[j] >> ch) & 1`.

---

## Code Snippet Artifacts

### C1: Modified `de5d_logic_analyzer_fns.c`

**Required for:** Submission — "Include the code you modified in de5d_logic_analyzer_fns.c"

**File path:** `/opt/proj_mp/de5d_logic_analyzer/src/de5d_logic_analyzer_fns.c`

**Functions implemented:**
1. `mp_init_set_LED1_reset_LED4()` — sets LED1 on (PA10), LED4 off (PB8) via BSRR
2. `mp_read_logic_samples()` — samples 3 channels into uint8_t array
3. `mp_print_logic_samples()` — prints channel data as binary strings

**Code:** See [c1.c](./c1.c) for the complete file.

**Artifact file:** [c1.c](./c1.c)

---

## Submission Checklist

### PDF Report

**Filename:** `de5d-report-lastname-firstname.pdf`

**Required contents:**
- [x] A1: Screenshot without Fnc6 — `a1.png`
- [x] A2: Screenshot with Fnc6 — `a2.png`
- [x] A3: Description of uint8_t sample packing — see findings
- [x] C1: Modified `de5d_logic_analyzer_fns.c` code — `c1.c`

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

- Reference project `de2f_direct_gpio_reg_access` not found on system — resolved by obtaining zip from instructor
- CubeMX naming issue: During "Save As", project was accidentally saved as `de2f_direct_gpio_reg_access_g431n32` instead of `de5d_logic_analyzer_g431n32`. Cosmetic only — build and functionality unaffected, but internal folder/references use the old name.
- Fnc6 confusion: "Fnc6" refers to a **physical hardware connection**, not the F6 keyboard key
  - On the game controller board: a physical button labeled Fnc6
  - Without the game controller: bridge **Pins 12 and 13** on the analog (right-side) connector of the Nucleo-32
  - Pin 12 = A0 = PA0 (input pin) = 4th from bottom; Pin 13 = AREF (~3.3V) = 3rd from bottom
  - ("Nth from bottom" counts the bottom-most pin as 1st: bottom=1st, +3V3=2nd, AREF=3rd, A0=4th)
  - Bridging pulls PA0 high → CH1 reads all 1s
- CN3/CN4 label swap on G431KB: The NUCLEO-G431KB is the only Nucleo-32 board where ST swapped the CN3/CN4 connector labels vs other boards (L432KC, F303K8). Physical pin positions are identical.

### Solutions Applied

- Obtained `de2f_direct_gpio_reg_access.zip` from instructor, extracted .ioc and used it for CubeMX project creation
- Copied `lib/` files (mp_supported_mcu.h, mp_uart_redirect.c/.h) from `cc1s_uart_redirect` project since reference zip didn't include lib/
- Created [nucleo32_pinout_reference.md](../nucleo32_pinout_reference.md) documenting full header pinout for future reference

### Fnc6 Bridge Procedure (for A2 artifact)

1. **Bridge pins 12 and 13** on the right-side header (analog connector) using a jumper wire, paperclip, or ballpoint pen tip
2. These are the **3rd and 4th pins from the bottom** on the right side (bottom-most pin = 1st)
3. **Hold the bridge** in place
4. Type `s` in PuTTY and press Enter
5. Keep bridging during entire sampling period (~5 seconds)
6. Release after output appears
7. CH1 should show all 1s

### Questions for TA/Instructor

