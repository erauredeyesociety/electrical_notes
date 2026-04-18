# Proj 05 Procedure: Load and Store (General)

**Course:** CEC 322 / MP-GE4A
**Points:** 100 total (15 PT1 + 30 PT2 + 45 PT3 + 10 submission)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-ge4a-proj5-load-n-store-general-26-03.pdf`
> - [known_issues.md](../known_issues.md)

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract ZIP to `/opt/proj_mp/ge4a_load_n_store/` (done) |
| 2 | LLM | PT1: implement `mp_load_modify_store_s` in `ge4a_load_n_store_sfns.s` |
| 3 | LLM | PT2a: implement `mp_str_cpy_s` in same file |
| 4 | LLM | PT2b: implement `mp_str_len_s` in same file |
| 5 | LLM | PT3a: implement `mp_array_abs_sum_s` in same file |
| 6 | LLM | PT3b: implement `mp_array_max_s` in same file |
| 7 | HUMAN | CubeIDE: Import both `_f412dsc` and `_g431n32` projects (File → Open Projects from File System) |
| 8 | HUMAN | Build F412dsc **Unity** config → run in Renode via `unity_ge4a_load_n_store_f412dsc.resc` |
| → | **ARTIFACT** | **A1:** Screenshot — all 9 tests pass in Renode (F412dsc) |
| 9 | HUMAN | Build G431n32 **Unity** config → Run As on real Nucleo-32 (no Renode for G431) |
| → | **ARTIFACT** | **A2:** Screenshot — all 9 tests pass on G431n32 via serial terminal |
| 10 | LLM | `c1.s` code artifact saved (done) |
| 11 | HUMAN | Clean builds in CubeIDE |
| 12 | LLM | Create submission ZIP |

---

## Point Breakdown

| Section | Points | Description |
|---------|--------|-------------|
| 5.3.1 PT1: `mp_load_modify_store_s` | 15 | Load + shift + store for int32/int16/int8 pointer params |
| 5.3.2 PT2a: `mp_str_cpy_s` | 18 | ASM translation of `mp_str_cpy_c2` (post-indexed ldrb/strb) |
| 5.3.2 PT2b: `mp_str_len_s` | 12 | ASM string length — student-designed algorithm |
| 5.3.3 PT3a: `mp_array_abs_sum_s` | 30 | ASM translation of the **abs**-sum loop (see Divergence note below) |
| 5.3.3 PT3b: `mp_array_max_s` | 15 | ASM array-maximum — student-designed algorithm |
| 5.4 Submission | 10 | Report + ZIP |

> **Manual vs. base-code divergence (IMPORTANT).** The PDF text in §5.3.3
> describes a "ReLU norm" (sum of **positive** elements) and declares
> `mp_array_relu_sum` / `mp_array_relu_sum_s`. The shipped
> `ge4a_load_n_store.zip` instead ships `mp_array_abs_sum`,
> `mp_array_abs_sum_s`, and `test_mp_array_abs_sum*` — the C reference in
> `ge4a_load_n_store_cfns.c` is the **absolute-value sum** (negates negatives
> *then* always accumulates). All deliverables for this project are written
> to match the shipped code (since those are the symbols the tests import and
> the header declares). This discrepancy is noted in the findings doc as a
> question for the instructor; it does not affect submission.

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Extract base ZIP to `/opt/proj_mp/` | CLAUDE CODE |
| Edit `ge4a_load_n_store_sfns.s` (all 5 PT functions) | CLAUDE CODE |
| CubeIDE: Import both projects | HUMAN |
| CubeIDE: Build Unity configs | HUMAN |
| Run Renode (F412dsc) and real board (G431n32) | HUMAN |
| Capture screenshots | HUMAN |
| Save code artifact, update docs | CLAUDE CODE |
| Clean builds | HUMAN |
| Create submission ZIP | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks

### A.1 Extract Base Files

Project now lives at:

```
/opt/proj_mp/ge4a_load_n_store/
├── ge4a_load_n_store_f412dsc/         # full CubeMX project (F412dsc, Renode)
│   └── STM32CubeIDE/
│       ├── Debug/                     # App build config
│       ├── Unity/                     # Unit test build config
│       └── UnitySoln/                 # Instructor soln config — IGNORE (references soln/ that doesn't exist on your system)
├── ge4a_load_n_store_g431n32/         # full CubeMX project (G431, real HW)
│   └── STM32CubeIDE/
│       ├── ge4a_load_n_store_g431n32.launch
│       ├── ge4a_load_n_store_g431n32 Unity.launch
│       └── ge4a_load_n_store_g431n32 UnitySoln.launch
├── lib/                               # Unity, UART redirect, helpers
├── renode/                            # app_..., unity_..., unitysoln_... (3 scripts, F412dsc only)
├── src_ge4a_load_n_store/             # note NON-STANDARD folder name
│   ├── _ge4a_load_n_store_main.c
│   ├── ge4a_load_n_store_app.c
│   ├── ge4a_load_n_store_cfns.c
│   ├── ge4a_load_n_store_fns.h
│   └── ge4a_load_n_store_sfns.s       # ← all 5 PTs live here
└── test_ge4a_load_n_store/            # note NON-STANDARD folder name
    └── test_ge4a_load_n_store.c       # 9 tests total (4 C-function + 5 asm-function)
```

The CubeIDE `.project` files link sources via `PARENT-2-PROJECT_LOC/src_ge4a_load_n_store/...`
and `PARENT-2-PROJECT_LOC/test_ge4a_load_n_store/...` (i.e., the `src_` and
`test_` folders keep their unusual names on purpose — do not rename them).
Because `.project` / `.cproject` are packaged, **no CubeMX "Generate Code"
step is needed** — just **File → Open Projects from File System** in CubeIDE.

### A.2 PT1 — `mp_load_modify_store_s`

**C reference** (from `ge4a_load_n_store_cfns.c`):

```c
void mp_load_modify_store(int32_t *Ai32, int16_t *Bi16, int8_t *Ci8) {
    *Ai32 = 3 * *Ai32 / 4;
    *Bi16 = 2 * *Bi16 / 4;
    *Ci8  = 1 * *Ci8  / 4;
}
```

Per §5.3.1, each modify **must use one instruction that involves a shift**.
The implementation therefore:

| Element | Modify algebra | One-instruction form |
|---------|----------------|----------------------|
| `*Ai32` (int32) | `(3·x)/4 = x − x/4` | `sub r3, r3, r3, asr #2` |
| `*Bi16` (int16) | `(2·x)/4 = x/2`     | `asr r3, r3, #1` |
| `*Ci8`  (int8)  | `(1·x)/4 = x/4`     | `asr r3, r3, #2` |

- `ldrsh` / `ldrsb` sign-extend the loaded halfword/byte into the full 32-bit
  working register; arithmetic `asr` then does the right thing for negative
  values.
- `strh` / `strb` write back only the low 16 / 8 bits. The Unity test relies
  on this — the `int[]` array `inp` is aliased as an int16/int8 through
  `(int16_t *)&inp[1]` / `(int8_t *)&inp[2]`, and the neighboring bytes
  happen to already be `0xFF` so the final full-word reads back as the
  negative value expected.

### A.3 PT2a — `mp_str_cpy_s`

Direct translation of `mp_str_cpy_c2` using post-indexed byte load/store:

```
cpy_loop:
    ldrb    r2, [r0], #1        @ r2 = *src++
    cbz     r2, cpy_end         @ break on NUL
    strb    r2, [r1], #1        @ *dst++ = ch
    b       cpy_loop
cpy_end:
    mov     r2, #0
    strb    r2, [r1]            @ *dst = 0
    bx      lr
```

The C loop `while ((ch = *src++))` maps cleanly onto the post-indexed
`ldrb r2, [r0], #1` (load then increment the pointer), then a zero-test
(`cbz`) to break out. `cbz` is the standard ARMv7-M idiom and saves one
compare-and-branch.

### A.4 PT2b — `mp_str_len_s`

No C reference is given (§5.3.2 says "figure out from the test"). The chosen
algorithm: walk a shadow pointer from `str` until we see NUL, then return
(end − start).

```
mp_str_len_s:
    mov     r1, r0              @ r1 = str  (walking pointer)
len_loop:
    ldrb    r2, [r1], #1        @ r2 = *r1++;   post-inc lands ONE PAST the NUL when it exits
    cbz     r2, len_end
    b       len_loop
len_end:
    sub     r0, r1, r0          @ length_incl_nul = r1 − str
    sub     r0, r0, #1          @ subtract 1 to drop the trailing NUL
    bx      lr
```

Test expectations: `len("hi") == 2`, `len("hello") == 5`. Both match.

### A.5 PT3a — `mp_array_abs_sum_s`

**Note the divergence from the PDF:** the shipped C reference (and the test)
are for *abs* sum, not ReLU. All deliverables follow the shipped code.

```
mp_array_abs_sum_s:
    mov     r2, #0                @ sum = 0
    cmp     r1, #0
    ble     abs_end               @ n <= 0 → return 0
    mov     r12, r1               @ counter = n
abs_loop:
    ldr     r3, [r0], #4          @ temp = *pArr++
    cmp     r3, #0
    it      lt
    neglt   r3, r3                @ if (temp < 0) temp = -temp
    add     r2, r2, r3            @ sum += temp
    subs    r12, r12, #1
    bne     abs_loop
abs_end:
    mov     r0, r2
    bx      lr
```

- **Post-indexed word load** `ldr r3, [r0], #4` auto-increments the array
  pointer, removing the need for a separate index register.
- **`it lt` + `neglt`**: conditional negate — a clean ARM idiom for abs.
- `r12` is a scratch caller-saved register, so no push/pop is needed.

Verified in Python against the test vectors:
`abs_sum([-5,-3,-1,0,1,3,5], 3) = 9`, `abs_sum(..., 7) = 18`, matching
`exp[] = {9, 18}`.

### A.6 PT3b — `mp_array_max_s`

Running-max pattern. Seed `max` with `pArr[0]` (n ≥ 1 in the test), loop
over the remaining elements, conditionally update when a larger value is
seen:

```
mp_array_max_s:
    ldr     r2, [r0], #4          @ max = *pArr++
    subs    r12, r1, #1           @ remaining = n − 1
    beq     max_end
max_loop:
    ldr     r3, [r0], #4
    cmp     r3, r2
    it      gt
    movgt   r2, r3                @ if (temp > max) max = temp
    subs    r12, r12, #1
    bne     max_loop
max_end:
    mov     r0, r2
    bx      lr
```

Verified: `max([-3,-5,-1,7], 3) = -1`, `max(..., 4) = 7`, matching
`exp[] = {-1, 7}`.

### A.7 Save Code Artifact

After tests pass, the edited `ge4a_load_n_store_sfns.s` is copied to
[`proj05/c1.s`](./c1.s) for the report.

---

## Part B: Human Tasks (GUI Required)

### B.1 CubeIDE: Import Both Projects

1. Open CubeIDE.
2. **File → Open Projects from File System…**
3. Directory: `/opt/proj_mp/ge4a_load_n_store/ge4a_load_n_store_f412dsc/STM32CubeIDE`
4. Confirm `ge4a_load_n_store_f412dsc` is checked → **Finish**.
5. Repeat for `/opt/proj_mp/ge4a_load_n_store/ge4a_load_n_store_g431n32/STM32CubeIDE`.

> **Note on `UnitySoln`:** A linked resource points to
> `PARENT-3-PROJECT_LOC/ge4a_load_n_store_base_n_soln/soln/ge4a_load_n_store_sfns.s`,
> which doesn't exist on your system. CubeIDE will show a warning about the
> missing linked resource in the `UnitySoln` config — **ignore it**, it only
> affects the instructor's solution build config. Use the `Unity` config.

No need to create `lib_src` folders, no need to link files manually, no need
to add include paths — everything is already defined in the pre-packaged
`.project` / `.cproject`.

### B.2 Build and Run Unity on F412dsc (Renode) — Artifact A1

1. In CubeIDE, select the **`ge4a_load_n_store_f412dsc`** project.
2. Select build config: **`Unity`** (hammer dropdown → `Unity`).
3. **Ctrl+B** to build. Watch for zero errors.
4. Open a terminal:

   ```bash
   cd /opt/proj_mp/ge4a_load_n_store/renode
   renode
   ```

5. In the Renode Monitor:

   ```text
   s @unity_ge4a_load_n_store_f412dsc.resc
   ```

6. The USART2 analyzer window should show:

   ```text
   Running ge4a unit test-----------------
   test/test_ge4a_load_n_store.c:8:test_mp_load_modify_store:PASS
   test/test_ge4a_load_n_store.c:17:test_mp_str_cpy_c1:PASS
   test/test_ge4a_load_n_store.c:29:test_mp_str_cpy_c2:PASS
   test/test_ge4a_load_n_store.c:41:test_mp_array_abs_sum:PASS
   test/test_ge4a_load_n_store.c:53:test_mp_load_modify_store_s:PASS
   test/test_ge4a_load_n_store.c:62:test_mp_str_cpy_s:PASS
   test/test_ge4a_load_n_store.c:74:test_mp_str_len_s:PASS
   test/test_ge4a_load_n_store.c:86:test_mp_array_abs_sum_s:PASS
   test/test_ge4a_load_n_store.c:98:test_mp_array_max_s:PASS
   -----------------------
   9 Tests 0 Failures 0 Ignored
   OK
   ```

7. **Capture screenshot → `a1.png`**

### B.3 Build and Run Unity on G431n32 (Real Board) — Artifact A2

No Renode script exists for G431, so unit tests must run on the real
Nucleo-32.

1. Connect the G431 Nucleo-32 board via USB.
2. Open a serial terminal (`tio /dev/ttyACM0 -b 115200` or Putty / minicom).
3. In CubeIDE, select **`ge4a_load_n_store_g431n32`** project → build config **`Unity`**.
4. **Ctrl+B**.
5. Right-click project → **Run As → STM32 C/C++ Application** (uses the
   packaged `ge4a_load_n_store_g431n32 Unity.launch`).
6. Serial terminal should show `9 Tests 0 Failures 0 Ignored / OK`.
7. **Capture screenshot → `a2.png`**

### B.4 (Optional) Run the App in Renode — Debug config on F412dsc

The shipped app is an empty stub ("This is now an empty app."). Running it
is optional:

```bash
cd /opt/proj_mp/ge4a_load_n_store/renode
renode
# monitor:  s @app_ge4a_load_n_store_f412dsc.resc
```

### B.5 Clean and Submit

1. In CubeIDE: right-click each project → **Build Configurations → Clean All**.
2. LLM creates submission ZIP (see checklist below).

---

## Programming Task Details

### PT1: `mp_load_modify_store_s` (15 pts)

See [Part A.2](#a2-pt1--mp_load_modify_store_s) above.

### PT2a: `mp_str_cpy_s` (18 pts)

See [Part A.3](#a3-pt2a--mp_str_cpy_s) above.

### PT2b: `mp_str_len_s` (12 pts)

See [Part A.4](#a4-pt2b--mp_str_len_s) above.

### PT3a: `mp_array_abs_sum_s` (30 pts)

See [Part A.5](#a5-pt3a--mp_array_abs_sum_s) above.

### PT3b: `mp_array_max_s` (15 pts)

See [Part A.6](#a6-pt3b--mp_array_max_s) above.

---

## Submission Checklist

- [ ] A1: Screenshot — 9/9 tests pass in Renode on F412dsc
- [ ] A2: Screenshot — 9/9 tests pass on real G431n32 board
- [ ] C1: Code snippet — edited `ge4a_load_n_store_sfns.s`
- [ ] Report PDF: `cec320-proj5-report-lastname-firstname.pdf`
- [ ] Project ZIP: `cec320-proj5-proj-lastname-firstname.zip`

**Zip command (excludes build output dirs):**

```bash
cd /opt/proj_mp/
zip -r cec320-proj5-proj-lastname-firstname.zip ge4a_load_n_store/ \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/Debug/*' \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/Release/*' \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/Unity/*' \
    -x 'ge4a_load_n_store/*/STM32CubeIDE/UnitySoln/*'
```

(`Clean All` from CubeIDE will also remove these; the `-x` flags just make
the zip idempotent whether or not Clean was run.)
