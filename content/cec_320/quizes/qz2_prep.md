# CEC 320 — Quiz Study Guide

## Homeworks 3, 4, & 5 | Lectures 6–9, 12–13

---

# Part 1: GPIO & Bitwise Operations (HW3, Lctr 6–7)

## 1.1 GPIO Modes — When to Use What

**For Input pins** (controlled by PUPDR, 2 bits per pin):
- HiZ should read as logic 1 → **Pull-up** (connects input to Vcc)
- HiZ should read as logic 0 → **Pull-down** (connects input to GND)
- No floating concern → **No-pull**

**For Output pins** (type controlled by OTYPER, 1 bit per pin):
- Need to both source AND sink current → **Push-pull** (both PMOS and NMOS)
- Only need to sink current (pull low) → **Open-drain** (NMOS only, needs external pull-up)
- LED turns on with logic 1 (source current to LED) → **Push-pull**
- LED turns on with logic 0 (sink current from LED) → **Open-drain**
- Load connected to higher voltage than Vcc → **Open-drain** (can level-shift)

> **HW3 P1 example:** "Output, turning on the LED when the output is logic 1"
> → Push-pull, because we need to actively drive the pin high to source current through the LED.


## 1.2 GPIO Register Summary

| Register | Purpose | Bits/Pin | Key Detail |
|----------|---------|----------|------------|
| MODER | Mode select | 2 | 00=Input, 01=Output, 10=AltFn, 11=Analog |
| OTYPER | Output type | 1 | 0=Push-pull, 1=Open-drain |
| OSPEEDR | Output speed | 2 | Usually leave default |
| PUPDR | Pull-up/down | 2 | 00=None, 01=Pull-up, 10=Pull-down |
| IDR | Input data (read) | 1 | Read-only |
| ODR | Output data (r/w) | 1 | Read-modify-write |
| BSRR | Bit set/reset | — | Write-only, atomic, no read-modify-write needed |


## 1.3 GPIO Address Calculation

**Formula:**

    Port base = Bus base + Port offset
    Register address = Port base + Register offset

**Bus bases** (from Lctr 6 §6.4.4):

    PERIPH_BASE     = 0x4000_0000
    AHB1PERIPH_BASE = 0x4002_0000
    AHB2PERIPH_BASE = 0x4800_0000

**Port offsets:** GPIOA = +0x0000, GPIOB = +0x0400, GPIOC = +0x0800, ...

**Register offsets** (from GPIO_TypeDef struct):

    MODER=+0x00, OTYPER=+0x04, OSPEEDR=+0x08, PUPDR=+0x0C
    IDR=+0x10, ODR=+0x14, BSRR=+0x18

> **HW3 P2 example:** "Address of IDR of GPIOC on AHB2"
> → GPIOC base = 0x4800_0000 + 0x0800 = 0x4800_0800
> → IDR = base + 0x10 = **0x4800_0810**


## 1.4 Bitwise Operation Templates

**Read a bit** (Lctr 7 §7.4.1):

    result = (Reg & (1U << N)) > 0;

**Set bit to 1** (Lctr 7 §7.4.2):

    Reg |= (1U << N);

**Clear bit to 0** (Lctr 7 §7.4.3):

    Reg &= ~(1U << N);

**Toggle bit(s)** (Lctr 7 §7.4.5):

    Reg ^= mask;       // where mask has 1s at positions to toggle

**Assign a multi-bit field** — two-step clear-then-set (Lctr 7 §7.4.4):

    Reg &= ~(FIELD_MASK << SHIFT);     // Step 1: clear
    Reg |= (NEW_VALUE << SHIFT);       // Step 2: set

> **HW3 P5 example:** "Toggle Pin5 and Pin7 of ODR — what mask?"
> → mask = (1U << 5) | (1U << 7) = 0x0020 | 0x0080 = **0x00A0**
> → Usage: `GPIOx->ODR ^= 0x00A0;`

> **HW3 P7 example:** "OTYPER = 0x0000_1234, then GPIOB->OTYPER |= (1U << 3)"
> → Bit 3 of 0x1234 is 0, OR with 1 sets it → 0x34 becomes 0x3C → result: **0x0000_123C**
> → "Change Pin 4 to push-pull" = clear bit 4: `GPIOB->OTYPER &= ~(1U << 4);`

> **HW3 P6 example:** Given A = 0b1010_1011:
> → `B = A | 4U`: 4U = bit 2; bit 2 was 0, OR sets it → **B = 0b1010_1111**
> → `C = A & ~(4U)`: ~4U clears bit 2; bit 2 was already 0 → **C = 0b1010_1011**


## 1.5 Hex Digit Manipulation (HW3 P8 patterns)

Each hex digit = 4 bits. Digit H₁ (second from right) sits at bits 7:4, so SHIFT = 4.

- **Clear a digit to 0:** `A &= ~(0xFU << 4);`
- **Set a digit to F:** `A |= (0xFU << 4);` (OR with all 1s always gives 1s — no clear needed)
- **Set a digit to specific value V:** clear first, then OR: `A &= ~(0xFU << 4); A |= (V << 4);`
- **Complement a digit (15 − H):** `A ^= (0xFU << 4);` (XOR with 1 flips each bit)
- **Right-shift entire value by one hex digit:** `A >>= 4;`

> **HW3 P8c example:** Set H₁ to 6 → `A &= ~(0xFU << 4); A |= (0x6U << 4);`
> **HW3 P8e example:** Complement H₁ → `A ^= (0xFU << 4);`
> **HW3 P8f example:** Shift right by one digit → `A >>= 4;`


## 1.6 Shift Operation Pitfall (uint8_t)

C promotes uint8_t to int (32-bit) before arithmetic.

> **HW3 P3:** `uint8_t B = (A >> 2) << 2;` where A = 0b1010_1011
> → Right-shift loses bottom 2 bits: 0b1010_1011 → 0b0010_1010
> → Left-shift fills with 0s: → 0b1010_1000
> → **B = 0b1010_1000** (bottom 2 bits cleared — information lost)

> **HW3 P4:** `uint8_t B = (A << 2) >> 2;` where A = 0b1010_1011
> → Left-shift first: promoted to 32-bit int, so top bits are NOT lost
> → Right-shift restores them → **B = 0b1010_1011** (equals A, nothing lost)
> → Key insight: left-shift in 32-bit preserves bits that would overflow 8 bits


## 1.7 Wire-AND (HW3 P9 concepts)

- **Open-drain/open-collector:** output can only pull low or float; needs external pull-up for high
- **Wire-AND works** because any single output pulling low drags the shared line low; line is high only when ALL outputs float (all logic 1) — mimics AND gate
- **Push-pull outputs must NEVER be wired together** — if one drives high and another drives low, short circuit from Vcc to GND (bus contention / shoot-through)

---

# Part 2: Exceptions & Interrupts (HW4, Lctr 8–9)

## 2.1 Key Definitions

- **Exception:** originates from ARM core (system faults, SysTick, SVC)
- **Interrupt (IRQ):** originates from peripherals (GPIO EXTI, UART, timers)
- **NVIC:** Nested Vectored Interrupt Controller — hardware that manages all of the above
- **ISR:** Interrupt Service Routine — the function that runs when an interrupt fires
- **Callback:** user-defined function called from within an ISR (weak function override pattern)


## 2.2 Reading a GPIO Pin with Masking (HW4 P1 pattern)

    bool state = ((GPIOx->IDR & GPIO_PIN_n) == GPIO_PIN_n);

- GPIO_PIN_n = (1U << n) — a mask with only bit n set
- AND isolates bit n from IDR; all other bits become 0
- If pin is high: result == GPIO_PIN_n → true (1)
- If pin is low: result == 0 → false (0)

> **HW4 P1 example:** GPIO_PIN_1 = (1U << 1) = 0x0002
> → Key pressed (bit 1 = 1): IDR & 0x0002 = 0x0002, equals GPIO_PIN_1 → **true**
> → Key released (bit 1 = 0): IDR & 0x0002 = 0x0000, not equal → **false**


## 2.3 PSR Exception Number ↔ IRQn

**Conversion** (Lctr 8 §8.4.3):

    PSR exception number = IRQn + 16
    IRQn = PSR exception number − 16

> **HW4 P3 example:** PSR = 22 → IRQn = 22 − 16 = **6** (which is EXTI0_IRQn)


## 2.4 Interrupt Response Time Calculation

**Sequence** (Lctr 8 §8.4.6, Figure 3):

    1. Stacking:  hardware pushes 8 registers (R0-R3, R12, LR, PC, PSR)
    2. ISR fetch:  happens IN PARALLEL with stacking (no extra cycles)
    3. ISR execution: count cycles using pipeline model
    4. Unstacking: hardware pops the 8 registers back

**Pipeline execution** (N instructions, P-stage pipeline):

    Total cycles = P + (N − 1)

**Total interrupted time = stacking cycles + ISR cycles + unstacking cycles**

> **HW4 P2 example:** 8 cycles stacking + (3 + 9 = 12) ISR cycles + 8 cycles unstacking = **28 cycles**
> (10 instructions on 3-stage pipeline: first takes 3 cycles, remaining 9 take 1 each)


## 2.5 NVIC Address Calculation

**Base addresses** (Lctr 8 §8.6.1):

    SCS_BASE     = 0xE000_E000
    SysTick_BASE = SCS_BASE + 0x0010 = 0xE000_E010
    NVIC_BASE    = SCS_BASE + 0x0100 = 0xE000_E100

**NVIC struct offsets** (from NVIC_Type in core_cm4.h):

    ISER[8]  → offset 0x000   (uint32_t, 4 bytes each)
    ICER[8]  → offset 0x080
    ISPR[8]  → offset 0x100
    ICPR[8]  → offset 0x180
    IABR[8]  → offset 0x200
    IP[240]  → offset 0x300   (uint8_t, 1 byte each)

**Element address formula:**

    For uint32_t arrays: base + array_offset + (index × 4)
    For uint8_t arrays:  base + array_offset + (index × 1)

> **HW4 P5 example:** Given NVIC at 0xE000_0000:
> → ICER[4] = 0xE000_0000 + 0x080 + (4×4) = **0xE000_0090**
> → IP[4] = 0xE000_0000 + 0x300 + (4×1) = **0xE000_0304**


## 2.6 Accessing NVIC Registers by IRQn

Each 32-bit register covers 32 IRQns (Lctr 8 §8.6.2):

    Register index = IRQn / 32    (equivalently: IRQn >> 5)
    Bit position   = IRQn % 32    (equivalently: IRQn & 0x1F)

> **HW4 P6 example:** IRQn = 69, clearing pending bit:
> → Register: 69 / 32 = **ICPR[2]**
> → Bit: 69 % 32 = **bit 5**


## 2.7 Priority and Preemption

**Core rule** (Lctr 9 §9.3.1): smaller number = higher priority

**IP register layout** (Lctr 9 §9.3.3):

    IP byte: [ PPN (n bits) | SPN (m bits) | zeros (8−n−m bits) ]

**Priority number** (Lctr 9 §9.3.5):

    PN = (PPN << m) + SPN       (m = number of sub-priority bits)

**What NVIC_SetPriority stores:**

    NVIC->IP[IRQn] = PN << (8 − total_implemented_bits)

**Decomposing a PN** (given n preemption bits, m sub-priority bits):

    PPN = PN >> m
    SPN = PN & ((1 << m) − 1)

**Preemption rules:**
- IRQ_A can preempt IRQ_B only if PPN_A < PPN_B (strictly less)
- Same PPN → cannot preempt each other
- Same PPN and SPN → lower IRQn number goes first

**Finding PN range:**
- To preempt target with PPN = T: need PPN < T → PN from 0 to ((T−1) << m) + max_SPN
- To NOT preempt: need PPN ≥ T → PN from (T << m) to max_PN

> **HW4 P7 example:** 4 implemented bits, 2 preempt bits, 2 sub-priority bits.
> → IRQn1: PN=12=0b1100 → PPN=3, SPN=0
> → IRQn2: PN=7=0b0111 → PPN=1, SPN=3
> → IRQn3: PN=3=0b0011 → PPN=0, SPN=3
>
> IP[IRQn2] = 7 << 4 = **0b0111_0000**
> Can IRQn1 preempt IRQn2? PPN 3 > 1 → **No**
> Can IRQn3 preempt IRQn2? PPN 0 < 1 → **Yes**
> PN range to preempt IRQn2: PPN must be 0 → **PN 0–3**
> PN range to NOT preempt: PPN ≥ 1 → **PN 4–15**


## 2.8 EXTICR Configuration (Lctr 9 §9.4.2)

**EXTICR register layout:** four 4-bit fields per register

    EXTICR1: bits[15:12]=EXTI3, bits[11:8]=EXTI2, bits[7:4]=EXTI1, bits[3:0]=EXTI0

**Port selection codes:**

    0000=PA, 0001=PB, 0010=PC, 0011=PD, 0100=PE, 0101=PF, 0110=PG

**Template** (for EXTIx, field at bit position S = x×4):

    SYSCFG->EXTICRn &= ~(0xFU << S);        // clear the 4-bit field
    SYSCFG->EXTICRn |=  (PORT_CODE << S);    // set port selection

> **HW4 P8 example:** Configure PC3 for EXTI3 in EXTICR1:
> → EXTI3 field is bits 15:12, so shift = 12
> → MASK_FOR_EXTI3 = 0xFU << 12 = **0xF000**
> → VALUE_FOR_EXTI3_PC = 0x2U << 12 = **0x2000** (PC = 0010)

---

# Part 3: Real Numbers — Floating & Fixed Point (HW5, Lctr 12–13)

## 3.1 IEEE 754 Single Precision (Lctr 12 §12.2.1)

**Format:** 32 bits total

    [1 bit Sign | 8 bits Exponent (E) | 23 bits Fraction (F)]

**Normal number formula:**

    f = (−1)^S × (1 + F_R) × 2^(E − 127)

    where F_R = F × 2^(−23)

**Decoding steps** (hex → real number):
1. Convert hex to 32-bit binary
2. Split into S (bit 31), E (bits 30:23), F (bits 22:0)
3. Compute F_R = F × 2^(−23)
4. Compute f = (−1)^S × (1 + F_R) × 2^(E − 127)

**Special values:**
- E=0, F=0 → ±0
- E=255, F=0 → ±∞
- E=255, F>0 → NaN
- E=0, F>0 → subnormal: f = (−1)^S × F_R × 2^(−126)

**Key detail:** the "1 +" in normal representation is implicit (free bit, not stored)


## 3.2 Unsigned Fixed-Point (UQm.n) (Lctr 13 §13.3.1)

**Total bits = m + n** (no sign bit)

**Decoding** (hex → real):
1. Read the encoded data as unsigned integer I_A
2. Scale: f_A = I_A × 2^(−n)

**Encoding** (real → hex):
1. Multiply: I = f × 2^n
2. Round to nearest integer
3. Convert to hex

> **HW5 P1 example:** Encode 2.75 in UQ3.5:
> → I = 2.75 × 2^5 = 2.75 × 32 = 88 = 0x58


## 3.3 Signed Fixed-Point (Qm.n) (Lctr 13 §13.3.2)

**Total bits N = 1 + m + n** (1 sign bit + m integer bits + n fraction bits)

**Decoding** (hex → real, integer TC approach):
1. Read encoded data as unsigned integer U_A
2. Check MSB:
   - If MSB = 0: I_A = U_A (positive)
   - If MSB = 1: I_A = U_A − 2^N (negative, two's complement)
3. Scale: f_A = I_A × 2^(−n)

**Encoding** (real → hex):
1. Multiply: I = f × 2^n
2. Round to nearest integer
3. If I ≥ 0: convert directly to hex
4. If I < 0: compute two's complement as I + 2^N, then convert to hex

> **HW5 P2 example:** Decode Q3.4 code 0xAA:
> → N = 1+3+4 = 8 bits. U_A = 0xAA = 170
> → MSB = 1 → I_A = 170 − 256 = −86
> → f = −86 × 2^(−4) = −86/16 = **−5.375**

> **HW5 P3 example:** Decode Q2.5 code 0b1001_1001:
> → N = 1+2+5 = 8 bits. U_A = 0x99 = 153
> → MSB = 1 → I_A = 153 − 256 = −103
> → f = −103 × 2^(−5) = −103/32 = **−3.21875**

> **HW5 P4c example:** Encode f = −2.25 in Q3.4:
> → I = −2.25 × 2^4 = −36
> → Negative, so TC: −36 + 2^8 = −36 + 256 = 220 = 0xDC


## 3.4 Q15 and Q31 Specifics (Lctr 13 §13.4.3)

- Q15 = Q0.15 → 16-bit signed, range [−1.0, +1.0)
- Q31 = Q0.31 → 32-bit signed, range [−1.0, +1.0)
- −1.0 encodes as 0x8000 (Q15) or 0x8000_0000 (Q31)
- +1.0 cannot be represented; max is 0x7FFF / 0x7FFF_FFFF
- (−1.0) × (−1.0) overflows back to −1.0 — workaround: clamp to 0x8001


## 3.5 Fixed-Point Arithmetic (Lctr 13 §13.4)

**Addition / Subtraction:**
- Operate directly on the encoded integers: I_C = I_A ± I_B
- The Q format must match (same n)

**Multiplication** (Lctr 13 §13.4.2):
1. Multiply encoded integers into a WIDER type: I_T = I_A × I_B
2. Right-shift by n: I_C = I_T >> n
3. Truncate/cast back to original width

**Why the shift?** Each operand is scaled by 2^n, so the product is scaled by 2^(2n). Shifting removes one factor of 2^n.

> **HW5 P5 example:** Q15 multiply-accumulate: f_A = 0.5×0.25 + 0.125×0.0625
>
> **Step 1 — Encode:**
> I₁ = 0.5 × 2^15 = 16384 = 0x4000
> I₂ = 0.25 × 2^15 = 8192 = 0x2000
> I₃ = 0.125 × 2^15 = 4096 = 0x1000
> I₄ = 0.0625 × 2^15 = 2048 = 0x0800
>
> **Step 2 — Multiply (16-bit × 16-bit → 32-bit, then >> 15):**
> I_T1 = 16384 × 8192 = 134,217,728 → I_P1 = 134217728 >> 15 = 4096 = 0x1000
> I_T2 = 4096 × 2048 = 8,388,608 → I_P2 = 8388608 >> 15 = 256 = 0x0100
>
> **Step 3 — Add:**
> I_A = 4096 + 256 = 4352 = 0x1100
>
> **Step 4 — Decode:**
> f_A = 4352 × 2^(−15) = 4352/32768 = **0.1328125**
> (Exact: 0.5×0.25 + 0.125×0.0625 = 0.125 + 0.0078125 = 0.1328125 ✓)

---

# Quick Reference

| Concept | Formula / Rule |
|---------|---------------|
| GPIO register address | Bus_base + Port_offset + Reg_offset |
| Set bit N | `Reg \|= (1U << N)` |
| Clear bit N | `Reg &= ~(1U << N)` |
| Toggle bit N | `Reg ^= (1U << N)` |
| Assign field | Clear with `&= ~mask`, then set with `\|= value` |
| PSR → IRQn | IRQn = exception_number − 16 |
| NVIC register index | IRQn / 32 |
| NVIC bit position | IRQn % 32 |
| Priority number | PN = (PPN << m) + SPN |
| IP register value | IP = PN << (8 − implemented_bits) |
| Can A preempt B? | Only if PPN_A < PPN_B |
| UQm.n decode | f = I × 2^(−n) |
| UQm.n encode | I = round(f × 2^n) |
| Qm.n decode | I = U − MSB×2^N, then f = I × 2^(−n) |
| Qm.n encode | I = round(f × 2^n); if neg: I + 2^N |
| Fixed-pt multiply | I_C = (I_A × I_B) >> n |
| IEEE 754 decode | f = (−1)^S × (1 + F×2^(−23)) × 2^(E−127) |