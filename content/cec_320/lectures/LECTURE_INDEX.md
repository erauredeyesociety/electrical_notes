# CEC 320 — Lecture Index and Topic Reference

A master navigation document for all CEC 320 lecture slide decks. Each entry lists the lecture number, title, the full topic list from the slide deck's page-1 agenda, and the PDF filename.

---

## Quick Navigation

| # | Title | Lecture file |
|---|-------|--------------|
| 2  | Hello from UART | [lctr2](<lctr2-hello-from-uart-slides-26-01-07 (2).pdf>) |
| 3  | MCU Architecture, Pipeline, Memory, and Number Expression | [lctr3](<mp-ce--lctr3-mp-arch-pipiline-memory-n-num-expr-slides-26-01 (2).pdf>) |
| 4  | Data Representation | [lctr4](<mp-cg--lctr4-data-representation-slides-26-01 (1).pdf>) |
| 5  | Pointers and Unit Test | [lctr5](<mp-ci--lctr5-pointers-n-unit-test-slides-26-01 (1).pdf>) |
| 6  | General-Purpose Input and Output (GPIO) | [lctr6](<mp-dc-lctr6-gpio-slides-2026-01 (1).pdf>) |
| 7  | Bitwise Operations and Direct GPIO Register Access | [lctr7](<mp-de-lctr7-bitwise-ops-n-gpio-reg-access-slides-2026-01 (1).pdf>) |
| 8  | Exception and Interrupt | [lctr8](<mp-dg-lctr8-exception-n-interrupt-slides-2026-02 (2).pdf>) |
| 9  | Preemption, EXTI, and Finite State Machine | [lctr9](<mp-di-lctr9-preemption-exti-n-fsm-2026-02 (3).pdf>) |
| 13 | Introduction to Real Numbers | [lctr13](<mp-ee-lctr13-real-numbers-slides-2026-02 (2).pdf>) |
| 14 | Mixed C and ASM Programming | [lctr14](<mp-fc-lctr14-mixed-c-n-asm-prog-slides-26-02 (1).pdf>) |
| 15 | Arithmetic Instructions | [lctr15](<mp-fe-lctr15-arithmetic-instructions-slides-26-02 (2).pdf>) |
| 16 | Shift and Rotation Instructions, Op2, and Applications | [lctr16](<mp-fg-lctr16-shift-instructions-n-op2-slides-26-03 (1).pdf>) |
| 17 | Bitwise Instructions | [lctr17](mp-fi-lctr17-bitwise-logic-instructions-slides-26-03.pdf) |
| 18 | ARM Processor Status Flags | [lctr18](mp-fm-lctr18-arm-status-flags-slides-26-03.pdf) |
| 19 | Condition Code Suffixes and Conditional Branch | [lctr19](mp-fo-lctr19-ccs-n-cond-branch-slides-26-03.pdf) |
| 20 | Immediate-Offset Load and Store Instructions and Macro | [lctr20](mp-gc-lctr20-imd-offset-ldr-n-str-n-macro-slides-26-03.pdf) |
| 21 | Additional Load and Store Instructions and Move Instructions | [lctr21](mp-ge-lctr21-more-ldr-n-str-n-mov-slides-26-03.pdf) |
| 22 | Increment Operations for Variables and Pointers in C and ASM | [lctr22](mp-gg-lctr22-incr-ops-4-c-vars-n-ptrs-n-impl-in-asm-slides-26-04.pdf) |
| 23 | Calling ASM Functions in an ASM Function | [lctr23](mp-gm-lctr23-calling-asm-fns-in-asm-fn-slides-26-04.pdf) |
| 24 | Combination Branching and Conditional Execution | [lctr24](mp-hc-lctr24-combo-branch-n-cond-execution-slides-26-04.pdf) |
| 25 | Selection Control in C and ASM (If-Based Flow Control) | [lctr25](mp-he-lctr25-if-based-flow-control-in-asm-slides-26-04.pdf) |
| 26 | Implementing C's Loop Control in ASM | [lctr26](mp-hg-lctr26-impl-c-loops-in-asm-26-04.pdf) |

> Gap: Lectures 10, 11, 12 are not currently present in the `lectures/` folder (likely exam week or not-yet-added decks).

---

## Detailed Topics

### Lctr 2 — Hello from UART

**Core concepts**
- Fundamentals of UART (universal asynchronous receiver and transmitter).
- Parameters and basic calculations for UART.

**Demo project**
- UART setup in CubeMX and parameters.
- HAL functions for UART.
- `stdout` and `stdin` redirection to UART.
- Requirements of the project.
- Project management in CubeIDE.
- Running the demo project using Renode.

---

### Lctr 3 — MCU Architecture, Instruction Pipeline, Memory, and Number Expression

**Core concepts**
- Architecture of ARM Cortex-M processors.
- Pipelines for instruction execution.
- Memory organization.
- Expressions of unsigned integers saved in memory: decimal, binary, and hexadecimal formats.

**Demo project**
- Printing numbers in different formats with UART redirect.
- Reading numbers with UART redirect with certain range.

**After-class review (C programming)**
- Static and global functions; static and global variables.
- `for` and `while` loops.
- `char` and ASCII coding.
- Strings and their ending.

---

### Lctr 4 — Data Representation

**Core concepts**
- Expression of negative integers in two's complement (TC).
- Encoding in both binary and decimal.
- Decoding in several ways, including the decimal-based approach.
- C's data types of different bit widths.
- Endianness of multi-byte data.
- Memory map.

**Demo project**
- Printing out the TC encoding of negative numbers.
- Printing out the contents of various data types.

**Additional reading**
- C's scalar variables, arrays, structs, and unions.

---

### Lctr 5 — Pointers and Unit Test

**Core concepts**
- Pointers of C: definition, using array names as pointers, typecasting pointers or dereferenced values, offset of pointers.
- Prefix and postfix increment/decrement of variables and pointers.
- Unit test with Unity.

**Demo project**
- Two builds: App and Unit Test.
- Unit test exercises various pointer operations and a string-copy function implemented with pointers and a `do-while` loop.
- App prints out various pointer operations.

**Additional reading**
- Stack and heap.

---

### Lctr 6 — General-Purpose Input and Output (GPIO)

**Core concepts**
- GPIO hardware composition.
- GPIO registers.
- GPIO programming: data structure of GPIO registers, pointer to that data structure, GPIO functions.

**Demo project**
- Controlling an LED (GPIO output) via a pushbutton (GPIO input).
- Controlling an LED via UART.

**Additional reading**
- GPIO modes: push-pull vs. open-drain output; pull-up / pull-down / no-pull input.

---

### Lctr 7 — Bitwise Operations and Direct GPIO Register Access

**Core concepts**
- Shift and bitwise operations in C.
- GPIO control via direct register access in C: setting GPIO mode, output type, input pull config; reading IDR and writing ODR.

**Demo project**
- Controlling a GPIO pin using direct GPIO register access.
- Using the SysTick timer to do two works in parallel (timer is discussed in detail later).

---

### Lctr 8 — Exception and Interrupt

**Core concepts**
- What is an interrupt and how it is handled.
- Differences between exception (Cortex core) and interrupt (peripherals).
- NVIC — nested vectored interrupt controller.
- Servicing interrupts with ISRs and callback functions.
- NVIC functions to manage interrupts.

**Demo project**
- Blinking an LED with a rate read from UART using interrupt mode.
- Super loop does only one thing; everything else is handled by interrupts.

**Additional reading**
- Setting up UART to use interrupts with CubeMX.
- C functions for UART interrupt operations.

---

### Lctr 9 — Preemption, EXTI, and Finite State Machine

**Core concepts**
- Priority of interrupt and preemption (principle and configuration).
- Preemption priority and sub-priority.
- EXTI (external interrupt) with GPIO pins.
- Finding callback functions.
- Using finite state machines to handle different cases.

**Demo project**
- Using EXTI0 to avoid polling.
- Preemptive interrupts with EXTI0 and UART2.

**Additional reading**
- Configuring EXTI in CubeMX.
- Tail-chaining of interrupts.

---

### Lctr 13 — Introduction to Real Numbers

**Core concepts**
- Floating-point real number representation: definition of floating-point numbers in C.
- Fixed-point real number representation: unsigned and signed fixed-point; definition of fixed-point numbers in C.
- Mathematical operations using fixed-point numbers: addition, subtraction, multiplication.

**Demo project**
- Real number operations based on fixed-point integers.

**Additional reading**
- Including the DSP library in a CubeIDE project.
- Using the FPU (floating-point unit) and floating-point functions.

---

### Lctr 14 — Mixed C and ASM Programming

**Core concepts**
- ARM Cortex-M core registers.
- ARM Cortex-M ISA (instruction set architecture).
- EABI (embedded application binary interface) standard for creating ASM functions.
- Using the stack in ASM functions.

**Demo project**
- Mixed C and ASM programming; calling ASM functions from C.
- Returning from a function: `bx lr` when LR is not stacked, or `pop pc` when LR is stacked.

---

### Lctr 15 — Arithmetic Instructions

**Core concepts**
- Carry and borrow for addition and subtraction.
- Arithmetic instructions: addition, subtraction, multiplication, and division.
- Implementing 64-bit addition and subtraction using 32-bit instructions.
- Implementing remainder (modulo) operation as an ASM function.

**Demo project**
- Testing various small ASM functions.
- M-word addition using mixed C and ASM programming.

---

### Lctr 16 — Shift and Rotation Instructions, Op2, and Applications

**Core concepts**
- Shift operations in C.
- ASM shift instructions with C counterparts (useful in combination with bitwise ops).
- Implementing Q31 multiplication in ASM using shifts.
- Rotation instructions without C counterparts (skipped in class).
- Barrel shifter, Op2 (flexible second operand), and applications: improved Q31 multiply, fast Q31 scaling, special operations.

**Demo project**
- Multiple ASM Q31 multiplication implementations.
- ASM functions for shifting 64-bit numbers (skipped in class).

---

### Lctr 17 — Bitwise Instructions

**Core concepts**
- Bitwise operations in C.
- Bitwise logic instructions having C counterparts.
- Bitwise logic instructions with no C counterparts.

**Demo project**
- Various ASM functions using bitwise operations.

---

### Lctr 18 — ARM Processor Status Flags

**Core concepts**
- Definition of the N, Z, C, and V status flags.
- Reading the status flags in ASM.
- N-bit operations that update NZCV.
- Examples of hand calculations.

**Demo project (optional)**
- Simulating additions and subtractions with status update using C.
- Using bit-field constructs in C to save the status flags.
- Code for updating NZCV.
- Tricks for variable assignment involving bit-fields.
- Verifying simulated status flags using ASM functions.

---

### Lctr 19 — Condition Code Suffixes and Conditional Branch

**Core concepts**
- Condition code suffixes based on the NZCV flags.
- Comparison instructions.
- Branch and conditional branch instructions.
- Basic `if-else`, `for`, and `while` constructs in ASM.

**Demo project**
- Basic `if-else` construct in ASM.
- Basic `for` and `while` constructs in ASM.

---

### Lctr 20 — Immediate-Offset Load and Store Instructions and Macro

**Core concepts**
- Immediate-offset load/store for various data types: 32-bit signed and unsigned, 16-bit signed and unsigned, 8-bit signed and unsigned.
- C pointer operations implemented by the above instructions.

**Demo project**
- Example problems of load and store.

**C and ASM programming**
- Macros in ASM for clean coding (optional).

---

### Lctr 21 — Additional Load and Store Instructions and Move Instructions

**Core concepts**
- Register-offset load/store for various data types (32-, 16-, 8-bit, signed and unsigned).
- C pointer operations implemented by the above instructions.
- Pseudo `LDR` and move instructions (optional).

**Demo project**
- Example problems of load/store.
- How `LDR Rd, =num_or_label` works (optional).

**C and ASM programming**
- `const` value and `const` pointer (optional).

---

### Lctr 22 — Increment Operations for Variables and Pointers in C and ASM

**Core concepts**
- Increment/decrement operations of C variables and pointers.
- ASM implementations.
- Mixed pointer and other operations (optional).

**Demo project**
- Various load/store-related functions for illustration.

**C and ASM programming**
- Issues with C increment and decrement operations.

---

### Lctr 23 — Calling ASM Functions in an ASM Function

**Core concepts**
- Why and how to call ASM functions from another ASM function.
- Preparing arguments for a function call: using `LDR`/`LDRSH`/`LDRH`/`LDRSB`/`LDRB` for different argument types; using `LDRD` for 64-bit arguments.
- Getting the return value: using `STR`/`STRH`/`STRB` for different types; using `STRD` for a 64-bit return.

**Demo project**
- Calling ASM functions to delegate 16-, 32-, and 64-bit operations.

**C and ASM programming**
- Using `BL` (branch with link) to call ASM functions in ASM.
- Calling an ASM function defined in another ASM source file.

---

### Lctr 24 — Combination Branching and Conditional Execution

**Core concepts**
- Combination branching (`CBZ` / `CBNZ`).
- Conditional execution instructions.
- The `IT` (If-Then) instruction for organizing conditional execution instructions.
- Implementing C's `if-else` construct with conditional execution instructions.

**Demo project**
- Applications of the above instructions.
- Contrast C's `if-else` implemented with conditional branch vs. conditional execution.

---

### Lctr 25 — Selection Control in C and ASM

**Core concepts**
- Basic `if` construct in C and ASM.
- Basic `if-else` construct in C and ASM.
- Basic `if-else-if-else` construct in C and ASM.
- Compound `if-else` (AND / OR tests) in C and ASM.

**Demo project**
- Examples and exercise solutions of `if`-based flow control in C and ASM.

---

### Lctr 26 — Implementing C's Loop Control in ASM

**Core concepts**
- The `for` loop in C and its ASM implementation.
- The `while` loop in C and its ASM implementation.
- The `do-while` loop in C and its ASM implementation.

**Demo project**
- Examples and exercise solutions of loops in C and ASM.

---

## Topic Clusters (Cross-Cutting View)

**Peripherals and HAL**
- Lctr 2 (UART), Lctr 6 (GPIO), Lctr 7 (direct GPIO register access), Lctr 8 (exceptions/interrupts), Lctr 9 (preemption + EXTI + FSM).

**Data & numeric representation**
- Lctr 3 (memory + number expression), Lctr 4 (data representation, two's complement, endianness), Lctr 5 (pointers), Lctr 13 (real numbers, fixed-point, FPU).

**ASM foundations**
- Lctr 14 (EABI, mixed C/ASM), Lctr 15 (arithmetic), Lctr 16 (shifts + Op2), Lctr 17 (bitwise), Lctr 18 (NZCV flags).

**Load / store / addressing**
- Lctr 20 (immediate offset), Lctr 21 (register offset, pseudo `LDR`), Lctr 22 (increment ops for vars and pointers), Lctr 23 (function calls + `LDRD`/`STRD`).

**Control flow in ASM**
- Lctr 19 (CCSs and conditional branch), Lctr 24 (combination branch + IT + conditional execution), Lctr 25 (if-else / if-else-if / compound tests), Lctr 26 (loops).
