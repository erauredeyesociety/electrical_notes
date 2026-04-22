# Lab Final Procedure: Debug + Asm + C Programming Tasks

**Course:** CEC 322 / LG
**Project code:** lg_lab_final
**Target:** G431n32 Nucleo-32 only (no F412dsc, no Renode)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Base zip: `lg_lab_final.zip`
> - [known_issues.md](../known_issues.md)

> **Note:** No separate manual PDF was provided. All task descriptions are embedded as comments in the source files (`lg_lab_final_app.c` bottom, `lg_lab_final_cfns.c`, `lg_lab_final_sfns.s`).

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract ZIP to `/opt/proj_mp/lg_lab_final/` (done) |
| 2 | LLM | Task 2: fill in `task2_func_c` in `lg_lab_final_cfns.c` (done) |
| 3 | LLM | Task 3: fill in `task3_func_s` in `lg_lab_final_sfns.s` (done) |
| 4 | **HUMAN** | Edit `lg_lab_final_app.c` — replace "Firstname Lastname" in `Task1_str1` with your real name |
| 5 | HUMAN | CubeIDE: Import `lg_lab_final_g431n32` project |
| 6 | HUMAN | Build **Debug** (Application) config → debugger walkthrough for Task 1 |
| → | **ARTIFACT** | **A1:** Screenshot — Registers view at breakpoint on `ldr r1, [r0]` (record r0 in hex) |
| → | **ARTIFACT** | **A2:** Screenshot — Variables view at `_app.c` line 17 (record A in hex) |
| → | **ARTIFACT** | **A3:** Screenshot — Expressions view at line 19 AND line 21 (record both pStr values) |
| → | **ARTIFACT** | **A4:** Screenshot — Memory view at `0x20000000` ASCII rendering (record Task1_str1 starting address) |
| 7 | HUMAN | Build **Unity** config → Run As on real board |
| → | **ARTIFACT** | **A5:** Screenshot — 2/2 tests pass (`test_task2_func_c`, `test_task3_func_s`) |
| 8 | LLM | Code artifacts saved (done) |
| 9 | HUMAN | Clean builds in CubeIDE |
| 10 | LLM | Create submission ZIP |

---

## Point Breakdown (inferred from comments)

| Section | Points | Description |
|---------|--------|-------------|
| Task 1.1 | 4 | Breakpoint at `ldr r1, [r0]` — record r0 (hex) |
| Task 1.2 | 4 | Pause at `_app.c` line 17 — record A (hex) |
| Task 1.3 | 4 | Pause at line 19 then line 21 — record pStr at both (hex) |
| Task 1.4 | 4 | Pause at line 21 — Memory view ASCII at `0x20000000`, record Task1_str1 address |
| Task 2 | ? | `task2_func_c` — sum of negative array elements |
| Task 3 | ? | `task3_func_s` — asm strcpy (null-terminated copy) |

Task 1 comment block explicitly gives 4 pts per subtask. Tasks 2 and 3 point values not stated in code; assume balanced weighting (likely ~16 each or ~20+24 split).

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Extract base ZIP | CLAUDE CODE |
| Edit `task2_func_c` (C) | CLAUDE CODE |
| Edit `task3_func_s` (asm) | CLAUDE CODE |
| Edit `Task1_str1` with real name | **HUMAN** |
| CubeIDE: Import project | HUMAN |
| Debugger walkthrough for Task 1 (4 screenshots + 5 recorded hex values) | HUMAN |
| Build Unity, run on real board | HUMAN |
| Clean builds | HUMAN |
| Create submission ZIP | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks

### A.1 Extract Base Files

Done. Project lives at:

```
/opt/proj_mp/lg_lab_final/
├── lg_lab_final_g431n32/      # CubeMX project, G431n32 only
│   └── STM32CubeIDE/
│       ├── Debug/              # Application build output
│       ├── Application/        # App build config
│       ├── Unity/              # Unit test build config
│       └── Soln4unity/         # Instructor solution — ignore
├── lib/                        # Unity, UART redirect
├── src_lg_lab_final/
│   ├── _lg_lab_final_main.c
│   ├── lg_lab_final_app.c      # Task 1 already implemented; contains Task1_str1 (HUMAN edits real name here)
│   ├── lg_lab_final_cfns.c     # ← Task 2 filled in
│   ├── lg_lab_final_fns.h
│   └── lg_lab_final_sfns.s     # ← Task 1 (pre-filled) + Task 3 filled in
└── test_lg_lab_final/
    └── test_lg_lab_final.c     # 2 tests: task2 + task3
```

The CubeIDE `.project` uses `PARENT-N-PROJECT_LOC` linked resources, so **no CubeMX generate step is needed**.

> **Note on `Soln4unity`:** Linked resource points to a non-existent `src_soln/` folder. CubeIDE shows a warning about the missing resource — **ignore it**, use the `Unity` config.

### A.2 Task 2 — `task2_func_c` (C)

Sum negative elements:

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

Verified by host-compile:
- `arr = {1, -2, 3, -4}`, n=2 → sum of `{1, -2}` negatives = `-2` ✓
- n=4 → sum of `{-2, -4}` = `-6` ✓

### A.3 Task 3 — `task3_func_s` (asm)

Register map from comment: `*src -> r0; *dst -> r1; ch -> r2`.

```
task3_func_s:
task3_func_s_loop:
    ldrb    r2, [r0], #1           @ ch = *src++
    strb    r2, [r1], #1           @ *dst++ = ch
    cmp     r2, #0                 @ ch == '\0' ?
    bne     task3_func_s_loop      @ loop until null copied
    bx      lr
```

The null terminator IS copied (comparison happens after the store), matching the spec's "ending 0 has to be copied to the destination."

Verified asm assembles cleanly with `arm-none-eabi-as -mcpu=cortex-m4 -mthumb`. Hand-sim:
- "Hello" → 'H','e','l','l','o','\0' copied to dst (6 bytes). Test checks 6 bytes ✓
- "Hi" → 'H','i','\0' copied (3 bytes). Test checks 3 bytes ✓

### A.4 Code Artifacts Saved

- [c1.c](./c1.c) — `lg_lab_final_cfns.c` with Task 2 body
- [c2.s](./c2.s) — `lg_lab_final_sfns.s` with Task 3 body (Task 1 unchanged, pre-supplied)

---

## Part B: Human Tasks (GUI Required)

### B.0 EDIT YOUR REAL NAME in `Task1_str1` (REQUIRED)

Open [/opt/proj_mp/lg_lab_final/src_lg_lab_final/lg_lab_final_app.c](/opt/proj_mp/lg_lab_final/src_lg_lab_final/lg_lab_final_app.c):

```c
char Task1_str1[] = "Hello, this is Firstname Lastname.";
```

Change **Firstname Lastname** to your real first and last name. The comment at the bottom of that file explicitly requires this.

### B.1 CubeIDE Import

1. **File → Open Projects from File System…**
2. Directory: `/opt/proj_mp/lg_lab_final/lg_lab_final_g431n32/STM32CubeIDE`
3. **Finish**.

Ignore the `Soln4unity`/`src_soln` missing-resource warning.

### B.2 Build Application (Debug) and Run the Debugger — Task 1 Artifacts

1. Connect the G431 Nucleo-32 via USB.
2. Select **Debug** (or **Application**) build config → **Ctrl+B**.
3. Open [lg_lab_final_sfns.s](/opt/proj_mp/lg_lab_final/src_lg_lab_final/lg_lab_final_sfns.s) and find `task1_func_s`. The first instruction is `ldr r1, [r0]`.
4. **Double-click the left gutter** on that `ldr r1, [r0]` line → breakpoint.
5. Right-click project → **Debug As → STM32 C/C++ Application** → switch to Debug perspective.
6. Press **F8 (Resume)** to skip past the main-entry halt → should stop at your asm breakpoint.

#### Artifact A1 — r0 value (Task 1.1, 4 pts)

- **Window → Show View → Registers**.
- Read `r0` — it's the pointer to local variable `A`, so it'll be somewhere in the stack range, typically `0x2000FFE0`–`0x2001FFFC` depending on MCU RAM.
- **Record r0 value in hex.** Example format: `r0 = 0x2000FFF8`.
- Screenshot Registers view → `lab_final/a1.png`.

#### Artifact A2 — A value at _app.c line 17 (Task 1.2, 4 pts)

- Press **F5 (Step Into)** / **F6 (Step Over)** to step through `task1_func_s` byte-store sequence.
- After the four `strb` instructions, **F7 (Step Return)** to go back to C.
- Step over to land the green arrow at **`_app.c` line 17** (`printf("First executable line...");`).
- Open **Window → Show View → Variables**. `A` should be visible.
- Right-click `A` → **Number Format → Hex**.
- **Expected value:** `A = 0x78563412` (the byte-swapped little-endian of `0x12345678`).
- **Record A in hex.**
- Screenshot Variables view → `lab_final/a2.png`.

#### Artifact A3 — pStr at lines 19 and 21 (Task 1.3, 4 pts)

- Step over until arrow on **line 19** (`printf("String pointed by pStr: %s\n", pStr);`).
- Open **Window → Show View → Expressions** → Add expression `pStr` → Enter.
- Right-click `pStr` → **Number Format → Hex**. Record its value — this is the address of `Task1_str1`.
- Step over to **line 21** (the second `printf`). `pStr` should have updated to the address of `Task1_str2`.
- **Record both pStr values in hex.**
- Screenshot Expressions view after each pause → `lab_final/a3.png` (one screenshot with both visible, or a3a.png / a3b.png — combine in your PDF).

#### Artifact A4 — Memory view at 0x20000000 (Task 1.4, 4 pts)

- Still paused around line 21.
- **Window → Show View → Memory**.
- Click green **[+]** → enter `0x20000000` → OK.
- Right-click the new rendering tab → **Add Rendering... → Traditional** (or use the default) — we want ASCII.
- Click **New Renderings…** tab → select **ASCII** (or Text) → Add Rendering.
- Scroll the ASCII rendering until you see `Hello, this is <your name>.` — that's `Task1_str1`.
- **Record the starting address of Task1_str1 in hex** (the memory column left of the first `H`).
- Screenshot Memory view → `lab_final/a4.png`.

### B.3 Build Unity and Run on Real Board — Artifact A5

1. Terminate the debug session (red ■ button).
2. Hammer dropdown → **Unity** build config → Ctrl+B.
3. Open serial terminal: `tio /dev/ttyACM0 -b 115200`.
4. Right-click project → **Run As → STM32 C/C++ Application** (pick the Unity launch config if prompted).
5. Serial shows:

   ```
   Lab final Unit Test-----------------
   test_task2_func_c:PASS
   test_task3_func_s:PASS
   -----------------------
   2 Tests 0 Failures 0 Ignored
   OK
   ```

6. Screenshot serial → `lab_final/a5.png`.

### B.4 Clean and Submit

1. Right-click project → **Build Configurations → Clean All**.
2. LLM creates submission ZIP.

---

## Programming Task Details

### Task 1 (pre-supplied, asm) — big→little endian byte swap

Already implemented in [lg_lab_final_sfns.s](/opt/proj_mp/lg_lab_final/src_lg_lab_final/lg_lab_final_sfns.s). Loads the 32-bit word at `[r0]`, then stores each byte of the loaded value (low to high) into offsets 3, 2, 1, 0 of the same address — effectively reversing byte order in place.

No code to write. This task is a **debugger walkthrough** for 16 pts total.

### Task 2 (C) — `task2_func_c`: sum negatives

Straight linear scan, add element if `< 0`. Return `int32_t` sum.

### Task 3 (asm) — `task3_func_s`: null-terminated copy

Post-increment byte load / store loop. Terminates after copying the null byte (the `cmp r2, #0; bne` is the only branch, and it fires AFTER the store — so `'\0'` is always written to `dst` before the loop exits).

---

## Submission Checklist

- [ ] B.0: `Task1_str1` edited with your real name
- [ ] A1: Screenshot — Registers view at `ldr r1, [r0]` breakpoint; r0 in hex recorded
- [ ] A2: Screenshot — Variables view at `_app.c` line 17; A in hex recorded
- [ ] A3: Screenshot — Expressions view at line 19 AND line 21; both pStr values in hex recorded
- [ ] A4: Screenshot — Memory view ASCII at `0x20000000`; Task1_str1 address in hex recorded
- [ ] A5: Screenshot — 2/2 Unity tests pass on real G431
- [ ] C1: Task 2 C code (`lg_lab_final_cfns.c`)
- [ ] C2: Task 3 asm code (`lg_lab_final_sfns.s`)
- [ ] Report PDF with all screenshots + recorded values + code listings
- [ ] Project ZIP

**Zip command:**

```bash
cd /opt/proj_mp
zip -r lg-lab-final-lastname-firstname.zip lg_lab_final/ \
    -x 'lg_lab_final/*/STM32CubeIDE/Debug/*' \
    -x 'lg_lab_final/*/STM32CubeIDE/Application/*' \
    -x 'lg_lab_final/*/STM32CubeIDE/Unity/*' \
    -x 'lg_lab_final/*/STM32CubeIDE/Soln4unity/*'
```
