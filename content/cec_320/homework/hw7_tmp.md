# Study Guide: Homework 7 - Shift and Bitwise Logic Instructions

## 1. High-Level Overview
This topic explores the synergy between **shift operations** and **bitwise logic instructions** in ARM assembly. It focuses on how the **barrel shifter** enables efficient mathematical scaling (multiplication/division by powers of 2) and complex data packing/unpacking within a single instruction cycle. These techniques are fundamental for high-performance Digital Signal Processing (DSP) and direct hardware register control where memory and execution time are constrained.

## 2. Core Concepts & Mental Models

*   **Barrel Shifter:** A hardware component that allows the second operand (`Op2`) of many instructions to be shifted or rotated before the primary operation (e.g., `ADD`, `SUB`, `BIC`) is performed, incurring no additional clock cycles.
*   **Flexible Second Operand (Op2):** A versatile parameter that can be a constant, a register, or a register modified by a shift instruction (`LSL`, `LSR`, `ASR`, `ROR`).
*   **Logical vs. Arithmetic Shifts:**
    *   **LSL (Logical Shift Left):** Multiplies by $2^n$ by shifting in 0s from the right; works for both signed and unsigned integers.
    *   **LSR (Logical Shift Right):** Divides unsigned integers by $2^n$ by shifting in 0s from the left.
    *   **ASR (Arithmetic Shift Right):** Divides signed integers by $2^n$ by repeating the sign bit (MSB) to preserve the value's sign.
*   **Bit-Field Instructions:** Specialized instructions like `BFC` (Bit Field Clear) and `BFI` (Bit Field Insert) that modify adjacent sets of bits without affecting the rest of the register.

## 3. Subtopics & Structural Breakdown

### 3.1 Advanced Q-Format Multiplication
Multiplication of fixed-point numbers (Qm.n) requires a 64-bit intermediate product followed by a right shift of $n$ bits to maintain the correct radix point.
*   **Q31 Implementation:** Uses `SMULL` to get a 64-bit result, then shifts right by 31 bits.
*   **Q15.16 Implementation:** Requires shifting the 64-bit product right by 16 bits to extract the correct 32-bit result.

### 3.2 Scaling with Op2
Common scaling factors that are not powers of 2 can be synthesized using one or two instructions by combining shifts with addition or subtraction.
*   **Multiplication:** $3 \times R0 = R0 + (R0 \ll 1)$.
*   **Division/Fractional Scaling:** $0.75 \times R0 = R0 - (R0 \gg 2)$.

### 3.3 Bitwise Logic for Register Control
Instructions such as `AND`, `ORR`, `EOR`, and `BIC` (Bit Clear) are used with masks to modify specific hardware bits.
*   **BIC:** Performs an `AND` with the complement of `Op2`, effectively "clearing" the bits specified in the mask.
*   **ORR:** Used to "set" bits by combining the register with a mask.

## 4. Homework 7 Problem Walkthrough

### Prob 1: Q15.16 Multiplication in Assembly
*   **Requirement:** Implement $I_C = (I_A \times I_B) \gg 16$.
*   **ASM Solution:**
    ```assembly
    @ int32_t mp_mult_q15p16_s(int A, int B)
    mp_mult_q15p16_s:
        smull r2, r3, r0, r1  @ [r3:r2] = 64-bit product (r3=HW, r2=LW)
        lsr r0, r2, #16       @ Shift LW right by 16 (bits 31:16 become bits 15:0)
        orr r0, r0, r3, lsl #16 @ Combine with HW shifted left 16 (bits 47:32 become bits 31:16)
        bx lr
    ```
*   **Theory:** `SMULL` produces a 64-bit result in two 32-bit registers. To shift a 64-bit value right by 16, we extract the middle 32 bits (bits 47 to 16).

### Prob 2: Shift Calculations and Carry Flag
*   **Initial:** $R0 = 0b1101\_1101$ (`0xDD`).
*   **Instruction 1:** `LSLS r1, r0, #1`.
    *   $R1 = 0b1\_1011\_1010$ (truncated to 32 bits) $\rightarrow$ **`0x0000_01BA`** (assuming 32-bit).
    *   **C flag = 1** (The MSB shifted out was 1).
*   **Instruction 2:** `LSRS r2, r0, #3`.
    *   $R2 = 0b0001\_1011$ $\rightarrow$ **`0x0000_001B`**.
    *   **C flag = 1** (The last bit shifted out was bit 2, which was 1).

### Prob 3: Single-Line Scaling with Op2
Assuming signed integers in R1 ($B$) and result in R0 ($A$):
1.  **A = 16 * B:** `lsl r0, r1, #4`
2.  **A = 17 * B:** `add r0, r1, r1, lsl #4` ($B + 16B$)
3.  **A = 15 * B:** `rsb r0, r1, r1, lsl #4` ($16B - B$)
4.  **A = B / 16:** `asr r0, r1, #4`
5.  **A = 17 * B / 16:** `add r0, r1, r1, asr #4` ($B + B/16$)
6.  **A = 15 * B / 16:** `sub r0, r1, r1, asr #4` ($B - B/16$)

### Prob 4: Analyzing `mp_func_s`
*   **Register Actions:**
    *   `bic r0, r0, #0xF, lsl #4`: Clears digit $H_1$ (bits 7:4).
    *   `orr r0, r0, #0xA, lsl #4`: Sets digit $H_1$ to `10` (`0xA`).
*   **Result for $0xH_3H_2H_1H_0$:** The function replaces digit $H_1$ with `A`. Final value = **`0xH3H2A0`** (if $H_1$ was previously arbitrary).
*   **C Translation:**
    ```c
    uint16_t mp_func_c(uint16_t a) {
        return (a & ~(0xF << 4)) | (0xA << 4);
    }
    ```

### Prob 5: Logic and Shift Trace
*   **Initial:** $A = 0xAD$ (`1010_1101`), $mask = 0x03$ (`0000_0011`).
1.  `lsr r2, r1, #2`: $0x03 \gg 2 = \mathbf{0x00}$.
2.  `lsl r2, #2`: $0 \ll 2 = \mathbf{0x00}$.
3.  `bic r3, r0, r1`: Clear bits 0, 1 of `0xAD`. $1010\_1101 \rightarrow 1010\_1100 = \mathbf{0xAC}$.
4.  `orr r4, r3, r1`: $0xAC | 0x03 = \mathbf{0xAF}$.
5.  `eor r5, r0, r1`: $0xAD \oplus 0x03 = \mathbf{0xAE}$.

### Prob 6: Digit Manipulation Functions
**(a) A = 0xH3H2H1H0 => A = 0xH3H25H0**
*   **ASM:**
    ```assembly
    mp_func_a_in_s:
        bic r0, #0xF0  @ Clear H1
        orr r0, #0x50  @ Set H1 to 5
        bx lr
    ```

**(b) A = 0xH3H2H1H0 => A = 0xH2H1H03**
*   **Theory:** Left shift 4 bits and set new LSB digit to 3.
*   **C:** `return (A << 4) | 0x3;`
*   **ASM:**
    ```assembly
    mp_func_b_in_s:
        lsl r0, #4
        orr r0, #3
        bx lr
    ```

**(c) A = 0xH3H2H1H0 => A = 0x7H3H2H1**
*   **Theory:** Right shift 4 bits and set new MSB digit to 7.
*   **C:** `return (A >> 4) | 0x7000;`
*   **ASM:**
    ```assembly
    mp_func_c_in_s:
        lsr r0, #4
        orr r0, #0x7000
        bx lr
    ```