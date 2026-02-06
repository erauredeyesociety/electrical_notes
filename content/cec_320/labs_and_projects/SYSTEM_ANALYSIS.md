# System Analysis: STM32 Development Environment

**Document Created:** 2026-02-04
**Last Updated:** 2026-02-04
**System Hostname:** err0r
**User:** devel

---

## Operating System

| Property | Value |
|----------|-------|
| OS | Ubuntu 22.04.5 LTS (Jammy Jellyfish) |
| Kernel | 6.8.0-90-generic |
| Architecture | x86_64 |

---

## STM32 DevTools Installation

### STM32CubeMX

| Property | Value |
|----------|-------|
| Installation Path | `/usr/local/STMicroelectronics/STM32Cube/STM32CubeMX/` |
| Binary | `/usr/local/STMicroelectronics/STM32Cube/STM32CubeMX/STM32CubeMX` |
| In PATH | Via shell function (see below) |
| Launch Method | Terminal: `STM32CubeMX` (GUI application) |

**Purpose:** MCU peripheral configuration, code generation, project skeleton creation from `.ioc` files.

**Note:** The launcher uses a relative path for the JAR file, so it must be run from its installation directory. The shell function in `~/.bashrc` handles this automatically.

### STM32CubeIDE

| Property | Value |
|----------|-------|
| Installation Path | `/opt/st/stm32cubeide_2.0.0/` |
| Binary | `/opt/st/stm32cubeide_2.0.0/stm32cubeide` |
| Wayland Binary | `/opt/st/stm32cubeide_2.0.0/stm32cubeide_wayland` |
| Version | 2.0.0 |
| In PATH | Yes (via `~/.bashrc` line 138) |
| Launch Method | Applications menu or terminal: `stm32cubeide` |

**Purpose:** Project management, code editing, building, debugging.

### Renode

| Property | Value |
|----------|-------|
| Binary | `/usr/bin/renode` |
| Version | 1.16.0.1573 |
| Build | 20ad06d9-202508030050 |
| Runtime | .NET 8.0.22 |
| Launch Method | Terminal: `renode` |

**Purpose:** Hardware emulation/simulation. Runs `.elf` binaries without physical MCU hardware.

---

## PATH Configuration (from ~/.bashrc)

```bash
# Line 132: Local binaries
export PATH="$HOME/.local/bin:$PATH"

# Line 138: STM32CubeIDE
export PATH="/opt/st/stm32cubeide_2.0.0/:$PATH"

# Lines 140-143: STM32CubeMX function (not PATH - must run from install dir)
STM32CubeMX() {
    (cd /usr/local/STMicroelectronics/STM32Cube/STM32CubeMX && ./STM32CubeMX "$@")
}
```

---

## Project Folder Structure

### Main Project Directory

```
/opt/proj_mp/                              # PRIMARY PROJECT ROOT
├── labs_and_projects/                     # DOCUMENTATION ONLY (no code)
│   ├── SYSTEM_ANALYSIS.md                 # This document
│   ├── LAB_PROJECT_ANALYSIS_PROCEDURE.md  # Analysis methodology
│   ├── analysis_prompt.md                 # Prompt template for LLM
│   ├── lab01/                             # Lab 01 documentation
│   │   ├── lab01_procedure.md             # Procedure document
│   │   ├── lab01_findings.md              # Findings/artifacts tracking
│   │   ├── mp-cc4d-lab1-*.pdf             # Lab PDF handout
│   │   └── lab01_about.jpg                # Whiteboard notes
│   ├── lab##/                             # Future labs
│   └── proj##/                            # Future projects
│
├── ca4b_cls_projs/                        # Demo/class projects
├── cb4a_str_case_cvt/                     # String case conversion project
├── cc1s_uart_redirect/                    # UART redirect demo (SOURCE for lab01)
├── cc4d_hello_from_uart/                  # Lab 01 project (actual code)
└── [future projects]/                     # All CubeIDE/CubeMX projects here
```

### Project Naming Convention

Projects follow the instructor's naming scheme:
- **cc** = Related to specific lecture
- **4** = Type 4 projects can run on Renode
- **d** = Class d projects need Debug configuration
- **_f412dsc** / **_g431n32** = Target MCU board suffix

Example: `cc4d_hello_from_uart_f412dsc`

### Standard Project Internal Structure

Each CubeMX-generated project follows this structure:

```
project_name/
├── project_name_f412dsc/        # MCU-specific folder
│   ├── project_name_f412dsc.ioc # CubeMX configuration
│   ├── STM32CubeIDE/            # CubeIDE project files
│   │   ├── Debug/               # Debug build output
│   │   │   └── *.elf            # Built executable
│   │   └── Application/         # Application code
│   ├── Drivers/                 # HAL drivers
│   ├── Inc/                     # Generated headers
│   └── Src/                     # Generated sources (main.c, etc.)
├── lib/                         # User library files (shared)
├── src/                         # User application code (shared)
└── renode/                      # Renode scripts
    └── debug_*.resc             # Renode launch script
```

---

## Other Notable Software

### ROS2 (Robot Operating System)

```bash
# Sourced in ~/.bashrc lines 129-130
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

- Version: Humble Hawksbill
- Workspace: `~/ros2_ws/`

### Node.js (NVM)

```bash
# Configured in ~/.bashrc lines 134-136
export NVM_DIR="$HOME/.nvm"
```

### SSH Configuration

- SSH agent auto-starts on shell login
- Key: `~/.ssh/id_git` (auto-added to agent)

---

## Important Notes for Claude Code

1. **Project Location:** All CubeMX/CubeIDE projects MUST be created in `/opt/proj_mp/` (NOT `~/proj_mp/`)

2. **Documentation Location:** All lab/project documentation goes in `/opt/proj_mp/labs_and_projects/` (NO code here)

3. **GUI Applications:** STM32CubeMX, STM32CubeIDE, and Renode are GUI applications. Provide copy-paste commands for human execution.

4. **Workspace Setting:** CubeIDE workspace should be set to `/opt/proj_mp/`

5. **Renode:** GUI application launched from terminal. Provide terminal commands AND Renode Monitor commands separately.

6. **.ioc Conversion:** Converting `.ioc` to CubeIDE project ALWAYS requires CubeMX GUI (no CLI alternative).

7. **Renode Scripts:** When modifying `.resc` files, paths are relative to the script location. Use `../` notation.

8. **USER CODE Sections:** When editing CubeMX-generated files like `main.c`, ONLY modify code within `/* USER CODE BEGIN */` and `/* USER CODE END */` markers.

9. **Analysis Workflow:** See `LAB_PROJECT_ANALYSIS_PROCEDURE.md` for how to analyze labs/projects.

---

## Quick Reference Commands

```bash
# Check STM32CubeMX location
which STM32CubeMX

# Check Renode version
renode --version

# Navigate to projects
cd /opt/proj_mp/

# Navigate to documentation
cd /opt/proj_mp/labs_and_projects/

# Run Renode script (from project's renode/ folder)
cd /opt/proj_mp/project_name/renode/
renode
# Then in Renode Monitor GUI:
# s @debug_project_name.resc
```

---

## Directory Permissions

The `/opt/proj_mp/` directory has mixed ownership:
- Some folders owned by `root`
- Some folders owned by `devel`

This may require `sudo` for certain operations or ownership changes.

---

## Version History

| Date | Changes |
|------|---------|
| 2026-02-04 | Fixed STM32CubeMX launcher: changed from PATH export to shell function (launcher uses relative JAR path) |
| 2026-02-04 | Initial system analysis document created |
