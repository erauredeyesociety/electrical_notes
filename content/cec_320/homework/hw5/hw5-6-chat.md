# CEC 320 — Homework 5/6 Solutions

## Fixed-Point Encoding, Decoding, and Arithmetic

---

# Problem 1 — Encode 2.75 using UQ3.5

### Format Identification

* UQ3.5 → unsigned
* m = 3 integer bits
* n = 5 fractional bits
* N = 8 total bits
* Scaling factor = ( 2^5 = 32 )

### Step-by-Step Encoding

1. **Scale the number**
   ( I = 2.75 \times 2^5 = 2.75 \times 32 = 88 )

2. **Round (if needed)**
   Already an integer → ( I = 88 )

3. **Convert to 8-bit binary**
   ( 88 = 0b0101_1000 )

4. **Convert to hexadecimal**
   ( 0b0101 = 5 ), ( 0b1000 = 8 )

### Final Answer

**0x58**

### Quick Verification

( 88 \times 2^{-5} = 88 / 32 = 2.75 ) ✓

---

# Problem 2 — Decode Q3.4 Codes

### Format Identification

* Q3.4 → signed
* 1 sign bit
* m = 3 integer bits
* n = 4 fractional bits
* N = 8
* Scale factor = ( 2^{-4} = 1/16 )

---

## (a) ( C_1 = 0x77 )

1. **Convert to binary**
   ( 0x77 = 0b0111_0111 )

2. **Determine sign**
   MSB = 0 → positive

3. **Unsigned value**
   ( U = 119 )

4. **Signed integer**
   ( I = 119 )

5. **Scale to real value**
   ( f = 119 \times 1/16 = 7.4375 )

### Final Answer

**7.4375**

---

## (b) ( C_2 = 0xAA )

1. **Convert to binary**
   ( 0xAA = 0b1010_1010 )

2. **Determine sign**
   MSB = 1 → negative

3. **Unsigned value**
   ( U = 170 )

4. **Two’s complement conversion**
   ( I = 170 - 2^8 = 170 - 256 = -86 )

5. **Scale to real value**
   ( f = -86 \times 1/16 = -5.375 )

### Final Answer

**−5.375**

---

# Problem 3 — Decode Q2.5 Code 0b1001_1001

### Format

* Q2.5 → signed
* m = 2
* n = 5
* N = 8
* Scale factor = ( 1/32 )

### Step-by-Step

1. **Unsigned value**
   ( U = 153 )

2. **MSB = 1 → negative**

3. **Convert to signed integer**
   ( I = 153 - 256 = -103 )

4. **Scale to real value**
   ( f = -103 \times 1/32 = -3.21875 )

### Final Answer

**−3.21875**

---

# Problem 4 — Encode into Q3.4 Format

### Format Rules

* Signed
* N = 8
* n = 4
* Scaling factor = 16
* Range: −8.0 to +7.9375

### Encoding Procedure

1. Multiply by ( 2^n )
2. Round
3. If negative → add ( 2^N )
4. Convert to hex

---

## (a) ( f_1 = 0.5 )

1. ( 0.5 \times 16 = 8 )
2. Positive → no TC
3. Hex: **0x08**

---

## (b) ( f_2 = 6.73 )

1. ( 6.73 \times 16 = 107.68 )
2. Round → 108
3. Hex: **0x6C**

Verification:
( 108 / 16 = 6.75 )
Rounding error = 0.02

---

## (c) ( f_3 = -2.25 )

1. ( -2.25 \times 16 = -36 )
2. Add ( 2^8 ): ( -36 + 256 = 220 )
3. Hex: **0xDC**

Verification:
( 220 - 256 = -36 )
( -36 / 16 = -2.25 ) ✓

---

## (d) ( f_4 = -4.5 )

1. ( -4.5 \times 16 = -72 )
2. Add 256 → 184
3. Hex: **0xB8**

Verification:
( 184 - 256 = -72 )
( -72 / 16 = -4.5 ) ✓

---

# Problem 5 — Q15 Multiply-Accumulate

Compute:

[
f_A = f_1 f_2 + f_3 f_4
]

Given:

[
f_1 = 0.5, \quad
f_2 = 0.25, \quad
f_3 = 0.125, \quad
f_4 = 0.0625
]

Expected real result:

[
0.125 + 0.0078125 = 0.1328125
]

---

## Step 1 — Encode in Q15

Q15 → Q0.15

* Signed
* n = 15
* Scale = ( 2^{15} = 32768 )

[
I = f \times 32768
]

| Value   | Real   | Decimal | Hex    |
| ------- | ------ | ------- | ------ |
| ( f_1 ) | 0.5    | 16384   | 0x4000 |
| ( f_2 ) | 0.25   | 8192    | 0x2000 |
| ( f_3 ) | 0.125  | 4096    | 0x1000 |
| ( f_4 ) | 0.0625 | 2048    | 0x0800 |

Shortcut check: all are powers of two ✓

---

## Step 2 — Perform Multiplications

Formula:

[
I_P = (I_A \times I_B) >> 15
]

### Product 1

[
16384 \times 8192 = 2^{14} \times 2^{13} = 2^{27}
]

[
2^{27} >> 15 = 2^{12} = 4096 = 0x1000
]

---

### Product 2

[
4096 \times 2048 = 2^{12} \times 2^{11} = 2^{23}
]

[
2^{23} >> 15 = 2^8 = 256 = 0x0100
]

---

## Step 3 — Add Products

[
4096 + 256 = 4352
]

Hex:

[
4352 = 0x1100
]

---

## Step 4 — Decode Result

[
f_A = 4352 \times 2^{-15}
]

[
f_A = 4352 / 32768 = 0.1328125
]

---

### Final Answer

[
\boxed{f_A = 0.1328125}
]

---

# Final Check

[
0.5 \times 0.25 = 0.125
]
[
0.125 \times 0.0625 = 0.0078125
]
[
\text{Sum} = 0.1328125 ; ✓
]

---

If you'd like, I can also:

• tighten this to reduce page count
• format it in LaTeX submission style
• convert it to a clean PDF-ready layout
• or simplify the wording to match exactly how your professor writes solutions

Just tell me the goal (page limit vs. polish vs. professor style).
