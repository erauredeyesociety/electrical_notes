# CEC 320 Quiz 4 — Lecture Notes Summary (Lectures 20–26)

Condensed lecture notes for quiz prep. Each lecture gets one paragraph of narrative plus key patterns/tables. Lecture 19 (CCS review) and Lecture 27 (break/continue/switch) are summarized briefly at the end as peripheral material.

---

## Lecture 20: Immediate-Offset Load and Store Instructions

Lctr 20 introduces the core LDR/STR instructions with immediate offsets and sets up the fundamental C-to-ASM pointer mapping. Two registers matter: `Ra` (address register, the pointer) and `Rv` (value register, the data being moved). Three addressing modes exist — basic `[Ra, #os]` (Ra unchanged), pre-index `[Ra, #os]!` (Ra updated *before* the access), and post-index `[Ra], #os` (Ra updated *after*). Five data-size suffixes on LOAD (`(none)`/`B`/`SB`/`H`/`SH`) pair with three on STORE (`(none)`/`H`/`B`) — note stores have no sign variant because the programmer controls what's in the low bits.

### Three addressing modes

| Mode | LDR syntax | Behavior | C equivalent |
|---|---|---|---|
| Basic | `LDR{t} Rv, [Ra, #os]` | `Rv = *(Ra+os)`, Ra unchanged | `var = *(ptr + k)` |
| Pre-indexed | `LDR{t} Rv, [Ra, #os]!` | `Ra = Ra+os; Rv = *Ra` | `var = *++ptr` |
| Post-indexed | `LDR{t} Rv, [Ra], #os` | `Rv = *Ra; Ra = Ra+os` | `var = *ptr++` |

### Data-type suffixes

| Suffix | Type | Extension | C type |
|---|---|---|---|
| (none) | 32-bit word | none | `uint32_t` / `int32_t` |
| `B` | unsigned byte | zero-extend | `uint8_t` |
| `SB` | signed byte | sign-extend | `int8_t` |
| `H` | unsigned halfword | zero-extend | `uint16_t` |
| `SH` | signed halfword | sign-extend | `int16_t` |

### C-to-ASM pointer idioms (LDR examples; STR mirrors)

| C | ASM | Notes |
|---|---|---|
| `var = *(p32 + k)` | `ldr r0, [r1, #4*k]` | offset = 4*k for 32-bit |
| `var = *++p32` | `ldr r0, [r1, #4]!` | pre-index |
| `var = *p32++` | `ldr r0, [r1], #4` | post-index |
| `var = *(p16 + k)` | `ldrh/ldrsh r0, [r1, #2*k]` | offset = 2*k for 16-bit |
| `var = *p8++` | `ldrb/ldrsb r0, [r1], #1` | offset = 1 for 8-bit |

### Memory aid
- `[r1, #4]` = nothing extra → Ra NOT updated
- `[r1, #4]!` = "exclamation = urgent" → Ra updated BEFORE
- `[r1], #4` = number after bracket → Ra updated AFTER

---

## Lecture 21: Additional Load/Store (Register-Offset) and Move Instructions

Lctr 21 extends Lctr 20 with **register-offset addressing** — the offset comes from another register (optionally shifted) rather than an immediate. The pattern `[Ra, Ri, LSL #n]` gives typed array indexing where `n = log2(element_size)`: `LSL #2` for words, `LSL #1` for halfwords, no shift for bytes. There is **no pre- or post-index version of register-offset** (only the immediate-offset form supports writeback). The lecture also introduces `MOV` variants (`MOV`, `MOVW`, `MOVT`) and the pseudo `LDR Rd, =expr` which the assembler converts to `MOV` for small immediates, `MOVW` for 16-bit values, or a literal-pool load for larger values.

### Register-offset loads

| Type | Instruction | Effective address |
|---|---|---|
| 32-bit | `LDR Rv, [Ra, Ri, LSL #2]` | `Ra + Ri*4` (= p32[i]) |
| 16-bit | `LDRH Rv, [Ra, Ri, LSL #1]` | `Ra + Ri*2` (= p16[i]) |
| 8-bit | `LDRB Rv, [Ra, Ri]` | `Ra + Ri` (= p8[i]) |

For signed loads, use `LDRSH` or `LDRSB`. Stores drop the S suffix.

### Two ways to iterate an array in a loop

**Pointer-update (post-index):** `ldr r4, [r0], #4` — the pointer itself advances.
**Register-offset (const ptr):** `ldr r4, [r0, r3, lsl #2]` — pointer stays put, index `r3` increments. The register-offset form is required when the pointer must remain a `const` or shared value.

### Pseudo-LDR

    ldr  r0, =42              @ assembler emits `mov.w r0, #42`
    ldr  r1, =0xBEEF          @ assembler emits `movw r1, #0xBEEF`
    ldr  r2, =0xDEADBEEF      @ assembler emits PC-relative LDR from literal pool

---

## Lecture 22: Increment Operations for C Variables and Pointers

Lctr 22 grapples with the most error-prone aspect of pointer manipulation: C's pre- and postfix `++`/`--` operators, especially when layered with dereference. Operator **precedence** is crucial — postfix `++` is precedence 1 (highest, LTR), while prefix `++`, `*`, `(cast)`, `&` are all precedence 2 (RTL). So in `*p++`, the postfix `++` binds to `p` first (returning the old pointer value); the `*` then dereferences the old address; after evaluation the pointer has advanced. In `*++p`, the prefix `++` is evaluated right-to-left with `*`, so `p` advances first and the new address is dereferenced. The lecture also clarifies that pointer arithmetic scales by `sizeof(element)`: `p32++` advances 4 bytes, `p16++` advances 2, `p8++` advances 1.

### Prefix vs. postfix (value):

    B[0] = ++A[0];        // increment A[0] first, then use
    B[1] = A[1]++;        // use A[1] first, then increment

### Compound increment patterns

| C | ASM implementation |
|---|---|
| `var = *p++;` | `ldrb r2, [r0], #1` |
| `var = *++p;` | `ldrb r2, [r0, #1]!` |
| `*p = ++var;` | `add r2, #1; strb r2, [r0]` (r2 = var) |
| `*p = var++;` | `strb r2, [r0]; add r2, #1` |
| `++*p` | `ldrb r2, [r0] / add r2, #1 / strb r2, [r0]` |
| `++*p++` | `ldrb r2, [r0], #1 / add r2, #1 / strb r2, [r0, #-1]` |
| `*q++ = *p++;` | `ldrb r2, [r0], #1 / strb r2, [r1], #1` |
| `*q++ = *++p;` | `ldrb r2, [r0, #1]! / strb r2, [r1], #1` |

### Warning: unsequenced modifications

Expressions like `B[i] = A[i++]++;` are undefined behavior (unsequenced modification and access to `i`). Use `B[i] = A[i]++; i++;` or the comma operator `B[i] = A[i]++, i++;` instead.

### Pointer arithmetic by type

    int16_t *p16;  p16++;     // +2 bytes
    int32_t *p32;  p32++;     // +4 bytes
    uint8_t *p8;   p8++;       // +1 byte

Difference `(p - arr)` on typed pointer yields elements; `(void*)p - (void*)arr` yields bytes.

---

## Lecture 23: Calling ASM Functions from ASM

Lctr 23 extends single-function EABI conventions to multi-function call chains. It distinguishes **leaf functions** (never call another — can use `bx lr` to return without stacking LR) from **stem functions** (do call others — MUST `push {lr}` on entry and `pop {pc}` on return because `BL` overwrites LR). It introduces `LDRD`/`STRD` for loading/storing 64-bit double words (two consecutive registers; Rv_L at lower address, Rv_H at higher; ARM little-endian). The lecture closes with the complete stem-function template: save callee-saved regs + LR, save your own args in R4–R7, loop over array work calling the leaf via `BL`, restore and return.

### BL semantics

    bl   asm_leaf       @ LR = address after this BL; PC = asm_leaf

The callee returns by moving LR → PC (`bx lr` or `pop {..., pc}`).

### Stem function template

    my_stem_fn:
        push    {r4-r7, lr}           @ preserve + save LR
        mov     r4, r0                @ save args to callee-saved
        mov     r5, r1
        mov     r6, r2
        mov     r7, r3
    loop:
        cmp     r_i, r_n
        bge     end
        ldr     r0, [r4, r_i, lsl #2]  @ prep arg0
        ldr     r1, [r5, r_i, lsl #2]  @ prep arg1
        bl      inner_leaf
        str     r0, [r6, r_i, lsl #2]  @ save return
        add     r_i, #1
        b       loop
    end:
        pop     {r4-r7, pc}

### LDRD / STRD

    ldrd    r2, r3, [r0, #8]!     @ pre-index: r0 += 8, then load 8 bytes → r2 (LW), r3 (HW)
    strd    r0, r1, [r6], #8      @ post-index: store 8 bytes, then r6 += 8

**No register-offset form exists for LDRD/STRD.**

### Argument-type load reference

| C type | Instruction to prep arg |
|---|---|
| `int32_t`, pointer | `LDR` |
| `uint16_t` | `LDRH` |
| `int16_t` | `LDRSH` |
| `uint8_t` | `LDRB` |
| `int8_t`, `char` (signed) | `LDRSB` |
| `int64_t`, `uint64_t` | `LDRD` |

Mirror store instructions (no sign variant) save the return.

---

## Lecture 24: Combination Branching and Conditional Execution

Lctr 24 introduces two compact control-flow tools: the **combination branch** instructions `CBZ` and `CBNZ`, and the **IT (If-Then) block** that organizes conditional instructions. `CBZ Rn, label` branches forward if `Rn == 0` (and `CBNZ` if `Rn != 0`); critically, Rn must be in R0–R7, the branch is only forward (range up to ~126 bytes), and neither instruction sets or reads any flag — they're perfect for zero-byte tests on freshly-loaded bytes. The IT block is more subtle: up to 4 conditional instructions (`IT`, `ITT`, `ITE`, ..., `ITTEE`, `ITTTT`) share a condition code. The first slot is always `T` (matching the block's `cond`); later slots can be `T` (same) or `E` (inverse). Each instruction inside the block must have its CCS explicitly appended (`lslge`, `asrlt`, `ldrshgt`, etc.).

### Hard rules

1. IT block maximum = 4 conditional instructions.
2. First slot must match the IT's `cond`; `T` slots match cond, `E` slots are inverse of cond.
3. **A conditional branch is allowed only in the LAST IT slot** — not in the middle.
4. **CBZ/CBNZ cannot appear inside an IT block.**
5. CBZ/CBNZ Rn restricted to R0–R7; forward branches only.

### IT block forms

| Form | Slots | Usage |
|---|---|---|
| `IT cond` | 1 | Single conditional instruction |
| `ITT cond` | 2 | Both slots match cond |
| `ITE cond` | 2 | T, E — then + else |
| `ITTE cond` | 3 | T, T, E |
| `ITTEE cond` | 4 | T, T, E, E — two-instr then + two-instr else |
| `ITTTT cond` | 4 | All T — four matching instructions |

### Worked example

    cmp    r0, #0
    ite    ge
    lslge  r0, #1                  @ then: r0 <<= 1 when ge
    asrlt  r0, #4                  @ else: r0 >>= 4 when lt (inverse of ge)

---

## Lecture 25: Selection Control (If-Based Flow Control in C and ASM)

Lctr 25 is the central control-flow lecture for Qz 4 — it teaches how to translate every if/if-else variant. The foundation is the choice between **positive logic (PL)** and **negative logic (NL)** layouts. In PL, the `cmp` is followed by a branch using the **same** CCS as the C test (e.g., `bgt` for `x > y`), which branches TO the `_then` label; the `_else` block is laid out first to fall through when the test is false. In NL, the branch uses the **inverse** CCS (`ble` for `x > y`), branching to `_else`; the `_then` block is first. NL is more idiomatic because its code order matches the C reading order. The lecture then layers on `if-else-if-else` as chained CMP/branches, `CEX` variants that collapse single-instruction branches into IT blocks, and compound tests with `&&`/`||` via short-circuit double-CMP patterns.

### PL vs NL

    @ C: if (x > y) then; else els;

    @ PL (positive logic) — branch to then on same CCS:
    cmp    r0, r1
    bgt    pl_then
    pl_else:
        ...
        b      pl_end
    pl_then:
        ...
    pl_end:

    @ NL (negative logic) — branch to else on inverse CCS:
    cmp    r0, r1
    ble    nl_else              @ LE = !GT
    nl_then:
        ...
        b      nl_end
    nl_else:
        ...
    nl_end:

### CEX form of if-else

    cmp    r0, #0
    ite    ge
    lslge  r0, #1                @ then (cond true)
    asrlt  r0, #4                @ else (cond false)

When each branch is 2 instructions, use `ITTEE`.

### if-else-if-else (CMP chain)

    cmp    r0, #-5               @ CMN r0, #5 assembled
    bge    elseif
    ldr    r0, =-10
    b      end
elseif:
    cmp    r0, #5
    blt    else_blk
    ldr    r0, =10
    b      end
else_blk:
    lsl    r0, r0, #1
end:
    bx     lr

### if-else-if-else (CEX chain with conditional B)

The CEX form uses `ITT cond` with a conditional B as the last slot to short-circuit out:

    cmp    r0, #-5
    itt    lt
    ldrlt  r1, =-10              @ T1
    blt    end                    @ T2 (conditional B at end — legal!)
    cmp    r0, #5
    ite    ge
    ldrge  r1, =10                @ T
    lsllt  r1, r0, #1             @ E: use original x in r0

### Compound OR (Example 6) — short-circuit double CMP

    @ C: if (x < 0 || x >= 8) then; else els;
    cmp    r0, #0
    blt    then                   @ first OR true → skip second test
    cmp    r0, #8
    blt    else                    @ second OR false → else
    then:
        ...
    else:

### Compound AND — De Morgan or two CMPs with inverse branches

    @ C: if (x > 0 && x < 8) then; else els;
    cmp    r0, #0
    ble    else                    @ if x ≤ 0, else
    cmp    r0, #8
    bge    else                    @ if x ≥ 8, else
    @ fall through = then

---

## Lecture 26: Implementing C's Loops in ASM

Lctr 26 translates the three C loops — `for`, `while`, `do-while` — into ASM skeletons. The instructor's standard label convention is `<fn>_lp:` (top of loop) and `<fn>_end:` (exit). `for` and `while` are top-tested (body can run 0 times); `do-while` is bottom-tested (body always runs ≥1 time). The lecture covers three equivalent `while`-loop shapes: **common CMP** (test at top, branch forward on exit), **late-check** (jump over the body on first entry, test at bottom on subsequent iterations), and **CEX** (put the conditional body inside an IT block). The "priming read" pattern — reading a byte before the loop and re-reading inside it — appears when the loop condition depends on a value that must be loaded, and is the duplication Lctr 27's `while (1)` + `break` idiom removes.

### `while` loop — common shape (top-test)

    @ while (cond) { body; }
    lp:
        cmp    r0, r1
        bge    end                 @ NL: exit when !(cond)
        @ body
        add    r0, #1               @ update
        b      lp
    end:

### `while` with CBZ on a loaded byte (Example 10 — string copy)

    @ void str_cpy(char *dst, char *src)
    ldrb   r2, [r1], #1           @ priming read
    lp:
        cbz    r2, end             @ while (ch)
        strb   r2, [r0], #1
        ldrb   r2, [r1], #1        @ in-loop read
        b      lp
    end:

### `do-while` — bottom-tested

    lp:
        @ body
        @ update
        cmp    r0, r1
        blt    lp                  @ while (cond)

### `for` loop

    @ for (int i = 0; i < n; i++) body;
    mov    r4, #0                 @ init
    lp:
        cmp    r4, r5
        bge    end                 @ test
        @ body
        add    r4, #1               @ update
        b      lp
    end:

### `for` loop using CEX (optional)

    lp:
        cmp    r4, r5
        itt    lt
        <body_insn1>lt
        blt    lp_continue        @ last IT slot can be conditional B
        b      end
    lp_continue:
        add    r4, #1
        b      lp
    end:

### Common loop + function call (stem pattern, Lctr 23 review)

See the stem template in the Lctr 23 section — when a loop body calls a leaf via `BL`, the stem function must push LR + callee-saved regs, save args in R4–R7, reload args before each BL, and save the return value after each BL.

---

## Lecture 19 (review): Condition Code Suffixes and Conditional Branch

Lctr 19 is nominally part of Qz 3 but is foundational for every if/loop translation in Qz 4. Key ideas: `CMP Rn, Op2` computes `Rn - Op2` and sets NZCV without storing the result. The four flags NZCV drive all conditional branches via **Condition Code Suffixes (CCS)**. Signed and unsigned comparisons use different CCS families: signed uses `GT`/`GE`/`LT`/`LE` (depends on V and N); unsigned uses `HI`/`HS`/`LO`/`LS` (depends on C and Z). `EQ`/`NE` (depending only on Z) work for both.

### CCS Quick Table

| C test | Signed | Unsigned |
|---|---|---|
| `==` | EQ | EQ |
| `!=` | NE | NE |
| `>` | GT | HI |
| `>=` | GE | HS (CS) |
| `<` | LT | LO (CC) |
| `<=` | LE | LS |

### Rule of thumb
- **Signed operands** (`int*_t`) → use signed CCSs and `ASR` for division.
- **Unsigned operands** (`uint*_t`) or address comparisons → use unsigned CCSs and `LSR` for division.
- **`CMP Rn, #-imm`** is assembled as `CMN Rn, #imm`. Signed CCSs still work because `CMN` sets flags as if adding.

---

## Lecture 27 (peripheral): Complex Flow Control

Lctr 27 extends Lctr 26 with the `break`, `continue` keywords and the `switch` construct, plus the `ADR` / `TBB` / `TBH` instructions. `break` becomes a forward branch to the loop's `_end` label. `continue` is a backward branch — to the test in `while`/`do-while`, but to the **update expression** in `for` (so the loop variable still advances). Switch can be implemented naively as a chain of `CMP`/`BEQ` (O(n)), or compactly with `ADR`-load-table + `TBB` (O(1), ~1 byte per case, up to 512-byte jump span via halving due to Thumb-2 halfword alignment). The `while (1) { ... break; }` idiom is the core refactoring tool for removing priming-read duplication in ASM string loops.

### `while (1) + break` pattern (Example 1b)

    lp:
        ldrb   r1, [r0], #1
        cbz    r1, end             @ break
        ldrb   r2, [r0], #1
        cbz    r2, end             @ break
        @ body
        b      lp
    end:

### `break` + `continue` pattern (Example 2b)

    @ while (1) { ch = *str++; if (ch==0) break; if (ch==' ') continue; count++; }
    lp:
        ldrb   r1, [r0], #1
        cbz    r1, end              @ break
        cmp    r1, #' '
        beq    lp                   @ continue
        add    r2, #1
        b      lp
    end:

### `switch` ladder (Example 3b)

    cmp    r0, #65                 @ 'A'
    beq    case_a
    cmp    r0, #66
    beq    case_b
    ...
    b      default
    case_a:
    case_b:                        @ stacked labels fall through
        ldr    r0, =80
        b      end
    default:
        ldr    r0, =69
    end:

### `switch` with TBB (Example 3c)

    sub    r0, #65                  @ normalize index 0..n-1
    cmp    r0, #0
    blt    default_label
    cmp    r0, #N
    bge    default_label
    adr    r1, table
    tbb    [r1, r0]                @ PC = PC+4+2*table[r0]
    case_a:
    ...
    table:
        .byte (case_a - case_a) / 2
        .byte (case_b - case_a) / 2
        ...

---

## Cross-lecture pattern summary

| Pattern | Found in | HW usage |
|---|---|---|
| Immediate-offset addressing | Lctr 20 | HW9 P1, HW10 P2 |
| Pre-/post-index writeback | Lctr 20 | HW9 P2, HW10 P1, HW11, HW12 |
| Register-offset array index | Lctr 21 | HW9 P3 Task 4, HW10 P2 Task 4 |
| Sign extension LDRSB/LDRSH | Lctr 20 | HW10 P2 Tasks 2-3 |
| Pointer arithmetic by type | Lctr 22 | HW9 P2, HW10 P1, HW11 P1/P3 |
| Increment composite `*++p`, `*p++`, `++*p++` | Lctr 22 | HW10 P1 |
| LDRD/STRD for 64-bit | Lctr 23 | HW10 P2 Tasks 1-3, Lctr 23 demo |
| Stem fn w/ BL + push/pop | Lctr 23 | Lctr 23 demo (umod_array, add_64bit_array) |
| CBZ/CBNZ | Lctr 24 | HW12 P1, HW12 P2 Parts 1&3 |
| IT block (ITE/ITT/ITTEE) | Lctr 24, 25 | HW11 P1/P2/P3 Part 3 |
| PL vs NL layout | Lctr 25 | HW11 P1 Parts 1&2 |
| if-else-if CMP chain | Lctr 25 | HW11 P2 Part 2 |
| if-else-if CEX chain w/ cond B | Lctr 25 | HW11 P2 Part 3 |
| Compound OR short-circuit | Lctr 25 | HW11 P3 Part 1 |
| while loop w/ priming read | Lctr 26 | HW12 P2 Part 1 |
| while (1) + break | Lctr 27 | HW12 P1, HW12 P2 Parts 2&3 |
