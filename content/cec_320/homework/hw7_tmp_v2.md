# CEC 320 HW 7 — Shift and Bitwise Logic Instructions

---

## Prob 1: Q15.16 Multiplication in Assembly

**Problem:** Given Q31 multiplication code that extracts bits $b_{62}$–$b_{31}$ (right-shift by 31), modify it to perform Q15.16 multiplication that extracts bits $b_{47}$–$b_{16}$ (right-shift by 16).

**Reference Q31 code:**
```assembly
@ int32_t mp_mult_q31_s(int A, int B)
mp_mult_q31_s:
    smull r1, r0, r0, r1   @ [r0:r1] = 64-bit product (r0=HW, r1=LW)
    lsl   r0, #1            @ shift HW left 1 → gets bits b62:b32
    add   r0, r0, r1, lsr #31  @ OR in b31 from LW
    bx    lr
```

After `SMULL r2, r3, r0, r1` (using r2=LW, r3=HW):
```
HW = R3                    LW = R2
 b63 | ... | b33 | b32      b31 | ... | b1 | b0
```

We need bits $b_{47}$–$b_{16}$:
- **Lower half** (bits $b_{31}$–$b_{16}$): these are in R2, obtained by `LSR r2, #16`
- **Upper half** (bits $b_{47}$–$b_{32}$): these are in R3, obtained by `LSL r3, #16`
- Combine with `ORR`

**Solution:**
```assembly
@ int32_t mp_mult_q15p16_s(int A, int B)
mp_mult_q15p16_s:
    smull r2, r3, r0, r1       @ [r3:r2] = 64-bit signed product (r3=HW, r2=LW)
    lsr   r0, r2, #16          @ r0 = LW >> 16 (bits 31:16 → bits 15:0)
    orr   r0, r0, r3, lsl #16  @ OR in HW << 16 (bits 15:0 of HW → bits 31:16)
    bx    lr
```

**Why it works:** `LSR r2, #16` extracts bits $b_{31}$–$b_{16}$ into the lower half of r0. `r3, LSL #16` takes bits $b_{47}$–$b_{32}$ from the high word and places them in the upper half. The `ORR` combines them → r0 holds exactly $b_{47}$–$b_{16}$, which is the 64-bit product right-shifted by 16.

---

## Prob 2: Shift Calculations and Carry Flag

**Given:**
```assembly
ldr  r0, =0b1101_1101   @ R0 = 0x000000DD
lsls r1, r0, #1
lsrs r2, r0, #3
```

$R0 = \texttt{0xDD} = \texttt{0b}\,1101\,1101$

### Instruction 1: `LSLS r1, r0, #1`

Shift R0 left by 1 bit (with flag update).

Full 32-bit R0: `0x000000DD` = `0000...0000 1101 1101`

Shift left by 1:

```
0000...0001 1011 1010
```

$$\boxed{R1 = \texttt{0x000001BA}}$$

**C flag** = bit 31 of R0 before the shift (the bit that gets shifted out of position 31). R0 = `0x000000DD`, so bit 31 = 0.

$$\boxed{C = 0 \text{ (after LSLS)}}$$

### Instruction 2: `LSRS r2, r0, #3`

Shift R0 right by 3 bits (with flag update). The 3 bits shifted out are bits 2, 1, 0 of R0.

```
R0 bits: ...1101 1[101]  ← bits 2:0 shifted out
Result:  ...0001 1011
```

$$\boxed{R2 = \texttt{0x0000001B}}$$

**C flag** = the **last** bit shifted out = bit 2 of R0. R0 bit 2 = 1.

$$\boxed{C = 1 \text{ (after LSRS)}}$$

### Final State

The C flag reflects the **last flag-setting instruction** executed, which is `LSRS`:

| Register | Value |
|---|---|
| R1 | `0x000001BA` |
| R2 | `0x0000001B` |
| **C flag** | **1** (from `LSRS`) |

---

## Prob 3: Single-Line Scaling with Op2

**Given:** Signed integers $A$ in R0, $B$ in R1. No overflow.

The barrel shifter lets us use a shifted register as Op2, so we can combine shift + add/sub in one instruction.

### (a) $A = 16 \times B$

$16B = B \ll 4$

```assembly
lsl r0, r1, #4
```

### (b) $A = 17 \times B$

$17B = B + 16B = B + (B \ll 4)$

```assembly
add r0, r1, r1, lsl #4
```

### (c) $A = 15 \times B$

$15B = 16B - B = (B \ll 4) - B$

Use `RSB` (Reverse Subtract): `Rd = Op2 - Rn`

```assembly
rsb r0, r1, r1, lsl #4
```

### (d) $A = B / 16$

$B / 16 = B \gg 4$ (arithmetic shift for signed)

```assembly
asr r0, r1, #4
```

### (e) $A = 17B / 16$

$17B/16 = B + B/16 = B + (B \gg 4)$

```assembly
add r0, r1, r1, asr #4
```

### (f) $A = 15B / 16$

$15B/16 = B - B/16 = B - (B \gg 4)$

```assembly
sub r0, r1, r1, asr #4
```

---

## Prob 4: Analyzing `mp_func_s`

**Given assembly:**
```assembly
@ uint16_t mp_func_s(uint16_t a);
mp_func_s:
    ldr  r1, =15
    bic  r0, r0, r1, lsl #4    @ r0 = r0 AND NOT(15 << 4)
    ldr  r2, =10
    orr  r0, r0, r2, lsl #4    @ r0 = r0 OR (10 << 4)
    bx   lr
```

### Part 1: Result for $a = \texttt{0x}H_3H_2H_1H_0$

**Step 1 — BIC clears digit $H_1$:**

- `r1 = 15 = 0xF`
- `r1, lsl #4` = `0xF0` = bits 7:4
- `BIC` = `AND NOT`: `r0 = r0 AND NOT(0xF0)` = `r0 AND 0xFF0F`
- Result: $\texttt{0x}H_3H_2\textbf{0}H_0$ (digit $H_1$ cleared)

**Step 2 — ORR sets digit $H_1$ to A:**

- `r2 = 10 = 0xA`
- `r2, lsl #4` = `0xA0`
- `ORR`: `r0 = r0 OR 0xA0`
- Result: $\texttt{0x}H_3H_2\textbf{A}H_0$

$$\boxed{b = \texttt{0x}H_3H_2\texttt{A}H_0}$$

### Part 2: C Translation

```c
uint16_t mp_func_c(uint16_t a) {
    return (a & ~(0xF << 4)) | (0xA << 4);
}
```

Equivalently: `return (a & 0xFF0F) | 0x00A0;`

---

## Prob 5: Logic and Shift Trace

**Given:** $R0 = A = \texttt{0xAD}$ (`1010_1101`), $R1 = mask = \texttt{0x03}$ (`0000_0011`).

### Step-by-step

**1.** `lsr r2, r1, #2` — shift mask right by 2

$\texttt{0x03} = \texttt{0000\_0011} \gg 2 = \texttt{0000\_0000}$

$$\boxed{R2 = \texttt{0x00}}$$

**2.** `lsl r2, #2` — shift R2 left by 2

$\texttt{0x00} \ll 2 = \texttt{0x00}$ (shifting zero gives zero)

$$\boxed{R2 = \texttt{0x00}}$$

**3.** `bic r3, r0, r1` — bit clear: $R3 = R0 \;\texttt{AND NOT}(R1)$

```
  1010_1101  (0xAD)
AND 1111_1100  (NOT 0x03)
= 1010_1100
```

$$\boxed{R3 = \texttt{0xAC}}$$

**4.** `orr r4, r3, r1` — OR: $R4 = R3 \;|\; R1$

```
  1010_1100  (0xAC)
OR 0000_0011  (0x03)
= 1010_1111
```

$$\boxed{R4 = \texttt{0xAF}}$$

**5.** `eor r5, r0, r1` — XOR: $R5 = R0 \oplus R1$

```
  1010_1101  (0xAD)
XOR 0000_0011  (0x03)
= 1010_1110
```

$$\boxed{R5 = \texttt{0xAE}}$$

### Summary

| Register | Binary | Hex |
|---|---|---|
| R2 | `0000_0000` | `0x00` |
| R3 | `1010_1100` | `0xAC` |
| R4 | `1010_1111` | `0xAF` |
| R5 | `1010_1110` | `0xAE` |

---

## Prob 6: Digit Manipulation Functions

**Given:** $A$ is `uint16_t`, written as $\texttt{0x}H_3H_2H_1H_0$.

### Part (a): $\texttt{0x}H_3H_2H_1H_0 \Rightarrow \texttt{0x}H_3H_2\texttt{5}H_0$

Replace digit $H_1$ (bits 7:4) with 5. Same pattern as Prob 4 — clear then set.

**C function:**
```c
uint16_t mp_func_a_in_c(uint16_t A) {
    return (A & 0xFF0F) | 0x0050;
}
```

**ASM function:**
```assembly
@ uint16_t mp_func_a_in_s(uint16_t A)
@ Input: A -> r0
@ Output: r0
mp_func_a_in_s:
    bic r0, r0, #0xF0       @ clear bits 7:4 (digit H1)
    orr r0, r0, #0x50       @ set bits 7:4 to 5
    bx  lr
```

### Part (b): $\texttt{0x}H_3H_2H_1H_0 \Rightarrow \texttt{0x}H_2H_1H_0\texttt{3}$

Shift left by one hex digit (4 bits), insert 3 as new LSB digit.

**C function:**
```c
uint16_t mp_func_b_in_c(uint16_t A) {
    return (A << 4) | 0x3;
}
```

**ASM function:**
```assembly
@ uint16_t mp_func_b_in_s(uint16_t A)
@ Input: A -> r0
@ Output: r0
mp_func_b_in_s:
    lsl r0, r0, #4          @ shift left 4 bits: 0xH2H1H00
    orr r0, r0, #3          @ insert 3 in lowest digit
    bx  lr
```

### Part (c): $\texttt{0x}H_3H_2H_1H_0 \Rightarrow \texttt{0x7}H_3H_2H_1$

Shift right by one hex digit (4 bits), insert 7 as new MSB digit.

**C function:**
```c
uint16_t mp_func_c_in_c(uint16_t A) {
    return (A >> 4) | 0x7000;
}
```

**ASM function:**
```assembly
@ uint16_t mp_func_c_in_s(uint16_t A)
@ Input: A -> r0
@ Output: r0
mp_func_c_in_s:
    lsr r0, r0, #4          @ shift right 4 bits: 0x0H3H2H1
    ldr r1, =0x7000
    orr r0, r0, r1          @ insert 7 in highest digit
    bx  lr
```

**Note:** `0x7000` can't be directly encoded as an ARM immediate in `ORR` (doesn't fit the 8-bit rotated format), so we use `LDR` to load the constant first.
