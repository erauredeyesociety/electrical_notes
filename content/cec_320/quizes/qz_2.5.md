Part 1: GPIO & Bitwise Operations 

This part covers General‑Purpose Input/Output (GPIO) configuration, register manipulation, and essential bitwise techniques. Understanding these fundamentals is crucial for any embedded programming. 

1.1 GPIO Modes – When to Use What 

Each GPIO pin can be configured in several modes. The choice depends on the electrical requirements of the connected circuit. 

Input Modes 

When a pin is used as an input, you decide whether to enable internal pull‑up or pull‑down resistors, or leave it floating (no pull). This is controlled by the PUPDR register (2 bits per pin). 

Pull‑up (PUPDR = 01): Connects the pin to Vcc through a resistor. 

Use when: The input should read logic 1 when the external signal is high‑impedance (HiZ). Example: a button connected between the pin and ground; when the button is open, the pin is pulled high to Vcc, giving a stable 1. 

Pull‑down (PUPDR = 10): Connects the pin to GND through a resistor. 

Use when: The input should read logic 0 when HiZ. Example: a button connected between the pin and Vcc; when open, the pin is pulled low to GND. 

No pull (PUPDR = 00): The pin is floating (high‑impedance). 

Use when: The external circuit already provides a definite high or low level. Avoid floating inputs as they can pick up noise and cause erratic readings. 

Output Modes 

When a pin is an output, you choose the output type via OTYPER (1 bit per pin). The two options are push‑pull and open‑drain. 

Push‑pull (OTYPER = 0): The output stage has both a PMOS transistor (to drive high) and an NMOS transistor (to drive low). 

Use when: You need to actively drive the pin to either Vcc or GND. Examples: driving an LED with current sourcing (logic 1 = LED on), controlling a digital input of another chip. 

Open‑drain (OTYPER = 1): Only the NMOS transistor is present; it can pull the pin low, but to get a high level you must rely on an external pull‑up resistor. 

Use when:  

You only need to pull the line low (e.g., driving an LED that turns on with logic 0, where the LED is connected between Vcc and the pin).  

Multiple outputs share the same line (wire‑AND, see Section 1.7).  

You need to interface with a device operating at a higher voltage than the microcontroller’s Vcc (level shifting). The external pull‑up can be connected to the higher voltage. 

Key Decision Examples (from HW3 P1): 

“Output, turning on the LED when the output is logic 1” → Use push‑pull because the pin must actively source current to the LED (drive high).  

“Output, turning on the LED when the output is logic 0” → Use open‑drain with an external pull‑up to Vcc; the pin sinks current when low. 

“Load connected to higher voltage than Vcc” → Open‑drain; the external pull‑up can be tied to the higher voltage, and the pin only pulls down, avoiding damage. 

1.2 GPIO Register Summary 

GPIO peripherals are controlled via a set of registers. Each register is 32 bits wide, and each pin typically uses 1 or 2 bits within those registers. Important: When modifying a single pin’s configuration, always use read‑modify‑write operations (or BSRR for output) to avoid disturbing other pins. The BSRR register is especially useful because it can set and reset pins in a single write without affecting other bits. 

1.3 GPIO Address Calculation 

GPIO registers are memory‑mapped. To access a register, you need its absolute address. The formula is: 

Port base = Bus base + Port offset 
Register address = Port base + Register offset 
  

Bus Bases 

From the reference manual (Lecture 6 §6.4.4): 

PERIPH_BASE     = 0x4000_0000 
AHB1PERIPH_BASE = 0x4002_0000   (GPIOs on AHB1, e.g., GPIOA, GPIOB, ... on some STM32 families) 
AHB2PERIPH_BASE = 0x4800_0000   (GPIOs on AHB2 for other families; check your microcontroller) 
  

Note: The exact bus base depends on the specific STM32 family. In your course, you may use AHB2 for GPIOs. Always refer to the provided memory map. 

Port Offsets (typical) 

GPIOA   offset = 0x0000 
GPIOB   offset = 0x0400 
GPIOC   offset = 0x0800 
GPIOD   offset = 0x0C00 
... and so on. 

Register Offsets (from GPIO_TypeDef structure) 

MODER    offset = 0x00 
OTYPER   offset = 0x04 
OSPEEDR  offset = 0x08 
PUPDR    offset = 0x0C 
IDR      offset = 0x10 
ODR      offset = 0x14 
BSRR     offset = 0x18 

Step‑by‑Step Example (HW3 P2) 

“Find the address of the IDR register of GPIOC on AHB2.” 

Identify bus base for GPIOs: AHB2PERIPH_BASE = 0x4800_0000. 

Find GPIOC offset: 0x0800. 

Compute GPIOC base: 0x4800_0000 + 0x0800 = 0x4800_0800. 

Add IDR offset: 0x4800_0800 + 0x10 = 0x4800_0810. 

Answer: 0x4800_0810. 

1.4 Bitwise Operation Templates 

Bitwise operations are essential for manipulating individual bits or fields in registers. Here are the canonical patterns. 

Read a Bit (check if bit N is 1 or 0) 

result = (Reg & (1U << N)) != 0;  // returns true (non‑zero) if bit is set 
  

or result = (Reg >> N) & 1U; // shifts bit N to LSB, then masks 

Explanation: (1U << N) creates a mask with a 1 only at position N. ANDing with the register isolates that bit. If the result is non‑zero, the bit was 1. 

Set a Bit to 1 

Reg |= (1U << N); 
  

Explanation: OR with the mask forces bit N to 1, leaving all other bits unchanged. 

Clear a Bit to 0 

Reg &= ~(1U << N); 
  

Explanation: ~(1U << N) inverts the mask, creating a mask with 0 at position N and 1s elsewhere. ANDing clears only that bit. 

Toggle a Bit 

Reg ^= (1U << N);        // XOR with 1 toggles the bit 
  

If you need to toggle multiple bits at once, combine masks with OR: Reg ^= ( (1U << N) | (1U << M) ); 

Assign a Multi‑Bit Field 

When a register uses several adjacent bits for a setting (e.g., MODER uses 2 bits per pin), you must clear the old value then set the new one. 

Reg &= ~(FIELD_MASK << SHIFT);     // clear the field 
Reg |= (NEW_VALUE << SHIFT);       // set new value 
  

FIELD_MASK is a bitmask covering the field (e.g., for 2 bits, 0x3). 

SHIFT is the starting bit position of the field. 

Example (HW3 P5-like): Set MODER for pin 3 to output (01). MODER uses 2 bits per pin, so for pin 3 the bits are at positions 6 and 7 (since pin0: bits 0-1, pin1: bits 2-3, pin2: bits 4-5, pin3: bits 6-7). So: GPIOx->MODER &= ~(0x3U << 6); // clear bits 6-7 GPIOx->MODER |= (0x1U << 6); // set output mode (01) 

Example (HW3 P7): Given OTYPER = 0x0000_1234, then GPIOB->OTYPER |= (1U << 3);  

Original: 0x1234 = binary ... 0010 0011 0100 (bits 3-0: bit3 is the 4th bit? Let's compute: 0x1234 = 0b0001_0010_0011_0100. Bit 3 is the 4th bit from LSB: bit3 = (0x1234 >> 3) & 1 = 0 (since 0x1234 >> 3 = 0x246, LSB 0). After OR with (1<<3), bit3 becomes 1, so new value = 0x1234 | 0x0008 = 0x123C. So answer: 0x0000_123C. 

Example (HW3 P6): Given A = 0b1010_1011. 

B = A | 4U: 4U = bit2 = 1<<2 = 0b100. A = 0b1010_1011, bit2 was 0 → OR sets it → B = 0b1010_1111. 

C = A & ~(4U): ~4U = ...11111011, clears bit2; bit2 was already 0 → C = 0b1010_1011 (unchanged). 

 

1.5 Hex Digit Manipulation (Nibble‑Level Operations) 

Often you need to modify a specific hexadecimal digit (4 bits) within a 32‑bit variable. Each digit is a nibble. If we label digits from right to left as H₀ (least significant) to H₇ (most significant), then digit H₁ is at bits 7‑4 (shift of 4). In general, digit Hₖ is at bits (4*k) + 3 down to 4*k. The shift amount = 4*k. 

Common Operations (for digit H₁, shift = 4): 

Clear the digit to 0: 

A &= ~(0xFU << 4); 

(0xF is mask for 4 bits; shift to the digit’s position; AND with its complement clears those bits.) 

Set the digit to F (all ones): 

A |= (0xFU << 4); 

(No need to clear first, because OR with all 1s will set them regardless of previous state. However, if you want to replace with F, clearing is optional since F is all 1s.) 

Set the digit to a specific value V (0–15): 

First clear the digit, then OR with (V << shift). 

A &= ~(0xFU << 4); 

A |= (V << 4); 

Complement the digit (flip all bits): 

XOR with (0xFU << 4) flips each bit of that digit. 

A ^= (0xFU << 4); 

(Since XOR with 1 toggles, XOR with F toggles all four bits.) 

Right‑shift the entire value by one hex digit: 

A >>= 4; 

(Each hex digit is 4 bits, so shifting right by 4 moves to the next lower digit.) 

Examples from HW3 P8: 

(c) Set H₁ to 6: 

A &= ~(0xFU << 4); 

A |= (0x6U << 4); 

(e) Complement H₁: 

A ^= (0xFU << 4); 

(f) Shift right by one digit: 

A >>= 4; 

1.6 Shift Operation Pitfall with uint8_t 

In C, when you perform arithmetic or bitwise operations on types smaller than int, they are promoted to int (usually 32‑bit) before the operation. This can lead to unexpected results if you assume that shifting will discard bits beyond the original width. 

Example (HW3 P3 and P4) 

Given uint8_t A = 0b1010_1011 (0xAB). 

P3: uint8_t B = (A >> 2) << 2; 

A is promoted to int (32‑bit).  

A >> 2 gives 0b0010_1010 (top bits zeroed).  

Then << 2 gives 0b1010_1000.  

Finally, this int is truncated to uint8_t when assigned to B. Result: 0b1010_1000 (the bottom two bits have been cleared and lost). 

P4: uint8_t B = (A << 2) >> 2; 

A promoted to int.  

A << 2 gives 0b1010_1011_00 (32‑bits, no loss of high bits because they are now in bits 9‑2).  

Then >> 2 restores the original bits: 0b1010_1011.  

Truncation to uint8_t yields 0b1010_1011, same as original. 

Key Insight: When left‑shifting an 8‑bit value, the promotion to 32‑bit preserves bits that would otherwise overflow an 8‑bit variable. This can be useful but also dangerous if you expect them to be discarded. Always be aware of integer promotions. 

1.7 Wire‑AND (Open‑Drain and Bus Contention) 

Wire‑AND is a technique where multiple open‑drain outputs are connected to a single line, usually with a pull‑up resistor. The line behaves as the logical AND of all the outputs: it is high only when all outputs are in the high‑impedance (floating) state (i.e., each output’s transistor is off). If any output pulls low, the line goes low. 

Why it works with open‑drain 

An open‑drain output can only pull the line low (sink current) or release it (let it float).  

When the output is logic 1, the transistor is off, so the pin floats; the external pull‑up then brings the line high.  

When any output drives a logic 0, its transistor pulls the line low, overriding the pull‑up. 

Dangers of wiring push‑pull outputs 

If one push‑pull output drives high and another drives low, a direct short circuit occurs between Vcc and GND through the transistors. This is called bus contention or shoot‑through, and can damage the device or cause excessive current draw.  

Therefore, never connect push‑pull outputs directly together. 

Example (HW3 P9): Wire‑AND is used in I²C communication, where multiple devices share the SDA and SCL lines using open‑drain outputs and pull‑up resistors. 

Part 2: Exceptions & Interrupts 

This part covers the interrupt system on ARM Cortex‑M processors, including the NVIC (Nested Vectored Interrupt Controller), priority handling, and external interrupt configuration. 

2.1 Key Definitions 

Exception: Any event that changes the normal flow of program execution. This includes system faults, system calls (SVC), and interrupts. Exceptions originate from the processor core itself. 

Interrupt (IRQ): A type of exception triggered by a peripheral (e.g., GPIO, timer, UART). In ARM Cortex‑M, interrupts are numbered from 0 upward and are managed by the NVIC. 

NVIC (Nested Vectored Interrupt Controller): A hardware unit that handles interrupt prioritisation, nesting, and vectoring. It controls enabling/disabling, pending status, and priority of interrupts. 

ISR (Interrupt Service Routine): A function that executes in response to an interrupt. Its address is stored in the vector table. 

Callback: A user‑defined function that is called from within a generic ISR (often using a weak function attribute). This allows application‑specific code to be invoked without modifying the driver’s ISR. 

2.2 Reading a GPIO Pin with Masking 

To read the state of a specific GPIO pin, you must mask the IDR register to isolate that pin’s bit. The common pattern: 

bool pin_state = ((GPIOx->IDR & GPIO_PIN_n) == GPIO_PIN_n); 
  

Where GPIO_PIN_n is defined as (1U << n). 

Step‑by‑step (HW4 P1): 

Suppose GPIO_PIN_1 = (1U << 1) = 0x0002.  

GPIOx->IDR contains the current levels of all pins on that port.  

IDR & 0x0002 clears all bits except bit 1.  

If the result equals 0x0002, then bit 1 was 1 → pin high → key pressed (if active high).  

If the result equals 0, then bit 1 was 0 → pin low. 

Why compare with GPIO_PIN_n? 

Because IDR & mask could yield a non‑zero value even if the pin is high, but it might not equal the mask if multiple pins are high. However, since we are only interested in that one pin, (result != 0) would also work. Using == GPIO_PIN_n is a clear way to indicate we are testing for that specific pin being high. 

2.3 PSR Exception Number ↔ IRQn 

The Program Status Register (PSR) contains the current exception number when an exception is active. In the vector table, exception numbers 1‑15 are system exceptions (e.g., Reset, NMI, HardFault). Interrupts (IRQs) start at exception number 16. The mapping is: 

PSR exception number = IRQn + 16 
IRQn = PSR exception number − 16 
  

Example (HW4 P3): If PSR contains 22, then IRQn = 22 − 16 = 6, which corresponds to EXTI0_IRQn (if EXTI0 is IRQ #6 on your MCU). 

2.4 Interrupt Response Time Calculation 

Understanding the cycle count for an interrupt response helps in real‑time analysis. The sequence is: 

Stacking: The hardware automatically pushes 8 registers onto the current stack (MSP or PSP): R0‑R3, R12, LR, PC, and xPSR. This takes a fixed number of cycles (typically 8 or 12 depending on memory system). In your course, it’s given as 8 cycles. 

ISR fetch: The first instruction of the ISR is fetched in parallel with stacking, so it does not add extra cycles. 

ISR execution: The time to execute the ISR depends on its instruction count and the pipeline. For a 3‑stage pipeline (fetch, decode, execute), the first instruction takes 3 cycles, and each subsequent instruction takes 1 cycle (assuming no stalls). So for N instructions:ISR cycles = 3 + (N − 1) = N + 2 
  

Unstacking: After the ISR completes, the hardware pops the 8 registers, which also takes a fixed number of cycles (again, 8 cycles in your examples). 

Total interrupted time (from interrupt assertion to return to background) = Stacking + ISR execution + Unstacking. 

Example (HW4 P2):  

Stacking: 8 cycles  

ISR: 10 instructions → 3 + 9 = 12 cycles  

Unstacking: 8 cycles 

Total = 8 + 12 + 8 = 28 cycles. 

Note: This is a simplified model; actual cycle counts may vary due to memory wait states, caching, and pipeline effects. 

2.5 NVIC Address Calculation 

The NVIC registers are memory‑mapped. The base addresses are: 

SCS_BASE     = 0xE000_E000   (System Control Space base) 
NVIC_BASE    = SCS_BASE + 0x0100 = 0xE000_E100 
  

Inside the NVIC region, registers are arranged as arrays. The offsets from NVIC_BASE are given by the NVIC_Type structure in core_cm4.h: 

To find the address of a specific element: 

For a uint32_t array at offset arr_offset, element at index i:address = NVIC_BASE + arr_offset + (i * 4) 
  

For the uint8_t IP array:address = NVIC_BASE + 0x300 + (i * 1) 
  

Example (HW4 P5): 

Given NVIC at 0xE000_0000 (this is unusual; normally NVIC_BASE is 0xE000_E100, but the problem may use a simplified base). Let’s assume the problem states “NVIC at 0xE000_0000” for calculation. 

ICER[4]: ICER offset = 0x080, index 4 → 0xE000_0000 + 0x080 + 4*4 = 0xE000_0090. 

IP[4]: IP offset = 0x300, index 4 → 0xE000_0000 + 0x300 + 4*1 = 0xE000_0304. 

2.6 Accessing NVIC Registers by IRQn 

Each NVIC register (ISER, ICER, etc.) is 32 bits wide and covers 32 interrupts. To manipulate a specific IRQ, you need to know which register (index) and which bit within that register. 

Register index = IRQn / 32   (or IRQn >> 5) 
Bit position   = IRQn % 32   (or IRQn & 0x1F) 
  

Example (HW4 P6): IRQn = 69.  

Register index = 69 / 32 = 2 (since 32*2=64, remainder 5). So we use ICPR[2] to clear pending.  

Bit position = 69 % 32 = 5. So we write a 1 to bit 5 of ICPR[2]. 

Why this matters: When writing CMSIS‑core functions like NVIC_ClearPendingIRQ(), they perform this calculation internally. In assembly or direct register access, you must compute it yourself. 

2.7 Priority and Preemption 

Interrupt priorities are stored in the IP (Interrupt Priority) registers, each an 8‑bit byte per interrupt. However, only the most significant bits are implemented (the number of implemented bits varies by MCU). The priority number (PN) is divided into two parts: pre‑emption priority (PPN) and sub‑priority (SPN). 

Priority Field Layout 

IP byte: [ PPN (n bits) | SPN (m bits) | zeros (8−n−m bits) ] 
  

n = number of pre‑emption priority bits. 

m = number of sub‑priority bits. 

Total implemented bits = n + m ≤ 8. 

The priority number PN (the value you use in CMSIS functions like NVIC_SetPriority) is formed as: 

PN = (PPN << m) + SPN 
  

But note: When you call NVIC_SetPriority(IRQn, PN), the function stores the priority in the IP register shifted left so that it occupies the most significant implemented bits. In other words: 

NVIC->IP[IRQn] = PN << (8 − total_implemented_bits) 

Decomposing a PN 

Given PN, and knowing n and m: 

PPN = PN >> m 
SPN = PN & ((1 << m) − 1) 

Preemption Rules 

Interrupt A can preempt interrupt B only if PPN_A < PPN_B (strictly less).  

If PPN_A == PPN_B, they cannot preempt each other; if both are pending, the one with higher sub‑priority (smaller SPN) runs first, and if SPN equal, the lower IRQ number runs first. 

If A’s PPN is less than B’s, A can preempt B regardless of SPN values. 

Finding PN Ranges 

To preempt an interrupt with pre‑emption priority = T: need PPN < T. The maximum PN with PPN = T−1 is: 

PN_max = ((T−1) << m) + ((1 << m) − 1). So any PN in 0 to that value can preempt. 

To not preempt (i.e., be unable to preempt that interrupt): need PPN ≥ T. Minimum PN with PPN = T is T << m. So PN from T << m up to maximum possible PN (which is ((1 << n) − 1) << m) + ((1 << m) − 1)). 

Example (HW4 P7): 

Given 4 implemented priority bits, with n=2 pre‑emption bits and m=2 sub‑priority bits. Total implemented bits = 4, so shift left by 4 when writing to IP (i.e., IP = PN << 4). 

IRQn1: PN = 12 = 0b1100 → PPN = 12 >> 2 = 3, SPN = 12 & 0x3 = 0. 

IRQn2: PN = 7 = 0b0111 → PPN = 7 >> 2 = 1, SPN = 7 & 0x3 = 3. 

IRQn3: PN = 3 = 0b0011 → PPN = 3 >> 2 = 0, SPN = 3 & 0x3 = 3. 

Questions: 

Value in IP[IRQn2]: PN << 4 = 7 << 4 = 0b0111_0000 = 0x70. 

Can IRQn1 preempt IRQn2? PPN1=3, PPN2=1 → 3 is not less than 1, so No. 

Can IRQn3 preempt IRQn2? PPN3=0 < 1 → Yes. 

PN range to preempt IRQn2: Must have PPN < 1, so PPN = 0 only. With m=2, PN from 0 to (0<<2)+3 = 0–3. 

PN range to NOT preempt: PPN ≥ 1, so PN from (1<<2)=4 up to max: (3<<2)+3 = 12+3=15 → 4–15. 

2.8 EXTICR Configuration (External Interrupt Mapping) 

External interrupts (EXTI) allow GPIO pins to trigger interrupts. Each EXTI line (0‑15) can be connected to one of several ports. This mapping is done via the SYSCFG_EXTICR registers (in SYSCFG peripheral). There are four EXTICR registers (EXTICR1 to EXTICR4), each controlling four EXTI lines. 

Register Layout (EXTICR1 as example) 

EXTICR1: bits [15:12] = EXTI3 field 
         bits [11:8]  = EXTI2 field 
         bits [7:4]   = EXTI1 field 
         bits [3:0]   = EXTI0 field 
  

Each 4‑bit field holds a port code: 

0000 = PA, 0001 = PB, 0010 = PC, 0011 = PD, 0100 = PE, 0101 = PF, 0110 = PG 

Configuration Steps for EXTIx (x = 0..15) 

Determine which EXTICR register contains the field for EXTIx.  

EXTI0‑3 → EXTICR1  

EXTI4‑7 → EXTICR2  

EXTI8‑11 → EXTICR3  

EXTI12‑15 → EXTICR4 

Find the shift amount for the field:  

For EXTIx, the field starts at bit (x % 4) * 4. So for EXTI3 (x=3), shift = (3%4)*4 = 12. 

Clear the 4‑bit field: 

SYSCFG->EXTICRn &= ~(0xFU << shift);  

Set the desired port code: 

SYSCFG->EXTICRn |= (PORT_CODE << shift); 

Example (HW4 P8): Configure PC3 for EXTI3 (i.e., EXTI line 3 should be connected to Port C, pin 3).  

EXTI3 is in EXTICR1, shift = 12.  

Port code for PC = 0010 = 0x2.  

Clear: SYSCFG->EXTICR1 &= ~(0xFU << 12); → mask = 0xF000, clear bits 15‑12.  

Set: SYSCFG->EXTICR1 |= (0x2U << 12); → value = 0x2000. 

Note: Before configuring EXTI, you must also enable the SYSCFG clock, configure the GPIO pin as input (or alternate function if needed), and set up the EXTI itself (edge trigger, interrupt enable). The EXTICR only selects the port. 

Part 3: Real Numbers – Floating & Fixed Point 

This part explains how real numbers are represented in computers, both in floating‑point (IEEE 754) and fixed‑point formats. Fixed‑point is often used in embedded systems when a floating‑point unit is not available. 

3.1 IEEE 754 Single Precision Floating‑Point 

Single‑precision (32‑bit) floating‑point numbers are stored as: 

[1 bit Sign | 8 bits Exponent | 23 bits Fraction] 
  

Sign bit (S): 0 for positive, 1 for negative. 

Exponent (E): Stored as an 8‑bit unsigned integer with a bias of 127. So the actual exponent is E − 127. 

Fraction (F): The fractional part of the significand (mantissa). In normal numbers, there is an implicit leading 1, so the significand is 1.F (in binary). 

Decoding Steps (Hex → Real Number) 

Convert the 32‑bit hex value to binary. 

Extract S (bit 31), E (bits 30‑23), and F (bits 22‑0). 

Compute the fractional part as F_R = F × 2^(−23). (Because F is the fractional bits after the binary point.) 

If E is between 1 and 254 (normal numbers), the real value is:value = (−1)^S × (1 + F_R) × 2^(E − 127) 
  

Special cases: 

If E = 0 and F = 0 → value = ±0 (signed zero). 

If E = 255 and F = 0 → value = ±∞. 

If E = 255 and F > 0 → value = NaN (Not a Number). 

If E = 0 and F > 0 → subnormal numbers: value = (−1)^S × F_R × 2^(−126). (The implicit leading 1 is not present.) 

Why the implicit 1? In normalised form, the significand is always between 1 and 2, so the leading 1 is not stored, saving one bit of precision. 

Example: Decode 0x40490FDB (approximately π).  

Binary: 0x40490FDB = 0100 0000 0100 1001 0000 1111 1101 1011  

S = 0, E = 10000000 (128), F = 10010010000111111011011 (binary)  

F_R = F × 2^(−23) ≈ 0.5707963... (since 1.5707963... is the fractional part of π/2?) Wait, better to compute accurately: 

F = 0b10010010000111111011011 = 4,785,627? Actually let's trust known value: 0x40490FDB decodes to about 3.141592...  

1 + F_R ≈ 1.570796...? No, that's wrong; π ≈ 3.14159, so (1 + F_R) should be about 1.5708? That can't be because exponent is 128, so factor 2^(128-127)=2, so (1+F_R)*2 = π → 1+F_R = π/2 ≈ 1.5708. Yes, that matches: F_R ≈ 0.5708. So F_R ≈ 0.5708, 1+F_R ≈ 1.5708, times 2 gives π. Works. 

3.2 Unsigned Fixed‑Point (UQm.n) 

In unsigned fixed‑point format UQm.n, the number is stored as an unsigned integer of total bits m + n. There is no sign bit. The interpretation is: 

real_value = integer_code × 2^(−n) 
  

where integer_code is the unsigned integer value of the stored bits. 

Decoding (hex → real) 

Interpret the stored bits as an unsigned integer I. 

Compute f = I × 2^(−n). 

Encoding (real → hex) 

Multiply the real number by 2^n: I = f × 2^n. 

Round to the nearest integer (common rounding: half‑up or to nearest even). 

If I is within the representable range [0, 2^(m+n)−1], convert to hex. Otherwise, saturation/clipping may be needed. 

Example (HW5 P1): Encode 2.75 in UQ3.5.  

m = 3 integer bits, n = 5 fractional bits → total 8 bits.  

I = 2.75 × 2^5 = 2.75 × 32 = 88.  

88 in hex = 0x58.  

Check: 0x58 = 88 decimal, /32 = 2.75. 

 

3.3 Signed Fixed‑Point (Qm.n) 

Signed fixed‑point uses two’s complement representations. The format Qm.n means: 1 sign bit, m integer bits, n fractional bits, total bits N = 1 + m + n. 

Decoding (hex → real) 

Read the stored bits as an unsigned integer U. 

If the most significant bit (bit N‑1) is 0, then the signed integer I = U (positive). 

If the MSB is 1, then I = U − 2^N (two’s complement conversion). 

Then f = I × 2^(−n). 

Encoding (real → hex) 

Compute I = round(f × 2^n). (Round to nearest integer.) 

If I ≥ 0, the hex code is simply the N‑bit unsigned representation of I. 

If I < 0, compute the two’s complement: code = I + 2^N. Then convert to hex (N bits). 

Examples (HW5 P2, P3, P4c): 

P2: Decode Q3.4 code 0xAA.  

N = 1+3+4 = 8 bits. U = 0xAA = 170.  

MSB = 1 (since 0xAA >= 128) → I = 170 − 256 = −86.  

f = −86 × 2^(−4) = −86/16 = −5.375. 

P3: Decode Q2.5 code 0b1001_1001.  

N = 1+2+5 = 8 bits. U = 0x99 = 153.  

MSB = 1 → I = 153 − 256 = −103.  

f = −103 × 2^(−5) = −103/32 = −3.21875. 

P4c: Encode f = −2.25 in Q3.4.  

I = round(−2.25 × 2^4) = round(−36) = −36 (already integer).  

Negative, so code = −36 + 2^8 = −36 + 256 = 220 = 0xDC. 

3.4 Q15 and Q31 Specifics 

Q15 and Q31 are common fixed‑point formats used in DSP (Digital Signal Processing). They are essentially Q0.15 and Q0.31: 

Q15: 16‑bit signed, with 0 integer bits, 15 fractional bits. Range: [−1.0, +1.0 − 2^(−15)].  

Q31: 32‑bit signed, with 0 integer bits, 31 fractional bits. Range: [−1.0, +1.0 − 2^(−31)]. 

Encoding of −1.0:  

Q15: −1.0 × 2^15 = −32768. Two’s complements: −32768 + 65536 = 32768 = 0x8000.  

Q31: −1.0 × 2^31 = −2147483648. Two’s complements: −2147483648 + 4294967296 = 2147483648 = 0x8000_0000. 

Encoding of +1.0: Cannot be represented exactly because the maximum positive value is 0x7FFF (Q15) or 0x7FFF_FFFF (Q31), which equals 1 − 2^(−n). So +1.0 is out of range. 

Multiplication overflow: Multiplying −1.0 by −1.0 in Q15 gives (+1.0), which would be 0x7FFF if we could represent it, but the product of 0x8000 × 0x8000 (if treated as 32‑bit) yields 0x4000_0000, which after right‑shifting by 15 gives 0x8000 = −1.0 again. This is a known issue; often a saturation or correction is applied (e.g., using 0x8001 for −1.0 to avoid overflow). 

3.5 Fixed‑Point Arithmetic 

Fixed‑point arithmetic operates directly on the encoded integers, but careful scaling is required, especially for multiplication. 

Addition and Subtraction 

If two numbers have the same Q format (same n), you can simply add or subtract their integer codes: 

I_C = I_A ± I_B 

The result is also in the same Q format. However, you must guard against overflow (range expansion). For example, adding two Q15 numbers can exceed the 16‑bit range; you may need to saturate or use a wider accumulator. 

Multiplication 

When multiplying two fixed‑point numbers in Qm.n, the product is in Q(2m).(2n) if you simply multiply the integers. To return to the original Qm.n format, you must remove the extra scaling. 

General formula for multiplication (both operands have same n): 

I_C = (I_A × I_B) >> n 

Why the shift?  

Each operand is scaled by 2^n: f_A = I_A × 2^(−n), f_B = I_B × 2^(−n).  

Their product f_A × f_B = (I_A × I_B) × 2^(−2n).  

To represent the product in the same Qm.n format, we need I_C × 2^(−n). Therefore, I_C = (I_A × I_B) × 2^(−n), i.e., right‑shift the product by n bits. 

Important: The multiplication I_A × I_B may overflow the original integer width. To preserve precision, it is typically performed in a wider type (e.g., 32‑bit for 16‑bit inputs, or 64‑bit for 32‑bit inputs) before shifting. 

Example (HW5 P5): Q15 multiply‑accumulate f_A = 0.5×0.25 + 0.125×0.0625. 

Encode each operand to Q15: 

0.5 → I₁ = 0.5 × 32768 = 16384 = 0x4000  

0.25 → I₂ = 0.25 × 32768 = 8192 = 0x2000  

0.125 → I₃ = 0.125 × 32768 = 4096 = 0x1000  

0.0625 → I₄ = 0.0625 × 32768 = 2048 = 0x0800 

Multiply (use 32‑bit intermediate): 

I_T1 = I₁ × I₂ = 16384 × 8192 = 134,217,728 

I_P1 = I_T1 >> 15 = 134,217,728 / 32768 = 4096 = 0x1000  

I_T2 = I₃ × I₄ = 4096 × 2048 = 8,388,608 

I_P2 = I_T2 >> 15 = 8,388,608 / 32768 = 256 = 0x0100 

Add the products (still Q15): 

I_A = I_P1 + I_P2 = 4096 + 256 = 4352 = 0x1100 

Decode the result: 

f_A = 4352 × 2^(−15) = 4352 / 32768 = 0.1328125  

Exact calculation: 0.5×0.25 = 0.125, 0.125×0.0625 = 0.0078125, sum = 0.1328125. ✓ 

Note: If you need to accumulate many products, use a wider accumulator (e.g., 64‑bit) to avoid overflow before shifting back. 

Register 

Array Size 

Element Size 

Offset from NVIC_BASE 

ISER 

8 

uint32_t 

0x000 

ICER 

8 

uint32_t 

0x080 

ISPR 

8 

uint32_t 

0x100 

ICPR 

8 

uint32_t 

0x180 

IABR 

8 

uint32_t 

0x200 

IP 

240 

uint8_t 

0x300 

