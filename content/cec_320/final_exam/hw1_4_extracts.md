# HW1-HW4 Condensed Extracts (CEC 320)

## HW1: UART, ARM Pipeline, Number Expression

### P1 (10pt) UART data rate
Setup: 115200 bps, 1 start + 8 data + 1 parity + 1 stop = 11 bits/frame.
Solution: 115200 / 11 = **10472.7 Bytes/s** (1 byte payload per frame).
Trap: include start/parity/stop bits in frame total, but only data bits count as payload.

### P2 (10pt) Parity bit
Data: 0b1101_1100 has 5 ones (odd count).
Even parity -> bit = **1** (makes total even). Odd parity -> bit = **0**.
Key: parity bit makes the total count of 1's match the chosen scheme.

### P3 (20pt) Pipeline loop throughput
Setup: 3-cycle pipeline, 5 task instr + 1 branch, branch flushes pipeline.
- Single loop: 6 instr -> 3 + (6-1) = 8 cycles -> **6/8 = 0.75 instr/cycle**.
- 5 instr unrolled 4x + 1 branch = 21 instr -> 3 + 20 = 23 cycles -> **21/23 = 0.913**.
Key: pipeline fill cost = (depth - 1) extra cycles after first instr; loop unrolling amortizes branch flush.

### P4 (20pt) 3-stage pipeline general
n instr take **n + 2** cycles. 10 instr -> 12 cycles -> 0.833. As n -> infinity, throughput -> 1.
Formula: cycles = n + (depth - 1).

### P5/P6 (15+15) Binary conversions and shifts
- 28 = 0b1_1100 (5b) = 0b0001_1100 (8b); 14 = 0b0_1110 = 0b0000_1110.
- 28 = 14 << 1 (left shift by 1 = multiply by 2).
- a = 0b1_1000 = 24, b = 0b0_0110 = 6 -> **b = a >> 2** (right shift by 2 = divide by 4).

---

## HW2: Data Repr, Memory, Pointers, Unity

### P1/P2 (10+10) 5-bit Two's Complement
Cardinality 2^5 = 32. Encode: value + 32 (if negative).
- -8 -> -8 + 32 = 24 = 0b11000; -12 -> 20 = 0b10100.
- Decode: if MSB=1, subtract 32. 0b11010 = 26 - 32 = **-6**; 0b00110 = **6**.

### P3 (10pt) Little-endian read
Memory @0x2000_0000: 0x01,02,03,04,05,06,07,08.
- uint16_t @0x2000_0002 reads bytes {3,4} -> LE = **0x0403**.
- uint32_t @0x2000_0004 reads {5,6,7,8} -> LE = **0x0807_0605**.
Trap: LE = high-address byte becomes MSB.

### P4 (10pt) 12-bit register range
Unsigned: [0, 2^12 - 1] = **[0, 4095]**. Signed (TC): [-2^11, 2^11 - 1] = **[-2048, 2047]**.

### P5 (10pt) Literal types on Cortex-M
- `1U` -> `uint32_t`, 32 bits. `1L` -> `int32_t`, 32 bits (long is 32-bit on these MCUs).

### P6 (10pt) Union memory aliasing
union { uint8_t arr08[8]; uint32_t arr32[2]; }. arr32[0]=0x12345678 (LE).
- arr08[0..3] = {0x78, 0x56, 0x34, 0x12} -> **arr08[2] = 0x34**.
- After arr08[0] = 0xAB -> **arr32[0] = 0x123456AB**.
Key: union shares memory; LE places LSB at lowest address.

### P7 (10pt) Pre/post increment in expressions
```c
int arr[4], base1=0, base2=0;
arr[0] = ++base1;     // arr[0]=1, base1=1
arr[1] = base2++;     // arr[1]=0, base2=1
arr[2] = ++base1+base2; // base1=2, arr[2]=2+1=3
arr[3] = base1+base2++; // arr[3]=2+1=3, base2=2
```
Trap: prefix ++ uses NEW value; postfix uses OLD value then increments.

### P8 (10pt) Pointer increment patterns
```c
int32_t arr[4]={0}, *ptr=arr;
*ptr++ = 10;   // arr[0]=10, then ptr->arr[1]
*++ptr = 20;   // ptr->arr[2] first, then arr[2]=20
*ptr++ = 30;   // arr[2]=30, then ptr->arr[3]
```
Result: arr = {10, 0, 30, 0}.

### P9 (10pt) Pointer arithmetic vs void* diff
`(void*)(ptr32+1) - (void*)ptr32` = **4** (sizeof(int32_t)).
`(void*)(ptr16+3) - (void*)ptr16` = **6** (3 * 2 bytes).
Key: pointer math scales by element size; cast to void* gives byte offset.

### P10 (10pt) Pointer cast + offset
arr32[4]={0x1122,0x3344,0x5566,0x7788} (LE bytes: 22,11,00,00,44,33,...).
- `*((uint8_t*)ptr32+1)` = byte 1 of arr32[0] = **0x11**.
- `(uint8_t)*(ptr16+2)` = ptr16+2 skips 4 bytes, reads uint16 at byte 4 = 0x3344, cast to u8 = **0x44**.

### P11 (10pt) Unity assertion macros
- uint16: `TEST_ASSERT_EQUAL_UINT16(expected, actual)`
- int32: `TEST_ASSERT_EQUAL_INT32(expected, actual)`
- uint32 array, 3 elem: `TEST_ASSERT_EQUAL_UINT32_ARRAY(expected, actual, 3)`

### P12 (20pt) Pointer cast eval (LE, mem 0x10..17 = 01,23,45,67,89,AB,CD,EF)
int *ptr32 = 0x2000_0010.
- `*ptr32` = LE 4 bytes -> **0x67452301**.
- `*(int16_t*)ptr32` = LE 2 bytes -> **0x2301**.
- `(int8_t)*ptr32` = low byte of 0x67452301 = **0x01**.
- `(int16_t)*(int8_t*)(ptr32+1)`: ptr32+1 advances 4 bytes (sizeof int) -> 0x14, byte=0x89, signed -> -119 -> int16 = **0xFF89**.
Trap: `ptr32+1` uses int* arithmetic (4 bytes), NOT 1 byte.

---

## HW3: GPIO Modes, Bitwise Operations

### P1 (20pt) GPIO mode selection
1. Input, HiZ as 1 -> **Pull-up** (tie up to Vcc).
2. Input, HiZ as 0 -> **Pull-down**.
3. Output drawing current from high-V load -> **Open-drain** (push-pull works but OD better).
4. LED on when out=0 (LED to Vcc) -> **Open-drain**.
5. LED on when out=1 (LED to GND) -> **Push-pull**.
Rule: pull-up/down only for input; open-drain when sinking; push-pull when sourcing.

### P2 (20pt) GPIO addresses
- AHB2: GPIOC base = **0x4800_0800**, IDR offset 0x10 -> **0x4800_0810**.
- AHB1: GPIOC = **0x4002_0800**, ODR offset 0x14 -> **0x4002_0814**.
Memorize: PERIPH_BASE + AHB offset + 0x0800 (per port). IDR=0x10, ODR=0x14, BSRR=0x18, OTYPER=0x04, MODER=0x00.

### P3/P4 (10+10) Shift clearing
A=0b1010_1011.
- `(A>>2)<<2` = **0b1010_1000** (clears low 2 bits).
- `(A<<2)>>2` = **0b0010_1011** (clears high 2 bits, unsigned -> shift in 0).

### P5 (10pt) Toggle mask
Toggle Pin5 + Pin7 -> bit5 + bit7 set: 0b1010_0000 = **0x00A0**.

### P6 (10pt) Set/clear single bit
A=0b1010_1011, mask 4U=0b0000_0100.
- `A | 4U` = 0b1010_1111 (sets bit 2).
- `A & ~4U` = 0b1010_1011 (clears bit 2; unchanged since already 0).

### P7 (10pt) OTYPER manipulation
- 0x0000_1234 | (1<<3) = **0x0000_123C** (set bit 3).
- Push-pull pin 4 = clear bit 4: `GPIOB->OTYPER &= ~(1U << 4);`

### P8 (30pt) 4-bit field manipulation (digit H1 = bits 4-7)
Preferred forms:
- (a) zero H1: `A &= ~(15u << 4);`
- (b) set H1 to 0xF: `A |= 15u << 4;`
- (c) write 6: `A &= ~(15u << 4); A |= 6u << 4;`
- (d) write 9: `A &= ~(15u << 4); A |= 9u << 4;`
- (e) toggle H1 (15-H1): `A ^= 15u << 4;` (XOR with 1's = bit flip)
- (f) shift right by digit: `A >>= 4;`
Pattern: clear field with `&= ~(mask<<pos)`, write with `|= (val<<pos)`. Mask N bits = `(1U<<N)-1`.

### P9 (15pt) Wire-AND with open-drain
Open-drain: only sinks low or floats; needs external pull-up. Multiple OD outputs share line: any low pulls all low (wired-AND). Connecting push-pull as wire-AND -> short between Vcc and GND -> bus contention/damage.

---

## HW4: NVIC, Interrupts, EXTI

### P1 (25pt) Pin state check decomposition
`bool s = ((GPIOA->IDR & GPIO_PIN_1) == GPIO_PIN_1);`
1. GPIO_PIN_1 = 1<<1 = **2** (0x0002).
2. Pressed (bit1=1): IDR & 2 = **2**.
3. (2 == 2) -> **1** (true).
4. Released (bit1=0): IDR & 2 = **0**.
5. (0 == 2) -> **0**.

### P2 (15pt) ISR total cycles
Stacking 8 reg = 8 cyc, 10 ISR instr on 3-stage pipe = 10 cyc (pipe full), unstack = 8 cyc.
Total = 8 + 10 + 8 = **26 cycles**. (ISR fetch overlaps with stacking.)

### P3 (5pt) IRQn from PSR
PSR exception number = 16 + IRQn. 22 - 16 = **IRQn = 6** (EXTI0_IRQn).

### P4 (10pt) NVIC / SysTick base
SCS_BASE = 0xE000E000. NVIC = SCS + 0x100 = **0xE000_E100**. SysTick = SCS + 0x010 = **0xE000_E010**.

### P5 (10pt) NVIC field addresses (struct @0xE000_0000)
Layout: ISER[8] @0x000, ICER[8] @0x080, ISPR @0x100, ICPR @0x180, IABR @0x200, IP[240] @0x300.
- ICER[4] (uint32, idx 4) -> 0x080 + 16 = 0x090 -> **0xE000_E090** (instructor uses NVIC base).
- IP[4] (uint8, idx 4) -> 0x300 + 4 = **0xE000_E304**.

### P6 (10pt) ICPR for IRQn = 69
Index = IRQn / 32 = **ICPR[2]**. Bit = IRQn % 32 = **bit 5**. Same logic for ISER/ICER/ISPR/ICPR.

### P7 (35pt) Priority + preemption (4 IP bits, 2 PPN bits, 2 SPN bits)
PN = (PPN << 2) + SPN, range 0-15. Stored in IP[7:4].
NVIC_SetPriority(IRQn1,12): PN=12 -> PPN=3,SPN=0.
NVIC_SetPriority(IRQn2,7): PN=7 -> PPN=1,SPN=3.
NVIC_SetPriority(IRQn3,3): PN=3 -> PPN=0,SPN=3.
1. IP[IRQn2] = 7 in upper nibble = **0b0111_0000 = 0x70**.
2. IRQn1 preempt IRQn2? PPN1=3, PPN2=1; need PPN1 < PPN2. **No** (3 > 1).
3. IRQn3 preempt IRQn2? PPN3=0 < PPN2=1. **Yes**.
4. To preempt IRQn2: PPN4 < 1 -> PPN4=0, SPN=0..3 -> PN range **0..3**.
5. Cannot preempt: PPN4 >= 1 -> PN range **4..15**.
Key: preemption requires strictly smaller PPN (sub-priority breaks ties only when not preempting).

### P8 (20pt) EXTICR3 mask + value for PC3
Each EXTICR controls 4 lines, 4 bits each. EXTI3 occupies bits 12-15 of its EXTICR. Port C = 0b0010.
- MASK_FOR_EXTI3 = **0xF000** (clear bits 12-15).
- VALUE_FOR_EXTI3_PC = 0b0010 << 12 = **0x2000**.
Pattern: `EXTICR &= ~MASK; EXTICR |= VALUE;` (read-modify-write).
