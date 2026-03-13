# CEC 320 Homework 7 Solutions — Shift and Bitwise Logic Instructions

**Total Points: 111**

---

## Problem 1 (10 pts): Q15.16 Multiplication in Assembly

### Background

Q31 multiplication shifts the 64-bit product right by 31 bits to extract bits $b_{62}$ down to $b_{31}$. For Q15.16, we need bits $b_{47}$ down to $b_{16}$ — a right shift of **16** bits instead of 31.

After `SMULL r2, r3, r0, r1` (using r2=LW, r3=HW):

```
HW = R3                    LW = R2
 b63 | ... | b33 | b32      b31 | ... | b1 | b0
```

We need to extract:

```
 b47 | ... | b17 | b16
```

### Solution

```assembly
@ int32_t mp_mult_q15p16_s(int A, int B)
mp_mult_q15p16_s:
    smull r2, r3, r0, r1   @ [r3:r2] = 64-bit signed product (r3=HW, r2=LW)
    lsr   r0, r2, #16      @ r0 = LW >> 16 (bits 31:16 of LW become bits 15:0)
    orr   r0, r0, r3, lsl #16  @ OR in HW << 16 (bits 15:0 of HW become bits 31:16)
    bx    lr
```

### Explanation

- `lsr r0, r2, #16` — extracts bits $b_{31}$–$b_{16}$ from the low word into the lower half of r0
- `orr r0, r0, r3, lsl #16` — takes bits $b_{47}$–$b_{32}$ from the high word (shifted left 16) and combines them into the upper half of r0
- Result: r0 holds bits $b_{47}$ through $b_{16}$ of the 64-bit product, which is exactly a right-shift by 16

---

## Problem 2 (15 pts): Shift Calculations and Carry Flag

### Given

```assembly
ldr  r0, =0b1101_1101   @ R0 = 0x000000DD
lsls r1, r0, #1
lsrs r2, r0, #3
```

$R0 = \texttt{0xDD} = \texttt{0b}1101\_1101$

### Instruction 1: `LSLS r1, r0, #1` (5 pts)

Logical shift left by 1 (with flag update):

$$R0 = \underbrace{0\ldots0}_{24} \; 1101\_1101$$

Shift left by 1:

$$R1 = \underbrace{0\ldots0}_{23} \; 1\_1011\_1010$$

$$\boxed{R1 = \texttt{0x000001BA}}$$

**C flag:** The MSB of the original value (bit 31) was 0, but for the shift, the C flag is set to the **last bit shifted out** (bit 31 of the source before shift). Since R0 bit 31 = 0:

Wait — more precisely, `LSLS r1, r0, #1` shifts R0 left by 1 and the bit shifted out of position 31 becomes C. R0 = 0x000000DD, so bit 31 = 0.

**C flag = 0** after `LSLS`.

### Instruction 2: `LSRS r2, r0, #3` (5 pts)

Logical shift right by 3 (with flag update):

$$R0 = \underbrace{0\ldots0}_{24} \; 1101\_1\underbrace{101}_{shifted\ out}$$

Shift right by 3:

$$R2 = \underbrace{0\ldots0}_{27} \; 1\_1011 = \texttt{0x1B}$$

$$\boxed{R2 = \texttt{0x0000001B}}$$

**C flag:** The last bit shifted out is bit 2 of R0. $R0$ bit 2 = 1.

$$\boxed{C = 1}$$

### Final Answer (after both instructions execute, C flag reflects the last flag-setting instruction = `LSRS`)

| Register | Value |
|---|---|
| R1 | `0x000001BA` |
| R2 | `0x0000001B` |
| C flag | **1** (from `LSRS`) |

---

## Problem 3 (30 pts): Single-Line Scaling with Op2

**Given:** Signed integers $A$ in R0, $B$ in R1. No overflow.

### (a) $A = 16 \times B$ (5 pts)

$$16B = B \ll 4$$

```assembly
lsl r0, r1, #4
```

### (b) $A = 17 \times B$ (5 pts)

$$17B = B + 16B = B + (B \ll 4)$$

```assembly
add r0, r1, r1, lsl #4
```

### (c) $A = 15 \times B$ (5 pts)

$$15B = 16B - B = (B \ll 4) - B$$

```assembly
rsb r0, r1, r1, lsl #4
```

### (d) $A = B / 16$ (5 pts)

$$B / 16 = B \gg 4 \quad \text{(arithmetic shift for signed)}$$

```assembly
asr r0, r1, #4
```

### (e) $A = 17B / 16$ (5 pts)

$$17B/16 = B + B/16 = B + (B \gg 4)$$

```assembly
add r0, r1, r1, asr #4
```

### (f) $A = 15B / 16$ (5 pts)

$$15B/16 = B - B/16 = B - (B \gg 4)$$

```assembly
sub r0, r1, r1, asr #4
```

---

## Problem 4 (10 pts): Analyzing `mp_func_s`

### Given

```assembly
@ uint16_t mp_func_s(uint16_t a);
mp_func_s:
    ldr  r1, =15
    bic  r0, r0, r1, lsl #4    @ clear bits 7:4
    ldr  r2, =10
    orr  r0, r0, r2, lsl #4    @ set bits 7:4 to 0xA
    bx   lr
```

### Part 1: Result for $a = \texttt{0x}H_3H_2H_1H_0$ (5 pts)

**Step-by-step:**

1. `r1 = 15 = 0xF`
2. `bic r0, r0, r1, lsl #4` → `r0 = r0 AND NOT(0xF << 4)` = `r0 AND NOT(0xF0)` = `r0 AND 0xFF0F`
   - Clears digit $H_1$ (bits 7:4) → $\texttt{0x}H_3H_2\mathbf{0}H_0$
3. `r2 = 10 = 0xA`
4. `orr r0, r0, r2, lsl #4` → `r0 = r0 OR (0xA << 4)` = `r0 OR 0xA0`
   - Sets digit $H_1$ to $\texttt{A}$ → $\texttt{0x}H_3H_2\mathbf{A}H_0$

$$\boxed{b = \texttt{0x}H_3H_2\texttt{A}H_0}$$

### Part 2: C Translation (5 pts)

```c
uint16_t mp_func_c(uint16_t a) {
    return (a & ~(0xF << 4)) | (0xA << 4);
}
```

Or equivalently:

```c
uint16_t mp_func_c(uint16_t a) {
    return (a & 0xFF0F) | 0x00A0;
}
```

---

## Problem 5 (16 pts): Logic and Shift Trace

**Given:** $R0 = A = \texttt{0xAD}$ ($\texttt{0b}1010\_1101$), $R1 = mask = \texttt{0x03}$ ($\texttt{0b}0000\_0011$).

### Step-by-step execution

**1.** `lsr r2, r1, #2` — $R2 = \texttt{0x03} \gg 2 = \texttt{0b}0000\_0000$ (4 pts)

$$\boxed{R2 = \texttt{0x00}}$$

**2.** `lsl r2, #2` — $R2 = \texttt{0x00} \ll 2 = \texttt{0b}0000\_0000$ (4 pts)

$$\boxed{R2 = \texttt{0x00}}$$

**3.** `bic r3, r0, r1` — $R3 = R0 \texttt{ AND NOT}(R1) = \texttt{0xAD} \;\&\; \texttt{0xFC}$ (4 pts)

$$\texttt{1010\_1101 AND 1111\_1100} = \texttt{1010\_1100}$$

$$\boxed{R3 = \texttt{0xAC}}$$

**4.** `orr r4, r3, r1` — $R4 = R3 \texttt{ OR } R1 = \texttt{0xAC} \;|\; \texttt{0x03}$ (4 pts)

$$\texttt{1010\_1100 OR 0000\_0011} = \texttt{1010\_1111}$$

$$\boxed{R4 = \texttt{0xAF}}$$

**5.** `eor r5, r0, r1` — $R5 = R0 \texttt{ XOR } R1 = \texttt{0xAD} \oplus \texttt{0x03}$ (4 pts — not counted toward 16 total, but included)

$$\texttt{1010\_1101 XOR 0000\_0011} = \texttt{1010\_1110}$$

$$\boxed{R5 = \texttt{0xAE}}$$

### Summary Table

| Register | Binary | Hex |
|---|---|---|
| R2 | `0000_0000` | `0x00` |
| R3 | `1010_1100` | `0xAC` |
| R4 | `1010_1111` | `0xAF` |
| R5 | `1010_1110` | `0xAE` |

---

## Problem 6 (30 pts): Digit Manipulation Functions

**Given:** $A$ is `uint16_t`, written as $\texttt{0x}H_3H_2H_1H_0$.

### Part (a): $\texttt{0x}H_3H_2H_1H_0 \Rightarrow \texttt{0x}H_3H_2\texttt{5}H_0$ (4 + 6 = 10 pts)

Replace digit $H_1$ (bits 7:4) with 5.

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

### Part (b): $\texttt{0x}H_3H_2H_1H_0 \Rightarrow \texttt{0x}H_2H_1H_0\texttt{3}$ (4 + 6 = 10 pts)

Shift left by one hex digit (4 bits) and insert 3 as the new LSB digit.

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

### Part (c): $\texttt{0x}H_3H_2H_1H_0 \Rightarrow \texttt{0x7}H_3H_2H_1$ (4 + 6 = 10 pts)

Shift right by one hex digit (4 bits) and insert 7 as the new MSB digit.

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

**Note:** `0x7000` cannot be directly encoded as an immediate in the `ORR` instruction (it doesn't fit the 8-bit rotated immediate format), so we use `LDR` to load the constant first.
