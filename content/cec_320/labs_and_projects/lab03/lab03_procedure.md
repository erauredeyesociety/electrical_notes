# Lab 03 Procedure: More CubeIDE Operations

**Course:** CEC 320 / MP-CI5D
**Points:** 100 (PC/MT 40 + DT 50 + Submission 10)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - [known_issues.md](../known_issues.md)
> - Original PDF: `mp-ci5d-lab3-more-cubeide-operations-26-02.pdf`

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract `ci5d_more_cubeide-files.zip` to `/opt/proj_mp/` |
| 2 | HUMAN | CubeMX: Open both `.ioc` files → Generate Code (PC1, 5 pts) |
| 3 | HUMAN | CubeIDE: Import both projects, add include paths, create `lib_src`, link source files (except `ci1s_ptr_funs_index.c`), add hook to `main.c`, build Debug for both (MT1, 10 pts) |
| 4 | HUMAN | CubeIDE: Define `CubeIDE` preprocessor symbol for all configs, both MPBs (MT2, 5 pts) |
| 5 | HUMAN | Build Debug for both MPBs. Run F412 in Renode, G431 on board. Resize windows side by side (MT3, 5 pts) |
| → | **ARTIFACT** | **A1:** Screenshot of both MPB outputs side by side |
| 6 | HUMAN | CubeIDE: Link `ci1s_ptr_funs_index.c` to `lib_src`, create `DebugIndex` build config, exclude files per config (MT4, 15 pts) |
| 7 | HUMAN | Build both Debug and DebugIndex. Run DebugIndex — notice `message` is wrong after `mp_strcpy` |
| 8 | HUMAN | Debug DebugIndex: set breakpoint at `mp_strcpy(message, hello)`, step into, watch `message` in Expressions (DT1, 15 pts) |
| → | **ARTIFACT** | **A2:** Screenshot of first 15 elements of `message` in Expressions view |
| 9 | LLM | Fix bug in `ci1s_ptr_funs_index.c` (double `i++` in `mp_strcpy`) |
| 10 | HUMAN | Rebuild DebugIndex, verify Debug and DebugIndex produce same output |
| 11 | HUMAN | Debug: hover over `message` before and after `mp_strcpy` call (DT2, 5 pts) |
| → | **ARTIFACT** | **A3:** Screenshots of hover values (before and after) |
| 12 | HUMAN | Remove all breakpoints. Set breakpoint at `free(heap_arr);` in `ci5d_info_print_funs.c`. Run to breakpoint. Get `heap_arr` address from Variables view (DT3, 30 pts) |
| 13 | HUMAN | Memory view: Word-based (Row 16, Col 4, Hex Integer) |
| → | **ARTIFACT** | **A4:** Screenshot of word-based memory view |
| 14 | HUMAN | Memory view: Halfword-based (Col 2) |
| → | **ARTIFACT** | **A5:** Screenshot of halfword-based memory view |
| 15 | HUMAN | Memory view: Byte-based (Col 1) |
| → | **ARTIFACT** | **A6:** Screenshot of byte-based memory view |
| 16 | LLM | Create submission ZIP, update report |

---

## Task Classification Summary

| Task | Description | Points | Who |
|------|-------------|--------|-----|
| PC1 | Project creation for two MPBs | 5 | HUMAN (CubeMX) |
| MT1 | Basic CubeIDE management | 10 | HUMAN (CubeIDE) |
| MT2 | MPB and DevTool specific build | 5 | HUMAN (CubeIDE) |
| MT3 | Running code on multiple MPBs | 5 | HUMAN (Renode + board) |
| MT4 | Multiple builds via source file selection | 15 | HUMAN (CubeIDE) |
| DT1 | Stepping through program line by line | 15 | HUMAN (debug) |
| DT2 | Checking results without printing | 5 | HUMAN (debug) |
| DT3 | Displaying memory in different formats | 30 | HUMAN (debug) |
| Submission | Report + ZIP | 10 | HUMAN + LLM |

---

## Zip Contents Analysis

```
ci5d_more_cubeide/
├── ci5d_more_cubeide_f412dsc/
│   └── ci5d_more_cubeide_f412dsc.ioc     # F412 Discovery board
├── ci5d_more_cubeide_g431n32/
│   └── ci5d_more_cubeide_g431n32.ioc     # G431 Nucleo-32 board
├── lib/
│   ├── mp_supported_mcu.h
│   ├── mp_uart_redirect.c
│   └── mp_uart_redirect.h
├── src/
│   ├── _mp_main.c                         # Dispatcher (mp_app/mp_unity)
│   ├── ci5d_more_cubeide_app.c           # Main app code
│   ├── ci5d_info_print_funs.c            # MCU/tool info + heap/stack printing
│   ├── ci5d_info_print_funs.h
│   ├── ci1s_ptr_funs.c                   # Pointer-based mp_strcpy (CORRECT)
│   ├── ci1s_ptr_funs.h
│   └── ci1s_ptr_funs_index.c            # Index-based mp_strcpy (BUGGY)
├── renode/
│   ├── debug_more_cubeide_f412dsc.resc   # Debug build Renode script
│   ├── debugindex_more_cubeide_f412dsc.resc  # DebugIndex build Renode script
│   └── renode.sh
└── create_proj.bat
```

---

## Part A: LLM Automated Tasks

### A.1 Extract Project ZIP (Step 1)

```bash
cd /opt/proj_mp/
unzip ~/electrical_notes/content/cec_320/labs_and_projects/lab03/ci5d_more_cubeide-files.zip
```

This creates `/opt/proj_mp/ci5d_more_cubeide/` with both .ioc files and all source.

### A.2 Fix Bug in ci1s_ptr_funs_index.c (Step 9)

**The bug:** `i` is incremented twice per loop iteration — once in `dst[i++] = ch` and once in `ch = src[i++]`. This skips every other character and writes to every other position.

**Buggy code:**
```c
void mp_strcpy(char *dst, char *src) {
    int i = 0;
    char ch = src[i];
    while (ch) {
        dst[i++] = ch;    // i goes 0→1
        ch = src[i++];     // i goes 1→2, reads src[1], skips to i=2
    }
}
```

**Fixed code:**
```c
void mp_strcpy(char *dst, char *src) {
    int i = 0;
    char ch = src[i];
    while (ch) {
        dst[i] = ch;
        i++;
        ch = src[i];
    }
    dst[i] = '\0';
}
```

---

## Part B: Human Tasks (GUI Required)

### B.1 PC1: Project Creation for Two MPBs (5 pts)

**After LLM extracts the zip:**

1. Open CubeMX
2. Open `/opt/proj_mp/ci5d_more_cubeide/ci5d_more_cubeide_f412dsc/ci5d_more_cubeide_f412dsc.ioc`
3. Click **GENERATE CODE** → When prompted, open in CubeIDE
4. Open `/opt/proj_mp/ci5d_more_cubeide/ci5d_more_cubeide_g431n32/ci5d_more_cubeide_g431n32.ioc`
5. Click **GENERATE CODE** → When prompted, open in CubeIDE
6. Both projects should now be in the CubeIDE workspace

**Tip:** Do both side by side — open both .ioc files and generate both before moving on.

### B.2 MT1: Basic CubeIDE Management (10 pts)

**For BOTH MPBs (`ci5d_more_cubeide_f412dsc` and `ci5d_more_cubeide_g431n32`):**

**Step 1: Add include paths**

1. Right-click project → **Properties → C/C++ General → Paths and Symbols → Includes**
2. Select **GNU C** language
3. Click **Add...** → enter `../../../lib` → check **Add to all configurations** + **Add to all languages** → OK
4. Click **Add...** → enter `../../../src` → check **Add to all configurations** + **Add to all languages** → OK
5. Click **Apply and Close**

**Step 2: Create lib_src folder**

1. Right-click project → **New → Source Folder**
2. Name: `lib_src`
3. Click **Finish**

**Step 3: Link source files to lib_src**

Use **New → File → Advanced → Link to file in the file system** for each file:

| Source File (full path) | Destination |
|-------------------------|-------------|
| `/opt/proj_mp/ci5d_more_cubeide/lib/mp_uart_redirect.c` | `lib_src` |
| `/opt/proj_mp/ci5d_more_cubeide/src/ci5d_info_print_funs.c` | `lib_src` |
| `/opt/proj_mp/ci5d_more_cubeide/src/ci5d_more_cubeide_app.c` | `lib_src` |
| `/opt/proj_mp/ci5d_more_cubeide/src/ci1s_ptr_funs.c` | `lib_src` |
| `/opt/proj_mp/ci5d_more_cubeide/src/_mp_main.c` | `lib_src` |

**DO NOT link `ci1s_ptr_funs_index.c` yet** — that comes in MT4.

**Step 4: Add hook function to main.c**

In each project's `Src/main.c`, find `/* USER CODE BEGIN 2 */` and add:
```c
/* USER CODE BEGIN 2 */
void mp_main(void);
mp_main();
/* USER CODE END 2 */
```

**Step 5: Build**

Build the **Debug** configuration for both MPBs (Ctrl+B). Verify no errors.

### B.3 MT2: MPB and DevTool Specific Build (5 pts)

**For BOTH MPBs, ALL build configurations:**

1. Right-click project → **Properties → C/C++ Build → Settings**
2. Select **Tool Settings** tab → **MCU GCC Compiler → Preprocessor**
3. In **Defined symbols (-D)**, click **Add (+)** → enter `CubeIDE`
4. Check **Add to all configurations** if available, otherwise repeat for each config
5. Click **Apply and Close**

This enables the `#if defined(CubeIDE)` branch in `ci5d_info_print_funs.c`.

### B.4 MT3: Running Code on Multiple MPBs (5 pts)

**F412 (Renode):**
```bash
cd /opt/proj_mp/ci5d_more_cubeide/renode/
renode
```
In Renode Monitor:
```
s @debug_more_cubeide_f412dsc.resc
```

**G431 (Physical board):**
1. Connect NUCLEO-G431KB via USB
2. Open PuTTY for serial output
3. In CubeIDE: right-click `ci5d_more_cubeide_g431n32` → **Debug As → STM32 C/C++ Application**
4. Resume (F8) to run

**Expected output (both boards):**
```
Running ci5d: More CubeIDE Operations:---

MCU is STM32F412. / MCU is STM32G431.
Built by CubeIDE.

The approximate start address of stack is: 0x...
The value of my local var is: 0x12345678

The approximate start address of heap is: 0x...

Print selected values of the heap array:
0x12345678  0x01234567  0x00123456  0x00012345

Hello world!
```

Resize Renode and PuTTY windows side by side.

**ARTIFACT A1:** Screenshot of both outputs side by side → save as `a1.png`

### B.5 MT4: Multiple Builds via Source File Selection (15 pts)

**For BOTH MPBs:**

**Step 1: Link the index-based file**

1. Right-click `lib_src` → **New → File → Advanced → Link to file in the file system**
2. Browse to `/opt/proj_mp/ci5d_more_cubeide/src/ci1s_ptr_funs_index.c`
3. Click **Finish**

**Step 2: Create DebugIndex build configuration**

1. Right-click project → **Build Configurations → Manage...**
2. Click **New...** → Name: `DebugIndex` → Copy settings from: `Debug` → OK
3. Click **OK** to close

**Step 3: Exclude files per configuration**

For the **Debug** configuration:
1. Right-click `ci1s_ptr_funs_index.c` in `lib_src` → **Resource Configurations → Exclude from Build...**
2. Check **Debug** → OK

For the **DebugIndex** configuration:
1. Right-click `ci1s_ptr_funs.c` in `lib_src` → **Resource Configurations → Exclude from Build...**
2. Check **DebugIndex** → OK

**Step 4: Build both configs**

1. Select **Debug** build config → Build (Ctrl+B) → verify success
2. Select **DebugIndex** build config → Build → verify success

### B.6 DT1: Stepping Through Program Line by Line (15 pts)

1. Run both **Debug** and **DebugIndex** builds — notice DebugIndex gives wrong `message` output
2. Switch to **DebugIndex** config
3. Set breakpoint at `mp_strcpy(message, hello);` in `ci5d_more_cubeide_app.c`
4. Right-click project → **Debug As → STM32 C/C++ Application**
5. Resume to breakpoint → **Step Into (F5)** to enter `mp_strcpy`
6. In **Expressions** view, add `message` → expand to see character elements
7. **Step through** the function line by line, watching how `message` elements change
8. **ARTIFACT A2:** Screenshot of first 15 elements of `message` in Expressions view → save as `a2.png`
9. Identify the bug: `i` increments twice per iteration (see Part A.2 for fix)

**After LLM fixes the bug:** Rebuild both configs, verify Debug and DebugIndex produce identical output.

### B.7 DT2: Checking Results Without Printing (5 pts)

1. Set breakpoint at `mp_strcpy(message, hello);`
2. Debug → Resume to breakpoint
3. **Hover** mouse over `message` variable → see its value (before mp_strcpy)
4. **Step Over (F6)** the mp_strcpy call
5. **Hover** mouse over `message` again → see updated value (after mp_strcpy)
6. **ARTIFACT A3:** Screenshots of hover values before and after → save as `a3.png` (or `a3a.png` + `a3b.png`)

### B.8 DT3: Displaying Memory in Different Formats (30 pts)

1. **Remove all breakpoints:** Breakpoints tab → click **Remove All Breakpoints** (double-cross icon)
2. Set breakpoint at `free(heap_arr);` in `ci5d_info_print_funs.c`
3. Debug → Resume to breakpoint
4. In **Variables** view, find `heap_arr` → note its hex address (the `int *` value)
5. Open **Memory** tab → click **[+] Add Memory Monitor** → enter the heap_arr address

**ARTIFACT A4: Word-based view**
- In memory rendering, right-click → **Format...**
- **Row Size:** 16, **Column Size:** 4
- Add **New Renderings → Hex Integer**
- You should see 4 values per row: `12345678`, `01234567`, `00123456`, `00012345`
- Screenshot → save as `a4.png`

**ARTIFACT A5: Halfword-based view**
- Right-click → **Format...**
- **Column Size:** 2
- You'll see 8 halfwords per row: `5678`, `1234`, etc. (note Little Endian byte ordering)
- Screenshot → save as `a5.png`

**ARTIFACT A6: Byte-based view**
- Right-click → **Format...**
- **Column Size:** 1
- You'll see 16 bytes per row: `78`, `56`, `34`, `12`, etc. (Little Endian)
- Screenshot → save as `a6.png`

---

## Bug Analysis: ci1s_ptr_funs_index.c

**Pointer-based version (ci1s_ptr_funs.c) — CORRECT:**
```c
void mp_strcpy(char *dst, char *src) {
    char ch;
    do {
        ch = *src++;
        *dst++ = ch;
    } while (ch);
}
```
Each iteration: read one char, write one char, advance both pointers by 1.

**Index-based version (ci1s_ptr_funs_index.c) — BUGGY:**
```c
void mp_strcpy(char *dst, char *src) {
    int i = 0;
    char ch = src[i];
    while (ch) {
        dst[i++] = ch;    // writes dst[0], i becomes 1
        ch = src[i++];     // reads src[1], i becomes 2
    }
}
```
Each iteration: `i` is post-incremented TWICE, so it jumps by 2 instead of 1. Characters are written to even positions only and read from alternating positions.

---

## Submission Checklist

### PDF Report
**Filename:** `ci5d-report-lastname-firstname.pdf`

**Required contents:**
- [ ] A1: Both MPB outputs side by side
- [ ] A2: Expressions view of `message` (first 15 elements)
- [ ] A3: Hover values before and after mp_strcpy
- [ ] A4: Word-based memory view — explain relation to values using Little Endian
- [ ] A5: Halfword-based memory view — explain relation to A4 using Little Endian
- [ ] A6: Byte-based memory view — explain relation to A4 using Little Endian
- [ ] Corrected `ci1s_ptr_funs_index.c` code

### Project ZIP
**Filename:** `ci5d-proj-lastname-firstname.zip`

**Before zipping:**
1. In CubeIDE: Right-click project → **Build Configurations → Clean All**
2. Do this for **both** MPB projects

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r ci5d-proj-lastname-firstname.zip ci5d_more_cubeide/
```
