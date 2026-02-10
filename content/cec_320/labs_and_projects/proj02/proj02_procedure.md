# Proj 02 Procedure: Mocking GPIO and BSRR

**Course:** CEC 320 / MP-DE4U
**Points:** 100 (Getting Started 5 + Programming Tasks 85 + Submission 10)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - [known_base_projects.md](../known_base_projects.md) (ca4b_cls_projs)
> - Original PDF: `mp-de4u-proj2-mocking-gpio-n-bsrr-26-02.pdf`

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract `de4u_src_test.zip` → place files in `proj2_src/` and `proj2_test/` |
| 2 | LLM | Create Renode script `proj2Unity_f412dsc.resc` |
| 3 | HUMAN | CubeIDE: Link 7 `.c` files into `proj2_src_test/` |
| 4 | HUMAN | CubeIDE: Select `Proj2Unity` config, Build (Ctrl+B) |
| 5 | HUMAN | Renode: Run `proj2Unity_f412dsc.resc` — verify initial build (all tests fail) |
| 6 | LLM | Implement PT 1: `mp_mock_write_idr()` in `mp_mock_utils_4_gpio_regs.c` |
| 7 | HUMAN | CubeIDE: Rebuild, Renode: Re-run |
| -> | **ARTIFACT** | **A1:** Screenshot — Tests 1,2 PASS (2 pass, 6 fail) |
| 8 | LLM | Implement PT 2: `mp_mock_odr_update_with_bsrr()` in `mp_mock_odr_update_with_bsrr_brr.c` |
| 9 | HUMAN | CubeIDE: Rebuild, Renode: Re-run |
| -> | **ARTIFACT** | **A2:** Screenshot — Tests 1-7 PASS (7 pass, 1 fail) |
| 10 | LLM | Implement PT 3: `test_mp_gpio_toggle_pins_func()` in `test_de4u_mocking_gpio_n_bsrr.c` |
| 11 | HUMAN | CubeIDE: Rebuild, Renode: Re-run |
| -> | **ARTIFACT** | **A3:** Screenshot — All 8 tests PASS (REQUIRED for submission) |
| 12 | LLM | Save code snippet artifact files (C1, C2, C3) |
| 13 | HUMAN | Clean all builds, create submission ZIP and PDF report |

---

## Task Classification Summary

| Step | Description | Who Does It | Points |
|------|-------------|-------------|--------|
| Extract zip, place source files | File operations | CLAUDE CODE | — |
| Create Renode script | File creation | CLAUDE CODE | — |
| Link .c files in CubeIDE | GUI (New → File → Link) | HUMAN | 5 pts (part of Getting Started) |
| Build Proj2Unity | GUI (Ctrl+B) | HUMAN | 5 pts (part of Getting Started) |
| Implement `mp_mock_write_idr()` | Code writing | CLAUDE CODE | 15 pts (PT 1) |
| Implement `mp_mock_odr_update_with_bsrr()` | Code writing | CLAUDE CODE | 45 pts (PT 2) |
| Write `test_mp_gpio_toggle_pins_func()` | Code writing | CLAUDE CODE | 25 pts (PT 3) |
| Rebuild + Renode after each PT | GUI + Renode | HUMAN | — |
| Take screenshots | OS interaction | HUMAN | — |
| Submission (report + zip) | File prep + upload | HUMAN | 10 pts |

---

## Part A: Claude Code Automated Tasks

> These tasks are performed by Claude Code. Human verifies completion.

### A.1 Extract Source Files from ZIP

Extract `de4u_src_test.zip` and place files into the correct folders:

| Source (in ZIP) | Destination |
|-----------------|-------------|
| `src/_mp_main.c` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/_mp_main.c` |
| `src/de4u_mocking_gpio_n_bsrr_app.c` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/de4u_mocking_gpio_n_bsrr_app.c` |
| `src/mp_gpio_toggle.c` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_gpio_toggle.c` |
| `src/mp_gpio_toggle.h` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_gpio_toggle.h` |
| `src/mp_mock_odr_update_with_bsrr_brr.c` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_odr_update_with_bsrr_brr.c` |
| `src/mp_mock_odr_update_with_bsrr_brr.h` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_odr_update_with_bsrr_brr.h` |
| `src/mp_mock_utils_4_gpio_regs.c` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_utils_4_gpio_regs.c` |
| `src/mp_mock_utils_4_gpio_regs.h` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_utils_4_gpio_regs.h` |
| `src/mp_stm32xx_mocked_gpiox.c` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_stm32xx_mocked_gpiox.c` |
| `src/mp_stm32xx_mocked_gpiox.h` | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_stm32xx_mocked_gpiox.h` |
| `test/test_de4u_mocking_gpio_n_bsrr.c` | `/opt/proj_mp/ca4b_cls_projs/proj2_test/test_de4u_mocking_gpio_n_bsrr.c` |

### A.2 Create Renode Script

Create `/opt/proj_mp/ca4b_cls_projs/renode/proj2Unity_f412dsc.resc` based on the existing proj1 pattern, pointing to the `Proj2Unity` build output.

### A.3 Implement PT 1: `mp_mock_write_idr()` (15 pts)

**File:** `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_utils_4_gpio_regs.c`

The function `mp_mock_write_idr()` is declared with `__attribute__((weak))` and has a stub body (`// Add your code here`). Replace the weak implementation with a real one that writes the `idr` value to the GPIO port's IDR register (`GPIOx->IDR = idr`).

**Tests passed after this step:** Tests 1, 2 (test_read_idr_via_hal_func, test_read_idr_directly)

### A.4 Implement PT 2: `mp_mock_odr_update_with_bsrr()` (45 pts)

**File:** `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_odr_update_with_bsrr_brr.c`

Implement the `mp_mock_odr_update_with_bsrr()` function. This function simulates how hardware propagates BSRR writes to ODR:

1. If BSRR is non-zero:
   - Lower 16 bits (BS bits): SET corresponding ODR bits (`ODR |= BSRR & 0xFFFF`)
   - Upper 16 bits (BR bits): CLEAR corresponding ODR bits (`ODR &= ~(BSRR >> 16)`)
2. After updating ODR, clear BSRR to 0 (so it doesn't affect the next operation)

**Key insight from BSRR bit map (Figure 1 in manual):**
- Bits [15:0] = BS15..BS0 (Bit Set) — writing 1 sets the corresponding ODR bit
- Bits [31:16] = BR15..BR0 (Bit Reset) — writing 1 clears the corresponding ODR bit

**Tests passed after this step:** Tests 3, 4, 5, 6, 7

### A.5 Implement PT 3: `test_mp_gpio_toggle_pins_func()` (25 pts)

**File:** `/opt/proj_mp/ca4b_cls_projs/proj2_test/test_de4u_mocking_gpio_n_bsrr.c`

The test function `test_mp_gpio_toggle_pins_func` is declared `__attribute__((weak))` with an empty body in the provided test file. Write a new implementation in a separate file or override it.

This test should be modeled after Test 7 (`test_hal_gpio_toggle_pin_via_hal_func`) but call `mp_GPIO_TogglePinS()` instead of `HAL_GPIO_TogglePin()`. Key considerations:
- `mp_GPIO_TogglePinS()` uses direct ODR XOR (not BSRR), so `mp_mock_odr_update_with_bsrr()` is NOT needed
- The function takes a `uint16_t GPIO_PinS` bitmask (multiple pins at once)
- Remove the `mp_mock_odr_update_with_bsrr()` call since the revised toggle writes directly to ODR

**Test passed after this step:** Test 8

### A.6 Save Code Snippet Artifact Files

After all programming tasks are complete, save code snippet files:
- `c1.c` — `mp_mock_write_idr()` function
- `c2.c` — `mp_mock_odr_update_with_bsrr()` function
- `c3.c` — `test_mp_gpio_toggle_pins_func()` function

---

## Part B: Human Tasks (GUI Required)

> Follow steps exactly. Copy-paste commands where provided.

### B.1 Link Source Files in CubeIDE (Getting Started — 5 pts)

**Prerequisites:** Claude Code has completed A.1 (files extracted to proj2_src/ and proj2_test/).

Link the following 7 `.c` files into the `proj2_src_test` folder in CubeIDE. Use **New → File → Link to file system** (drag-and-drop is unreliable on Linux — see [known_issues.md](../known_issues.md)).

**For each file below:**
1. In CubeIDE Project Explorer, expand `ca4b_cls_projs_f412dsc` → `proj2_src_test`
2. Right-click `proj2_src_test` → **New → File**
3. Click **Advanced >>**
4. Check **Link to file in the file system**
5. Click **Browse...**, navigate to the file path below
6. Click **Open**, then **Finish**

| # | File to Link (full path) |
|---|--------------------------|
| 1 | `/opt/proj_mp/ca4b_cls_projs/proj2_src/_mp_main.c` |
| 2 | `/opt/proj_mp/ca4b_cls_projs/proj2_src/de4u_mocking_gpio_n_bsrr_app.c` |
| 3 | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_gpio_toggle.c` |
| 4 | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_odr_update_with_bsrr_brr.c` |
| 5 | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_mock_utils_4_gpio_regs.c` |
| 6 | `/opt/proj_mp/ca4b_cls_projs/proj2_src/mp_stm32xx_mocked_gpiox.c` |
| 7 | `/opt/proj_mp/ca4b_cls_projs/proj2_test/test_de4u_mocking_gpio_n_bsrr.c` |

**Note:** Do NOT link `.h` header files — only `.c` source files. The include paths for `proj2_src/` are already pre-configured in the build settings.

### B.2 Build Proj2Unity

1. In CubeIDE, click the **dropdown arrow** next to the hammer icon
2. Select **Proj2Unity** build configuration
3. Click the hammer icon (or **Ctrl+B**) to build
4. Verify build succeeds with 0 errors

**If build fails:** Check [known_issues.md](../known_issues.md) for common solutions.

### B.3 Run in Renode (Initial Verification)

**Terminal commands:**
```bash
cd /opt/proj_mp/ca4b_cls_projs/renode/
renode
```

**Renode Monitor commands:**
```
s @proj2Unity_f412dsc.resc
```

Verify the UART2 window opens and shows Unity test output. At this point, most tests should FAIL (only Test 4 may pass since it uses direct ODR write).

### B.4 Rebuild and Test After PT 1

After Claude Code implements PT 1 (`mp_mock_write_idr`):

1. In CubeIDE: **Ctrl+B** to rebuild (Proj2Unity should still be selected)
2. In Renode Monitor: `s @proj2Unity_f412dsc.resc` (or restart Renode)
3. Verify Tests 1, 2 now PASS

> **ARTIFACT A1:** Take a screenshot of the UART2 window showing Tests 1, 2 PASS.
> Save as: `~/electrical_notes/content/cec_320/labs_and_projects/proj02/a1.png`

### B.5 Rebuild and Test After PT 2

After Claude Code implements PT 2 (`mp_mock_odr_update_with_bsrr`):

1. In CubeIDE: **Ctrl+B** to rebuild
2. In Renode Monitor: `s @proj2Unity_f412dsc.resc`
3. Verify Tests 1-7 now PASS (Test 4 was already passing)

> **ARTIFACT A2:** Take a screenshot of the UART2 window showing Tests 1-7 PASS.
> Save as: `~/electrical_notes/content/cec_320/labs_and_projects/proj02/a2.png`

### B.6 Rebuild and Test After PT 3

After Claude Code implements PT 3 (`test_mp_gpio_toggle_pins_func`):

1. In CubeIDE: **Ctrl+B** to rebuild
2. In Renode Monitor: `s @proj2Unity_f412dsc.resc`
3. Verify ALL 8 tests PASS

> **ARTIFACT A3:** Take a screenshot of the UART2 window showing all 8 tests PASS.
> Save as: `~/electrical_notes/content/cec_320/labs_and_projects/proj02/a3.png`
> **This is the REQUIRED submission screenshot.**

### B.7 Submission Preparation

**Clean all builds first** (important — multiple project builds may exist):
1. In CubeIDE: Right-click `ca4b_cls_projs_f412dsc` → **Build Configurations → Clean All**
2. Also clean `ca4b_cls_projs_g431n32` if it was used

**Create submission ZIP:**
```bash
cd /opt/proj_mp/
zip -r de4u-lastname-firstname.zip ca4b_cls_projs/
```

**Create PDF report** from `proj02_report.md` — export or convert to PDF.

**Submission filenames:**
- Report: `de4u-report-lastname-firstname.pdf`
- Project ZIP: `de4u-lastname-firstname.zip`

---

## Test Function Reference

| Test # | Function Name | What It Tests | Passes After |
|--------|---------------|---------------|--------------|
| 1 | `test_read_idr_via_hal_func` | Read mocked IDR via HAL_GPIO_ReadPin | PT 1 |
| 2 | `test_read_idr_directly` | Read mocked IDR directly (GPIOx->IDR) | PT 1 |
| 3 | `test_write_odr_via_hal_func` | Write ODR via HAL_GPIO_WritePin (uses BSRR) | PT 2 |
| 4 | `test_write_odr_directly` | Write ODR directly (GPIOx->ODR = exp) | Auto (no BSRR needed) |
| 5 | `test_write_bsrr_to_set_odr` | BSRR lower bits set ODR bits | PT 2 |
| 6 | `test_write_bsrr_to_clear_odr` | BSRR upper bits clear ODR bits | PT 2 |
| 7 | `test_hal_gpio_toggle_pin_via_hal_func` | HAL toggle uses BSRR, needs update | PT 2 |
| 8 | `test_mp_gpio_toggle_pins_func` | Revised toggle (direct ODR XOR) | PT 3 |

---

## Submission Checklist

- [ ] All 8 tests passing (screenshot A3)
- [ ] Code for `mp_mock_write_idr()` (C1)
- [ ] Code for `mp_mock_odr_update_with_bsrr()` (C2)
- [ ] Code for `test_mp_gpio_toggle_pins_func()` (C3)
- [ ] PDF report: `de4u-report-lastname-firstname.pdf`
- [ ] Clean project ZIP: `de4u-lastname-firstname.zip`
