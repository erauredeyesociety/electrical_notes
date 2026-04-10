# HW 10 - References and Expanded Lecture Notes

This document provides expanded explanations of the key concepts used in HW 10, with direct references to the course lecture slides.

---

## 1. Immediate-Offset Load and Store Instructions (Lctr 20)

**Source:** `mp-gc-lctr20-imd-offset-ldr-n-str-n-macro-slides-26-03.pdf`

### 1.1 The Three Forms of LDR/STR

There are three forms of immediate-offset addressing, each corresponding to a different C pointer operation (Lctr 20, pp. 2-3):

| Form | Syntax | Operation | C Equivalent |
|------|--------|-----------|-------------|
| **Basic** | `LDR{type} Rv, [Ra{, #os}]` | Load from `Ra + os`, Ra unchanged | `var = *(ptr + k)` |
| **Pre-indexed** | `LDR{type} Rv, [Ra, #os]!` | First `Ra = Ra + os`, then load from `Ra` | `var = *++ptr` or `var = *--ptr` |
| **Post-indexed** | `LDR{type} Rv, [Ra], #os` | First load from `Ra`, then `Ra = Ra + os` | `var = *ptr++` or `var = *ptr--` |

**How to remember** (Lctr 20, p. 3):
- `[r1, #4]` — nothing after bracket, address register NOT updated
- `[r1, #4]!` — exclamation mark = urgently update BEFORE using it
- `[r1], #4` — number trails after bracket = update AFTER the main business

**Used in HW 10:**
- **Problem 1, Part 3:** Post-indexed `strb r2, [r1], #1` implements `*p8b++` — stores the byte and then increments the destination pointer. Basic offset `ldrb r2, [r0, #2]` implements `*(p8a + 2)` — reads from a constant offset without changing the source pointer.
- **Problem 2, Task 1:** Pre-indexed `ldrd r2, r3, [r0, #8]!` advances `r0` by 8 before loading the double word.
- **Problem 2, Task 3:** Post-indexed `ldrsh r2, [r0], #10` loads the halfword first, then advances `r0` by 10.

### 1.2 Data Type Suffixes for Load Instructions

The load instruction can work with different data sizes (Lctr 20, pp. 8-11):

| Suffix | Data Type | Extension | C Type |
|--------|-----------|-----------|--------|
| (none) | 32-bit word | None needed | `int32_t`, `uint32_t` |
| `B` | Unsigned byte | Zero-extend to 32 bits | `uint8_t` |
| `SB` | Signed byte | Sign-extend to 32 bits | `int8_t` |
| `H` | Unsigned halfword | Zero-extend to 32 bits | `uint16_t` |
| `SH` | Signed halfword | Sign-extend to 32 bits | `int16_t` |

**Sign extension explained:**
- A byte `0x40` (bit 7 = 0): `LDRSB` extends to `0x00000040` (positive)
- A byte `0x80` (bit 7 = 1): `LDRSB` extends to `0xFFFFFF80` (negative, = -128)
- A halfword `0x1000` (bit 15 = 0): `LDRSH` extends to `0x00001000` (positive)
- A halfword `0xB0A0` (bit 15 = 1): `LDRSH` extends to `0xFFFFB0A0` (negative)

**Used in HW 10:**
- **Problem 1:** `LDRB` / `STRB` for `uint8_t` pointer operations (each element is 1 byte, so offset = index).
- **Problem 2, Task 2:** `LDRSB` sign-extends bytes to 32-bit values — this is why `0x80` becomes `0xFFFFFF80`.
- **Problem 2, Task 3:** `LDRSH` sign-extends halfwords — `0xB0A0` becomes `0xFFFFB0A0`.
- **Problem 2, Task 4:** `LDRH` zero-extends halfwords — `0x3020` stays `0x00003020`.

### 1.3 C-to-ASM Equivalence Tables

**Load operations** (Lctr 20, p. 11):

| C Code | ASM Instruction | Note |
|--------|----------------|------|
| `var = *(pu8 + k)` | `ldrb r0, [r1, #os]` | `os = k` |
| `var = *++pu8` | `ldrb r0, [r1, #1]!` | Pre-indexed |
| `var = *pu8++` | `ldrb r0, [r1], #1` | Post-indexed |
| `var = *(pi8 + k)` | `ldrsb r0, [r1, #os]` | `os = k`, sign-extend |
| `var = *(pu16 + k)` | `ldrh r0, [r1, #os]` | `os = 2*k` |
| `var = *pu16++` | `ldrh r0, [r1], #2` | Post-indexed, step = 2 |
| `var = *(pi16 + k)` | `ldrsh r0, [r1, #os]` | `os = 2*k`, sign-extend |

**Store operations** (Lctr 20, pp. 12-13) — note that stores do NOT have signed/unsigned variants:

| C Code | ASM Instruction | Note |
|--------|----------------|------|
| `*(p8 + k) = var` | `strb r0, [r1, #os]` | `os = k` |
| `*p8++ = var` | `strb r0, [r1], #1` | Post-indexed |
| `*p16++ = var` | `strh r0, [r1], #2` | Post-indexed, step = 2 |

**Used in HW 10:**
- **Problem 1, Part 3:** Every line of the assembly solution directly maps to entries in these tables.

---

## 2. Register-Offset Load and Store Instructions (Lctr 21)

**Source:** `mp-ge-lctr21-more-ldr-n-str-n-mov-slides-26-03.pdf`

### 2.1 Register-Offset Addressing

Instead of an immediate constant for the offset, we use a register with an optional shift (Lctr 21, pp. 3-4):

| Data Type | Load Instruction | Shift |
|-----------|-----------------|-------|
| 32-bit word | `LDR Rv, [Ra, Ri, LSL #2]` | `Ri * 4` bytes |
| 16-bit halfword | `LDRH Rv, [Ra, Ri, LSL #1]` | `Ri * 2` bytes |
| 8-bit byte | `LDRB Rv, [Ra, Ri]` | `Ri * 1` byte |

The shift value matches the size of the data type:
- `LSL #2` for words (4 bytes) → equivalent to `*(p32 + i)`
- `LSL #1` for halfwords (2 bytes) → equivalent to `*(p16 + i)`
- No shift for bytes (1 byte) → equivalent to `*(p8 + i)`

**Used in HW 10:**
- **Problem 2, Task 4:** `ldrh r3, [r0, r2, LSL #1]` loads an unsigned halfword from `ipt + r2 * 2`. The `LSL #1` matches the 2-byte size of a halfword. With `r2 = 1`, this reads from `ipt + 2`; with `r2 = 2`, from `ipt + 4`.

---

## 3. Increment Operations for C Variables and Pointers (Lctr 22)

**Source:** `mp-gg-lctr22-incr-ops-4-c-vars-n-ptrs-n-impl-in-asm-slides-26-04.pdf`

### 3.1 C Operator Precedence (Relevant Subset)

From the precedence table (Lctr 22, pp. 2-3):

| Precedence | Operators | Description | Associativity |
|------------|-----------|-------------|---------------|
| 1 (highest) | `()` `[]` `.` `->` `++` `--` (postfix) | Grouping, subscript, postfix inc/dec | Left to right |
| 2 | `++` `--` (prefix), `+` `-` (unary), `*` `&` `(type)` | Prefix inc/dec, dereference, address-of | **Right to left** |
| 14 (low) | `=` `+=` `-=` ... | Assignment | Right to left |

**Key insight for Problem 1:** In the expression `++*p8a++`:
1. **Postfix `++`** on `p8a` has **precedence 1** (highest) → `p8a++` returns old pointer value, then advances pointer
2. **Dereference `*`** has **precedence 2** → `*p8a` reads the byte at the old pointer address
3. **Prefix `++`** has **precedence 2**, right-to-left → `++(*p8a)` increments the loaded value and writes it back

### 3.2 Prefix vs. Postfix Increment

From Lctr 22, p. 4:

**Prefix `++A[0]`:** Increment happens BEFORE the value is used in the expression.
```
// Before: A[0] = 0
B[0] = ++A[0];
// After: A[0] = 1, B[0] = 1
```

**Postfix `A[1]++`:** The original value is used in the expression, increment happens AFTER.
```
// Before: A[1] = 1
B[1] = A[1]++;
// After: A[1] = 2, B[1] = 1
```

**ASM implementation** (Lctr 22, p. 5):
```asm
@ B[0] = ++A[0]:
ldr  r2, [r0]       @ temp = A[0]
add  r2, #1         @ temp++
str  r2, [r0]       @ A[0] = temp  (write back)
str  r2, [r1]       @ B[0] = temp  (use incremented value)

@ B[1] = A[1]++:
ldr  r2, [r0, #4]   @ temp = A[1]
str  r2, [r1, #4]   @ B[1] = temp  (use original value)
add  r2, #1         @ temp++
str  r2, [r0, #4]   @ A[1] = temp  (write back)
```

**Used in HW 10:**
- **Problem 1, Line 5:** `++*(p8a + 4)` is a prefix increment on the dereferenced value at `p8a + 4`. The value `0x08` is incremented to `0x09` before being assigned.
- **Problem 1, Line 6:** `++*p8a++` combines postfix pointer increment with prefix value increment.
- **Problem 1, Line 7:** `*p8a++` is a simple postfix pointer increment — use the current value, then advance.

### 3.3 Pointer Increment and Data Type Size

From Lctr 22, pp. 9-10:

When you increment a pointer, the address changes by `sizeof(*pointer)`:
- `uint8_t *p8`:  `p8++` adds **1 byte** to the address
- `int16_t *p16`: `p16++` adds **2 bytes** to the address
- `int32_t *p32`: `p32++` adds **4 bytes** to the address

This is why in **Problem 1**, where pointers are `uint8_t *`, every `p8a++` or `p8b++` advances the pointer by exactly 1 byte — matching the post-indexed `#1` in the assembly.

---

## 4. LDRD and STRD Instructions (Lctr 23)

**Source:** `mp-gm-lctr23-calling-asm-fns-in-asm-fn-slides-26-04.pdf`

### 4.1 Double-Word Load and Store

LDRD and STRD load/store 8 consecutive bytes (64 bits) using two registers (Lctr 23, pp. 3-4):

| Form | Syntax |
|------|--------|
| Basic | `LDRD Rv_L, Rv_H, [Ra{, #os}]` |
| Pre-indexed | `LDRD Rv_L, Rv_H, [Ra, #os]!` |
| Post-indexed | `LDRD Rv_L, Rv_H, [Ra], #os` |

- `Rv_L` gets the word at the **lower** address (first 4 bytes)
- `Rv_H` gets the word at the **higher** address (next 4 bytes)
- ARM is little-endian: the least significant byte is at the lowest address

**Used in HW 10:**
- **Problem 2, Task 1:** `ldrd r2, r3, [r0, #8]!` loads 8 bytes from `ipt+8`:
  - `r2 = 0xB0A09080` (bytes at `ipt+8` through `ipt+11`)
  - `r3 = 0xF0E0D0C0` (bytes at `ipt+12` through `ipt+15`)
- **All tasks use** `strd r2, r3, [r1, #0]` to store the two 32-bit results into `opt[0]` and `opt[1]`.

---

## 5. Little-Endian Byte Ordering

ARM processors use **little-endian** byte ordering by default. This means:

- The **least significant byte** (LSB) is stored at the **lowest** address.
- When loading a 32-bit word from address `A`, the bytes are assembled as:

```
Word = byte[A] | (byte[A+1] << 8) | (byte[A+2] << 16) | (byte[A+3] << 24)
```

**Example from Problem 2:** The `ipt` array at `ipt+8`:
```
Address:  ipt+8   ipt+9   ipt+10  ipt+11
Byte:     0x80    0x90    0xA0    0xB0
```
When loaded as a 32-bit word: `0xB0A09080`
- `0x80` is at the lowest address = least significant byte
- `0xB0` is at the highest address = most significant byte

---

## 6. ARM Calling Convention (AAPCS) — Quick Reference

From Lctr 23, pp. 2, 7:

| Register | Usage | Preserved? |
|----------|-------|-----------|
| R0-R3 | Arguments and return value | No (caller-saved) |
| R4-R11 | General purpose | Yes (callee-saved via PUSH/POP) |
| R12 | Scratch | No |
| R13 (SP) | Stack pointer | Yes |
| R14 (LR) | Link register (return address) | Saved if calling other functions |
| R15 (PC) | Program counter | N/A |

**For HW 10 function calls:**
- `task1(ipt, opt)`: `r0 = ipt`, `r1 = opt`
- `task4(ipt, opt, 1)`: `r0 = ipt`, `r1 = opt`, `r2 = 1`
- `my_fn(p8a, p8b)`: `r0 = p8a`, `r1 = p8b`

---

## 7. Summary: Mapping Each HW Problem to Lecture Material

| Problem | Key Concepts | Primary Lecture Reference |
|---------|-------------|-------------------------|
| 1.1 | C operator precedence, prefix/postfix on values vs. pointers | Lctr 22, Sec 22.1-22.2 |
| 1.2 | Tracing pointer writes through memory | Lctr 20, Sec 20.2; Lctr 22, Sec 22.3 |
| 1.3 | Translating C pointer ops to LDRB/STRB with post-indexing | Lctr 20, Sec 20.2-20.4 (tables on pp. 11, 13) |
| 2a | LDRD pre-indexed, little-endian word loading | Lctr 23, Sec 23.2 |
| 2b | LDRSB pre-indexed, sign extension of bytes | Lctr 20, Sec 20.3 |
| 2c | LDRSH post-indexed, sign extension of halfwords | Lctr 20, Sec 20.3; Lctr 21, Sec 21.1 |
| 2d | LDRH register-offset with LSL, zero extension | Lctr 21, Sec 21.2 |
| 2e | Reverse-engineering ASM back to C pointer code | Lctr 20-23 (all sections on C-ASM equivalence) |
