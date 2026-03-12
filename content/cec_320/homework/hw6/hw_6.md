## Problem 1

**Given:**
- R_i has value (1 << i) + (1 << 2i) for i = 1, 2, ..., 12
- SP = 0x2000_1020 before the push
- Full descending stack
- Instruction: `PUSH {r7, r5, r8, r6}`

---

### P1.1

Count the registers being pushed.

    PUSH {r7, r5, r8, r6} so 4 registers

Each register is 32 bits = 4 bytes.

    Total bytes = 4 registers × 4 bytes = 16 bytes = 0x10

Full descending stack so SP decreases.

    SP_after = SP_before - 16
             = 0x2000_1020 - 0x10
             = 0x2000_1010

**Answer: SP = 0x2000_1010**

---

### P1.2

Apply the formula with i = 5.

    R5 = (1 << 5) + (1 << 2×5)
       = (1 << 5) + (1 << 10)

Compute each term.

    1 << 5  = 32    = 0x0000_0020
    1 << 10 = 1024  = 0x0000_0400

Add them.

    R5 = 32 + 1024 = 1056

Convert to hex.

    1056 = 4×256 + 2×16 + 0 = 0x0000_0420


**Answer: R5 = 0x0000_0420**

---

### P1.3

Determine the storage order.

    PUSH {r7, r5, r8, r6}

hardware ignores the listed order and stores registers sorted by register number, lowest number at lowest address:

    Address         Register
    0x2000_1010     R5          lowest register number so lowest address
    0x2000_1014     R6          next register number
    0x2000_1018     R7          next
    0x2000_101C     R8          highest register number so highest address

So address 0x2000_1014 contains R6.

Compute R6 using the formula with i = 6.

    R6 = (1 << 6) + (1 << 12)
       = 64 + 4096
       = 4160

Convert to hex.

    4096 = 0x1000
    64   = 0x0040
    R6   = 0x1000 + 0x0040 = 0x0000_1040

**Answer: The word at 0x2000_1014 is 0x0000_1040 (value of R6)**

---

### P1.4

We just found that the 32-bit word at 0x2000_1014 is 0x0000_1040.

ARM is little-endian, so bytes are stored least significant first:

    Address         Byte
    0x2000_1014     0x40    (least significant byte)
    0x2000_1015     0x10
    0x2000_1016     0x00
    0x2000_1017     0x00    (most significant byte)

The byte at 0x2000_1014 is the LSB of 0x1040.

    0x1040 & 0xFF = 0x40

**Answer: 0x40**

---

---

## Problem 2

**Given:**

    uint8_t var1 = 0xF;      // = 15 decimal
    uint8_t var2 = 0xFF;     // = 255 decimal
    Call: fn1(var1, var2, 0xFFF, 0xFFFF);
    Prototype: void fn1(uint32_t x, uint32_t y, uint32_t z, uint32_t w);

The function takes uint32_t parameters, so all arguments are promoted to 32 bits.
Since all source types are unsigned (uint8_t) or unsigned integer literals,
the promotion is **zero extension** so fill upper bits with 0.

---

### R0 = first argument (var1)

    var1 = 0xF (uint8_t)
    Zero-extend to 32 bits: pad upper 24 bits with 0s

**R0 = 0x0000_000F**

### R1 = second argument (var2)

    var2 = 0xFF (uint8_t)
    Zero-extend to 32 bits: pad upper 24 bits with 0s

**R1 = 0x0000_00FF**

### R2 = third argument (0xFFF)

    0xFFF is an integer literal, already fits in 32 bits
    Zero-extend (it's already a positive int): pad upper 20 bits with 0s

**R2 = 0x0000_0FFF**

### R3 = fourth argument (0xFFFF)

    0xFFFF is an integer literal, already fits in 32 bits
    Zero-extend: pad upper 16 bits with 0s

**R3 = 0x0000_FFFF**

---

**Answers:**

    R0 = 0x0000_000F
    R1 = 0x0000_00FF
    R2 = 0x0000_0FFF
    R3 = 0x0000_FFFF

---

---

## Problem 3

**Given:**

    int8_t var1 = 0xF;       // int8_t, 0xF = 15 decimal (positive, MSB=0)
    int8_t var2 = 0xFF;      // int8_t, 0xFF = -1 decimal (MSB=1, two's complement)
    Call: fn2(var1, var2);
    Prototype: void fn2(int32_t x, int32_t y);

The function takes int32_t parameters, so signed arguments are promoted using
**sign extension** so the MSB (sign bit) is replicated across bits 8–31.

---

### R0 = first argument (var1)

    var1 = 0xF as int8_t
    Binary: 0b0000_1111
    MSB (bit 7) = 0 so positive
    Sign-extend: fill bits 31:8 with 0

**R0 = 0x0000_000F**

### R1 = second argument (var2)

    var2 = 0xFF as int8_t
    Binary: 0b1111_1111
    MSB (bit 7) = 1 so negative (this is -1 in two's complement)
    Sign-extend: fill bits 31:8 with 1

    Bits 31:8 all become 1: 0xFFFFFF
    Combined with bottom byte 0xFF:

**R1 = 0xFFFF_FFFF**

Verification: 0xFFFF_FFFF as int32_t = -1, and 0xFF as int8_t = -1. Value preserved.

---

**Answers:**

    R0 = 0x0000_000F
    R1 = 0xFFFF_FFFF

---

---

## Problem 4

**Given:**
- ASM function returns in Q15.16 format
- The real number returned is 3.25

---

### P4a

Decode Format Q15.16.

    - 1 sign bit
    - 15 integer bits
    - 16 fractional bits
    - Total: 1 + 15 + 16 = 32 bits
    - n = 16 (number of fractional bits)

Encode using the standard formula.

    I = f × 2^n
    I = 3.25 × 2^16
    I = 3.25 × 65536

Compute the multiplication.

    3 × 65536 = 196608
    0.25 × 65536 = 16384
    Total: 196608 + 16384 = 212992

Convert to hexadecimal.

    212992 / 65536 = 3 remainder 16384
    3 in hex = 0x3
    16384 = 0x4000

    So 212992 = 0x0003_4000

    Alternatively: 3.25 = 3 + 1/4
    Integer part 3 so shifted left by 16 bits so 3 << 16 = 0x0003_0000
    Fractional part 0.25 = 1/4 so 0.25 × 65536 = 16384 = 0x4000
    Sum: 0x0003_0000 + 0x4000 = 0x0003_4000

**Answer: The encoded value is 0x0003_4000**

### P4b

    EABI convention: 32-bit return values go in R0

**Answer: R0**

---

---

## Problem 5

**Given function:**

    mp_add_64bit_s:
        adds r0, r2       @ R0 = R0 + R2 (low word), updates C flag
        adc  r1, r3       @ R1 = R1 + R3 + C (high word)
        bx   lr

**Convention:** For 64-bit values, R0:R1 = first operand (R0=low, R1=high),
R2:R3 = second operand (R2=low, R3=high).

**Given test cases:**

    int64_t A1 = (int64_t)0x388 << 24,  B1 = (int64_t)0x289 << 24;
    int64_t A2 = (int64_t)0x378 << 24,  B2 = (int64_t)0x279 << 24;

---

### Step 1: Compute A1, B1, A2, B2 as 64-bit hex values

**A1 = 0x388 << 24:**

    0x388 = 904 decimal
    0x388 << 24: shift left by 24 bits = shift left by 6 hex digits

    0x388 in binary has 10 bits (0b11_1000_1000)
    Shifting left by 24: the result needs 10 + 24 = 34 bits so requires 64-bit

    0x388 << 24 = 0x0000_0003_8800_0000

    Breakdown: 0x388 × 0x100_0000 (= 2^24)
    0x388 × 0x1000000:
        0x300 × 0x1000000 = 0x3_0000_0000
        0x088 × 0x1000000 = 0x0_8800_0000
        Sum = 0x3_8800_0000 = 0x0000_0003_8800_0000

**B1 = 0x289 << 24:**

    Same method:
    0x289 × 0x1000000:
        0x200 × 0x1000000 = 0x2_0000_0000
        0x089 × 0x1000000 = 0x0_8900_0000
        Sum = 0x2_8900_0000 = 0x0000_0002_8900_0000

**A2 = 0x378 << 24:**

    0x378 × 0x1000000:
        0x300 × 0x1000000 = 0x3_0000_0000
        0x078 × 0x1000000 = 0x0_7800_0000
        Sum = 0x3_7800_0000 = 0x0000_0003_7800_0000

**B2 = 0x279 << 24:**

    0x279 × 0x1000000:
        0x200 × 0x1000000 = 0x2_0000_0000
        0x079 × 0x1000000 = 0x0_7900_0000
        Sum = 0x2_7900_0000 = 0x0000_0002_7900_0000

---

### Step 2: Split into register pairs (low word, high word)

    A1 = 0x0000_0003_8800_0000
         R1 (high) = 0x0000_0003
         R0 (low)  = 0x8800_0000

    B1 = 0x0000_0002_8900_0000
         R3 (high) = 0x0000_0002
         R2 (low)  = 0x8900_0000

    A2 = 0x0000_0003_7800_0000
         R1 (high) = 0x0000_0003
         R0 (low)  = 0x7800_0000

    B2 = 0x0000_0002_7900_0000
         R3 (high) = 0x0000_0002
         R2 (low)  = 0x7900_0000

---

### Step 3: Perform A1 + B1

**Low word addition (ADDS R0, R2):**

    R0 + R2 = 0x8800_0000 + 0x8900_0000

      0x8800_0000
    + 0x8900_0000
      0x1_1100_0000   this is 33 bits

    The result overflows 32 bits.
    Low word result: 0x1100_0000 (bottom 32 bits)
    Carry flag C = 1 (overflow from bit 31)

**High word addition (ADC R1, R3):**

    R1 + R3 + C = 0x0000_0003 + 0x0000_0002 + 1 = 0x0000_0006

**Full 64-bit result: A1 + B1**

    High:Low = 0x0000_0006 : 0x1100_0000
    = 0x0000_0006_1100_0000

**In C format:**

    int64_t C1 = (int64_t)0x611 << 24;

---

### Step 4: Perform A2 + B2

**Low word addition (ADDS R0, R2):**

    R0 + R2 = 0x7800_0000 + 0x7900_0000

     0x7800_0000
    + 0x7900_0000
     0x0_F100_0000   this is 32 bits, fits

    Low word result: 0xF100_0000
    Carry flag C = 0 (no overflow from bit 31)

**High word addition (ADC R1, R3):**

    R1 + R3 + C = 0x0000_0003 + 0x0000_0002 + 0 = 0x0000_0005

**Full 64-bit result: A2 + B2**

    High:Low = 0x0000_0005 : 0xF100_0000
    = 0x0000_0005_F100_0000

**In C format:**

    int64_t C2 = (int64_t)0x5F1 << 24;

---

### P5.1 Answers (values in C format):

    int64_t C1 = (int64_t)0x611 << 24;    // A1 + B1
    int64_t C2 = (int64_t)0x5F1 << 24;    // A2 + B2

### P5.2 Answers (C flag values):

    A1 + B1: C flag = 1   (low word 0x88000000 + 0x89000000 overflows 32 bits)
    A2 + B2: C flag = 0   (low word 0x78000000 + 0x79000000 = 0xF1000000, fits)

---

---

## Problem 6

**Given function:**

    mp_sub_64bit_s:
        subs r0, r2       @ R0 = R0 - R2 (low word), updates C flag
        sbc  r1, r3       @ R1 = R1 - R3 - !C (high word, subtract borrow)
        bx   lr

**Important:** In ARM, for subtraction, the C flag is the INVERSE of borrow:
- C = 1 means NO borrow occurred (result >= 0 for unsigned)
- C = 0 means borrow occurred (result < 0 for unsigned)

**Given test cases:**

    int64_t A1 = (int64_t)0x387 << 28,  B1 = (int64_t)0x28 << 28;
    int64_t A2 = (int64_t)0x388 << 28,  B2 = (int64_t)0x288 << 28;

---

### Step 1: Compute values as 64-bit hex

**A1 = 0x387 << 28:**

    0x387 << 28: shift left by 28 bits = 7 hex digits

    0x387 × 0x1000_0000:
        0x300 × 0x1000_0000 = 0x30_0000_0000
        0x087 × 0x1000_0000 = 0x08_7000_0000
        Sum = 0x38_7000_0000 = 0x0000_0038_7000_0000

**B1 = 0x28 << 28:**

    0x28 × 0x1000_0000 = 0x2_8000_0000
    = 0x0000_0002_8000_0000

**A2 = 0x388 << 28:**

    0x388 × 0x1000_0000:
        0x300 × 0x1000_0000 = 0x30_0000_0000
        0x088 × 0x1000_0000 = 0x08_8000_0000
        Sum = 0x38_8000_0000 = 0x0000_0038_8000_0000

**B2 = 0x288 << 28:**

    0x288 × 0x1000_0000:
        0x200 × 0x1000_0000 = 0x20_0000_0000
        0x088 × 0x1000_0000 = 0x08_8000_0000
        Sum = 0x28_8000_0000 = 0x0000_0028_8000_0000

---

### Step 2: Split into register pairs

    A1 = 0x0000_0038_7000_0000
         R1 = 0x0000_0038,  R0 = 0x7000_0000

    B1 = 0x0000_0002_8000_0000
         R3 = 0x0000_0002,  R2 = 0x8000_0000

    A2 = 0x0000_0038_8000_0000
         R1 = 0x0000_0038,  R0 = 0x8000_0000

    B2 = 0x0000_0028_8000_0000
         R3 = 0x0000_0028,  R2 = 0x8000_0000

---

### Step 3: Perform A1 - B1

**Low word subtraction (SUBS R0, R2):**

    R0 - R2 = 0x7000_0000 - 0x8000_0000

    0x7000_0000 < 0x8000_0000 so unsigned underflow (borrow needed)

    Compute: 0x7000_0000 - 0x8000_0000
    = 0x1_7000_0000 - 0x8000_0000    (borrow 1 from next word = add 0x1_0000_0000)
    = 0xF000_0000

    Low word result: 0xF000_0000
    C flag = 0 (borrow occurred so ARM sets C = 0 for borrow)

**High word subtraction (SBC R1, R3):**

    SBC computes: R1 - R3 - !C = R1 - R3 - (1 - C)
    C = 0, so !C = 1

    R1 - R3 - 1 = 0x0000_0038 - 0x0000_0002 - 1
                 = 0x38 - 0x02 - 1
                 = 0x35
                 = 0x0000_0035

**Full 64-bit result: A1 - B1**

    High:Low = 0x0000_0035 : 0xF000_0000
    = 0x0000_0035_F000_0000

**In C format:**

    int64_t D1 = (int64_t)0x35F << 28;


---

### Step 4: Perform A2 - B2

**Low word subtraction (SUBS R0, R2):**

    R0 - R2 = 0x8000_0000 - 0x8000_0000 = 0x0000_0000

    Equal values so no borrow needed
    Low word result: 0x0000_0000
    C flag = 1 (no borrow so ARM sets C = 1)

**High word subtraction (SBC R1, R3):**

    C = 1, so !C = 0

    R1 - R3 - 0 = 0x0000_0038 - 0x0000_0028
                 = 0x10
                 = 0x0000_0010

**Full 64-bit result: A2 - B2**

    High:Low = 0x0000_0010 : 0x0000_0000
    = 0x0000_0010_0000_0000

**In C format:**

    int64_t D2 = (int64_t)0x100 << 28;


---

### P6.1 Answers (values in C format):

    int64_t D1 = (int64_t)0x35F << 28;    // A1 - B1
    int64_t D2 = (int64_t)0x100 << 28;    // A2 - B2

### P6.2 Answers (C flag values):

    A1 - B1: C flag = 0   (0x70000000 - 0x80000000 requires borrow so C = 0)
    A2 - B2: C flag = 1   (0x80000000 - 0x80000000 = 0, no borrow so C = 1)

---

---

## Problem 7

**Goal:** Implement `A % B = A - (A/B) * B` in ARM assembly.

**Function signature:**

    uint32_t umod32bit_s(uint32_t A, uint32_t B)

**Inputs:** R0 = A, R1 = B
**Output:** R0 = A % B

Compute A / B (unsigned integer division).

    UDIV R2, R0, R1      @ R2 = A / B (quotient, truncated toward zero)

    We use R2 as a scratch register (it's caller-saved, safe to use).

Compute (A / B) * B.

    MUL R2, R2, R1       @ R2 = (A / B) * B

    This gives us the largest multiple of B that is ≤ A.

Compute A - (A/B)*B.

    SUB R0, R0, R2        @ R0 = A - (A/B)*B = A % B

    Result goes in R0, which is the return register per EABI.

Return.

    BX LR                 @ return to caller

---

### Complete assembly function:

    @ 32-bit unsigned modulo operation: A % B
    @ uint32_t umod32bit_s(uint32_t A, uint32_t B)
    @ Input:  R0 = A, R1 = B
    @ Output: R0 = A % B

    .global umod32bit_s
    .thumb_func

    umod32bit_s:
        UDIV R2, R0, R1       @ R2 = A / B
        MUL  R2, R2, R1       @ R2 = (A/B) * B
        SUB  R0, R0, R2       @ R0 = A - (A/B)*B = A mod B
        BX   LR               @ return

---

### example: A = 17, B = 5

    R0 = 17, R1 = 5

    UDIV R2, R0, R1   so R2 = 17 / 5 = 3 (integer division, truncated)
    MUL  R2, R2, R1   so R2 = 3 * 5 = 15
    SUB  R0, R0, R2   so R0 = 17 - 15 = 2

    Result: 17 % 5 = 2


---

### Notes on this function:

- This is a **leaf function** (it doesn't call any other functions)
- So we don't need to save LR
- We only use R0, R1, R2 
  - all caller-saved, so no PUSH/POP needed
- The function is 4 instructions, very efficient