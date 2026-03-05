# Lab 05 Procedure: Pseudo Random Number Generation in C

**Course:** CEC 320 / MP-DK5U
**Points:** 100 total (20 setup + 70 programming + 10 submission)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-dk5u-lab5-prn-generation-in-c-26-03.pdf`
> - [known_issues.md](../known_issues.md)

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract ZIP, verify folder structure at `/opt/proj_mp/dk5u_prn_generation_in_c/` |
| 2 | HUMAN | CubeMX: Open F412dsc .ioc → Save As → Generate Code |
| 3 | HUMAN | CubeMX: Open G431n32 .ioc → Save As → Generate Code |
| 4 | HUMAN | CubeIDE: Import both projects, create `lib_src` folders, add include paths (`lib`, `src`), link source files |
| 5 | HUMAN | CubeIDE: Create Unity build configs for both boards (with `UNIT_TEST` define) |
| 6 | LLM | Embed `mp_main()` hook in both `main.c` files |
| 7 | HUMAN | Build F412dsc Unity, run in Renode |
| 8 | LLM | Implement PT1: `mp_prn_ini_c()` |
| 9 | HUMAN | Rebuild F412dsc Unity, run in Renode |
| → | **ARTIFACT** | **A1:** Screenshot — test_prn_ini_c PASSED (1 pass, 5 fail) |
| 10 | LLM | Implement PT2: `mp_prn_tap_mask_c()` |
| 11 | HUMAN | Rebuild F412dsc Unity, run in Renode |
| → | **ARTIFACT** | **A2:** Screenshot — 2 tests pass, 4 fail |
| 12 | LLM | Implement PT3: `mp_prn_gen_c()` |
| 13 | HUMAN | Rebuild F412dsc Unity, run in Renode |
| → | **ARTIFACT** | **A3:** Screenshot — all 6 tests pass (F412dsc) |
| 14 | HUMAN | Build G431n32 Unity, run on real board (no Renode script for G431n32) |
| → | **ARTIFACT** | **A4:** Screenshot (Putty) — all 6 tests pass (G431n32) |
| 15 | LLM | Implement PT4: Embed Timer 4 callback in `stm32g4xx_it.c` |
| 16 | HUMAN | Build G431n32 App (Debug), upload to real board |
| → | **ARTIFACT** | **A5:** Screenshot/video — LED4 blinking pseudo-randomly on G431n32 |
| 17 | LLM | Save code artifacts, update findings/report |
| 18 | HUMAN | Clean builds in CubeIDE |
| 19 | LLM | Create submission ZIP |

---

## Point Breakdown

| Section | Points | Description |
|---------|--------|-------------|
| 5.3 Project Creation | 20 | CubeMX generate, CubeIDE setup, build configs |
| 5.4.1 PT1: mp_prn_ini_c | 15 | Initialization function |
| 5.4.2 PT2: mp_prn_tap_mask_c | 15 | Tap mask generation |
| 5.4.3 PT3: mp_prn_gen_c | 35 | Main PRN generation function |
| 5.4.4 PT4: App | 5 | Timer-driven LED blinking |
| 5.5 Submission | 10 | Report + ZIP |

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Extract base files ZIP | CLAUDE CODE |
| CubeMX: Generate projects from .ioc | HUMAN |
| CubeIDE: Import, create lib_src, link files, build configs | HUMAN |
| Embed mp_main() hook in main.c | CLAUDE CODE |
| Implement PT1-PT3 (3 functions in mp_prn_c.c) | CLAUDE CODE |
| Embed Timer 4 callback in stm32g4xx_it.c | CLAUDE CODE |
| Build and run (Renode + real board) | HUMAN |
| Capture screenshots | HUMAN |
| Save code artifacts, update docs | CLAUDE CODE |
| Create submission ZIP | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks

### A.1 Extract Base Files

Extract `dk5u_prn_generation_in_c-base-files.zip` to `/opt/proj_mp/dk5u_prn_generation_in_c/`:

```bash
cd /opt/proj_mp/
mkdir -p dk5u_prn_generation_in_c
cd dk5u_prn_generation_in_c
unzip ~/electrical_notes/content/cec_320/labs_and_projects/lab05/dk5u_prn_generation_in_c-base-files.zip
```

**Expected structure:**
```
/opt/proj_mp/dk5u_prn_generation_in_c/
├── dk5u_prn_generation_in_c_f412dsc/
│   └── dk5u_prn_generation_in_c_f412dsc.ioc
├── dk5u_prn_generation_in_c_g431n32/
│   └── dk5u_prn_generation_in_c_g431n32.ioc
├── lib/          # Unity, UART redirect, mp_sum_of_1s, etc.
├── renode/       # Renode scripts for F412dsc Unity
├── src/          # App code, PRN source, callbacks, _mp_main.c
└── test/         # test_dk5u_prn_generation_in_c.c
```

### A.2 Embed mp_main() Hook

After CubeMX generates code for both boards, add the `mp_main()` call in each `main.c`:

**In both `main.c` files** — inside `/* USER CODE BEGIN 2 */`:
```c
/* USER CODE BEGIN 2 */
extern void mp_main(void);
mp_main();
/* USER CODE END 2 */
```

### A.3 Implement Programming Tasks

Implement 3 functions in `/opt/proj_mp/dk5u_prn_generation_in_c/src/mp_prn_c.c`. Done incrementally.

### A.4 Embed Timer 4 Callback (PT4)

For the G431n32 App, modify `stm32g4xx_it.c` to embed the Timer 4 callback:

**In `TIM4_IRQHandler`** — inside `/* USER CODE BEGIN TIM4_IRQn 0 */`:
```c
/* USER CODE BEGIN TIM4_IRQn 0 */
void mp_TIM_Callback(void);
mp_TIM_Callback();
/* USER CODE END TIM4_IRQn 0 */
```

### A.5 Save Code Artifacts and Update Documentation

After all tasks pass, save code snippets to `lab05/c1.c` (3 functions) and update findings/report.

---

## Part B: Human Tasks (GUI Required)

### B.1 CubeMX: Generate Projects (20 pts setup)

**For F412dsc (Renode/unit test only):**

1. Open CubeMX:
   ```bash
   STM32CubeMX
   ```
2. **File → Open** → navigate to:
   ```
   /opt/proj_mp/dk5u_prn_generation_in_c/dk5u_prn_generation_in_c_f412dsc/dk5u_prn_generation_in_c_f412dsc.ioc
   ```
3. Click **GENERATE CODE**
4. When prompted, click **Open Project** (or import manually later)

**For G431n32 (unit test + real board App):**

1. In CubeMX, **File → Open** → navigate to:
   ```
   /opt/proj_mp/dk5u_prn_generation_in_c/dk5u_prn_generation_in_c_g431n32/dk5u_prn_generation_in_c_g431n32.ioc
   ```
2. Click **GENERATE CODE**
3. When prompted, click **Open Project** (or import manually later)

### B.2 CubeIDE: Import and Configure Both Projects

**For EACH project (F412dsc and G431n32):**

1. If not already imported: **File → Open Projects from File System** → browse to STM32CubeIDE folder
2. Right-click project → **New → Folder** → name it `lib_src`
3. Add include paths: Right-click project → **Properties → C/C++ General → Paths and Symbols → Includes → GNU C → Add**:

| Include Path | Check |
|---|---|
| `../../lib` | Add to all configurations + all languages |
| `../../src` | Add to all configurations + all languages |

4. Link source files into `lib_src` using **New → File → Advanced → Link to file system**:

**F412dsc project — link these files to `lib_src`:**

| Source File (full path) |
|-------------------------|
| `/opt/proj_mp/dk5u_prn_generation_in_c/src/_mp_main.c` |
| `/opt/proj_mp/dk5u_prn_generation_in_c/src/mp_prn_c.c` |
| `/opt/proj_mp/dk5u_prn_generation_in_c/lib/mp_sum_of_1s.c` |
| `/opt/proj_mp/dk5u_prn_generation_in_c/lib/mp_uart_redirect.c` |
| `/opt/proj_mp/dk5u_prn_generation_in_c/test/test_dk5u_prn_generation_in_c.c` |
| `/opt/proj_mp/dk5u_prn_generation_in_c/lib/unity.c` |

**G431n32 project — link ALL the above files PLUS these additional files to `lib_src`:**

| Additional Source File (full path) |
|-------------------------|
| `/opt/proj_mp/dk5u_prn_generation_in_c/src/dk5u_prn_generation_in_c_app.c` |
| `/opt/proj_mp/dk5u_prn_generation_in_c/src/dk5u_timer_fn_n_callback.c` |
| `/opt/proj_mp/dk5u_prn_generation_in_c/src/dk5u_uart_callback.c` |

### B.3 CubeIDE: Create Unity Build Configurations

**For EACH project:**

1. Right-click the project → hover over **Build Configurations** → click **Manage...**
2. Click **New...** → Name: `Unity` → Copy settings from: `Debug` → **OK**
3. Select `Unity` in the hammer dropdown (a new `Unity/` build output folder appears)
4. Right-click project → **Properties → C/C++ Build → Settings → MCU GCC Compiler → Preprocessor → Define symbols**
5. Click **Add** (+) → enter: `UNIT_TEST` → **OK**
6. Click **Apply and Close**
7. Build Unity: **Ctrl+B**

### B.4 Run Unit Tests in Renode (F412dsc)

1. Open terminal:
   ```bash
   cd /opt/proj_mp/dk5u_prn_generation_in_c/renode/
   renode
   ```
2. In Renode Monitor:
   ```
   s @unity_dk5u_prn_generation_in_c_f412dsc.resc
   ```
3. Check UART output for test results

### B.5 Incremental Build-Test-Screenshot Cycle

After each LLM implementation:
1. In CubeIDE: **Ctrl+B** (rebuild Unity)
2. In Renode: Reset or re-run script
3. Capture screenshot at each artifact point (A1, A2, A3)

### B.6 Run Unity on G431n32 — Real Board (for A4)

No Renode script exists for G431n32, so unit tests run on the **real Nucleo-32 board**.

1. Connect G431 Nucleo-32 board via USB
2. Open a serial terminal (Putty or minicom) on the board's serial port (typically `/dev/ttyACM0`, baud 115200)
3. In CubeIDE: select **dk5u_prn_generation_in_c_g431n32**, select **Unity** build config
4. Build: **Ctrl+B**
5. Right-click project → **Run As → STM32 C/C++ Application** (or **Debug As** if Run As is unavailable)
6. The serial terminal (Putty) shows Unity test output — should be 6 Tests, 0 Failures
7. Capture Putty screenshot → **a4.png**

### B.7 Run App on G431n32 — Real Board (for A5)

1. In CubeIDE: switch to **Debug** build config (NOT Unity)
2. Build: **Ctrl+B**
3. Right-click project → **Run As → STM32 C/C++ Application** (or Debug As)
4. In serial terminal (Putty): press any key to start
5. The UART shows `"Input a number between 100 and 10000 for PSC:"`
6. Type a PSC value (e.g., `1000`) and press **Enter** — observe LED4 blink rate change
7. Try another value (e.g., `5000`) to see different blink speed
8. Capture Putty screenshot showing the app output with at least one PSC input → **a5.png**

### B.8 Clean and Submit

1. In CubeIDE: Right-click each project → **Build Configurations → Clean All**
2. LLM creates submission ZIP

---

## Programming Task Details

### PT1: mp_prn_ini_c (15 pts)

**Function signature:**
```c
uint32_t mp_prn_ini_c(uint32_t *prn_reg, int *poly, int poly_n);
```

**What it does:**
- Initialize `*prn_reg` to all 1s for the effective bit width (determined by max value in `poly[]`)
- Set the static `reg_mask` to same value (e.g., `0x03FF` for poly [3,10])
- Return `reg_mask` (aliased as `a_reg_mask`)

**Test:** `test_prn_ini_c` — expects `{0x000F, 0x03FF}` for poly1=[3,4] and poly2=[3,10]

### PT2: mp_prn_tap_mask_c (15 pts)

**Function signature:**
```c
uint32_t mp_prn_tap_mask_c(int *poly, int poly_n);
```

**What it does:**
- Build a bitmask with 1s at positions `poly[i]-1` for each element of poly
- Set the static `tap_mask` to this value
- Return `tap_mask` (aliased as `a_tap_mask`)

**Example:** poly=[3,10] → bits at positions 2 and 9 → `(1<<2) | (1<<9)` = `0x0204`

**Test:** `test_prn_tap_mask_c` — expects `{(1<<2)+(1<<3), (1<<2)+(1<<9)}`

### PT3: mp_prn_gen_c (35 pts)

**Function signature:**
```c
bool mp_prn_gen_c(uint32_t *prn_reg);
```

**What it does (per call):**
1. Get value from `*prn_reg`
2. AND with `tap_mask` to get tapped bits
3. Sum the 1s using `mp_sum_of_1s()`, AND result with `1U` to get feedback bit (XOR of tapped bits)
4. Extract output bit = MSB of the n-bit register (bit at position of highest poly value minus 1)
5. Shift register left by 1 (LSB to MSB direction)
6. OR feedback bit into LSB (bit 0)
7. AND with `reg_mask` to keep within bit width
8. Write back to `*prn_reg`
9. Return output bit as bool

**Tests:** 4 tests using poly1 and poly2, checking both output bits and register states over 15 iterations

### PT4: App (5 pts)

**Embed Timer 4 callback** in `stm32g4xx_it.c` so `mp_TIM_Callback()` is called on each Timer 4 interrupt. This drives the PRN generator to control LED4 blinking on the G431n32 board.

---

## Submission Checklist

- [ ] A1: Screenshot — test_prn_ini_c passes (1/6)
- [ ] A2: Screenshot — tap_mask test also passes (2/6)
- [ ] A3: Screenshot — all 6 tests pass on F412dsc
- [ ] A4: Screenshot — all 6 tests pass on G431n32
- [ ] A5: Screenshot — App running on G431n32 (LED4 blinking)
- [ ] C1: Code for 3 functions in mp_prn_c.c
- [ ] Report PDF: `dk5u-report-lastname-firstname.pdf`
- [ ] Project ZIP: `dk5u-proj-lastname-firstname.zip`
