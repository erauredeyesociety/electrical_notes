# CEC 320 Homework Solutions Summary (Quiz 3)

Consolidated summary of HW6, HW7, and HW8 (labeled HW9 in PDF) solutions for quiz preparation.

---

## HW 6: Mixed C and Assembly Programming (112 pts total)

### Problem 1 (20 pts) -- Stack Push Operations

**Setup:** Ri has value `(1 << i) + (1 << 2i)` for i = 1..12. SP = 0x2000_1020 (descending full stack). Instruction: `push {r7, r5, r8, r6}`.

**Part 1: SP after push?**
- Answer: **0x2000_1010**
- Each push decrements SP by 4. Four registers = 16 bytes = 0x10 decrement.

**Part 2: Value of R5?**
- Answer: **0x0420**
- R5 = (1 << 5) + (1 << 10) = 0x20 + 0x400 = 0x0420

**Part 3: Word at address 0x2000_1014?**
- Answer: **0x1040**
- Registers are pushed in order R8, R7, R6, R5 (highest register number at highest address).
- Addresses: R8 at 0x201C, R7 at 0x2018, R6 at 0x2014, R5 at 0x2010.
- R6 = (1 << 6) + (1 << 12) = 0x40 + 0x1000 = 0x1040

**Part 4: Byte at address 0x2000_1014?**
- Answer: **0x40**
- Least significant byte of R6 (0x1040) is 0x40.

**Key concept:** Push always stores registers in order of register number regardless of the order listed in the instruction.

---

### Problem 2 (12 pts) -- Unsigned Function Arguments (EABI)

**Setup:** `uint8_t var1 = 0xF; uint8_t var2 = 0xFF;` called as `fn1(var1, var2, 0xFFF, 0xFFFF)` with prototype `void fn1(uint32_t x, uint32_t y, uint32_t z, uint32_t w)`.

**Answer:**
- R0 = 0xF
- R1 = 0xFF
- R2 = 0xFFF
- R3 = 0xFFFF

**Key concept:** First four arguments go to R0-R3. Unsigned values are zero-extended to 32 bits.

---

### Problem 3 (10 pts) -- Signed Function Arguments (Sign Extension)

**Setup:** `int8_t var1 = 0xF; int8_t var2 = 0xFF;` called as `fn2(var1, var2)` with prototype `void fn2(int32_t x, int32_t y)`.

**Answer:**
- R0 = **15** (0x0000_000F)
- R1 = **-1** (0xFFFF_FFFF)

**Key concept:** var2 = 0xFF as int8_t is -1. Sign extension from 8-bit to 32-bit preserves the value (-1 becomes 0xFFFF_FFFF).

---

### Problem 4 (10 pts) -- Q15.16 Fixed-Point Return Value

**Setup:** ASM function returns center of gravity in Q15.16 format. Real value = 3.25.

**Part (a): Encoded value?**
- Formula: 3.25 * 2^16 = 3.25 * 65536 = 213,504
- 3.25 * 4 * 2^14 = 13 * 2^14 = 52 * 2^12
- Answer: **0x0003_4000**
- Binary: 0b0000_0000_0000_0011_0100_0000_0000_0000

**Part (b): Return register?**
- Answer: **R0** (per EABI standard)

---

### Problem 5 (20 pts) -- 64-bit Addition Test Cases

**Assembly function:**
```asm
mp_add_64bit_s:
    adds    r0, r2
    adc     r1, r3
    bx      lr
```

**Test values:**
```c
int64_t A1 = (int64_t)0x388<<24, B1 = (int64_t)0x289<<24;
int64_t A2 = (int64_t)0x378<<24, B2 = (int64_t)0x279<<24;
```

**Part 1: Results**
- A1 + B1 = `(int64_t)0x611<<24`
- A2 + B2 = `(int64_t)0x5F1<<24`

**Part 2: Carry flags**
- A1 + B1: **C = 1** (carry from low word to high word: 0x88000000 + 0x89000000 overflows 32 bits)
- A2 + B2: **C = 0** (no carry from low word)

**Key concept:** `adds` sets flags on the low-word addition. `adc` adds the high words plus the carry.

---

### Problem 6 (20 pts) -- 64-bit Subtraction Test Cases

**Assembly function:**
```asm
mp_sub_64bit_s:
    subs    r0, r2
    sbc     r1, r3
    bx      lr
```

**Test values:**
```c
int64_t A1 = (int64_t)0x387<<28, B1 = (int64_t)0x28<<28;
int64_t A2 = (int64_t)0x388<<28, B2 = (int64_t)0x288<<28;
```

**Part 1: Results**
- A1 - B1 = `(int64_t)0x35F<<28`
- A2 - B2 = `(int64_t)0x100<<28`

**Part 2: Carry flags**
- A1 - B1: **C = 0** (borrow occurred, C = 1 - B = 0)
- A2 - B2: **C = 1** (no borrow, C = 1 - B = 1)

**Key concept:** In ARM subtraction, C flag = NOT borrow. If borrow occurs, C = 0.

---

### Problem 7 (20 pts) -- Unsigned Modulo in Assembly

**Task:** Implement `uint32_t umod32bit_s(uint32_t A, uint32_t B)` as `A % B = A - (A/B)*B`.

```asm
umod32bit_s:
    udiv    r2, r0, r1      @ r2 = A/B
    mul     r2, r1          @ r2 = (A/B) * B
    sub     r0, r2          @ r0 = A - (A/B)*B
    bx      lr
```

---

## HW 7: Shift and Bitwise Logic Instructions (111 pts total)

### Problem 1 (10 pts) -- Q15.16 Multiplication

**Background:** Q31 multiplication code:
```asm
mp_mult_q31_s:
    smull   r1, r0, r0, r1   @ 64-bit result: HW in R0, LW in R1
    lsl     r0, #1            @ shift HW left by 1
    add     r0, r0, r1, lsr #31  @ bring in bit 31 from LW
    bx      lr
```

After `smull`, bits are: R0 = [b63..b32], R1 = [b31..b0]. Q31 needs bits [b62..b31]. Q15.16 needs bits [b47..b16].

**Solution for Q15.16:**
```asm
mp_mult_q15p16_s:
    smull   r1, r0, r0, r1
    lsl     r0, #16           @ shift HW left by 16 (47-31 = 16)
    add     r0, r0, r1, lsr #16  @ bring in top 16 bits of LW
    bx      lr
```

**Key formula:** Right shift of LW = number of fractional bits in format. Left shift of HW = (target MSB position - 31).

**Note:** For Q16.15 the shifts would be `lsl r0, #17` and `lsr #15`.

---

### Problem 2 (15 pts) -- Shift Operations and C Flag

**Code:**
```asm
ldr     r0, =0b1101_1101
lsls    r1, r0, #1
lsrs    r2, r0, #3
```

**Answers:**
- R1 = 0b1_1011_1010 = **0x1BA**
- R2 = 0b0001_1011 = **0x1B**
- C flag = **1** (last bit shifted out by `lsrs` was b2 of R0, which is 1)

**Key concept:** The C flag is set to the last bit shifted out. `lsrs` shifts right by 3, so the last bit out is bit 2.

---

### Problem 3 (30 pts) -- Barrel Shifter Scaling (Single Instruction)

Signed integers A in R0, B in R1.

| Operation | Assembly | Decomposition |
|---|---|---|
| A = 16 * B | `lsl r0, r1, #4` | 16 = 2^4 |
| A = 17 * B | `add r0, r1, r1, lsl #4` | 17 = 1 + 2^4 |
| A = 15 * B | `rsb r0, r1, r1, lsl #4` | 15 = 2^4 - 1 |
| A = B / 16 | `asr r0, r1, #4` | 1/16 = 2^(-4) |
| A = 17*B/16 | `add r0, r1, r1, asr #4` | 17/16 = 1 + 2^(-4) |
| A = 15*B/16 | `sub r0, r1, r1, asr #4` | 15/16 = 1 - 2^(-4) |

**Key concept:** Use `asr` (not `lsr`) for signed division. `rsb` (reverse subtract) computes Op2 - Rn, useful for (2^n - 1) * B patterns.

---

### Problem 4 (10 pts) -- BIC/ORR Bit Field Manipulation

**Assembly function:**
```asm
@ uint16_t mp_func_s(uint16_t a);
mp_func_s:
    ldr     r1, =15
    bic     r0, r0, r1, lsl #4    @ clear bits [7:4]
    ldr     r2, =10
    orr     r0, r0, r2, lsl #4    @ set bits [7:4] to 0xA
    bx      lr
```

**Part 1:** If a = 0xH3 H2 H1 H0, result = **0xH3 H2 A H0** (replaces second hex digit with A).

**Part 2: C equivalent:**
```c
uint16_t mp_func_c(uint16_t a) {
    a &= ~(15 << 4);   // clear the nibble
    a |= (10 << 4);    // set the nibble to 0xA
    return a;
}
```

**Key concept:** To assign a bit field: (1) BIC to clear, then (2) ORR to set.

---

### Problem 5 (16 pts) -- Bitwise Logic Operations

**Given:** R0 = 0xAD = 0b1010_1101, R1 = 0x03 = 0b0000_0011

```asm
lsr     r2, r1, #2      @ 0x03 >> 2 = 0
lsl     r2, #2          @ 0 << 2 = 0
bic     r3, r0, r1      @ 0xAD & ~0x03 = 0b1010_1100
orr     r4, r3, r1      @ 0xAC | 0x03  = 0b1010_1111
eor     r5, r0, r1      @ 0xAD ^ 0x03  = 0b1010_1110
```

**Answers (LSB):**
- R2 = **0x00**
- R3 = **0xAC**
- R4 = **0xAF**
- R5 = **0xAE**

---

### Problem 6 (30 pts) -- Hex Digit Manipulation (C and ASM)

**(a) Replace H1 with 5:** 0xH3 H2 H1 H0 => 0xH3 H2 5 H0

```c
uint16_t mp_func_a_in_c(uint16_t A) {
    A &= ~(15u << 4);    // clear nibble at position 1
    A |= 5u << 4;        // set nibble to 5
    return A;
}
```

```asm
@ uint16_t mp_func_a_in_s(uint16_t A)
mp_func_a_in_s:
    ldr     r1, =15
    lsl     r1, #4
    bic     r0, r1
    ldr     r2, =5
    lsl     r2, #4
    orr     r0, r2
    bx      lr
```

**(b) Shift left and insert 3:** 0xH3 H2 H1 H0 => 0xH2 H1 H0 3

```c
uint16_t mp_func_b_in_c(uint16_t A) {
    A <<= 4;
    A |= 3;
    return A;
}
```

```asm
@ uint16_t mp_func_b_in_s(uint16_t A)
mp_func_b_in_s:
    lsl     r0, #4
    orr     r0, #3
    bx      lr
```

**(c) Shift right and insert 7 at top:** 0xH3 H2 H1 H0 => 0x7 H3 H2 H1

```c
uint16_t mp_func_c_in_c(uint16_t A) {
    A >>= 4;
    A |= (7U << 12);
    return A;
}
```

```asm
@ uint16_t mp_func_c_in_s(uint16_t A)
mp_func_c_in_s:
    lsr     r0, #4
    ldr     r1, =7
    lsl     r1, #12
    orr     r0, r1
    bx      lr
```

**Key concept:** Shift + ORR pattern for inserting digits. BIC + ORR pattern for replacing digits in place.

---

## HW 8: Status Flags, CCS, and Branch (132 pts total)

### Problem 1 (42 pts) -- NZCV Flags on a 5-bit System

**Constants for 5-bit system:** C_N = 32, U_MIN = 0, U_MAX = 31, S_MIN = -16, S_MAX = 15.

#### (a) (-15) + (-5)

**Unsigned view:** u_temp = (-15 + 32) + (-5 + 32) = 17 + 27 = 44 > U_MAX(31)
- Result = 44 - 32 = **12**
- **C = 1** (carry)
- **Z = 0**

**Signed view:** s_temp = -15 + (-5) = -20 < S_MIN(-16)
- Result = -20 + 32 = **12**
- **V = 1** (overflow)
- **N = 0** (result is positive in binary: 0b01100)

**Binary result:** **0b01100**

#### (b) 11 - 18

**Unsigned view:** u_temp = 11 - 18 = -7 < U_MIN(0)
- Result = -7 + 32 = **25**
- **C = 0** (borrow)
- **Z = 0**

**Signed view:** s_temp = 11 - (18 - 32) = 11 + 14 = 25 > S_MAX(15)
- Result = 25 - 32 = **-7**
- **V = 1** (overflow)
- **N = 1** (result is negative)

**Binary result:** **0b11001**

---

### Problem 2 (40 pts) -- CMP and Condition Code Suffixes (6-bit system)

**Constants for 6-bit system:** C_N = 64, U_MIN = 0, U_MAX = 63, S_MIN = -32, S_MAX = 31.

#### Part 1: Flags after CMP r0, r1

**(a) r0 = 22, r1 = 20:** CMP computes 22 - 20 = 2
- Unsigned: 2 in [0, 63] => no borrow => **C = 1**
- Signed: 2 in [-32, 31] => no overflow => **V = 0**
- **Z = 0**, **N = 0**

**(b) r0 = -20, r1 = -22:** CMP computes -20 - (-22) = 2
- Unsigned: (64-20) - (64-22) = 44 - 42 = 2 in [0, 63] => **C = 1**
- Signed: 2 in [-32, 31] => **V = 0**
- **Z = 0**, **N = 0**

#### Part 2: CCS Verification (both cases have N=0, Z=0, C=1, V=0)

| CCS | Logic Equation | Evaluation | Result |
|-----|----------------|------------|--------|
| GE | V == N | 0 == 0 = true | **true** |
| GT | (V == N) && (Z == 0) | true && true | **true** |
| LT | V != N | 0 != 0 = false | **false** |
| LE | (V != N) \|\| (Z == 1) | false \|\| false | **false** |
| HI | C != Z | 1 != 0 = true | **true** |
| HS | C == 1 | 1 == 1 = true | **true** |
| LS | C == Z | 1 == 0 = false | **false** |
| LO | C == 0 | 1 == 0 = false | **false** |

Both case (a) and case (b) produce identical flags and therefore identical CCS results.

#### Part 3: EQ and NE Logic Equations
- **EQ:** `(Z == 1)`
- **NE:** `(Z == 0)`

**Key CCS reference table:**

| Suffix | Meaning (signed) | Logic |
|--------|-------------------|-------|
| GT | Greater than | (V == N) && (Z == 0) |
| GE | Greater or equal | V == N |
| LT | Less than | V != N |
| LE | Less or equal | (V != N) \|\| (Z == 1) |
| HI | Higher (unsigned >) | C != Z |
| HS | Higher or same (unsigned >=) | C == 1 |
| LS | Lower or same (unsigned <=) | C == Z |
| LO | Lower (unsigned <) | C == 0 |
| EQ | Equal | Z == 1 |
| NE | Not equal | Z == 0 |

---

### Problem 3 (20 pts) -- Conditional Branch: Max Function

**C function:**
```c
int mp_max_ab_i_c(int a, int b) {
    if (a >= b) return a;
    else return b;
}
```

**Assembly solution:**
```asm
@ int mp_max_ab_i_s(int a, int b)
@ Input:  a -> r0, b -> r1
@ Output: r0
mp_max_ab_i_s:
    cmp     r0, r1
    blt     mp_max_ab_i_s_else      @ negative logic: branch if a < b

mp_max_ab_i_s_then:
    b       mp_max_ab_i_s_end_if    @ a >= b, r0 already has a

mp_max_ab_i_s_else:
    mov     r0, r1                  @ return b

mp_max_ab_i_s_end_if:
    bx      lr
```

**Key concept:** Use "negative logic" -- branch on the opposite condition to skip the "then" block. For `a >= b`, the negative logic branch is `blt` (branch if less than).

---

### Problem 4 (30 pts) -- While Loop: 64-bit Sum of Squares

**C function:**
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

**Assembly solution:**
```asm
@ int64_t mp_range_square_sum_standard_while_s(int s, int e)
@ Input:  s -> r0 (reused as i), e -> r1
@ Output: r1:r0 (64-bit return)
@ Others: sum_low_word -> r2, sum_high_word -> r3
mp_range_square_sum_standard_while_s:
    ldr     r2, =0              @ sum_low_word = 0
    ldr     r3, =0              @ sum_high_word = 0

mp_range_square_sum_standard_while_s_loop:
    cmp     r0, r1              @ (i <= e)?
    bgt     mp_range_square_sum_standard_while_s_end_loop

    smlal   r2, r3, r0, r0     @ sum += i*i (signed 32x32->64 multiply-accumulate)
    add     r0, #1              @ i++
    b       mp_range_square_sum_standard_while_s_loop

mp_range_square_sum_standard_while_s_end_loop:
    mov     r0, r2              @ prepare sum_low_word for return
    mov     r1, r3              @ prepare sum_high_word for return
    bx      lr
```

**Key concepts:**
- `smlal` performs signed 32x32 -> 64-bit multiply-accumulate: `{Rhi, Rlo} += Rn * Rm`
- 64-bit return uses R1:R0 (R1 = high word, R0 = low word) per EABI
- Loop variable `i` reuses R0 (the input `s`), saving a register
- Loop condition uses negative logic: `bgt` exits when i > e
