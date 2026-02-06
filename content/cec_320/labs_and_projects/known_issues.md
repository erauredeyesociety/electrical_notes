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

## Template for New Issues

```markdown
### Issue: [Brief description]

**Symptom:** [What you observe]

**Cause:** [Root cause if known]

**Solution:** [Step-by-step fix]

**Date discovered:** YYYY-MM-DD
**Affected labs/projects:** [list]
```
