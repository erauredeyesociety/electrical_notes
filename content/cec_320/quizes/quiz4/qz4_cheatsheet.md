# CEC 320 — Quiz 4 Cheatsheet

## HWs 9, 10, 11, 12 | Lectures 20–26 (Lctr 19/27 peripheral)

---

## 1. LDR/STR Load/Store Matrix (Lctr 20–21)

**Two registers:** `Ra` = address register (pointer), `Rv` = value register (data).

### Data-size suffixes on LOAD

| Suffix | Size | Extension | C type |
|--------|------|-----------|--------|
| (none) | 32-bit word | none | `uint32_t` / `int32_t` |
| `B`    | unsigned byte | zero-ext | `uint8_t` |
| `SB`   | signed byte | sign-ext | `int8_t` |
| `H`    | unsigned halfword | zero-ext | `uint16_t` |
| `SH`   | signed halfword | sign-ext | `int16_t` |

**STORE has no sign variant** — only `STR`, `STRH`, `STRB`.

### Three immediate-offset addressing modes

| Mode | Syntax | Behavior |
|------|--------|----------|
| Basic | `LDR{t} Rv, [Ra, #os]` | Load from `Ra+os`. Ra unchanged. |
| Pre-index (writeback) | `LDR{t} Rv, [Ra, #os]!` | `Ra = Ra+os`, then load from `[Ra]`. |
| Post-index (writeback) | `LDR{t} Rv, [Ra], #os` | Load from `[Ra]`, then `Ra = Ra+os`. |

**Memory aid:** `!` = "urgent, update BEFORE"; trailing `#os` = "update AFTER".

### Register-offset addressing (no immediate) — Lctr 21

    LDR   Rv, [Ra, Ri, LSL #2]     @ 32-bit: addr = Ra + Ri*4
    LDRH  Rv, [Ra, Ri, LSL #1]     @ 16-bit: addr = Ra + Ri*2
    LDRB  Rv, [Ra, Ri]              @  8-bit: addr = Ra + Ri

Shift amount = `log2(element size)`. No pre/post writeback form on register-offset.

### LDRD / STRD — 64-bit double word (Lctr 23)

    LDRD  Rv_L, Rv_H, [Ra, #os]     @ basic, 8 bytes
    LDRD  Rv_L, Rv_H, [Ra, #os]!    @ pre-index
    LDRD  Rv_L, Rv_H, [Ra], #os     @ post-index

- `Rv_L` = lower address (LSW), `Rv_H` = higher address (MSW). Little-endian.
- **No register-offset form for LDRD/STRD.**

> **HW9 P1 (2c):** `ldr r1, [r4, #2]!` with r4=0x20000000 → r4 first becomes 0x20000002, then loads bytes at 0x20000002..05 → r1 = 0x05040302.
> **HW9 P1 (2d):** `ldr r2, [r4], #4` with r4=0x20000002 → loads first (r2=0x05040302), then r4 = 0x20000006.
> **HW10 P2 (Task 1):** `ldrd r2, r3, [r0, #8]!` with `r0=ipt` → r0 += 8; r2 = word at ipt+8 = 0xB0A09080; r3 = word at ipt+12 = 0xF0E0D0C0.

---

## 2. C Pointer Idiom → ASM Translation (Lctr 20, 22)

### 32-bit pointer (`int32_t *p32`): step = 4

| C expression | LDR (load) | STR (store) |
|---|---|---|
| `*(p32 + k)` | `ldr r0, [r1, #4*k]` | `str r0, [r1, #4*k]` |
| `*++p32` | `ldr r0, [r1, #4]!` | `str r0, [r1, #4]!` |
| `*p32++` | `ldr r0, [r1], #4` | `str r0, [r1], #4` |
| `*--p32` | `ldr r0, [r1, #-4]!` | `str r0, [r1, #-4]!` |
| `*p32--` | `ldr r0, [r1], #-4` | `str r0, [r1], #-4` |

### 16-bit pointer: step = 2 — use LDRH / LDRSH / STRH

| C expression (signed) | ASM |
|---|---|
| `*(pi16 + k)` | `ldrsh r0, [r1, #2*k]` |
| `*++pi16` | `ldrsh r0, [r1, #2]!` |
| `*pi16++` | `ldrsh r0, [r1], #2` |

(Replace `ldrsh` with `ldrh` for unsigned; use `strh` for stores — no sign variant.)

### 8-bit pointer: step = 1 — use LDRB / LDRSB / STRB

| C expression | ASM |
|---|---|
| `*(p8 + k)` | `ldrb r0, [r1, #k]` |
| `*p8++` | `ldrb r0, [r1], #1` |
| `*++p8` | `ldrb r0, [r1, #1]!` |

### Array indexing idiom (const pointer, running index i)

    ldr   r4, [r0, r3, lsl #2]     @ 32-bit: r4 = pArr[i]
    ldrh  r4, [r0, r3, lsl #1]     @ 16-bit
    ldrb  r4, [r0, r3]              @ 8-bit

> **HW9 P2 (mp_task1):** `ldrsh r2, [r0], #4` / `str r2, [r1, #0]` → `*p32 = (int32_t)*p16s; p16s += 2;` (post-index #4 skips an entire element — reads every other halfword).
> **HW9 P3 (Task 4):** `ldr r3, [r0, r2, lsl #2]` = register-offset array index (i in r2 means byte offset = 4*i for 32-bit elements).
> **HW10 P2 (Task 4):** `ldrh r3, [r0, r2, LSL #1]` = `iptr[r2]` with `uint16_t *iptr`.

---

## 3. Increment / Decrement — Values vs. Pointers (Lctr 22)

**C precedence that bites on the quiz:**
- Level 1 (LTR): postfix `++`/`--`, `[]`, `()`
- Level 2 (RTL): prefix `++`/`--`, unary `*`, `&`, `(type)`, `sizeof`

**Critical:** `p++` is evaluated **before** any adjacent `*` or prefix `++` — but its effect (incrementing `p`) happens after the original pointer value is "used" by the expression.

### Prefix vs. postfix on a value

    B[0] = ++A[0];            @ increment A[0] first, then assign
    ldr  r2, [r0]             @ temp = A[0]
    add  r2, #1               @ temp++
    str  r2, [r0]             @ A[0] = temp
    str  r2, [r1]             @ B[0] = temp

    B[1] = A[1]++;            @ assign old A[1] first, then increment
    ldr  r2, [r0, #4]         @ temp = A[1]
    str  r2, [r1, #4]         @ B[1] = temp   (old value used)
    add  r2, #1
    str  r2, [r0, #4]         @ A[1] = temp

### Composite patterns

| C expression | Meaning | ASM pattern |
|---|---|---|
| `*p++` | read `*p`, then `p++` | `ldrb r2, [r0], #1` |
| `*++p` | `p++`, then read `*p` | `ldrb r2, [r0, #1]!` |
| `*p++ = v` | store v at `*p`, then `p++` | `strb r2, [r0], #1` |
| `++*p` | increment the **value** at `*p` | `ldrb r2, [r0]` / `add r2, #1` / `strb r2, [r0]` |
| `++*p++` | `p++` returns old p; dereference old p; increment the value there | `ldrb r2, [r0], #1` / `add r2, #1` / `strb r2, [r0, #-1]` |
| `*p = *q++` | read `*q`, advance q, store into `*p` | `ldrb r2, [r1], #1` / `strb r2, [r0]` |

> **HW10 P1 Line 5:** `*p8b++ = ++*(p8a + 4);` — increment the byte at p8a+4 in memory (0x08 → 0x09), write it back, then store to `*p8b` and advance p8b.
> → `ldrb r2, [r0, #4]` / `add r2, #1` / `strb r2, [r0, #4]` / `strb r2, [r1], #1`
>
> **HW10 P1 Line 6:** `*p8b++ = ++*p8a++;` — p8a returns old value, dereferenced, value incremented, written back to original address, then stored at *p8b.
> → `ldrb r2, [r0], #1` / `add r2, #1` / `strb r2, [r0, #-1]` / `strb r2, [r1], #1`

**Pointer arithmetic by type:**
- `p8++` → address +1
- `p16++` → address +2
- `p32++` → address +4
- Difference `p - arr` on typed ptr → **elements**. On `(void*)p - (void*)arr` → **bytes**.

---

## 4. Function Calls in ASM (Lctr 23)

**AAPCS / EABI register roles:**

| Register | Role | Preserved? |
|---|---|---|
| R0–R3 | Args 1–4, return (R0, or R1:R0 for 64-bit) | No (caller-saved / scratch) |
| R12 (IP) | Scratch | No |
| R4–R11 | General | **Yes** (callee must PUSH/POP if used) |
| LR (R14) | Return address | Saved if stem function calls another |

**Leaf function:** never calls another → `bx lr` is fine, no need to push LR.
**Stem function:** calls another → **must** `push {lr}` (or include LR in a push list), then `pop {pc}` to return.

### `BL` semantics

    bl   target        @ LR = PC_next; PC = target

### Stem function pattern (full template)

    my_stem_fn:
        push    {r4-r7, lr}       @ save callee-saved + LR
        mov     r4, r0            @ save args in callee-saved regs
        mov     r5, r1
        mov     r6, r2
        mov     r7, r3
        @ ... body: loop, prepare args in R0-R3, bl inner, save return ...
        pop     {r4-r7, pc}       @ restore and return

### Loading arguments by C type

| C arg type | Load for R_arg |
|---|---|
| `int32_t` / `uint32_t` / pointer | `ldr` |
| `int16_t` | `ldrsh` |
| `uint16_t` | `ldrh` |
| `int8_t` / `char` (signed) | `ldrsb` |
| `uint8_t` | `ldrb` |
| `int64_t` / `uint64_t` | `ldrd r_lo, r_hi, ...` |

### Saving return values

- 32-bit or less: `str`, `strh`, or `strb` on R0
- 64-bit: `strd r0, r1, [Rdst]`

### Array loop + call template (Lctr 23 demo)

    ldr     r8, =0               @ i = 0
    loop:
        cmp     r8, r7           @ i < n?
        bge     end_loop
        ldr     r0, [r4, r8, lsl #2]   @ arg = x[i]
        ldr     r1, [r5, r8, lsl #2]   @ arg = y[i]
        bl      mp_umod_32bit_s
        str     r0, [r6, r8, lsl #2]   @ z[i] = return
        add     r8, #1
        b       loop
    end_loop:

For 64-bit elements (`int64_t` arrays), swap in `LDRD`/`STRD` with post-index `#8`:

    ldrd    r0, r1, [r4], #8     @ x[i], x ptr += 8
    ldrd    r2, r3, [r5], #8
    bl      mp_add_64bit_s
    strd    r0, r1, [r6], #8

---

## 5. Conditional Execution (IT blocks) and CBZ/CBNZ (Lctr 24)

### IT block syntax

    IT{x{y{z}}} cond        @ up to 4 slots: first = T, later = T or E

- `I` = If (the block itself), `T` = same as `cond`, `E` = inverse of `cond`.
- Each **instruction inside** the block must carry the matching CCS (`le`, `gt`, etc.).
- Common forms: `IT`, `ITT`, `ITE`, `ITTT`, `ITTE`, `ITEE`, `ITTEE`, `ITTTT`.

### Hard rules (test-favorite traps)

1. Max **4** conditional instructions per IT block.
2. The first slot must match `cond`; all `T` = cond, all `E` = inverse.
3. **Conditional branch** (`Bcc`) allowed only at the **end** of the IT block (not in the middle).
4. **CBZ / CBNZ cannot appear inside an IT block.**
5. `CBZ`/`CBNZ` only forward branches (up to ~126 bytes); **Rn must be R0–R7**; no flags set or read.

### CBZ / CBNZ

    CBZ  Rn, label     @ branch if Rn == 0
    CBNZ Rn, label     @ branch if Rn != 0

Natural replacement for `cmp Rn, #0` / `beq label`. Perfect for null-terminator tests on freshly-loaded bytes.

> **HW12 P1/P2:** `cbz r2, ..._end` after each `ldrb r2, [r1], #1` — tests just-loaded byte for zero without disturbing flags.

### CEX-form if/else (from Lctr 25 Ex. 2)

    @ C: if (x >= 0) x <<= 1; else x >>= 4;
    cmp    r0, #0
    ite    ge                @ T=ge, E=lt
    lslge  r0, #1            @ then (ge)
    asrlt  r0, #4            @ else (lt)
    bx     lr

### CEX with two instructions per branch

    cmp    r0, r1
    ittee  le                @ T,T=le ; E,E=gt
    ldrle   r0, [r3], #4     @ else: two instructions (le)
    asrle   r0, r0, #1
    ldrshgt r0, [r2, #2]!    @ then: two instructions (gt)
    lslgt   r0, r0, #1
    bx     lr

> **HW11 P1 Part 3:** `ITTEE le` packs 2-instr else + 2-instr then.

### Using a conditional branch to short-circuit an IT chain (from Lctr 25 Ex. 4)

    cmp    r0, #-5            @ assembles as CMN r0, #5
    itt    lt
    ldrlt  r1, =-10           @ T1
    blt    end_label          @ T2: conditional B — legal only as LAST slot

Then start a fresh `CMP` and a new IT block for the remaining cases.

> **HW11 P2 Part 3:** `ITT lt` ends with `BLT end`; then `ITE ge` handles `x>=5 ? 10 : 2*x`.

---

## 6. CCS Signed vs. Unsigned Quick Reference (review from Lctr 18–19)

| C test | Signed CCS | Unsigned CCS |
|---|---|---|
| `==` | `EQ` | `EQ` |
| `!=` | `NE` | `NE` |
| `>` | `GT` | `HI` |
| `>=` | `GE` | `HS` (`CS`) |
| `<` | `LT` | `LO` (`CC`) |
| `<=` | `LE` | `LS` |

**Pick signed CCSs when the C operands are `int*_t`**. Pick unsigned CCSs when they are `uint*_t` or addresses.

### Pseudo-instruction: CMP with negative immediate

`cmp r0, #-5` assembles to `CMN r0, #5`. Signed CCSs still work correctly because `CMN` sets flags for `r0 + 5`.

---

## 7. If / If-Else Translation — Positive vs. Negative Logic (Lctr 25)

### Positive Logic (PL) — branch-to-then on C condition true

    @ if (x > y) then_stuff; else else_stuff;
    cmp    r0, r1
    bgt    pl_then              @ SAME CCS as the C test
    pl_else:
        @ else block
        b      pl_end
    pl_then:
        @ then block
    pl_end:
        bx     lr

**Layout:** `cmp` → (same-CCS branch) → **else first**, `b end`, **then**, `end`.

### Negative Logic (NL) — branch-to-else on C condition false

    @ if (x > y) then_stuff; else else_stuff;
    cmp    r0, r1
    ble    nl_else              @ OPPOSITE of C test (LE is !GT)
    nl_then:
        @ then block
        b      nl_end
    nl_else:
        @ else block
    nl_end:
        bx     lr

**Layout:** `cmp` → (opposite-CCS branch) → **then first**, `b end`, **else**, `end`. NL reads closer to the original C.

### If-else-if-else (CMP chain)

    cmp    r0, #-5
    bge    elseif                 @ NL for x < -5
    then:
        ldr    r0, =-10
        b      end
    elseif:
        cmp    r0, #5
        blt    else_blk            @ NL for x >= 5
        ldr    r0, =10
        b      end
    else_blk:
        lsl    r0, r0, #1          @ 2*x
    end:
        bx     lr

> **HW11 P2 Part 2:** exactly this 3-way cascade pattern.

### Compound `OR` — short-circuit double CMP (Lctr 25 Ex. 6)

    @ if (x <= 20 || x >= 25) then_block; else else_block;
    cmp    r0, #20
    ble    then_block                  @ first cond TRUE → jump to then
    cmp    r0, #25
    bge    then_block                  @ second cond TRUE → then
    b      else_block                   @ both false → else

> **HW11 P3 Part 1:** literal of this pattern (two `ble` / `bge` tests share one `then_block` label).

### Compound `AND` — negate the AND via De Morgan, use `OR` pattern (or chained CMP/branches on falsity)

    @ if (x > 0 && x < 8) then_block; else else_block;
    cmp    r0, #0
    ble    else_block          @ if x <= 0, else
    cmp    r0, #8
    bge    else_block          @ if x >= 8, else
    @ fall through = then

---

## 8. Loops: for / while / do-while (Lctr 26)

### Standard label naming convention (instructor style)

- `<fn>_lp` = top of loop (jump target for `continue` / loop back)
- `<fn>_end` = after loop body (jump target for `break` / exit)
- Optional `<fn>_body`, `<fn>_cond`, `<fn>_update`

### while loop (top-tested) — Example 10 shape

    @ while (ch) { body; ch = *src++; }
    ldrb    r2, [r1], #1           @ PRIMING READ
    lp:
        cbz    r2, end              @ exit if zero
            @ ... body ...
            ldrb   r2, [r1], #1     @ in-loop read (duplicate!)
        b      lp
    end:
        @ post-loop work (often: store terminator)

### do-while loop (bottom-tested) — body runs ≥1 time

    lp:
        @ ... body ...
    cmp    r0, r1
    blt    lp                       @ while (r0 < r1)

### for loop — init, top-test, body, update, back to test

    mov    r4, #0                   @ i = 0
    lp:
        cmp    r4, r5               @ i < n?
        bge    end
            @ body
        add    r4, #1                @ i++
        b      lp
    end:

### while-using-CEX variant (Example 4 shape)

    lp:
        cmp     r0, r1
        it      lt                   @ run body only if lt
        blt     body_inside_it       @ must be last IT slot
        b       end
        body_inside_it:
            @ ... body ...
        b       lp
    end:

### while (1) + break — removes priming-read duplication

    lp:
        ldrb    r2, [r1], #1         @ SINGLE read per iteration
        cbz     r2, end              @ if (ch == 0) break
            @ ... body ...
        b       lp
    end:
        @ post-exit work

> **HW12 P2 Part 1 (plain while):** two `ldrb r2, [r1], #1` — one priming, one in-loop.
> **HW12 P2 Part 3 (while-1+break):** one `ldrb` inside loop, terminator `strb` at `_end`.
> **HW12 P1:** three `cbz` after three `ldrb`-post-index — any null char breaks out of the trio-swap.

---

## 9. break, continue (Lctr 27, peripheral to Qz 4)

- `break` = forward `b <loop_end>` (or `cbz`/`cbnz` inline).
- `continue` in a `while`/`do-while` = backward `b <loop_lp>` (to condition test).
- `continue` in a `for` loop = branch to the **update** expression, not the top (so update still runs).
- **CBZ/CBNZ cannot live inside an IT block** — but as free-standing conditional branches they're the preferred null-terminator test.

### `while (1) { ... break; }` template (Lctr 27 Ex. 1b)

    lp:
        ldrb    r1, [r0], #1
        cbz     r1, end             @ break
        ldrb    r2, [r0], #1
        cbz     r2, end             @ break
            @ body
        b       lp
    end:
        @ possibly write-back terminator or accumulator

### switch naive (CMP/BEQ ladder) — Lctr 27 Sec 27.4.2

    cmp    r0, #65               @ 'A'
    beq    case_a
    cmp    r0, #66
    beq    case_b
    ...
    b      default_label
    case_a:
    case_b:                      @ stacked labels = fall-through case bodies
        ldr    r0, =80            @ 'P'
        b      end
    default_label:
        ldr    r0, =69            @ 'E'
    end:
        bx     lr

### switch with ADR + TBB (Lctr 27 Sec 27.4.3) — table-based O(1) dispatch

    adr    r1, table              @ r1 = address of byte table
    tbb    [r1, r0]               @ PC = PC + 4 + 2*table[r0]
    case_a:
        ...
    table:
        .byte 0                                  @ entry 0 = first case after TBB
        .byte (case_b - case_a)/2                @ /2 because Thumb-2 halfword aligned

---

## 10. ASM Instruction Reference (LDR/STR focus)

### Immediate-offset loads

    ldr    r0, [r1]                @ r0 = *r1              (word)
    ldr    r0, [r1, #4]            @ r0 = *(r1 + 4)
    ldr    r0, [r1, #4]!           @ r1 += 4; r0 = *r1
    ldr    r0, [r1], #4            @ r0 = *r1; r1 += 4
    ldrb   r0, [r1]                @ r0 = *(uint8_t*)r1    (zero-extended)
    ldrsb  r0, [r1]                @ r0 = *(int8_t*)r1     (sign-extended)
    ldrh   r0, [r1]                @ r0 = *(uint16_t*)r1
    ldrsh  r0, [r1]                @ r0 = *(int16_t*)r1
    ldrd   r0, r1, [r2, #8]!       @ 64-bit: r2 += 8; r0=LW, r1=HW

### Register-offset loads

    ldr    r0, [r1, r2, lsl #2]    @ r0 = *((uint32_t*)r1 + r2)
    ldrh   r0, [r1, r2, lsl #1]    @ r0 = *((uint16_t*)r1 + r2)
    ldrb   r0, [r1, r2]             @ r0 = *((uint8_t*)r1 + r2)

### Stores (mirror of loads — no sign variant)

    str    r0, [r1, #4]!           @ r1 += 4; *r1 = r0
    strb   r0, [r1], #1            @ *r1 = (r0 & 0xFF); r1 += 1
    strh   r0, [r1, #-2]           @ *(uint16_t*)(r1 - 2) = low halfword of r0
    strd   r0, r1, [r2], #8        @ *r2 = r0; *(r2+4) = r1; r2 += 8

### MOV and pseudo-LDR

    mov    r0, r1                  @ r0 = r1
    mov    r0, #42                 @ small immediate only
    movw   r0, #0xBEEF             @ low 16 bits, zero upper
    movt   r0, #0xDEAD             @ upper 16 bits, low unchanged
    ldr    r0, =0x12345678         @ assembler picks MOV/MOVW or literal pool

### CBZ / CBNZ

    cbz    r0, label               @ branch if r0 == 0 (forward, Rn in R0–R7)
    cbnz   r0, label               @ branch if r0 != 0

### IT block examples

    cmp    r0, #0
    ite    ge
    lslge  r0, #1                  @ then
    asrlt  r0, #4                  @ else

    cmp    r0, r1
    ittee  le
    ldrle   r0, [r3], #4
    asrle   r0, r0, #1
    ldrshgt r0, [r2, #2]!
    lslgt   r0, r0, #1

### Stack

    push   {r4-r7, lr}              @ SP -= 5*4; stores R4,R5,R6,R7,LR (sorted low→high)
    pop    {r4-r7, pc}              @ restore + return (LR → PC)

---

## 11. Quick Translation Checklist (use this during the quiz)

Given a C statement, answer in order:

1. **What's the data type?** Picks `LDR` variant (`B`/`SB`/`H`/`SH`/none) and offset multiplier (1/2/4/8).
2. **What's the increment order?** Prefix vs postfix → pre-index (`!`) vs post-index vs no-writeback.
3. **What side is being modified?** Value in memory (need store-back), pointer (`r` offset changes), or both.
4. **Signed or unsigned?** Picks CCS (GT/LT vs HI/LO), shift (`ASR` vs `LSR`), and load suffix (`SB`/`SH` vs `B`/`H`).
5. **Single arithmetic or branch?** Single instruction → barrel-shifter Op2 or conditional execution. Multi-statement → branch with labels.
6. **Leaf or stem?** If calling any BL, push LR + callee-saved regs.

---
