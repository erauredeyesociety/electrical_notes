# CEC 320 — Homework 5/6 Solutions

## Real Numbers: Fixed-Point Encoding, Decoding, and Arithmetic

---

## Problem 1 — Encode 2.75 using UQ3.5 (8 pts)

**Format:** UQ3.5 → 3 integer bits, 5 fraction bits, 8 bits total, unsigned

**Encoding steps** (reversed integer approach from Lctr 13 §13.3.1.5):

    1. Multiply by 2^n:    2.75 × 2^5 = 2.75 × 32 = 88
    2. Round:               88 (already an integer, no rounding needed)
    3. Convert to hex:      88 = 0x58

**Verify by decoding:** 0x58 = 88, then 88 × 2^(−5) = 88/32 = 2.75 ✓

**Answer: 0x58**

---

## Problem 2 — Decode Q3.4 codes to real numbers (16 pts)

**Format:** Q3.4 → 1 sign bit + 3 integer bits + 4 fraction bits = 8 bits total (N=8)

**Method:** Integer TC approach (Lctr 13 §13.3.2.1)


### Part (a): C₁ = 0x77

    1. Unsigned integer:    U_A = 0x77 = 119
    2. Check MSB:           0x77 = 0b0111_0111 → MSB = 0 → positive
       So I_A = 119
    3. Scale:               f = 119 × 2^(−4) = 119/16 = 7.4375

**Answer: 7.4375**


### Part (b): C₂ = 0xAA

    1. Unsigned integer:    U_A = 0xAA = 170
    2. Check MSB:           0xAA = 0b1010_1010 → MSB = 1 → negative
       So I_A = 170 − 2^8 = 170 − 256 = −86
    3. Scale:               f = −86 × 2^(−4) = −86/16 = −5.375

**Answer: −5.375**

---

## Problem 3 — Decode Q2.5 code 0b1001_1001 (10 pts)

**Format:** Q2.5 → 1 sign bit + 2 integer bits + 5 fraction bits = 8 bits total (N=8)

    1. Unsigned integer:    U_A = 0b1001_1001 = 0x99 = 153
    2. Check MSB:           MSB = 1 → negative
       So I_A = 153 − 2^8 = 153 − 256 = −103
    3. Scale:               f = −103 × 2^(−5) = −103/32 = −3.21875

**Answer: −3.21875**

---

## Problem 4 — Encode real numbers into Q3.4 format (32 pts)

**Format:** Q3.4 → 1 sign bit + 3 integer bits + 4 fraction bits = 8 bits total (N=8)

**Range:** −(2^3) to +(2^3 − 2^(−4)) = −8.0 to +7.9375

**Encoding steps** (Lctr 13 §13.3.2.3):
1. Multiply f × 2^n
2. Round to nearest integer
3. If negative: add 2^N for two's complement
4. Convert to hex


### Part (a): f₁ = 0.5

    1. Multiply:    0.5 × 2^4 = 8
    2. Round:        8
    3. Positive:     no TC needed
    4. Hex:          8 = 0x08

**Answer: 0x08**


### Part (b): f₂ = 6.73

    1. Multiply:    6.73 × 2^4 = 107.68
    2. Round:        108 (0.68 ≥ 0.5, round up)
    3. Positive:     no TC needed
    4. Hex:          108 = 0x6C

**Verify:** 0x6C = 108, then 108 × 2^(−4) = 108/16 = 6.75
(Rounding error: |6.75 − 6.73| = 0.02)

**Answer: 0x6C**


### Part (c): f₃ = −2.25

    1. Multiply:    −2.25 × 2^4 = −36
    2. Round:        −36
    3. Negative TC:  −36 + 2^8 = −36 + 256 = 220
    4. Hex:          220 = 0xDC

**Verify:** 0xDC = 220, MSB=1 → I = 220 − 256 = −36, then −36/16 = −2.25 ✓

**Answer: 0xDC**


### Part (d): f₄ = −4.5

    1. Multiply:    −4.5 × 2^4 = −72
    2. Round:        −72
    3. Negative TC:  −72 + 2^8 = −72 + 256 = 184
    4. Hex:          184 = 0xB8

**Verify:** 0xB8 = 184, MSB=1 → I = 184 − 256 = −72, then −72/16 = −4.5 ✓

**Answer: 0xB8**

---

## Problem 5 — Q15 Multiply-Accumulate (44 pts)

Compute f_A = f₁ × f₂ + f₃ × f₄ where:

    f₁ = 0.5,  f₂ = 0.25,  f₃ = 0.125,  f₄ = 0.0625

**Format:** Q15 = Q0.15 → 16-bit signed, n = 15

**Expected result:** 0.5 × 0.25 + 0.125 × 0.0625 = 0.125 + 0.0078125 = 0.1328125


### Step 1 — Encode the real numbers in Q15 (16 pts)

Formula: I = f × 2^15

    I₁ = 0.5    × 2^15 = 0.5    × 32768 = 16384 = 0x4000
    I₂ = 0.25   × 2^15 = 0.25   × 32768 = 8192  = 0x2000
    I₃ = 0.125  × 2^15 = 0.125  × 32768 = 4096  = 0x1000
    I₄ = 0.0625 × 2^15 = 0.0625 × 32768 = 2048  = 0x0800

**Quick shortcut check:**
- 0.5 = 2^(−1), so I = 2^(−1) × 2^15 = 2^14 = 16384 = 0x4000 ✓
- 0.25 = 2^(−2), so I = 2^13 = 8192 = 0x2000 ✓
- 0.125 = 2^(−3), so I = 2^12 = 4096 = 0x1000 ✓
- 0.0625 = 2^(−4), so I = 2^11 = 2048 = 0x0800 ✓


### Step 2 — Perform multiplications (16 pts)

Each multiplication is 16-bit × 16-bit → 32-bit, then shift right by 15 to get
back to Q15 (Lctr 13 §13.4.2).

**Multiplication 1: I₁ × I₂**

    I_T1 = 16384 × 8192

To compute: 16384 = 2^14, 8192 = 2^13, so I_T1 = 2^27 = 134,217,728

    I_P1 = I_T1 >> 15 = 2^27 >> 15 = 2^12 = 4096 = 0x1000

**Multiplication 2: I₃ × I₄**

    I_T2 = 4096 × 2048

To compute: 4096 = 2^12, 2048 = 2^11, so I_T2 = 2^23 = 8,388,608

    I_P2 = I_T2 >> 15 = 2^23 >> 15 = 2^8 = 256 = 0x0100


### Step 3 — Add the two products (6 pts)

    I_A = I_P1 + I_P2
        = 4096 + 256
        = 4352
        = 0x1100

This is straightforward Q15 addition — just add the encoded integers directly.


### Step 4 — Decode I_A to obtain f_A (6 pts)

    f_A = I_A × 2^(−15)
        = 4352 × 2^(−15)
        = 4352 / 32768
        = 0.1328125

**Verify against expected:**

    0.5 × 0.25     = 0.125
    0.125 × 0.0625 = 0.0078125
    Sum             = 0.1328125 ✓

**Answer: f_A = 0.1328125**


### Problem 5 Summary Table

| Value | Real Number | Q15 Encoded (decimal) | Q15 Encoded (hex) |
|-------|-------------|----------------------|-------------------|
| f₁ | 0.5 | 16384 | 0x4000 |
| f₂ | 0.25 | 8192 | 0x2000 |
| f₃ | 0.125 | 4096 | 0x1000 |
| f₄ | 0.0625 | 2048 | 0x0800 |
| I_P1 = f₁×f₂ | 0.125 | 4096 | 0x1000 |
| I_P2 = f₃×f₄ | 0.0078125 | 256 | 0x0100 |
| I_A = sum | 0.1328125 | 4352 | 0x1100 |