# CEC 320 — Quiz 4 Prep Topics

Quiz 4 covers **HW 9, 10, 11, 12** — load/store, pointers, function calls, conditional execution, if-based flow control, and loops. Scope = **Lectures 20–26** (with possible spillover from Lctr 19 / Lctr 27).

> "Just a reminder that you can use your own formula sheets for Qz 4. Ideally, you use ONE new piece of letter-sized paper for the new contents covered by HWs 9–12. You can also use the pieces of paper you used for the previous QZes. You need to write down the commonly used ASM instructions we have learned in class on your formula sheet. No creation of fake instructions is allowed."

---

## Topics to Understand (with Lecture Anchors)

### HW 9 — LDR and STR Instructions

**Lecture 20: Immediate-Offset Load and Store**
- Three addressing modes (basic, pre-index `!`, post-index).
- Data-type suffixes: none / `B` / `SB` / `H` / `SH` for load; only `B` / `H` / (none) for store.
- Sign vs zero extension on load (byte 0x80 → 0xFFFFFF80 with LDRSB).
- Little-endian byte assembly into 32-bit words.
- C → ASM pointer idioms: `*(p+k)`, `*p++`, `*++p`, `*p--`, `*--p`.

**Lecture 21: Register-Offset Load and Store, MOV**
- `LDR Rv, [Ra, Ri, LSL #2]` = array index for 32-bit elements.
- Shift amount matches element size: `LSL #2` (word), `LSL #1` (halfword), no shift (byte).
- `MOV` / `MOVW` / `MOVT` / `LDR Rd, =expr` — when each is used.
- No pre/post-index version of register-offset.

### HW 10 — C Pointers, LDR/STR, and Function Call

**Lecture 22: Increment Ops for C Variables and Pointers**
- Precedence: postfix `++` (level 1, LTR) vs prefix `++`/`*`/`(cast)` (level 2, RTL).
- Prefix vs postfix on a value: when you use new value vs. old.
- Combination expressions: `*p++`, `*++p`, `++*p`, `++*p++`.
- Pointer arithmetic step size = `sizeof(element)`.
- Cast-and-step: `((uint16_t*)p + i)` multiplies by 2, not 4.

**Lecture 23: Calling ASM from ASM**
- EABI review: R0–R3 = args / return; R4–R11 callee-saved; LR saved in stem fns.
- `BL target` sets LR = PC_next, then jumps.
- Leaf vs stem function distinction.
- `LDRD` / `STRD` for 64-bit args/returns — pre-/post-index forms exist, no register-offset.
- Preparing arguments in R0–R3 using the right LDR variant for each type.

### HW 11 — If-Based Flow Control

**Lecture 24: Combination Branching and Conditional Execution**
- `CBZ Rn, label` / `CBNZ Rn, label` — Rn in R0–R7, forward branch only, no flag effects.
- Conditional execution: any instruction can take a CCS suffix.
- `IT{T/E}{T/E}{T/E} cond` — up to 4 conditional instructions in one block.
- Rules: first slot = T = cond; E = inverse of cond.
- Only last IT slot can be a conditional branch. CBZ/CBNZ forbidden inside IT.

**Lecture 25: Selection Control (If-Based Flow Control)**
- Basic `if`, `if-else`, `if-else-if-else` in C.
- PL (positive logic) vs NL (negative logic) layouts — both produce same result.
- CEX approach using IT blocks for single/multi-instruction branches.
- Compound tests with `&&` and `||` — short-circuit double-CMP pattern.
- De Morgan's law for converting AND ↔ OR compound conditions.

### HW 12 — Loops

**Lecture 26: Implementing C's Loops in ASM**
- `for` / `while` / `do-while` — all three translations.
- Standard ASM shape: `_lp:` label, test, body, `b _lp`, `_end:`.
- Priming read + in-loop read for `while (cond)` with `cond` depending on a loaded value.
- Using `CBZ` to exit on a null byte (replaces `cmp r0, #0` / `beq`).
- Loop with function call (stem fn pattern from Lctr 23).

**Lecture 27 (peripheral): Complex Flow Control**
- `while (1) { ... break; }` idiom to remove priming-read duplication.
- `break` = forward branch to loop's `_end` label.
- `continue` = backward branch to `_lp` (while/do-while) or update step (for).
- `switch` — naive CMP/BEQ ladder vs. `ADR` + `TBB` table dispatch.

---

## Sample Problem Set

These 6 problems simulate the style of the HW 9–12 questions. Work them on paper before looking at the solutions section at the bottom.

---

### Problem 1 — LDR/STR Trace (HW 9 style)

Given 16 bytes at 0x2000_0200 with values `byte_i = 2*i + 3` for i = 0..15, and the following assembly runs sequentially:

    ldr    r4, =0x20000200     @ (1)
    ldrh   r0, [r4, #6]         @ (2)
    ldrsb  r1, [r4, #5]!        @ (3)
    ldr    r2, [r4], #4         @ (4)
    ldrsh  r3, [r4]             @ (5)

Determine:
(a) R0 and R4 after instruction (2).
(b) R1 and R4 after instruction (3).
(c) R2 and R4 after instruction (4).
(d) R3 after instruction (5).

---

### Problem 2 — C Pointer Decoding from ASM (HW 10 style)

Given the following ASM function:

    my_task:
        ldrsh  r2, [r0, #4]
        str    r2, [r1], #4
        ldrsh  r2, [r0, #8]!
        str    r2, [r1, #0]
        bx     lr

(a) Write the function prototype.
(b) Give a calling example using `int16_t *p16s = arr_s;` and `int32_t *p32 = arr_32;`.
(c) Write equivalent C code (using temporary pointers if needed to preserve `arr_s`/`arr_32`).

---

### Problem 3 — Increment and Pointer Ops (HW 10 P1 style)

Given:

    uint8_t A[4] = { 0x10, 0x20, 0x30, 0x40 };
    uint8_t *pA = A;
    uint8_t *pB = &A[0];

Translate each line into the minimum-instruction ASM (using `r0` = `pA`, `r1` = `pB`, `r2` = scratch):

(a) `*pB++ = *(pA + 1);`
(b) `*pB++ = ++*(pA + 2);`
(c) `*pB++ = *pA++;`
(d) `*pB = ++*pA++;`

Also identify which memory addresses (relative to A) get modified by each RHS.

---

### Problem 4 — If-Else with Pointers (HW 11 style, three variants)

Given:

    uint32_t cond_load(int x, uint32_t *ptrA, uint16_t *ptrB) {
        if (x <= 10) {
            return *++ptrA * 4;
        } else {
            return (uint32_t)*ptrB++ / 2;
        }
    }

(a) Write ASM using **Positive Logic** (PL). Use `BLE` or `BGT` as appropriate.
(b) Write ASM using **Negative Logic** (NL).
(c) Write ASM using the **CEX** approach with `ITTEE`. Identify which CCS each slot needs.

---

### Problem 5 — If-Else-If with Compound Test (HW 11 P2/P3 style)

Given:

    int piecewise_c(int x) {
        if (x < -10 || x > 50) return 0;
        else if (x <= 10) return x << 1;
        else return x >> 1;
    }

(a) Write the C function as a clean if-else-if chain (rewrite using only if-else-if).
(b) Translate to ASM using the CMP approach with a short-circuit `OR` for the first compound.
(c) Is this a signed or unsigned comparison? Which CCSs do you use?

---

### Problem 6 — Loop with Function Call (HW 12 + Lctr 23 style)

Given the leaf function already exists:

    @ uint32_t mp_max2_s(uint32_t a, uint32_t b) — returns larger of a, b
    @ a → r0, b → r1, return → r0

Write `mp_arr_max_s`, the stem function matching this C prototype, in ASM:

    uint32_t mp_arr_max_s(uint32_t *arr, int n);

that returns the maximum element of `arr[0..n-1]` (assume n ≥ 1). Use `BL mp_max2_s` inside your loop. Follow the stem-function template (push/pop, save args to callee-saved regs).

---

### Problem 7 — While Loop with CBZ (HW 12 P1 style)

Write the C function and its ASM:

    int mp_count_letter_in_str_c(char *str, char target);

returns the number of occurrences of `target` in the null-terminated string `str`. Use `while (1) { ... break; }` in C; use `ldrb`/`cbz` and `cmp`/`beq` in ASM. Uses only scratch registers.

---

## Answers / Solution Sketches

### Problem 1 Answers

Bytes at 0x2000_0200: `byte_i = 2i+3` → `0x03, 0x05, 0x07, 0x09, 0x0B, 0x0D, 0x0F, 0x11, 0x13, 0x15, 0x17, 0x19, 0x1B, 0x1D, 0x1F, 0x21`.

(a) `ldrh r0, [r4, #6]` — halfword at 0x206..207: bytes 0x0F, 0x11 → `r0 = 0x0000110F`. R4 unchanged = 0x20000200.

(b) `ldrsb r1, [r4, #5]!` — R4 += 5 → 0x20000205, then load byte at [R4] = 0x0D. MSB = 0, zero-extend → `r1 = 0x0000000D`. R4 = 0x20000205.

(c) `ldr r2, [r4], #4` — word at 0x205..208: bytes 0x0D, 0x0F, 0x11, 0x13 → `r2 = 0x13110F0D`. Then R4 = 0x20000209.

(d) `ldrsh r3, [r4]` — halfword at 0x209..20A: bytes 0x15, 0x17 → 0x1715. MSB bit 15 = 0, zero-extend → `r3 = 0x00001715`.

---

### Problem 2 Answers

(a) **Prototype:** `void my_task(int16_t *pSrc, int32_t *pDst);`
(b) **Call:** `my_task(p16s, p32);`
(c) **Equivalent C** (preserving caller state):

    int16_t *s = p16s;
    int32_t *d = p32;
    *d = (int32_t)*(s + 2);        // *(s+2) is signed halfword at offset 4 bytes
    d++;                             // store advanced d by 4
    s += 4;                          // pre-index #8 = 4 * sizeof(int16_t)
    *d = (int32_t)*s;                // *(s+4)

Note: the first `str r2, [r1], #4` is post-index (advance after store), the second `ldrsh r2, [r0, #8]!` is pre-index (advance before load).

---

### Problem 3 Answers

(a) `*pB++ = *(pA + 1);` (no value-modification on RHS)

    ldrb   r2, [r0, #1]
    strb   r2, [r1], #1

(b) `*pB++ = ++*(pA + 2);` (modifies `A[2]` from 0x30 → 0x31)

    ldrb   r2, [r0, #2]
    add    r2, #1
    strb   r2, [r0, #2]       @ write back incremented value
    strb   r2, [r1], #1

(c) `*pB++ = *pA++;` (no memory modification on RHS)

    ldrb   r2, [r0], #1
    strb   r2, [r1], #1

(d) `*pB = ++*pA++;` (pA++ returns old pA, `*old_pA` incremented in memory)

    ldrb   r2, [r0], #1
    add    r2, #1
    strb   r2, [r0, #-1]      @ write incremented value back to old pA addr
    strb   r2, [r1]            @ no pB++ (no ++ on pB)

---

### Problem 4 Answers

Register map: `r0 = x`, `r1 = ptrA` (`uint32_t *`), `r2 = ptrB` (`uint16_t *`). Return in `r0`. Signed `x ≤ 10` → CCS `LE` / `GT`.

**(a) Positive Logic (PL):** branch to `then` on C-true (`BLE`).

    cond_load_pl:
        cmp    r0, #10
        ble    pl_then
    pl_else:
        ldrh   r0, [r2], #2      @ *ptrB++ (pre advance? No — postfix → post)
        lsr    r0, r0, #1         @ / 2 (unsigned since ptrB is uint16_t*)
        b      pl_end
    pl_then:
        ldr    r0, [r1, #4]!     @ *++ptrA
        lsl    r0, r0, #2         @ * 4
    pl_end:
        bx     lr

**(b) Negative Logic (NL):** branch to `else` on C-false (`BGT`).

    cond_load_nl:
        cmp    r0, #10
        bgt    nl_else
    nl_then:
        ldr    r0, [r1, #4]!
        lsl    r0, r0, #2
        b      nl_end
    nl_else:
        ldrh   r0, [r2], #2
        lsr    r0, r0, #1
    nl_end:
        bx     lr

**(c) CEX with ITTEE:** Use `LE` so T slots = then-branch, E slots = else-branch.

    cond_load_cex:
        cmp    r0, #10
        ittee  le                  @ T,T = le (then) ; E,E = gt (else)
        ldrle  r0, [r1, #4]!      @ T1: ptrA++; r0 = *ptrA
        lslle  r0, r0, #2          @ T2: r0 * 4
        ldrhgt r0, [r2], #2        @ E1: r0 = *ptrB; ptrB++
        lsrgt  r0, r0, #1          @ E2: r0 / 2
        bx     lr

---

### Problem 5 Answers

(a) Rewrite with only `if-else-if-else`:

    int piecewise_c(int x) {
        if (x < -10) return 0;
        else if (x > 50) return 0;
        else if (x <= 10) return x << 1;
        else return x >> 1;
    }

or using a compound OR:

    int piecewise_c(int x) {
        if (x < -10 || x > 50) return 0;
        else if (x <= 10) return x << 1;
        else return x >> 1;
    }

(b) ASM (signed `x`, `r0 = x`):

    piecewise_s:
        cmp    r0, #-10              @ assembles as CMN r0, #10
        blt    return_zero           @ first OR branch: x < -10
        cmp    r0, #50
        bgt    return_zero           @ second OR branch: x > 50
        cmp    r0, #10
        ble    shift_left            @ x <= 10 → return x << 1
        asr    r0, r0, #1             @ else return x >> 1 (signed!)
        bx     lr
    shift_left:
        lsl    r0, r0, #1
        bx     lr
    return_zero:
        ldr    r0, =0
        bx     lr

(c) **Signed** — `x` is `int`. Use `LT`, `GT`, `LE` (not `LO`/`HI`/`LS`). Also use `ASR` (signed shift) not `LSR` for the `x >> 1`.

---

### Problem 6 Answer

    @ uint32_t mp_arr_max_s(uint32_t *arr, int n)
    @ r0 = arr, r1 = n
    @ r4 = arr (saved), r5 = n (saved), r6 = max_so_far, r7 = i
    mp_arr_max_s:
        push    {r4-r7, lr}
        mov     r4, r0                  @ save arr
        mov     r5, r1                  @ save n
        ldr     r6, [r4]                @ max = arr[0]
        mov     r7, #1                  @ i = 1
    lp:
        cmp     r7, r5
        bge     end_loop
        ldr     r0, [r4, r7, lsl #2]   @ arg0 = arr[i]
        mov     r1, r6                  @ arg1 = max_so_far
        bl      mp_max2_s
        mov     r6, r0                  @ max_so_far = ret
        add     r7, #1
        b       lp
    end_loop:
        mov     r0, r6                  @ return max
        pop     {r4-r7, pc}

---

### Problem 7 Answer

**C (while-1 + break):**

    int mp_count_letter_in_str_c(char *str, char target) {
        int count = 0;
        while (1) {
            char ch = *str++;
            if (ch == 0) break;
            if (ch == target) count++;
        }
        return count;
    }

**ASM** (r0 = str, r1 = target, r12 = count):

    @ int mp_count_letter_in_str_s(char *str, char target)
    mp_count_letter_in_str_s:
        mov     r12, #0
    lp:
        ldrb    r2, [r0], #1           @ ch = *str++
        cbz     r2, end                 @ if (ch == 0) break
        cmp     r2, r1                  @ ch == target?
        bne     skip
        add     r12, r12, #1
    skip:
        b       lp
    end:
        mov     r0, r12                 @ return count
        bx      lr

(Optional CEX-style tweak: replace the `cmp`/`bne`/`add` with `cmp r2,r1 ; it eq ; addeq r12, #1`.)
