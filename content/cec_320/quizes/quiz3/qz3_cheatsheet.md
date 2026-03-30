# CEC 320 — Quiz 3 Cheatsheet

## HWs 6, 7, 8 | Lectures 14–18

---

## 1. EABI Calling Convention (Lctr 14)

**Arguments:** First 4 args → R0, R1, R2, R3. Additional args → stack.

**Return values:**
- 32-bit → R0
- 64-bit → R0 (low word), R1 (high word)

**Register preservation:**
- Caller-saved (scratch): R0–R3, R12, LR
- Callee-saved (must PUSH/POP): R4–R11

**Type promotion to 32-bit:**
- Unsigned (`uint8_t`, `uint16_t`) → **zero-extend** (pad upper bits with 0)
- Signed (`int8_t`, `int16_t`) → **sign-extend** (replicate MSB)

> **HW6 P2:** `uint8_t var1=0xF, var2=0xFF;` called as `fn1(var1, var2, 0xFFF, 0xFFFF)` with `uint32_t` params.
> → R0=0x0000_000F, R1=0x0000_00FF, R2=0x0000_0FFF, R3=0x0000_FFFF (zero-extended)

> **HW6 P3:** `int8_t var1=0xF, var2=0xFF;` called as `fn2(var1, var2)` with `int32_t` params.
> → R0=0x0000_000F (0xF as int8_t = +15, MSB=0, sign-extend with 0s)
> → R1=0xFFFF_FFFF (0xFF as int8_t = -1, MSB=1, sign-extend with 1s)


---

## 2. Stack Operations — Full Descending (Lctr 14)

**PUSH:** SP decrements first, then stores. Each register = 4 bytes.

    PUSH {r7, r5, r8, r6}    @ 4 regs × 4 bytes = 16 (0x10) bytes
                               @ SP_after = SP_before - 0x10

**Storage order:** Always sorted by register number, regardless of listed order.
Lowest register number → lowest address.

    PUSH {r7, r5, r8, r6} with SP_before = 0x2000_1020:
    0x2000_1010 → R5    (lowest reg#, lowest addr)
    0x2000_1014 → R6
    0x2000_1018 → R7
    0x2000_101C → R8    (highest reg#, highest addr)

**Little-endian byte order:** LSB at lowest address.

> **HW6 P1:** R6 = 0x0000_1040 stored at 0x2000_1014.
> → Byte at 0x2000_1014 = **0x40** (LSB), byte at 0x2000_1015 = **0x10**

**Leaf vs. Stem functions:**
- Leaf (no function calls): use `bx lr` to return
- Stem (calls other functions): must `push {lr}` on entry, `pop {pc}` on return


---

## 3. Arithmetic Instructions (Lctr 15)

**Basic:**

    ADD  Rd, Rn, Op2     @ Rd = Rn + Op2
    SUB  Rd, Rn, Op2     @ Rd = Rn - Op2
    RSB  Rd, Rn, Op2     @ Rd = Op2 - Rn  (Reverse Subtract)
    MUL  Rd, Rn, Rm      @ Rd = Rn × Rm   (low 32 bits only)
    UDIV Rd, Rn, Rm      @ Rd = Rn / Rm   (unsigned, truncated)
    SDIV Rd, Rn, Rm      @ Rd = Rn / Rm   (signed, truncated)

**64-bit multiply:**

    SMULL RdLo, RdHi, Rn, Rm    @ [RdHi:RdLo] = Rn × Rm (signed)
    UMULL RdLo, RdHi, Rn, Rm    @ [RdHi:RdLo] = Rn × Rm (unsigned)
    SMLAL RdLo, RdHi, Rn, Rm    @ [RdHi:RdLo] += Rn × Rm (signed multiply-accumulate)

**64-bit addition (ADDS/ADC):**

    adds r0, r2       @ low:  R0 = R0 + R2, sets C flag
    adc  r1, r3       @ high: R1 = R1 + R3 + C

**64-bit subtraction (SUBS/SBC):**

    subs r0, r2       @ low:  R0 = R0 - R2, sets C flag
    sbc  r1, r3       @ high: R1 = R1 - R3 - !C

**C flag in subtraction:** C = NOT borrow. C=1 means NO borrow. C=0 means borrow occurred.

> **HW6 P5:** A1+B1: low words 0x8800_0000 + 0x8900_0000 = 0x1_1100_0000 → overflows 32 bits → **C=1**
> → High: 0x3 + 0x2 + 1 = 0x6 → Result = 0x0000_0006_1100_0000

> **HW6 P6:** A1-B1: low words 0x7000_0000 - 0x8000_0000 → borrow → **C=0**
> → High: 0x38 - 0x02 - 1 = 0x35 → Result = 0x0000_0035_F000_0000

**Modulo (no MOD instruction):** A % B = A - (A/B) * B

> **HW6 P7 (using MUL+SUB):**
>
>     udiv r2, r0, r1       @ r2 = A / B
>     mul  r2, r2, r1       @ r2 = (A/B) * B
>     sub  r0, r0, r2       @ r0 = A - (A/B)*B = A % B
>     bx   lr
>
> **Equivalent using MLS (from Lctr 15 — one fewer instruction):**
>
>     udiv r2, r0, r1       @ r2 = A / B
>     mls  r0, r1, r2, r0   @ r0 = r0 - r1*r2 = A - B*(A/B) = A % B
>     bx   lr


---

## 4. Q-Format Fixed-Point (Lctr 14–15)

**Encode:** I = f × 2^n (where n = fractional bits)

**Decode:** f = I × 2^(-n)

> **HW6 P4:** Encode 3.25 in Q15.16:
> → I = 3.25 × 2^16 = 3.25 × 65536 = 213,504 = **0x0003_4000**
> → Return register: **R0** (per EABI)

**Q-format multiplication:** I_C = (I_A × I_B) >> n

**Q31 multiply in ASM:** Extract bits b62–b31 (shift right by 31)

    smull r1, r0, r0, r1    @ [r0:r1] = 64-bit product (r0=HW, r1=LW)
    lsl   r0, #1             @ HW << 1 gets bits b62:b32
    add   r0, r0, r1, lsr #31  @ OR in b31 from LW

**Q15.16 multiply in ASM:** Extract bits b47–b16 (shift right by 16)

    smull r1, r0, r0, r1    @ [r0:r1] = 64-bit product
    lsl   r0, #16            @ HW << 16 gets bits b47:b32
    add   r0, r0, r1, lsr #16  @ OR in bits b31:b16 from LW

> **HW7 P1:** The shift amounts come from the format: right-shift of LW = n (fractional bits), left-shift of HW = 32 - n.


---

## 5. Shift Instructions (Lctr 16)

    LSL Rd, Rn, #imm     @ Logical Shift Left:  Rd = Rn << imm  (multiply by 2^n)
    LSR Rd, Rn, #imm     @ Logical Shift Right: Rd = Rn >> imm  (unsigned divide by 2^n)
    ASR Rd, Rn, #imm     @ Arithmetic Shift Right: preserves sign bit (signed divide by 2^n)
    ROR Rd, Rn, #imm     @ Rotate Right: bits wrap around

**S suffix updates flags:** `LSLS`, `LSRS`, `ASRS`

**C flag = last bit shifted out:**
- `LSLS Rd, Rn, #k` → C = bit (32-k) of Rn
- `LSRS Rd, Rn, #k` → C = bit (k-1) of Rn

> **HW7 P2:** R0 = 0x000000DD = 0b1101_1101
> → `LSLS r1, r0, #1`: R1 = 0x000001BA, C = bit 31 of R0 = **0**
> → `LSRS r2, r0, #3`: R2 = 0x0000001B, C = bit 2 of R0 = **1**
> → Final C flag = **1** (reflects last flag-setting instruction)


---

## 6. Barrel Shifter and Op2 (Lctr 16)

The **Flexible Second Operand (Op2)** can be `Rm, shift #imm` — allows shift + arithmetic in ONE instruction.

| Expression | Decomposition | Instruction |
|---|---|---|
| A = 16B | 2^4 × B | `lsl r0, r1, #4` |
| A = 17B | (1 + 2^4) × B | `add r0, r1, r1, lsl #4` |
| A = 15B | (2^4 - 1) × B | `rsb r0, r1, r1, lsl #4` |
| A = B/16 | 2^(-4) × B | `asr r0, r1, #4` |
| A = 17B/16 | (1 + 2^(-4)) × B | `add r0, r1, r1, asr #4` |
| A = 15B/16 | (1 - 2^(-4)) × B | `sub r0, r1, r1, asr #4` |

**Key rules:**
- Use **ASR** (not LSR) for signed division to preserve sign bit
- **RSB** (Reverse Subtract) computes `Op2 - Rn`, needed for (2^n - 1) × B patterns
- Barrel shifter costs **zero extra clock cycles**


---

## 7. Bitwise Logic Instructions (Lctr 17)

    AND Rd, Rn, Op2     @ Rd = Rn AND Op2    (extract/test bits)
    ORR Rd, Rn, Op2     @ Rd = Rn OR Op2     (set bits)
    EOR Rd, Rn, Op2     @ Rd = Rn XOR Op2    (toggle bits)
    BIC Rd, Rn, Op2     @ Rd = Rn AND NOT(Op2)  (clear bits)
    ORN Rd, Rn, Op2     @ Rd = Rn OR NOT(Op2)
    MVN Rd, Op2         @ Rd = NOT(Op2)

**Bit-field instructions:**

    BFC Rd, #lsb, #width     @ Bit Field Clear: clear width bits starting at lsb
    BFI Rd, Rn, #lsb, #width @ Bit Field Insert: insert width bits from Rn into Rd

**Two-step field assignment pattern** (clear then set):

    bic r0, r0, #0xF0       @ clear bits [7:4]  (digit H1)
    orr r0, r0, #0x50       @ set bits [7:4] to 5

    @ In C: a = (a & ~(0xF << 4)) | (0x5 << 4);

> **HW7 P4:** `bic r0, r0, r1, lsl #4` then `orr r0, r0, r2, lsl #4`
> → Replaces hex digit H1: 0xH3H2**H1**H0 → 0xH3H2**A**H0

> **HW7 P5:** R0=0xAD, R1=0x03
> → `bic r3, r0, r1` = 0xAD AND NOT(0x03) = 0xAD AND 0xFC = **0xAC**
> → `orr r4, r3, r1` = 0xAC OR 0x03 = **0xAF**
> → `eor r5, r0, r1` = 0xAD XOR 0x03 = **0xAE**

**Hex digit manipulation patterns:**

| Transformation | C Code | ASM |
|---|---|---|
| Replace H1 with 5 | `(A & 0xFF0F) \| 0x0050` | `bic r0, #0xF0` then `orr r0, #0x50` |
| Shift left, insert 3 | `(A << 4) \| 0x3` | `lsl r0, #4` then `orr r0, #3` |
| Shift right, insert 7 | `(A >> 4) \| 0x7000` | `lsr r0, #4` then `orr r0, r1` (r1=0x7000) |


---

## 8. Status Flags — NZCV (Lctr 18)

**Flags only update with S suffix** (`ADDS`, `SUBS`, `CMP`, `LSLS`, etc.)

| Flag | Name | Set when |
|---|---|---|
| **N** | Negative | MSB of result = 1 |
| **Z** | Zero | Result = 0 |
| **C** | Carry | Unsigned overflow (ADD) or no borrow (SUB) |
| **V** | Overflow | Signed overflow (result outside signed range) |

**Computing NZCV for N-bit system:**
1. Compute u_temp (unsigned interpretation) and s_temp (signed interpretation)
2. C=1 if u_temp > U_MAX (addition) or u_temp < 0 gives C=0 (subtraction, ARM inverts)
3. V=1 if s_temp > S_MAX or s_temp < S_MIN
4. Correct result: wrap by adding/subtracting C_N = 2^N
5. N = MSB of result, Z = (result == 0)

**N-bit system ranges:**
- Unsigned: [0, 2^N - 1]
- Signed: [-2^(N-1), 2^(N-1) - 1]

> **HW8 P1a:** 5-bit system, (-15) + (-5):
> → Unsigned: 17 + 27 = 44 > 31 → **C=1**, result = 44 - 32 = 12
> → Signed: -15 + (-5) = -20 < -16 → **V=1**, result = -20 + 32 = 12
> → Binary: 0b01100 → **N=0, Z=0, C=1, V=1**

> **HW8 P1b:** 5-bit system, 11 - 18:
> → Unsigned: 11 - 18 = -7 < 0 → borrow → **C=0**, result = -7 + 32 = 25
> → Signed: 11 - (-14) = 25 > 15 → **V=1**, result = 25 - 32 = -7
> → Binary: 0b11001 → **N=1, Z=0, C=0, V=1**

**Special instructions:**

    CMP Rn, Op2      @ computes Rn - Op2, sets NZCV, discards result
    CMN Rn, Op2      @ computes Rn + Op2, sets NZCV, discards result
    TST Rn, Op2      @ computes Rn AND Op2, sets NZ flags
    TEQ Rn, Op2      @ computes Rn XOR Op2, sets NZ flags
    MRS Rd, APSR     @ read status flags into Rd
    MSR APSR, Rn     @ write Rn into status flags


---

## 9. Condition Code Suffixes — CCS (Lctr 18–19)

| Suffix | Meaning | Logic Equation |
|--------|---------|----------------|
| **EQ** | Equal | Z == 1 |
| **NE** | Not equal | Z == 0 |
| **GT** | Signed > | (V == N) AND (Z == 0) |
| **GE** | Signed >= | V == N |
| **LT** | Signed < | V != N |
| **LE** | Signed <= | (V != N) OR (Z == 1) |
| **HI** | Unsigned > | (C == 1) AND (Z == 0) |
| **HS/CS** | Unsigned >= | C == 1 |
| **LO/CC** | Unsigned < | C == 0 |
| **LS** | Unsigned <= | (C == 0) OR (Z == 1) |

**Memory aid:**
- **Signed** conditions use **V** and **N**
- **Unsigned** conditions use **C** (and Z)
- **Equality** uses only **Z**

> **HW8 P2:** CMP r0, r1 with r0=22, r1=20 → flags N=0, Z=0, C=1, V=0
> → GT: (0==0) AND (0==0) = **True** ✓ (22 > 20)
> → HI: (1==1) AND (0==0) = **True** ✓ (22 >u 20)
> → LT: (0!=0) = **False** ✓ (22 is not < 20)


---

## 10. Conditional Branching (Lctr 19)

**Negative logic pattern:** Branch on the **opposite** condition to skip the "then" block.

    @ if (a >= b) { return a; } else { return b; }
    @ Negative logic: branch if a < b (opposite of a >= b)

    cmp   r0, r1
    blt   else_label         @ branch if a < b (V != N)
    @ then: r0 already holds a
    b     end_label
    else_label:
    mov   r0, r1             @ else: return b
    end_label:
    bx    lr

> **HW8 P3:** `mp_max_ab_i_s` — C condition is `a >= b` (GE), so branch on opposite: `BLT` (Less Than).

**While loop pattern:**

    @ while (i <= e) { body; i++; }

    loop:
        cmp   r0, r1         @ compare i and e
        bgt   end_loop       @ exit if i > e (negative logic: opposite of i <= e)
        @ ... loop body ...
        add   r0, r0, #1     @ i++
        b     loop
    end_loop:

**Quick branch instructions:**

    CBZ  Rn, label      @ Compare and Branch if Zero (Rn == 0)
    CBNZ Rn, label      @ Compare and Branch if Not Zero (Rn != 0)

> **HW8 P4:** 64-bit sum of squares using `SMLAL` (signed multiply-accumulate long):
>
>     ldr   r2, =0               @ sum_lo = 0
>     ldr   r3, =0               @ sum_hi = 0
>     loop:
>         cmp   r0, r1           @ i <= e?
>         bgt   end_loop
>         smlal r2, r3, r0, r0  @ [r3:r2] += i*i (64-bit accumulate)
>         add   r0, #1           @ i++
>         b     loop
>     end_loop:
>         mov   r0, r2           @ return low word
>         mov   r1, r3           @ return high word
>         bx    lr


---

## 11. ASM Instruction Reference with Examples

**Syntax notes:**
- `{Rd,}` means Rd can be omitted if Rd == Rn (e.g., `add r0, #1` = `add r0, r0, #1`)
- **Op2** = immediate `#imm`, register `Rm`, or shifted register `Rm, LSL #n`
- When using shifted Op2, Rd **cannot** be omitted
- **S suffix** updates NZCV flags: `ADDS`, `SUBS`, `LSLS`, etc.

### Data Movement

    mov  r0, r1         @ r0 = r1           (copy register)
    mov  r0, #42        @ r0 = 42           (load small immediate)
    mvn  r0, r1         @ r0 = NOT(r1)      (bitwise complement)
    mvn  r0, #0         @ r0 = 0xFFFFFFFF   (all ones)
    ldr  r0, =0x7000    @ r0 = 0x7000       (load any 32-bit constant)

### Addition & Subtraction

    add  r0, r1, r2     @ r0 = r1 + r2
    add  r0, #5         @ r0 = r0 + 5       (Rd omitted, same as add r0, r0, #5)
    sub  r0, r1, r2     @ r0 = r1 - r2
    sub  r0, #1         @ r0 = r0 - 1
    rsb  r0, r1, #0     @ r0 = 0 - r1       (negate: r0 = -r1)
    rsb  r0, r1, r1, lsl #4  @ r0 = 16*r1 - r1 = 15*r1  (reverse sub with Op2)

    @ With flag updates (S suffix):
    adds r0, r2         @ r0 = r0 + r2, updates NZCV
    subs r0, r2         @ r0 = r0 - r2, updates NZCV (C = NOT borrow)

### Add/Subtract with Carry (64-bit math)

    @ 64-bit add: [r1:r0] = [r1:r0] + [r3:r2]
    adds r0, r2         @ low word add, sets C flag if overflow
    adc  r1, r3         @ high word: r1 = r1 + r3 + C

    @ 64-bit sub: [r1:r0] = [r1:r0] - [r3:r2]
    subs r0, r2         @ low word sub, C=1 if no borrow, C=0 if borrow
    sbc  r1, r3         @ high word: r1 = r1 - r3 - (1-C) = r1 - r3 - borrow

### Multiplication

    mul  r0, r1, r2     @ r0 = r1 * r2       (low 32 bits only)
    mul  r0, r1         @ r0 = r0 * r1       (Rd omitted)
    mla  r0, r1, r2, r3 @ r0 = r3 + r1*r2    (multiply-accumulate)
    mls  r0, r1, r2, r3 @ r0 = r3 - r1*r2    (multiply-subtract, used for modulo)

    @ Example: 17 % 5 using MLS
    @ r0=17, r1=5
    udiv r2, r0, r1     @ r2 = 17/5 = 3
    mls  r0, r1, r2, r0 @ r0 = 17 - 5*3 = 2

### 64-bit Multiply (32×32 → 64)

    smull r2, r3, r0, r1  @ [r3:r2] = r0 * r1 (signed)    r3=HW, r2=LW
    umull r2, r3, r0, r1  @ [r3:r2] = r0 * r1 (unsigned)   r3=HW, r2=LW
    smlal r2, r3, r0, r1  @ [r3:r2] += r0 * r1 (signed accumulate)
    umlal r2, r3, r0, r1  @ [r3:r2] += r0 * r1 (unsigned accumulate)

    @ Example: Q15.16 multiply — extract bits b47:b16 from 64-bit product
    smull r1, r0, r0, r1  @ [r0:r1] = A*B (r0=HW, r1=LW)
    lsl   r0, #16          @ keep bits b47:b32 of HW
    add   r0, r0, r1, lsr #16  @ combine with bits b31:b16 of LW

    @ Example: sum of squares using SMLAL (HW8 P4)
    smlal r2, r3, r0, r0  @ [r3:r2] += i*i  (no separate add step needed!)

### Division

    udiv r0, r1, r2     @ r0 = r1 / r2      (unsigned, truncated toward 0)
    sdiv r0, r1, r2     @ r0 = r1 / r2      (signed, truncated toward 0)

    @ No S version. No remainder — use MLS for that.

### Shift Instructions

    lsl  r0, r1, #4     @ r0 = r1 << 4      (multiply by 16)
    lsl  r0, #3         @ r0 = r0 << 3      (Rd omitted: multiply r0 by 8)
    lsr  r0, r1, #4     @ r0 = r1 >> 4      (unsigned divide by 16, fills 0s)
    asr  r0, r1, #4     @ r0 = r1 >> 4      (signed divide by 16, fills sign bit)

    @ With S suffix — C flag = last bit shifted out:
    lsls r1, r0, #1     @ r1 = r0 << 1, C = bit 31 of r0 (bit shifted out of MSB)
    lsrs r2, r0, #3     @ r2 = r0 >> 3, C = bit 2 of r0 (last bit shifted out)

    @ Example: r0 = 0xDD = 0b1101_1101
    lsls r1, r0, #1     @ r1 = 0x1BA, C = 0 (bit 31 was 0)
    lsrs r2, r0, #3     @ r2 = 0x1B,  C = 1 (bit 2 was 1)

### Barrel Shifter (Op2 with shift — zero extra cycles)

    add  r0, r1, r1, lsl #4   @ r0 = r1 + r1*16 = 17*r1
    sub  r0, r1, r1, asr #4   @ r0 = r1 - r1/16 = 15*r1/16
    rsb  r0, r1, r1, lsl #4   @ r0 = r1*16 - r1 = 15*r1

    @ Op2 forms: #imm, Rm, or Rm shifted by LSL/LSR/ASR #n
    @ When using shifted Op2, MUST write all 3 registers:
    add  r0, r1, r1, lsl #4   @ CORRECT (Rd, Rn, Op2)
    @ add  r1, r1, lsl #4     @ WRONG — cannot omit Rd with shifted Op2

### Bitwise Logic

    and  r0, r1, r2     @ r0 = r1 AND r2    (extract bits with mask)
    and  r0, #0xFF      @ r0 = r0 AND 0xFF  (keep lowest byte)
    orr  r0, r1, r2     @ r0 = r1 OR r2     (set bits)
    orr  r0, #0x50      @ r0 = r0 OR 0x50   (set bits 6,4)
    eor  r0, r1, r2     @ r0 = r1 XOR r2    (toggle bits)
    bic  r0, r1, r2     @ r0 = r1 AND NOT(r2)  (clear bits specified by r2)
    bic  r0, #0xF0      @ r0 = r0 AND NOT(0xF0) (clear bits 7:4)
    orn  r0, r1, r2     @ r0 = r1 OR NOT(r2)

    @ Example: replace hex digit H1 (bits 7:4) with 0xA
    bic  r0, r0, #0xF0     @ clear digit H1: 0xH3H2_0_H0
    orr  r0, r0, #0xA0     @ set digit H1:   0xH3H2_A_H0

    @ Example: trace from HW7 P5 (r0=0xAD, r1=0x03)
    bic  r3, r0, r1        @ 0xAD AND NOT(0x03) = 0xAD AND 0xFC = 0xAC
    orr  r4, r3, r1        @ 0xAC OR 0x03 = 0xAF
    eor  r5, r0, r1        @ 0xAD XOR 0x03 = 0xAE

### Bit-Field Instructions

    bfc  r0, #4, #4     @ clear 4 bits starting at bit 4 (bits [7:4] → 0)
    bfi  r0, r1, #4, #4 @ insert lowest 4 bits of r1 into r0 at bits [7:4]

    @ Example: replace digit H1 with value in r1 (alternative to BIC+ORR)
    bfc  r0, #4, #4         @ clear bits [7:4]
    bfi  r0, r1, #4, #4     @ insert r1[3:0] at bits [7:4]

### Compare & Test (set flags, discard result)

    cmp  r0, r1         @ computes r0 - r1, sets NZCV, result NOT stored
    cmp  r0, #10        @ computes r0 - 10, sets NZCV
    cmn  r0, r1         @ computes r0 + r1, sets NZCV, result NOT stored
    tst  r0, r1         @ computes r0 AND r1, sets NZ flags

    @ Example: CMP for branching
    cmp  r0, r1         @ if r0=22, r1=20: 22-20=2 → N=0,Z=0,C=1,V=0

### Branch Instructions

    b    label          @ unconditional branch (always jump)
    b{cc} label         @ conditional branch (jump only if condition cc is true)
    bx   lr             @ return from leaf function
    cbz  r0, label      @ branch if r0 == 0 (compare and branch if zero)
    cbnz r0, label      @ branch if r0 != 0

    @ Common conditional branches after CMP:
    beq  label          @ branch if equal        (Z==1)
    bne  label          @ branch if not equal    (Z==0)
    bgt  label          @ branch if signed >     (V==N and Z==0)
    bge  label          @ branch if signed >=    (V==N)
    blt  label          @ branch if signed <     (V!=N)
    ble  label          @ branch if signed <=    (V!=N or Z==1)
    bhi  label          @ branch if unsigned >   (C==1 and Z==0)
    bhs  label          @ branch if unsigned >=  (C==1)
    blo  label          @ branch if unsigned <   (C==0)
    bls  label          @ branch if unsigned <=  (C==0 or Z==1)

    @ Example: if (a >= b) return a; else return b;
    cmp  r0, r1
    blt  else           @ negative logic: branch if a < b (opposite of a >= b)
    b    end            @ then: r0 already holds a
    else:
    mov  r0, r1         @ else: return b
    end:
    bx   lr

### Stack & Function Call

    push {r4, r5, lr}   @ save callee-saved regs + link register
                         @ SP decreases by 4 per register
                         @ lowest reg# stored at lowest address
    pop  {r4, r5, pc}   @ restore regs, pop LR directly into PC (return)

    @ Leaf function (no calls): just use bx lr
    @ Stem function (calls others): must push lr, pop pc

### Special Registers

    mrs  r0, apsr       @ read APSR flags (N,Z,C,V) into r0
    msr  apsr_nzcvq, r0 @ write r0 into APSR flags

    @ Example: read the C flag
    mrs  r0, apsr       @ r0 = APSR (flags in bits 31:28)
    lsr  r0, #29        @ shift C flag (bit 29) to bit 0
    and  r0, #1         @ mask to get just C


---
---

# Worked Examples — Step-by-Step Homework Solutions

These walk through complete problems from HW6, HW7, and HW8 with explicit objectives and numbered steps.

---

## WE-1: Stack Push and Memory Layout (HW6 P1)

**Objective:** Given `PUSH {r7, r5, r8, r6}` with SP = 0x2000_1020 and R_i = (1 << i) + (1 << 2i), find the final SP, the word at address 0x2000_1014, and the byte at that address.

**Step 1 — Compute SP after push:**
Count registers being pushed: r5, r6, r7, r8 = 4 registers.
Each register = 4 bytes, so total = 16 bytes = 0x10.
Full descending: SP decreases.

    SP_after = 0x2000_1020 - 0x10 = 0x2000_1010

**Step 2 — Determine which register is at 0x2000_1014:**
PUSH stores registers sorted by number (lowest reg# at lowest address):

    0x2000_1010 → R5
    0x2000_1014 → R6   ← this address
    0x2000_1018 → R7
    0x2000_101C → R8

**Step 3 — Compute R6 using the formula:**

    R6 = (1 << 6) + (1 << 12) = 64 + 4096 = 4160 = 0x0000_1040

**Step 4 — Find the byte at 0x2000_1014 (little-endian):**
Little-endian: LSB stored at lowest address.

    0x2000_1014 → 0x40  (LSB of 0x1040)
    0x2000_1015 → 0x10
    0x2000_1016 → 0x00
    0x2000_1017 → 0x00

**Answer:** SP = 0x2000_1010, word = 0x0000_1040, byte = **0x40**

---

## WE-2: Type Promotion — Zero vs Sign Extension (HW6 P2 & P3)

**Objective:** Determine R0–R3 when calling functions with narrower types promoted to 32-bit.

### Unsigned case (HW6 P2): `fn1(var1, var2, 0xFFF, 0xFFFF)` where var1=0xF (uint8_t), var2=0xFF (uint8_t), params are uint32_t.

**Step 1 — Identify promotion type:** Source is unsigned → **zero-extend** (pad upper bits with 0).

**Step 2 — Extend each argument to 32 bits:**

    var1 = 0xF  (uint8_t) → pad 24 bits of 0s → R0 = 0x0000_000F
    var2 = 0xFF (uint8_t) → pad 24 bits of 0s → R1 = 0x0000_00FF
    0xFFF  (fits in 32 bits)                   → R2 = 0x0000_0FFF
    0xFFFF (fits in 32 bits)                   → R3 = 0x0000_FFFF

### Signed case (HW6 P3): `fn2(var1, var2)` where var1=0xF (int8_t), var2=0xFF (int8_t), params are int32_t.

**Step 1 — Identify promotion type:** Source is signed → **sign-extend** (replicate MSB).

**Step 2 — Check MSB of each 8-bit value:**

    var1 = 0xF = 0b0000_1111 → MSB = 0 (positive, value = +15)
    → pad 24 bits of 0s → R0 = 0x0000_000F

    var2 = 0xFF = 0b1111_1111 → MSB = 1 (negative, value = -1)
    → pad 24 bits of 1s → R1 = 0xFFFF_FFFF

**Verify:** 0xFFFF_FFFF as int32_t = -1, same value as 0xFF as int8_t. ✓

---

## WE-3: Q15.16 Fixed-Point Encoding (HW6 P4)

**Objective:** Encode the real number 3.25 in Q15.16 format and determine the return register.

**Step 1 — Identify the format:**
Q15.16 = 1 sign bit + 15 integer bits + 16 fractional bits = 32 bits total.
n = 16 (number of fractional bits).

**Step 2 — Apply the encoding formula:** I = f × 2^n

    I = 3.25 × 2^16 = 3.25 × 65536

**Step 3 — Compute:**

    3 × 65536 = 196608
    0.25 × 65536 = 16384
    Total = 196608 + 16384 = 212992

**Step 4 — Convert to hex:**

    Integer part: 3 → shifted left by 16 → 0x0003_0000
    Fractional part: 0.25 → 0.25 × 65536 = 16384 = 0x4000
    Sum: 0x0003_0000 + 0x4000 = 0x0003_4000

**Step 5 — Return register:** EABI: 32-bit return → **R0**

**Answer:** R0 = **0x0003_4000**

---

## WE-4: 64-bit Addition with Carry (HW6 P5)

**Objective:** Compute A1 + B1 where A1 = (int64_t)0x388 << 24, B1 = (int64_t)0x289 << 24. Find the result and C flag.

**Step 1 — Expand to 64-bit hex:**

    A1 = 0x388 << 24 = 0x0000_0003_8800_0000
    B1 = 0x289 << 24 = 0x0000_0002_8900_0000

**Step 2 — Split into register pairs (Hi:Lo):**

    A1: R1 = 0x0000_0003,  R0 = 0x8800_0000
    B1: R3 = 0x0000_0002,  R2 = 0x8900_0000

**Step 3 — ADDS (low word):**

    R0 + R2 = 0x8800_0000 + 0x8900_0000 = 0x1_1100_0000  (33 bits!)
    Low word result = 0x1100_0000 (bottom 32 bits)
    C = 1 (overflow from bit 31)

**Step 4 — ADC (high word):**

    R1 + R3 + C = 0x3 + 0x2 + 1 = 0x6

**Answer:** Result = 0x0000_0006_1100_0000, **C = 1**

---

## WE-5: 64-bit Subtraction with Borrow (HW6 P6)

**Objective:** Compute A1 - B1 where A1 = (int64_t)0x387 << 28, B1 = (int64_t)0x28 << 28.

**Step 1 — Expand and split:**

    A1 = 0x0000_0038_7000_0000 → R1=0x38, R0=0x7000_0000
    B1 = 0x0000_0002_8000_0000 → R3=0x02, R2=0x8000_0000

**Step 2 — SUBS (low word):**

    R0 - R2 = 0x7000_0000 - 0x8000_0000
    0x7000_0000 < 0x8000_0000 → borrow needed!
    Borrow from high word: 0x1_7000_0000 - 0x8000_0000 = 0xF000_0000
    C = 0 (borrow occurred → ARM sets C = 0)

**Step 3 — SBC (high word):**

    SBC computes: R1 - R3 - (1-C) = R1 - R3 - 1  (since C=0)
    0x38 - 0x02 - 1 = 0x35

**Answer:** Result = 0x0000_0035_F000_0000, **C = 0**

---

## WE-6: Unsigned Modulo in ASM (HW6 P7)

**Objective:** Implement `uint32_t umod32bit_s(uint32_t A, uint32_t B)` returning A % B.

**Step 1 — Recall:** No MOD instruction in ARM. Use identity: A % B = A - (A/B) × B.

**Step 2 — Write the function (MLS version):**

    umod32bit_s:
        udiv r2, r0, r1       @ Step 2a: r2 = A / B (integer quotient)
        mls  r0, r1, r2, r0   @ Step 2b: r0 = A - B*(A/B) = remainder
        bx   lr               @ Step 2c: return (leaf function)

**Step 3 — Trace with A=17, B=5:**

    R0=17, R1=5
    udiv r2, r0, r1  → r2 = 17/5 = 3
    mls  r0, r1, r2, r0 → r0 = 17 - 5×3 = 17 - 15 = 2

**Answer:** 17 % 5 = **2**. Only uses R0–R2 (all caller-saved), no PUSH/POP needed.

---

## WE-7: Q15.16 Multiply — Extracting Middle Bits (HW7 P1)

**Objective:** Modify Q31 multiply code to perform Q15.16 multiply. Q31 extracts bits b62–b31 (right-shift 31). Q15.16 needs bits b47–b16 (right-shift 16).

**Step 1 — Understand the bit layout after SMULL:**

    After smull r1, r0, r0, r1:  r0 = HW [b63..b32], r1 = LW [b31..b0]

    Q31  needs: [b62 .......... b31]  → shift right by 31
    Q15.16 needs: [b47 ...... b16]    → shift right by 16

**Step 2 — Figure out the shift amounts:**
For Q15.16 (n=16): LW right-shift = n = 16. HW left-shift = 32 - n = 16.

**Step 3 — Write the code:**

    smull r1, r0, r0, r1    @ [r0:r1] = 64-bit product (r0=HW, r1=LW)
    lsl   r0, #16            @ HW << 16: keeps bits b47:b32 in upper half
    add   r0, r0, r1, lsr #16  @ LW >> 16: brings bits b31:b16 into lower half
    bx    lr

**Step 4 — Verify bit positions:**
- `lsl r0, #16`: HW bits b47:b32 move to positions [31:16] of result
- `r1, lsr #16`: LW bits b31:b16 move to positions [15:0] of result
- `add` combines them: result = bits [b47:b16] ✓

**Answer:** Change `lsl r0, #1` to `lsl r0, #16`, and `r1, lsr #31` to `r1, lsr #16`.

---

## WE-8: Shift Operations and C Flag (HW7 P2)

**Objective:** Given R0 = 0x000000DD, trace `lsls r1, r0, #1` and `lsrs r2, r0, #3`. Find R1, R2, and the C flag.

**Step 1 — Write R0 in binary:**

    R0 = 0xDD = 0b1101_1101

Full 32-bit: `0000_0000_0000_0000_0000_0000_1101_1101`

**Step 2 — LSLS r1, r0, #1 (shift left by 1):**

    Shift all bits left by 1, fill 0 from right:
    0000_0000_0000_0000_0000_0001_1011_1010

    R1 = 0x000001BA
    C flag = bit 31 of R0 before shift = 0  (bit 31 was shifted out)

**Step 3 — LSRS r2, r0, #3 (shift right by 3):**

    R0 bits: ...1101_1[101]  ← these 3 bits are shifted out
                               last one out (bit 2) sets C flag
    Result: ...0001_1011

    R2 = 0x0000001B
    C flag = bit 2 of R0 = 1

**Step 4 — Final C flag:**
C reflects the **last flag-setting instruction**, which is LSRS.

**Answer:** R1 = 0x000001BA, R2 = 0x0000001B, **C = 1**

---

## WE-9: Single-Instruction Scaling with Op2 (HW7 P3)

**Objective:** Express each scaling operation as a single ARM instruction using the barrel shifter. B is in R1 (signed), result in R0.

**Step 1 — Decompose each factor into powers of 2:**

    16  = 2^4           → just shift
    17  = 1 + 16        → add original + shifted
    15  = 16 - 1        → subtract original from shifted (reverse sub)
    1/16 = 2^(-4)       → just shift right (ASR for signed)
    17/16 = 1 + 1/16    → add original + shifted right
    15/16 = 1 - 1/16    → subtract shifted right from original

**Step 2 — Write each instruction:**

    (a) A = 16B:     lsl r0, r1, #4          @ r0 = r1 << 4 = 16*r1
    (b) A = 17B:     add r0, r1, r1, lsl #4  @ r0 = r1 + 16*r1 = 17*r1
    (c) A = 15B:     rsb r0, r1, r1, lsl #4  @ r0 = 16*r1 - r1 = 15*r1
    (d) A = B/16:    asr r0, r1, #4          @ r0 = r1 >> 4 (signed)
    (e) A = 17B/16:  add r0, r1, r1, asr #4  @ r0 = r1 + r1/16
    (f) A = 15B/16:  sub r0, r1, r1, asr #4  @ r0 = r1 - r1/16

**Key insight:** Use RSB for (c) because we need `(shifted) - (original)`. RSB computes Op2 - Rn. Use ASR (not LSR) for (d)–(f) because B is signed.

---

## WE-10: BIC/ORR Field Assignment (HW7 P4)

**Objective:** Analyze `mp_func_s` which uses BIC and ORR with shifted Op2. Determine what it does to input 0xH3H2H1H0, then write the C equivalent.

**Given code:**

    ldr  r1, =15               @ r1 = 0xF
    bic  r0, r0, r1, lsl #4   @ r0 = r0 AND NOT(0xF << 4)
    ldr  r2, =10               @ r2 = 0xA
    orr  r0, r0, r2, lsl #4   @ r0 = r0 OR (0xA << 4)

**Step 1 — Trace the BIC:**

    r1, lsl #4 = 0xF << 4 = 0xF0 (bits [7:4] are all 1s)
    NOT(0xF0) = 0xFFFFFF0F
    r0 AND 0xFFFFFF0F = clears bits [7:4] → 0xH3H2_0_H0

**Step 2 — Trace the ORR:**

    r2, lsl #4 = 0xA << 4 = 0xA0
    r0 OR 0xA0 = sets bits [7:4] to 0xA → 0xH3H2_A_H0

**Step 3 — Summary:** The function replaces hex digit H1 with 0xA.

**Step 4 — C equivalent:**

    uint16_t mp_func_c(uint16_t a) {
        return (a & ~(0xF << 4)) | (0xA << 4);
        // equivalently: (a & 0xFF0F) | 0x00A0;
    }

**Answer:** Result = **0xH3H2AH0** (digit H1 replaced with A)

---

## WE-11: Bitwise Logic Trace (HW7 P5)

**Objective:** Trace 5 bitwise operations given R0 = 0xAD, R1 = 0x03.

**Step 1 — Write initial values in binary:**

    R0 = 0xAD = 1010_1101
    R1 = 0x03 = 0000_0011

**Step 2 — `lsr r2, r1, #2`:**

    0000_0011 >> 2 = 0000_0000
    R2 = 0x00

**Step 3 — `lsl r2, #2`:**

    0000_0000 << 2 = 0000_0000   (shifting zero gives zero)
    R2 = 0x00

**Step 4 — `bic r3, r0, r1`:** (R0 AND NOT R1)

      1010_1101  (0xAD)
    AND 1111_1100  (NOT 0x03 = 0xFC)
    = 1010_1100
    R3 = 0xAC

**Step 5 — `orr r4, r3, r1`:**

      1010_1100  (0xAC)
    OR 0000_0011  (0x03)
    = 1010_1111
    R4 = 0xAF

**Step 6 — `eor r5, r0, r1`:**

      1010_1101  (0xAD)
    XOR 0000_0011  (0x03)
    = 1010_1110
    R5 = 0xAE

**Answer:** R2=0x00, R3=0xAC, R4=0xAF, R5=0xAE

---

## WE-12: Hex Digit Manipulation — Three Patterns (HW7 P6)

**Objective:** Write C and ASM functions for three digit transformations on A = 0xH3H2H1H0 (uint16_t).

### (a) Replace H1 with 5: 0xH3H2H1H0 → 0xH3H25H0

**Step 1 — Strategy:** Clear digit H1 (bits [7:4]), then set it to 5. Same pattern as WE-10.

**Step 2 — C:**

    return (A & 0xFF0F) | 0x0050;

**Step 3 — ASM:**

    bic r0, r0, #0xF0       @ clear bits [7:4]
    orr r0, r0, #0x50       @ set bits [7:4] to 5
    bx  lr

### (b) Shift left and insert 3: 0xH3H2H1H0 → 0xH2H1H03

**Step 1 — Strategy:** Shift entire value left by 4 bits (one hex digit), then insert 3 at the bottom.

**Step 2 — C:**

    return (A << 4) | 0x3;

**Step 3 — ASM:**

    lsl r0, r0, #4          @ shift left: 0xH2H1H00
    orr r0, r0, #3          @ insert 3:   0xH2H1H03
    bx  lr

### (c) Shift right and insert 7: 0xH3H2H1H0 → 0x7H3H2H1

**Step 1 — Strategy:** Shift entire value right by 4 bits, then insert 7 at the top (bits [15:12]).

**Step 2 — C:**

    return (A >> 4) | 0x7000;

**Step 3 — ASM:**

    lsr r0, r0, #4          @ shift right: 0x0H3H2H1
    ldr r1, =0x7000         @ can't encode 0x7000 as immediate
    orr r0, r0, r1          @ insert 7:    0x7H3H2H1
    bx  lr

**Note:** 0x7000 doesn't fit the ARM 8-bit rotated immediate format, so we must use LDR.

---

## WE-13: NZCV Flag Computation — 5-bit System (HW8 P1)

**Objective:** Compute NZCV flags for two operations in a 5-bit system (N=5).

**Setup:** C_N = 2^5 = 32, Unsigned range [0, 31], Signed range [-16, 15].

### (a) (-15) + (-5)

**Step 1 — Convert to unsigned equivalents:**

    -15 → -15 + 32 = 17  (binary: 10001)
    -5  → -5 + 32 = 27   (binary: 11011)

**Step 2 — Unsigned check (for C flag):**

    u_temp = 17 + 27 = 44
    44 > U_MAX(31) → carry! → C = 1
    Corrected: 44 - 32 = 12

**Step 3 — Signed check (for V flag):**

    s_temp = (-15) + (-5) = -20
    -20 < S_MIN(-16) → overflow! → V = 1
    Corrected: -20 + 32 = 12

**Step 4 — Binary result and remaining flags:**

    12 = 0b01100
    MSB (bit 4) = 0 → N = 0
    Result ≠ 0     → Z = 0

**Answer:** N=0, Z=0, C=1, V=1, binary = 0b01100

### (b) 11 - 18

**Step 1 — Unsigned check (for C flag):**

    u_temp = 11 - 18 = -7
    -7 < U_MIN(0) → borrow! → C = 0 (ARM: C = 1 - borrow)
    Corrected: -7 + 32 = 25

**Step 2 — Signed check (for V flag):**
18 in 5-bit signed = 18 - 32 = -14 (since 18 > S_MAX).

    s_temp = 11 - (-14) = 25
    25 > S_MAX(15) → overflow! → V = 1
    Corrected: 25 - 32 = -7

**Step 3 — Binary result and remaining flags:**

    25 = 0b11001
    MSB (bit 4) = 1 → N = 1
    Result ≠ 0     → Z = 0

**Answer:** N=1, Z=0, C=0, V=1, binary = 0b11001

---

## WE-14: CMP and CCS Verification (HW8 P2)

**Objective:** After `CMP r0, r1` with r0=22, r1=20 in a 6-bit system, determine NZCV flags and verify all 8 condition code suffixes.

**Step 1 — Compute flags from CMP (which does r0 - r1):**

    22 - 20 = 2
    Unsigned: 2 ∈ [0,63] → no borrow → C = 1
    Signed: 2 ∈ [-32,31] → no overflow → V = 0
    Result = 2 → N = 0 (positive), Z = 0 (nonzero)

    Flags: N=0, Z=0, C=1, V=0

**Step 2 — Evaluate each CCS using logic equations:**

    EQ: Z==1          → 0==1 → False  (22 ≠ 20)    ✓
    NE: Z==0          → 0==0 → True   (22 ≠ 20)    ✓
    GT: (V==N)&&(Z==0) → (0==0)&&(0==0) → True  (22 > 20)   ✓
    GE: V==N          → 0==0 → True   (22 ≥ 20)    ✓
    LT: V!=N          → 0!=0 → False  (22 not < 20) ✓
    LE: (V!=N)||(Z==1) → F||F → False (22 not ≤ 20) ✓
    HI: (C==1)&&(Z==0) → T&&T → True  (22 >u 20)   ✓
    HS: C==1          → True           (22 ≥u 20)   ✓
    LO: C==0          → False          (22 not <u 20) ✓
    LS: (C==0)||(Z==1) → F||F → False (22 not ≤u 20) ✓

**Answer:** All conditions match expected behavior for 22 > 20.

---

## WE-15: Conditional Branch — Max Function (HW8 P3)

**Objective:** Implement `if (a >= b) return a; else return b;` in ARM assembly.

**Step 1 — Identify the C condition and its negative:**
C condition: `a >= b` (GE). Negative logic: branch on `a < b` (LT).

**Step 2 — Choose the branch suffix:**
LT (Less Than, signed) triggers when V != N.

**Step 3 — Map registers:**
EABI: a → R0, b → R1, return in R0.

**Step 4 — Write the assembly:**

    mp_max_ab_i_s:
        cmp   r0, r1                   @ compare a and b
        blt   mp_max_ab_i_s_else       @ if a < b, go to else
    mp_max_ab_i_s_then:
        b     mp_max_ab_i_s_end_if     @ a >= b: r0 has a, skip else
    mp_max_ab_i_s_else:
        mov   r0, r1                   @ a < b: put b in r0
    mp_max_ab_i_s_end_if:
        bx    lr                       @ return r0

**Step 5 — Trace with a=10, b=7:**

    cmp r0, r1 → 10 - 7 = 3 → N=0, V=0 → V==N → LT is False
    blt: NOT taken → fall through to then
    b: jump to end → return r0 = 10 ✓

**Step 6 — Trace with a=3, b=8:**

    cmp r0, r1 → 3 - 8 = -5 → N=1, V=0 → V!=N → LT is True
    blt: TAKEN → jump to else
    mov r0, r1 → r0 = 8
    bx lr → return 8 ✓

---

## WE-16: While Loop with 64-bit Accumulator (HW8 P4)

**Objective:** Implement `int64_t sum = 0; while (i <= e) { sum += i*i; i++; }` in ARM assembly.

**Step 1 — Register allocation:**

    r0 = i (reuse input s as loop variable)
    r1 = e (loop bound, unchanged)
    r2 = sum low word
    r3 = sum high word
    Return: r0 (low), r1 (high)

**Step 2 — Choose multiplication strategy:**
i*i needs 32×32 → 64-bit result, and we accumulate into [r3:r2].
Use **SMLAL** (signed multiply-accumulate long): [r3:r2] += r0 × r0.
This replaces SMULL + ADDS + ADC with a single instruction.

**Step 3 — Loop condition (negative logic):**
C condition: `i <= e`. Branch on opposite: `i > e` → `BGT`.

**Step 4 — Write the assembly:**

    mp_range_square_sum_standard_while_s:
        ldr   r2, =0                @ sum_lo = 0
        ldr   r3, =0                @ sum_hi = 0

    loop:
        cmp   r0, r1                @ compare i and e
        bgt   end_loop              @ if i > e, exit
        smlal r2, r3, r0, r0       @ [r3:r2] += i*i
        add   r0, #1               @ i++
        b     loop                  @ repeat

    end_loop:
        mov   r0, r2               @ return low word in r0
        mov   r1, r3               @ return high word in r1
        bx    lr

**Step 5 — Trace with s=1, e=3:**

    Init: r0=1, r1=3, r2=0, r3=0

    Iter 1: cmp 1,3 → not GT. smlal: [r3:r2] += 1*1 = 1. i=2.
    Iter 2: cmp 2,3 → not GT. smlal: [r3:r2] += 2*2 = 5. i=3.
    Iter 3: cmp 3,3 → not GT. smlal: [r3:r2] += 3*3 = 14. i=4.
    Iter 4: cmp 4,3 → GT! Exit loop.

    Return: [r1:r0] = [0:14] = 14.  Verify: 1+4+9 = 14 ✓

**Note:** No PUSH/POP needed here because we only use R0–R3 (all caller-saved). If we needed R4/R5, we would need to push/pop them.
