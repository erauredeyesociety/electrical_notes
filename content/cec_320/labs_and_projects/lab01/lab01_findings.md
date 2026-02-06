# Lab 01 Findings: Hello from UART

**Student:** ____________________
**Date:** ____________________

---

## Artifact Tracking

| Artifact | Description | Points | Status | File/Location |
|----------|-------------|--------|--------|---------------|
| Artifact 1 | Screenshot of UART2 - "Hello World!" | Task 2 (20 pts) | [ ] | |
| Artifact 2 | Screenshot of UART2 - Your name greeting | Task 3 (20 pts) | [ ] | |
| Code 1 | Source code from cc4d_hello_from_uart_app.c | Task 3 (20 pts) | [ ] | |

---

## Artifact 1: UART2 Screenshot - Hello World

**Required for:** Task 2 - Building and running the executable (20 pts)

**Expected output:**
```
Hello World!
Input a string:
```

**Screenshot:**
<!--
Paste screenshot here or note file location
Example: ![Artifact 1](./screenshots/artifact1.png)
-->

**File location:** ____________________

**Notes:**
<!-- Any observations, issues encountered, etc. -->

---

## Artifact 2: UART2 Screenshot - Name Greeting

**Required for:** Task 3 - Add new code (20 pts)

**Expected output:**
```
Please input your name (with '~' for space):
{Your~Name}
Hello {Your Name}.
```

**Your actual input:** ____________________

**Screenshot:**
<!--
Paste screenshot here or note file location
Example: ![Artifact 2](./screenshots/artifact2.png)
-->

**File location:** ____________________

**Notes:**
<!-- Any observations, issues encountered, etc. -->

---

## Code Snippets

### cc4d_hello_from_uart_app.c

**Required for:** Task 3 - Add new code (20 pts)

**File path:** `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/src/cc4d_hello_from_uart_app.c`

```c
// Paste your final code here for the report

```

---

## Submission Mapping

| Report Section | Artifact(s) | Status |
|----------------|-------------|--------|
| Source Code | Code 1 (cc4d_hello_from_uart_app.c) | [ ] |
| Screenshot 1 | Artifact 1 (Hello World output) | [ ] |
| Screenshot 2 | Artifact 2 (Name greeting with YOUR name) | [ ] |

---

## Submission Files

### PDF Report

**Filename:** `cc4d-report-{lastname}-{firstname}.pdf`

Contents:
- [ ] Source code from cc4d_hello_from_uart_app.c
- [ ] Artifact 1 screenshot
- [ ] Artifact 2 screenshot (with your real name)

### ZIP File

**Filename:** `cc4d-proj-{lastname}-{firstname}.zip`

Before zipping:
- [ ] Cleaned build in CubeIDE (Build Configurations → Clean All)

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r cc4d-proj-{lastname}-{firstname}.zip cc4d_hello_from_uart_f412dsc/
```

---

## Execution Log

### Step 1: Create folder structure + copy .ioc (LLM)

**Date:** 2026-02-04

**Commands executed:**
```bash
# Create target folder structure
mkdir -p /opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc

# Copy .ioc file from source project
cp /opt/proj_mp/cc1s_uart_redirect/cc1s_uart_redirect_f412dsc/cc1s_uart_redirect_f412dsc.ioc \
   /opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/
```

**Result:**
```
/opt/proj_mp/cc4d_hello_from_uart_f412dsc/
└── cc4d_hello_from_uart_f412dsc/
    └── cc1s_uart_redirect_f412dsc.ioc   ← Ready for CubeMX Save As
```

**Status:** ✓ Complete

---

### Step 2: CubeMX Save As + Generate Code (HUMAN)

**Date:** 2026-02-04

**Actions:**
- [x] Opened CubeMX
- [x] File → Open Project → `/opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/cc1s_uart_redirect_f412dsc.ioc`
- [x] File → Save Project As → (same folder, auto-renames to `cc4d_hello_from_uart_f412dsc.ioc`)
- [x] Clicked GENERATE CODE
- [x] Opened project in CubeIDE (via CubeMX popup)

**Result:** STM32CubeIDE/ folder created, project opened in CubeIDE

**Status:** ✓ Complete

---

### Step 3: Copy lib/, src/, renode/ (LLM)

**Date:** 2026-02-04

**Commands executed:**
```bash
# Create lib, src, renode folders
mkdir -p /opt/proj_mp/cc4d_hello_from_uart_f412dsc/{lib,src,renode}

# Copy lib files (as-is)
cp /opt/proj_mp/cc1s_uart_redirect/lib/* /opt/proj_mp/cc4d_hello_from_uart_f412dsc/lib/

# Copy src files (rename app.c)
cp /opt/proj_mp/cc1s_uart_redirect/src/_mp_main.c /opt/proj_mp/cc4d_hello_from_uart_f412dsc/src/
cp /opt/proj_mp/cc1s_uart_redirect/src/cc1s_uart_redirect_app.c \
   /opt/proj_mp/cc4d_hello_from_uart_f412dsc/src/cc4d_hello_from_uart_app.c

# Copy renode.sh
cp /opt/proj_mp/cc1s_uart_redirect/renode/renode.sh /opt/proj_mp/cc4d_hello_from_uart_f412dsc/renode/

# Create renode script (written via Write tool - see debug_cc4d_hello_from_uart_f412dsc.resc)

# Remove old .ioc file
rm /opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/cc1s_uart_redirect_f412dsc.ioc
```

**Result:**
```
/opt/proj_mp/cc4d_hello_from_uart_f412dsc/
├── cc4d_hello_from_uart_f412dsc/   ← CubeMX-generated
│   └── STM32CubeIDE/
├── lib/
│   ├── mp_supported_mcu.h
│   ├── mp_uart_redirect.c
│   └── mp_uart_redirect.h
├── src/
│   ├── _mp_main.c
│   └── cc4d_hello_from_uart_app.c
└── renode/
    ├── debug_cc4d_hello_from_uart_f412dsc.resc
    └── renode.sh
```

**Status:** ✓ Complete

---

### Step 4: CubeIDE configuration (HUMAN)

**Date:** ____________________

**Status:** [ ] Pending

---

### Step 5: Renode test + Artifact 1 (HUMAN)

**Date:** ____________________

**Status:** [ ] Pending

---

### Step 6: Write Task 3 code (LLM)

**Date:** ____________________

**Commands executed:**
```bash
# To be filled after Step 5
```

**Status:** [ ] Pending

---

### Step 7: Rebuild + Artifact 2 (HUMAN)

**Date:** ____________________

**Status:** [ ] Pending

---

## Notes and Observations

<!-- Use this section for any additional notes, issues encountered, or observations during the lab -->

### Issues Encountered

### Solutions Applied

### Questions for TA/Instructor
