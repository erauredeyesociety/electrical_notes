# Lab 01 Procedure: Creating a "Hello from UART" Project

**Course:** MP-CC4D
**Instructor:** Jianhua Liu
**Term:** Spring 2026
**Total Points:** 100

> **Reference Documents:**
> - [SYSTEM_ANALYSIS.md](../SYSTEM_ANALYSIS.md) - Environment setup
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md) - Analysis methodology
> - [lab01_findings.md](./lab01_findings.md) - Artifact tracking
> - Original PDF: `mp-cc4d-lab1-mp-cc4d--hello-from-uart-26-01.pdf`

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Create folders, copy `.ioc` file |
| 2 | HUMAN | CubeMX: Open `.ioc` → Save As → Generate Code |
| 3 | LLM | Copy `lib/`, `src/`, `renode/` + update renode script |
| 4 | HUMAN | CubeIDE: Import, add hook, create lib_src, add paths, link files, build |
| 5 | HUMAN | Renode: Run simulation |
| → | **ARTIFACT** | **A1:** Screenshot of UART2 showing `Hello World!` and `Input a string:` |
| 6 | LLM | Write Task 3 code (`cc4d_hello_from_uart_app.c`) |
| 7 | HUMAN | CubeIDE: Rebuild → Renode: Test with YOUR NAME |
| → | **ARTIFACT** | **A2:** Screenshot of UART2 showing name greeting with YOUR REAL NAME |

### Artifacts Required

| ID | Description | Where to Capture | Points |
|----|-------------|------------------|--------|
| **A1** | Screenshot of UART2 showing `Hello World!` and `Input a string:` | Step 5: Renode UART2 window | Task 2 (20 pts) |
| **A2** | Screenshot of UART2 showing name greeting with YOUR REAL NAME | Step 7: Renode UART2 window | Task 3 (20 pts) |
| **Code** | Source code from `cc4d_hello_from_uart_app.c` | After Step 6 | Task 3 (20 pts) |

### Expected Output

**Artifact 1 (A1):**
```
Hello World!
Input a string:
```

**Artifact 2 (A2):**
```
Hello from UART!
Please input your name (with '~' for space):
Your~Real~Name
Hello Your Real Name.
```

**Project Location:** `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/`

---

## Overview

This lab teaches creating an STM32 project from scratch using three DevTools:
- **CubeMX** - MCU peripheral configuration and code generation (GUI)
- **CubeIDE** - Project management, editing, and building (GUI)
- **Renode** - Simulation/emulation (GUI launched from terminal)

**Source Project:** `cc1s_uart_redirect` (in `/opt/proj_mp/`)
**Target Project:** `cc4d_hello_from_uart` (to be created in `/opt/proj_mp/`)

---

## Point Breakdown

| Task | Points | Description |
|------|--------|-------------|
| Task 1 | 50 | Creating the project from scratch |
| Task 2 | 20 | Building and running the executable |
| Task 3 | 20 | Adding new code functionality |
| Submission | 10 | Report format and completeness |

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| 1.1 | Create folder structure | CLAUDE CODE |
| 1.2 | Copy lib/, src/, renode/ folders | CLAUDE CODE |
| 1.3 | Rename files | CLAUDE CODE |
| 1.4 | Copy .ioc file | CLAUDE CODE |
| 1.5 | Open .ioc, Save Project As | HUMAN (CubeMX GUI) |
| 1.6 | Generate Code | HUMAN (CubeMX GUI) |
| 1.7 | Import project to CubeIDE | HUMAN (CubeIDE GUI) |
| 1.8 | Add hook in main.c | HUMAN (CubeIDE GUI) |
| 1.9 | Create lib_src folder | HUMAN (CubeIDE GUI) |
| 1.10 | Add include paths | HUMAN (CubeIDE GUI) |
| 1.11 | Link source files | HUMAN (CubeIDE GUI) |
| 2.1 | Build project | HUMAN (CubeIDE GUI) |
| 2.2 | Update Renode script | CLAUDE CODE |
| 2.3 | Run in Renode, take Artifact 1 | HUMAN (Renode GUI) |
| 3.1 | Write Task 3 code | CLAUDE CODE |
| 3.2 | Rebuild and test, take Artifact 2 | HUMAN (CubeIDE + Renode GUI) |

---

## Part A: Claude Code Automated Tasks

> These tasks are performed by Claude Code. Human should verify completion.

### A.1 Create Folder Structure

**Target structure:**
```
/opt/proj_mp/cc4d_hello_from_uart_f412dsc/
├── cc4d_hello_from_uart_f412dsc/    # For .ioc and CubeMX-generated code
├── lib/                              # Copied from cc1s_uart_redirect
├── renode/                           # Copied from cc1s_uart_redirect
└── src/                              # Copied from cc1s_uart_redirect
```

### A.2 Copy and Rename Files

**lib/** (copy as-is):
- `mp_supported_mcu.h`
- `mp_uart_redirect.c`
- `mp_uart_redirect.h`

**src/** (copy and rename):
- `_mp_main.c` (no rename needed)
- `cc1s_uart_redirect_app.c` → `cc4d_hello_from_uart_app.c`

**renode/** (copy and rename):
- `debug_cc1s_uart_redirect_f412dsc.resc` → `debug_cc4d_hello_from_uart_f412dsc.resc`
- `renode.sh` (copy as-is)

### A.3 Copy .ioc File

Copy from source to target (human will rename via CubeMX Save As):
- FROM: `/opt/proj_mp/cc1s_uart_redirect/cc1s_uart_redirect_f412dsc/cc1s_uart_redirect_f412dsc.ioc`
- TO: `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/`

### A.4 Update Renode Script

Update `renode/debug_cc4d_hello_from_uart_f412dsc.resc`:

```resc
using sysbus

mach create
machine LoadPlatformDescription @platforms/cpus/stm32f412.repl

$path?=  @../cc4d_hello_from_uart_f412dsc/STM32CubeIDE/Debug
$bin?= $path/cc4d_hello_from_uart_f412dsc.elf

showAnalyzer usart2

macro reset
"""
    sysbus LoadELF $bin
"""

runMacro $reset
```

### A.5 Write Task 3 Code

Write to `src/cc4d_hello_from_uart_app.c`:

```c
#include <stdio.h>
#include "mp_supported_mcu.h"
#include "mp_uart_redirect.h"

static void mp_str2name(char *str, char *name);

void mp_app(void) {
    printf("Hello from UART!\n");

    SET_STDIN_TO_NO_BUFFER;
    char str[50];
    char name[50];
    while (1) {
        printf("Please input your name (with '~' for space): \n");
        scanf("%s", str);
        mp_str2name(str, name);
        printf("Hello %s.\n", name);
    }
}

static void mp_str2name(char *str, char *name) {
    char ch;
    do {
        ch = *str++;
        if (ch == '~') {
            *name++ = ' ';
        } else {
            *name++ = ch;
        }
    } while (ch);
}
```

---

## Part B: Human Tasks (GUI Required)

> These tasks require GUI interaction. Follow steps exactly.

### B.1 CubeMX: Convert .ioc to Project

**IMPORTANT:** The `.ioc` file alone is NOT a buildable project. You must use CubeMX GUI to generate the STM32CubeIDE project files.

1. Open CubeMX (from Applications menu or terminal: `STM32CubeMX`)
2. **File -> Open Project**
3. Navigate to: `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/`
4. Open: `cc1s_uart_redirect_f412dsc.ioc` (the copied file)
5. **File -> Save Project As...**
6. Ensure location is: `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/`
7. Click **Save** (file auto-renames to `cc4d_hello_from_uart_f412dsc.ioc`)
8. Click **[GENERATE CODE]** button
9. Click **Close** (or Open Project for quick approach)
10. Delete old `.ioc` file: `cc1s_uart_redirect_f412dsc.ioc`

### B.2 CubeIDE: Import Project

1. Open CubeIDE (from Applications menu)
2. Set workspace to: `/opt/proj_mp`
3. **File -> Import...**
4. Select: **General -> Projects from Folder or Archive**
5. Click **Next**
6. Click **Directory...** and navigate to:
   ```
   /opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/STM32CubeIDE
   ```
7. Ensure **STM32CubeIDE** checkbox is checked
8. Click **Finish**

### B.3 CubeIDE: Add Hook Function

1. In Project Explorer, expand: `cc4d_hello_from_uart_f412dsc -> Application -> User`
2. Double-click `main.c` to open
3. Find `/* USER CODE BEGIN 2 */` section
4. Add these lines between the BEGIN and END markers:
   ```c
   void mp_main(void);
   mp_main();
   ```
5. Save file (Ctrl+S)

### B.4 CubeIDE: Create lib_src Folder

1. Right-click project title (`cc4d_hello_from_uart_f412dsc`)
2. Select: **New -> Folder**
3. Enter name: `lib_src`
4. Click **Finish**

### B.5 CubeIDE: Add Include Paths

1. Right-click project title
2. Select: **Properties**
3. Navigate: **C/C++ General -> Paths and Symbols**
4. Ensure Configuration shows: **Debug [Active]**
5. Click **Includes** tab
6. Under Languages, select: **GNU C**
7. Click **Add...**
8. Enter: `../../lib`
9. Check: **Add to all configurations**
10. Check: **Add to all languages**
11. Click **OK**
12. Click **Add...** again
13. Enter: `../../src`
14. Check both checkboxes again
15. Click **OK**
16. Click **Apply and Close**

### B.6 CubeIDE: Link Source Files

**Files to link:**

| Source File (full path) | Destination |
|-------------------------|-------------|
| `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/lib/mp_uart_redirect.c` | `lib_src` folder |
| `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/src/_mp_main.c` | `lib_src` folder |
| `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/src/cc4d_hello_from_uart_app.c` | `lib_src` folder |

**Method (New → File → Link):**

For each file, repeat these steps:

1. Right-click `lib_src` folder in Project Explorer
2. Select **New → File**
3. Click **Advanced >>** to expand options
4. Check **Link to file in the file system**
5. Click **Browse...** and navigate to the file:
   - First: `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/lib/mp_uart_redirect.c`
   - Second: `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/src/_mp_main.c`
   - Third: `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/src/cc4d_hello_from_uart_app.c`
6. Click **Open**, then **Finish**

**Verify:** `lib_src` folder should now show 3 linked files (with arrow overlay icon)

### B.7 CubeIDE: Build Project

1. Ensure **Debug** is selected in the build configuration dropdown
2. Click the **Build** button (hammer icon) or press **Ctrl+B**
3. Verify in Console: **0 errors, 0 warnings**
4. Output file created: `Debug/cc4d_hello_from_uart_f412dsc.elf`

### B.8 Renode: Run and Capture Artifact 1

**IMPORTANT:** Renode is a GUI application launched from terminal. Copy-paste the commands below.

**Terminal commands (copy and paste):**
```bash
cd /opt/proj_mp/cc4d_hello_from_uart_f412dsc/renode/
renode
```

**Renode Monitor command (type in Renode GUI window):**
```
s @debug_cc4d_hello_from_uart_f412dsc.resc
```

**Expected output in UART2 window:**
```
Hello World!
Input a string:
```

**ARTIFACT 1:** Take screenshot of UART2 window showing this output.

### B.9 Rebuild and Capture Artifact 2

After Claude Code writes the Task 3 code:

1. In CubeIDE, rebuild project (hammer icon)
2. In Renode (restart if needed):
   ```bash
   cd /opt/proj_mp/cc4d_hello_from_uart_f412dsc/renode/
   renode
   ```
   Then in Monitor:
   ```
   s @debug_cc4d_hello_from_uart_f412dsc.resc
   ```
3. In UART2 window, type your name with `~` for spaces:
   ```
   Your~Real~Name
   ```
4. Expected output:
   ```
   Please input your name (with '~' for space):
   Your~Real~Name
   Hello Your Real Name.
   ```

**ARTIFACT 2:** Take screenshot of UART2 window showing conversation with YOUR REAL NAME.

---

## Submission Checklist

### PDF Report: `cc4d-report-lastname-firstname.pdf`

- [ ] Source code from `cc4d_hello_from_uart_app.c`
- [ ] Artifact 1 screenshot (Hello World)
- [ ] Artifact 2 screenshot (with your real name)

### ZIP File: `cc4d-proj-lastname-firstname.zip`

Before zipping:
1. In CubeIDE: Right-click project -> **Build Configurations -> Clean All**
2. Then zip the entire `cc4d_hello_from_uart_f412dsc` folder

**Zip command (copy and paste):**
```bash
cd /opt/proj_mp/
zip -r cc4d-proj-lastname-firstname.zip cc4d_hello_from_uart_f412dsc/
```

---

## Quick Reference: Key Paths

```
Source Project:
  /opt/proj_mp/cc1s_uart_redirect/

Target Project:
  /opt/proj_mp/cc4d_hello_from_uart_f412dsc/
  ├── cc4d_hello_from_uart_f412dsc/
  │   ├── cc4d_hello_from_uart_f412dsc.ioc
  │   └── STM32CubeIDE/
  │       └── Debug/
  │           └── cc4d_hello_from_uart_f412dsc.elf
  ├── lib/
  ├── src/
  │   └── cc4d_hello_from_uart_app.c
  └── renode/
      └── debug_cc4d_hello_from_uart_f412dsc.resc

Lab Documentation:
  /opt/proj_mp/labs/lab01/
```
