# CEC 320 Homework 8 Solutions — Status Flags, CCS, and Branch

**(PDF labeled "HW 9")**
**Total Points: 132**

---

## Problem 1 (42 pts): 5-bit Signed/Unsigned Operations

**System:** $N = 5$ bits, $C_N = 2^5 = 32$

- Unsigned range: $[0, 31]$
- Signed range: $[-16, 15]$

### Part (a): $(-15) + (-5)$ (21 pts)

**Step 1 — Represent operands in 5-bit binary:**

| Decimal | 5-bit Unsigned Equivalent | 5-bit Binary |
|---|---|---|
| $-15$ | $-15 + 32 = 17$ | `10001` |
| $-5$ | $-5 + 32 = 27$ | `11011` |

**Step 2 — Unsigned interpretation ($u_{temp}$):**

$$u_{temp} = 17 + 27 = 44$$

$44 > 31$ (exceeds unsigned max) → **Carry** ($C = 1$)

Corrected unsigned result: $44 - 32 = \mathbf{12}$

**Step 3 — Signed interpretation ($s_{temp}$):**

$$s_{temp} = (-15) + (-5) = -20$$

$-20 < -16$ (below signed min) → **Overflow** ($V = 1$)

Corrected signed result: $-20 + 32 = \mathbf{12}$

**Step 4 — Binary result:**

$$12 = \mathbf{0b\,01100}$$

**Step 5 — NZCV flags:**

| Flag | Value | Reasoning |
|---|---|---|
| **N** | 0 | MSB (bit 4) of `01100` is 0 |
| **Z** | 0 | Result $\neq 0$ |
| **C** | 1 | Unsigned carry occurred ($44 \geq 32$) |
| **V** | 1 | Signed overflow occurred ($-20 < -16$) |

### Part (b): $11 - 18$ (21 pts)

**Step 1 — Represent operands in 5-bit binary:**

| Decimal | 5-bit Binary |
|---|---|
| $11$ | `01011` |
| $18$ | `10010` (note: as signed 5-bit, this is $18 - 32 = -14$) |

**Step 2 — Unsigned interpretation ($u_{temp}$):**

$$u_{temp} = 11 - 18 = -7$$

$-7 < 0$ (below unsigned min) → **Borrow** → $C = 0$ (ARM: $C = 1 - \text{Borrow}$)

Corrected unsigned result: $-7 + 32 = \mathbf{25}$

**Step 3 — Signed interpretation ($s_{temp}$):**

The operands in signed 5-bit are 11 and $-14$ (since `10010` in signed = $-14$).

$$s_{temp} = 11 - (-14) = 25$$

$25 > 15$ (exceeds signed max) → **Overflow** ($V = 1$)

Corrected signed result: $25 - 32 = \mathbf{-7}$

**Step 4 — Binary result:**

$$25 = \mathbf{0b\,11001}$$

(Verify: as signed, `11001` $= -32 + 25 = -7$ ✓)

**Step 5 — NZCV flags:**

| Flag | Value | Reasoning |
|---|---|---|
| **N** | 1 | MSB (bit 4) of `11001` is 1 |
| **Z** | 0 | Result $\neq 0$ |
| **C** | 0 | Unsigned borrow occurred ($11 < 18$) |
| **V** | 1 | Signed overflow occurred ($25 > 15$) |

---

## Problem 2 (40 pts): 6-bit CMP and CCS Verification

**System:** $N = 6$ bits, $C_N = 64$

- Unsigned range: $[0, 63]$
- Signed range: $[-32, 31]$

`CMP r0, r1` computes `r0 - r1` and sets flags (result not stored).

### Part 1: Determine NZCV Flags (20 pts)

#### Case (a): $r0 = 22$, $r1 = 20$ (10 pts)

$$r0 - r1 = 22 - 20 = 2$$

- **Unsigned:** $2 \in [0, 63]$ → no borrow → $C = 1$
- **Signed:** $2 \in [-32, 31]$ → no overflow → $V = 0$

| Flag | Value | Reasoning |
|---|---|---|
| **N** | 0 | Result 2 is positive (MSB = 0) |
| **Z** | 0 | Result $\neq 0$ |
| **C** | 1 | No borrow ($22 \geq 20$ unsigned) |
| **V** | 0 | No signed overflow |

#### Case (b): $r0 = -20$, $r1 = -22$ (10 pts)

Convert to unsigned: $-20 \to 44$, $-22 \to 42$.

$$r0 - r1 = (-20) - (-22) = 2$$

Unsigned check: $44 - 42 = 2$

- **Unsigned:** $2 \in [0, 63]$ → no borrow → $C = 1$
- **Signed:** $2 \in [-32, 31]$ → no overflow → $V = 0$

| Flag | Value | Reasoning |
|---|---|---|
| **N** | 0 | Result 2 is positive |
| **Z** | 0 | Result $\neq 0$ |
| **C** | 1 | No borrow ($44 \geq 42$ unsigned) |
| **V** | 0 | No signed overflow |

### Part 2: CCS Verification for All 8 Conditions (16 pts)

**CCS Logic Equations (from lecture):**

| CCS | Meaning (signed) | Logic Equation |
|---|---|---|
| **GT** | Greater than | $(V = N)$ AND $(Z = 0)$ |
| **GE** | Greater or equal | $V = N$ |
| **LT** | Less than | $V \neq N$ |
| **LE** | Less or equal | $(V \neq N)$ OR $(Z = 1)$ |
| **HI** | Higher (unsigned >) | $(C = 1)$ AND $(Z = 0)$ |
| **HS** | Higher or same (unsigned ≥) | $C = 1$ |
| **LO** | Lower (unsigned <) | $C = 0$ |
| **LS** | Lower or same (unsigned ≤) | $(C = 0)$ OR $(Z = 1)$ |

#### Case (a): $r0 = 22$, $r1 = 20$ → N=0, Z=0, C=1, V=0

Here $22 > 20$ (both signed and unsigned), so all "greater" conditions should be True.

| CCS | Equation | Evaluation | Result | Expected |
|---|---|---|---|---|
| **GT** | $(V=N)$ AND $(Z=0)$ | $(0=0)$ AND $(0=0)$ = T AND T | **True** ✓ | $22 > 20$ |
| **GE** | $V = N$ | $0 = 0$ | **True** ✓ | $22 \geq 20$ |
| **LT** | $V \neq N$ | $0 \neq 0$? | **False** ✓ | $22 \not< 20$ |
| **LE** | $(V \neq N)$ OR $(Z=1)$ | F OR F | **False** ✓ | $22 \not\leq 20$ |
| **HI** | $(C=1)$ AND $(Z=0)$ | T AND T | **True** ✓ | $22 >_u 20$ |
| **HS** | $C = 1$ | T | **True** ✓ | $22 \geq_u 20$ |
| **LO** | $C = 0$ | F | **False** ✓ | $22 \not<_u 20$ |
| **LS** | $(C=0)$ OR $(Z=1)$ | F OR F | **False** ✓ | $22 \not\leq_u 20$ |

#### Case (b): $r0 = -20$, $r1 = -22$ → N=0, Z=0, C=1, V=0

Flags are identical to Case (a), so CCS results are identical.

Signed: $-20 > -22$ ✓. Unsigned: $44 > 42$ ✓. All conditions consistent.

| CCS | Result |
|---|---|
| **GT** | **True** ✓ |
| **GE** | **True** ✓ |
| **LT** | **False** ✓ |
| **LE** | **False** ✓ |
| **HI** | **True** ✓ |
| **HS** | **True** ✓ |
| **LO** | **False** ✓ |
| **LS** | **False** ✓ |

### Part 3: Logic Equations for EQ and NE (4 pts)

$$\textbf{EQ} \iff (Z = 1)$$

$$\textbf{NE} \iff (Z = 0)$$

**Reasoning:** `CMP r0, r1` computes $r0 - r1$. The result is zero if and only if $r0 = r1$, which sets $Z = 1$. This is independent of signed/unsigned interpretation — equality is the same either way.

---

## Problem 3 (20 pts): Assembly Implementation of `mp_max_ab_i_s`

### Given Template

The example function `mp_x_cmp_y_ab_i_s` compares $x$ vs $y$ and returns $a$ or $b$. We modify it so that $a$ and $b$ are both the values being compared AND the return values.

### C Specification

```c
int mp_max_ab_i_c(int a, int b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}
```

### Assembly Solution

```assembly
@ int mp_max_ab_i_s(int a, int b)
@ Input:
@   * a -> r0
@   * b -> r1
@ Output:
@   * r0
mp_max_ab_i_s:
    cmp   r0, r1                     @ compare a and b
    blt   mp_max_ab_i_s_else         @ if a < b, branch to else (negative logic)
mp_max_ab_i_s_then:
    b     mp_max_ab_i_s_end_if       @ a >= b: r0 already holds a, skip else
mp_max_ab_i_s_else:
    mov   r0, r1                     @ a < b: return b
mp_max_ab_i_s_end_if:
    bx    lr                         @ return
```

### Explanation

- **Negative logic:** The C condition is `a >= b` (GE). We branch on the **opposite** — `a < b` (LT) — to skip the `then` block.
- `BLT` = Branch if Less Than (signed): triggers when $V \neq N$.
- If $a \geq b$: fall through, r0 already contains $a$, branch to end.
- If $a < b$: branch to else, move $b$ into r0.

---

## Problem 4 (30 pts): 64-bit Squared Sum While Loop

### C Specification

```c
int64_t mp_range_square_sum_standard_while_c(int s, int e) {
    int64_t sum = 0;
    int64_t i = s;
    while (i <= e) {
        sum += i * i;
        i++;
    }
    return sum;
}
```

### Key Insight: 64-bit Accumulation

- `sum` is `int64_t` → needs **two 32-bit registers** (e.g., r2=low, r3=high)
- `i*i` uses `SMULL` for 32×32 → 64-bit result
- We accumulate into a 64-bit pair using `ADDS`/`ADC` (add with carry for upper word)
- As noted in the problem, we can reuse `s` (r0) as the loop counter instead of defining a separate `i`
- `int64_t` return: low word in r0, high word in r1 (ARM AAPCS)

### Assembly Solution

```assembly
@ int64_t mp_range_square_sum_standard_while_s(int s, int e)
@ Input:
@   * s -> r0
@   * e -> r1
@ Output:
@   * r0 (low 32 bits of sum)
@   * r1 (high 32 bits of sum)
@ Others:
@   * sum_lo -> r2, sum_hi -> r3
@   * s (r0) used as loop variable i
@   * e saved in r1
@   * r4, r5 used for SMULL temp result
mp_range_square_sum_standard_while_s:
    push  {r4, r5}              @ save callee-saved registers
    ldr   r2, =0                @ sum_lo = 0
    ldr   r3, =0                @ sum_hi = 0
    @ r0 = i = s, r1 = e

mp_range_square_sum_loop:
    cmp   r0, r1                @ compare i and e
    bgt   mp_range_square_sum_end_loop  @ if i > e, exit loop
    smull r4, r5, r0, r0        @ [r5:r4] = i * i (64-bit signed product)
    adds  r2, r2, r4            @ sum_lo += product_lo (set C flag)
    adc   r3, r3, r5            @ sum_hi += product_hi + carry
    add   r0, r0, #1            @ i++
    b     mp_range_square_sum_loop

mp_range_square_sum_end_loop:
    mov   r0, r2                @ return low word in r0
    mov   r1, r3                @ return high word in r1
    pop   {r4, r5}              @ restore callee-saved registers
    bx    lr                    @ return
```

### Explanation

1. **Register allocation:**
   - `r0`: loop variable `i` (initialized to `s`, incremented each iteration)
   - `r1`: loop bound `e` (unchanged)
   - `r2:r3`: 64-bit accumulator `sum` (r2 = low, r3 = high)
   - `r4:r5`: temporary for `SMULL` result (r4 = low, r5 = high)

2. **`SMULL r4, r5, r0, r0`**: Computes $i \times i$ as a full 64-bit signed product. This is necessary because squaring large 32-bit values can exceed 32 bits (e.g., $50000^2 = 2.5 \times 10^9$).

3. **64-bit addition via `ADDS`/`ADC`:**
   - `ADDS r2, r2, r4` adds the low words and sets the Carry flag if there's overflow
   - `ADC r3, r3, r5` adds the high words **plus** the carry from the low addition
   - Together, these correctly accumulate $sum = sum + i^2$ in 64 bits

4. **Return convention:** ARM AAPCS returns 64-bit values in `r0` (low) and `r1` (high).

5. **`PUSH`/`POP` for r4, r5:** These are callee-saved registers per AAPCS, so we preserve them.
