# CEC 320 HW 05
---

## Problem 1

**Format:** UQ3.5 into 3 integer bits, 5 fraction bits, 8 bits total, unsigned

    1. Multiply by 2^n:    2.75 × 2^5 = 2.75 × 32 = 88
    2. Round:               88 (already an integer, no rounding needed)
    3. Convert to hex:      88 = 0x58

**Answer: 0x58**

---

## Problem 2

**Format:** Q3.4 into 1 sign bit + 3 integer bits + 4 fraction bits = 8 bits total (N=8)

### part a): C_1 = 0x77

    1. Unsigned integer:    U_A = 0x77 = 119
    2. Check MSB:           0x77 = 0b0111_0111
                            MSB = 0
                            positive
       So I_A = 119
    3. Scale:               f = 119 × 2^(−4) = 119/16 = 7.4375

**Answer: 7.4375**


### part b): C_2 = 0xAA

    1. Unsigned integer:    U_A = 0xAA = 170
    2. Check MSB:           0xAA = 0b1010_1010
                            MSB = 1
                            negative
       So I_A = 170 − 2^8 = 170 − 256 = −86
    3. Scale:               f = −86 × 2^(−4) = −86/16 = −5.375

**Answer: −5.375**

---

## Problem 3

**Format:** Q2.5 into 1 sign bit + 2 integer bits + 5 fraction bits = 8 bits total (N=8)

    1. Unsigned integer:    U_A = 0b1001_1001 = 0x99 = 153
    2. Check MSB:           MSB = 1
                            negative
       So I_A = 153 − 2^8 = 153 − 256 = −103
    3. Scale:               f = −103 × 2^(−5) = −103/32 = −3.21875

**Answer: −3.21875**

---

## Problem 4

**Format:** Q3.4 into 1 sign bit + 3 integer bits + 4 fraction bits = 8 bits total (N=8)

**Range:** −(2^3) to +(2^3 − 2^(−4)) = −8.0 to +7.9375

**Encoding steps**:

    1. Multiply f × 2^n
    2. Round to nearest integer
    3. If negative: add 2^N for two's complement
    4. Convert to hex


### part a): f_1 = 0.5

    1. Multiply:    0.5 × 2^4 = 8
    2. Round:        8
    3. Positive:     no TC needed
    4. Hex:          8 = 0x08

**Answer: 0x08**


### part b): f_2 = 6.73

    1. Multiply:    6.73 × 2^4 = 107.68
    2. Round:        108 (0.68 ≥ 0.5, round up)
    3. Positive:     no TC needed
    4. Hex:          108 = 0x6C

**Answer: 0x6C**


### Part (c): f_3 = −2.25

    1. Multiply:    −2.25 × 2^4 = −36
    2. Round:        −36
    3. Negative TC:  −36 + 2^8 = −36 + 256 = 220
    4. Hex:          220 = 0xDC

**Answer: 0xDC**


### Part (d): f_4 = −4.5

    1. Multiply:    −4.5 × 2^4 = −72
    2. Round:        −72
    3. Negative TC:  −72 + 2^8 = −72 + 256 = 184
    4. Hex:          184 = 0xB8

**Answer: 0xB8**

---

## Problem 5

Compute f_A = f_1 × f_2 + f_3 × f_4 where:

    f_1 = 0.5,  f_2 = 0.25,  f_3 = 0.125,  f_4 = 0.0625

**Format:** Q15 = Q0.15 into 16-bit signed, n = 15

**Expected result:** 0.5 × 0.25 + 0.125 × 0.0625 = 0.125 + 0.0078125 = 0.1328125


### Step 1: Encode the real numbers in Q15

Formula: I = f × 2^15

    I_1 = 0.5    × 2^15 = 0.5    × 32768 = 16384 = 0x4000
    I_2 = 0.25   × 2^15 = 0.25   × 32768 = 8192  = 0x2000
    I_3 = 0.125  × 2^15 = 0.125  × 32768 = 4096  = 0x1000
    I_4 = 0.0625 × 2^15 = 0.0625 × 32768 = 2048  = 0x0800


### Step 2

Each multiplication is 16-bit × 16-bit into 32-bit, then shift right by 15 to get
back to Q15

**Multiplication 1: I_1 × I_2**

    I_T1 = 16384 × 8192

To compute: 16384 = 2^14, 8192 = 2^13, so I_T1 = 2^27 = 134,217,728

    I_P1 = I_T1 >> 15 = 2^27 >> 15 = 2^12 = 4096 = 0x1000

**Multiplication 2: I_3 × I_4**

    I_T2 = 4096 × 2048

To compute: 4096 = 2^12, 2048 = 2^11, so I_T2 = 2^23 = 8,388,608

    I_P2 = I_T2 >> 15 = 2^23 >> 15 = 2^8 = 256 = 0x0100


### Step 3

    I_A = I_P1 + I_P2
        = 4096 + 256
        = 4352
        = 0x1100

This is straightforward Q15 addition: just add the encoded integers directly.


### Step 4

    f_A = I_A × 2^(−15)
        = 4352 × 2^(−15)
        = 4352 / 32768
        = 0.1328125

**Answer: f_A = 0.1328125**
