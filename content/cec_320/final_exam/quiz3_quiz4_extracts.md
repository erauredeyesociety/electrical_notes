# Quiz 3 & Quiz 4 Extracts (CEC 320 Final Prep)

Extracted problems + accepted solutions from Fall-2025 quizzes. Source PDFs in `content/cec_320/quizes/quiz3/` and `quiz4/`.

---

## Quiz 3 — ASM programming in C (qz4b)

### Q3 P1 (7pts) — Return register for signed int32

**Given:** An ASM function returns a signed 32-bit value of -2.
**Solution:**
    (a) Return register = R0.
    (b) R0 = 0xFFFF_FFFE  (two's complement of -2).
**Key pattern:** AAPCS: R0 holds 32-bit return values; signed negatives become the two's complement hex. Trap: writing 0x8000_0002.

### Q3 P2 (20pts) — 64-bit add and the C flag

**Given:** `mp_add_64bit_s` does `adds r0,r2; adc r1,r3`; tests use `A = 0x377<<24`, `B = 0x287<<24` (set 1), `0x378<<24`, `0x288<<24` (set 2).
**Solution:**
    A1+B1 = (int64_t)0x5FE << 24    -> C flag = 0 (low add did not overflow)
    A2+B2 = (int64_t)0x600 << 24    -> C flag = 1 (low 32 bits carried into high)
**Key pattern:** 64-bit ADD tests must be designed so the low word overflows (C=1) AND doesn't (C=0) to cover `adc`. Just shift the low-nibble into the MSB of the low word.

### Q3 P3 (20pts) — Push {r4, r8, r6} on descending-full stack

**Given:** Ri = (1<<i)+(1<<(2+i)); SP = 0x2000_1020 before push; `push {r4, r8, r6}`.
**Solution:**
    SP after   = 0x2000_1014          (3 regs x 4 = 12 off)
    R4         = (1<<4)+(1<<6) = 0x0000_0050
    word@1018  = R6 = (1<<6)+(1<<8) = 0x0000_0140
    byte@1019  = second byte of R6  = 0x01
**Key pattern:** `push {list}` ALWAYS writes in ascending register-number order regardless of list syntax (R4 lowest addr, R8 highest). Addr layout: R4@1014, R6@1018, R8@101C.

### Q3 P4 (25pts) — Barrel shifter mul/div by 8

**Given:** Signed A in r0, B in r1. Write single-line Op2 instruction for A = k*B/8.
**Solution:**
    (a) A = 6*B/8:   sub r0, r1, r1, asr #2    ; B - B/4
    (b) A = 7*B/8:   sub r0, r1, r1, asr #3    ; B - B/8
    (c) A = 8*B/8:   mov r0, r1                ; or add r0, r1, #0
    (d) A = 9*B/8:   add r0, r1, r1, asr #3    ; B + B/8
    (e) A = 10*B/8:  add r0, r1, r1, asr #2    ; B + B/4
**Key pattern:** Factor k/8 as 1 +/- 1/2^n so it becomes one ADD/SUB with ASR-shifted Op2. Use ASR (not LSR) because B is signed.

### Q3 P5 (20pts) — bic/and/orr bitfield splice to C

**Given:** ASM uses mask=15, clears bits[11:8] of a, then inserts low 4 bits of b into [11:8].
**Solution:**
    uint16_t func_c(uint16_t a, uint16_t b) {
        uint16_t mask = 15;
        a &= ~(mask << 8);
        a |= (b & mask) << 8;
        return a;
    }
    With a=0xH3H2H1H0, b=17=0x11: result = 0xH3 1 H1 H0  (nibble H2 replaced by 1).
**Key pattern:** Recognize `bic ... LSL` + `orr ... LSL` as the canonical "clear-then-insert" bitfield splice. 17 = 0x11, low nibble = 1.

### Q3 P6 (8pts) — int8_t to int32_t sign extension in args

**Given:** `int8_t var1=0x7E, var2=0x81; fn(var1,var2)` where fn takes int32_t args.
**Solution:**
    R0 = 0x0000_007E   (0x7E positive, zero-extended)
    R1 = 0xFFFF_FF81   (0x81 is -127 as int8_t, sign-extended)
**Key pattern:** Sign-extension happens at the call site per AAPCS. A byte >= 0x80 becomes 0xFFFF_FFxx in the arg register.

---

## Quiz 4 — CCS + conditional branch + LDR/STR (qz-25b-qz5)

### Q4 P1 (20pts) — if/else selector in ASM

**Given:** C: `int mp_selector(int a,int x,int y){ if(a>=0) return x; else return y; }`
**Solution:**
    mp_selector:            @ a->r0, x->r1, y->r2, return r0
        cmp     r0, #0
        blt     mp_selector_else
        mov     r0, r1
        bx      lr
    mp_selector_else:
        mov     r0, r2
        bx      lr
**Key pattern:** Standard compare-and-branch idiom. `blt` is signed less-than (because int). Fall-through handles the then-branch; no push/pop since nothing is preserved.

### Q4 P2 (30pts) — NZCV on 5-bit system

**Given:** 5-bit ARM conventions: CN=32, SMIN=-16, SMAX=15. Compute (-15)-(-16) and 16-18.
**Solution:**
    (-15)-(-16): unsigned: 17-16=1 in range -> result=1, B=0 => C=1, Z=0
                 signed:   1 in [-16,15] -> V=0, N=0; binary=0b00001
    16-18:       unsigned: -2 not in range -> result=-2+32=30, B=1 => C=0, Z=0
                 signed:   -16-(-14)=-2 in range -> V=0, N=1; binary=0b11110
**Key pattern:** ARM subtract flag rule: C = NOT Borrow. For unsigned use x+CN map; for signed use x-CN map when MSB=1. V=0 when signed temp is in [SMIN,SMAX].

### Q4 P3 (50pts) — LDR/STR pre-/post-indexing + scaled offset

**Given:** memory at 0x2000_0000..000F filled with 0x80..0x87, 0x78..0x7F. `task1` uses `[r0,#4]!` twice; `task2` uses `[r0],#8` then `[r0, r2, lsl #2]`. Called as `task1(0x20000000, 0x20000020)`, `task2(0x20000000, 0x20000030, -1)`.
**Solution:**
    task1: r2 = *[0x2000_0004] = 0x8786_8584;  r3 = *[0x2000_0008] = 0x7B7A_7978
    task2: r0 after postinc = 0x2000_0008; r3 = *[0x2000_0000] = 0x8382_8180
           then r3 = *[0x2000_0008 + (-1)*4] = *[0x2000_0004] = 0x8786_8584
    Mem@0x2000_0030: bytes 0x80 0x81 0x82 0x83 0x84 0x85 0x86 0x87  (from task1 stores)
    Prototypes: void task1(int *p1,int *p2);  void task2(int *p1,int *p2,int n);
    task1_c:  *p2 = *++p1;  *(p2+1) = *++p1;
**Key pattern:** Pre-index `[Rn,#off]!` updates Rn BEFORE load; post-index `[Rn],#off` updates AFTER. Scaled `[r0, r2, lsl #2]` uses signed r2 as word index (-1 -> -4 bytes). ARM pointer arith is in bytes but C pointer arith (`++p1` on int*) is in sizeof(int).

---

## Quiz 6a — pointer / flow-ctrl in ASM (worksheet only, no soln PDF)

### Q6a P1 (45pts) — ldrd/strd + ldrsb pre-indexed copy

**Given:** `uint8_t ipt[20]` filled `ipt[i]=0x70+(i<<2)` (i.e. 0x70,0x74,0x78,...,0xBC). `task_a` does: `ldrd r2,r3,[r0,#8]!`, `strd r2,r3,[r1,#0]`, then two `ldrsb r?,[r0,#4]!`, `strd r2,r3,[r1,#8]`.
**Solution (derived):**
    After ldrd from ipt+8: r2 = 0x7C7884+... little-endian word at ipt[8..11] = 0x8884807C; r3 = word at ipt[12..15]
      r2 = 0x8884807C  (bytes 0x7C 0x80 0x84 0x88 -> little endian)  ... actually 0x88848 0x7C
      Correcting: ipt[8]=0x90, ipt[12]=0xA0 (0x70+(8<<2)=0x70+32=0x90; 0x70+(12<<2)=0x70+48=0xA0)
      r2 = 0x9C989490,  r3 = 0xACA8A4A0
    Then ldrsb at ipt[16]=0xB0 -> r2 = 0xFFFF_FFB0 (sign-extend);  ldrsb at ipt[20? out of bounds conceptually but ipt[20]=beyond; if extended ipt[20]= 0x70+80=0xC0] r3 = 0xFFFF_FFC0
    opt[0]=r2,opt[1]=r3,opt[2]=signed ipt[16],opt[3]=signed ipt[20]
    R0 just before bx = &ipt[20];  R1 = &opt[0] (strd didn't auto-update r1)
**Key pattern:** `ldrd/strd` needs even-odd reg pair, loads 8 bytes (2 words). `ldrsb` sign-extends a byte to 32 bits (>0x7F becomes 0xFFFF_FFxx). Pre-index `!` updates base; plain offset doesn't.

### Q6a P2 (20pts) — saturate to [-5,5] in ASM

**Given:** C: clamp x to [-5,5].
**Solution:**
    math_fun_s:        @ x->r0
        cmp     r0, #-5
        blt     .clamp_lo
        cmp     r0, #5
        bgt     .clamp_hi
        bx      lr
    .clamp_lo: mov r0, #-5
               bx  lr
    .clamp_hi: mov r0, #5
               bx  lr
**Key pattern:** Two compares and two exit branches. Alternatively use IT blocks. Signed comparisons (`blt`/`bgt`) are required.

### Q6a P3 (35pts) — sum of negative elements

**Given:** `int mp_neg_sum_array(int *arr, int N)` — sum only arr[i] < 0.
**Solution:**
    C:  int s=0; for(int i=0;i<N;i++) if(arr[i]<0) s+=arr[i]; return s;
    ASM:                 @ arr->r0, N->r1, sum->r2, i->r3, tmp->r12
        mov     r2, #0
        mov     r3, #0
    .loop:
        cmp     r3, r1
        bge     .done
        ldr     r12, [r0, r3, lsl #2]
        cmp     r12, #0
        bge     .skip
        add     r2, r2, r12
    .skip:
        add     r3, r3, #1
        b       .loop
    .done:
        mov     r0, r2
        bx      lr
**Key pattern:** Standard array-loop template: index counter, bound-compare at top, scaled `[r0, ri, lsl #2]` for int*, conditional skip, return via r0. Drill this until automatic.

---

## Exam-trap patterns seen in previous quizzes

- Sign extension on sub-word args: `int8_t` >= 0x80 becomes `0xFFFF_FFxx` in the 32-bit arg register (Q3 P6). Same rule for `ldrsb`/`ldrsh` (Q6a P1).
- `push {list}` writes regs in ascending register-number order regardless of list syntax; lowest reg# lands at lowest address (Q3 P3).
- 64-bit `adds`/`adc` test cases must exercise both C=0 and C=1 on the low word — pick operands whose low 32 bits sum crosses 2^32 (Q3 P2).
- Barrel-shifter mul/div: rewrite k/8 as 1 +/- 1/2^n and collapse to ONE `add/sub/rsb Rd, Rn, Rn, ASR #n`. Use ASR for signed (Q3 P4).
- `bic` + `orr` with matching `LSL #n` is the "clear-field then insert" idiom: translates to `a &= ~(mask<<n); a |= (b & mask)<<n;` (Q3 P5).
- Pre-index `[Rn,#off]!` updates base BEFORE access (like `*++p`); post-index `[Rn],#off` updates AFTER (like `*p++`). Scaled `[Rn, Rm, lsl #2]` treats Rm as signed word index (Q4 P3).
- 5-bit NZCV: ARM sets C = NOT Borrow on SUB. Map unsigned/signed decimal via +/- CN then test range to get C/V; Z from zero-ness; N from MSB of result (Q4 P2).
- Array-sum-with-condition pattern: init sum=0 + i=0, loop-top bound compare, `ldr r?, [base, i, lsl #2]`, predicate compare, conditional skip, increment, branch (Q6a P3).
