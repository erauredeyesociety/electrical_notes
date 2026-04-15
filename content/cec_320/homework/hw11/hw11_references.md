# HW 11 - References and Expanded Lecture Notes

This document provides expanded explanations of the key concepts used in HW 11, with direct references to the course lecture slides.

---

## 1. ARM Status Flags and Condition Code Suffixes (Lctr 18-19)

**Sources:** `mp-fm-lctr18-arm-status-flags-slides-26-03.pdf`, `mp-fo-lctr19-ccs-n-cond-branch-slides-26-03.pdf`

### 1.1 The Four Status Flags (NZCV)

ARM updates four flags in the APSR after a flag-setting instruction (like `CMP`, `CMN`, or any `S`-suffixed instruction):

| Flag | Name | Meaning |
|------|------|---------|
| N | Negative | Bit 31 of the result (1 if result is negative in signed interpretation) |
| Z | Zero | Set if result is zero |
| C | Carry | Unsigned overflow / borrow out |
| V | Overflow | Signed overflow |

`CMP Rn, Op2` sets flags as if computing `Rn - Op2` (result discarded).

### 1.2 Condition Code Suffixes (CCS) — Signed vs. Unsigned

Because `x > y` compares signed integers, we must use signed CCSs. Unsigned comparisons use a different set.

| Relational test | Signed CCS | Unsigned CCS |
|-----------------|------------|--------------|
| `==` | `EQ` | `EQ` |
| `!=` | `NE` | `NE` |
| `>`  | `GT` | `HI` |
| `>=` | `GE` | `HS` (or `CS`) |
| `<=` | `LE` | `LS` |
| `<`  | `LT` | `LO` (or `CC`) |

**Used in HW 11:**
- **Prob 1** (`x_cmp_y_load`): `x` and `y` are `int32_t` — use signed CCSs (`GT`, `LE`).
- **Prob 2** (`mathf`): `x` is `int` — signed (`LT`, `GE`).
- **Prob 3** (`load_based_on_x`): `x` is `int` — signed (`LE`, `GE`, `GT`, `LT`).

---

## 2. Combination Branching and Conditional Execution (Lctr 24)

**Source:** `mp-hc-lctr24-combo-branch-n-cond-execution-slides-26-04.pdf`

### 2.1 Conditional Execution Syntax

Most Thumb-2 data-processing and load/store instructions can be attached a CCS to become conditional (Lctr 24, Sec 24.3.1):

```
INST{S}{cond} Rd, Rn, Op2
```

If the condition fails, the instruction:
- does not execute,
- does not write its destination,
- does not affect any flags,
- does not generate an exception.

**Examples used in HW 11:**
- `ldrshgt r0, [r2, #2]!` — pre-indexed signed-halfword load, only when `GT`.
- `ldrle r0, [r3], #4` — post-indexed word load, only when `LE`.
- `asrle r0, r0, #1` — arithmetic shift right, only when `LE`.
- `lslgt r0, r0, #1` — logical shift left, only when `GT`.

### 2.2 The IT (If-Then) Instruction

Under the GNU assembler, conditional execution must be organized under an `IT` block (Lctr 24, Sec 24.3.2):

```
IT{x{y{z}}} cond
```

- `I` = If, `T` = Then (required, first conditional instruction).
- `x`, `y`, `z` are optional second/third/fourth slots, each being `T` (matches `cond`) or `E` (matches inverse of `cond`).
- The first `T`'s CCS must equal `cond`; any `E`'s CCS must be the inverse of `cond`.

Common forms used in HW 11:

| Form | Slots | Meaning |
|------|-------|---------|
| `IT cond`    | 1 | One conditional instruction |
| `ITT cond`   | 2 | Two instructions, both match `cond` |
| `ITE cond`   | 2 | First matches `cond`, second is inverse |
| `ITTT cond`  | 3 | Three instructions, all match `cond` |
| `ITTE cond`  | 3 | T, T, E |
| `ITTEE cond` | 4 | T, T, E, E |

**Rules (Lctr 24, p. 9):**
- A conditional branch can be at the end of an IT block, but not in the middle.
- `CBZ`/`CBNZ` cannot appear inside an IT block.

**Used in HW 11:**
- **Prob 1 Part 3:** `ITTEE le` — two `le` (else-branch) instructions followed by two `gt` (then-branch) instructions.
- **Prob 2 Part 3:** `ITTT lt` covers the load + branch for the first range, then `ITE ge` covers the `x >= 5` override and the default `2x`.
- **Prob 3 Part 2:** `ITTEE ge` packs the four instructions for the second sub-test of the compound `OR` condition.

### 2.3 Comparing to a Negative Immediate

`CMP Rn, #-imm` is not a directly encodable Thumb-2 immediate form, but the GNU assembler translates it to `CMN Rn, #imm`, which sets flags based on `Rn + imm` (equivalent to `Rn - (-imm)`). For `x < -5`, we can write `CMP r0, #-5` — the assembler will emit `CMN r0, #5`. Signed CCSs (`LT`, `GE`, ...) behave correctly afterward.

**Used in HW 11:**
- **Prob 2:** `cmp r0, #-5` tests the lower bound of the piecewise function.

---

## 3. If-Based Flow Control in ASM (Lctr 25)

**Source:** `mp-he-lctr25-if-based-flow-control-in-asm-slides-26-04.pdf`

### 3.1 Positive vs. Negative Logic for `if-else`

Positive logic (PL): branch to the `then` label when the C test is true; the `else` block is physically laid out first.

```asm
    cmp     r0, r1
    bgt     my_then            @ PL: same condition as C
my_else:
    @ ... else-block ...
    b       my_end
my_then:
    @ ... then-block ...
my_end:
    bx      lr
```

Negative logic (NL): branch to the `else` label when the C test is false; the `then` block is laid out first.

```asm
    cmp     r0, r1
    ble     my_else            @ NL: opposite of C test
my_then:
    @ ... then-block ...
    b       my_end
my_else:
    @ ... else-block ...
my_end:
    bx      lr
```

Both produce the same result. Negative logic is the more common style because the fall-through case (the `then` block) matches how we read the C code.

**Used in HW 11:**
- **Prob 1 Part 1:** PL using `BGT` (same as C's `>`).
- **Prob 1 Part 2:** NL using `BLE` (opposite of C's `>`).
- **Prob 3 Part 1:** NL-style CMP approach for a compound `OR` condition.

### 3.2 CEX Implementation of `if-else`

From Lctr 25 (Example 2, p. 5), the CEX version of a simple if-else uses `ITE cond`:

```asm
@ C: if (x >= 0) x <<= 1; else x >>= 4;
mp_a_mllu_cex:
    cmp     r0, #0
    ite     ge             @ T = ge, E = lt
    lslge   r0, #1         @ then: x <<= 1
    asrlt   r0, #4         @ else: x >>= 4
    bx      lr
```

When each branch needs more than one instruction, extend the IT block (e.g., `ITTEE`).

**Used in HW 11:**
- **Prob 1 Part 3:** Each branch is load + shift (two instructions), so `ITTEE le` is needed.
- **Prob 3 Part 2:** Same — two instructions per branch means `ITTEE ge`.

### 3.3 The `if-else-if-else` Construct

From Lctr 25 (Example 4, p. 8), the CMP approach chains two conditional branches, and the CEX approach chains two IT blocks (optionally terminating the first with a conditional `B` so subsequent tests fall through correctly).

The CEX pattern uses `ITT cond` with a conditional branch as the second slot to short-circuit the chain:

```asm
mp_a_crlu_cex:
    cmp     r0, #0
    itt     lt
    ldrlt   r1, =0
    blt     end                 @ conditional B ends the IT block
    cmp     r0, #8
    ite     lt
    movlt   r1, r0              @ middle range: y = x
    ldrge   r1, =8              @ upper range: y = 8
end:
    mov     r0, r1
    bx      lr
```

**Used in HW 11:**
- **Prob 2 Part 3:** Exactly this pattern — first `ITT lt` handles `x < -5` with a conditional branch to end, then `ITE ge` handles `x >= 5` vs the `2x` default.

### 3.4 Compound Tests with `||`

From Lctr 25 (Example 6, p. 10), an `OR` compound is most naturally written with two separate `CMP`s and a short-circuit branch:

```asm
@ C: if (x < 0 || x >= 8) { x = 0; } else { x = 1; }
mp_d_crlu_or_cmp:
    cmp     r0, #0
    blt     then_block         @ first condition true → take then
    cmp     r0, #8
    blt     else_block         @ second condition false → take else
then_block:
    ldr     r0, =0
    b       end
else_block:
    ldr     r0, =1
end:
    bx      lr
```

De Morgan's law can convert `OR` to `AND` (Lctr 25, Example 7), but the short-circuit branch form is clearer for HW 11 Prob 3.

**Used in HW 11:**
- **Prob 3 Part 1:** CMP approach uses the two-test short-circuit pattern directly.
- **Prob 3 Part 2:** CEX version keeps the first `BGT` as a normal branch (since `CBZ`/conditional branches in the middle of an IT block are restricted to the end position) and uses `ITTEE` for the second test.

---

## 4. Shift Instructions for Multiply/Divide by Powers of 2 (Lctr 16)

**Source:** `mp-fg-lctr16-shift-instructions-n-op2-slides-26-03.pdf`

| C Operation | ASM Instruction | Notes |
|-------------|-----------------|-------|
| `x * 2`     | `LSL r0, r0, #1` | Logical shift left by 1 |
| `x * 4`     | `LSL r0, r0, #2` | Logical shift left by 2 |
| `x / 2` (unsigned) | `LSR r0, r0, #1` | Logical shift right |
| `x / 4` (unsigned) | `LSR r0, r0, #2` | Logical shift right |
| `x / 2` (signed)   | `ASR r0, r0, #1` | Arithmetic shift right (preserves sign) |
| `x / 4` (signed)   | `ASR r0, r0, #2` | Arithmetic shift right |

The `S` in `LSR`/`ASR` stands for "shift right" — use `LSR` for unsigned types and `ASR` for signed types so sign bits are correctly extended.

**Used in HW 11:**
- **Prob 1:** `*(ptrB++) / 2` is a signed divide (`ptrB` is `int32_t *`), so `ASR r0, r0, #1`. `*(++ptrA) * 2` uses `LSL r0, r0, #1`.
- **Prob 2:** `2*x` is `LSL r0, r0, #1`.
- **Prob 3:** `*++ptrA * 4` uses `LSL r0, r0, #2`. `*++ptrB / 4` is an unsigned divide (`ptrB` is `uint32_t *`), so `LSR r0, r0, #2`.

---

## 5. Load Instructions for Pointer Dereference (Lctr 20)

**Source:** `mp-gc-lctr20-imd-offset-ldr-n-str-n-macro-slides-26-03.pdf`

The three addressing forms for `LDR`/`STR` map directly onto C pointer operations (review from HW 10):

| Form | Syntax | C Equivalent |
|------|--------|--------------|
| Basic | `LDR{type} Rv, [Ra, #os]` | `var = *(ptr + k)` |
| Pre-indexed | `LDR{type} Rv, [Ra, #os]!` | `var = *++ptr` |
| Post-indexed | `LDR{type} Rv, [Ra], #os` | `var = *ptr++` |

For a `uint16_t *` pointer, `++ptr` advances the address by `sizeof(uint16_t) = 2` bytes, so the offset in the `LDRH` must be `#2`. For a `uint32_t *`, the offset is `#4`.

**Used in HW 11:**
- **Prob 1** (`int16_t *ptrA`): `*(++ptrA)` → `ldrsh r0, [r2, #2]!` (pre-indexed, signed halfword, step = 2).
- **Prob 1** (`int32_t *ptrB`): `*(ptrB++)` → `ldr r0, [r3], #4` (post-indexed, word, step = 4).
- **Prob 3** (`uint16_t *ptrA`): `*++ptrA` → `ldrh r0, [r1, #2]!` (pre-indexed, unsigned halfword, step = 2).
- **Prob 3** (`uint32_t *ptrB`): `*++ptrB` → `ldr r0, [r2, #4]!` (pre-indexed, word, step = 4).

### 5.1 Pre-Indexing Matches C Prefix Operators

Prefix `++` on a pointer followed by dereference (`*++ptr`) advances the pointer *before* loading — the exact semantics of a pre-indexed `LDR` with writeback. This is why HW 11's `*++ptrA` and `*(++ptrA)` both use the `[Ra, #os]!` form.

### 5.2 Post-Indexing Matches C Postfix Operators

Postfix `++` on a pointer inside a dereference (`*(ptr++)`) dereferences the *old* pointer first, then advances — the exact semantics of a post-indexed `LDR`. This is why `*(ptrB++)` in Prob 1 uses `ldr r0, [r3], #4`.

---

## 6. ARM Calling Convention (AAPCS) — Quick Reference

From Lctr 23, pp. 2, 7:

| Register | Usage |
|----------|-------|
| R0 | 1st argument / return value |
| R1 | 2nd argument |
| R2 | 3rd argument |
| R3 | 4th argument |
| R4-R11 | Callee-saved |
| R14 (LR) | Return address |

**For HW 11 function calls:**
- `x_cmp_y_load(x, y, ptrA, ptrB)`: `r0 = x`, `r1 = y`, `r2 = ptrA`, `r3 = ptrB`. Return value in `r0`.
- `mathf_*(x)`: `r0 = x`. Return value in `r0`.
- `load_based_on_x_*(x, ptrA, ptrB)`: `r0 = x`, `r1 = ptrA`, `r2 = ptrB`. Return value in `r0`.

---

## 7. Summary: Mapping Each HW Problem to Lecture Material

| Problem | Key Concepts | Primary Lecture Reference |
|---------|--------------|--------------------------|
| 1.1 (PL) | Positive-logic `if-else` with signed `BGT`/`LE`, pre/post-indexed LDR | Lctr 25, Sec 25.3; Lctr 20, Sec 20.2 |
| 1.2 (NL) | Negative-logic `if-else` with signed `BLE` | Lctr 25, Sec 25.3 |
| 1.3 (CEX) | `ITTEE` for two-instruction branches, conditional LDR/ASR/LSL | Lctr 24, Sec 24.3.2; Lctr 25, Sec 25.3 |
| 2.1 (C)  | `if-else-if-else` construct | Lctr 25, Sec 25.4 |
| 2.2 (CMP) | Chained `CMP`/conditional-branch, negative immediate via `CMN` | Lctr 25, Sec 25.4 |
| 2.3 (CEX) | `ITT` with conditional `B`, chained `ITE` blocks | Lctr 25, Example 4 (Sec 25.4) |
| 3.1 (CMP) | Compound `OR` via short-circuit double `CMP` | Lctr 25, Sec 25.5 |
| 3.2 (CEX) | `ITTEE` for two-instruction then/else branches inside a compound test | Lctr 24, Sec 24.3.2; Lctr 25, Sec 25.5 |
