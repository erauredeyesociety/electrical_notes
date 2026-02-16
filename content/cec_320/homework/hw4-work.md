# Homework 4 - Question Outline

## Problem 1
(Lecture 6, Section 6.6.1; Lecture 7, Section 7.4.1)

### 1.

> Reference: Lctr 6, Section 6.6.1 "Bit definition of the GPIO Input Data register" (Page 13)


GPIO_PIN_1 is a bit mask constant defined in STM32 HAL libraries. Each GPIO pin has a corresponding bit mask where only that specific bit is set to 1.


GPIO_PIN_1 = 0x0002 

2^1 = 2

**Answer: 2**

### 2.

> Reference: Lctr 6, Figure 7 (Page 13) showing IDR bit assignment, and Lctr 7, Section 7.4.1 "Using bitwise AND to check a bit" (Page 6)

GPIO_PIN_1 = 2 (binary: 0000 0000 0000 0010)

When pin is pressed, IDR bit 1 = 1

IDR value (only showing relevant bits): xxxx xxxx xxxx xx1x (bit 1 = 1)

Bitwise AND operation:


GPIO->IDR:    xxxx xxxx xxxx xx1x

GPIO_PIN_1:   0000 0000 0000 0010

AND result:   0000 0000 0000 0010 = 2

**Answer: 2**

### 3.

> Reference: Lctr 7, Section 7.4.1 (Page 6) - this is the standard method to check if a specific bit is set

From part 2: GPIO->IDR & GPIO_PIN_1 = 2

GPIO_PIN_1 = 2

The expression (GPIO->IDR & GPIO_PIN_1) == GPIO_PIN_1 compares if the result equals the mask.

Since 2 == 2 is true, the expression evaluates to 1 (true in C).

**Answer: 1**

### 4.

> Reference: Lctr 6, Figure 7 (Page 13) showing IDR bit assignment, and Lctr 7, Section 7.4.1 "Using bitwise AND to check a bit" (Page 6)

GPIO_PIN_1 = 2

When pin is released, IDR bit 1 = 0

IDR value: xxxx xxxx xxxx xx0x (bit 1 = 0)

Bitwise AND:

GPIO->IDR:    xxxx xxxx xxxx xx0x

GPIO_PIN_1:   0000 0000 0000 0010

AND result:   0000 0000 0000 0000 = 0

**Answer: 0**

### 5.

> Reference: Lctr 7, Section 7.4.1 (Page 6) - this is the standard method to check if a specific bit is set

From part 4: GPIO->IDR & GPIO_PIN_1 = 0

GPIO_PIN_1 = 2

Since 0 == 2 is false, the expression evaluates to 0 (false in C).

**Answer: 0**

---

## Problem 2

> Reference: Lctr 8, Section 8.4.6 "Interrupt stacking and unstacking" (Page 8) and Figure 3

Stacking phase: 8 clock cycles for stacking 8 registers (R0-R3, R12, LR, PC, PSR)

During this time, the address of the ISR is fetched (overlapped, so no extra cycles)

ISR execution phase: 10 instructions on a 3-stage pipeline

With a 3-stage pipeline (fetch, decode, execute), once the pipeline is filled, each instruction takes 1 cycle to execute

10 instructions = 10 clock cycles

Unstacking phase: 8 clock cycles to unstack the registers

Total = Stacking + ISR execution + Unstacking

= 8 + 10 + 8 = 26 clock cycles

**Answer: 26 clock cycles**

---

## Problem 3

> Reference: Lctr 8, Section 8.4.3 "PSR exception number" (Page 6)

From the lecture: "PSR exception number = 16 + IRQn"

Given: PSR exception number = 22

Therefore:
22 = 16 + IRQn
IRQn = 22 - 16 = 6

From the IRQn enum in Lctr 8 (Page 5), IRQn 6 corresponds to EXTI0_IRQn (EXTI Line0 Interrupt).

**Answer: 6**

---

## Problem 4

> Reference: Lctr 8, Section 8.6.1 "Definitions of the NVIC struct and pointer" (Page 9-10)

From the lecture (Page 10):

#define SCS_BASE      (0xE000E000UL)  // System Control Space

#define SysTick_BASE  (SCS_BASE + 0x0010UL)  // SysTick

#define NVIC_BASE     (SCS_BASE + 0x0100UL)  // NVIC Base

NVIC address:

NVIC_BASE = SCS_BASE + 0x0100

= 0xE000E000 + 0x0100

= 0xE000E100

SysTick address:

SysTick_BASE = SCS_BASE + 0x0010

= 0xE000E000 + 0x0010

= 0xE000E010

**Answer: NVIC: 0xE000E100, SysTick: 0xE000E010**

---

## Problem 5

> Reference: Lctr 8, Section 8.6.1 "Definitions of the NVIC struct and pointer" (Page 9)

From the NVIC struct definition (Page 9):

typedef struct {

    __IOM uint32_t ISER[8U];     // offset 0x000 (0x00 to 0x1C)
    
    uint32_t RESERVED0[24U];      // offset 0x020 to 0x07C
    
    __IOM uint32_t ICER[8U];      // offset 0x080 to 0x09C
    
    ...
    
    __IOM uint8_t  IP[240U];      // offset 0x300 to 0x3EF

} NVIC_Type;


Given: NVIC struct address = 0xE000_E000

For ICER[4]:

ICER array starts at offset 0x080

Each ICER element is 4 bytes (uint32_t)

ICER[4] is the 5th element (index 4)

Offset = 0x080 + (4 × 4) = 0x080 + 0x010 = 0x090

Address = 0xE000_E000 + 0x090 = 0xE000_E090

For IP[4]:

IP array starts at offset 0x300

Each IP element is 1 byte (uint8_t)

IP[4] is the 5th element (index 4)

Offset = 0x300 + 4 = 0x304

Address = 0xE000_E000 + 0x304 = 0xE000_E304

**Answer: ICER[4] = 0xE000_E090, IP[4] = 0xE000_E304**

---

## Problem 6

> Reference: Lctr 8, Section 8.6.2 "Direct access of NVIC registers" (Page 10)

From the lecture (Page 10):

"the index for the ISER register should be IRQn / 32"

"the bit location in a specific ISER register should be IRQn % 32"

This same logic applies to ICPR (Interrupt Clear Pending Register)

Given: IRQn = 69

ICPR index:
IRQn / 32 = 69 / 32 = 2 (since 32 × 2 = 64, and 32 × 3 = 96 which is > 69)

Bit position:

IRQn % 32 = 69 % 32 = 5 (since 69 - 64 = 5)

Therefore, we need to write to ICPR[2], bit 5.

**Answer: ICPR[2], bit 5**

---

## Problem 7

> Reference: Lctr 9, Section 9.3 "Priority of interrupt and preemption" (Pages 3-8)

Given information:

Most significant 4 bits of IP register are used (bits [7:4])

2 bits for preemption priority (PPN)

Therefore, remaining 2 bits (from the 4 bits) are for sub-priority (SPN)

Total bits used = 4, so PN values range from 0 to 15

From Lctr 9, Section 9.3.3 (Page 5):

PN = (PPN << m) + SPN, where m = number of sub-priority bits

Here, m = 2, so PN = (PPN << 2) + SPN

Priority number structure:

PPN: 2 bits (0-3)

SPN: 2 bits (0-3)

PN range: 0 to 15

### 1.

> Reference: Looking at the enum in Lctr 8 (Page 5), we can identify the IRQn numbers:

IRQn1, IRQn2, IRQn3 are not specified in the enum, but from context, they are likely:

IRQn2 = USART2_IRQn = 38 (from Lctr 8, Page 5: "USART2_IRQn = 38")

IRQn1 and IRQn3 are other interrupts (possibly EXTI0_IRQn = 6 and TIM2_IRQn = 28)

From Lctr 9, Section 9.3.6 (Page 8) - "Priority setups for the demo project":

4 bits total for PPN and SPN

2 bits for the priority group (PPN)

Fixed priority for UART2 with PPN = 1 and SPN = 0

Therefore:

PN for UART2 (IRQn2) = (1 << 2) + 0 = 4

NVIC->IP[IRQn2] stores this priority number in the most significant 4 bits:

PN = 4 = 0b0100

Stored in bits [7:4] of the IP register

So IP[IRQn2] = 0b0100xxxx (where xxxx are the unused lower 4 bits, typically 0)

In binary: 0100 0000 (or 0x40)

**Answer: 0100 0000 binary (or 0x40)**

### 2.

> Reference: Lctr 9, Section 9.3.2.1 "Preemption priority" (Page 3)

From the demo project in Lctr 9 (Page 8), IRQn1 is likely EXTIO_IRQn (IRQn = 6) which has:

Initial PPN = 2, SPN = 0 (PN = 8)

But can be changed to PPN = 1, SPN = 0 (PN = 4)

For IRQn1 (EXTIO) to preempt IRQn2 (UART2), we need PPN1 < PPN2.

IRQn2 (UART2) has fixed PPN = 1 (from Lctr 9, Page 8)

Two cases for IRQn1:

If IRQn1 has PPN = 2: 2 < 1? No → Cannot preempt

If IRQn1 has PPN = 1: 1 < 1? No (equal) → Cannot preempt (same preemption priority)

Since IRQn1 has PPN ≥ 1, it cannot preempt IRQn2 because preemption requires strictly smaller PPN value.

**Answer: No, IRQn1 cannot preempt IRQn2 because it has equal or greater PPN value (PPN1 ≥ PPN2). Preemption requires PPN1 < PPN2.**

### 3.

> Reference: Lctr 9, Section 9.3.2.1 "Preemption priority" (Page 3)

From the SysTick setup in Lctr 9 (Page 8): "Highest priority for SysTick timer with PPN = 0 and SPN = 0"

If IRQn3 is SysTick_IRQn (IRQn = -1):

PPN3 = 0

PPN2 = 1

Since PPN3 (0) < PPN2 (1), IRQn3 can preempt IRQn2.

**Answer: Yes, IRQn3 can preempt IRQn2 because PPN3 (0) < PPN2 (1).**

### 4.

> Reference: Lctr 9, Section 9.3.5, Example 2 (Page 8)

For IRQn4 to preempt IRQn2, we need PPN4 < PPN2.

Given PPN2 = 1, so PPN4 can be 0 only.

With PPN = 0, SPN can range from 0 to 3.

PN = (PPN << 2) + SPN = (0 << 2) + SPN = SPN

Therefore, PN range = 0 to 3

**Answer: 0 to 3 (inclusive)**

### 5.

> Reference: Lctr 9, Section 9.3.5, Example 2 (Page 8)

For IRQn4 to NOT preempt IRQn2, we need PPN4 ≥ PPN2.

Given PPN2 = 1, so PPN4 can be 1, 2, or 3.

Case 1: PPN4 = 1

SPN can be 0 to 3

PN = (1 << 2) + SPN = 4 + SPN

Range: 4 to 7

Case 2: PPN4 = 2

SPN can be 0 to 3

PN = (2 << 2) + SPN = 8 + SPN

Range: 8 to 11

Case 3: PPN4 = 3

SPN can be 0 to 3

PN = (3 << 2) + SPN = 12 + SPN

Range: 12 to 15

Combining all cases: PN range = 4 to 15

**Answer: 4 to 15 (inclusive)**

---

## Problem 8

> Reference: Lctr 9, Section 9.4.2 "Setting up an EXTI via using SYSCFG registers" (Page 12) and Lctr 7, Figure 6 (Page 9)

From Lctr 9, Page 12, the code pattern is:

SYSCFG->EXTICR[0] &= ~MASK_FOR_EXTIO;   // Clear the bits

SYSCFG->EXTICR[0] |= VALUE_FOR_EXTIO_PA; // Set the value

Now we're using EXTICR1 instead of EXTICR[0], and configuring PC3 for EXTI3.

Understanding EXTICR registers:

Each EXTICR register controls 4 EXTI lines (4 bits per line)

EXTICR0 controls EXTI0-3

EXTICR1 controls EXTI4-7

EXTICR2 controls EXTI8-11

EXTICR3 controls EXTI12-15

However, the problem states "Assume we are using EXTICR1 instead of EXTICR[0]" - this means EXTI3 is being configured through EXTICR1 instead of its normal position in EXTICR0.

For EXTI3 in EXTICR1:

EXTI3 would occupy 4 bits in EXTICR1

The position depends on which EXTI lines EXTICR1 controls

Normally EXTI3 is in EXTICR0, but if we're using EXTICR1 for EXTI3, it could be at bits 0-3, 4-7, 8-11, or 12-15

From Figure 2 in the problem (Control bits for EXTICR):

Port A = 0b0000

Port B = 0b0001

Port C = 0b0010

Port D = 0b0011

Port E = 0b0100

Port F = 0b0101

Port G = 0b0110

Port H = 0b0111

For PC3 (Port C, Pin 3), the port value = 0b0010 = 2

Assuming EXTI3 is placed in the lower 4 bits of EXTICR1 (bits 0-3):

### 1.

MASK_FOR_EXTI3:

Need to clear 4 bits for EXTI3

Mask with 1's where we want to clear

For bits 0-3: mask = 0xF (0b1111) at position 0

MASK_FOR_EXTI3 = 0xF << 0 = 0xF

**Answer: MASK_FOR_EXTI3 = 0xF000**

### 2.

VALUE_FOR_EXTI3_PC:

Port C value = 0b0010 = 2

Need to place this at bits 0-3

VALUE = 2 << 0 = 0x2

If EXTI3 is at bits 4-7:

MASK = 0xF << 4 = 0xF0

VALUE = 2 << 4 = 0x20

If EXTI3 is at bits 8-11:

MASK = 0xF << 8 = 0xF00

VALUE = 2 << 8 = 0x200

If EXTI3 is at bits 12-15:

MASK = 0xF << 12 = 0xF000

VALUE = 2 << 12 = 0x2000

Based on typical STM32 documentation, EXTI3 normally occupies bits 12-15 of EXTICR0. Since we're using EXTICR1 instead, and the problem mentions Figure 1 showing EXTICR bit fields, the most likely placement is bits 12-15 of EXTICR1.

Therefore:

MASK_FOR_EXTI3 = 0xF000

VALUE_FOR_EXTI3_PC = 0x2000

**Answer: VALUE_FOR_EXTI3_PC = 0x2000**