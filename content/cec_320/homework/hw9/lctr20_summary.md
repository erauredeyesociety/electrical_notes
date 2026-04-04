# Lecture 20: Immediate-Offset Load and Store Instructions and Macro

## Key Concepts

Two registers are central to all load/store instructions:
- **Ra** = address register (holds the pointer / memory address)
- **Rv** = value register (holds the data being loaded or stored)

---

## Immediate-Offset LDR (Load) Instructions

### Three addressing modes for LDR

| Mode | Syntax | Behavior |
|------|--------|----------|
| **Basic** | `LDR Rv, [Ra{, #os}]` | Load from address Ra+os. Ra unchanged. |
| **Pre-indexed** | `LDR Rv, [Ra, #os]!` | First Ra = Ra+os, then load from [Ra]. (Ra updated BEFORE use) |
| **Post-indexed** | `LDR Rv, [Ra], #os` | Load from [Ra], then Ra = Ra+os. (Ra updated AFTER use) |

### How to remember the notation
- `ldr r0, [r1, #4]` -- no `!`, nothing after bracket --> Ra NOT updated
- `ldr r0, [r1, #4]!` -- exclamation mark = "urgent" --> Ra updated BEFORE the load
- `ldr r0, [r1], #4` -- offset trails after bracket --> Ra updated AFTER the load

### C-to-ASM mapping (32-bit, assuming R0=var, R1=p32)
- `var = *(p32 + k)` --> `ldr r0, [r1, #os]` where os = 4*k
- `var = *++p32` --> `ldr r0, [r1, #4]!`
- `var = *--p32` --> `ldr r0, [r1, #-4]!`
- `var = *p32++` --> `ldr r0, [r1], #4`
- `var = *p32--` --> `ldr r0, [r1], #-4`

---

## Data Type Suffixes for LDR

| Suffix | Type | Extension | C Type |
|--------|------|-----------|--------|
| (none) | 32-bit word | none | `uint32_t` / `int32_t` |
| `B` | unsigned byte | zero-extend | `uint8_t` |
| `SB` | signed byte | sign-extend | `int8_t` |
| `H` | unsigned halfword | zero-extend | `uint16_t` |
| `SH` | signed halfword | sign-extend | `int16_t` |

### Sign/zero extension examples
- `LDRB`: byte 0xFF --> word 0x0000_00FF (255)
- `LDRSB`: byte 0xFF --> word 0xFFFF_FFFF (-1); byte 0x7F --> 0x0000_007F (127)
- `LDRH`: halfword 0xFFFF --> 0x0000_FFFF (65535)
- `LDRSH`: halfword 0xFFFF --> 0xFFFF_FFFF (-1); halfword 0x7FFF --> 0x0000_7FFF (32767)

---

## Offset Calculation by Data Type

The offset in bytes depends on the element size:
- **32-bit** (`int32_t *p32`): `os = 4*k`
- **16-bit** (`int16_t *p16`): `os = 2*k`
- **8-bit** (`int8_t *p8`): `os = k`

### C-to-ASM for 8-bit and 16-bit (R0=var, R1=address)

| C expression | ASM instruction | Offset note |
|---|---|---|
| `var = *(pu8 + k)` | `ldrb r0, [r1, #os]` | os = k |
| `var = *(pi8 + k)` | `ldrsb r0, [r1, #os]` | os = k |
| `var = *(pu16 + k)` | `ldrh r0, [r1, #os]` | os = 2*k |
| `var = *(pi16 + k)` | `ldrsh r0, [r1, #os]` | os = 2*k |

Pre-indexed and post-indexed work the same way -- just change the offset to match the element size (1 for byte, 2 for halfword, 4 for word).

### Complete C-to-LDR reference table (8/16-bit, R0=var, R1=ptr)

| C operation | LDR instruction |
|---|---|
| `var = *++pu8` | `ldrb r0, [r1, #1]!` |
| `var = *pu8++` | `ldrb r0, [r1], #1` |
| `var = *++pi8` | `ldrsb r0, [r1, #1]!` |
| `var = *pi8++` | `ldrsb r0, [r1], #1` |
| `var = *++pu16` | `ldrh r0, [r1, #2]!` |
| `var = *pu16++` | `ldrh r0, [r1], #2` |
| `var = *++pi16` | `ldrsh r0, [r1, #2]!` |
| `var = *pi16++` | `ldrsh r0, [r1], #2` |

---

## Immediate-Offset STR (Store) Instructions

Store instructions mirror load instructions. Key difference: **no signed/unsigned distinction for stores** -- only `STR`, `STRH`, `STRB` (the programmer must put the right value in the lower bits).

### Three addressing modes for STR

| Mode | Syntax | Behavior |
|------|--------|----------|
| **Basic** | `STR{type} Rv, [Ra{, #os}]` | Store Rv to address Ra+os. Ra unchanged. |
| **Pre-indexed** | `STR{type} Rv, [Ra, #os]!` | Ra = Ra+os first, then store Rv to [Ra]. |
| **Post-indexed** | `STR{type} Rv, [Ra], #os` | Store Rv to [Ra], then Ra = Ra+os. |

Where `{type}` is `H` (halfword) or `B` (byte) or omitted (word).

### C-to-STR reference table (R0=var, R1=ptr)

| C operation | STR instruction | Note |
|---|---|---|
| `*(p32+k) = var` | `str r0, [r1, #os]` | os = 4*k |
| `*++p32 = var` | `str r0, [r1, #4]!` | |
| `*p32++ = var` | `str r0, [r1], #4` | |
| `*(p16+k) = var` | `strh r0, [r1, #os]` | os = 2*k |
| `*++p16 = var` | `strh r0, [r1, #2]!` | |
| `*p16++ = var` | `strh r0, [r1], #2` | |
| `*(p8+k) = var` | `strb r0, [r1, #os]` | os = k |
| `*++p8 = var` | `strb r0, [r1, #1]!` | |
| `*p8++ = var` | `strb r0, [r1], #1` | |

---

## Quick Reference: Load vs Store by Data Type

| Size | Load unsigned | Load signed | Store |
|------|-------------|------------|-------|
| 32-bit | `ldr r0, [r1]` | `ldr r0, [r1]` | `str r0, [r1]` |
| 16-bit | `ldrh r0, [r1]` | `ldrsh r0, [r1]` | `strh r0, [r1]` |
| 8-bit | `ldrb r0, [r1]` | `ldrsb r0, [r1]` | `strb r0, [r1]` |
