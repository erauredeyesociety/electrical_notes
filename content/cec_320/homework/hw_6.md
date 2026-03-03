# CEC 320 — Complete Solutions Walkthrough

## HW3, HW4, HW5, and Quiz 2 — Every Problem, Step by Step

---

---

# HOMEWORK 3: GPIO & Bitwise Operations (135 pts)

---

## P1 (20 pts) — GPIO Mode Selection

For each scenario, pick the right mode.

**P1.1: Input, seeing HiZ as logic 1**

- The pin is an input, so we're choosing a pull resistor
- When nothing is driving the pin (HiZ), we want it to read 1
- A pull-up resistor connects the pin to Vcc, so when floating it reads high
- **Answer: Pull-up**

**P1.2: Input, seeing HiZ as logic 0**

- Same idea, but we want the default to be 0
- A pull-down resistor connects the pin to GND, so when floating it reads low
- **Answer: Pull-down**

**P1.3: Output, drawing current from load connected to higher voltage**

- The load is at a higher voltage than the MCU's Vcc
- Push-pull would try to drive high to Vcc, but the load needs higher — that's a problem
- Open-drain only pulls low (NMOS transistor to GND)
- An external pull-up can be connected to the higher voltage
- The pin either pulls low or floats, never tries to drive to MCU Vcc
- **Answer: Open-drain**

**P1.4: Output, LED on when output is logic 0**

- LED turns on when pin is LOW
- That means the LED is connected between Vcc and the pin
- When pin goes low, current flows from Vcc through LED into pin (sinking current)
- Open-drain can sink current (pull low) and float (LED off)
- **Answer: Open-drain**

**P1.5: Output, LED on when output is logic 1**

- LED turns on when pin is HIGH
- That means current flows from pin through LED to ground (sourcing current)
- We need to actively drive the pin to Vcc
- Push-pull has both PMOS (drive high) and NMOS (drive low)
- **Answer: Push-pull**

---

## P2 (20 pts) — GPIO Address Calculation

**Key info:**

    AHB1PERIPH_BASE = 0x4002_0000
    AHB2PERIPH_BASE = 0x4800_0000
    GPIOC offset    = 0x0800
    IDR offset      = 0x10
    ODR offset      = 0x14

**P2.1: Start address of GPIOC on AHB2**

    GPIOC base = AHB2 base + GPIOC offset
               = 0x4800_0000 + 0x0800
               = 0x4800_0800

**Answer: 0x4800_0800**

**P2.2: Address of IDR of GPIOC on AHB2**

    IDR address = GPIOC base + IDR offset
                = 0x4800_0800 + 0x10
                = 0x4800_0810

**Answer: 0x4800_0810**

**P2.3: Start address of GPIOC on AHB1**

    GPIOC base = AHB1 base + GPIOC offset
               = 0x4002_0000 + 0x0800
               = 0x4002_0800

**Answer: 0x4002_0800**

**P2.4: Address of ODR of GPIOC on AHB1**

    ODR address = GPIOC base + ODR offset
                = 0x4002_0800 + 0x14
                = 0x4002_0814

**Answer: 0x4002_0814**

---

## P3 (10 pts) — Shift Pitfall: Right-Then-Left

    Given: uint8_t A = 0b1010_1011;
    Find:  uint8_t B = (A >> 2) << 2;

**Step 1:** A is promoted to int (32-bit) before any operation.

    A = 0b0000_0000_0000_0000_0000_0000_1010_1011

**Step 2:** Right-shift by 2. Bottom 2 bits fall off.

    A >> 2 = 0b0000_0000_0000_0000_0000_0000_0010_1010

The original bottom 2 bits (1 and 1) are gone forever.

**Step 3:** Left-shift by 2. Fills bottom with 0s.

    (A >> 2) << 2 = 0b0000_0000_0000_0000_0000_0000_1010_1000

**Step 4:** Truncate to uint8_t (keep bottom 8 bits).

    B = 0b1010_1000

**Answer: 0b1010_1000**

The bottom 2 bits were cleared. Right-shifting first destroys information.

---

## P4 (10 pts) — Shift Pitfall: Left-Then-Right

    Given: uint8_t A = 0b1010_1011;
    Find:  uint8_t B = (A << 2) >> 2;

**Step 1:** A is promoted to int (32-bit).

    A = 0b0000_0000_0000_0000_0000_0000_1010_1011

**Step 2:** Left-shift by 2. Bits move up, nothing lost (32-bit has room).

    A << 2 = 0b0000_0000_0000_0000_0000_0010_1010_1100

The original bits are now at positions 9:2. No bits fell off the top because
we're in 32-bit space.

**Step 3:** Right-shift by 2. Moves everything back down.

    (A << 2) >> 2 = 0b0000_0000_0000_0000_0000_0000_1010_1011

**Step 4:** Truncate to uint8_t.

    B = 0b1010_1011

**Answer: 0b1010_1011** (same as A — nothing lost)

Key insight: left-shift in 32-bit preserves bits that would overflow 8-bit.

---

## P5 (10 pts) — Toggle Mask for Pin5 and Pin7

We need a mask with 1s at bit positions 5 and 7.

    Pin5 bit: 1U << 5 = 0b0010_0000 = 0x0020
    Pin7 bit: 1U << 7 = 0b1000_0000 = 0x0080

    Combine with OR:
    mask = 0x0020 | 0x0080 = 0x00A0

    Binary check: 0b1010_0000 — bits 5 and 7 are set ✓

**Answer: 0x00A0**

Usage: `GPIOx->ODR ^= 0x00A0;`

---

## P6 (10 pts) — OR and AND Operations

    Given: uint8_t A = 0b1010_1011;

**Part 1: B = A | (4U)**

    4U in binary = 0b0000_0100 (this is bit 2)

    Look at bit 2 of A:
    A =    0b1010_1011
                  ^
              bit 2 = 0

    OR with 1 sets a bit. Bit 2 was 0, becomes 1:
    A    = 0b1010_1011
    4U   = 0b0000_0100
    ----- OR ----------
    B    = 0b1010_1111

**Answer: B = 0b1010_1111**

**Part 2: C = A & ~(4U)**

    ~(4U) = ~(0b0000_0100) = 0b1111_1011 (all 1s except bit 2)

    AND with 0 clears a bit. But bit 2 of A was already 0:
    A      = 0b1010_1011
    ~(4U)  = 0b1111_1011
    ----- AND ----------
    C      = 0b1010_1011

**Answer: C = 0b1010_1011** (unchanged, bit 2 was already 0)

---

## P7 (10 pts) — OTYPER Manipulation

**P7.1: OTYPER = 0x0000_1234, then GPIOB->OTYPER |= (1U << 3)**

    First, what is bit 3 of 0x1234?
    Look at the bottom nibble: 0x4 = 0b0100
    Bit 3 of 0x4 = 0 (bits are: bit3=0, bit2=1, bit1=0, bit0=0)

    So bit 3 is currently 0. OR with (1U << 3) = 0x0008 sets it:
    0x1234 | 0x0008 = 0x123C

    Verify: 0x34 = 0b0011_0100, OR with 0x08 = 0b0000_1000:
            0b0011_0100
          | 0b0000_1000
          = 0b0011_1100 = 0x3C ✓

**Answer: 0x0000_123C**

**P7.2: Change Pin 4 to push-pull**

    Push-pull means OTYPER bit = 0
    We need to CLEAR bit 4

**Answer: `GPIOB->OTYPER &= ~(1U << 4);`**

---

## P8 (30 pts) — Hex Digit Manipulation

    Given: A is uint16_t = 0xH3H2H1H0 (arbitrary hex digits)
    Target digit H1 is at bits 7:4, so shift = 4

**P8a: Clear H1 to 0** → Result: 0xH3H20H0

    A &= ~(0xFU << 4);

    This creates mask ~(0x00F0) = 0xFF0F
    AND clears bits 7:4, leaving everything else alone

**P8b: Set H1 to F** → Result: 0xH3H2FH0

    A |= (0xFU << 4);

    0xFU << 4 = 0x00F0. OR with all 1s guarantees 1s regardless of prior value.
    No need to clear first because F = all 1s.

**P8c: Set H1 to 6** → Result: 0xH3H26H0

    A &= ~(0xFU << 4);    // clear: A has ...0... at H1
    A |= (0x6U << 4);     // set:   A has ...6... at H1

    Must clear first because if H1 was, say, 0xB = 0b1011, and you OR with
    0x6 = 0b0110, you'd get 0b1111 = 0xF, not 0x6.

**P8d: Set H1 to 9** → Result: 0xH3H29H0

    A &= ~(0xFU << 4);    // clear H1
    A |= (0x9U << 4);     // set H1 to 9

**P8e: Complement H1** → Result: 0xH3H2(H̄1)H0 where H̄ = 15 − H

    A ^= (0xFU << 4);

    XOR with F = 0b1111 flips all 4 bits of the digit.
    Example: if H1 = 0x3 = 0b0011, XOR with 0b1111 = 0b1100 = 0xC = 15-3 ✓

**P8f: Shift right by one hex digit** → Result: 0x0H3H2H1

    A >>= 4;

    Each hex digit is 4 bits. Shifting right by 4 moves every digit
    one position right. H0 is lost. A 0 fills in from the top.

---

## P9 (15 pts) — Wire-AND

**What is open-drain?** Only has an NMOS transistor. Can pull the line LOW (transistor on) or let it FLOAT (transistor off). Cannot actively drive HIGH. Needs an external pull-up resistor to reach Vcc.

**Why can open-drain outputs be wire-ANDed?** Connect multiple open-drain outputs to the same line with one shared pull-up. If ALL transistors are off, the pull-up brings the line HIGH. If ANY transistor turns on, it pulls the line LOW. This is AND logic: output is 1 only when all inputs are 1.

**What if push-pull outputs are connected together?** If one drives HIGH (connects to Vcc) and another drives LOW (connects to GND), there's a direct short circuit path: Vcc → PMOS of one → wire → NMOS of other → GND. This is called bus contention or shoot-through. It can damage the chip or draw excessive current.

---

---

# HOMEWORK 4: Interrupts & Preemption (130 pts)

---

## P1 (25 pts) — Reading a GPIO Pin

    Code: bool PA1_state = ((GPIOA->IDR & GPIO_PIN_1) == GPIO_PIN_1);

**P1.1: What is GPIO_PIN_1?**

    GPIO_PIN_1 = (1U << 1) = 0b0000_0000_0000_0010

**Answer: 0x0002**

**P1.2: Key pressed, Pin 1 = 1. What is IDR & GPIO_PIN_1?**

    IDR has bit 1 = 1 (among other bits we don't care about)
    IDR & 0x0002 isolates bit 1
    Since bit 1 = 1: result = 0x0002

**Answer: 0x0002**

**P1.3: What is (0x0002 == GPIO_PIN_1)?**

    0x0002 == 0x0002 → true

**Answer: true (1)**

**P1.4: Key released, Pin 1 = 0. What is IDR & GPIO_PIN_1?**

    IDR has bit 1 = 0
    IDR & 0x0002: bit 1 AND 0 = 0, so result = 0x0000

**Answer: 0x0000**

**P1.5: What is (0x0000 == GPIO_PIN_1)?**

    0x0000 == 0x0002 → false

**Answer: false (0)**

---

## P2 (15 pts) — Interrupt Response Time

    Given: 8 cycles stacking, 10 ISR instructions, 3-stage pipeline, 8 cycles unstacking

**Step 1: Stacking**

    Hardware pushes 8 registers (R0-R3, R12, LR, PC, xPSR)
    Takes 8 cycles
    ISR address is fetched IN PARALLEL (no extra cost)

**Step 2: ISR execution**

    3-stage pipeline: Fetch → Decode → Execute
    First instruction: takes 3 cycles to fill pipeline
    Each subsequent instruction: 1 cycle (pipeline is full)
    Total for 10 instructions: 3 + (10 - 1) = 3 + 9 = 12 cycles

**Step 3: Unstacking**

    Hardware pops 8 registers back
    Takes 8 cycles

**Step 4: Total**

    8 + 12 + 8 = 28 cycles

**Answer: 28 cycles**

---

## P3 (5 pts) — PSR to IRQn

    Given: PSR exception number = 22

    Formula: IRQn = PSR exception number - 16

    Exception numbers 1-15 are system exceptions (Reset, NMI, HardFault, etc.)
    Peripheral interrupts start at exception number 16

    IRQn = 22 - 16 = 6

**Answer: IRQn = 6**

---

## P4 (10 pts) — NVIC and SysTick Addresses

    SCS_BASE = 0xE000_E000 (System Control Space)

**NVIC:**

    NVIC_BASE = SCS_BASE + 0x0100
              = 0xE000_E000 + 0x0100
              = 0xE000_E100

**Answer: NVIC at 0xE000_E100**

**SysTick:**

    SysTick_BASE = SCS_BASE + 0x0010
                 = 0xE000_E000 + 0x0010
                 = 0xE000_E010

**Answer: SysTick at 0xE000_E010**

---

## P5 (10 pts) — NVIC Element Addresses

    Given: NVIC struct starts at 0xE000_0000 (simplified for this problem)

**Address of ICER[4]:**

    ICER array offset from NVIC base = 0x080
    ICER is uint32_t → each element is 4 bytes
    Element 4 offset = 4 × 4 = 16 = 0x10

    Address = 0xE000_0000 + 0x080 + 0x10
            = 0xE000_0090

**Answer: 0xE000_0090**

**Address of IP[4]:**

    IP array offset from NVIC base = 0x300
    IP is uint8_t → each element is 1 byte
    Element 4 offset = 4 × 1 = 4 = 0x04

    Address = 0xE000_0000 + 0x300 + 0x04
            = 0xE000_0304

**Answer: 0xE000_0304**

---

## P6 (10 pts) — ICPR for IRQn 69

**Which ICPR register?**

    Each ICPR register is 32 bits → covers 32 IRQs
    Register index = IRQn / 32 = 69 / 32 = 2 (since 32×2=64, 69 > 64)

    (64 through 95 are in ICPR[2])

**Answer: ICPR[2]**

**Which bit?**

    Bit position = IRQn % 32 = 69 % 32 = 69 - 64 = 5

**Answer: bit 5**

To clear pending: write 1 to bit 5 of ICPR[2].

---

## P7 (35 pts) — Priority and Preemption

    Given: 4 implemented bits, n=2 preemption bits, m=2 sub-priority bits
    IP register: PN << (8 - 4) = PN << 4
    PN = (PPN << 2) + SPN

**Step 1: Decompose all three priorities**

    IRQn1: PN = 12
        Binary: 12 = 0b1100
        PPN = 12 >> 2 = 3
        SPN = 12 & 0x3 = 12 & 3 = 0
        Check: (3 << 2) + 0 = 12 ✓

    IRQn2: PN = 7
        Binary: 7 = 0b0111
        PPN = 7 >> 2 = 1
        SPN = 7 & 0x3 = 7 & 3 = 3
        Check: (1 << 2) + 3 = 7 ✓

    IRQn3: PN = 3
        Binary: 3 = 0b0011
        PPN = 3 >> 2 = 0
        SPN = 3 & 0x3 = 3 & 3 = 3
        Check: (0 << 2) + 3 = 3 ✓

**P7.1: Value of NVIC->IP[IRQn2] in binary?**

    IP = PN << 4 = 7 << 4 = 112
    Binary: 0b0111_0000

**Answer: 0b0111_0000 (= 0x70)**

**P7.2: Can IRQn1 preempt IRQn2?**

    Rule: A preempts B only if PPN_A < PPN_B (strictly less)
    PPN1 = 3, PPN2 = 1
    3 < 1? No. 3 is greater than 1.

**Answer: No.** IRQn1 has lower priority (higher PPN number) than IRQn2.

**P7.3: Can IRQn3 preempt IRQn2?**

    PPN3 = 0, PPN2 = 1
    0 < 1? Yes.

**Answer: Yes.** IRQn3 has higher priority (lower PPN number).

**P7.4: PN range to preempt IRQn2?**

    IRQn2 has PPN = 1
    To preempt: need PPN < 1, so PPN must be 0
    With PPN = 0 and m = 2 sub-priority bits:
        SPN can be 0, 1, 2, or 3
        PN = (0 << 2) + SPN = 0 to 3

**Answer: PN 0 to 3**

**P7.5: PN range to NOT preempt IRQn2?**

    Need PPN >= 1, so PPN can be 1, 2, or 3
    Minimum PN: PPN=1, SPN=0 → (1 << 2) + 0 = 4
    Maximum PN: PPN=3, SPN=3 → (3 << 2) + 3 = 15

**Answer: PN 4 to 15**

---

## P8 (20 pts) — EXTICR Configuration

    Goal: Configure PC3 for EXTI3 using EXTICR1

**Step 1: Find which EXTICR register**

    EXTI0-3 → EXTICR1
    EXTI4-7 → EXTICR2
    EXTI8-11 → EXTICR3
    EXTI12-15 → EXTICR4

    EXTI3 is in EXTICR1 ✓

**Step 2: Find the shift amount**

    EXTICR1 layout:
        bits [15:12] = EXTI3 field
        bits [11:8]  = EXTI2 field
        bits [7:4]   = EXTI1 field
        bits [3:0]   = EXTI0 field

    For EXTI3: shift = (3 % 4) × 4 = 3 × 4 = 12

**Step 3: Find the port code**

    PA=0x0, PB=0x1, PC=0x2, PD=0x3, PE=0x4, PF=0x5, PG=0x6
    Port C = 0x2

**P8.1: MASK_FOR_EXTI3**

    We need to clear a 4-bit field at shift = 12
    Mask = 0xFU << 12 = 0xF000

**Answer: 0xF000**

**P8.2: VALUE_FOR_EXTI3_PC**

    Port code for PC = 0x2, shifted to position 12
    Value = 0x2U << 12 = 0x2000

**Answer: 0x2000**

The code would be:

    SYSCFG->EXTICR1 &= ~0xF000;   // clear EXTI3 field
    SYSCFG->EXTICR1 |=  0x2000;   // set to Port C

---

---

# HOMEWORK 5: Real Numbers (116 pts)

---

## P1 (8 pts) — Encode 2.75 in UQ3.5

    Format: UQ3.5 = 3 integer bits, 5 fraction bits, 8 bits total, unsigned

**Step 1: Multiply by 2^n**

    I = 2.75 × 2^5
    I = 2.75 × 32
    I = 88

**Step 2: Check if rounding needed**

    88 is already an integer. No rounding needed.

**Step 3: Convert to hex**

    88 = 5×16 + 8 = 0x58

**Step 4: Verify**

    Decode: 0x58 = 88, then 88 × 2^(-5) = 88/32 = 2.75 ✓

**Answer: 0x58**

---

## P2 (16 pts) — Decode Q3.4 Codes

    Format: Q3.4 = 1 sign + 3 integer + 4 fraction = 8 bits total (N=8)
    Decode formula: read as unsigned U, if MSB=1 then I = U - 2^N, then f = I × 2^(-n)

**P2a: Decode C1 = 0x77**

**Step 1: Convert to unsigned integer**

    U = 0x77 = 7×16 + 7 = 119

**Step 2: Check MSB**

    0x77 = 0b0111_0111
    MSB (bit 7) = 0 → positive
    I = 119

**Step 3: Scale by 2^(-n)**

    f = 119 × 2^(-4) = 119 / 16 = 7.4375

**Answer: 7.4375**

**P2b: Decode C2 = 0xAA**

**Step 1: Convert to unsigned integer**

    U = 0xAA = 10×16 + 10 = 170

**Step 2: Check MSB**

    0xAA = 0b1010_1010
    MSB (bit 7) = 1 → negative
    I = U - 2^N = 170 - 256 = -86

**Step 3: Scale by 2^(-n)**

    f = -86 × 2^(-4) = -86 / 16 = -5.375

**Answer: -5.375**

---

## P3 (10 pts) — Decode Q2.5 Code 0b1001_1001

    Format: Q2.5 = 1 sign + 2 integer + 5 fraction = 8 bits total (N=8)

**Step 1: Convert to unsigned integer**

    0b1001_1001 = 0x99
    U = 9×16 + 9 = 153

**Step 2: Check MSB**

    Bit 7 = 1 → negative
    I = 153 - 256 = -103

**Step 3: Scale by 2^(-n)**

    f = -103 × 2^(-5) = -103 / 32

    Long division: 103 / 32 = 3 remainder 7
    7/32 = 0.21875
    So 103/32 = 3.21875

    f = -3.21875

**Answer: -3.21875**

---

## P4 (32 pts) — Encode Real Numbers in Q3.4

    Format: Q3.4 = 1 sign + 3 integer + 4 fraction = 8 bits (N=8), n=4
    Encode: I = round(f × 2^n). If negative: code = I + 2^N.

**P4a: f = 0.5**

**Step 1:** I = 0.5 × 2^4 = 0.5 × 16 = 8
**Step 2:** 8 is already integer, no rounding
**Step 3:** Positive, so code = 8
**Step 4:** 8 in hex = 0x08

**Answer: 0x08**

**P4b: f = 6.73**

**Step 1:** I = 6.73 × 2^4 = 6.73 × 16 = 107.68
**Step 2:** Round to nearest integer: 107.68 → 108 (0.68 ≥ 0.5, round up)
**Step 3:** Positive, so code = 108
**Step 4:** 108 = 6×16 + 12 = 0x6C
**Verify:** 108/16 = 6.75 (rounding error = |6.75 - 6.73| = 0.02)

**Answer: 0x6C**

**P4c: f = -2.25**

**Step 1:** I = -2.25 × 2^4 = -2.25 × 16 = -36
**Step 2:** Already integer, no rounding
**Step 3:** Negative → two's complement: code = -36 + 2^8 = -36 + 256 = 220
**Step 4:** 220 = 13×16 + 12 = 0xDC
**Verify:** 0xDC = 220, MSB=1, I = 220-256 = -36, f = -36/16 = -2.25 ✓

**Answer: 0xDC**

**P4d: f = -4.5**

**Step 1:** I = -4.5 × 2^4 = -4.5 × 16 = -72
**Step 2:** Already integer, no rounding
**Step 3:** Negative → code = -72 + 256 = 184
**Step 4:** 184 = 11×16 + 8 = 0xB8
**Verify:** 0xB8 = 184, MSB=1, I = 184-256 = -72, f = -72/16 = -4.5 ✓

**Answer: 0xB8**

---

## P5 (44 pts) — Q15 Multiply-Accumulate

    Compute: f_A = f1×f2 + f3×f4
    where f1=0.5, f2=0.25, f3=0.125, f4=0.0625
    Format: Q15 = Q0.15 → 16-bit signed, n=15

**Step 1: Encode (16 pts)**

    I = f × 2^15 = f × 32768

    I1 = 0.5    × 32768 = 16384
    I2 = 0.25   × 32768 = 8192
    I3 = 0.125  × 32768 = 4096
    I4 = 0.0625 × 32768 = 2048

    In hex:
    I1 = 16384 = 0x4000
    I2 = 8192  = 0x2000
    I3 = 4096  = 0x1000
    I4 = 2048  = 0x0800

    Quick check using powers of 2:
    0.5    = 2^(-1), so I = 2^(-1) × 2^15 = 2^14 = 16384 ✓
    0.25   = 2^(-2), so I = 2^13 = 8192 ✓
    0.125  = 2^(-3), so I = 2^12 = 4096 ✓
    0.0625 = 2^(-4), so I = 2^11 = 2048 ✓

**Step 2: Multiply and shift (16 pts)**

    Rule: I_product = (I_A × I_B) >> 15
    Use 32-bit intermediate to avoid overflow.

    Multiplication 1: I1 × I2
        I_T1 = 16384 × 8192
             = 2^14 × 2^13
             = 2^27
             = 134,217,728

        I_P1 = I_T1 >> 15
             = 2^27 >> 15
             = 2^12
             = 4096
             = 0x1000

    Multiplication 2: I3 × I4
        I_T2 = 4096 × 2048
             = 2^12 × 2^11
             = 2^23
             = 8,388,608

        I_P2 = I_T2 >> 15
             = 2^23 >> 15
             = 2^8
             = 256
             = 0x0100

**Step 3: Add (6 pts)**

    I_A = I_P1 + I_P2
        = 4096 + 256
        = 4352
        = 0x1100

    This is straightforward Q15 addition — same format, just add the integers.

**Step 4: Decode (6 pts)**

    f_A = I_A × 2^(-15)
        = 4352 / 32768
        = 0.1328125

**Verify against expected result:**

    0.5 × 0.25     = 0.125
    0.125 × 0.0625 = 0.0078125
    Sum             = 0.1328125 ✓

**Answer: f_A = 0.1328125**

---

---

# QUIZ 2 (100 pts)

---

## P1 (10 pts) — Toggle Pin1, Pin3, Pin5

**Part 1: What is the mask? (6 pts)**

    Pin1: 1U << 1 = 0b0000_0000_0010 = 0x0002
    Pin3: 1U << 3 = 0b0000_0000_1000 = 0x0008
    Pin5: 1U << 5 = 0b0000_0010_0000 = 0x0020

    Combine with OR:
    mask = 0x0002 | 0x0008 | 0x0020 = 0x002A

    Binary check: 0b0000_0000_0010_1010
    Bits 1, 3, 5 are set ✓

**Answer: 0x002A**

**Part 2: C code (4 pts)**

    GPIOA->ODR ^= 0x002A;

---

## P2 (30 pts) — Hex Digit Rearrangement

    Given: A = 0xH3H2H1H0 (uint16_t)

**P2a (6 pts): Set H1 to 5** → Result: 0xH3H25H0

    Step 1: Clear H1 (bits 7:4)
        A &= ~(0xFU << 4);

    Step 2: Set H1 to 5
        A |= (0x5U << 4);

    This is the standard clear-then-set for a 4-bit field.

**P2b (6 pts): 0xH3H2H1H0 → 0xH2H1H03**

    Observation: every digit shifted left by one position. H3 is lost (16-bit overflow).
    The new bottom digit H0 is forced to 3.

    Step 1: Shift left by 4 (one hex digit)
        A << 4 gives: 0xH2H1H00 (bottom digit = 0)

    Step 2: OR in the constant 3 at the bottom
        | 0x3U gives: 0xH2H1H03

    Code:
        A = (A << 4) | 0x3U;

**P2c (6 pts): 0xH3H2H1H0 → 0x7H3H2H1**

    Observation: every digit shifted right by one position. H0 is lost.
    The new top digit H3 is forced to 7.

    Step 1: Shift right by 4
        A >> 4 gives: 0x0H3H2H1 (top digit = 0)

    Step 2: OR in 7 at the top (position 3 = shift 12)
        | (0x7U << 12) gives: 0x7H3H2H1

    Code:
        A = (A >> 4) | (0x7U << 12);

**P2d (6 pts): 0xH3H2H1H0 → 0xH0_H̄3_H2_H1** (H̄3 means 15 - H3)

    This one is complex. Let's trace what happens to each digit:
        H0 → moves to position 3 (top)
        H3 → moves to position 2, AND gets complemented
        H2 → moves to position 1 (shifted right by one)
        H1 → moves to position 0 (shifted right by one)

    Step 1: Extract H0 before we lose it
        uint16_t h0 = A & 0xF;          // isolates bottom digit

    Step 2: Extract H3 and complement it
        uint16_t h3c = ((A >> 12) & 0xF) ^ 0xF;
        // (A >> 12) & 0xF extracts H3
        // ^ 0xF flips all 4 bits (complement = 15 - H)

    Step 3: Shift A right by 4 to move H2→H1 and H1→H0
        (A >> 4) gives 0x0H3H2H1
        Mask out the top two digits to keep only H2 and H1:
        (A >> 4) & 0x00FF gives 0x00H2H1

    Step 4: Place h3c at position 2 and h0 at position 3
        | (h3c << 8)   → puts complemented H3 at bits 11:8
        | (h0 << 12)   → puts H0 at bits 15:12

    Code:
        uint16_t h0 = A & 0xF;
        uint16_t h3c = ((A >> 12) & 0xF) ^ 0xF;
        A = ((A >> 4) & 0x00FF) | (h3c << 8) | (h0 << 12);

**P2e (6 pts): 0xH3H2H1H0 → 0xF_H0_H3_H2**

    Trace each digit:
        F   → position 3 (constant)
        H0  → position 2 (was at 0, jumps to 2)
        H3  → position 1 (was at 3, drops to 1)
        H2  → position 0 (was at 2, drops to 0)

    Step 1: Extract H0 before it gets overwritten
        uint16_t h0 = A & 0xF;

    Step 2: Shift A right by 8 to get H3 and H2 into positions 1 and 0
        A >> 8 gives: 0x00H3H2
        This puts H3 at position 1 and H2 at position 0 ✓

    Step 3: Place H0 at position 2
        | (h0 << 8) gives: 0x0_H0_H3_H2

    Step 4: Force top digit to F
        | (0xFU << 12) gives: 0xF_H0_H3_H2

    Code:
        uint16_t h0 = A & 0xF;
        A = (A >> 8) | (h0 << 8) | (0xFU << 12);

---

## P3 (10 pts) — ICPR for IRQn 64

**Which ICPR register?**

    Register index = IRQn / 32
    64 / 32 = 2

    ICPR[0] covers IRQn 0-31
    ICPR[1] covers IRQn 32-63
    ICPR[2] covers IRQn 64-95 ← this one

**Answer: ICPR[2]**

**Which bit?**

    Bit position = IRQn % 32
    64 % 32 = 0

    IRQn 64 is the first interrupt in ICPR[2], so it's bit 0.

**Answer: bit 0**

---

## P4 (20 pts) — Reading PB4

    Code:
        uint16_t pb_idr = GPIOB->IDR;
        uint16_t pb4_val = pb_idr & GPIO_PIN_4;
        bool pb4_state = (pb4_val == GPIO_PIN_4);

**P4.1: Value of GPIO_PIN_4?**

    GPIO_PIN_4 = (1U << 4) = 0b0000_0000_0001_0000

**Answer: 0x0010**

**P4.2: IDR = 0x7777, what is pb4_val?**

    We need to know if bit 4 is set in 0x7777.
    Bit 4 is in nibble H1 (bits 7:4).
    H1 of 0x7777 = 7 = 0b0111.
    Within H1, bit 4 is the least significant bit of this nibble.
    0b0111 → bit0=1, so bit 4 = 1.

    Therefore: 0x7777 & 0x0010 = 0x0010 (bit 4 survives the mask)

**Answer: 0x0010**

**P4.3: What is pb4_state?**

    pb4_val = 0x0010
    GPIO_PIN_4 = 0x0010
    0x0010 == 0x0010 → true

**Answer: true**

**P4.4: IDR = 0x8888, what is pb4_val?**

    Again check bit 4 in 0x8888.
    H1 of 0x8888 = 8 = 0b1000.
    Bit 4 is the LSB of H1.
    0b1000 → bit0=0, so bit 4 = 0.

    Therefore: 0x8888 & 0x0010 = 0x0000

**Answer: 0x0000**

**P4.5: What is pb4_state?**

    pb4_val = 0x0000
    GPIO_PIN_4 = 0x0010
    0x0000 == 0x0010 → false

**Answer: false**

---

## P5 (30 pts) — Priority with 5 Implemented Bits

    Given: 5 implemented bits, n=2 preemption bits, m=3 sub-priority bits
    NVIC_SetPriority(IRQn3, 12)

    Key formulas:
        PN = (PPN << m) + SPN = (PPN << 3) + SPN
        IP = PN << (8 - 5) = PN << 3
        Max PPN = 2^n - 1 = 2^2 - 1 = 3
        Max SPN = 2^m - 1 = 2^3 - 1 = 7
        Max PN = (3 << 3) + 7 = 24 + 7 = 31

**P5.1 (10 pts): PPN, SPN, and IP value for IRQn3 with PN=12?**

    Decompose PN = 12:
        PPN = PN >> m = 12 >> 3 = 1
        SPN = PN & ((1 << m) - 1) = 12 & ((1 << 3) - 1) = 12 & 7 = 4

    Verify: (1 << 3) + 4 = 8 + 4 = 12 ✓

    IP register value:
        IP = PN << 3 = 12 << 3 = 96

    In hex: 96 = 0x60
    In binary: 0b0110_0000

**Answer: PPN = 1, SPN = 4, IP[IRQn3] = 0x60**

**P5.2 (10 pts): PN range to preempt IRQn3?**

    IRQn3 has PPN = 1
    To preempt: need PPN < 1, which means PPN must be 0

    With PPN = 0 and m = 3 sub-priority bits:
        SPN can range from 0 to 7 (= 2^3 - 1)
        Minimum PN: (0 << 3) + 0 = 0
        Maximum PN: (0 << 3) + 7 = 7

**Answer: PN 0 to 7**

**P5.3 (10 pts): PN range to NOT preempt IRQn3?**

    Need PPN >= 1, so PPN can be 1, 2, or 3

        Minimum PN: PPN=1, SPN=0 → (1 << 3) + 0 = 8
        Maximum PN: PPN=3, SPN=7 → (3 << 3) + 7 = 24 + 7 = 31

**Answer: PN 8 to 31**