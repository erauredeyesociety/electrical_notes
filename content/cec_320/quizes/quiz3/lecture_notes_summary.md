# CEC 320 Quiz 3 - Lecture Notes Summary (Lectures 14-18)

---

## Lecture 14: Mixed C and ASM Programming

### ARM Cortex-M Core Registers

| Register | Name | Purpose |
|----------|------|---------|
| R0-R7 | Low registers | General-purpose. Some 16-bit instructions can only use these. |
| R8-R12 | High registers | General-purpose. Some have special designated uses. |
| R13 (SP) | Stack Pointer | Points to top of stack. Two SPs exist: MSP and PSP. |
| R14 (LR) | Link Register | Holds return address when a function is called. |
| R15 (PC) | Program Counter | Address of the next instruction to execute. |

- **MSP** (Main Stack Pointer): used by interrupt handlers and the main super loop when no RTOS.
- **PSP** (Process Stack Pointer): used by user tasks/threads under an RTOS.

### EABI Calling Convention

- **R0-R3**: pass up to four 32-bit arguments. Arg1 -> R0, Arg2 -> R1, etc.
- **R0**: holds the 32-bit return value.
- 64-bit argument: lower word in R0, upper word in R1 (little-endian).
- 64-bit return: lower word in R0, upper word in R1.
- **R0-R3 do not need to be preserved** by the callee (caller's responsibility).
- **R4+ must be preserved** by the callee if used (push/pop on stack).

### Returning from a Function

1. `bx lr` -- when LR is not stacked.
2. `pop {pc}` -- when LR was pushed to the stack (pop LR value directly into PC).
   - `pop {r4, r6, r8-r10, pc}` is equivalent to `pop {r4, r6, r8-r10, lr}` + `bx lr`.

### Stack (Full Descending)

- **Full**: SP points to the last pushed data item (not an empty slot).
- **Descending**: pushing decrements SP (by 4 per word); popping increments SP.
- `push {r4}` -- save R4 to stack, SP decrements by 4.
- `pop {r4}` -- restore R4 from stack, SP increments by 4.
- Multi-register push: `push {r6, r4, r8-r10, lr}` -- lower-numbered registers are stored at lower addresses regardless of order in the braces.

### ASM File Structure Directives

| Directive | Purpose |
|-----------|---------|
| `.section .text` | Define program (code) section |
| `.syntax unified` | Use Thumb-2 instructions |
| `.align` | Align to memory boundary (always use it) |
| `.global func_name` | Make symbol visible to linker |
| `.type func_name, %function` | Declare symbol as a function |
| `.fnstart` / `.fnend` | Optional function boundary markers |
| `.end` | End of file |

### Instruction Format

```
a_label:
    add  r0, r1, r2   @ r0 = r1 + r2
```
- Label: no whitespace before it. Mnemonic: must have whitespace before it.
- `{Rd,}` notation: destination register can be omitted if same as first source.
- Second operand (Op2) can be: register, immediate number, or shifted register (**flexible operand 2**).
- Comments: `@ comment` or C-style `/* comment */`.

### GNU ASM vs ARMASM

- **GNU (CubeIDE)**: lowercase for instructions and registers (code snippets).
- **ARMASM (ARM docs)**: uppercase (text/documentation).

### Type-Casting Rules

- Narrow to wider type: value is preserved (sign-extended or zero-extended as appropriate).
- Same width signed/unsigned: no data change, just reinterpretation.
- **Wide to narrow: lose most significant bytes.**

### Instruction Classification

- Arithmetic & logic (ADD, SUB, MUL, shift, rotate, bitwise)
- Data movement (LDR, STR, MOV)
- Compare & branch
- Floating-point arithmetic
- Miscellaneous (breakpoints, barriers, interrupt control)
- Common pattern: **load, modify, store**

---

## Lecture 15: Arithmetic Instructions

### xPSR - Program Status Registers

- **APSR** (Application): N, Z, C, V, Q flags
- **IPSR** (Interrupt)
- **EPSR** (Execution)

### APSR Status Flags

| Bit | Flag | Meaning |
|-----|------|---------|
| 31 | N | Negative -- MSB of result is 1 |
| 30 | Z | Zero -- result is 0 |
| 29 | C | Carry/Borrow |
| 28 | V | Overflow (signed) |
| 27 | Q | Saturation |

### C Flag Rules

- **Unsigned addition**: C = 1 if carry (result > 2^N - 1); else C = 0.
- **Unsigned subtraction**: C = 1 - B (where B = borrow).
  - No borrow (B=0): C = 1.
  - Borrow (B=1): C = 0.

### Multi-Word Number Representation

- Only the most significant word retains its original type (signed or unsigned).
- All other (lower) words are treated as unsigned.
- Process from least significant to most significant word.
- C flag carries from lower word operations to upper word operations.

### Loading an Immediate Number

```
ldr  rd, =an_immediate_num    @ virtual LDR instruction
```

### 32-bit Addition & Subtraction (Without Carry)

| Instruction | Operation |
|-------------|-----------|
| `ADD {Rd,} Rn, Op2` | Rd <- Rn + Op2 |
| `SUB {Rd,} Rn, Op2` | Rd <- Rn - Op2 |
| `RSB {Rd,} Rn, Op2` | Rd <- Op2 - Rn (reverse subtract) |

- `{Rd,}` means Rd can be omitted if Rd == Rn.
- `add r0, r0, #1` is equivalent to `add r0, #1`.
- `sub r0, r0, #1` is equivalent to `sub r0, #1`.
- **RSB** exists because Rn must be a register (cannot be immediate). To compute `1 - a`, use `rsb r0, r0, #1`.
- Negation: `rsb r1, r0, #0` computes `r1 = -r0`.

### S Suffix (Status Flag Update)

- `ADDS`, `SUBS` update the status flags (including C flag). Non-S versions do not.
- Many S versions are 16-bit instructions (more compact code).
- Some applications require the non-S version (when you must not disturb flags).

### 32-bit Addition & Subtraction (With Carry)

| Instruction | Operation |
|-------------|-----------|
| `ADC {Rd,} Rn, Op2` | Rd <- Rn + Op2 + C |
| `SBC {Rd,} Rn, Op2` | Rd <- Rn - Op2 + C - 1 |

#### 64-bit Addition Pattern (a = a + b)

```
@ x -> r1:r0, y -> r3:r2, result -> r1:r0
adds  r0, r2       @ lower word add, sets C flag
adc   r1, r3       @ upper word add with carry
bx    lr
```

#### 64-bit Subtraction with SBC

- If R0 >= R2 (no borrow): C=1, so `sbc r1, r3` = r1 - r3.
- If R0 < R2 (borrow): C=0, so `sbc r1, r3` = r1 - r3 - 1.

### 32-bit Multiplication & Accumulation

| Instruction | Operation |
|-------------|-----------|
| `MUL {Rd,} Rn, Rm` | Rd <- Rn * Rm (lower 32 bits) |
| `MLA Rd, Rn, Rm, Ra` | Rd <- Ra + Rn * Rm |
| `MLS Rd, Rn, Rm, Ra` | Rd <- Ra - Rn * Rm |

- MUL, MLA, MLS work for both signed and unsigned (lower 32 bits are the same).

### 32-bit Division

| Instruction | Operation |
|-------------|-----------|
| `UDIV {Rd,} Rn, Rm` | Rd <- Rn / Rm (unsigned) |
| `SDIV {Rd,} Rn, Rm` | Rd <- Rn / Rm (signed) |

- Division **requires separate instructions** for signed vs unsigned (results differ).
- Division has **no S version** and cycle count is not constant.

### Remainder (Modulo) Implementation

```
@ x % y = x - (x/y)*y
@ uint32_t mp_umod_32bit_s(uint32_t x, uint32_t y)
@ r0 = x, r1 = y
udiv  r2, r0, r1       @ r2 = x / y
mls   r0, r1, r2, r0   @ r0 = x - y * r2
bx    lr
```

### 64-bit (32x32->64) Multiplication & Accumulation

| Instruction | Operation |
|-------------|-----------|
| `UMULL RdLo, RdHi, Rn, Rm` | (RdHi:RdLo) <- Rn * Rm (unsigned) |
| `SMULL RdLo, RdHi, Rn, Rm` | (RdHi:RdLo) <- Rn * Rm (signed) |
| `UMLAL RdLo, RdHi, Rn, Rm` | (RdHi:RdLo) += Rn * Rm (unsigned) |
| `SMLAL RdLo, RdHi, Rn, Rm` | (RdHi:RdLo) += Rn * Rm (signed) |

### 64-bit Argument Passing

- 64-bit arg: lower word in R0, upper word in R1.

---

## Lecture 16: Shift and Rotation Instructions, Op2, and Applications

### C Shift Operators (Precedence 5, Left-to-Right)

| Operator | Description |
|----------|-------------|
| `<<` | Left shift (0s fill from LSB). Multiplies by 2^n. May overflow. |
| `>>` | Right shift. Unsigned: 0s from MSB. Signed: MSB repeated (arithmetic). |

### 32-bit Shift Instructions

| Instruction | Operation |
|-------------|-----------|
| `LSL {Rd,} Rn, Rm (or #n)` | Logic shift left: Rd <- Rn << Rm (or #n) |
| `LSR {Rd,} Rn, Rm (or #n)` | Logic shift right: Rd <- (unsigned Rn) >> Rm (or #n) |
| `ASR {Rd,} Rn, Rm (or #n)` | Arithmetic shift right: Rd <- (signed Rn) >> Rm (or #n) |

- **LSL**: used for both unsigned and signed left shift. 0 fills from LSB. Last bit shifted out goes to C flag.
- **LSR**: unsigned right shift only. 0 fills from MSB. Last bit shifted out goes to C flag.
- **ASR**: signed right shift only. MSB (sign bit) repeats. Last bit shifted out goes to C flag.
- All have S versions (`LSLS`, `LSRS`, `ASRS`) that update N, Z, and C flags.

### Shift Examples

```
lsl  r1, r2           @ r1 = r1 << r2
lsl  r1, #3           @ r1 = r1 << 3
lsl  r1, r2, #3       @ r1 = r2 << 3
lsl  r1, r2, r3       @ r1 = r2 << r3
lsls r1, r2, r3       @ r1 = r2 << r3, N/Z/C flags updated
lsr  r1, r2, r3       @ r1 = r2 >> r3 (unsigned)
asr  r1, r2, r3       @ r1 = r2 >> r3 (signed)
```

### Q31 Multiplication

- `q31_t` = `int32_t`, `q63_t` = `int64_t`.
- C formula: `return (q31_t)((q63_t)A * B >> 31);`

#### Fast Q31 Multiply (2 instructions, loses 1 bit of accuracy)

```
smull  r1, r0, r0, r1   @ (r0:r1) = r0 * r1 (64-bit signed)
lsl    r0, #1            @ shift HW left by 1 (approximates >>31)
bx     lr
```

#### Accurate Q31 Multiply (4 instructions)

```
smull  r1, r0, r0, r1
lsl    r0, #1
lsls   r1, #1           @ shift b31 into C flag
adc    r0, #0            @ add C flag (b31) to r0
bx     lr
```

#### Best Q31 Multiply (3 instructions, using Op2)

```
smull  r1, r0, r0, r1
lsl    r0, #1
add    r0, r0, r1, lsr #31   @ add bit 31 of r1 to r0
bx     lr
```

### Barrel Shifter and Op2 (Flexible Operand 2)

Op2 can be one of three forms:
1. An immediate number: `#imm`
2. A register without shift: `Rm`
3. A register with shift: `Rm, LSL #n` / `Rm, LSR #n` / `Rm, ASR #n`

**When using a register with shift as Op2, the destination register cannot be omitted even if it equals the first source register.**

### Op2 Special Operations Examples

```
add r2, r1, r0, lsl #1    @ r2 = r1 + 2*r0
rsb r2, r1, r0, asr #2    @ r2 = r0/4 - r1 (signed)
```

### Fast Q31 Scaling with Op2

| Scale Factor | Instruction | Equivalent |
|-------------|-------------|------------|
| 5/4 = 1.25 | `add r0, r0, r0, asr #2` | r0 + r0/4 |
| 3/4 = 0.75 | `sub r0, r0, r0, asr #2` | r0 - r0/4 |
| 9/8 = 1.125 | `add r0, r0, r0, asr #3` | r0 + r0/8 |
| 7/8 = 0.875 | `sub r0, r0, r0, asr #3` | r0 - r0/8 |

- Only works when denominator is a power of 2.
- Faster than multiplication approach and avoids overflow/accuracy issues.

---

## Lecture 17: Bitwise Logic Instructions

### C Bitwise Operators

| Precedence | Operator | Description | Associativity |
|------------|----------|-------------|---------------|
| 2 | `~` | Bitwise NOT | Right to left |
| 8 | `&` | Bitwise AND | Left to right |
| 9 | `^` | Bitwise XOR | Left to right |
| 10 | `\|` | Bitwise OR | Left to right |
| 14 | `&=`, `^=`, `\|=` | Assignment by bitwise op | Right to left |

### ASM Bitwise Instructions

| Instruction | Operation | C Equivalent |
|-------------|-----------|--------------|
| `MVN Rd, Op2` | Rd = ~Op2 | `~x` |
| `AND {Rd,} Rn, Op2` | Rd = Rn & Op2 | `x & y` |
| `ORR {Rd,} Rn, Op2` | Rd = Rn \| Op2 | `x \| y` |
| `EOR {Rd,} Rn, Op2` | Rd = Rn ^ Op2 | `x ^ y` |
| `ORN {Rd,} Rn, Op2` | Rd = Rn \| ~Op2 | No direct C equivalent |
| `BIC {Rd,} Rn, Op2` | Rd = Rn & ~Op2 | No direct C equivalent |
| `BFC Rd, #s, #w` | Clear w bits starting at bit s | No direct C equivalent |
| `BFI Rd, Rn, #s, #w` | Insert w LSBs of Rn into Rd starting at bit s | No direct C equivalent |

### Bit Manipulation Patterns

#### Read a bit (bit N of A)

```
@ C: A = (A >> N) & 1U;
lsr  r0, r1       @ A >>= N
and  r0, #1       @ A &= 1U
bx   lr
```

#### Read the C flag from APSR

```
mrs  r0, apsr     @ MRS: Move to Register from Special register
lsr  r0, #29      @ C flag is bit 29
and  r0, #1       @ mask other bits
bx   lr
```

#### Set bit N of A to 1

```
@ C: A |= (1U << N);
ldr  r2, =1       @ mask = 1
lsl  r2, r1       @ mask <<= N
orr  r0, r2       @ A |= mask
bx   lr
```

#### Clear bit N of A to 0

```
@ C: A &= ~(1U << N);
ldr  r2, =1       @ mask = 1
lsl  r2, r1       @ mask <<= N
bic  r0, r2       @ A &= ~mask  (BIC does AND with NOT)
bx   lr
```

#### Toggle bits using a mask

```
@ C: A ^= mask;
eor  r0, r1       @ A ^= mask
bx   lr
```

#### Assign a bit field (w bits starting at bit s, value v)

Two-step process:
1. Clear the target bits using BIC with a mask.
2. OR in the new value shifted to position.

```
@ r0=A, r1=s, r2=w, r3=v
push  {r4, lr}
ldr   r4, =1
lsl   r4, r2       @ mask = 2^w
sub   r4, #1        @ mask = 2^w - 1 (w ones)
lsl   r4, r1       @ shift mask to position s
bic   r0, r4       @ clear the target bits
lsl   r3, r1       @ shift value to position
and   r3, r4       @ ensure value fits in w bits
orr   r0, r3       @ assign the bits
pop   {r4, pc}
```

### MRS / MSR Instructions

| Instruction | Operation |
|-------------|-----------|
| `MRS Rd, apsr` | Move APSR to general-purpose register (Read special register) |
| `MSR apsr_nzcvq, Rn` | Move general-purpose register to APSR (Write special register) |

---

## Lecture 18: ARM Processor Status Flags

### Key Principle

- **Instructions for additions and subtractions are the same for unsigned and signed operands.** The Cortex-M processor does not know whether the operation is unsigned or signed.
- The processor updates both C and V flags simultaneously.
- C flag is for unsigned operations; V flag is for signed operations.

### Two Ways to Update Status Flags

1. Use the **S suffix**: `[op]s Rd, Rn, Op2` (e.g., `ADDS`, `SUBS`)
2. Use **test instructions** (covered in later lecture)

### Flag Update Rules

Flags are updated based on:
- **Value of result (NUT = Number Under Test)**: N and Z flags.
- **Condition of operation (OUT = Operation Under Test)**: C and V flags.

### APSR Bit Definitions

| Bit | Flag | Condition to Set (=1) |
|-----|------|----------------------|
| 31 | N (Negative) | MSB of NUT is 1 |
| 30 | Z (Zero) | NUT is zero |
| 29 | C (Carry/Borrow) | Unsigned carry or no borrow (see below) |
| 28 | V (Overflow) | Signed overflow (see below) |

### Which Flags for Which Number Type

- **Unsigned numbers**: use C, N, and Z flags.
- **Signed numbers**: use V, N, and Z flags.

### N-bit Number Constants and Ranges

| Constant | Formula |
|----------|---------|
| C_N (Cardinality) | 2^N |
| U_MIN | 0 |
| U_MAX | 2^N - 1 |
| S_MIN | -2^(N-1) |
| S_MAX | 2^(N-1) - 1 |

- **Unsigned N-bit range**: [0, 2^N - 1]
- **Signed N-bit range**: [-2^(N-1), 2^(N-1) - 1]

### Unsigned/Signed Number Conversion

- Unsigned to signed: if value > S_MAX, subtract C_N.
- Signed to unsigned: if value < 0, add C_N.

### C Flag Setting Rules (Detailed)

For unsigned numbers u1 and u2:
- **Addition**: C = 1 if u1 + u2 > 2^N - 1 (carry out); else C = 0.
- **Subtraction**: C = 1 if u1 - u2 >= 0 (no borrow); C = 0 if u1 - u2 < 0 (borrow).

### V Flag Setting Rules

For signed numbers s1 and s2:
- V = 0 if s1 +/- s2 is in [-2^(N-1), 2^(N-1) - 1] (no overflow).
- V = 1 otherwise (overflow occurred).

### N and Z Flag Rules

- N = 1 if the MSB of the result is 1; else N = 0.
- Z = 1 if the result is zero; else Z = 0.

### Correcting the Result (N-bit)

After an N-bit operation, the result must be brought back into the N-bit range:
- Unsigned: if result > U_MAX, subtract C_N. If result < 0, add C_N.
- Signed: if result > S_MAX, subtract C_N. If result < S_MIN, add C_N.

### Hand Calculation Method (5-bit example: C_N=32, U_MAX=31, S_MIN=-16, S_MAX=15)

For each operation, determine:
1. Unsigned result and C flag (carry/borrow).
2. Signed result and V flag (overflow).
3. N flag (MSB of result) and Z flag (result == 0).
4. Final binary result (same for both unsigned and signed interpretations).

### N-bit ASM Verification Function

```
@ uint64_t mp_n_bit_adds_s(int32_t x, int32_t y, int N)
@ r0=x, r1=y, r2=N
@ Output: r1:r0 where r0 = x+y result, r1 = APSR
rsb   r2, r2, #32    @ r2 = 32 - N
lsl   r0, r2         @ shift to use only N bits
lsl   r1, r2         @ shift to use only N bits
adds  r0, r1         @ add and update flags
asr   r0, r2         @ shift result back
mrs   r1, apsr       @ read APSR into r1
bx    lr
```

### Bit-field Struct for APSR in C

```c
typedef struct {
    uint32_t _reserve : 28;
    uint32_t V        : 1;   // Bit 28
    uint32_t C        : 1;   // Bit 29
    uint32_t Z        : 1;   // Bit 30
    uint32_t N        : 1;   // Bit 31
} APSR_t;
```

### Key Formula: N+1 Bits for N-bit Results

To express addition/subtraction results of N-bit numbers without overflow risk, use an (N+1)-bit system.
