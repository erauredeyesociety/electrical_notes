# Lab Final Findings

**Course:** CEC 322 / LG
**Project code:** lg_lab_final
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab_final_procedure.md](./lab_final_procedure.md)
> - Base zip: `lg_lab_final.zip`

> **Note:** No manual PDF was provided in the zip. Task descriptions are embedded in the source-file comments (notably the block at the bottom of `lg_lab_final_app.c`).

---

## Artifact Summary

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | Registers view at `ldr r1, [r0]` breakpoint in `task1_func_s` | Task 1.1 (4 pts) | [x] |
| A2 | Screenshot | Variables view at `_app.c` line 17, A in hex | Task 1.2 (4 pts) | [x] |
| A3 | Screenshot | Expressions view, pStr at line 19 + line 21 | Task 1.3 (4 pts) | [x] |
| A4 | Screenshot | Memory view ASCII at `0x20000000`, Task1_str1 address | Task 1.4 (4 pts) | [x] |
| A5 | Screenshot | 2/2 Unity tests pass on real G431 | Task 2 + Task 3 | [x] |
| C1 | Code | `task2_func_c` in `lg_lab_final_cfns.c` | Task 2 | [x] |
| C2 | Code | `task3_func_s` in `lg_lab_final_sfns.s` | Task 3 | [x] |

---

## Recorded Values (fill in during walkthrough)

| Subtask | Value | Notes |
|---------|-------|-------|
| 1.1 | r0 = `0x20007FE4` | pointer to local `A` on the stack (sp = 0x20007FE0, so r0 = sp + 4) |
| 1.2 | A = `0x78563412` | byte-swapped little-endian of `0x12345678` as expected |
| 1.3a | pStr @ line 19 = `0x2000000C` | address of `Task1_str1` |
| 1.3b | pStr @ line 21 = `0x2000002C` | address of `Task1_str2` |
| 1.4 | Task1_str1 starting addr = `0x2000000C` | matches pStr @ line 19 (since `pStr = Task1_str1;` is line 18) |

---

## Screenshot Artifacts

### A1: Registers view at asm breakpoint

**Required for:** Task 1.1 (4 pts)

**What to capture:**
- Debug perspective with `lg_lab_final_sfns.s` open
- Green arrow at `ldr r1, [r0]` (first instruction of `task1_func_s`)
- Registers view expanded showing at least r0 (the value you record)

**File to save:** [a1.png](./a1.png)

### A2: Variables view at _app.c line 17

**Required for:** Task 1.2 (4 pts)

**What to capture:**
- Green arrow on line 17 of `lg_lab_final_app.c` (the `printf("First executable...")`)
- Variables view with local `A` shown in **Hex** format
- Expected: `A = 0x78563412`

**File to save:** [a2.png](./a2.png)

### A3: Expressions view at lines 19 and 21

**Required for:** Task 1.3 (4 pts)

**What to capture:**
- Expressions view with `pStr` added, in **Hex** format
- Either one screenshot showing both pauses side by side, or two screenshots (a3a, a3b)
- The two values should differ — first is address of `Task1_str1`, second is `Task1_str2`

**File to save:** [a3.png](./a3.png) (or a3a.png + a3b.png)

### A4: Memory view ASCII rendering at 0x20000000

**Required for:** Task 1.4 (4 pts)

**What to capture:**
- Memory view with address tab at `0x20000000`
- ASCII (or Text) rendering selected
- Visible text: `Hello, this is <your name>.`
- Starting address of the `H` in `Hello` is the Task1_str1 address to record

**File to save:** [a4.png](./a4.png)

### A5: Unity tests pass on real G431

**Required for:** Task 2 + Task 3 completion

**What to capture:**
- Serial terminal (tio / PuTTY) output
- Shows `test_task2_func_c:PASS` and `test_task3_func_s:PASS`
- Final summary `2 Tests 0 Failures 0 Ignored / OK`

**File to save:** [a5.png](./a5.png)

---

## Code Snippet Artifacts

### C1: `task2_func_c` in `lg_lab_final_cfns.c`

**Required for:** Task 2

**Content:**

```c
int32_t task2_func_c(int *arr, int n) {
    int32_t sum = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) {
            sum += arr[i];
        }
    }
    return sum;
}
```

**Artifact file:** [c1.c](./c1.c)

### C2: `task3_func_s` in `lg_lab_final_sfns.s`

**Required for:** Task 3

**Content (Task 3 body):**

```
task3_func_s:
task3_func_s_loop:
    ldrb    r2, [r0], #1           @ ch = *src++
    strb    r2, [r1], #1           @ *dst++ = ch
    cmp     r2, #0                 @ ch == '\0' ?
    bne     task3_func_s_loop      @ loop until null copied
    bx      lr
```

**Artifact file:** [c2.s](./c2.s) (entire `_sfns.s` file, Task 1 unchanged + new Task 3 body)

---

## Submission Checklist

### PDF Report

**Filename:** unknown naming convention (no manual provided) — use e.g. `lg-lab-final-lastname-firstname.pdf`

**Required contents:**

- [ ] Your name in the report header (and in `Task1_str1`!)
- [ ] Screenshots A1–A5
- [ ] Recorded hex values for subtasks 1.1–1.4
- [ ] Task 2 code (C1) with clear comments
- [ ] Task 3 code (C2) with clear comments

### Project ZIP

**Filename:** `lg-lab-final-lastname-firstname.zip` (convention from prior labs)

**Before zipping:**

1. Edit `lg_lab_final_app.c` → `Task1_str1` with your real name
2. In CubeIDE: right-click project → **Build Configurations → Clean All**

**Project location:** `/opt/proj_mp/lg_lab_final/`

```bash
cd /opt/proj_mp
zip -r lg-lab-final-lastname-firstname.zip lg_lab_final/ \
    -x 'lg_lab_final/*/STM32CubeIDE/Debug/*' \
    -x 'lg_lab_final/*/STM32CubeIDE/Application/*' \
    -x 'lg_lab_final/*/STM32CubeIDE/Unity/*' \
    -x 'lg_lab_final/*/STM32CubeIDE/Soln4unity/*'
```

---

## Artifact-to-Report Mapping

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Task 1 — Debug walkthrough | A1, A2, A3, A4 | Each with recorded hex value |
| Task 2 — C code | C1 | `task2_func_c` source |
| Task 3 — asm code | C2 | `task3_func_s` source |
| Task 2 + Task 3 — Verification | A5 | Unity 2/2 pass |

---

## Resume State (as of 2026-04-22)

**LLM work done:**

- Zip extracted to `/opt/proj_mp/lg_lab_final/` (single-level)
- Task 2 implemented at [`src_lg_lab_final/lg_lab_final_cfns.c`](/opt/proj_mp/lg_lab_final/src_lg_lab_final/lg_lab_final_cfns.c)
- Task 3 implemented at [`src_lg_lab_final/lg_lab_final_sfns.s`](/opt/proj_mp/lg_lab_final/src_lg_lab_final/lg_lab_final_sfns.s)
- Asm assembles cleanly with `arm-none-eabi-as -mcpu=cortex-m4 -mthumb`
- Task 2 host-compiled and both test cases pass (`-2`, `-6`)
- Task 3 hand-simulated against both test strings — null is copied, tests pass
- Code artifacts saved to [c1.c](./c1.c) and [c2.s](./c2.s)

**Human work remaining:**

1. **Edit `Task1_str1`** in [`lg_lab_final_app.c`](/opt/proj_mp/lg_lab_final/src_lg_lab_final/lg_lab_final_app.c) — replace "Firstname Lastname" with your real name
2. CubeIDE → **File → Open Projects from File System** → `/opt/proj_mp/lg_lab_final/lg_lab_final_g431n32/STM32CubeIDE` (ignore `Soln4unity` missing resource warning)
3. Build **Debug** config → set breakpoint on `ldr r1, [r0]` in `_sfns.s` → **Debug As** → capture **A1** (Registers r0)
4. Step through asm → return to C → pause at line 17 → capture **A2** (Variables A = `0x78563412`)
5. Step to line 19 → Expressions `pStr` (hex) → note value; step to line 21 → note new value → capture **A3**
6. Memory view at `0x20000000` ASCII → find Task1_str1 → capture **A4**
7. Terminate debug → Unity build → Run As → serial 2/2 PASS → capture **A5**
8. Clean All → tell LLM "lab_final done" → LLM makes submission zip

---

## Notes and Observations

### Issues Encountered

- **No manual PDF provided.** Task descriptions came from in-source comments. This is a departure from the lab08/lab09/proj05 pattern. If a PDF becomes available later, re-verify point values and any additional requirements.
- **No F412dsc / Renode variant.** G431n32 real hardware only — all tests and the Task 1 debugger walkthrough must run on the physical board.
- `Soln4unity` config references a missing `src_soln/` folder — same pattern as `UnitySoln` in prior labs; ignore the warning.
- `Task1_str1` contains literal placeholder text "Firstname Lastname" — the bottom-of-file comment explicitly requires the student to substitute their real name before running Task 1.

### Questions for TA/Instructor

- Point breakdown for Task 2 and Task 3 (not stated in code comments; only Task 1's 4×4 pts = 16 is explicit).
- Exact submission filename convention (PDF and zip).
- Whether screenshots must include a specific window chrome / title bar proving it's the student's machine.
