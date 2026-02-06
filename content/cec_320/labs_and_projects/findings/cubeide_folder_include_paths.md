# CubeIDE Folder-Level Include Path Override Issue

**Date:** 2026-02-04
**Source:** Web research + hands-on debugging

---

## Problem

When adding include paths at the **project level** in STM32CubeIDE, source folders (like `lib_src`) can have their own **folder-level settings** that override the project settings. This causes the wrong include paths to be used during compilation.

## Symptom

- Project Properties → C/C++ General → Paths and Symbols shows correct paths (e.g., `../../lib`)
- But compilation fails with "file not found" errors
- Inspecting the generated makefile (`Debug/lib_src/subdir.mk`) shows wrong paths (e.g., `../../../lib_src` instead of `../../../lib`)

## Root Cause

Eclipse CDT (which CubeIDE is based on) supports **per-folder build settings**. When you create a virtual source folder and link files to it, that folder can inherit default settings that differ from project-level settings.

The `.cproject` file contains `<folderInfo>` sections for each source folder, and these can have their own include path configurations.

## How to Diagnose

1. Check the generated makefile:
   ```bash
   cat Debug/lib_src/subdir.mk | grep -I
   ```

2. Look for folder-specific settings in `.cproject`:
   ```bash
   grep -A50 'resourcePath="lib_src"' .cproject | grep includepaths
   ```

3. In CubeIDE GUI:
   - Right-click the **folder** (not project) → Properties
   - C/C++ General → Paths and Symbols
   - Compare with project-level settings

## Solution

### Option 1: Edit .cproject directly (quick fix)

Replace the wrong paths in the `.cproject` file:
```bash
# Replace lib_src with lib in include paths
sed -i 's|../../../lib_src|../../../lib|g' .cproject
```

### Option 2: Fix via GUI

1. Right-click the `lib_src` folder (not the project!)
2. Properties → C/C++ General → Paths and Symbols
3. Under "Includes", check/fix the entries
4. Or click "Restore Defaults" to inherit from project

### Option 3: Use Eclipse Variables (recommended for portability)

Instead of relative paths like `../../lib`, use:
```
${ProjDirPath}/../../lib
```

This uses the Eclipse macro system which resolves paths more reliably.

## Path Relativity in CubeIDE

| Context | Paths Relative To |
|---------|-------------------|
| Project Properties GUI | Project root (where `.project` is) |
| Makefile/Compiler | Build directory (e.g., `Debug/`) |
| `.cproject` file | Depends on the `resourcePath` context |

For a project structure:
```
project_root/
├── inner_folder/
│   └── STM32CubeIDE/      ← .project here
│       └── Debug/         ← Compiler runs from here
├── lib/                   ← Headers here
└── src/
```

- In GUI: Enter `../../lib` (from STM32CubeIDE to lib)
- In makefile: Becomes `../../../lib` (from Debug to lib)

---

## Sources

- [ST Community: Relative and Absolute Paths](https://community.st.com/t5/stm32cubeide-mcus/relative-and-absolute-paths-in-stm32cubeide/td-p/82185)
- [ST Community: Include path don't work](https://community.st.com/t5/stm32cubeide-mcus/include-path-don-t-work/td-p/694015)
- [Eclipse CDT Project Portability](https://eclipse-embed-cdt.github.io/eclipse/project/portability/)
