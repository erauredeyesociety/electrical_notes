# Lecture 21: Additional Load and Store Instructions and Move Instructions

## Review: Immediate-Offset Instructions (from Lctr 20)

| Offset type | Load syntax | Store syntax |
|---|---|---|
| Basic | `LDR{type} Rv, [Ra{, #os}]` | `STR{type} Rv, [Ra{, #os}]` |
| Pre-indexed | `LDR{type} Rv, [Ra, #os]!` | `STR{type} Rv, [Ra, #os]!` |
| Post-indexed | `LDR{type} Rv, [Ra], #os` | `STR{type} Rv, [Ra], #os` |

Where `type` = `B`, `SB`, `H`, `SH`, or omitted (word).

---

## Register-Offset Load Instructions

Replace the immediate `#os` with a register-based operand `Ri, LSL #n`.

### 32-bit register-offset load

```
LDR Rv, [Ra, Ri, LSL #2]
```
- Equivalent C: `var = *(p32 + i)` where Rv=var, Ra=p32, Ri=i
- The `LSL #2` shifts Ri left by 2 (multiplies by 4) because each word is 4 bytes
- To load every OTHER element: `LDR Rv, [Ra, Ri, LSL #3]` (offset = 8*i)

### 16-bit register-offset load

| C type | Instruction |
|--------|------------|
| `uint16_t` | `LDRH Rv, [Ra, Ri, LSL #1]` |
| `int16_t` | `LDRSH Rv, [Ra, Ri, LSL #1]` |

The `LSL #1` multiplies index by 2 (each halfword = 2 bytes).

### 8-bit register-offset load

| C type | Instruction |
|--------|------------|
| `uint8_t` | `LDRB Rv, [Ra, Ri]` |
| `int8_t` | `LDRSB Rv, [Ra, Ri]` |

No shift needed -- each byte = 1 byte.

---

## Register-Offset Store Instructions

| Size | Instruction |
|------|------------|
| 32-bit | `STR Rv, [Ra, Ri, LSL #2]` |
| 16-bit | `STRH Rv, [Ra, Ri, LSL #1]` |
| 8-bit | `STRB Rv, [Ra, Ri]` |

**Important**: For stores, we only save the least significant halfword (STRH) or byte (STRB) from Rv.

---

## Example: Translating C stores to ASM (register-offset)

C function:
```c
void mp_store_for_different_types_c(uint32_t *p32, int i, int var32) {
    *(p32 + i) = var32;           // 32-bit store
    *((uint16_t *)p32 + i) = var32;  // 16-bit store
    *((uint8_t *)p32 + i) = var32;   // 8-bit store
}
```

ASM (R0=p32, R1=i, R2=var32):
```asm
str   r2, [r0, r1, lsl #2]   @ 32-bit: offset = i*4
strh  r2, [r0, r1, lsl #1]   @ 16-bit: offset = i*2
strb  r2, [r0, r1]            @ 8-bit:  offset = i*1
bx    lr
```

---

## Non-standard offset detection

If a register-offset load skips a non-standard number of bytes for its data type, it is "non-standard":
- 32-bit load with `LSL #1` skips 2 bytes per index (standard is 4) -- non-standard
- 16-bit load with `LSL #2` skips 4 bytes per index (standard is 2) -- non-standard

---

## L1 Norm Example (pointer-update vs register-offset)

### Pointer-update approach (modifies the pointer)
C: `int temp = *pArr++;`
ASM: `ldr r4, [r0], #4` (post-indexed, advances pointer by 4)

### Register-offset approach (pointer stays constant)
C: `int temp = *(pArr + i);`
ASM: `ldr r4, [r0, r3, lsl #2]` (r3 = index i)

Key difference: pointer-update uses post-indexed `[r0], #4`; register-offset uses `[r0, r3, lsl #2]` with a separate counter.

---

## Move Instructions

| Instruction | Description |
|-------------|-------------|
| `MOV Rt, Op2` | Move value of Op2 (register or small immediate) to Rt |
| `MOVW Rd, #xyz_16` | Move 16-bit immediate to bottom half [15:0], clear top half [31:16] |
| `MOVT Rd, #xyz_16` | Move 16-bit immediate to top half [31:16], bottom half unchanged |

In practice, use `MOV Rt, Rs` for register-to-register moves. For loading constants, use `LDR Rt, =expr` (the pseudo load instruction).

---

## Pseudo Load Instruction: `LDR Rd, =num_or_label`

The assembler translates `LDR Rd, =value` differently depending on the value:
- **Small values** (fits in 8 bits): translated to `MOV` (e.g., `ldr r1, =0xEE` becomes `mov.w r1, #238`)
- **16-bit values**: translated to `MOVW` (e.g., `ldr r2, =0xBEEF` becomes `movw r2, #48879`)
- **Large values** (>16 bits): translated to a PC-relative `LDR` that reads from a literal pool at the end of the code (e.g., `ldr r3, =0xDEADBEEF` becomes `ldr r3, [pc, #28]` pointing to `.word 0xDEADBEEF`)
- **Labels**: same as large values -- loads the address from the literal pool

---

## Contrasting Post-Indexed vs Register-Offset Store

Two C approaches to initialize a memory block:
1. **Pointer update** (`*pArr++ = val`): uses post-indexed `strb r4, [r0], #1`
2. **Index variable** (`*(pArr + i) = val`): uses register-offset `strb r4, [r0, r2]`

The pointer-update version cannot use a `const` pointer. The index version can.
