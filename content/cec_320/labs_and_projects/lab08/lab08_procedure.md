# Lab 08 Procedure: Bit Reversal in C and Assembly

**Course:** CEC 322 / MP-FI4B
**Points:** 100 total (90 programming + 10 submission)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-fi4b-lab8-bit-reversal-26-03.pdf`
> - [known_issues.md](../known_issues.md)

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract ZIP to `/opt/proj_mp/fi4b_bit_reversal/` (already done) |
| 2 | LLM | Fix PT1: two register bugs in `mp_bit_reverse_n_bit_naive_s` |
| 3 | LLM | Fix PT2: write full `mp_bit_reverse_16_bit_fast_s` |
| 4 | HUMAN | CubeIDE: Import both `_f412dsc` and `_g431n32` projects (File → Open Projects from File System) |
| 5 | HUMAN | Build F412dsc **Unity** config → run in Renode via `unity_fi4b_bit_reversal_f412dsc.resc` |
| → | **ARTIFACT** | **A1:** Screenshot — all 14 tests pass in Renode (F412dsc) |
| 6 | HUMAN | Build G431n32 **Unity** config → Run As on real Nucleo-32 (no Renode for G431) |
| → | **ARTIFACT** | **A2:** Screenshot — all 14 tests pass on G431n32 via Putty |
| 7 | HUMAN | (optional) Build F412dsc **Debug** (App) → run via `debug_fi4b_bit_reversal_f412dsc.resc` to see the App printout |
| 8 | LLM | Save `c1.s` code artifact, fill in report |
| 9 | HUMAN | Clean builds in CubeIDE |
| 10 | LLM | Create submission ZIP |

---

## Point Breakdown

| Section | Points | Description |
|---------|--------|-------------|
| 8.4.1 PT1: debug `mp_bit_reverse_n_bit_naive_s` | 30 | Fix bugs in provided asm |
| 8.4.2 PT2: write `mp_bit_reverse_16_bit_fast_s` | 60 | Extend 8-bit asm to 16-bit |
| 8.5 Submission | 10 | Report + ZIP |

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Extract base ZIP to `/opt/proj_mp/` | CLAUDE CODE |
| Edit `fi4b_bit_reversal_sfns.s` (PT1 + PT2) | CLAUDE CODE |
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

Already done. Project now lives at:

```
/opt/proj_mp/fi4b_bit_reversal/
├── fi4b_bit_reversal_f412dsc/         # full CubeMX project (F412dsc, Renode)
│   └── STM32CubeIDE/                  # pre-generated CubeIDE config
│       ├── Debug/                     # App build config
│       ├── Unity/                     # Unit test build config
│       └── UnitySoln/                 # Instructor soln config (may fail — ignore)
├── fi4b_bit_reversal_g431n32/         # full CubeMX project (G431, real HW)
│   └── STM32CubeIDE/
├── lib/                               # Unity, UART redirect, helpers
├── renode/                            # 3 Renode scripts (debug, unity, unitysoln)
├── src/
│   ├── _mp_main.c
│   ├── fi4b_bit_reversal_app.c
│   ├── fi4b_bit_reversal_cfns.c
│   ├── fi4b_bit_reversal_fns.h
│   └── fi4b_bit_reversal_sfns.s       # ← PT1 + PT2 live here
└── test/
    └── test_fi4b_bit_reversal.c       # 14 tests (6 for C fns, 8 for asm fns)
```

The CubeIDE `.project` files use `PARENT-N-PROJECT_LOC` linked resources, which
resolve correctly at `/opt/proj_mp/...`, so **no CubeMX generate step is needed**.
The `.mxproject` / `.ioc` and the `Src/main.c` etc. already exist in the zip.

### A.2 PT1 Fix — Two Register Bugs

In `src/fi4b_bit_reversal_sfns.s`, inside `mp_bit_reverse_n_bit_naive_s`:

**Bug 1:** `mask_j = 1 << j`, but the shift used `r4` (= i) instead of `r3` (= j).

```diff
-        lsl     r6, r2, r4    @ mask_j
+        lsl     r6, r2, r3    @ mask_j = 1 << j
```

**Bug 2:** `b_i = (x >> i) & 1U`, but the shift used `r3` (= j) instead of `r4` (= i).

```diff
-        lsr     r7, r0, r3    @ x >> i
+        lsr     r7, r0, r4    @ x >> i
```

Walk-through for `x = 0b10, n = 2`: with bugs, both masks = 1, both source bits
read from bit j=1 → result `x = 0b11` (wrong). With the fixes: `mask_i=1, mask_j=2`,
`b_i=0, b_j=1`, `x` becomes `0b01` ✓.

### A.3 PT2 Fix — Write `mp_bit_reverse_16_bit_fast_s`

Extends the given `mp_bit_reverse_8_bit_fast_s` pattern to 16 bits: four swap
stages (distance 1, 2, 4, 8) with masks `0x5555, 0x3333, 0x0f0f`. For the
distance-8 stage the low half of `x` is already zero after the earlier masking,
so we only need `z = x >> 8; x = z | (x << 8)`, matching the C reference in
§8.3.5 of the manual. A final `and r0, 0xFFFF` clamps to 16 bits.

Both fixes have been applied to [`/opt/proj_mp/fi4b_bit_reversal/src/fi4b_bit_reversal_sfns.s`](/opt/proj_mp/fi4b_bit_reversal/src/fi4b_bit_reversal_sfns.s).

### A.4 Save Code Artifact

After tests pass, the edited `fi4b_bit_reversal_sfns.s` is copied to
`lab08/c1.s` for the report.

---

## Part B: Human Tasks (GUI Required)

### B.1 CubeIDE: Import Both Projects

1. Open CubeIDE.
2. **File → Open Projects from File System…**
3. Directory: `/opt/proj_mp/fi4b_bit_reversal/fi4b_bit_reversal_f412dsc/STM32CubeIDE`
4. Make sure `fi4b_bit_reversal_f412dsc` is checked → **Finish**.
5. Repeat for `/opt/proj_mp/fi4b_bit_reversal/fi4b_bit_reversal_g431n32/STM32CubeIDE`

No need to create `lib_src` folders, no need to link files, no need to add
include paths — everything is already defined in the pre-packaged
`.project` / `.cproject`.

> **Note on `UnitySoln`:** A linked resource points to
> `PARENT-3-PROJECT_LOC/fi4b_bit_reversal_soln/src_soln/fi4b_bit_reversal_sfns_soln.s`,
> which doesn't exist on your system. CubeIDE will show a warning about the
> missing linked resource in the `UnitySoln` config — **ignore it**, it only
> affects the instructor's solution build config. Use the `Unity` config.

### B.2 Build and Run Unity on F412dsc (Renode) — Artifact A1

1. In CubeIDE, select the **`fi4b_bit_reversal_f412dsc`** project.
2. Select build config: **`Unity`** (hammer dropdown → `Unity`).
3. **Ctrl+B** to build.
4. Open terminal:
   ```bash
   cd /opt/proj_mp/fi4b_bit_reversal/renode/
   renode
   ```
5. In the Renode Monitor:
   ```
   s @unity_fi4b_bit_reversal_f412dsc.resc
   ```
6. The USART2 analyzer window should show:
   ```
   fi4b unit test-----------------
   ...
   14 Tests 0 Failures 0 Ignored
   OK
   ```
7. **Capture screenshot → `a1.png`**

### B.3 Build and Run Unity on G431n32 (Real Board) — Artifact A2

No Renode script exists for G431, so unit tests must run on the real Nucleo-32.

1. Connect the G431 Nucleo-32 board via USB.
2. Open a serial terminal (Putty / minicom / `tio /dev/ttyACM0 -b 115200`).
3. In CubeIDE, select **`fi4b_bit_reversal_g431n32`** project → build config **`Unity`**.
4. **Ctrl+B**.
5. Right-click project → **Run As → STM32 C/C++ Application** (use the existing
   `fi4b_bit_reversal_g431n32 Unity.launch`).
6. Serial terminal shows `14 Tests 0 Failures 0 Ignored OK`.
7. **Capture screenshot → `a2.png`**

### B.4 (Optional) Run the App in Renode — Debug config on F412dsc

Only if you want to visually verify the app prints binary strings:

```
cd /opt/proj_mp/fi4b_bit_reversal/renode/
renode
(monitor) s @debug_fi4b_bit_reversal_f412dsc.resc
```

You should see the `0x5D` input printed with its 8-bit and 16-bit reversals.

### B.5 Clean and Submit

1. In CubeIDE: right-click each project → **Build Configurations → Clean All**.
2. LLM creates submission ZIP (see A.4 / below).

---

## Programming Task Details

### PT1: Debug `mp_bit_reverse_n_bit_naive_s` (30 pts)

**Location:** `src/fi4b_bit_reversal_sfns.s`, function `mp_bit_reverse_n_bit_naive_s`.

**Register map (from comment header):**
- `r0` = x (in/out), `r1` = n, `r2` = 1u, `r3` = j, `r4` = i
- `r5` = mask_i, `r6` = mask_j, `r7` = b_i, `r8` = b_j

**Bugs:**
1. `lsl r6, r2, r4` → should use `r3` (j) not `r4` (i). `mask_j = 1 << j`.
2. `lsr r7, r0, r3` → should use `r4` (i) not `r3` (j). `b_i = (x >> i) & 1U`.

Both are "wrong register for an intended variable" bugs from the manual's list.

### PT2: Write `mp_bit_reverse_16_bit_fast_s` (60 pts)

**Location:** Same file, empty stub at `mp_bit_reverse_16_bit_fast_s`.

**Approach:** Copy the 8-bit fast structure and:
- Replace `0x55 / 0x33` with `0x5555 / 0x3333`.
- Add a third swap stage with mask `0x0f0f` and shift 4.
- Replace the `>> 4 / << 4` final stage with `>> 8 / << 8` (since we now operate on 16 bits).
- Final mask changes from `0xFF` to `0xFFFF`.

---

## Submission Checklist

- [ ] A1: Screenshot — 14/14 tests pass in Renode on F412dsc
- [ ] A2: Screenshot — 14/14 tests pass on real G431n32 board
- [ ] C1: Code snippet — edited `fi4b_bit_reversal_sfns.s`
- [ ] Report PDF: `fi4b-report-lastname-firstname.pdf`
- [ ] Project ZIP: `fi4b-proj-lastname-firstname.zip`

**Zip command:**

```bash
cd /opt/proj_mp/
zip -r fi4b-proj-lastname-firstname.zip fi4b_bit_reversal/ \
    -x 'fi4b_bit_reversal/*/STM32CubeIDE/Debug/*' \
    -x 'fi4b_bit_reversal/*/STM32CubeIDE/Unity/*' \
    -x 'fi4b_bit_reversal/*/STM32CubeIDE/UnitySoln/*'
```
(Exclude build output directories so the zip isn't bloated — Clean All from
CubeIDE first will also remove them.)
