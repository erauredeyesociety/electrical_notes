# CEC 320 HW 8 (PDF labeled HW 9) — Status Flags, CCS, and Branch

---

## Prob 1: 5-bit Signed/Unsigned Operations

**System:** $N = 5$ bits, $C_N = 2^5 = 32$
- Unsigned range: $[0, 31]$
- Signed range: $[-16, 15]$

### Part (a): $(-15) + (-5)$

**Step 1 — Represent operands in 5-bit binary:**

| Decimal | Unsigned equivalent | 5-bit Binary |
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
| **C** | 1 | Unsigned carry: $44 \geq 32$ |
| **V** | 1 | Signed overflow: $-20 < -16$ |

### Part (b): $11 - 18$

**Step 1 — Represent operands in 5-bit binary:**

| Decimal | 5-bit Binary | Notes |
|---|---|---|
| $11$ | `01011` | |
| $18$ | `10010` | As signed 5-bit: $18 - 32 = -14$ |

**Step 2 — Unsigned interpretation ($u_{temp}$):**

$$u_{temp} = 11 - 18 = -7$$

$-7 < 0$ (below unsigned min) → **Borrow** → $C = 0$ (ARM convention: $C = 1 - \text{Borrow}$)

Corrected unsigned result: $-7 + 32 = \mathbf{25}$

**Step 3 — Signed interpretation ($s_{temp}$):**

The operands as signed 5-bit are $11$ and $-14$ (since `10010` = $18 - 32 = -14$):

$$s_{temp} = 11 - (-14) = 25$$

$25 > 15$ (exceeds signed max) → **Overflow** ($V = 1$)

Corrected signed result: $25 - 32 = \mathbf{-7}$

**Step 4 — Binary result:**

$$25 = \mathbf{0b\,11001}$$

Verify: as signed, `11001` $= -32 + 25 = -7$ ✓

**Step 5 — NZCV flags:**

| Flag | Value | Reasoning |
|---|---|---|
| **N** | 1 | MSB (bit 4) of `11001` is 1 |
| **Z** | 0 | Result $\neq 0$ |
| **C** | 0 | Unsigned borrow: $11 < 18$ |
| **V** | 1 | Signed overflow: $25 > 15$ |

---

## Prob 2: 6-bit CMP and CCS Verification

**System:** $N = 6$ bits, $C_N = 64$
- Unsigned range: $[0, 63]$
- Signed range: $[-32, 31]$

`CMP r0, r1` computes `r0 - r1` and sets NZCV flags (result not stored).

### Part 1: Determine NZCV Flags

#### Case (a): $r0 = 22$, $r1 = 20$

$$r0 - r1 = 22 - 20 = 2$$

- **Unsigned:** $2 \in [0, 63]$ → no borrow → $C = 1$
- **Signed:** $2 \in [-32, 31]$ → no overflow → $V = 0$

| Flag | Value | Reasoning |
|---|---|---|
| **N** | 0 | Result 2 is positive (MSB = 0) |
| **Z** | 0 | Result $\neq 0$ |
| **C** | 1 | No borrow ($22 \geq 20$ unsigned) |
| **V** | 0 | No signed overflow |

#### Case (b): $r0 = -20$, $r1 = -22$

Convert to 6-bit unsigned: $-20 \to 44$, $-22 \to 42$.

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

### Part 2: CCS Verification — All 8 Conditions

**CCS Logic Equations (from Lctr 19):**

| CCS | Meaning | Logic Equation |
|---|---|---|
| **GT** | Signed > | $(V = N)$ AND $(Z = 0)$ |
| **GE** | Signed ≥ | $V = N$ |
| **LT** | Signed < | $V \neq N$ |
| **LE** | Signed ≤ | $(V \neq N)$ OR $(Z = 1)$ |
| **HI** | Unsigned > | $(C = 1)$ AND $(Z = 0)$ |
| **HS** | Unsigned ≥ | $C = 1$ |
| **LO** | Unsigned < | $C = 0$ |
| **LS** | Unsigned ≤ | $(C = 0)$ OR $(Z = 1)$ |

#### Case (a): $r0 = 22$, $r1 = 20$ → N=0, Z=0, C=1, V=0

$22 > 20$ both signed and unsigned, so all "greater" conditions should be True.

| CCS | Equation | Evaluation | Result | Consistent? |
|---|---|---|---|---|
| **GT** | $(V=N)$ AND $(Z=0)$ | $(0=0)$ AND $(0=0)$ = T AND T | **True** | $22 > 20$ ✓ |
| **GE** | $V = N$ | $0 = 0$ | **True** | $22 \geq 20$ ✓ |
| **LT** | $V \neq N$ | $0 \neq 0$? No | **False** | $22 \not< 20$ ✓ |
| **LE** | $(V \neq N)$ OR $(Z=1)$ | F OR F | **False** | $22 \not\leq 20$ ✓ |
| **HI** | $(C=1)$ AND $(Z=0)$ | T AND T | **True** | $22 >_u 20$ ✓ |
| **HS** | $C = 1$ | T | **True** | $22 \geq_u 20$ ✓ |
| **LO** | $C = 0$ | F | **False** | $22 \not<_u 20$ ✓ |
| **LS** | $(C=0)$ OR $(Z=1)$ | F OR F | **False** | $22 \not\leq_u 20$ ✓ |

#### Case (b): $r0 = -20$, $r1 = -22$ → N=0, Z=0, C=1, V=0

Flags are **identical** to Case (a), so all CCS results are the same.

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

### Part 3: Logic Equations for EQ and NE

$$\boxed{\textbf{EQ} \iff (Z = 1)}$$

$$\boxed{\textbf{NE} \iff (Z = 0)}$$

**Why:** `CMP r0, r1` computes $r0 - r1$. The result is zero iff $r0 = r1$, which sets $Z = 1$. Equality is the same regardless of signed/unsigned interpretation.

---

## Prob 3: Assembly `mp_max_ab_i_s`

**Problem:** Modify the given `mp_x_cmp_y_ab_i_s` template to implement:

```c
int mp_max_ab_i_c(int a, int b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}
```

**Key difference from template:** In the template, `x` and `y` (r2, r3) are compared but `a` and `b` (r0, r1) are returned. Here, $a$ and $b$ are both the comparison operands AND the return values.

**Negative logic:** The C condition is `a >= b` (GE). We branch on the **opposite** — `a < b` (LT) — to skip the `then` block.

**Solution:**
```assembly
@ int mp_max_ab_i_s(int a, int b)
@ Input:
@   * a -> r0
@   * b -> r1
@ Output:
@   * r0
mp_max_ab_i_s:
    cmp   r0, r1                     @ compare a and b (sets NZCV)
    blt   mp_max_ab_i_s_else         @ if a < b, branch to else (negative logic)
mp_max_ab_i_s_then:
    b     mp_max_ab_i_s_end_if       @ a >= b: r0 already holds a, skip else
mp_max_ab_i_s_else:
    mov   r0, r1                     @ a < b: put b in r0 for return
mp_max_ab_i_s_end_if:
    bx    lr                         @ return
```

**Walkthrough:**
- `CMP r0, r1` sets flags for $a - b$
- `BLT` = Branch if Less Than (signed): fires when $V \neq N$
- If $a \geq b$: fall through to `then`, r0 already contains $a$, branch to end
- If $a < b$: branch to `else`, `MOV r0, r1` puts $b$ in the return register

---

## Prob 4: 64-bit Squared Sum While Loop

**Problem:** Modify the given `mp_range_sum_for_while_s` (which computes $\sum_{i=s}^{e} i$) to compute $\sum_{i=s}^{e} i^2$ with a 64-bit accumulator.

**C specification:**
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

**Key differences from template:**
1. `sum` is `int64_t` → needs **two** 32-bit registers (lo/hi pair)
2. `i*i` needs `SMULL` for 32×32 → 64-bit product
3. 64-bit addition via `ADDS`/`ADC` (add with carry for upper word)
4. Return convention: `int64_t` returns in r0 (low) and r1 (high) per ARM AAPCS
5. Per problem hint: no need for 64-bit `i` in ASM — use `s` (r0) as the loop counter

**Solution:**
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
@   * s (r0) reused as loop variable i
@   * e stays in r1
@   * r4, r5 used for SMULL temp result
mp_range_square_sum_standard_while_s:
    push  {r4, r5}                          @ save callee-saved registers
    ldr   r2, =0                            @ sum_lo = 0
    ldr   r3, =0                            @ sum_hi = 0
    @ r0 = i = s, r1 = e

mp_range_square_sum_loop:
    cmp   r0, r1                            @ compare i and e
    bgt   mp_range_square_sum_end_loop      @ if i > e, exit loop
    smull r4, r5, r0, r0                    @ [r5:r4] = i * i (64-bit signed)
    adds  r2, r2, r4                        @ sum_lo += product_lo (sets C flag)
    adc   r3, r3, r5                        @ sum_hi += product_hi + carry
    add   r0, r0, #1                        @ i++
    b     mp_range_square_sum_loop          @ repeat

mp_range_square_sum_end_loop:
    mov   r0, r2                            @ return low word in r0
    mov   r1, r3                            @ return high word in r1
    pop   {r4, r5}                          @ restore callee-saved registers
    bx    lr                                @ return
```

**Register allocation:**

| Register | Purpose |
|---|---|
| r0 | Loop variable `i` (initialized to `s`, incremented each iteration) |
| r1 | Loop bound `e` (unchanged throughout) |
| r2 | `sum` low word (bits 31:0) |
| r3 | `sum` high word (bits 63:32) |
| r4 | `SMULL` result low word (temp) |
| r5 | `SMULL` result high word (temp) |

**Why `SMULL`:** Squaring large 32-bit values can exceed 32 bits (e.g., $50000^2 = 2.5 \times 10^9 > 2^{31}$). `SMULL` gives the full 64-bit signed product.

**Why `ADDS`/`ADC`:** This is the standard pattern for 64-bit addition on a 32-bit processor:
- `ADDS r2, r2, r4` adds the low words and sets the C flag if there's a carry out of bit 31
- `ADC r3, r3, r5` adds the high words **plus** the carry from the low addition
- Together: $[r3:r2] = [r3:r2] + [r5:r4]$

**Why `PUSH`/`POP`:** r4 and r5 are callee-saved registers per AAPCS — the function must preserve their values for the caller.
