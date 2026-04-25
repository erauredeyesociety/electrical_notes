# HW7 / HW8 Extracts — Final Exam Cheatsheet Source

Source: `content/cec_320/quizes/quiz3/hw_solutions_summary.md`. Skips LDR/STR,
if-else, loops, CBZ/CBNZ, AAPCS — already covered in qz4_cheatsheet.md.

---

## HW7 — Shift and Bitwise Logic (Lctr 16-17)

### HW7 Problem 1 (10pts) — Q15.16 multiply from smull

**Task:** After `smull r1,r0,r0,r1` (R0=HW, R1=LW), extract Q15.16 result (bits b47..b16).
**ASM (key lines):**

    smull  r1, r0, r0, r1
    lsl    r0, #16              @ HW left by (target MSB - 31) = 47-31
    add    r0, r0, r1, lsr #16  @ bring top 16 bits of LW in

**Key concept:** For Qm.n: `lsr` of LW by n, `lsl` of HW by (target_msb-31). Q31 = lsl 1 / lsr 31; Q15.16 = lsl 16 / lsr 16; Q16.15 = lsl 17 / lsr 15.

---

### HW7 Problem 2 (15pts) — LSLS/LSRS and C flag

**Task:** R0=0xDD; predict R1=lsls r0,#1, R2=lsrs r0,#3, and C.
**ASM (key lines):**

    ldr   r0, =0b1101_1101
    lsls  r1, r0, #1           @ R1 = 0x1BA (9-bit result, b7 shifted out → C=0-ish)
    lsrs  r2, r0, #3           @ R2 = 0x1B; last bit out = b2 of R0 = 1 → C=1

**Key concept:** S-suffix shifts set C to the **last bit shifted out**. For `lsrs #n`, that's bit (n-1) of the source; for `lsls #n`, bit (32-n).

---

### HW7 Problem 3 (30pts) — Barrel-shifter scaling (one-instr multiplies)

**Task:** Compute A = k*B (signed) in a single instruction using Op2.
**ASM (key lines):**

    lsl  r0, r1, #4              @ A = 16*B        (2^4)
    add  r0, r1, r1, lsl #4      @ A = 17*B        (1 + 2^4)
    rsb  r0, r1, r1, lsl #4      @ A = 15*B        (2^4 - 1)    <-- rsb: Op2 - Rn
    asr  r0, r1, #4              @ A = B/16
    add  r0, r1, r1, asr #4      @ A = 17*B/16     (1 + 2^-4)
    sub  r0, r1, r1, asr #4      @ A = 15*B/16     (1 - 2^-4)

**Key concept:** Decompose k as `1 ± 2^n` or `2^n ± 1`. Signed division → `ASR` (not LSR). `RSB` gives Op2-Rn for `(2^n-1)*B` patterns. Also common: `add r1,r0,r0,lsl #1 = 3*r0`; `add r1,r0,r0,lsl #2 = 5*r0`; `rsb r1,r0,r0,lsl #3 = 7*r0`.

---

### HW7 Problem 4 (10pts) — BIC+ORR to replace a nibble

**Task:** `uint16_t a = 0xH3 H2 H1 H0` → `0xH3 H2 A H0` (set bits[7:4] = 0xA).
**ASM (key lines):**

    ldr   r1, =15
    bic   r0, r0, r1, lsl #4    @ clear bits [7:4]
    ldr   r2, =10
    orr   r0, r0, r2, lsl #4    @ OR in 0xA << 4

C form: `a &= ~(15<<4); a |= (10<<4);`
**Key concept:** BIC-then-ORR is the canonical "assign bit field" idiom. `bic Rd,Rn,Op2` = `Rd = Rn & ~Op2` (no C equivalent — must write `&~mask`).

---

### HW7 Problem 5 (16pts) — BIC / ORR / EOR hand-evaluation

**Task:** R0=0xAD, R1=0x03. Compute BIC, ORR, EOR results.
**ASM (key lines):**

    lsr   r2, r1, #2    @ R2 = 0
    bic   r3, r0, r1    @ 0xAD & ~0x03 = 0xAC
    orr   r4, r3, r1    @ 0xAC | 0x03 = 0xAF
    eor   r5, r0, r1    @ 0xAD ^ 0x03 = 0xAE

**Key concept:** BIC clears bits set in Op2 (mask of bits to kill). ORR sets bits. EOR toggles bits. "Set-clear-toggle" triad.

---

### HW7 Problem 6 (30pts) — Hex-digit manipulation patterns

**Task (a):** Replace H1 with 5. `A &= ~(15<<4); A |= 5<<4;` — same BIC/ORR as P4.
**Task (b):** Shift-left and insert low digit: `H3H2H1H0 → H2H1H0 3`.

    lsl   r0, #4
    orr   r0, #3             @ insert 3 at bottom

**Task (c):** Shift-right and insert top digit: `H3H2H1H0 → 7 H3H2H1`.

    lsr   r0, #4
    ldr   r1, =7
    lsl   r1, #12
    orr   r0, r1             @ insert 7 at top

**Key concept:** To **insert** a digit at an end: `shift the word → ORR the new digit at the vacated position`. To **replace** a digit in-place: BIC the nibble → ORR the new value. No shift-mask needed for (b)/(c) since the shifted-out end is already zero.

---

## HW8 — NZCV, CCS, Conditional Branch (Lctr 18-19)

### HW8 Problem 1 (42pts) — NZCV by hand (5-bit system)

5-bit constants: C_N=32, U_MAX=31, S_MIN=-16, S_MAX=15.
**Procedure per operation:**
1. Unsigned view: convert negatives by +C_N; if result > U_MAX → subtract C_N, **C=1 (add)** or **C=0 (sub borrow)**.
2. Signed view: add directly; if result outside [S_MIN,S_MAX] → **V=1**, correct by ±C_N.
3. N = MSB of binary result; Z = (result==0). Binary result is the **same for both views**.

**Example (-15)+(-5):** unsigned 17+27=44 → -32=12, **C=1**. Signed -20<-16 → +32=12, **V=1**. Result 0b01100, **N=0, Z=0**.

**Example 11-18:** unsigned -7 → +32=25, **C=0** (borrow). Signed 11-(-14)=25>15 → -32=-7, **V=1**. 0b11001, **N=1, Z=0**.

**Key concept:** C and V are set independently and simultaneously — processor doesn't know signed vs unsigned. Always work **two tables** (unsigned→C, signed→V) then combine.

---

### HW8 Problem 2 (40pts) — CMP flags and CCS evaluation

**Task:** After `CMP r0, r1` on a 6-bit system (C_N=64), compute NZCV and evaluate every CCS.
**Key insight:** CMP = `r0 - r1` without writeback. Equal magnitudes (e.g., 22-20 and (-20)-(-22)) produce **identical flags** because `(-20)+64 - ((-22)+64) = 22-20`.

**CCS logic reference (memorize):**

| Suffix | Signed/Unsigned | Logic |
|---|---|---|
| EQ | — | Z==1 |
| NE | — | Z==0 |
| GE | signed | V==N |
| GT | signed | (V==N) && (Z==0) |
| LT | signed | V!=N |
| LE | signed | (V!=N) \|\| (Z==1) |
| HS (CS) | unsigned | C==1 |
| LO (CC) | unsigned | C==0 |
| HI | unsigned | (C==1) && (Z==0) — often written **C!=Z** on flags like N=Z=0,C=1 |
| LS | unsigned | (C==0) \|\| (Z==1) — often **C==Z** |

**Key concept:** After a "clean" compare (Z=0,V=0,C=1,N=0) GE/GT/HI/HS all true, LT/LE/LO/LS all false. CCS is **flag-driven, not value-driven** — two different CMPs with same flags give identical branches.

---

### HW8 Problem 3 (20pts) — Max via negative-logic branch

**Task:** `int max(int a,int b){ return a>=b ? a : b; }`
**ASM (key lines):**

    cmp   r0, r1
    blt   .else            @ NL: branch on !(a>=b) = a<b
    b     .end             @ then: r0 already = a
    .else:
      mov r0, r1           @ r0 = b
    .end:
      bx  lr

**Key concept:** Negative logic = branch on **opposite** CCS to skip to the else block. For `>=` use `blt`. (Quiz4 cheatsheet covers PL vs NL layouts in full — see §7.)

---

### HW8 Problem 4 (30pts) — 64-bit sum of squares with smlal

**Task:** `int64_t sum = 0; for(i=s;i<=e;i++) sum += i*i;` return R1:R0.
**ASM (key lines):**

    ldr   r2, =0                @ sum_lo = 0
    ldr   r3, =0                @ sum_hi = 0
    .lp:
      cmp   r0, r1              @ i vs e
      bgt   .end                @ NL: exit when i>e
      smlal r2, r3, r0, r0      @ {r3:r2} += i*i  (signed 32x32→64 MAC)
      add   r0, #1              @ i++
      b     .lp
    .end:
      mov   r0, r2              @ lo → R0
      mov   r1, r3              @ hi → R1
      bx    lr

**Key concept:** `SMLAL Rlo,Rhi,Rn,Rm` = `{Rhi:Rlo} += Rn*Rm` (signed 64-bit accumulate). Pair with `UMLAL` for unsigned. 64-bit return per EABI: R0=low, R1=high. Reuse the input register for the loop counter to save a callee-saved register.

---

## Key Patterns (exam-relevant idioms)

- **LSL #n = multiply by 2^n; LSR = unsigned /2^n; ASR = signed /2^n.** Pick ASR for signed division — LSR on a negative number gives garbage.
- **Op2 barrel shift is free** — `add/sub/rsb Rd, Rn, Rm, {LSL|LSR|ASR} #n` fuses a shift into the arithmetic. Classic multiplies: `add r1,r0,r0,lsl #1`=3x, `add r1,r0,r0,lsl #2`=5x, `rsb r1,r0,r0,lsl #3`=7x, `sub r0,r0,r0,asr #2`=0.75x.
- **Destination register cannot be omitted when Op2 uses a shifted register** (e.g., `add r0, r1, lsl #3` is illegal — must write `add r0, r0, r1, lsl #3`).
- **S-suffix shift → C = last bit shifted out.** Use this to pluck a single bit into C (e.g., `lsls r0,#1` puts old b31 in C).
- **Bit-field set/clear/toggle:** ORR sets, BIC clears (`Rn & ~Op2`), EOR toggles, MVN = ~Op2. ORN = `Rn | ~Op2` (no C operator).
- **Assign-a-field idiom:** BIC with mask to clear, then ORR with `value << position` to set. Same two-step in C: `a &= ~mask; a |= (v<<s);`.
- **Insert a digit at an end:** shift the word toward that end, then `ORR` the new digit (the vacated nibble is already zero).
- **CMP sets flags like SUB but discards result.** CMN sets flags like ADD but discards (used by `cmp r0,#-5` → assembler emits `cmn r0,#5`).
- **C = !borrow for subtraction** (ARM convention). After `subs`: no borrow → C=1; borrow → C=0. Opposite of x86.
- **V is for signed overflow only; C is for unsigned carry/borrow only.** Processor sets both every add/sub; the programmer decides which to consult via CCS choice.
- **Signed CCS:** GT/GE/LT/LE (uses V==N logic). **Unsigned CCS:** HI/HS/LO/LS (uses C and Z). Matching the C operand type to the CCS is a common exam trap.
- **N-bit result correction:** if unsigned result > 2^N-1 subtract 2^N; if signed result outside [-2^(N-1), 2^(N-1)-1] add/subtract 2^N. Final binary pattern is identical for both views.
- **SMLAL / UMLAL:** `{Rhi:Rlo} += Rn*Rm` (signed/unsigned). Essential for 64-bit accumulators. Pair with EABI: R0=lo, R1=hi on return.
- **Negative-logic branch** = branch on the **opposite** CCS of the C test to skip the then-block. Reads closer to the source C than positive logic.
