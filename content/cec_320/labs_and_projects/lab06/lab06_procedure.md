# Lab 06 Procedure: LED Candle Based on PWM

**Course:** CEC 320 / MP-DM5D
**Points:** 100 total (10 setup + 60 programming + 20 experimentation + 10 submission)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-dm5d-lab6-led-candle-26-03.pdf`
> - [known_issues.md](../known_issues.md)

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract ZIP, verify folder structure at `/opt/proj_mp/dm5d_led_candle/` |
| 2 | LLM | Implement PT1-PT4 in `dm5d_led_candle_fns.c` |
| 3 | HUMAN | CubeMX: Open .ioc → Generate Code |
| 4 | LLM | Embed `mp_main()` hook in `main.c` |
| 5 | HUMAN | CubeIDE: Import, create `lib_src`, add include paths, link files |
| 6 | HUMAN | Build Debug, run on G431n32 board |
| 7 | HUMAN | Test PT1: press 'd' and 'r' to switch candle type |
| → | **ARTIFACT** | **A1:** Screenshot — Putty showing candle type transitions |
| 8 | HUMAN | Test PT2: press '1'-'4' in deterministic mode to change state |
| → | **ARTIFACT** | **A2:** Screenshot — Putty showing deterministic state changes |
| 9 | HUMAN | Verify PT3: check cumulative transition matrix printout at startup |
| → | **ARTIFACT** | **A3:** Screenshot — matrix printout (should show 30,55,80,100 etc.) |
| 10 | HUMAN | Test PT4: observe random candle flickering in random mode |
| 11 | HUMAN | ET1: Test with and without NVIC_DisableIRQ/EnableIRQ guards |
| → | **ARTIFACT** | **A4:** Screenshot/notes — ET1 observations (Case 1 vs Case 2) |
| 12 | HUMAN | ET2: Tune CCR_vals for realistic brightness at 4 states |
| → | **ARTIFACT** | **A5:** Notes — final CCR_vals and LED intensity observations |
| 13 | LLM | Save code artifacts, update findings/report |
| 14 | HUMAN | Clean builds in CubeIDE |
| 15 | LLM | Create submission ZIP |

---

## Point Breakdown

| Section | Points | Description |
|---------|--------|-------------|
| 6.2 Project Creation | 10 | CubeMX generate, CubeIDE setup |
| 6.3.1 PT1: update_candle_type | 20 | Toggle random/deterministic with 'r'/'d' |
| 6.3.2 PT2: update_det_candle_state | 10 | Set state 1-4 in deterministic mode |
| 6.3.3 PT3: create_cumu_trans_matrix | 20 | Cumulative probability distribution |
| 6.3.4 PT4: update_random_candle_state | 10 | Random dwell time (DWELL_TIM_MIN to DWELL_TIM_MAX) |
| 6.4.1 ET1: UART2 interrupt guarding | 10 | Test with/without NVIC disable/enable |
| 6.4.2 ET2: LED intensity tuning | 10 | Experiment with CCR_vals for 4 states |
| 6.5 Submission | 10 | Report + ZIP |

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Extract base files ZIP | CLAUDE CODE |
| Implement PT1-PT4 | CLAUDE CODE |
| CubeMX: Generate project from .ioc | HUMAN |
| Embed mp_main() hook in main.c | CLAUDE CODE |
| CubeIDE: Import, create lib_src, link files | HUMAN |
| Build and run on real board | HUMAN |
| ET1/ET2 experimentation on board | HUMAN |
| Capture screenshots | HUMAN |
| Save code artifacts, update docs | CLAUDE CODE |
| Create submission ZIP | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks

### A.1 Extract Base Files

Extract `dm5d_led_candle_g431n32-base-files.zip` to `/opt/proj_mp/dm5d_led_candle/`.

**Expected structure:**
```
/opt/proj_mp/dm5d_led_candle/
├── dm5d_led_candle_g431n32/
│   └── dm5d_led_candle_g431n32.ioc
├── lib/          # mp_uart_redirect, mp_simple_pwm_leds.h, mp_supported_mcu.h
└── src/          # _mp_main.c, dm5d_led_candle_app.c, dm5d_led_candle_fns.c/.h
```

### A.2 Implement Programming Tasks

All 4 functions in `/opt/proj_mp/dm5d_led_candle/src/dm5d_led_candle_fns.c`:

- **PT1 `update_candle_type()`:** Toggle `is_rdm_candle` and clear `has_new_command` on 'd'/'r'
- **PT2 `update_det_candle_state()`:** Set `candle_state = command - '1'` and clear `has_new_command`
- **PT3 `create_cumu_trans_matrix()`:** Accumulate `F += trans_prob[i][j]` before computing `lrint(F * STATE_TRANS_RANGE)`
- **PT4 `update_random_candle_state()`:** Replace `HAL_Delay(DWELL_TIM_MIN)` with random delay between DWELL_TIM_MIN and DWELL_TIM_MAX

### A.3 Embed mp_main() Hook

After CubeMX generates code, add in `main.c` inside `/* USER CODE BEGIN 2 */`:
```c
extern void mp_main(void);
mp_main();
```

---

## Part B: Human Tasks (GUI Required)

### B.1 CubeMX: Generate Project

1. Open CubeMX: `STM32CubeMX`
2. **File → Open** → `/opt/proj_mp/dm5d_led_candle/dm5d_led_candle_g431n32/dm5d_led_candle_g431n32.ioc`
3. Click **GENERATE CODE**
4. Open in CubeIDE when prompted

### B.2 CubeIDE: Import and Configure

1. If not already imported: **File → Open Projects from File System** → browse to STM32CubeIDE folder
2. Right-click project → **New → Folder** → name: `lib_src`
3. Add include paths: Right-click project → **Properties → C/C++ General → Paths and Symbols → Includes → GNU C → Add**:

| Include Path | Check |
|---|---|
| `../../lib` | Add to all configurations + all languages |
| `../../src` | Add to all configurations + all languages |

4. Link source files into `lib_src` (Right-click lib_src → **New → File → Advanced → Link to file system**):

| Source File (full path) |
|-------------------------|
| `/opt/proj_mp/dm5d_led_candle/src/_mp_main.c` |
| `/opt/proj_mp/dm5d_led_candle/src/dm5d_led_candle_app.c` |
| `/opt/proj_mp/dm5d_led_candle/src/dm5d_led_candle_fns.c` |
| `/opt/proj_mp/dm5d_led_candle/lib/mp_uart_redirect.c` |

5. Build Debug: **Ctrl+B**

> **Note:** No Unity build config needed — this lab has no unit tests. Only Debug config.

### B.3 Run on G431n32 Board

1. Connect G431 Nucleo-32 board via USB
2. Open Putty on serial port (`/dev/ttyACM0`, 115200 baud)
3. Right-click project → **Run As → STM32 C/C++ Application**
4. Putty shows cumulative transition matrix, then help message

### B.4 Test PT1 — Candle Type Switching (A1)

1. App starts in random mode (LED flickering)
2. Press **d** → should print "Candle type is Deterministic"
3. Press **r** → should print "Candle type is Random"
4. Toggle a few times
5. Capture Putty screenshot → **a1.png**

### B.5 Test PT2 — Deterministic State (A2)

1. Switch to deterministic mode (press **d**)
2. Press **1** → "Candle state is 1" (very bright)
3. Press **2** → "Candle state is 2" (bright)
4. Press **3** → "Candle state is 3" (dim)
5. Press **4** → "Candle state is 4" (very dim)
6. Observe LED brightness changes at each state
7. Capture Putty screenshot → **a2.png**

### B.6 Verify PT3 — Cumulative Transition Matrix (A3)

The matrix prints at startup. Expected output:
```
	30, 	55, 	80, 	100,
	25, 	55, 	80, 	100,
	25, 	50, 	80, 	100,
	20, 	45, 	70, 	100,
```

Capture Putty screenshot showing this → **a3.png**

### B.7 ET1 — UART2 Interrupt Guarding (A4)

**Case 1:** Run as-is (with `NVIC_DisableIRQ`/`NVIC_EnableIRQ` guards in the super loop). Test switching modes and states — should work correctly.

**Case 2:** Comment out the two NVIC lines in `dm5d_led_candle_app.c`:
```c
// NVIC_DisableIRQ(USART2_IRQn);
...
// NVIC_EnableIRQ(USART2_IRQn);
```
Rebuild and run. Rapidly press keys and observe if behavior becomes inconsistent.

Document observations in report → **A4** (notes, optionally screenshot)

### B.8 ET2 — LED Intensity Tuning (A5)

1. Use deterministic mode to test each state (1-4)
2. Adjust `CCR_vals[]` in `dm5d_led_candle_app.c` for realistic candle brightness:
   - State 1 (very bright): high CCR (near ARR=50000)
   - State 4 (very dim): low CCR
3. Rebuild and re-test after each change
4. Document final CCR_vals and observations → **A5** (notes in report)

### B.9 Clean and Submit

1. In CubeIDE: Right-click project → **Build Configurations → Clean All**
2. LLM creates submission ZIP

---

## Submission Checklist

- [ ] A1: Screenshot — candle type transitions (PT1)
- [ ] A2: Screenshot — deterministic state changes (PT2)
- [ ] A3: Screenshot — cumulative transition matrix printout (PT3)
- [ ] A4: Notes/screenshot — ET1 interrupt guarding observations
- [ ] A5: Notes — ET2 final CCR_vals and LED intensities
- [ ] C1: Code snippets of the 4 functions
- [ ] Report PDF: `dm5d-report-lastname-firstname.pdf`
- [ ] Project ZIP: `dm5d-proj-lastname-firstname.zip`
