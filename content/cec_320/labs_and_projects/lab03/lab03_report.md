# Lab 03 Report: More CubeIDE Operations

**Course:** CEC 320 / MP-CI5D
**Lab Start Date:** 2026-02-09
**Report Date:** 2026-02-10

---

## Introduction

This lab explores advanced CubeIDE operations including managing multiple microprocessor boards (MPBs), creating multiple build configurations with selective source file inclusion, debugging with Expressions and Memory views, and understanding Little Endian byte ordering. The project targets both an STM32F412 (Renode simulation) and STM32G431 (physical NUCLEO-G431KB board), demonstrating cross-platform embedded development. A key exercise involves identifying and fixing a string copy bug, then using CubeIDE's memory inspection tools to examine how 32-bit integers are stored in memory.

---

## Narrative

Setup involved extracting the `ci5d_more_cubeide` project, generating code from both `.ioc` files in CubeMX, and importing both sub-projects into CubeIDE. A recurring include path issue was encountered — the `.cproject` files contained `../../../../lib` (4 directory levels up) instead of `../../../lib` (3 levels), which was fixed by editing both `.cproject` files directly and deleting the Debug build folders to force a clean rebuild.

The `CubeIDE` preprocessor symbol was added to enable conditional compilation for MCU and toolchain identification. Both boards were run successfully, showing identical output aside from different stack/heap addresses due to different RAM configurations.

For MT4, a second build configuration (`DebugIndex`) was created, using `ci1s_ptr_funs_index.c` instead of `ci1s_ptr_funs.c`. The index-based version contained an intentional bug where `i` was post-incremented twice per loop iteration, causing characters to be skipped and written to every other position. This was identified by stepping through the function with the Expressions view, then fixed by using a single `i++` per iteration.

The memory view exercise demonstrated how the same data (`heap_arr` populated with `stack_var >> i` where `stack_var = 0x12345678`) appears differently depending on column size, illustrating Little Endian byte ordering on ARM Cortex-M processors.

---

## Code Snippets and Screenshots

### Artifact A1: Both MPB Outputs Side by Side

![A1 - Both MPB outputs](./a1.png)

*Figure 1: Renode UART window (F412) and PuTTY (G431) showing identical program output. Both display MCU type, "Built by CubeIDE", stack/heap addresses, heap array values, and "Hello world!". Stack addresses differ due to different RAM sizes (F412: 256KB, G431: 32KB).*

### Artifact A2: Expressions View of `message` During Stepping

![A2 - message in Expressions](./a2.png)

*Figure 2: Expressions view showing the `message` array while stepping through the buggy `mp_strcpy` in `ci1s_ptr_funs_index.c`. The double `i++` bug causes characters to be written to every other position, corrupting the string copy.*

### Artifact A3: Hover Values Before and After mp_strcpy

![A3 - Hover before and after](./a3.png)

*Figure 3: Hover inspection of `message` before and after the `mp_strcpy` call. After the bug fix, the function correctly copies "Hello world!" into the message buffer.*

### Artifact A4: Word-Based Memory View

![A4 - Word-based memory](./a4.png)

*Figure 4: Memory view at `heap_arr` address with Row Size 16, Column Size 4 (word-based). Shows 4 words per row: `12345678`, `01234567`, `00123456`, `00012345`. These are the results of `stack_var >> i` for i = 0, 4, 8, 12 — each right-shift by 4 bits removes one hex digit from the right.*

### Artifact A5: Halfword-Based Memory View

![A5 - Halfword-based memory](./a5.png)

*Figure 5: Same memory with Column Size 2 (halfword-based). The word `0x12345678` appears as halfwords `5678` then `1234`. This is Little Endian ordering — the least significant halfword (`5678`) is stored at the lower memory address, and the most significant halfword (`1234`) at the higher address.*

### Artifact A6: Byte-Based Memory View

![A6 - Byte-based memory](./a6.png)

*Figure 6: Same memory with Column Size 1 (byte-based). The word `0x12345678` appears as bytes `78`, `56`, `34`, `12`. Little Endian stores the least significant byte (`0x78`) at the lowest memory address, progressing to the most significant byte (`0x12`) at the highest address. This is the native byte ordering for all ARM Cortex-M processors.*

### Source Code: Corrected ci1s_ptr_funs_index.c

**File:** [c1.c](./c1.c)

```c
#include "ci1s_ptr_funs.h"

void mp_strcpy(char *dst, char *src) {
    int i = 0;
    char ch = src[i];
    while (ch) {
        dst[i] = ch;
        i++;
        ch = src[i];
    }
    dst[i] = '\0';
}
```

**Bug fix:** The original had `dst[i++] = ch;` and `ch = src[i++];` — two post-increments per iteration. This caused `i` to advance by 2 each loop, skipping every other source character and writing to every other destination position. The fix uses a single `i++` between the write and the next read.

---

## Discussions and Results

**Key Learnings:**

- **Multiple build configurations** allow testing different implementations (pointer-based vs. index-based `mp_strcpy`) without duplicating projects. CubeIDE's "Exclude from Build" feature selectively includes source files per configuration.
- **The Expressions view** is valuable for watching array contents change during step-by-step execution, making bugs like the double-increment immediately visible.
- **Hover inspection** provides a quick way to check variable values without adding print statements or configuring the Expressions view.
- **Little Endian byte ordering** means the least significant byte is stored at the lowest memory address. For `0x12345678`:
  - Word view (Col 4): `12345678` — displayed as the complete 32-bit value
  - Halfword view (Col 2): `5678`, `1234` — lower halfword first
  - Byte view (Col 1): `78`, `56`, `34`, `12` — lowest byte first
- **Cross-platform development:** The same source code runs on both F412 (Renode) and G431 (physical board) with only MCU-specific differences in memory addresses.

**Heap Array Values Explained:**

The heap array is populated with `stack_var >> i` where `stack_var = 0x12345678` and `i` ranges from 0 to 15. The printed values (every 4th element) are:

- `heap_arr[0]` = `0x12345678 >> 0` = `0x12345678`
- `heap_arr[4]` = `0x12345678 >> 4` = `0x01234567`
- `heap_arr[8]` = `0x12345678 >> 8` = `0x00123456`
- `heap_arr[12]` = `0x12345678 >> 12` = `0x00012345`

Each right-shift by 1 divides by 2; shifting by 4 removes one hex digit from the least significant end.
