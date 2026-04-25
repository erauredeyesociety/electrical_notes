# CEC 320 Final Exam - Early Lectures Extract (Part 2)

Compact notes from Lectures 2-9 and 13. Companion to Part 1 (Lectures 14-27).

---

## Lctr 2: UART (Universal Asynchronous Receiver/Transmitter)

- UART = simplified USART without sync clock; uses 2 wires (TX, RX) + GND. USART uses 3 wires (adds CLK).
- Idle line is HIGH; START bit is LOW (logic 0); STOP bit is HIGH (logic 1). Receiver triggers on the 1->0 edge of START.
- Frame layout: `START | D0 D1 ... Dn | [Parity] | STOP(1 or 2)`. Raw data 6/7/8 bits, LSB-first by default.
- Both ends must agree on baud rate, frame size, parity, stop bits before communications.
- Baud rate = bits/sec (in digital comms). Includes start/stop/parity overhead.
- 8N1 = 8 data, no parity, 1 stop -> 10 bits per byte transmitted.
  - Throughput example: 9600 bps with 8N1 -> 9600/10 = **960 bytes/sec**.
- Parity: even = make total #1s even; odd = make total #1s odd. Detects 1-bit errors only.
  - Even-parity example: 0b0111_1110 has six 1s (even) -> parity bit = 0.
- Modern UART hardware oversamples (e.g., 16x) at the receiver to reject noise.
- STM32 default project params (cc1s_uart_redirect): 115200 bps, 8 bits, no parity, 1 stop, 16x oversampling.
- HAL: `HAL_UART_Transmit(&huart, *pData, Size, Timeout)`, `HAL_UART_Receive(...)`. `huart2` is a pointer to the handle struct.
- For `printf`/`scanf` over UART, redirect via `__io_putchar` / `__io_getchar` calling HAL functions. Use `SET_STDIN_TO_NO_BUFFER` macro before `scanf`.

---

## Lctr 3: MCU Architecture, Pipeline, Memory, Number Expression

### Architecture
- Cortex-M0/M0+ uses **Von-Neumann** (one bus for instr + data). Cortex-M3/M4/M7 uses **Harvard** (separate instr/data buses).
- Cortex-M is **32-bit**: 32-bit registers, 32-bit ALU (32x32->64 bit MUL supported), 32-bit address bus.
- Registers: R0-R12 general purpose (R0-R7 "low", R8-R12 "high"), R13=SP (MSP/PSP), R14=LR, R15=PC. Special: xPSR, BASEPRI, PRIMASK, FAULTMASK, CONTROL.

### Memory map (32-bit address space = 4 GiB)
| Range | Region |
|---|---|
| `0x0000_0000` - `0x0800_0000` | Code/Flash (instruction memory, 128 MB region) |
| `0x2000_0000` | SRAM (data memory) start |
| `0x4000_0000` - `0x6000_0000` | Peripheral region (512 MB) |
| `0x6000_0000` - `0xA000_0000` | External RAM (1 GB) |
| `0xA000_0000` - `0xE000_0000` | External device (1 GB) |
| `0xE000_0000` - `0xE010_0000` | Cortex-M Internal Peripherals (64 KB) |

- Min storage unit = byte (each byte uniquely addressed). 2 bytes = halfword, 2 halfwords = word (32 bits).
- Aligned word reads (addr % 4 == 0) take same time as byte reads.
- SRAM: stack grows DOWN from high addr; heap grows UP from low addr; data segment at bottom of SRAM.
- Flash stores code; RAM stores data.

### Pipeline (Cortex-M3/4 = 3-stage: Fetch, Decode, Execute)
- 1 instruction takes 3 clock cycles standalone.
- n instructions in the pipeline take **n + (3-1) = n + 2** total clock cycles.
- Throughput = real instructions / total clock cycles. Branches FLUSH the pipeline -> restart cost.
- Loop with K real ops + 1 branch repeated R times: total cycles = R*(K+1) + 2 each iteration if flushed; or K*R + 1 branch + 2 once if unrolled.

### Number expressions (unsigned)
- Decimal: `70`. Binary: `0b1000110`. Octal: `0106`. Hex: `0x46` or `0X46`.
- `1U` = unsigned long (32-bit). Use underscores for readability: `0b0100_0110`.
- Conversion any-base -> decimal: sum d_i * r^i.
- Decimal -> binary by divide-by-2: `b_i = num % 2; num = num / 2;` until num=0.
- Mask of n LSBs: `(1U << n) - 1`.
- Binary <-> octal: group bits by 3 from LSB. Binary <-> hex: group by 4 from LSB.

---

## Lctr 4: Data Representation (Two's Complement, Endianness, C Types)

### Three encodings of signed N-bit integers
| Binary | SnM | OC (1's comp) | TC (2's comp) |
|---|---|---|---|
| 0b0000 | +0 | +0 | 0 |
| 0b0111 | +7 | +7 | +7 |
| 0b1000 | -0 | -7 | **-8** |
| 0b1111 | -7 | -0 | -1 |

- All three: MSB=0 positive, MSB=1 negative (sign bit).
- TC has only ONE zero, so MCU hardware uses TC for signed.
- 4-bit TC range: -8 to +7. N-bit TC range: -2^(N-1) to 2^(N-1) - 1.

### TC encoding
- Binary method: take magnitude in binary -> invert all bits (OC) -> add 1 = TC.
- Decimal method: `TC_N(-alpha) = 2^N - alpha`. E.g., 5-bit TC of -3 = 32 - 3 = 29 = 0b11101.
- **Sign-extension rule: when widening, REPEAT the MSB.** So -3 is 0b1101 (4-bit), 0b11101 (5-bit), 0b111101 (6-bit).

### TC decoding (Approach 4 / direct decimal)
- View bits as unsigned to get U_A. If MSB=1 (negative), value = U_A - 2^N.
- Example: 0b11101 (5-bit) = 29 unsigned, MSB=1 -> 29 - 32 = -3.

### Why TC?
- Single zero -> easier zero check.
- Subtraction = addition with TC of subtrahend: `a - b = a + TC(b)`.
- ADD/SUB/MUL hardware identical for signed and unsigned.

### C data types (always remember widths and ranges)
| Type | N (bits) | Unsigned range | Signed range |
|---|---|---|---|
| char / int8_t | 8 | 0..255 | -128..127 |
| short / int16_t | 16 | 0..65535 | -32768..32767 |
| int / long / int32_t | 32 | 0..2^32-1 | -2^31..2^31-1 (-2,147,483,648 .. 2,147,483,647) |
| long long / int64_t | 64 | 0..2^64-1 | -2^63..2^63-1 |

- Literal suffixes: `432U` = uint32_t, `432L` = int32_t.

### Memory storage / endianness
- 16-bit halfword address = lowest byte address; must be aligned to 2 (addr % 2 == 0).
- 32-bit word address = lowest byte address; aligned to 4.
- **Little Endian: MSB stored at HIGHEST address (LSB at lowest).** ARM default.
- Big Endian: MSB at lowest address.
- Example memory at 0x2000_0000..0x2000_0003 = 0xEF, 0xBE, 0xAD, 0xDE:
  - Little-endian word at 0x2000_0000 = `0xDEADBEEF`.
  - Big-endian word at 0x2000_0000 = `0xEFBEADDE`.
- Word address is the LOWEST address regardless of endianness.

---

## Lctr 5: Pointers and Unit Test

- A pointer is a variable holding the address of another variable.
- Definition: `data_type *ptr_name [= address];`. E.g., `int16_t *p_16_var1 = &v16a;`.
- `&` = address-of; `*` = dereference. `*p_16_var1 = 0xBEEF` writes through pointer.
- Operator precedence: postfix `[]`, `++`, `--` (prec 1, L->R); prefix `++`, `--`, `(type)`, `*`, `&` (prec 2, R->L).
- Array name decays to pointer to first element. `arr[i]` == `*(arr + i)`. Both `*str = 'h'` and `str[0] = 'h'` work.

### Pointer arithmetic auto-scales by sizeof(type)
- `pvar08 + 2` advances address by 2 bytes (int8_t).
- `pvar32 + 2` advances address by 8 bytes (int32_t).
- `void *` is the universal pointer (points to bytes); cannot be dereferenced directly.

### Typecasting
- Cast pointer: `int8_t *p8 = (int8_t *)p_16_var1;` -> p8 sees same address but reads 1 byte.
- Cast dereference: `int8_t v = (int8_t)*p_16_var1;` -> reads 16 bits then truncates.
- For `p_16_var1` -> 0xBEEF: `(int32_t)*p_16_var1` = 0xFFFF_BEEF (sign-extended); `(int8_t)*p_16_var1` = 0xEF.

### Increment/decrement on pointers
- `ch = *src++` == `ch = *(src++)` -> dereference, then increment pointer.
- `ch = (*src)++` -> dereference, then increment the value pointed to.
- `*dst++ = ch` -> write to *dst, then increment dst (used in strcpy).

### Unit testing with Unity
- Assertions: `TEST_ASSERT_TRUE`, `TEST_ASSERT_FALSE`, `TEST_ASSERT_EQUAL_INT[8/16/32/64]`, `TEST_ASSERT_EQUAL_UINT32`, `TEST_ASSERT_EQUAL_INT32_ARRAY(exp, act, n)`.
- Runner: `UNITY_BEGIN(); RUN_TEST(test_fn); ... UNITY_END();`
- Naming convention: `test_<FUT_name>`.

### Memory & qualifiers
- `extern` makes a global available across files; `static` (file-scope) makes it private; `static` (local) persists between calls.
- `volatile` tells compiler value can change unexpectedly (registers, ISR-modified vars).
- RAM layout: high->low = Stack (down) / Heap (up) / Uninitialized data / Initialized data.

---

## Lctr 6: GPIO

### GPIO pin functions
- Digital input (Schmitt trigger threshold), Digital output, Analog (ADC/DAC), Alternate function (UART, timer, etc.).

### Output stage
- **Push-pull**: PMOS (top) + NMOS (bottom). Can SOURCE or SINK current. Default for driving LEDs.
- **Open-drain**: NMOS only (no PMOS). Outputs 0 (sinks) or HiZ (floating). Needs external pull-up. Used for level-shifting, wired-AND logic.

### Input stage
- HiZ (floating) input reads randomly -> use **pull-up** (read 1 when floating) or **pull-down** (read 0 when floating). PUPDR has 2 bits/pin.

### GPIO register map (STM32G4, GPIOA base = 0x4800_0000)
| Offset | Register | Purpose | Bits/pin |
|---|---|---|---|
| 0x00 | MODER | Mode | 2 |
| 0x04 | OTYPER | Output type (PP/OD) | 1 |
| 0x08 | OSPEEDR | Output speed | 2 |
| 0x0C | PUPDR | Pull-up/down | 2 |
| 0x10 | IDR | Input data (read-only) | 1 (low 16 bits) |
| 0x14 | ODR | Output data | 1 (low 16 bits) |
| 0x18 | BSRR | Bit set/reset (write-only) | 1+1 |
| 0x1C | LCKR | Config lock | 1 |
| 0x20 | AFR[2] | Alternate function (low/high) | 4 |
| 0x28 | BRR | Bit reset only | 1 |

### MODER encoding (2 bits per pin)
- `0b00` Input | `0b01` Output | `0b10` Alternate function | `0b11` Analog (reset state)

### PUPDR encoding (2 bits per pin)
- `0b00` No pull | `0b01` Pull-up | `0b10` Pull-down | `0b11` Reserved

### Memory map base addresses
- `FLASH_BASE = 0x0800_0000`, `SRAM1_BASE = 0x2000_0000`, `PERIPH_BASE = 0x4000_0000`.
- `AHB2PERIPH_BASE = PERIPH_BASE + 0x0800_0000` -> 0x4800_0000 = `GPIOA_BASE`. `GPIOB = GPIOA + 0x0400`, `GPIOC = +0x0800`.
- APB = low-speed peripherals (UART). AHB = high-speed (GPIO).
- `GPIO_TypeDef` struct lays out registers in order; `#define GPIOA ((GPIO_TypeDef *)GPIOA_BASE)`.

### HAL functions
- `HAL_GPIO_Init(GPIOx, &init)`, `HAL_GPIO_DeInit`, `HAL_GPIO_ReadPin`, `HAL_GPIO_WritePin`, `HAL_GPIO_TogglePin`.

---

## Lctr 7: Bitwise Operations and Direct GPIO Register Access

### Shift operations
- Left shift `<<`: shift in 0s from the right. Can change sign of signed numbers (disastrous).
- Unsigned right shift `>>`: shift in 0s from left. So `0xABCD >> 4 = 0x0ABC`.
- Signed right shift `>>`: REPEAT the sign bit. So `(int16_t)0xABCD >> 4 = 0xFABC`.

### Bitwise truth table
| a b | AND | OR | XOR | NOT a |
|---|---|---|---|---|
| 0 0 | 0 | 0 | 0 | 1 |
| 0 1 | 0 | 1 | 1 | 1 |
| 1 0 | 0 | 1 | 1 | 0 |
| 1 1 | 1 | 1 | 0 | 0 |

- `a XOR 0 = a` (preserve); `a XOR 1 = NOT a` (toggle).

### Bitwise operators (precedence)
| Prec | Op | Name |
|---|---|---|
| 2 | `~` | NOT |
| 8 | `&` | AND |
| 9 | `^` | XOR |
| 10 | `|` | OR |
| 14 | `&=`, `^=`, `|=` | Compound assign |

- Logical operators `&&`, `||`, `!` work on whole values (booleans), NOT bitwise.

### Bit manipulation patterns (mask M, bit position N)
- Read bit N: `(A & (1U << N)) > 0`.
- Set bit N: `A |= (1U << N);`
- Clear bit N: `A &= ~(1U << N);`
- Toggle bits in mask: `A ^= mask;`
- Assign w-wide field at position s with value v: `mask = ((1U << w)-1) << s; A &= ~mask; A |= mask & (v << s);`

### Direct register access examples
- Set PA10 mode to output: `GPIOA->MODER &= ~(3U << 10*2); GPIOA->MODER |= (1U << 10*2);` (3U=0b11, 1U=0b01).
- Configure PA0 as pull-down: `GPIOA->PUPDR &= ~(3U << 0*2); GPIOA->PUPDR |= (2U << 0*2);` (2U=0b10).
- Read PA0: `bool s = (GPIOA->IDR & (1U << 0)) > 0;`
- Write PA10 high, PA8 low (load-modify-store, ~3 instructions each):
  ```c
  GPIOA->ODR |= (1U << 10);
  GPIOA->ODR &= ~(1U << 8);
  ```
- Toggle PA10 and PA8: `GPIOB->ODR ^= (1U << 10) | (1U << 8);`

### BSRR layout (32 bits, write-only, ATOMIC, single-store)
| Bit | 31..16 | 15..0 |
|---|---|---|
| Field | BR15..BR0 (reset/clear) | BS15..BS0 (set to 1) |

- Set PA10: `GPIOA->BSRR = (1U << 10);`
- Reset PA8: `GPIOA->BSRR = (1U << (8+16));` OR equivalently `GPIOA->BRR = (1U << 8);`
- BSRR avoids load-modify-store; safe against ISR races.

---

## Lctr 8: Exceptions and Interrupts (NVIC)

### Definitions
- **Exception**: condition concerning the ARM core / SW instructions.
- **Interrupt**: expected condition from peripherals.
- Cortex-M supports up to 255 exceptions/interrupts each with unique CMSIS **IRQn**.

### IRQn numbering
- First 15 IRQns are **system exceptions** (negative): NMI=-14, HardFault=-13, MemMgmt=-12, BusFault=-11, UsageFault=-10, SVCall=-5, DebugMon=-4, PendSV=-2, SysTick=-1.
- Peripheral interrupts have non-negative IRQn defined by chip vendor: e.g. EXTI0=6, EXTI1=7,..., EXTI4=10, EXTI9_5=23, EXTI15_10=40, USART2=38, TIM2=28.
- **PSR exception number = 16 + IRQn** (PSR holds unsigned exception number in bits 0..8).

### Vector table (NVIC table)
- Defined in `startup_stm32g431kbtx.s` at section `.isr_vector` placed at physical address 0x0000_0000.
- Entry 0 = initial stack pointer (`_estack`), Entry 1 = Reset_Handler, then NMI, HardFault, ..., SysTick_Handler at index 15, peripheral handlers from index 16.
- Each handler is declared `.weak` with default `Default_Handler` so user can override (e.g., `void SysTick_Handler(void)` in stm32g4xx_it.c overrides).

### Interrupt service flow
1. ISR triggers, processor stops main code.
2. **Auto-stacking**: hardware pushes R0-R3, R12, LR, PC, PSR onto stack.
3. PC <- ISR address from vector table; runs in **Handler mode** (uses MSP).
4. ISR returns. **Auto-unstacking**: hardware pops back. Main resumes in Thread mode.

### Two processor modes
- **Thread mode**: normal app code, MSP (or PSP if RTOS).
- **Handler mode**: ISRs, always uses MSP.

### NVIC management functions (CMSIS)
- `NVIC_EnableIRQ(IRQn)`, `NVIC_DisableIRQ(IRQn)`, `NVIC_ClearPendingIRQ(IRQn)`, `NVIC_SetPriority(IRQn, prio)`, `NVIC_SetPriorityGrouping(group)`.

### NVIC registers (defined in core_cm4.h, NVIC_BASE = 0xE000_E100)
| Offset | Reg | Purpose |
|---|---|---|
| 0x000 | ISER[8] | Interrupt Set Enable |
| 0x080 | ICER[8] | Interrupt Clear Enable |
| 0x100 | ISPR[8] | Interrupt Set Pending |
| 0x180 | ICPR[8] | Interrupt Clear Pending |
| 0x200 | IABR[8] | Active Bit Register |
| 0x300 | IP[240] | Priority Registers (1 byte/IRQn) |
| 0xE00 | STIR | Software Trigger |

### Direct ISER access
- `NVIC->ISER[IRQn / 32] = 1U << (IRQn % 32);` or `NVIC->ISER[IRQn >> 5] = 1U << (IRQn & 0x1F);`
- IRQn=38 (USART2): `NVIC->ISER[1] = 1U << (38-32);`

### Callback functions
- HAL provides ISRs (e.g. `SysTick_Handler` calls `HAL_IncTick`); user overrides `__weak` callbacks like `HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)`.
- For UART RX interrupt: `HAL_UART_Receive_IT(&huart2, buf, n);` then implement callback.

---

## Lctr 9: Preemption, EXTI, FSM

### Priority semantics
- ARM uses REVERSED priority: **smaller priority number = HIGHER priority** (more urgent).
- Each IRQn has 8-bit priority register in `NVIC->IP[240]` array, but typically only top n bits (n=4 for STM32) are implemented; lower bits read as 0.

### Preemption priority + sub-priority
- 8-bit IP layout: `[ PPN (n bits) | SPN (m bits) | empty (8-n-m) ]`.
- Total priority number: **`PN = (PPN << m) + SPN`**.
- **Higher PPN-priority can preempt the running ISR of lower PPN-priority.** Same PPN cannot preempt each other.
- For pending interrupts at same PPN: lower SPN serviced first.
- Tied priorities: lower IRQn (lower index in vector table) serviced first.

### Priority grouping (controlled by AIRCR bits [10:8])
| G | n bits PPN | m bits SPN |
|---|---|---|
| 0 | 7 | 1 (mostly all preemption) |
| 3 | 4 | 4 |
| 4 | 3 | 5 |
| 7 | 0 | 8 (no preemption, all sub) |

- STM32 macros: `NVIC_PRIORITYGROUP_4` etc.
- `NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_n);`

### Worked example
- 4 bits implemented, 2 bits PPN (group), 2 bits SPN. Set USART2 PPN=2, SPN=1:
  - `PN = (2 << 2) + 1 = 9`.
  - `NVIC_SetPriority(USART2_IRQn, 9);`
  - Read-back IP value = `9 << (8-4) = 0x90`.
- For EXTI0 to preempt USART2 (PPN<2): PN range 0..7. To NOT preempt: PN range 8..15.

### EXTI (External Interrupt/Event Controller)
- Drives interrupts from GPIO edges WITHOUT polling.
- Per-line registers: RTSR (rising-edge sel), FTSR (falling-edge sel), IMR (interrupt mask), EMR (event mask), PR (pending), SWIER (SW trigger).

### EXTI line -> GPIO port mapping
- Each EXTI line N (0-15) selects ONE port (A,B,C,D,E,F,G,H) via SYSCFG_EXTICR registers.
- 4 EXTICR regs hold 16 lines, 4 bits/line: `EXTICR[N/4]` bits `[(N%4)*4 ... +3]` = port code (000=PA, 001=PB, ...).
- Lines 5-9 share one IRQn (`EXTI9_5_IRQn=23`), 10-15 share another (`EXTI15_10_IRQn=40`).

### EXTI setup steps (for EXTI0 from PA0)
1. Configure PA0 as GPIO input (MODER=00, PUPDR set).
2. Enable SYSCFG clock: `__HAL_RCC_SYSCFG_CLK_ENABLE()`.
3. Select PA0: `SYSCFG->EXTICR[0] &= ~MASK; SYSCFG->EXTICR[0] |= 0x0;` (port A).
4. Enable rising trigger: `EXTI->RTSR1 |= EXTI_RTSR1_RT0;`
5. Unmask: `EXTI->IMR1 |= EXTI_IMR1_IM0;`
6. `NVIC_EnableIRQ(EXTI0_IRQn);`

### Finite State Machine
- A state is a status defining function behavior; transitions on events.
- Implement in C with: `typedef enum { STATE_INI, STATE_A, STATE_B } state_t;` and `static state_t state = STATE_INI;` then `switch(state){ case ...: ... state = ...; break; }`.

---

## Lctr 13: Real Numbers (Floating Point + Fixed Point Intro)

### IEEE 754 floating-point normal form
- `f_N = (-1)^S * (1 + F_R) * 2^(E_B)`
- S = sign bit (1 bit). F_R = fraction in [0, 1). E_B = true exponent (signed via bias B).
- Single precision (4 bytes): 1 sign + 8 exp + 23 frac. Bias B = 127. Min normal exp = 1-127 = -126.
- Double precision (8 bytes): 1 + 11 + 52. Bias = 1023.

### Special values
| Encoding | Value |
|---|---|
| S=0, E=0, F=0 | +0 |
| S=1, E=0, F=0 | -0 |
| S=0, E=2B+1, F=0 | +inf |
| S=1, E=2B+1, F=0 | -inf |
| E=2B+1, F>0 | NaN |
| 0 < E < 2B+1 | Normal f_N |
| E=0, F>0 | Subnormal: `(-1)^S * F_R * 2^-126` |

- Smallest positive normal (single): 2^-126 ~ 1.18e-38.

### Float in C
- `float pi = 3.1415926;` -- type cast `(float)int_var` to convert.
- `lrint(f)` rounds to nearest int (long); `llrint(f)` for 64-bit. Default ARM rounds to nearest, ties to even.

### Fixed-point: UQm.n (unsigned)
- Layout: m integer bits | radix point | n fraction bits. Total bits = m+n.
- Range: [0, 2^m - 2^-n]. Resolution: 2^-n.
- **Decode (integer approach)**: treat all bits as unsigned int I_A. Value f_A = I_A * 2^-n.
- **Encode**: round(f * 2^n) -> binary.
- Example UQ5.3, 0xFF: I_A = 255, f = 255/8 = 31.875.
- Example: encode 3.141593 to UQ4.12 -> 3.141593 * 2^12 = 12867.96 -> round 12868 = 0x3244.

### Fixed-point: Qm.n (signed, total = 1 + m + n bits)
- 1 sign bit + m integer + n fraction. Decode via TC integer interpretation, then scale by 2^-n.
- **Decode (TC integer approach)**: Compute U_A unsigned. If MSB=1, I_A = U_A - 2^N. Then f = I_A * 2^-n.
- Example Q4.3, 0xAD = 0b1010_1101: U_A = 173, MSB=1 -> I_A = 173 - 256 = -83. f = -83 * 2^-3 = -10.375.
- **Encode** -3.1234 to Q5.10: -3.1234 * 2^10 = -3198.36 -> round -3198 -> TC: -3198 + 2^16 = 62338 = 0xF382.

### Q15 and Q31 (CMSIS DSP)
- `q15_t` (int16_t) and `q31_t` (int32_t) in `arm_math.h`.
- Range: [-1.0, +1.0). -1.0 = 0x8000 (Q15) / 0x8000_0000 (Q31). Max = 0x7FFF / 0x7FFF_FFFF (just under +1.0).
- (-1.0) * (-1.0) overflow trap: result wraps to -1.0; mitigation: scale -1.0 to 0x8001.

### Fixed-point arithmetic
- **Add/sub**: same as integer add/sub (operands must share same Qm.n format).
  - `f_C = (I_A + I_B) * 2^-n; I_C = I_A + I_B`.
- **Multiply (Qm.n)**: I_T = I_A * I_B is **2*N bits wide** (e.g., 32x32->64).
  - To stay in same Qm.n: shift right by n bits and cast back: `I_C = (I_T >> n);`
  - Q15 mul: `q15_t r = (q15_t)((((int32_t)x * y) >> 15));`
  - Q31 mul: `q31_t r = (q31_t)(((q63_t)x * y) >> 31);`

### Range vs precision tradeoff
- Float: huge range (~1e-38 to 1e38) with relative precision; SLOW without FPU.
- Fixed: limited range/precision but uses integer ALU (fast). Choose Qm.n based on signal range.

---

**End. Source PDFs in `/home/devel/electrical_notes/content/cec_320/lectures/`.**
