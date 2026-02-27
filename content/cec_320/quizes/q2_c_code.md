# CEC 320 — C Code Cheatsheet

## Bitwise Operations, Register Access, and Embedded Patterns

---

## 1. Single-Bit Operations

**Set bit N to 1:**

    Reg |= (1U << N);

**Clear bit N to 0:**

    Reg &= ~(1U << N);

**Toggle bit N:**

    Reg ^= (1U << N);

**Read bit N (returns 0 or 1):**

    val = (Reg >> N) & 1U;

**Read bit N (returns 0 or non-zero):**

    val = Reg & (1U << N);

**Test if bit N is set (boolean):**

    if (Reg & (1U << N)) { /* bit is 1 */ }


---

## 2. Multi-Bit Field Operations

**Clear a field of W bits starting at position S:**

    Reg &= ~(MASK << S);

where MASK = (1U << W) − 1. For common widths:
- 1-bit field: MASK = 0x1
- 2-bit field: MASK = 0x3
- 4-bit field (hex digit): MASK = 0xF
- 8-bit field: MASK = 0xFF

**Set a field to value V (two-step clear-then-set):**

    Reg &= ~(MASK << S);       // clear
    Reg |=  (V << S);          // set

**Set a field to all 1s (no clear needed):**

    Reg |= (MASK << S);

**Complement (flip) a field:**

    Reg ^= (MASK << S);


---

## 3. Hex Digit Operations (4-bit nibbles)

Digit Hk occupies bits [4k+3 : 4k]. Shift amount = 4*k.

**Clear digit k to 0:**

    A &= ~(0xFU << (4*k));

**Set digit k to value V:**

    A &= ~(0xFU << (4*k));
    A |=  (V << (4*k));

**Complement digit k:**

    A ^= (0xFU << (4*k));

**Extract digit k (as 0–15):**

    digit = (A >> (4*k)) & 0xF;

**Place a digit at position k in a result:**

    result |= (digit << (4*k));

**Shift entire value right by one digit:**

    A >>= 4;

**Shift entire value left by one digit:**

    A <<= 4;


---

## 4. Digit Rearrangement Patterns

These combine extraction, shifting, and placement to move digits around.

**General approach:**
1. Extract any digits that move to non-obvious positions
2. Shift the bulk if most digits move in the same direction
3. Clear positions that need new values
4. OR in extracted or constant digits

**Example: 0xH3H2H1H0 → 0xH2H1H03**

    A = (A << 4) | 0x3U;

**Example: 0xH3H2H1H0 → 0x7H3H2H1**

    A = (A >> 4) | (0x7U << 12);

**Example: 0xH3H2H1H0 → 0xF_H0_H3_H2**

    uint16_t h0 = A & 0xF;
    A = (A >> 8) | (h0 << 8) | (0xFU << 12);

**Example: extract H0, complement H3, rearrange**

    uint16_t h0 = A & 0xF;
    uint16_t h3c = ((A >> 12) & 0xF) ^ 0xF;   // extract and complement
    A = ((A >> 4) & 0x00FF) | (h3c << 8) | (h0 << 12);


---

## 5. GPIO Register Access

**Toggle pin(s):**

    GPIOA->ODR ^= mask;
    // e.g., toggle Pin1, Pin3, Pin5:
    GPIOA->ODR ^= (1U << 1) | (1U << 3) | (1U << 5);
    // mask = 0x002A

**Set pin(s) high (atomic, no read-modify-write):**

    GPIOx->BSRR = (1U << N);           // sets pin N

**Set pin(s) low (atomic):**

    GPIOx->BSRR = (1U << (N + 16));    // resets pin N

**Read a single pin:**

    bool state = ((GPIOx->IDR & (1U << N)) == (1U << N));

**Set output type to push-pull (clear OTYPER bit):**

    GPIOx->OTYPER &= ~(1U << N);

**Set output type to open-drain (set OTYPER bit):**

    GPIOx->OTYPER |= (1U << N);

**Set MODER for pin N to output (01):**

    GPIOx->MODER &= ~(0x3U << (2*N));    // clear 2-bit field
    GPIOx->MODER |=  (0x1U << (2*N));    // set to 01 (output)

**Set PUPDR for pin N to pull-up (01):**

    GPIOx->PUPDR &= ~(0x3U << (2*N));
    GPIOx->PUPDR |=  (0x1U << (2*N));


---

## 6. NVIC / Interrupt Code

**Enable an interrupt:**

    NVIC_EnableIRQ(IRQn);
    // or direct: NVIC->ISER[IRQn >> 5] = 1U << (IRQn & 0x1F);

**Disable an interrupt:**

    NVIC_DisableIRQ(IRQn);
    // or direct: NVIC->ICER[IRQn >> 5] = 1U << (IRQn & 0x1F);

**Clear pending:**

    NVIC_ClearPendingIRQ(IRQn);
    // or direct: NVIC->ICPR[IRQn >> 5] = 1U << (IRQn & 0x1F);

**Set priority:**

    NVIC_SetPriority(IRQn, priority_number);

**Read priority from IP register:**

    uint8_t pn = NVIC->IP[IRQn] >> (8 - implemented_bits);


---

## 7. EXTICR Configuration

**Configure port P for EXTI line x:**

    // shift = (x % 4) * 4
    // register = EXTICR[x / 4] or EXTICR1..EXTICR4
    SYSCFG->EXTICRn &= ~(0xFU << shift);          // clear
    SYSCFG->EXTICRn |=  (PORT_CODE << shift);      // set

**Port codes:** PA=0x0, PB=0x1, PC=0x2, PD=0x3, PE=0x4, PF=0x5, PG=0x6

**Don't forget to enable SYSCFG clock first:**

    __HAL_RCC_SYSCFG_CLK_ENABLE();


---

## 8. Fixed-Point Encode / Decode in C

**Encode real to Qm.n:**

    int16_t code = (int16_t)lrint(f * (1 << n));
    // lrint rounds to nearest integer

**Decode Qm.n to real:**

    float f = (float)code / (float)(1 << n);
    // or: f = code * powf(2, -n);

**Q15 multiply (two Q15 values → Q15 result):**

    q15_t a = ...;
    q15_t b = ...;
    q31_t temp = (q31_t)a * (q31_t)b;   // 16x16 → 32
    q15_t result = (q15_t)(temp >> 15);  // shift back to Q15

**Q31 multiply:**

    q31_t a = ...;
    q31_t b = ...;
    q63_t temp = (q63_t)a * (q63_t)b;   // 32x32 → 64
    q31_t result = (q31_t)(temp >> 31);  // shift back to Q31

**Q15 multiply-accumulate:**

    q31_t acc = 0;
    acc += (q31_t)a1 * (q31_t)b1;       // accumulate in 32-bit
    acc += (q31_t)a2 * (q31_t)b2;
    q15_t result = (q15_t)(acc >> 15);   // shift once at the end


---

## 9. Common Type Definitions

    #include <stdint.h>
    #include <stdbool.h>

    uint8_t     // unsigned 8-bit  (0 to 255)
    int8_t      // signed 8-bit    (-128 to 127)
    uint16_t    // unsigned 16-bit (0 to 65535)
    int16_t     // signed 16-bit   (-32768 to 32767)
    uint32_t    // unsigned 32-bit
    int32_t     // signed 32-bit

    // DSP types (from arm_math.h)
    q15_t       // int16_t, represents Q0.15
    q31_t       // int32_t, represents Q0.31
    q63_t       // int64_t, for intermediate products


---

## 10. Operator Precedence Gotchas

**Always parenthesize shifts and masks in comparisons:**

    // WRONG — == binds tighter than &
    if (Reg & mask == value)         // parsed as: Reg & (mask == value)

    // CORRECT
    if ((Reg & mask) == value)

**Always use U suffix for unsigned constants in shifts:**

    // GOOD
    (1U << 31)      // unsigned, well-defined

    // DANGEROUS
    (1 << 31)       // signed int, undefined behavior if int is 32-bit

**Cast before shifting for wide results:**

    // 16-bit × 16-bit needs 32-bit result
    int32_t product = (int32_t)a * (int32_t)b;    // cast BEFORE multiply

    // NOT: int32_t product = a * b;  (overflow happens before cast)