# Lab 09 Procedure: Condition Code Suffices and Conditional Branch

**Course:** CEC 322 / MP-FO4B
**Points:** 100 total (10 CET + 30 PT1 + 15 PT2 + 35 PT3 + 10 submission)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-fo4b-lab9-ccs-n-cond-branch-26-04.pdf`
> - [known_issues.md](../known_issues.md)

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract ZIP to `/opt/proj_mp/fo4b_ccs_n_cond_branch/` (already done) |
| 2 | LLM | PT1: fill in `mp_apsr_to_ccs` in `fo4b_ccs_n_cond_branch_cfns.c` |
| 3 | LLM | PT2: fill in `mp_max_ab_i_s` in `fo4b_ccs_n_cond_branch_sfns.s` |
| 4 | LLM | PT3: fill in `mp_range_square_sum_standard_while_s` in the same asm file |
| 5 | HUMAN | CubeIDE: Import both `_f412dsc` and `_g431n32` projects |
| 6 | HUMAN | Build F412dsc **Unity** → run in Renode via `unity_fo4b_ccs_n_cond_branch_f412dsc.resc` |
| → | **ARTIFACT** | **A1:** Screenshot — all 5 tests pass (F412dsc Renode) |
| 7 | HUMAN | Build G431n32 **Unity** → Run As on real Nucleo-32 |
| → | **ARTIFACT** | **A2:** Screenshot — all 5 tests pass on real board |
| 8 | HUMAN | Write the CET explanation in the report (10 pts, writing-only) |
| 9 | LLM | Save `c1.c` and `c2.s` code artifacts |
| 10 | HUMAN | Clean builds in CubeIDE |
| 11 | LLM | Create submission ZIP |

---

## Point Breakdown

| Section | Points | Description |
|---------|--------|-------------|
| 9.3.1 CET | 10 | Explain the type-cast trick in `mp_val_apsr_to_apsr` and the `val_apsr1` shift |
| 9.3.2 PT1: `mp_apsr_to_ccs` | 30 | 10 CCS values from APSR flags |
| 9.3.3 PT2: `mp_max_ab_i_s` | 15 | Signed max of two ints (asm) |
| 9.3.4 PT3: `mp_range_square_sum_standard_while_s` | 35 | int64 sum of squares loop (asm) |
| 9.4 Submission | 10 | Report + ZIP |

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Extract base ZIP to `/opt/proj_mp/` | CLAUDE CODE |
| Edit `fo4b_ccs_n_cond_branch_cfns.c` (PT1) | CLAUDE CODE |
| Edit `fo4b_ccs_n_cond_branch_sfns.s` (PT2 + PT3) | CLAUDE CODE |
| CubeIDE: Import both projects | HUMAN |
| CubeIDE: Build Unity configs | HUMAN |
| Run Renode (F412dsc) and real board (G431n32) | HUMAN |
| Capture screenshots | HUMAN |
| Write CET explanation paragraph in the report | HUMAN |
| Save code artifacts, update docs | CLAUDE CODE |
| Clean builds | HUMAN |
| Create submission ZIP | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks

### A.1 Extract Base Files

Already done. Project now lives at:

```
/opt/proj_mp/fo4b_ccs_n_cond_branch/
├── fo4b_ccs_n_cond_branch_f412dsc/    # full CubeMX project (F412dsc, Renode)
│   └── STM32CubeIDE/                  # pre-generated CubeIDE config
│       ├── Debug/                     # App build config
│       ├── Unity/                     # Unit test build config
│       └── UnitySoln/                 # Instructor soln config — ignore
├── fo4b_ccs_n_cond_branch_g431n32/    # full CubeMX project (G431, real HW)
├── lib/                               # Unity, UART redirect, helpers
├── renode/                            # 3 Renode scripts (debug, unity, unitysoln)
├── src/
│   ├── _mp_main.c
│   ├── fo4b_ccs_n_cond_branch_app.c
│   ├── fo4b_ccs_n_cond_branch_cfns.c  # ← PT1 lives here
│   ├── fo4b_ccs_n_cond_branch_fns.h
│   └── fo4b_ccs_n_cond_branch_sfns.s  # ← PT2 + PT3 live here
└── test/
    └── test_fo4b_ccs_n_cond_branch.c  # 5 tests total
```

Linked resources use `PARENT-N-PROJECT_LOC`, so no CubeMX "Generate Code"
step is needed — just **File → Open Projects from File System** in CubeIDE.

### A.2 PT1 — `mp_apsr_to_ccs` (C)

Replaces the empty weak stub in `fo4b_ccs_n_cond_branch_cfns.c`. 10
one-liners derived directly from the ARM condition-code definitions:

| CCS | Expression | CCS | Expression |
|-----|------------|-----|------------|
| EQ  | `Z`        | LO  | `!C`       |
| NE  | `!Z`       | LS  | `!C \|\| Z` |
| LT  | `N != V`   | HS  | `C`        |
| LE  | `Z \|\| (N != V)` | HI  | `C && !Z`  |
| GE  | `N == V`   |     |            |
| GT  | `!Z && (N == V)` |     |            |

Verified against the manual's two test cases by hand simulation:
- **case1** (N=5, x=-3, y=13): APSR = `{N=1, Z=0, C=1, V=0}` → `[0,1,1,1,0,0,0,0,1,1]` ✓
- **case2** (N=5, x=y=17 → both −15): APSR = `{N=0, Z=1, C=1, V=0}` → `[1,0,0,1,1,0,0,1,1,0]` ✓

### A.3 PT2 — `mp_max_ab_i_s` (asm)

```
mp_max_ab_i_s:
    cmp     r0, r1                  @ compare a and b (signed)
    bge     mp_max_ab_i_s_end_if    @ if a >= b, keep r0 (= a)
    mov     r0, r1                  @ else return b
mp_max_ab_i_s_end_if:
    bx      lr
```

Uses **signed** `BGE` so the test case `a = 0xFFFFFFFF (=-1), b = 0` correctly
picks `b = 0` (the expected value).

### A.4 PT3 — `mp_range_square_sum_standard_while_s` (asm)

Register map (from function header comment):
- `r0` = i (in) / return low word
- `r1` = e / return high word
- `r2` = sum_low_word, `r3` = sum_high_word
- `r4, r5` = scratch for 64-bit square (callee-saved, so push/pop)

```
mp_range_square_sum_standard_while_s:
    push    {r4, r5, lr}
    mov     r2, #0                  @ sum_low  = 0
    mov     r3, #0                  @ sum_high = 0
loop_sq_s:
    cmp     r0, r1                  @ compare i, e (signed)
    bgt     end_sq_s                @ if i > e, exit loop
    smull   r4, r5, r0, r0          @ r5:r4 = (int64_t)i * i
    adds    r2, r2, r4              @ sum_low  += r4 (sets carry)
    adc     r3, r3, r5              @ sum_high += r5 + carry
    add     r0, r0, #1              @ i++
    b       loop_sq_s
end_sq_s:
    mov     r0, r2                  @ return low word in r0
    mov     r1, r3                  @ return high word in r1
    pop     {r4, r5, pc}
```

Key points:

- **`smull`** for 32×32 → signed 64-bit. Needed because `i` can be negative
  (test case `s = −3`) and/or large (test case `0x100000^2 = 0x1_0000_0000_00`
  which overflows 32 bits).
- **`adds` + `adc`** correctly propagates the carry from the 32-bit low-word
  addition into the high word.
- **Signed** `BGT` on `cmp r0, r1` so negative `i` still loops until `i > e`.

All 4 test cases verified in Python simulation:
`(3,0)→0`, `(−3,0)→14`, `(0,3)→14`, `(0x100000,0x100000)→0x10000000000` ✓

### A.5 Save Code Artifacts

After tests pass:

- `lab09/c1.c` — snippet of `mp_apsr_to_ccs` (plus for reference the existing `mp_val_apsr_to_apsr`)
- `lab09/c2.s` — full edited `fo4b_ccs_n_cond_branch_sfns.s`

---

## Part B: Human Tasks (GUI Required)

### B.1 CubeIDE: Import Both Projects

1. Open CubeIDE.
2. **File → Open Projects from File System…**
3. Directory: `/opt/proj_mp/fo4b_ccs_n_cond_branch/fo4b_ccs_n_cond_branch_f412dsc/STM32CubeIDE`
4. Click **Finish**.
5. Repeat for `/opt/proj_mp/fo4b_ccs_n_cond_branch/fo4b_ccs_n_cond_branch_g431n32/STM32CubeIDE`

> **Note on `UnitySoln`:** A linked resource points to
> `PARENT-3-PROJECT_LOC/fo4b_ccs_n_cond_branch_soln/src_soln/...`, which
> doesn't exist. CubeIDE will show a warning — **ignore it**, use the
> `Unity` config.

### B.2 Build and Run Unity on F412dsc (Renode) — Artifact A1

1. Select **`fo4b_ccs_n_cond_branch_f412dsc`** project → build config **`Unity`**.
2. **Ctrl+B**.
3. Open terminal:

   ```bash
   cd /opt/proj_mp/fo4b_ccs_n_cond_branch/renode
   renode
   ```

4. In Renode Monitor:

   ```text
   s @unity_fo4b_ccs_n_cond_branch_f412dsc.resc
   ```

5. USART2 analyzer should show:

   ```text
   Running fo4b unit test-----------------
   ...
   5 Tests 0 Failures 0 Ignored
   OK
   ```

6. **Capture screenshot → `a1.png`**

### B.3 Build and Run Unity on G431n32 (Real Board) — Artifact A2

No Renode script exists for G431, so unit tests run on the real Nucleo-32.

1. Connect the G431 Nucleo-32 board via USB.
2. Open a serial terminal (`tio /dev/ttyACM0 -b 115200` or Putty).
3. In CubeIDE, select **`fo4b_ccs_n_cond_branch_g431n32`** → build config **`Unity`**.
4. **Ctrl+B**.
5. Right-click project → **Run As → STM32 C/C++ Application** (use the
   existing `fo4b_ccs_n_cond_branch_g431n32 Unity.launch`).
6. Serial terminal shows `5 Tests 0 Failures 0 Ignored OK`.
7. **Capture screenshot → `a2.png`**

### B.4 Write the CET Explanation (Human — Report Only)

The CET is a **writing task**, not a coding task. In the report, answer:

1. **How does `mp_val_apsr_to_apsr` copy the upper 32 bits of the `uint64_t`
   into the bit-field `APSR_t`?**
   Sketch of the answer: `&val_apsr` is a pointer to a 64-bit value. Cast to
   `(APSR_t *)` so pointer arithmetic steps in units of `sizeof(APSR_t) = 4`
   bytes. Adding `+ 1` advances to the second 32-bit slot, which on a
   little-endian machine is the upper word of `val_apsr`. Dereferencing
   reads those 4 bytes as an `APSR_t`, which is a direct bit-reinterpret
   into the bit-field — no arithmetic conversion is performed, so the flag
   bits line up with the bit-field positions defined in `fo4b_ccs_n_cond_branch_fns.h`.

2. **Why does `((uint64_t)15) << (32+28)` correspond to `exp[1] = 0xF0000000`?**
   Sketch of the answer: the APSR flags live in bits 28..31 of the upper
   32-bit word (V=28, C=29, Z=30, N=31). Shifting `15 = 0b1111` left by
   `32 + 28` places those four `1` bits starting at bit 60 of the 64-bit
   value, i.e. at bits 28..31 of the upper word. Reading the upper word as
   a `uint32_t` gives `0xF0000000`, which matches what `act[1]` reads back
   after the cast-and-offset trick.

### B.5 Clean and Submit

1. In CubeIDE: right-click each project → **Build Configurations → Clean All**.
2. LLM creates submission ZIP (see findings doc).

---

## Programming Task Details

### PT1: `mp_apsr_to_ccs` (30 pts) — C in `fo4b_ccs_n_cond_branch_cfns.c`

See [Part A.2](#a2-pt1--mp_apsr_to_ccs-c) above.

### PT2: `mp_max_ab_i_s` (15 pts) — asm in `fo4b_ccs_n_cond_branch_sfns.s`

See [Part A.3](#a3-pt2--mp_max_ab_i_s-asm) above.

### PT3: `mp_range_square_sum_standard_while_s` (35 pts) — asm

See [Part A.4](#a4-pt3--mp_range_square_sum_standard_while_s-asm) above.

---

## Submission Checklist

- [ ] CET: written explanation in the report (10 pts)
- [ ] A1: Screenshot — 5/5 tests pass in Renode on F412dsc
- [ ] A2: Screenshot — 5/5 tests pass on real G431n32 board
- [ ] C1: `mp_apsr_to_ccs` C code
- [ ] C2: Edited `fo4b_ccs_n_cond_branch_sfns.s` (PT2 + PT3)
- [ ] Report PDF: `fo4b-report-lastname-firstname.pdf`
- [ ] Project ZIP: `fo4b-proj-lastname-firstname.zip`

**Zip command:**

```bash
cd /opt/proj_mp/
zip -r fo4b-proj-lastname-firstname.zip fo4b_ccs_n_cond_branch/ \
    -x 'fo4b_ccs_n_cond_branch/*/STM32CubeIDE/Debug/*' \
    -x 'fo4b_ccs_n_cond_branch/*/STM32CubeIDE/Unity/*' \
    -x 'fo4b_ccs_n_cond_branch/*/STM32CubeIDE/UnitySoln/*'
```
