# Lecture 23: Calling ASM Functions in an ASM Function

## Review: Function Calling Conventions (EABI)

- **R0-R3**: arguments to the callee; R0 (or R0:R1 for 64-bit) holds the return value
- **R4-R12**: callee must preserve these (push at start, pop at end)
- **LR** (Link Register): holds the return address
- **Return**: either `bx lr` or `pop {..., pc}`

---

## LDRD and STRD Instructions (64-bit Load/Store)

For loading/storing 64-bit (double word) values, use LDRD/STRD. They come in the same three addressing modes:

| Mode | LDRD Syntax | STRD Syntax |
|------|-------------|-------------|
| Basic | `LDRD Rv_L, Rv_H, [Ra{, #os}]` | `STRD Rv_L, Rv_H, [Ra{, #os}]` |
| Pre-indexed | `LDRD Rv_L, Rv_H, [Ra, #os]!` | `STRD Rv_L, Rv_H, [Ra, #os]!` |
| Post-indexed | `LDRD Rv_L, Rv_H, [Ra], #os` | `STRD Rv_L, Rv_H, [Ra], #os` |

- **Rv_L** = register for the lower 32 bits (lower address)
- **Rv_H** = register for the upper 32 bits (higher address)
- ARM is **little-endian** by default: first 4 bytes go to Rv_L, next 4 to Rv_H
- Loads 8 consecutive bytes total
- **No register-offset version** of LDRD/STRD exists

### Example (R0 = 0x2000_0200, memory map with known bytes)
```asm
ldrd r2, r3, [r0, #8]    @ Load 8 bytes from 0x2000_0208. R0 unchanged.
ldrd r4, r5, [r0, #4]!   @ R0 = 0x2000_0204, then load 8 bytes from R0.
ldrd r6, r7, [r0], #-4   @ Load 8 bytes from current R0, then R0 = R0-4.
```

### Related: LDM/STM
- LDRD/STRD extend to LDM (load multiple) and STM (store multiple)
- PUSH and POP are built on LDM/STM
- Details not covered in this course

---

## The BL (Branch and Link) Instruction

```asm
bl   asm_leaf
```

BL performs two operations atomically:
1. **LR = address of the next instruction** (the one right after the BL)
2. **PC = address of the called function** (jumps to it)

The callee returns by putting LR back into PC (via `bx lr` or `pop {..., pc}`).

---

## Leaf vs Stem Functions

- **Leaf function**: does NOT call other functions. At the bottom of the call chain. Only a callee.
- **Stem function**: DOES call other functions. Can be both caller and callee.

---

## Preserving Environment in a Leaf Function

Per EABI:
- R0-R3 can be used freely (scratch registers)
- If R4-R12 are used, they must be preserved via PUSH/POP
- Return via `bx lr` (PUSH {LR} is optional in a leaf)

---

## Preserving Environment in a Stem Function

A stem function must handle three things:

### 1. Preserve callee-saved registers (R4-R12)
Same as leaf -- PUSH at entry, POP at exit.

### 2. Preserve LR (REQUIRED for stem functions)
Because BL overwrites LR when calling the inner function. Must `push {... lr}` at entry and `pop {... pc}` at exit.

### 3. Preserve the caller's arguments (R0-R3)
Before calling the inner function, the stem's own arguments in R0-R3 will be overwritten. Solution: **MOV them to callee-saved registers** (R4-R7) at the start of the function.

### Pattern for a stem function:
```asm
my_stem_fn:
    push    {r4-r8, lr}       @ Save callee-saved regs + LR
    mov     r4, r0            @ Save arg0
    mov     r5, r1            @ Save arg1
    mov     r6, r2            @ Save arg2
    mov     r7, r3            @ Save arg3
    @ ... loop / work ...
    @ Prepare arguments for callee in R0-R3:
    ldr     r0, [r4, ...]     @ Load argument for callee
    ldr     r1, [r5, ...]
    bl      my_leaf_fn        @ Call leaf
    str     r0, [r6, ...]     @ Save return value
    @ ... continue loop ...
    pop     {r4-r8, pc}       @ Restore regs + return
```

---

## Preparing Arguments for the Callee

Use the appropriate load instruction to put arguments in R0-R3:
- **Up to 32-bit args**: `LDR`, `LDRSH`, `LDRH`, `LDRSB`, `LDRB` based on data type
- **64-bit args**: `LDRD` loads into two registers (e.g., R0:R1 or R2:R3)
- **Pointers**: always 32-bit on a 32-bit ARM, use `LDR` or `MOV`

---

## Getting the Return Value from the Callee

After `bl callee`, save the return value immediately before it gets lost:
- **Up to 32-bit return**: use `STR`, `STRH`, or `STRB` to save R0
- **64-bit return**: use `STRD` to save R0:R1

---

## Demo: Modulo Operation (Leaf + Stem)

### Leaf: `mp_umod_32bit_s` -- computes `x % y`
```asm
@ uint32_t mp_umod_32bit_s(uint32_t x, uint32_t y)
@ x -> r0, y -> r1, return in r0
mp_umod_32bit_s:
    udiv  r2, r0, r1       @ r2 = x / y
    mls   r0, r1, r2, r0   @ r0 = x - (x/y)*y = x % y
    bx    lr
```
No need to preserve environment -- only uses R0-R2.

### Stem: `mp_umod_32bit_array_s` -- computes `z[i] = x[i] % y[i]`
```asm
@ void mp_umod_32bit_array_s(uint32_t *x, uint32_t *y, uint32_t *z, int n)
@ x->r0, y->r1, z->r2, n->r3
mp_umod_32bit_array_s:
    push    {r4-r8, lr}
    mov     r4, r0          @ Save x
    mov     r5, r1          @ Save y
    mov     r6, r2          @ Save z
    mov     r7, r3          @ Save n
    ldr     r8, =0          @ i = 0
loop:
    cmp     r8, r7          @ i < n?
    bge     end_loop
    ldr     r0, [r4, r8, lsl #2]   @ x[i] -> r0
    ldr     r1, [r5, r8, lsl #2]   @ y[i] -> r1
    bl      mp_umod_32bit_s        @ call leaf
    str     r0, [r6, r8, lsl #2]   @ z[i] = return value
    add     r8, #1                  @ i++
    b       loop
end_loop:
    pop     {r4-r8, pc}
```

### 16-bit variant: only change LDR/STR to LDRH/STRH
```asm
    ldrh    r0, [r4, r8, lsl #1]   @ x[i] (16-bit)
    ldrh    r1, [r5, r8, lsl #1]   @ y[i] (16-bit)
    bl      mp_umod_32bit_s        @ same leaf works (handles up to 32 bits)
    strh    r0, [r6, r8, lsl #1]   @ z[i] = result (16-bit)
```

---

## Demo: 64-bit Addition (Leaf + Stem)

### Leaf: `mp_add_64bit_s` -- computes 64-bit `x + y`
```asm
@ int64_t mp_add_64bit_s(int64_t x, int64_t y)
@ x -> r1:r0, y -> r3:r2, return in r1:r0
mp_add_64bit_s:
    adds  r0, r2       @ Add lower 32 bits (set carry)
    adc   r1, r3       @ Add upper 32 bits + carry
    bx    lr
```

### Stem: `mp_add_64bit_array_s` -- computes `z[i] = x[i] + y[i]`
Uses LDRD/STRD with post-indexed `#8` to step through 64-bit elements:
```asm
mp_add_64bit_array_s:
    push    {r4-r7, lr}
    mov     r4, r0          @ Save x ptr
    mov     r5, r1          @ Save y ptr
    mov     r6, r2          @ Save z ptr
    mov     r7, r3          @ Save n
loop:
    cmp     r7, #0
    ble     end_loop
    ldrd    r0, r1, [r4], #8   @ x[i] -> r1:r0, advance x ptr
    ldrd    r2, r3, [r5], #8   @ y[i] -> r3:r2, advance y ptr
    bl      mp_add_64bit_s
    strd    r0, r1, [r6], #8   @ z[i] = r1:r0, advance z ptr
    sub     r7, #1             @ n--
    b       loop
end_loop:
    pop     {r4-r7, pc}
```

Key: uses **post-indexed LDRD/STRD** with `#8` offset to advance pointers by 8 bytes (one 64-bit element) each iteration.
