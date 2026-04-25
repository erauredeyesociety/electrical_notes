% HW5 + HW6 compact extracts for final-exam cheatsheet
% HW5 = Fixed-point Q-format (not mixed C/ASM — user desc mismatch).
% HW6 = EABI arg passing, 64-bit ADC/SBC, UDIV+MUL modulo.

### HW5 P1 (8pts) — Encode 2.75 in UQ3.5

**Rule:** I = round(f * 2^n); then hex (add 2^N if negative).
**Calc:** 2.75 * 2^5 = 88 = **0x58**.
**Key concept:** UQm.n unsigned, N=m+n. Scale by 2^n, round, hex.

### HW5 P2 (16pts) — Decode Q3.4 codes (signed, N=8)

**(a)** 0x77 = 119, MSB=0 -> +119/16 = **7.4375**.
**(b)** 0xAA = 170, MSB=1 -> I=170-256=-86; -86/16 = **-5.375**.
**Key concept:** Qm.n = 1 sign + m int + n frac. If MSB=1, subtract 2^N before scaling.

### HW5 P3 (10pts) — Decode Q2.5 code 0b1001_1001

**Calc:** U=153, MSB=1, I=153-256=-103; -103/32 = **-3.21875**.
**Key concept:** Same TC decode rule; scale factor 2^-n.

### HW5 P4 (32pts) — Encode into Q3.4 (range -8.0 to +7.9375)

**(a)** 0.5*16=8 -> **0x08**.
**(b)** 6.73*16=107.68, round->108 -> **0x6C** (err 0.02).
**(c)** -2.25*16=-36, +256=220 -> **0xDC**.
**(d)** -4.5*16=-72, +256=184 -> **0xB8**.
**Key concept:** Encode = f*2^n, round, if neg add 2^N, hex.

### HW5 P5 (44pts) — Q15 multiply-accumulate f1*f2+f3*f4

**Encode (I=f*2^15):** 0.5->0x4000, 0.25->0x2000, 0.125->0x1000, 0.0625->0x0800.
**Mult:** (I_A*I_B)>>15. 0x4000*0x2000>>15=0x1000; 0x1000*0x0800>>15=0x0100.
**Add:** 0x1000+0x0100=**0x1100** -> 4352/32768 = **0.1328125**.
**Key concept:** Q15*Q15=Q30 in 32-bit; >>15 renormalizes to Q15. Q-format addition is plain int add.

---

### HW6 P1 (PUSH to full-descending stack)

**Setup:** SP=0x20001020; `PUSH {r7,r5,r8,r6}`; Ri=(1<<i)+(1<<2i).
**P1.1 SP after:** 4 regs*4B=16 -> **SP=0x20001010**.
**P1.2 R5:** (1<<5)+(1<<10) = 32+1024 = **0x00000420**.
**P1.3 Storage order:** HW sorts by register number, low reg -> low addr.
  0x..1010=R5, 0x..1014=R6, 0x..1018=R7, 0x..101C=R8. Word@1014 = R6 = (1<<6)+(1<<12) = **0x00001040**.
**P1.4 Byte @0x20001014:** little-endian LSB = **0x40**.
**Key concept:** PUSH ignores listed order; stores ascending by reg#, lowest reg at lowest addr. ARM little-endian.

### HW6 P2 (EABI arg promotion — unsigned)

**Call:** `fn1(uint8_t 0xF, uint8_t 0xFF, 0xFFF, 0xFFFF)` with uint32_t params.
**Regs:** R0=0x0000000F, R1=0x000000FF, R2=0x00000FFF, R3=0x0000FFFF.
**Key concept:** Unsigned args zero-extend to 32b; first 4 args in R0-R3.

### HW6 P3 (EABI arg promotion — signed)

**Call:** `fn2(int8_t 0xF, int8_t 0xFF)` with int32_t params.
**R0:** 0xF, MSB=0 -> **0x0000000F**. **R1:** 0xFF (=-1), MSB=1 -> **0xFFFFFFFF**.
**Key concept:** Signed args sign-extend (replicate MSB); value is preserved.

### HW6 P4 (Q15.16 return value)

**Encode 3.25:** I = 3.25*2^16 = 3*0x10000 + 0x4000 = **0x00034000**.
**Return reg:** 32-bit return goes in **R0** (EABI).
**Key concept:** Qm.n: I=f*2^n. 32-bit returns in R0; 64-bit returns in R0:R1.

### HW6 P5 (64-bit ADD with ADDS/ADC)

**Code:**
    mp_add_64bit_s:
        ADDS r0, r2       @ low, sets C
        ADC  r1, r3       @ high + C
        BX   lr
**Convention:** R0=lo(A), R1=hi(A), R2=lo(B), R3=hi(B).
**Test 1:** 0x88000000+0x89000000=0x1_11000000 -> lo=0x11000000, **C=1**; hi=3+2+1=6 -> C1=0x611<<24.
**Test 2:** 0x78000000+0x79000000=0xF1000000, **C=0**; hi=3+2+0=5 -> C2=0x5F1<<24.
**Key concept:** ADDS sets C on unsigned overflow from bit 31; ADC adds C into high word.

### HW6 P6 (64-bit SUB with SUBS/SBC)

**Code:**
    mp_sub_64bit_s:
        SUBS r0, r2       @ low, sets C (C=NOT borrow)
        SBC  r1, r3       @ high - !C
        BX   lr
**ARM subtract flag:** C=1 -> no borrow; C=0 -> borrow. SBC computes R1 - R3 - (1-C).
**Test 1:** 0x70000000-0x80000000 needs borrow -> lo=0xF0000000, **C=0**; hi=0x38-0x02-1=0x35 -> D1=0x35F<<28.
**Test 2:** 0x80000000-0x80000000=0, no borrow -> **C=1**; hi=0x38-0x28-0=0x10 -> D2=0x100<<28.
**Key concept:** On ARM, C=!borrow. SBC subtracts the inverted carry, so a borrow in the low word propagates to high.

### HW6 P7 (UDIV + MUL for modulo)

**Identity:** A % B = A - (A/B)*B.
**ASM (leaf, caller-saved R0-R2, no push/pop):**
    umod32bit_s:
        UDIV r2, r0, r1    @ r2 = A/B
        MUL  r2, r2, r1    @ r2 = (A/B)*B
        SUB  r0, r0, r2    @ r0 = A - (A/B)*B
        BX   lr
**Example:** A=17,B=5 -> 17/5=3, 3*5=15, 17-15=2.
**Key concept:** ARM has no modulo instruction; synthesize with UDIV/SDIV + MUL + SUB. MUL (no S) doesn't touch flags.
