# CEC 320 Homework Solutions Summary (Quiz 4)

Consolidated summary of HW 9, 10, 11, and 12 solutions for quiz preparation.

---

## HW 9: LDR and STR Instructions (160 pts total)

### Problem 1 (40 pts) — LDR addressing-mode trace

16 bytes at 0x2000_0000 = 0..15 (0x00..0x0F). Memory map (little-endian):

| Addr         | B0   | B1   | B2   | B3   |
|--------------|------|------|------|------|
| 0x20000000   | 0x00 | 0x01 | 0x02 | 0x03 |
| 0x20000004   | 0x04 | 0x05 | 0x06 | 0x07 |
| 0x20000008   | 0x08 | 0x09 | 0x0A | 0x0B |
| 0x2000000C   | 0x0C | 0x0D | 0x0E | 0x0F |

| Instr | Mode | After |
|-------|------|-------|
| `ldr r4, =0x20000000` | pseudo | R4 = 0x20000000 |
| `ldr r0, [r4, #4]` | basic | R0 = 0x07060504, R4 unchanged |
| `ldr r1, [r4, #2]!` | pre-index | R4 = 0x20000002, R1 = 0x05040302 |
| `ldr r2, [r4], #4` | post-index | R2 = 0x05040302, R4 = 0x20000006 |
| `ldr r3, [r4]` | basic | R3 = 0x09080706 |

**Key concept:** `[Ra, #os]!` updates Ra before load; `[Ra], #os` updates after.

---

### Problem 2 (40 pts) — Reverse-engineer two ASM functions

**mp_task1:**

    ldrsh r2, [r0], #4    @ *p32 = (int32_t)*p16s (sign-ext), then p16s += 2 elements
    str   r2, [r1, #0]
    ldrsh r3, [r0], #4
    str   r3, [r1, #4]

- Prototype: `void mp_task1(int16_t *pSrc, int32_t *pDst);`
- Call: `mp_task1(p16s, p32);`
- C: `*p32 = (int32_t)*p16s; p16s += 2; *(p32+1) = (int32_t)*p16s; p16s += 2;`
- LDRSH with `#4` post-index → skips every **other** halfword.

**mp_task2:**

    ldrh  r2, [r0, #2]!   @ p16u += 1 (pre-index 2 bytes); *p32 = (int32_t)*p16u
    str   r2, [r1, #0]
    ldrh  r3, [r0, #2]!
    str   r3, [r1, #4]

- Prototype: `void mp_task2(uint16_t *pSrc, int32_t *pDst);`
- C: `p16u++; *p32 = (int32_t)*p16u; p16u++; *(p32+1) = (int32_t)*p16u;`
- LDRH with `#2` pre-index → reads consecutive halfwords, skipping the first.

---

### Problem 3 (80 pts) — Four tasks, register state tracking

`ipt[i] = i << 4` → bytes 0x00, 0x10, 0x20, ... 0xF0. 32-bit words at offsets:
- ipt+0 = 0x30201000
- ipt+4 = 0x70605040
- ipt+8 = 0xB0A09080
- ipt+12 = 0xF0E0D0C0

| Task | ASM highlights | Printout | Final R0/R1/R2/R3 |
|------|----------------|----------|-------------------|
| 1 | basic offsets `#4` and `#0xC` | Out1=0x70605040, Out2=0xF0E0D0C0 | (no change) |
| 2 | pre-index `#4`! (×2) | Out1=0x70605040, Out2=0xB0A09080 | R0 = 0x20001018, R1 unchanged |
| 3 | post-index `#4` (×2) | Out1=0x30201000, Out2=0x70605040 | R0 = 0x20001018 |
| 4 | `[r0, r2, lsl #2]` (array index) with r2=1 | Out1=0x70605040, Out2=0xB0A09080 | R2=0x3, R3=0xB0A09080 |

C equivalents (all use `int32_t *p = (int32_t *)ipt`):

- Task 1: `opt[0] = p[1]; opt[1] = p[3];`
- Task 2: `p++; opt[0] = *p; p++; opt[1] = *p;`
- Task 3: `opt[0] = *p; p++; opt[1] = *p; p++;`
- Task 4: `int i=1; opt[0] = p[i]; i++; opt[1] = p[i]; i++;`

**Key concept:** register-offset `[r0, r2, lsl #2]` implements typed-pointer array indexing (offset = 4*i for 32-bit elements).

---

## HW 10: C Pointers + LDR/STR + Function Call (134 pts total)

### Problem 1 (60 pts) — Increment/decrement trace and ASM

`uint8_t *p8a = 0x20000100` (pointing at 0x00, 0x02, 0x04, 0x06, ...). `p8b = 0x2000010C`.

Lines:

    *p8b++ = *(p8a + 2);        // Line 4
    *p8b++ = ++*(p8a + 4);      // Line 5
    *p8b++ = ++*p8a++;           // Line 6
    *p8b++ = *p8a++;             // Line 7

**Part 1 (RHS memory writes):**

| Line | Addr changed | Old → New |
|------|-------------|-----------|
| 4 | (none — pure read) | — |
| 5 | 0x20000104 | 0x08 → 0x09 |
| 6 | 0x20000100 | 0x00 → 0x01 |
| 7 | (none) | — |

**Part 2 (4 bytes written at 0x2000_010C..0F):**

| Addr | Value |
|------|-------|
| 0x2000010C | 0x04 |
| 0x2000010D | 0x09 |
| 0x2000010E | 0x01 |
| 0x2000010F | 0x02 |

**Part 3 (ASM of the four lines):**

    @ Line 4: *p8b++ = *(p8a + 2);
    ldrb   r2, [r0, #2]
    strb   r2, [r1], #1

    @ Line 5: *p8b++ = ++*(p8a + 4);
    ldrb   r2, [r0, #4]
    add    r2, r2, #1
    strb   r2, [r0, #4]       @ write back incremented value to memory
    strb   r2, [r1], #1

    @ Line 6: *p8b++ = ++*p8a++;
    ldrb   r2, [r0], #1       @ r2 = *p8a, p8a++
    add    r2, r2, #1
    strb   r2, [r0, #-1]      @ write back to original p8a address
    strb   r2, [r1], #1

    @ Line 7: *p8b++ = *p8a++;
    ldrb   r2, [r0], #1
    strb   r2, [r1], #1

**Key concept:** Prefix `++` on a dereferenced value requires a write-back STRB after the ADD. Postfix `++` on a pointer uses post-index addressing.

---

### Problem 2 (74 pts) — Four tasks with register-state tracking

Same `ipt[i] = i << 4` array as HW 9 P3.

**Task 1:** `ldrd r2, r3, [r0, #8]!` / `strd r2, r3, [r1, #0]`
- Pre-index #8 → load from ipt+8 (word pair = 0xB0A09080 and 0xF0E0D0C0).
- Out1 = 0xB0A09080, Out2 = 0xF0E0D0C0.

**Task 2:** `ldrsb r2, [r0, #4]!` / `ldrsb r3, [r0, #4]!` / `strd r2, r3, [r1, #0]`
- Pre-index #4 (×2) → reads byte at ipt+4 (0x40 → r2=0x00000040) and ipt+8 (0x80 → r3=0xFFFFFF80, sign-extended!).
- Out1 = 0x40, Out2 = 0xFFFFFF80.
- R0 = 0x20001018, R1 unchanged.

**Task 3:** `ldrsh r2, [r0], #10` / `ldrsh r3, [r0], #4` / `strd r2, r3, [r1, #0]`
- Post-index #10 → load halfword at ipt+0 (0x1000 → r2=0x00001000), then r0 += 10.
- Post-index #4 → load halfword at ipt+10 (0xB0A0 → r3=0xFFFFB0A0, sign-extended).
- Out1 = 0x1000, Out2 = 0xFFFFB0A0. R0 = 0x2000101E.

**Task 4:** `ldrh r3, [r0, r2, LSL #1]` (register-offset, r2 starts at 1)
- r2=1 → addr = ipt+2 → halfword 0x3020 → r3=0x00003020
- r2=2 → addr = ipt+4 → halfword 0x5040 → r3=0x00005040
- Out1 = 0x3020, Out2 = 0x5040. R2=3, R3=0x5040.

C equivalents: see `hw10_solutions.md` — all use typed temporary pointers, e.g. `int16_t *iptr3 = (int16_t *)ipt`.

**Key concepts:**
- LDRD loads 8 bytes with writeback when `!` present.
- LDRSB sign-extends byte → 0x80 becomes 0xFFFFFF80.
- LDRSH sign-extends halfword → 0xB0A0 becomes 0xFFFFB0A0.
- LDRH zero-extends → 0x3020 stays 0x00003020.

---

## HW 11: If-Based Flow Control (140 pts total)

### Problem 1 (40 pts) — Three styles of the same if-else

C function:

    int32_t x_cmp_y_load(int32_t x, int32_t y, int16_t *ptrA, int32_t *ptrB) {
        if (x > y) return (int32_t)*(++ptrA) * 2;
        else return *(ptrB++) / 2;
    }

Registers: r0=x, r1=y, r2=ptrA (`int16_t *`), r3=ptrB (`int32_t *`). Signed comparison (`GT`/`LE`), signed divide (`ASR`).

**Key translations:**
- `*(++ptrA)` = pre-index on 16-bit signed: `ldrsh r0, [r2, #2]!`
- `*2` = `lsl r0, r0, #1`
- `*(ptrB++)` = post-index on 32-bit: `ldr r0, [r3], #4`
- `/2` signed = `asr r0, r0, #1`

**Part 1 — Positive Logic (BGT):** branches to `_then` on C-true.

    cmp    r0, r1
    bgt    pl_then           @ same as C test (x > y)
pl_else:
    ldr    r0, [r3], #4
    asr    r0, r0, #1
    b      pl_end
pl_then:
    ldrsh  r0, [r2, #2]!
    lsl    r0, r0, #1
pl_end:
    bx     lr

**Part 2 — Negative Logic (BLE):** branches to `_else` on C-false.

    cmp    r0, r1
    ble    nl_else           @ opposite of x > y
nl_then:
    ldrsh  r0, [r2, #2]!
    lsl    r0, r0, #1
    b      nl_end
nl_else:
    ldr    r0, [r3], #4
    asr    r0, r0, #1
nl_end:
    bx     lr

**Part 3 — CEX (ITTEE le):** 2 inst per branch.

    cmp    r0, r1
    ittee  le                @ T=le=else, E=gt=then
    ldrle   r0, [r3], #4      @ else: 2 instr
    asrle   r0, r0, #1
    ldrshgt r0, [r2, #2]!    @ then: 2 instr
    lslgt   r0, r0, #1
    bx     lr

**Key concept:** IT slot assignment: `LE`-slots run when condition matches `le`; `GT`-slots are the inverse. Pre- and post-indexed conditional LDRs are supported.

---

### Problem 2 (60 pts) — Piecewise function, three approaches

    f(x) = -10 if x < -5
         = +10 if x >= 5
         = 2x  otherwise

**Part 1 — C:**

    int mathf_c(int x) {
        int y;
        if (x < -5) y = -10;
        else if (x >= 5) y = 10;
        else y = 2 * x;
        return y;
    }

**Part 2 — CMP chain:**

    mathf_cmp:
        cmp    r0, #-5           @ CMN r0, #5
        bge    elseif            @ x >= -5 → skip to next test
        ldr    r0, =-10
        b      end
    elseif:
        cmp    r0, #5
        blt    else_blk
        ldr    r0, =10
        b      end
    else_blk:
        lsl    r0, r0, #1         @ 2*x
    end:
        bx     lr

**Part 3 — CEX with chained IT blocks:**

    mathf_cex:
        cmp    r0, #-5
        itt    lt
        ldrlt  r1, =-10           @ T1
        blt    end                 @ T2: cond B at END of IT block (legal)
        cmp    r0, #5
        ite    ge
        ldrge  r1, =10             @ T
        lsllt  r1, r0, #1          @ E: uses original x in r0
    end:
        mov    r0, r1
        bx     lr

**Key concept:** A conditional branch IS allowed inside an IT block, but **only as the last slot**. Use `ITT` with conditional B to short-circuit out after the first-range case.

---

### Problem 3 (40 pts) — Compound OR test

    int32_t load_based_on_x_c(int x, uint16_t *ptrA, uint32_t *ptrB) {
        if (x <= 20 || x >= 25) return (int32_t)*++ptrA * 4;
        else return *++ptrB / 4;
    }

Registers: r0=x, r1=ptrA (`uint16_t *`), r2=ptrB (`uint32_t *`). Signed test on `x`; unsigned divide (`LSR`) on `*++ptrB`.

**Part 1 — CMP short-circuit (Lctr 25 Ex. 6):**

    load_based_on_x_cmp:
        cmp    r0, #20
        ble    cmp_then          @ first OR: x ≤ 20 → then
        cmp    r0, #25
        bge    cmp_then          @ second OR: x ≥ 25 → then
        b      cmp_else          @ both false → else
    cmp_then:
        ldrh   r0, [r1, #2]!
        lsl    r0, r0, #2         @ * 4
        b      cmp_end
    cmp_else:
        ldr    r0, [r2, #4]!
        lsr    r0, r0, #2         @ / 4 (UNSIGNED!)
    cmp_end:
        bx     lr

**Part 2 — CEX (ITTEE ge), as much conditional execution as possible:**

    load_based_on_x_cex:
        cmp    r0, #20
        bgt    check25            @ first OR falls through to then-block
        ldrh   r0, [r1, #2]!     @ x ≤ 20 path
        lsl    r0, r0, #2
        bx     lr
    check25:
        cmp    r0, #25
        ittee  ge                 @ T,T=ge=then ; E,E=lt=else
        ldrhge  r0, [r1, #2]!    @ then
        lslge   r0, r0, #2
        ldrlt   r0, [r2, #4]!    @ else
        lsrlt   r0, r0, #2
        bx     lr

**Key concept:** The first sub-test of a compound OR can't fully fit in an IT block (because a conditional B can only be at the end). Handle it with a regular `bgt`, then pack the remaining test's two branches as an `ITTEE`.

---

## HW 12: Loops (100 pts total)

### Problem 1 (40 pts) — Swap-last-two-of-three encryption

    int mp_swap_last_2_chars_in_3_in_str_c(char *str);

For every trio of chars (i, i+1, i+2), swap chars at i+1 and i+2. Return pairs swapped.

**Part 1 — C using `while (1) { ... break; }`:**

    int mp_swap_last_2_chars_in_3_in_str_c(char *str) {
        int pair_swapped = 0;
        while (1) {
            char c1 = *str++;
            if (c1 == 0) break;
            char c2 = *str++;
            if (c2 == 0) break;
            char c3 = *str++;
            if (c3 == 0) break;
            *(str - 2) = c3;
            *(str - 1) = c2;
            pair_swapped++;
        }
        return pair_swapped;
    }

Test: `"hellow"` → `"hlelwo"`, return 2.

**Part 2 — ASM:** r0 = str, r1-3 = c1-c3, r12 = pair_swapped (all scratch, no push/pop).

    mp_swap_last_2_chars_in_3_in_str_s:
        mov    r12, #0
    lp:
        ldrb   r1, [r0], #1
        cbz    r1, end
        ldrb   r2, [r0], #1
        cbz    r2, end
        ldrb   r3, [r0], #1
        cbz    r3, end
        strb   r3, [r0, #-2]        @ *(str-2) = c3
        strb   r2, [r0, #-1]        @ *(str-1) = c2
        add    r12, r12, #1
        b      lp
    end:
        mov    r0, r12
        bx     lr

**Key concepts:**
- Post-index `ldrb [r0], #1` implements `*str++`.
- `CBZ` replaces `cmp`/`beq` for freshly-loaded byte — cannot appear inside IT block but fine as a standalone.
- After three LDRBs, the trio's 2nd/3rd chars live at offsets -2/-1 from new r0.
- Use `r12` (IP) as scratch accumulator — avoids pushing r4.

---

### Problem 2 (60 pts) — Lowercase-to-uppercase string copy, three parts

Given:

    void mp_str_cpy_2_caps_while_c(char *dst, char *src) {
        char ch = *src++;
        while (ch) {
            ch -= 0x20;
            *dst++ = ch;
            ch = *src++;
        }
        *dst++ = ch;        // writes the '\0' terminator
    }

Registers: r0=dst, r1=src, r2=ch.

**Part 1 — ASM of given `while` version** (30 pts):

    mp_str_cpy_2_caps_while_s:
        ldrb   r2, [r1], #1         @ priming read
    lp:
        cbz    r2, end              @ while (ch)
        sub    r2, r2, #0x20        @ 'a'→'A' mapping
        strb   r2, [r0], #1
        ldrb   r2, [r1], #1         @ update (duplicate code)
        b      lp
    end:
        strb   r2, [r0], #1          @ writes '\0' terminator
        bx     lr

**Part 2 — C refactored using `while (1) { break; }`** (10 pts):

    void mp_str_cpy_2_caps_while_brk_c(char *dst, char *src) {
        while (1) {
            char ch = *src++;
            if (ch == 0) {
                *dst++ = ch;
                break;
            }
            ch -= 0x20;
            *dst++ = ch;
        }
    }

**Part 3 — ASM of refactored version** (20 pts):

    mp_str_cpy_2_caps_while_brk_s:
    lp:
        ldrb   r2, [r1], #1         @ single read per iteration
        cbz    r2, end              @ if (ch == 0) break
        sub    r2, r2, #0x20
        strb   r2, [r0], #1
        b      lp
    end:
        strb   r2, [r0], #1          @ '\0' store (ch is 0 here)
        bx     lr

**Key concepts:**
- The `while (1) + break` form removes the duplicated priming/update read.
- The terminator store *must* still happen — it's placed at `_end:` after the loop.
- Both versions use identical number of total LDRB reads per input character (N+1); the difference is source-code cleanliness (one LDRB text instead of two).

---

## Big-picture key concepts (condensed)

1. **LDR/STR addressing modes.** Basic `[Ra, #os]`; pre-index `[Ra, #os]!`; post-index `[Ra], #os`. Same pattern for all data sizes and LDRD/STRD.
2. **C prefix → pre-index with `!`.** `*++p` = `ldr ... [r, #size]!`.
3. **C postfix → post-index.** `*p++` = `ldr ... [r], #size`.
4. **Sign extension matters.** `LDRSB 0x80 → 0xFFFFFF80`, `LDRB 0x80 → 0x00000080`.
5. **Register-offset = typed array indexing.** `[Ra, Ri, LSL #n]` where `n = log2(element_size)`.
6. **Signed vs unsigned.** Picks CCS (`GT` vs `HI`), shift (`ASR` vs `LSR`), and load suffix (`SB`/`SH` vs `B`/`H`).
7. **IT block limits.** Max 4 conditional insns; first slot = T = cond; conditional B only at end; no CBZ/CBNZ inside.
8. **PL vs NL layout.** PL: same CCS, else first. NL: opposite CCS, then first. NL reads closer to C.
9. **Compound OR = short-circuit double CMP.** Both conditions share a `_then` label.
10. **Loop shapes.** Plain while = priming + in-loop read; while(1)+break = single read. CBZ on freshly-loaded byte is the clean null-terminator test.
11. **Stem function template.** `push {r4-r?, lr}` / save args in R4+ / ... / `pop {r4-r?, pc}`.
12. **Scratch registers.** R0–R3, R12 are caller-saved — use R12 as an accumulator to avoid pushing R4.
