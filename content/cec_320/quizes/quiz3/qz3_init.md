ok i am having a quiz on homework 6,7,8, please make a list of topics that i need to understand and the corresponding lectures.


"Just a reminder that you can use your own formula sheets for QZ3. Ideally, you use ONE new piece of letter-sized paper for the new contents covered by HWs 6, 7, and 8. You can also use the two pieces of paper you used for the previous QZes. 

Note that you need to write down the commonly used ASM instructions we have learned in class on your formula sheet. No creation of fake instructions is allowed. No instructions or approaches that we have not covered in class can be used either."



For your upcoming quiz on Homeworks 6, 7, and 8, you should focus on the transition from high-level C logic to ARM assembly implementation. The following list breaks down the topics you need to understand and their corresponding lectures.

### **Homework 6: Mixed C and Assembly Programming**
This unit focuses on the rules for function interaction and multi-word arithmetic.

*   **Lecture 14: Mixed C and ASM Programming**
    *   **The EABI Standard:** Understanding how registers R0–R3 are used for input arguments and R0 (or R0:R1 for 64-bit) for return values.
    *   **Register Preservation:** Differentiating between caller-saved (R0–R3, R12, LR) and callee-saved (R4–R11) registers.
    *   **Stack Operations:** Mastering the **Full Descending Stack** model, where the Stack Pointer (SP) decrements before storing data.
    *   **Function Returns:** Knowing when to use `bx lr` (leaf functions) versus `pop {pc}` (stem functions that stack LR).
    *   **Type-casting:** How the compiler promotes 8-bit or 16-bit variables to 32-bit registers using sign or zero extension.

*   **Lecture 15: Arithmetic Instructions**
    *   **Status Flags (C Flag):** Understanding that $C=1$ for a carry in addition, but $C = 1 - Borrow$ in subtraction.
    *   **Multi-word Math:** Implementing 64-bit operations using `ADDS`/`ADC` (Add with Carry) and `SUBS`/`SBC` (Subtract with Borrow).
    *   **Multiplication & Division:** Using `MUL`, `SMULL`/`UMULL` (64-bit results), and implementing the C modulo operator (`%`) using `UDIV` and `MLS` logic.

---

### **Homework 7: Shift and Bitwise Logic Instructions**
This unit explores how to use the processor's hardware to manipulate bits and scale numbers efficiently.

*   **Lecture 16: Shift Instructions, Op2, and Applications**
    *   **Shift Types:** Understanding `LSL` (multiplication), `LSR` (unsigned division), and `ASR` (signed division, which repeats the MSB to preserve the sign).
    *   **Barrel Shifter and Op2:** Using the Flexible Second Operand to perform scaling in a single instruction, such as $A = 17 \times B$ (`add r0, r1, r1, lsl #4`).
    *   **Advanced Multiplication:** Implementing fixed-point Q-format multiplication (like Q15.16) by extracting the middle 32 bits from a 64-bit `SMULL` result.

*   **Lecture 17: Bitwise Logic Instructions**
    *   **Logic Operations:** Mastering `AND`, `ORR`, `EOR` (XOR), and `BIC` (Bit Clear).
    *   **Bit Masking:** Creating masks to selectively check, set, clear, or toggle specific bits within hardware registers [749–753].
    *   **Bit-Field Instructions:** Using `BFC` (Bit Field Clear) and `BFI` (Bit Field Insert) for modifying adjacent sets of bits.
    *   **Field Assignment:** The two-step algorithm to clear a multi-bit field and then insert a new value using `ORR`.

---

### **Homework 8: Status Flags, CCS, and Branch**
This unit covers how the processor makes decisions and controls program flow.

*   **Lecture 18: ARM Processor Status Flags**
    *   **NZCV Definitions:** Understanding the **N**egative, **Z**ero, **C**arry, and o**V**erflow flags.
    *   **Flag Updating:** Knowing that flags are only updated if the `S` suffix is used (e.g., `ADDS` vs `ADD`).
    *   **Manual Calculation:** Practicing hand calculations for status flags in 5-bit or 6-bit systems to simulate processor logic.
    *   **Special Register Access:** Using `MRS` and `MSR` to read from or write to the APSR.

*   **Lecture 19: Condition Code Suffixes (CCS) and Conditional Branch**
    *   **Relational Tests:** Mapping C operators (`==`, `>`, `<=`, etc.) to assembly suffixes like `EQ`, `GT`, `LE`, `HI`, `HS`, etc..
    *   **Signed vs. Unsigned Logic:** Differentiating between signed suffixes (e.g., `GT`, `LT`) and unsigned suffixes (e.g., `HI`, `LO`).
    *   **Flow Control Implementation:** Translating C `if-else` blocks, `while` loops, and `for` loops into assembly labels and conditional branches.
    *   **Comparison Instructions:** Using `CMP` and `CMN` to update flags without storing a result.
    *   **Optimized Branches:** Using `CBZ` (Compare and Branch if Zero) and `CBNZ` for efficient loop termination.