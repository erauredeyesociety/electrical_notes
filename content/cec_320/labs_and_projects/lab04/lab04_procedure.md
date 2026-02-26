# Lab 04 Procedure: Logic Analyzer Based on Direct GPIO Register Access

**Course:** CEC 320 / MP-DE5D
**Points:** 100 (Project Creation 10 + Programming Tasks 80 + Submission 10)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `lab4-de5d-logic-analyzer-with-gpio-26-02.pdf`

> **IMPORTANT: This lab runs on REAL HARDWARE (G431n32 Nucleo-32) — NOT Renode.**
> You need physical board access and PuTTY/serial terminal for UART output.

---

## BLOCKER: Missing Reference Project

The reference project `de2f_direct_gpio_reg_access` does **NOT** exist on this system. The manual requires copying the `.ioc` file and `lib/` folder from it.

**Action needed:** Obtain `de2f_direct_gpio_reg_access` from the instructor/course materials and place it at `/opt/proj_mp/de2f_direct_gpio_reg_access/`.

Once available, the LLM can proceed with Step 1.

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 0 | HUMAN | Obtain `de2f_direct_gpio_reg_access` reference project |
| 1 | LLM | Create `de5d_logic_analyzer/` skeleton, copy .ioc + lib/, extract src/ from zip |
| 2 | HUMAN | CubeMX: Open .ioc → Save As `de5d_logic_analyzer_g431n32` → Generate Code |
| 3 | HUMAN | CubeIDE: Import project, create `lib_src` folder |
| 4 | HUMAN | CubeIDE: Link .c files into `lib_src`, add include paths (`../../lib` and `../../src`) |
| 5 | LLM | Add `mp_main();` hook in generated `main.c` (USER CODE section) |
| 6 | HUMAN | CubeIDE: Build — verify 0 errors |
| 7 | LLM | Implement `mp_init_set_LED1_reset_LED4()` (part of 4.3.2.1, 20 pts) |
| 8 | LLM | Implement `mp_read_logic_samples()` (4.3.2.2, 40 pts) |
| 9 | LLM | Implement `mp_print_logic_samples()` (4.3.2.3, 20 pts) |
| 10 | HUMAN | CubeIDE: Rebuild |
| 11 | HUMAN | Upload to G431n32 board, open PuTTY |
| 12 | HUMAN | Run WITHOUT Fnc6 pressed, type `s` + Enter |
| -> | **ARTIFACT** | **A1:** Screenshot of PuTTY output (CH1 all 0s) |
| 13 | HUMAN | Run WITH Fnc6 pressed, type `s` + Enter |
| -> | **ARTIFACT** | **A2:** Screenshot of PuTTY output (CH1 all 1s) |
| -> | **ARTIFACT** | **A3:** Description of how samples are saved to uint8_t |
| 14 | LLM | Save code snippet artifact files |
| 15 | HUMAN | Clean builds, create submission ZIP and PDF |

---

## Task Classification Summary

| Step | Description | Who Does It | Points |
|------|-------------|-------------|--------|
| Create project skeleton, copy files | File operations | CLAUDE CODE | — |
| CubeMX Save As + Generate | GUI | HUMAN | 10 pts (project creation) |
| CubeIDE import, link files, add paths | GUI | HUMAN | 10 pts (project creation) |
| Add hook in main.c | Code edit | CLAUDE CODE | — |
| Implement `mp_init_set_LED1_reset_LED4()` | Code writing | CLAUDE CODE | 20 pts |
| Implement `mp_read_logic_samples()` | Code writing | CLAUDE CODE | 40 pts |
| Implement `mp_print_logic_samples()` | Code writing | CLAUDE CODE | 20 pts |
| Build, upload, run on board | GUI + hardware | HUMAN | — |
| Take screenshots | Hardware + PuTTY | HUMAN | — |
| Submission (report + zip) | File prep | HUMAN | 10 pts |

---

## Part A: Claude Code Automated Tasks

> These tasks are performed by Claude Code. Human verifies completion.
> **BLOCKED** until reference project `de2f_direct_gpio_reg_access` is available.

### A.1 Create Project Skeleton and Copy Files

Create the folder structure:
```
/opt/proj_mp/de5d_logic_analyzer/
├── de5d_logic_analyzer_g431n32/    ← copy .ioc from reference
├── lib/                            ← copy from de2f_direct_gpio_reg_access/lib/
└── src/                            ← extract from de5d_logic_analyzer_src.zip
```

**Steps:**
1. Create `/opt/proj_mp/de5d_logic_analyzer/` with subdirs
2. Copy `.ioc` file from `/opt/proj_mp/de2f_direct_gpio_reg_access/*_g431n32/*.ioc` → `de5d_logic_analyzer_g431n32/`
3. Copy `/opt/proj_mp/de2f_direct_gpio_reg_access/lib/` → `de5d_logic_analyzer/lib/`
4. Extract `de5d_logic_analyzer_src.zip` `src/` contents → `de5d_logic_analyzer/src/`

### A.2 Add Hook Function in main.c

After CubeMX generates code and the human imports the project, add the `mp_main()` call in the generated `main.c` file inside the `/* USER CODE BEGIN 2 */` section (or appropriate USER CODE section in the while loop).

The pattern (from the app file):
```c
/* USER CODE BEGIN 2 */
mp_main();
/* USER CODE END 2 */
```

### A.3 Implement `mp_init_set_LED1_reset_LED4()` (20 pts partial)

**File:** `/opt/proj_mp/de5d_logic_analyzer/src/de5d_logic_analyzer_fns.c`

This function initializes the LED states using direct register access:
- **LED1 = PA10** → Turn ON (set bit) using `GPIOA->BSRR = mask_Pin10;`
- **LED4 = PB8** → Turn OFF (reset bit) using `GPIOB->BSRR = mask_Pin8 << 16;` (or `GPIOB->BRR = mask_Pin8;`)

Note: `mp_Fnc6_init()` and `mp_LED1_init()` are already implemented — no changes needed.

### A.4 Implement `mp_read_logic_samples()` (40 pts)

**File:** `/opt/proj_mp/de5d_logic_analyzer/src/de5d_logic_analyzer_fns.c`

Sample 3 channels in a loop of `SAMPLES` (50) iterations:
- **CH1:** Read PA0 via `GPIOA->IDR`, extract bit at Pin0_pos
- **CH2:** Read PA10 via `GPIOA->ODR`, extract bit at Pin10_pos
- **CH3:** Read PB8 via `GPIOB->ODR`, extract bit at Pin8_pos
- Pack into `uint8_t`: `logic_samples[i] = (bit2 << 2) | (bit1 << 1) | bit0`
- Delay: `HAL_Delay(sample_delay);`

### A.5 Implement `mp_print_logic_samples()` (20 pts)

**File:** `/opt/proj_mp/de5d_logic_analyzer/src/de5d_logic_analyzer_fns.c`

Print the sampled data via UART:
```
Sampling data for you...just a moment.
CH1: 00000000000000000000000000000000000000000000000000
CH2: 11111111111100000000000000000000011111111111111111
CH3: 00000000000001111111111111111111100000000000000000
```

For each channel, extract the corresponding bit from each `logic_samples[i]` element and print '0' or '1'.

### A.6 Save Code Snippet Artifact Files

After all implementations, save:
- `c1.c` — all three implemented functions from `de5d_logic_analyzer_fns.c`

---

## Part B: Human Tasks (GUI + Hardware Required)

> Follow steps exactly. This lab requires physical hardware.

### B.1 Obtain Reference Project

If not already available, get `de2f_direct_gpio_reg_access` from the instructor and place at:
```
/opt/proj_mp/de2f_direct_gpio_reg_access/
```

Then tell the LLM to proceed with Part A.

### B.2 CubeMX: Save As and Generate Code

1. Open the `.ioc` file that was copied to `de5d_logic_analyzer_g431n32/`:
   ```bash
   STM32CubeMX
   ```
   File → Open → navigate to `/opt/proj_mp/de5d_logic_analyzer/de5d_logic_analyzer_g431n32/*.ioc`

2. **File → Save Project As** → navigate to `/opt/proj_mp/de5d_logic_analyzer/de5d_logic_analyzer_g431n32/` → set project name to `de5d_logic_analyzer_g431n32` → Save

3. Click **GENERATE CODE**

4. When prompted to open in CubeIDE, click **Open Project** (or import manually later)

### B.3 CubeIDE: Import and Configure

1. If not auto-opened: **File → Import → General → Existing Projects into Workspace** → browse to:
   ```
   /opt/proj_mp/de5d_logic_analyzer/de5d_logic_analyzer_g431n32/STM32CubeIDE/
   ```

2. **Create `lib_src` folder:** Right-click project → **New → Folder** → name it `lib_src`

3. **Link .c files** into `lib_src` (use New → File → Advanced → Link to file system):

   | # | File to Link |
   |---|--------------|
   | 1 | `/opt/proj_mp/de5d_logic_analyzer/lib/mp_uart_redirect.c` |
   | 2 | `/opt/proj_mp/de5d_logic_analyzer/src/_mp_main.c` |
   | 3 | `/opt/proj_mp/de5d_logic_analyzer/src/de5d_callbacks.c` |
   | 4 | `/opt/proj_mp/de5d_logic_analyzer/src/de5d_logic_analyzer_app.c` |
   | 5 | `/opt/proj_mp/de5d_logic_analyzer/src/de5d_logic_analyzer_fns.c` |

   **Note:** The lib/ may contain additional `.c` files — link ALL `.c` files from both `lib/` and `src/`.

4. **Add include paths:** Right-click project → **Properties → C/C++ General → Paths and Symbols → Includes → GNU C → Add:**
   - `../../lib`
   - `../../src`

   Check **Add to all configurations** and **Add to all languages**.

5. **Build:** Ctrl+B — verify 0 errors

### B.4 Build and Upload After Programming Tasks

After the LLM implements the programming tasks (A.3–A.5):

1. **Ctrl+B** to rebuild
2. Connect G431n32 board via USB
3. Right-click project → **Debug As → STM32 C/C++ Application** (or Run As)
4. Open **PuTTY** (or other serial terminal) connected to the board's COM port

### B.5 Capture Artifact A1 — Without Fnc6

1. With PuTTY connected and program running
2. Do NOT press Fnc6 (do not connect Pins 12 and 13)
3. Type `s` and press Enter
4. Wait ~5 seconds for sampling to complete
5. Expected output: CH1 all 0s, CH2 and CH3 show alternating patterns (opposite each other)

> **ARTIFACT A1:** Screenshot the PuTTY output.
> Save as: `~/electrical_notes/content/cec_320/labs_and_projects/lab04/a1.png`

### B.6 Capture Artifact A2 — With Fnc6

1. Press Fnc6 (or connect Pins 12 and 13 of analog connector with metal object)
2. Type `s` and press Enter
3. Wait ~5 seconds for sampling
4. Expected output: CH1 all 1s, CH2 and CH3 same alternating pattern

> **ARTIFACT A2:** Screenshot the PuTTY output.
> Save as: `~/electrical_notes/content/cec_320/labs_and_projects/lab04/a2.png`

### B.7 Submission Preparation

**Clean builds:**
1. In CubeIDE: Right-click project → **Build Configurations → Clean All**

**Create submission ZIP:**
```bash
cd /opt/proj_mp/
zip -r de5d-proj-lastname-firstname.zip de5d_logic_analyzer/
```

**Submission filenames:**
- Report: `de5d-report-lastname-firstname.pdf`
- Project ZIP: `de5d-proj-lastname-firstname.zip`

**Note:** Team submission allowed — list both team members' names.

---

## Programming Task Reference

| Task | Function | Points | Description |
|------|----------|--------|-------------|
| 4.3.2.1 | `mp_init_set_LED1_reset_LED4()` | 20 pts | Set LED1 (PA10) on, LED4 (PB8) off via BSRR |
| 4.3.2.2 | `mp_read_logic_samples()` | 40 pts | Sample 3 channels × 50 samples into uint8_t array |
| 4.3.2.3 | `mp_print_logic_samples()` | 20 pts | Print channel data as 0/1 strings via UART |

**Channel Mapping:**

| Channel | Pin | GPIO Port | Register | Bit in uint8_t |
|---------|-----|-----------|----------|----------------|
| CH1 | PA0 | GPIOA | IDR | Bit 0 |
| CH2 | PA10 | GPIOA | ODR | Bit 1 |
| CH3 | PB8 | GPIOB | ODR | Bit 2 |

---

## Submission Checklist

- [ ] A1: Screenshot without Fnc6 (CH1 all 0)
- [ ] A2: Screenshot with Fnc6 (CH1 all 1)
- [ ] A3: Description of uint8_t sample packing approach
- [ ] Code: Modified `de5d_logic_analyzer_fns.c`
- [ ] PDF report: `de5d-report-lastname-firstname.pdf`
- [ ] Clean project ZIP: `de5d-proj-lastname-firstname.zip`
