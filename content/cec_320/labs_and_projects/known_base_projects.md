# Known Base Projects

**Purpose:** Document base projects that labs and projects build upon. Each lab/project manual PDF references its base project — this file describes what those base projects are and how they work.

**Usage:** When analyzing a new lab/project, check this file to understand the base project's structure, build configurations, and any special setup requirements.

---

## ca4b_cls_projs

**Location:** `/opt/proj_mp/ca4b_cls_projs/`

**Purpose:** Shared base project for all class projects (Proj 1–6). Contains pre-configured build infrastructure so individual projects only require placing source files and linking them in CubeIDE — no CubeMX step needed.

### Structure

```
/opt/proj_mp/ca4b_cls_projs/
├── ca4b_cls_projs_f412dsc/          # STM32F412 board variant
│   ├── ca4b_cls_projs_f412dsc.ioc
│   ├── Drivers/
│   ├── Inc/
│   ├── Src/
│   └── STM32CubeIDE/
│       ├── proj0_src_test/          # Linked source folder for Proj0
│       ├── proj1_src_test/          # Linked source folder for Proj1
│       ├── ...                      # proj2–6, projx
│       ├── Proj0App/                # Build output: Proj0 application
│       ├── Proj0Unity/              # Build output: Proj0 unit tests
│       ├── Proj1App/                # Build output: Proj1 application
│       ├── Proj1Unity/              # Build output: Proj1 unit tests
│       └── ...                      # Proj2–6, Projx
├── ca4b_cls_projs_g431n32/          # STM32G431 board variant (same structure)
├── lib/                             # Shared library (Unity framework, UART, utilities)
├── proj0_src/                       # Proj0 source files (demo, pre-populated)
├── proj0_test/                      # Proj0 test files (demo, pre-populated)
├── proj1_src/                       # Proj1 source files (empty until populated)
├── proj1_test/                      # Proj1 test files (empty until populated)
├── proj2_src/ through proj6_src/    # Empty folders for future projects
├── proj2_test/ through proj6_test/  # Empty folders for future projects
├── projx_src/                       # Extra project source
├── projx_test/                      # Extra project tests
└── renode/                          # Renode simulation scripts
    ├── proj0App_f412dsc.resc
    ├── proj0Unity_f412dsc.resc
    ├── proj1App_f412dsc.resc
    ├── proj1Unity_f412dsc.resc
    └── ...
```

### Build Configurations

Each project N has two build configurations:

| Config | Purpose | Define |
|--------|---------|--------|
| `ProjNApp` | Application build | (none) |
| `ProjNUnity` | Unit test build | `UNIT_TEST` |

The `UNIT_TEST` define controls which entry point is called in `_mp_main.c`:
- Defined → calls `mp_unity()` (runs tests)
- Not defined → calls `mp_app()` (runs application)

### Include Paths (Pre-Configured)

All build configurations already include paths for **all** project source folders:

```
../../../lib
../../../proj0_src
../../../proj1_src
../../../proj2_src
../../../proj3_src
../../../proj4_src
../../../proj5_src
../../../proj6_src
../../../projx_src
```

**The human does NOT need to add include paths manually.** This differs from standalone CubeMX projects (like lab01's `cc4d_hello_from_uart`) where include paths must be set up during configuration.

### Renode Scripts (Pre-Configured)

Renode scripts for each project already exist in `/opt/proj_mp/ca4b_cls_projs/renode/`. They reference the ELF output from the corresponding build configuration.

**Example (Proj1Unity):**
```
s @proj1Unity_f412dsc.resc
```

### Workflow for New Projects Using This Base

1. **LLM:** Place source files in `projN_src/` and `projN_test/`
2. **HUMAN:** Link `.c` files into `projN_src_test/` in CubeIDE (use New → File → Link to file system)
3. **HUMAN:** Select `ProjNUnity` or `ProjNApp` build configuration
4. **HUMAN:** Build (Ctrl+B)
5. **HUMAN:** Run in Renode

### Key Differences from Standalone CubeMX Projects

| Aspect | Standalone (e.g., cc4d_hello_from_uart) | ca4b_cls_projs |
|--------|----------------------------------------|----------------|
| CubeMX step | Required (open .ioc → generate) | NOT needed |
| Include paths | Must be added manually | Pre-configured |
| Renode scripts | Must be created/updated | Pre-configured |
| Build configs | Created during CubeMX generation | Pre-configured |
| Source linking | Link into `lib_src/` folder | Link into `projN_src_test/` folder |

### Known Issues

- The `projN_src_test/` folders contain `subdir.mk` files but no source files until the human links them
- Drag-and-drop file linking is unreliable on Linux — use **New → File → Link to file system** (see [known_issues.md](./known_issues.md))

---

## Template for New Base Projects

```markdown
## {project_name}

**Location:** `/opt/proj_mp/{project_name}/`

**Purpose:** {brief description}

### Structure
{directory tree}

### Build Configurations
{list of build configs and their purposes}

### Include Paths
{pre-configured or manual setup required}

### Renode Scripts
{pre-configured or need creation}

### Workflow
{numbered steps for using this base project}

### Key Notes
{any special considerations}
```

---

## Version History

| Date | Changes |
|------|---------|
| 2026-02-07 | Added ca4b_cls_projs base project (discovered during Proj01 analysis) |
