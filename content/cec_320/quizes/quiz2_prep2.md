Based on the course schedule, homework assignments, and lecture materials, **Quiz 2** covers the foundational mechanics of how the processor interacts with hardware (GPIO and Interrupts) and how it handles complex data (Real Numbers and Arithmetic).

Below is the comprehensive list of topics and subtopics you should review for a quiz covering **Homeworks 3, 4, and 5**.

### 1. GPIO and Bitwise Operations (Homework 3)
This topic focuses on how to control individual pins and how to use C logic to manipulate hardware registers.

*   **GPIO Hardware Modes:**
    *   **Input States:** High, Low, and High Impedance (HiZ/Floating).
    *   **Internal Resistors:** Pull-up (connects to VDD) and Pull-down (connects to Ground) to stabilize HiZ inputs.
    *   **Output Types:** Push-pull (drives High and Low) vs. Open-drain (can only pull to Ground, requires external pull-up).
*   **Bitwise Manipulation Algorithms:**
    *   **Checking Bits:** Using bitwise `AND` with a mask.
    *   **Setting Bits:** Using bitwise `OR` with a mask.
    *   **Clearing Bits:** Using bitwise `AND` with an inverted mask (`~mask`) or the `BIC` instruction.
    *   **Toggling Bits:** Using bitwise `XOR` (EOR) with a mask.
    *   **Field Assignment:** The two-step process of clearing a multi-bit field and then inserting a new value.
*   **Direct Register Access:**
    *   **Register Mapping:** Understanding the structure of GPIO register banks (MODER, IDR, ODR, BSRR).
    *   **Atomic Operations:** Using the **BSRR** (Bit Set/Reset Register) to modify output bits in a single cycle without a load-modify-store sequence.

### 2. Interrupts and Preemption (Homework 4)
This topic covers how the processor responds to real-time events without constantly checking (polling) them.

*   **NVIC (Nested Vectored Interrupt Controller):**
    *   The hardware unit that manages all interrupts and system exceptions.
    *   Distinction between **System Exceptions** (ARM core specific, negative IRQn) and **Peripheral Interrupts** (Vendor specific, IRQn $\ge 0$).
*   **Interrupt Response Sequence:**
    *   **Stacking:** The automatic hardware process of saving eight core registers (R0-R3, R12, LR, PC, xPSR) to the stack upon an interrupt.
    *   **Vector Table:** A memory array containing the starting addresses of all ISRs (Interrupt Service Routines).
    *   **Tail-chaining:** An optimization that skips unstacking/stacking when moving directly from one ISR to another pending ISR.
*   **Priority and Preemption Theory:**
    *   **Preemption (Group) Priority:** Determines if an interrupt can halt a currently running ISR.
    *   **Sub-priority:** Determines the order of execution for multiple pending interrupts with the same group priority.
    *   **Priority Calculation:** Using the formula $PN = (PPN \ll m) + SPN$ to determine the value placed in the Priority Register.
*   **EXTI (Extended Interrupt/Event Controller):**
    *   Multiplexing GPIO pins to interrupt lines using the **SYSCFG** registers.
    *   Configuring trigger detection for rising edges, falling edges, or both.

### 3. Real Numbers and Arithmetic (Homework 5)
This topic covers how microprocessors perform math on non-integer values using both hardware and software methods.

*   **IEEE 754 Floating-Point:**
    *   The standard 32-bit (Single Precision) format consisting of a Sign bit, 8-bit Biased Exponent (Bias = 127), and 23-bit Fraction (Mantissa) [12.2.1.1, 13.1.2].
*   **Fixed-Point Representation (Qm.n):**
    *   **Notation:** $m$ bits for the whole-number part and $n$ bits for the fractional part.
    *   **Encoding Algorithm:** Scaling the real number by $2^n$, rounding to the nearest integer, and applying Two's Complement for negative values [13.2, 716].
    *   **Decoding Algorithm:** Converting the integer value back to a real number by multiplying by $2^{-n}$.
*   **Fixed-Point Arithmetic:**
    *   **Addition/Subtraction:** Operations can be performed directly on encoded integers.
    *   **Multiplication:** Requires a right shift by $n$ bits after multiplying the two encoded integers to maintain the correct decimal position ($I_C = (I_A \times I_B) \gg n$).
*   **Processor Status Flags:**
    *   Understanding the **C (Carry)**, **V (Overflow)**, **Z (Zero)**, and **N (Negative)** flags in the APSR and how they are updated by arithmetic instructions (`ADDS`, `SUBS`, etc.).