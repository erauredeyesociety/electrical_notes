# HW 12 - References and Expanded Lecture Notes

This document provides expanded explanations of the key concepts used in HW 12, with direct references to the course lecture slides.

---

## 1. C Loop Constructs and Their ASM Equivalents (Lctr 26)

**Source:** `mp-hg-lctr26-impl-c-loops-in-asm-26-04.pdf`

### 1.1 The Three C Loops

Lctr 26 Sec 26.1 introduces the three C loops:

- **`for` loop.** Executes a code block a specified number of times. Number of executions can be 0.
- **`while` loop.** Tests condition at the top — if the condition fails at entry, the body runs 0 times.
- **`do-while` loop.** Tests condition at the bottom — the body always runs at least once.

For HW 12 Prob 2, the given C function uses the `while` loop. For HW 12 Prob 1, we use `while (1) { ... break; }` because:

- We do not know the number of trios in advance → `for` is inappropriate.
- We may not make any swap at all (e.g., input `"he"`) → `do-while` is inappropriate.
- The compound test inside the loop has *three* independent zero checks, which is cleaner as a `while (1)` with `break` than as a natural `while (cond)` (Lctr 27 Sec 27.2 makes this same argument explicitly for Exercise 1).

### 1.2 The Three Equivalent ASM Shapes for a `for` or `while` Loop

Lctr 26 Sec 26.2.4 gives three standard ASM shapes. The **common CMP** shape (Example 2) tests at the top; the **late-check** shape (Example 3) tests at the bottom but jumps around on first entry; the **CEX** shape (Example 4) puts the body inside an IT block.

For HW 12 Prob 2, the `while`-loop shape used in the solutions is equivalent to the standard `while`-loop listing from Lctr 26 Example 10 (`mp_str_cpy_while_s`):

```asm
mp_str_cpy_while_s:
    ldrb    r2, [r1], #1           @ priming read
mp_str_cpy_while_s_lp:
    cbz     r2, mp_str_cpy_while_s_end
        ldrb    r2, [r1], #1
        strb    r2, [r0], #1
    b       mp_str_cpy_while_s_lp
mp_str_cpy_while_s_end:
    bx      lr
```

The HW 12 Prob 2 Part 1 solution follows this exact structure, inserting an additional `SUB r2, r2, #0x20` for the upper-case conversion and adding the post-loop `STRB` for the null terminator.

### 1.3 The `while (1) { ... break; }` Idiom

Lctr 27 Sec 27.2 explains the `while (1)` construct as a way to eliminate the priming-read repetition inherent to the plain `while` loop. The associated ASM listing (Example 1b, `mp_swap_pairs_in_str_break_s`) is:

```asm
mp_swap_pairs_in_str_break_s:
    ldr     r3, =0
mp_swap_pairs_in_str_break_s_lp:
    ldrb    r1, [r0], #1
    cbz     r1, mp_swap_pairs_in_str_break_s_end
    ldrb    r2, [r0], #1
    cbz     r2, mp_swap_pairs_in_str_break_s_end
        strb    r1, [r0, #-1]
        strb    r2, [r0, #-2]
        add     r3, #1
    b       mp_swap_pairs_in_str_break_s_lp
mp_swap_pairs_in_str_break_s_end:
    mov     r0, r3
    bx      lr
```

HW 12 Prob 1 Part 2 follows this pattern, extended to check **three** characters per pass. HW 12 Prob 2 Part 3 follows the same pattern with a single-character test plus a post-`_end` store of the null byte.

**Used in HW 12:**

- **Prob 1:** `while (1) { ... break; ... }` in C; ASM uses `CBZ ..., _end` three times in series.
- **Prob 2 Part 1:** plain `while (ch)` — priming read + in-loop read.
- **Prob 2 Parts 2 & 3:** `while (1) { ... break; }` refactor to eliminate the priming-read repetition.

---

## 2. Complex Flow Control: `break`, `continue`, and `switch` (Lctr 27)

**Source:** `mp-hi-lctr27-complex-flow-control-in-c-n-asm-26-04.pdf`

### 2.1 The `break` Keyword

Lctr 27 Sec 27.2 states that `break` "changes the flow in the loop by jumping out of it" and notes that it must be wrapped in an `if` (or another construct that can conditionally execute it). In ASM, a `break` target is simply the loop-exit label, and the conditional `if`-plus-`break` becomes a conditional branch (`CBZ`, `CBNZ`, `BEQ`, etc.) to that label.

**Used in HW 12:**

- **Prob 1 Part 1:** three separate `if (cX == 0) { break; }` checks, one per char of the trio.
- **Prob 1 Part 2:** three `CBZ r?, ..._end` branches, directly implementing the three `break`s.
- **Prob 2 Part 2:** one `if (ch == 0) { *dst++ = ch; break; }` — the terminator store *before* the `break` is faithfully preserved in the ASM by placing an `STRB` at the `_end` label.
- **Prob 2 Part 3:** one `CBZ r2, ..._end` followed by an `STRB r2, [r0], #1` at `_end` (to write the `\0`).

### 2.2 The `continue` Keyword

Lctr 27 Sec 27.3 covers `continue`. It is not used in HW 12 (no "skip-rest-of-iteration" semantics appear in either problem), but students should be aware:

- In a `for` loop, `continue` jumps to the `update` expression.
- In a `while`/`do-while` loop, `continue` jumps to the condition test — so any loop-control update must appear **before** the `continue`, not after.

### 2.3 The `switch` Construct

Lctr 27 Sec 27.4 covers the naïve (`CMP`/`BEQ` chain) and TBB-based implementations of `switch`. HW 12 does not use `switch`, so this material is not exercised here — but understanding it is important for Exam 3.

---

## 3. Byte Load/Store and Pointer Post-Increment (Lctr 20)

**Source:** `mp-gc-lctr20-imd-offset-ldr-n-str-n-macro-slides-26-03.pdf`

### 3.1 `LDRB` and `STRB` for `char` Access

Both HW 12 problems work exclusively on `char` (byte) data. The relevant instructions:

- **`LDRB Rd, [Rn], #1`** — post-indexed unsigned-byte load. Loads `*Rn`, then `Rn += 1`. Zero-extends to 32 bits.
- **`STRB Rd, [Rn], #1`** — post-indexed byte store. Writes the low 8 bits of `Rd` to `*Rn`, then `Rn += 1`.
- **`STRB Rd, [Rn, #os]`** — base-plus-offset byte store, **no writeback**. Writes to `*(Rn + os)`, leaves `Rn` unchanged.

### 3.2 Mapping C Pointer Idioms to ASM Addressing Modes

| C Expression            | ASM (byte)                   | Notes                        |
|-------------------------|------------------------------|------------------------------|
| `x = *p++`              | `ldrb r0, [r1], #1`          | post-indexed, writeback      |
| `*p++ = x`              | `strb r0, [r1], #1`          | post-indexed, writeback      |
| `x = *++p`              | `ldrb r0, [r1, #1]!`         | pre-indexed, writeback       |
| `*++p = x`              | `strb r0, [r1, #1]!`         | pre-indexed, writeback       |
| `*(p - 1) = x` (no upd) | `strb r0, [r1, #-1]`         | base + neg offset, no writeback |
| `*(p - 2) = x` (no upd) | `strb r0, [r1, #-2]`         | base + neg offset, no writeback |

**Used in HW 12:**

- **Prob 1:** `c_i = *str++` → `ldrb r_i, [r0], #1` (three times). Then, after all three post-increments, `*(str - 2) = c3` → `strb r3, [r0, #-2]`, and `*(str - 1) = c2` → `strb r2, [r0, #-1]` — offsets of −2 and −1 from the post-increment position land exactly on the 2nd and 3rd chars of the just-read trio.
- **Prob 2 (both ASM parts):** `ch = *src++` → `ldrb r2, [r1], #1`; `*dst++ = ch` → `strb r2, [r0], #1`.

### 3.3 Why Offset −2 and −1 (not −3 and −2) in Prob 1

After the three `LDRB ..., [r0], #1` loads for one trio, `r0` has advanced by **three** bytes. The three chars of the trio are now at addresses `r0 - 3`, `r0 - 2`, `r0 - 1`. The C code swaps the **last two** chars of each trio — i.e., the chars at `r0 - 2` and `r0 - 1`. So the correct stores are:

- `strb r3, [r0, #-2]` — put the 3rd char into the 2nd slot.
- `strb r2, [r0, #-1]` — put the 2nd char into the 3rd slot.

A common mistake is to write `#-3` and `#-2` (as if the whole trio were being swapped); this would corrupt the first char of the trio and miss the last one.

---

## 4. `CBZ`/`CBNZ` — Compare-and-Branch-on-Zero (Lctr 25)

**Sources:** `mp-he-lctr25-if-based-flow-control-in-asm-slides-26-04.pdf`, `mp-hc-lctr24-combo-branch-n-cond-execution-slides-26-04.pdf`

### 4.1 When to Use `CBZ`/`CBNZ`

`CBZ Rn, label` and `CBNZ Rn, label` test whether `Rn` is zero (unsigned) and branch accordingly. Unlike `CMP`/`Bcc`, they do **not** set or use any flag — so they can safely be used anywhere that does not disturb a pending flag-dependent test.

**Key restrictions:**

- The branch distance is short (typically up to +126 bytes forward) — cannot branch backward.
- `CBZ`/`CBNZ` **cannot appear inside an IT block** (Lctr 24, Sec 24.3.2).
- Only `Rn` in `{r0..r7}` is encodable.

### 4.2 Why `CBZ` Is Ideal for Null-Terminator Checks

When scanning a C string, the natural exit condition is "the byte just loaded is zero." `CBZ Rn, end_label` replaces the two-instruction sequence `cmp Rn, #0; beq end_label`. In both HW 12 problems, a loaded byte is tested against zero immediately, and neither problem has any in-flight flag-dependent test — so `CBZ` is the cleanest choice.

**Used in HW 12:**

- **Prob 1:** three `CBZ r?, ..._end` to test each char of the trio for null.
- **Prob 2 Parts 1, 3:** one `CBZ r2, ..._end` to test the loaded byte for null.

---

## 5. AAPCS Scratch Registers (Lctr 23)

**Source:** `mp-gs-lctr23-aapcs-slides-26-04.pdf` (series position)

From the AAPCS summary used throughout the course:

| Register | Role                                           |
|----------|------------------------------------------------|
| R0       | 1st argument / return value                    |
| R1       | 2nd argument                                   |
| R2       | 3rd argument                                   |
| R3       | 4th argument                                   |
| R12 (IP) | Scratch — callee may freely clobber            |
| R4–R11   | Callee-saved — must be preserved if used       |
| R14 (LR) | Return address                                 |

### 5.1 Consequences for HW 12

- **Prob 1** uses `r0` (arg & return), `r1`, `r2`, `r3` (all scratch for up to four-arg functions), and `r12` for the `pair_swapped` accumulator. None of these require push/pop. The function is leaf (no inner calls), so `lr` also does not need saving.
- **Prob 2** uses `r0`, `r1`, `r2` only — all scratch, all arg-passing. No push/pop needed.

A common mistake on previous homework was pushing/popping `r4` for a local when one of the scratch registers (e.g., `r12`) would have sufficed. This adds four bytes of stack traffic per call for no benefit.

---

## 6. Summary: Mapping Each HW Problem to Lecture Material

| Problem  | Key Concepts                                                    | Primary Lecture Reference                                      |
|----------|-----------------------------------------------------------------|----------------------------------------------------------------|
| 1.1 (C)  | `while (1) { ... break; }` idiom; three-step compound test      | Lctr 27, Sec 27.2 (Example 1a, reproduced pattern)              |
| 1.2 (ASM)| Post-indexed `LDRB`, `CBZ` for zero-byte test, `STRB` with negative offset (no writeback), scratch-register accumulator | Lctr 20, Sec 20.2; Lctr 25; Lctr 27, Example 1b                 |
| 2.1 (ASM)| Priming read, top-tested `while` loop translation, `CBZ` exit, post-loop null-terminator store | Lctr 26, Sec 26.3 (Example 10, left column); Lctr 20, Sec 20.2 |
| 2.2 (C)  | Refactor from `while (cond)` to `while (1) { ... break; }` to eliminate code repetition | Lctr 27, Sec 27.2                                              |
| 2.3 (ASM)| `while (1)` + `break` translation; `CBZ` to `_end`; terminator store placed at `_end` | Lctr 27, Example 1b                                            |

---

## 7. Common Mistakes to Avoid

1. **Wrong offsets on the trio swap (Prob 1).** After three post-incrementing `LDRB`s, the trio's chars live at `[r0, #-3]`, `[r0, #-2]`, `[r0, #-1]`. The last-two swap uses **−2** and **−1**, not −3 and −2. Using the wrong offsets corrupts the first char of the trio (which should be left alone).

2. **Using `LDRB` writeback on the last read when the char is the terminator.** In Prob 1 the early-exit path does still advance `r0`, but we never write through the new `r0`, so this is harmless. The subtle danger is if you try to "undo" the writeback by subtracting — don't. Just branch to `_end`.

3. **Putting the terminator store inside the loop in Prob 2 Part 3.** The refactored C writes `*dst++ = ch` **inside** the `if (ch == 0)` branch before `break`ing. Translating literally, that store must still happen. The cleanest placement is the first instruction at `_end` — not inside the loop body.

4. **Using `CMP`/`BEQ` when `CBZ` suffices.** On a freshly-loaded byte with no in-flight flag-dependent work, `CBZ` is one instruction and leaves flags untouched. Use it.

5. **Pushing `r4`/`r5` for short-lived scratch.** `r12` is caller-clobbered scratch under AAPCS and is perfect for a loop accumulator that outlives only the loop itself. No prologue/epilogue cost.

6. **Forgetting that `while (ch)` runs zero times on an empty input.** The given Prob 2 C code reads a priming `*src++` first — if `src` points to `'\0'`, the loop body never runs, and the post-loop `*dst++ = ch` still writes the `\0` terminator to `dst`. The ASM must produce the same observable: one byte (zero) written to `dst`. Both Prob 2 Parts 1 and 3 do so correctly.

7. **Trying to put `CBZ`/`CBNZ` inside an IT block.** Lctr 24 explicitly forbids this. For HW 12 there is no need for an IT block anyway — the conditional branches are free-standing.
