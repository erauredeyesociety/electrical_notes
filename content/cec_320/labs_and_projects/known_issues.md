# Known Issues and Solutions

**Purpose:** Document recurring issues and their solutions for future reference.

---

## CubeMX / CubeIDE Integration

### Issue: Missed "Open in CubeIDE" notification after Generate Code

**Symptom:** CubeMX shows a popup after code generation with option to open in CubeIDE, but you clicked away or closed it.

**Solution:** Import manually in CubeIDE (this is what CubeMX does behind the scenes):

1. Open CubeIDE
2. **File → Open Projects from File System...**
3. Click **Directory...** and navigate to the `STM32CubeIDE` folder inside your project:
   ```
   /opt/proj_mp/{project_name}/.../STM32CubeIDE
   ```
   (The exact path depends on project structure - look for the folder containing `.project` and `.cproject` files)
4. Ensure the project checkbox is selected
5. Click **Finish**

**Alternative method:**
1. **File → Import...**
2. Select **General → Existing Projects into Workspace**
3. Click **Next**
4. Browse to the `STM32CubeIDE` folder
5. Click **Finish**

**How to find the right folder:**
- The `STM32CubeIDE` folder is created by CubeMX during code generation
- It's inside the same folder as your `.ioc` file
- It contains `.project` and `.cproject` files (Eclipse project files)

**Note:** Both import methods are equivalent to what CubeMX does when you click "Open Project".

---

### Issue: Drag-and-drop file linking doesn't work in CubeIDE

**Symptom:** Dragging files from the file manager (Nautilus/Files) to CubeIDE's Project Explorer doesn't work - files don't appear in the destination folder, or the "File Operation" dialog never appears.

**Cause:** Drag-and-drop between external applications and Eclipse-based IDEs can be unreliable on Linux, especially with Wayland or certain GTK configurations.

**Solution:** Use CubeIDE's built-in link functionality via **New → File**:

**Recommended Method: New → File → Link to file system**
1. Right-click the destination folder (e.g., `lib_src`)
2. Select **New → File**
3. Click **Advanced >>** to expand options
4. Check **Link to file in the file system**
5. Click **Browse...** and navigate to the source file
6. Click **Open**, then **Finish**
7. Repeat for each file

**Note:** The Import method (`Import → File System → Create links in workspace`) may not work due to permissions or CubeIDE configuration issues. The **New → File** method is more reliable.

**Date discovered:** 2026-02-04
**Affected labs/projects:** Any project requiring linked source files

---

### Issue: Folder-level include paths override project settings

**Symptom:** Build fails with "file not found" errors (e.g., `fatal error: mp_supported_mcu.h: No such file or directory`) even though project-level include paths appear correct in Properties. The generated makefile shows wrong paths (e.g., `../../../lib_src` instead of `../../../lib`).

**Cause:** Eclipse CDT supports per-folder build settings. When you create a virtual source folder (like `lib_src`) and link files to it, that folder inherits default include path settings that may differ from project-level settings. The `.cproject` file contains `<folderInfo>` sections for each source folder with their own compiler settings.

**How to diagnose:**

1. Check the generated makefile for actual compiler flags:
   ```bash
   cat /path/to/project/STM32CubeIDE/Debug/lib_src/subdir.mk | grep "\-I"
   ```
   Look for paths like `-I../../../lib_src` (wrong) vs `-I../../../lib` (correct)

2. In CubeIDE, compare:
   - **Project** properties → Paths and Symbols → Includes
   - **Folder** properties (right-click `lib_src`) → Paths and Symbols → Includes

   If they differ, folder settings override project settings!

3. Search the `.cproject` file for folder-specific settings:
   ```bash
   grep -A50 'resourcePath="lib_src"' .cproject | grep includepaths
   ```

---

**Solution A: LLM/Command-Line Fix**

1. Edit `.cproject` directly to replace the wrong path:
   ```bash
   cd /path/to/project/STM32CubeIDE/

   # Replace lib_src with lib in include paths
   sed -i 's|../../../lib_src|../../../lib|g' .cproject
   ```

2. **CRITICAL:** Delete the **ENTIRE Debug folder** to force complete makefile regeneration:
   ```bash
   rm -rf Debug/
   ```

   **Note:** Deleting only `Debug/lib_src/` is NOT sufficient! CubeIDE caches makefiles and won't regenerate them unless the entire Debug folder is removed.

3. In CubeIDE: Close and reopen project, then Build (Ctrl+B)

**What the LLM actually ran:**
```bash
# Used Edit tool to replace all occurrences in .cproject:
# old: <listOptionValue builtIn="false" value="../../../lib_src"/>
# new: <listOptionValue builtIn="false" value="../../../lib"/>

# IMPORTANT: Delete ENTIRE Debug folder, not just lib_src subfolder
rm -rf /opt/proj_mp/cc4d_hello_from_uart_f412dsc/cc4d_hello_from_uart_f412dsc/STM32CubeIDE/Debug/
```

---

**Solution B: Human GUI Fix**

1. In CubeIDE Project Explorer, right-click the `lib_src` **folder** (NOT the project root!)
2. Select **Properties**
3. Navigate to **C/C++ General → Paths and Symbols**
4. Click the **Includes** tab
5. Under Languages, select **GNU C**
6. Look for entries like `../../lib_src` - these are WRONG
7. Select the wrong entry and click **Delete**
8. Click **Add...** and enter the correct path: `../../lib`
9. Check **Add to all configurations** and **Add to all languages**
10. Click **OK**, then **Apply and Close**
11. **Project → Clean** to remove old build files
12. **Ctrl+B** to rebuild

**Alternative GUI approach:**
1. Right-click `lib_src` folder → Properties
2. C/C++ General → Paths and Symbols
3. Click **Restore Defaults** button (if available) to inherit from project
4. Clean and rebuild

---

**Prevention:**

When adding include paths to a project with linked source folders:
1. Add paths at **project level** (right-click project, not folder)
2. ALWAYS check **"Add to all configurations"**
3. ALWAYS check **"Add to all languages"**
4. After adding, verify folder-specific settings match by checking lib_src Properties
5. If in doubt, check the generated makefile to see actual compiler flags

**Date discovered:** 2026-02-04
**Affected labs/projects:** Any project with linked source folders (lib_src pattern)
**See also:** [findings/cubeide_folder_include_paths.md](./findings/cubeide_folder_include_paths.md)

---

## STM32CubeMX Launcher

### Issue: STM32CubeMX won't start from PATH

**Symptom:** Running `STM32CubeMX` from any directory fails or shows Java errors.

**Cause:** The CubeMX launcher script uses a relative path for its JAR file, so it must be run from its installation directory.

**Solution:** Use a shell function instead of PATH (already configured in `~/.bashrc`):

```bash
STM32CubeMX() {
    (cd /usr/local/STMicroelectronics/STM32Cube/STM32CubeMX && ./STM32CubeMX "$@")
}
```

---

### Issue: Missing `_mp_main.c` in file linking causes `undefined reference to 'mp_main'`

**Symptom:** Build fails with linker error: `undefined reference to 'mp_main'`. The `main.c` hook calls `mp_main()` but the linker can't find its definition.

**Cause:** The `_mp_main.c` file (which defines `mp_main()` and dispatches to `mp_app()` or `mp_unity()`) was not linked into `lib_src` in CubeIDE. This file lives in the project's `src/` folder alongside the app source file and is easy to overlook.

**Solution:** Link the missing file into `lib_src`:

1. Right-click `lib_src` folder
2. **New → File → Advanced → Link to file in the file system**
3. Browse to `/opt/proj_mp/{project_name}/src/_mp_main.c`
4. Click **Finish**
5. Rebuild (**Ctrl+B**)

**Prevention:** When listing files to link in `lib_src`, always include ALL `.c` files from `src/` — not just the app file. Check for `_mp_main.c` which is the dispatcher between app and test modes.

**Date discovered:** 2026-02-07
**Affected labs/projects:** Lab 02 (ce5d_debug_fib), potentially any project with `src/_mp_main.c`

---

## Debugging

### Issue: Debug launches wrong project (wrong .elf)

**Symptom:** Clicking the Debug button (bug icon) launches a debug session for a different project than expected. The GDB console shows a path to the wrong project, e.g.:

```
Temporary breakpoint 5, main ()
    at /opt/proj_mp/cb4a_str_case_cvt/cb4a_str_case_cvt_g431n32/Src/main.c:75
```

**Cause:** CubeIDE's Debug button re-launches the **last-used debug configuration**, not the currently selected project. If you previously debugged a different project, clicking the bug icon will debug that old project again.

**Solution (recommended):** Right-click the correct project in Project Explorer → **Debug As → STM32 C/C++ Application**. This always launches the debug configuration for the selected project.

**Alternative:** Click the **dropdown arrow** next to the Debug button → **Debug Configurations...** → select the correct configuration under **STM32 C/C++ Application** → click **Debug**.

**Prevention:** Always use right-click → Debug As when switching between projects. The plain Debug button is only reliable when working with a single project.

**Date discovered:** 2026-02-07
**Affected labs/projects:** Any workspace with multiple STM32 projects

---

## CubeIDE Navigation

### Issue: Project Explorer disappeared (accidentally detached and closed)

**Symptom:** Right-clicked in Project Explorer and selected **Detach**, turning it into a floating window. Then closed the floating window. The Project Explorer is now completely gone from the IDE.

**Cause:** "Detach" undocks a view into a floating window. Closing that floating window removes the view entirely from the current perspective.

**Solution:** **Window → Show View → Project Explorer** from the menu bar. This restores it as a docked panel.

**If not in the list:** **Window → Show View → Other...** → type "Project Explorer" in the filter → select it → **Open**

**To reset the entire layout:** **Window → Perspective → Reset Perspective** restores all panels to their default positions.

**Date discovered:** 2026-02-26
**Affected labs/projects:** Any CubeIDE session

---

### Issue: Accidentally used "Go Into" in Project Explorer

**Symptom:** Right-clicked a folder in CubeIDE's Project Explorer and selected **Go Into**. The Project Explorer now only shows the contents of that one folder — the rest of the project tree is hidden.

**Cause:** "Go Into" is an Eclipse feature that zooms the Project Explorer into a subfolder, hiding everything else. It's easy to trigger accidentally from the right-click context menu.

**Solution:**
1. Look at the **Project Explorer toolbar** (small icons at the top of the explorer pane)
2. Click the **Back arrow** (←) to go back one level
3. Or click the **Up arrow** (↑) to go to the parent
4. Or right-click in the Project Explorer → **Go Home** to return to the full workspace root

**Alternative:** The keyboard shortcut **Alt+Left** may also navigate back.

**Date discovered:** 2026-02-26
**Affected labs/projects:** Any CubeIDE project

---

## Template for New Issues

```markdown
### Issue: [Brief description]

**Symptom:** [What you observe]

**Cause:** [Root cause if known]

**Solution:** [Step-by-step fix]

**Date discovered:** YYYY-MM-DD
**Affected labs/projects:** [list]
```
