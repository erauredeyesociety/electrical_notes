# Nucleo-32 Board Pinout Reference

**Applies to:** STM32 Nucleo-32 boards (Arduino Nano form factor)
**Boards used in CEC 320:** NUCLEO-G431KB (STM32G431KBT6)

> **Important CN3/CN4 Label Swap:** The NUCLEO-G431KB is the **only** Nucleo-32 variant where ST swapped the CN3 and CN4 connector labels compared to other boards (e.g., L432KC, F303K8). The **physical pin positions** are identical across all Nucleo-32 boards — only the connector label names differ. This document uses **physical position** (left/right side) rather than CN3/CN4 labels to avoid confusion.
>
> Sources: [ST Community - G0 vs G4 CN3/CN4 swap](https://community.st.com/t5/stm32-mcus-boards-and-hardware/nucleo-32-g0-vs-g4-cn3-cn4-connector-references/td-p/712273)

---

## Board Orientation

Hold the board with:
- **USB connector at the top**
- **Component side facing you** (you can see the chips and text)
- Two rows of 15 header pins, one on each side

```
        [USB Connector]
        _______________
       |               |
  Left |   Nucleo-32   | Right
  Side |   (top view)  | Side
       |               |
       |_______________|

  Left Side = Digital pins (D0-D12)
  Right Side = Analog pins (A0-A7), power, AREF, D13
```

---

## Right Side — Analog Connector

Pin 1 is at the **top** (nearest USB connector). Pin 15 is at the **bottom** (farthest from USB connector).

> **Convention used in this document:**
>
> - "Top" = closest to USB connector. "Bottom" = farthest from USB connector.
> - "Nth from bottom" counts the bottom-most pin as the **1st from bottom**. Example: "3rd from bottom" = bottom pin is 1st, next up is 2nd, the one above that is 3rd.
> - Same logic applies to "Nth from top", "Nth from left", etc. The edge pin is always counted as 1st.

On G431KB this is labeled **CN4**. On L432KC/F303K8 this is labeled **CN3**.

| Pin | Arduino Name | G431KB GPIO | L432KC GPIO | Notes |
|-----|-------------|-------------|-------------|-------|
| 1   | VIN         | —           | —           | External power input |
| 2   | GND         | —           | —           | Ground |
| 3   | NRST        | NRST        | NRST        | Reset |
| 4   | +5V         | —           | —           | 5V from USB |
| 5   | A7          | PA2         | PA2         | ADC |
| 6   | A6          | PA7         | PA7         | ADC |
| 7   | A5          | PA6         | PA6         | ADC/SCL |
| 8   | A4          | PA5         | PA5         | ADC/SDA |
| 9   | A3          | PA4         | PA4         | ADC |
| 10  | A2          | PA3         | PA3         | ADC |
| 11  | A1          | PA1         | PA1         | ADC |
| **12** | **A0**   | **PA0**     | **PA0**     | **ADC / Fnc6 input** |
| **13** | **AREF** | **VREF+**   | **VREF+**   | **~3.3V reference** |
| 14  | +3V3        | —           | —           | 3.3V regulated |
| 15  | D13/SCK     | PB3         | PB3         | SPI clock / LED |

---

## Left Side — Digital Connector

Pin 1 is at the **top** (nearest USB connector). Pin 15 is at the **bottom**.

On G431KB this is labeled **CN3**. On L432KC/F303K8 this is labeled **CN4**.

| Pin | Arduino Name | G431KB GPIO | L432KC GPIO | Notes |
|-----|-------------|-------------|-------------|-------|
| 1   | D1/TX       | PA9         | PA9         | USART1 TX |
| 2   | D0/RX       | **PA10**    | **PA10**    | **USART1 RX / LED1** |
| 3   | NRST        | NRST        | NRST        | Reset |
| 4   | GND         | —           | —           | Ground |
| 5   | D2          | PA12        | PA12        | GPIO |
| 6   | D3          | PB0         | PB0         | GPIO |
| 7   | D4          | PB7         | PB7         | GPIO |
| 8   | D5          | PB6         | PB6         | GPIO |
| 9   | D6          | PB1         | PB1         | GPIO |
| 10  | D7          | PF0         | PC14        | GPIO (differs!) |
| 11  | D8          | PF1         | PC15        | GPIO (differs!) |
| 12  | D9          | PA8         | PA8         | GPIO |
| 13  | D10         | PA11        | PA11        | GPIO |
| 14  | D11/MOSI    | PB5         | PB5         | SPI MOSI |
| 15  | D12/MISO    | PB4         | PB4         | SPI MISO |

---

## Lab04-Specific: Fnc6 Pin Bridge

The lab04 Fnc6 function connects **PA0** to a high voltage to make CH1 read logic 1.

**Physical pins to bridge:**
- **Right side, Pin 13** (AREF = ~3.3V) — 3rd from bottom (bottom pin=1st, +3V3=2nd, AREF=3rd)
- **Right side, Pin 12** (A0 = PA0) — 4th from bottom (bottom pin=1st, +3V3=2nd, AREF=3rd, A0=4th)

These two pins are **physically adjacent** on the right-side header.

```
  Right side of board (analog connector):
  Pin 1  [VIN]         ← top (near USB)
  Pin 2  [GND]
  Pin 3  [NRST]
  Pin 4  [+5V]
  Pin 5  [A7]
  Pin 6  [A6]
  Pin 7  [A5]
  Pin 8  [A4]
  Pin 9  [A3]
  Pin 10 [A2]
  Pin 11 [A1]
  Pin 12 [A0  = PA0]   ← BRIDGE THESE TWO
  Pin 13 [AREF ≈ 3.3V] ← BRIDGE THESE TWO
  Pin 14 [+3V3]
  Pin 15 [D13/SCK]     ← bottom
```

**How to bridge:** Touch a metal object (paperclip, jumper wire, ballpoint pen tip) across both pins simultaneously. Hold during entire sampling period (~5 seconds).

**What it does:** Connects PA0 (configured as input with pull-down) to the 3.3V analog reference voltage, pulling PA0 high → CH1 reads all 1s.

---

## Key GPIO Locations (Lab04)

| Signal | GPIO | Arduino Name | Connector Side | Pin # | Position from Bottom |
|--------|------|-------------|----------------|-------|---------------------|
| CH1 (Fnc6 input) | PA0  | A0    | Right | 12 | 4th from bottom |
| CH2 (LED1)        | PA10 | D0/RX | Left  | 2  | 14th from bottom (2nd from top) |
| CH3 (LED4)        | PB8  | —     | —     | Not on header | On-board LED only |

Note: PB8 (LED4) is directly connected to the on-board LED and is **not** broken out to the Arduino Nano headers.

---

## Sources

- [STM32G4 Nucleo-32 User Manual (UM2397)](https://www.st.com/resource/en/user_manual/um2397-stm32g4-nucleo32-board-mb1430-stmicroelectronics.pdf)
- [STM32 Nucleo-32 User Manual (UM1956)](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf)
- [Nucleo-L432KC mbed page](https://os.mbed.com/platforms/ST-Nucleo-L432KC/)
- [TinyGo Nucleo-L432KC pin mapping](https://tinygo.org/docs/reference/microcontrollers/machine/nucleo-l432kc/)
- [ST Community: CN3/CN4 connector swap discussion](https://community.st.com/t5/stm32-mcus-boards-and-hardware/nucleo-32-g0-vs-g4-cn3-cn4-connector-references/td-p/712273)
- [ManualsLib: G431KB Nucleo-32 Arduino Connector Pinout](https://www.manualslib.com/manual/1749668/St-Stm32g4-Nucleo-32.html?page=21)
