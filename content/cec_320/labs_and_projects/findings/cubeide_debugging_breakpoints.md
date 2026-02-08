# STM32CubeIDE Debugging and Breakpoints Reference

**Date:** 2026-02-07
**Context:** Lab 02 (ce5d_debug_fib) on NUCLEO-G431KB, CEC 320

---

## 1. Debug Configurations: Selecting the Correct Project

### The Problem

STM32CubeIDE (Eclipse-based) remembers the **last launched debug configuration**. When multiple projects exist in the workspace (e.g., `cb4a_str_case_cvt`, `ce5d_debug_fib_g431n32`, `ca4b_cls_projs_g431n32`), clicking the Debug button (bug icon) re-launches whichever configuration ran most recently -- NOT necessarily the project currently open in the editor. This is the most common reason for accidentally debugging `cb4a_str_case_cvt` when you intend to debug `ce5d_debug_fib`.

### How Debug Configurations Work

Each CubeIDE project with an STM32 target gets a **debug configuration** (also called a "launch configuration"). It is stored in the workspace metadata (`.metadata/.plugins/org.eclipse.debug.core/.launches/`) and specifies:

- **The ELF binary** to flash (e.g., `Debug/ce5d_debug_fib_g431n32.elf`)
- **The target MCU** (STM32G431KB)
- **The debug probe** (ST-LINK, SWD interface)
- **GDB server settings** (port, reset behavior)
- **SVD file** for peripheral register viewing

### How to Select the Right Configuration

**Method 1: Drop-down arrow on Debug button (recommended)**

1. Click the **small down-arrow** next to the Debug button (bug icon) in the toolbar
2. A list of all available debug configurations appears
3. Select the one matching your target project (e.g., `ce5d_debug_fib_g431n32 Debug`)
4. CubeIDE now remembers this as the most recent configuration

**Method 2: Debug Configurations dialog**

1. **Run -> Debug Configurations...** (or right-click the debug button drop-down -> Debug Configurations...)
2. In the left panel, expand **STM32 C/C++ Application**
3. You will see one entry per project that has been debugged before
4. Select the correct configuration (e.g., `ce5d_debug_fib_g431n32 Debug`)
5. Verify the **C/C++ Application** field points to the correct `.elf` file
6. Click **Debug**

**Method 3: Project Explorer context menu**

1. In the **Project Explorer**, right-click the project you want to debug
2. Select **Debug As -> STM32 C/C++ Application**
3. This creates or reuses the debug configuration for that specific project

**Method 4: Make your project the active/selected project**

1. Click on the project name in Project Explorer to select it
2. Then click the Debug button -- CubeIDE may prefer the selected project's configuration
3. This behavior is not always reliable; Method 1 or 2 is more dependable

### Verifying Which Configuration is Active

After launching debug, check the **Debug view** (top-left pane in Debug perspective). It shows the configuration name in the tree root, for example:

```
ce5d_debug_fib_g431n32 Debug [STM32 C/C++ Application]
  arm-none-eabi-gdb (xxxx)
    Thread #1 (Suspended : Breakpoint)
      mp_app() at ce5d_debug_fib_app.c:30
```

If this shows `cb4a_str_case_cvt` instead of `ce5d_debug_fib`, you launched the wrong configuration. Terminate it (red square) and relaunch using Method 1 or 2.

---

## 2. Breakpoints: Setting, Removing, and Managing

### Setting Breakpoints

**Method 1: Double-click the gutter (most common)**

- Open the source file in the editor
- **Double-click** in the left margin (gutter) next to the line number
- A blue circle appears, indicating a breakpoint is set

**Method 2: Right-click context menu**

- Right-click the gutter next to the desired line
- Select **Toggle Breakpoint**

**Method 3: Keyboard shortcut**

- Place the cursor on the target line
- Press **Ctrl+Shift+B** to toggle a breakpoint

**Method 4: Run menu**

- Place the cursor on the target line
- **Run -> Toggle Breakpoint**

### Removing Breakpoints

- **Double-click** the blue circle in the gutter (toggles it off)
- Or right-click the breakpoint marker -> **Remove Breakpoint**
- Or select the breakpoint in the Breakpoints view and press **Delete**

### The Breakpoints View

Open via **Window -> Show View -> Breakpoints** (or it appears automatically in the Debug perspective).

The Breakpoints view shows **all breakpoints across all projects in the workspace**. This is critical to understand because breakpoints from `cb4a_str_case_cvt` will appear alongside breakpoints from `ce5d_debug_fib`.

Features of the Breakpoints view:

| Action | How |
|--------|-----|
| See all breakpoints | They are listed with file name and line number |
| Enable/disable a breakpoint | Check/uncheck the checkbox next to it |
| Remove a breakpoint | Select it, click the **X** (Remove) button |
| Remove ALL breakpoints | Click the **XX** (Remove All) button |
| Skip all breakpoints | Click the **Skip All Breakpoints** button (crossed-out circle) -- all breakpoints remain but none trigger |
| Go to source | Double-click a breakpoint to jump to its location |

### Breakpoint Types

| Type | Description | How to Set |
|------|-------------|------------|
| **Line breakpoint** | Pauses at a specific source line | Double-click gutter |
| **Conditional breakpoint** | Pauses only when a condition is true | Right-click breakpoint -> Breakpoint Properties -> Condition |
| **Hardware breakpoint** | Uses MCU hardware debug registers (limited count) | Right-click breakpoint -> Breakpoint Properties -> check "Hardware" |
| **Watchpoint** | Pauses when a variable is read or written | Run -> Add Watchpoint, or right-click variable -> Add Watchpoint |

### Hardware Breakpoint Limits

The STM32G431 (Cortex-M4) has **6 hardware breakpoint comparators**. STM32CubeIDE defaults to hardware breakpoints for flash-resident code. If you set more than 6 breakpoints, the debugger may:

- Silently fail to set some breakpoints
- Report an error: "Cannot insert breakpoint" or "No more HW breakpoints available"
- Fall back to software breakpoints (which require writable memory, not available in flash)

**Practical limit for Lab 02:** You need 4 breakpoints (BP1-BP4), which is well within the 6-breakpoint limit.

### Breakpoint Hit Count

Right-click a breakpoint -> **Breakpoint Properties** -> **Hit Count** lets you set the breakpoint to only trigger after N hits. Useful for loops.

---

## 3. Debug Perspective Controls

### Entering the Debug Perspective

When you launch a debug session, CubeIDE prompts to switch to the **Debug perspective**. Click **Switch** (or check "Remember my decision" and click Switch).

You can also manually switch:
- Click **Window -> Perspective -> Open Perspective -> Debug**
- Or click the **Debug** button in the perspective switcher bar (upper-right corner)

To return to the code editor: click the **C/C++** perspective button (upper-right).

### Debug Toolbar Controls

These are the primary execution controls in the Debug perspective toolbar (and under the **Run** menu):

| Button | Name | Shortcut | Description |
|--------|------|----------|-------------|
| Green triangle | **Resume** | **F8** | Continue execution until the next breakpoint or program end |
| Yellow pause | **Suspend** | -- | Pause a running program at its current location |
| Red square | **Terminate** | **Ctrl+F2** | Stop the debug session entirely |
| Step arrow over | **Step Over** | **F6** | Execute the current line; if it contains a function call, execute the entire function without entering it |
| Step arrow into | **Step Into** | **F5** | Execute the current line; if it contains a function call, enter the function and pause at its first line |
| Step arrow out | **Step Return** | **F7** | Execute until the current function returns, then pause at the caller |
| Arrow to line | **Run to Line** | **Ctrl+R** | Run until the cursor position is reached (acts as a temporary breakpoint) |
| Restart icon | **Restart** | -- | Reset the MCU and restart the debug session from the beginning |

### Execution Flow for Lab 02

The typical debug flow for this lab is:

1. **Launch debug** (bug icon) -- program is flashed and halted at `main()` or the first breakpoint
2. **Resume (F8)** -- runs to BP1 (the first `printf` in `mp_app`)
3. **Resume (F8)** -- runs to BP2 (first `mp_update_fib_array` call)
4. Inspect variables in the **Variables** view
5. **Resume (F8)** -- runs to BP3
6. Inspect global variables in the **Expressions** view
7. Continue as needed through BP4

### When to Use Step Over vs. Step Into

- **Step Over (F6):** Use when you want to execute a function call (like `printf` or `mp_update_fib_array`) as a single step without entering its source code. The function runs completely, and the debugger pauses at the next line in the current function.
- **Step Into (F5):** Use when you want to enter a function to see how it executes line-by-line. For `mp_update_fib_array`, this would take you inside the function to watch the Fibonacci computation loop.
- **Step Return (F7):** Use when you have stepped into a function and want to finish it quickly and return to the caller.

---

## 4. Debug Perspective Views

### Variables View

- Shows **local variables** of the currently paused function
- Variables update automatically when execution pauses
- Arrays can be expanded to see individual elements
- Values highlighted in **yellow** have changed since the last step/resume

### Expressions View

- Shows **user-specified expressions** (add by clicking "Add new expression" and typing the variable name)
- Use this for **global variables** that do not appear in the Variables view
- Can also evaluate arbitrary C expressions (e.g., `fibonacci_arr1[5]`, `sizeof(fibonacci_arr1)`)

### Registers View

- Shows all CPU registers (R0-R12, SP, LR, PC, xPSR)
- Useful for low-level debugging

### Memory View

- Click the **+** (Add Memory Monitor) button
- Enter a hex address (e.g., `0x20000000`) or a variable name (e.g., `&fibonacci_arr1`)
- Change the rendering: right-click the memory pane -> **Format** -> select **Unsigned Integer** for array data
- Can display in Hex, Signed/Unsigned Integer, Float, or Raw Hex

### Disassembly View

- Shows the assembly instructions corresponding to the current C source line
- Useful for understanding what the compiler generated

---

## 5. Common Pitfalls and Solutions

### Pitfall 1: Wrong Project Gets Debugged

**Symptom:** You click Debug expecting `ce5d_debug_fib` to run, but `cb4a_str_case_cvt` starts instead. The Debug view shows the wrong project name. Breakpoints in your file do not trigger.

**Cause:** CubeIDE launches the **most recently used** debug configuration by default.

**Fix:**
1. **Terminate** the wrong session (red square or Ctrl+F2)
2. Use the **drop-down arrow** next to the Debug button
3. Select the correct configuration: `ce5d_debug_fib_g431n32 Debug`
4. Alternatively: right-click the correct project in Project Explorer -> **Debug As -> STM32 C/C++ Application**

**Prevention:** Before clicking Debug, glance at the debug button's tooltip. It shows the name of the configuration that will launch. You can also use **Run -> Debug Configurations** to set a default.

### Pitfall 2: Stale Breakpoints from Other Projects

**Symptom:** The Breakpoints view shows breakpoints in files from `cb4a_str_case_cvt` or other old projects. These can cause confusion or consume hardware breakpoint slots.

**Fix:**
1. Open the **Breakpoints** view
2. Sort by file/resource to identify which breakpoints belong to which project
3. Select breakpoints from other projects and click **Remove** (X button)
4. Or click **Remove All** (XX button) and re-set only the ones you need

**Note:** The lab procedure (B.4, step 4) explicitly says "Remove leftover breakpoints from other projects."

### Pitfall 3: Breakpoints Set But Not Hit

**Symptom:** You set a breakpoint but the program runs past it without stopping.

**Possible causes and fixes:**

| Cause | Fix |
|-------|-----|
| Breakpoint is **disabled** (empty circle, not filled) | Check the checkbox in Breakpoints view |
| **Skip All Breakpoints** is active | Check the Breakpoints view toolbar for the skip icon (toggle it off) |
| Wrong debug configuration (different project's ELF) | Verify the debug configuration matches your project |
| Code was modified but not rebuilt | Rebuild (Ctrl+B) before debugging |
| Breakpoint on an **optimized-out** line | Compiler optimization removed the line; set breakpoint elsewhere or disable optimization (use `-O0`) |
| Exceeded hardware breakpoint limit | Remove some breakpoints (max 6 on Cortex-M4) |

### Pitfall 4: Source Code Mismatch

**Symptom:** The debugger highlights the wrong line, or stepping behaves erratically.

**Cause:** The `.elf` file on the MCU does not match the source code shown in the editor. This happens when you edit code but forget to rebuild before debugging.

**Fix:** Always **rebuild (Ctrl+B)** after any code change, then launch a new debug session. CubeIDE normally rebuilds automatically when you click Debug, but if the build configuration is not set to auto-build, you may need to do this manually.

### Pitfall 5: "Target not responding" or ST-LINK Errors

**Symptom:** Debug session fails to start with errors about ST-LINK communication or target not responding.

**Possible fixes:**

1. **Unplug and replug** the NUCLEO board's USB cable
2. **Upgrade ST-LINK firmware:** CubeIDE may prompt this; accept the upgrade
3. **Check USB connection:** Use `lsusb` on Linux to verify the ST-LINK appears (vendor 0483)
4. **Close other debug sessions:** Only one debugger can connect to the ST-LINK at a time
5. **Hold RESET during connect:** If the target is in a bad state (e.g., infinite loop consuming power), hold the board's RESET button while starting the debug session, then release
6. **Check SWD wiring:** On NUCLEO boards the SWD connection is built-in, so this should not be an issue unless jumpers were changed

### Pitfall 6: Program Runs After Flashing (No Halt at Start)

**Symptom:** After clicking Debug, the program runs immediately without stopping at the first breakpoint or `main()`.

**Fix:** In **Run -> Debug Configurations -> Startup** tab, ensure these options are set:
- **Reset behavior:** "Software system reset" (or "Connect under reset")
- Check **"Set breakpoint at: main"** (or your desired initial halt point)
- Check **"Halt on exception"** for catching hard faults

---

## 6. NUCLEO-G431KB Specific Notes

### Board Details

- MCU: STM32G431KB (Cortex-M4, 170 MHz, 128 KB Flash, 32 KB SRAM)
- Built-in ST-LINK/V3 debugger on the NUCLEO board
- Connection: Micro-USB cable to the ST-LINK USB connector (not the user USB)
- Serial output: Virtual COM Port (VCP) through the same USB cable

### Debug Interface

- Uses **SWD** (Serial Wire Debug), 2-pin interface (SWDIO + SWCLK)
- On NUCLEO boards, SWD is routed through the on-board ST-LINK -- no external probe needed
- The ST-LINK acts as both the debug probe and the USB-to-UART bridge

### Serial Output (PuTTY)

- The VCP appears as `/dev/ttyACM0` (Linux) or a COM port (Windows)
- Baud rate depends on the UART configuration in CubeMX (commonly 115200)
- PuTTY must be connected **before** running the program to capture early output
- If PuTTY shows garbled text, verify the baud rate matches the CubeMX USART configuration

### Power and Reset

- Board is powered through the USB cable
- The blue user button (B1) is on pin PA0 or PB8 depending on the NUCLEO variant
- The black RESET button resets the MCU (useful if stuck in a hard fault)

### Firmware Upgrade

When connecting a NUCLEO board for the first time (or after a CubeIDE update), you may be prompted to upgrade the ST-LINK firmware. Accept the upgrade. If it fails:

1. Close CubeIDE
2. Run the standalone **STM32CubeProgrammer**
3. Use its ST-LINK firmware upgrade utility
4. Retry in CubeIDE

---

## 7. Quick Reference: Lab 02 Debug Workflow

```
1. Build the project                    Ctrl+B
2. Click Debug drop-down arrow          Verify it says "ce5d_debug_fib_g431n32 Debug"
3. Switch to Debug perspective          Click "Switch" when prompted
4. Check Breakpoints view               Remove stale breakpoints from other projects
5. Resume (F8)                          Run to BP1
6. [Take screenshot A1]
7. Resume (F8)                          Run to BP2
8. Variables view -> expand N[]
9. [Take screenshot A2]
10. Resume (F8)                         Run to BP3
11. Expressions view -> add fibonacci_arr1
12. [Take screenshot A3]
13. Resume (F8)                         Run to BP4
14. [Take screenshot A4 from PuTTY]
15. Memory view -> add array address
16. [Take screenshot A5]
17. Terminate (Ctrl+F2)
18. Fix bug, rebuild, repeat for A6
```

---

## 8. Keyboard Shortcuts Summary

| Action | Shortcut |
|--------|----------|
| Build | Ctrl+B |
| Debug (last config) | F11 |
| Resume | F8 |
| Suspend | (no default) |
| Terminate | Ctrl+F2 |
| Step Over | F6 |
| Step Into | F5 |
| Step Return | F7 |
| Run to Line | Ctrl+R |
| Toggle Breakpoint | Ctrl+Shift+B |
| Switch to Debug perspective | (click perspective button) |
| Switch to C/C++ perspective | (click perspective button) |

---

## Sources

- STM32CubeIDE is based on Eclipse CDT; debug configuration management follows Eclipse conventions
- ARM Cortex-M4 Technical Reference Manual (hardware breakpoint limits)
- ST UM2609: STM32CubeIDE User Guide (debug perspectives, launch configurations, breakpoint management)
- Lab 02 manual: mp-ce5d-lab2-cubeide-debug-4-fib-26-02.pdf
