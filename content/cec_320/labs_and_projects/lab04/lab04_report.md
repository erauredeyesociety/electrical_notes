# Lab 04 Report: Logic Analyzer Based on Direct GPIO Register Access

**Course:** CEC 320 / MP-DE5D
**Lab Start Date:** 2026-02-26
**Report Date:** 2026-03-04

---

## Introduction

This lab implements a 3-channel logic analyzer (LA) on the STM32G431KB Nucleo-32 board using direct GPIO register access. The LA samples digital signals from three sources: CH1 reads PA0 via the Input Data Register (IDR), while CH2 (PA10/LED1) and CH3 (PB8/LED4) are read from their respective Output Data Registers (ODR). The target system is emulated on the same board by toggling two LEDs every 2 seconds via a SysTick callback. Each sample packs three 1-bit channel states into a single `uint8_t` using bitwise operations, and results are printed over UART to a PuTTY terminal.

---

## Narrative

### Project Setup

The project was created based on the reference project `de2f_direct_gpio_reg_access`, using CubeMX "Save As" to create a new G431n32 project. The source files from `de5d_logic_analyzer_src.zip` were placed in the `src/` folder, and library files (`mp_supported_mcu.h`, `mp_uart_redirect.c/.h`) were copied from the `cc1s_uart_redirect` project since the reference zip did not include a `lib/` folder.

**CubeMX naming issue:** During the "Save As" step, the project was accidentally saved with the reference project name (`de2f_direct_gpio_reg_access_g431n32`) instead of the intended name (`de5d_logic_analyzer_g431n32`). This is a cosmetic issue only -- the project builds and runs correctly regardless of the internal CubeMX project name. However, it means the generated folder and some internal references use the old name. This differs from creating a fresh CubeMX project where the name would be set correctly from the start.

### Programming Tasks

Three functions were implemented in `de5d_logic_analyzer_fns.c`:

1. **`mp_init_set_LED1_reset_LED4()`** (20 pts): Uses BSRR register to set PA10 (LED1 ON) via the lower 16-bit set field, and reset PB8 (LED4 OFF) via the upper 16-bit reset field.

2. **`mp_read_logic_samples()`** (40 pts): Loops through 50 samples, reading each channel from the appropriate GPIO register (IDR for input PA0, ODR for outputs PA10 and PB8), packing 3 bits into each `uint8_t` element of `logic_samples[]`, with a 100ms delay between samples.

3. **`mp_print_logic_samples()`** (20 pts): Iterates through channels and samples, extracting each bit via `(logic_samples[j] >> ch) & 1` and printing as '0' or '1'.

### Fnc6 and Hardware Testing

The "Fnc6" function is activated by physically bridging Pins 12 (A0/PA0) and 13 (AREF/3.3V) on the right-side (analog) header of the Nucleo-32 board. This pulls PA0 high, causing CH1 to read all 1s. Without the bridge, PA0 reads low due to its pull-down resistor configuration.

The game controller board was not available, so a wire was used to bridge pins 12 and 13 directly on the Nucleo-32 header. Initial confusion arose because "Fnc6" was mistaken for the F6 keyboard key -- it is actually a physical hardware connection, not a keyboard shortcut.

---

## Code Snippets and Screenshots

### Artifact 1: PuTTY Output Without Fnc6

Screenshot showing CH1 as all 0s (PA0 pulled low), with CH2 and CH3 alternating in opposite patterns due to LED toggling.

**File:** [a1.png](./a1.png)

### Artifact 2: PuTTY Output With Fnc6 (Pin Bridge)

Screenshot showing CH1 as all 1s (PA0 bridged to 3.3V AREF pin using a wire across pins 12 and 13 on the analog connector), with CH2 and CH3 showing the same alternating pattern.

**File:** [a2.png](./a2.png)

### Artifact 3: Description of uint8_t Sample Packing

Each sample captures 3 channels packed into one `uint8_t` using bitwise operations:

- **Bit 0 -- CH1 (PA0):** Read from `GPIOA->IDR` (Input Data Register). Extracted via `(GPIOA->IDR >> 0) & 1`.
- **Bit 1 -- CH2 (PA10):** Read from `GPIOA->ODR` (Output Data Register). Extracted via `(GPIOA->ODR >> 10) & 1`.
- **Bit 2 -- CH3 (PB8):** Read from `GPIOB->ODR`. Extracted via `(GPIOB->ODR >> 8) & 1`.
- **Packing:** `logic_samples[i] = (bit2 << 2) | (bit1 << 1) | bit0`

Only bits [2:0] are used; bits [7:3] remain 0. During printing, each channel is unpacked: `(logic_samples[j] >> ch) & 1`.

### Code: Modified `de5d_logic_analyzer_fns.c`

**File:** [c1.c](./c1.c)

---

## Discussions and Results

The logic analyzer successfully captured and displayed 3-channel data:

- **Without Fnc6:** CH1 showed all 0s (PA0 in high-impedance with pull-down reads low), while CH2 and CH3 showed complementary toggling patterns with a 2-second period, confirming the SysTick callback toggles LED1 and LED4 correctly.

- **With Fnc6:** CH1 showed all 1s (PA0 pulled to 3.3V via AREF bridge), confirming the input reads high when externally driven. CH2 and CH3 maintained the same toggling behavior.

Key observations:
- The ODR is both writable and readable, allowing it to serve as both an output driver and a logic analyzer input source for emulated signals.
- The BSRR register provides atomic set/reset capability without a read-modify-write cycle, unlike direct ODR manipulation.
- The starting phase of CH2/CH3 varies between runs because there is no synchronization between the toggle timer and the sampling start.
