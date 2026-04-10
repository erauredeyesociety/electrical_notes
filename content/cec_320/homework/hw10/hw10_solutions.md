# HW 10 - Solutions

## Problem 1

### Setup: Memory Map (Individual Bytes)

Since `my_arr` is a `uint8_t` array, each element is 1 byte:

| Address      | Value |
|--------------|-------|
| 0x20000100   | 0x00  |
| 0x20000101   | 0x02  |
| 0x20000102   | 0x04  |
| 0x20000103   | 0x06  |
| 0x20000104   | 0x08  |
| 0x20000105   | 0x0A  |
| 0x20000106   | 0x0C  |
| 0x20000107   | 0x0E  |
| 0x20000108   | 0x10  |
| 0x20000109   | 0x12  |
| 0x2000010A   | 0x14  |
| 0x2000010B   | 0x16  |

**Initial pointer values:**
- `p8a = 0x20000100`
- `p8b = 0x2000010C`

---

### Part 1: Addresses and Values Changed by Right-Side Expressions

We trace each line, focusing on what the **right-hand side** modifies in memory:

**Line 4: `*p8b++ = *(p8a + 2);`**

- Right side: `*(p8a + 2)` = `*(0x20000102)` = `0x04`
- This is a pure read with no modification.
- **No addresses changed by the right side.**
- After line 4: `p8a = 0x20000100`, `p8b = 0x2000010D`

**Line 5: `*p8b++ = ++*(p8a + 4);`**

- Right side: `*(p8a + 4)` = `*(0x20000104)` = `0x08`
- The `++` prefix increments the **value** at that address: `0x08` becomes `0x09`, and the incremented value is written back.
- **Address 0x20000104 changed from 0x08 to 0x09.**
- After line 5: `p8a = 0x20000100`, `p8b = 0x2000010E`

**Line 6: `*p8b++ = ++*p8a++;`**

- Operator precedence: postfix `++` on `p8a` has highest precedence (level 1). The prefix `++` and dereference `*` are both level 2, right-to-left associativity.
- Step 1: `p8a++` returns the old value `0x20000100`, then `p8a` becomes `0x20000101`.
- Step 2: `*p8a++` dereferences the **old** pointer value: `*(0x20000100)` = `0x00`.
- Step 3: `++` prefix increments that value: `0x00` becomes `0x01`, written back to `0x20000100`.
- **Address 0x20000100 changed from 0x00 to 0x01.**
- After line 6: `p8a = 0x20000101`, `p8b = 0x2000010F`

**Line 7: `*p8b++ = *p8a++;`**

- `p8a` is currently `0x20000101`.
- `*p8a++` reads `*(0x20000101)` = `0x02`, then `p8a` becomes `0x20000102`.
- This is a pure read with no modification.
- **No addresses changed by the right side.**
- After line 7: `p8a = 0x20000102`, `p8b = 0x20000110`

**Summary of Part 1:**

| Line | Address Changed | Old Value | New Value |
|------|----------------|-----------|-----------|
| 4    | None           | -         | -         |
| 5    | 0x20000104     | 0x08      | 0x09      |
| 6    | 0x20000100     | 0x00      | 0x01      |
| 7    | None           | -         | -         |

---

### Part 2: Four Bytes at 0x2000010C After Execution

Each line stores a value at `*p8b` before incrementing `p8b`:

| Line | Store Address | Value Stored | Source                              |
|------|-------------|--------------|-------------------------------------|
| 4    | 0x2000010C  | **0x04**     | `*(p8a + 2)` = `*(0x20000102)`      |
| 5    | 0x2000010D  | **0x09**     | `++*(p8a + 4)` = `0x08 + 1`         |
| 6    | 0x2000010E  | **0x01**     | `++*p8a++` = `0x00 + 1`             |
| 7    | 0x2000010F  | **0x02**     | `*p8a++` = `*(0x20000101)`          |

**Answer:**

| Address      | Value  |
|--------------|--------|
| 0x2000010C   | 0x04   |
| 0x2000010D   | 0x09   |
| 0x2000010E   | 0x01   |
| 0x2000010F   | 0x02   |

---

### Part 3: Assembly Implementation

Function prototype: `void my_fn(uint8_t *pa, uint8_t *pb);`

Register mapping per ARM calling convention:
- `r0` = `pa` (initially `p8a = 0x20000100`)
- `r1` = `pb` (initially `p8b = 0x2000010C`)

```asm
    .global my_fn
    .text

my_fn:
    @ Line 4: *p8b++ = *(p8a + 2);
    @ Read byte at (pa + 2), store to *pb, pb++
    ldrb    r2, [r0, #2]        @ r2 = *(p8a + 2)
    strb    r2, [r1], #1        @ *p8b = r2, then p8b++

    @ Line 5: *p8b++ = ++*(p8a + 4);
    @ Read byte at (pa + 4), increment it, write back, store to *pb, pb++
    ldrb    r2, [r0, #4]        @ r2 = *(p8a + 4)
    add     r2, r2, #1          @ r2 = r2 + 1 (prefix increment)
    strb    r2, [r0, #4]        @ write incremented value back to *(p8a + 4)
    strb    r2, [r1], #1        @ *p8b = r2, then p8b++

    @ Line 6: *p8b++ = ++*p8a++;
    @ Read byte at *pa, increment value, write back, store to *pb, pb++; pa++
    ldrb    r2, [r0], #1        @ r2 = *p8a, then p8a++ (r0 increments by 1)
    add     r2, r2, #1          @ r2 = r2 + 1 (prefix increment on value)
    strb    r2, [r0, #-1]       @ write back to original address (r0 - 1)
    strb    r2, [r1], #1        @ *p8b = r2, then p8b++

    @ Line 7: *p8b++ = *p8a++;
    @ Read byte at *pa, store to *pb, both pa++ and pb++
    ldrb    r2, [r0], #1        @ r2 = *p8a, then p8a++
    strb    r2, [r1], #1        @ *p8b = r2, then p8b++

    bx      lr
```

**Line-by-line explanation:**

- **Line 4 (5 pts):** Simple byte load with constant offset (`ldrb r2, [r0, #2]`) followed by post-indexed store (`strb r2, [r1], #1`). The `#2` offset corresponds to `p8a + 2`, and the post-index `#1` on the store implements the `p8b++`.

- **Line 5 (10 pts):** Four instructions needed because we must: (1) load the byte, (2) increment the loaded value, (3) write the incremented value back to the source, and (4) store it at the destination. The `strb r2, [r0, #4]` writes back the incremented value to `*(p8a + 4)`.

- **Line 6 (10 pts):** The trickiest line. The post-index `ldrb r2, [r0], #1` handles both the dereference and the `p8a++` in one instruction. After loading, `r0` has already advanced, so to write back the incremented value, we use `strb r2, [r0, #-1]` to reach the original address.

- **Line 7 (5 pts):** Straightforward post-indexed load and post-indexed store, each with offset `#1` to implement both `p8a++` and `p8b++`.

---

## Problem 2

### Setup: The ipt Array

After the initialization loop `ipt[i] = i << 4`:

| Index | Value (hex) | Index | Value (hex) |
|-------|-------------|-------|-------------|
| 0     | 0x00        | 8     | 0x80        |
| 1     | 0x10        | 9     | 0x90        |
| 2     | 0x20        | 10    | 0xA0        |
| 3     | 0x30        | 11    | 0xB0        |
| 4     | 0x40        | 12    | 0xC0        |
| 5     | 0x50        | 13    | 0xD0        |
| 6     | 0x60        | 14    | 0xE0        |
| 7     | 0x70        | 15    | 0xF0        |

In memory (little-endian), when loaded as 32-bit words:
- Word at `ipt+0`:  bytes `0x00, 0x10, 0x20, 0x30` -> `0x30201000`
- Word at `ipt+4`:  bytes `0x40, 0x50, 0x60, 0x70` -> `0x70605040`
- Word at `ipt+8`:  bytes `0x80, 0x90, 0xA0, 0xB0` -> `0xB0A09080`
- Word at `ipt+12`: bytes `0xC0, 0xD0, 0xE0, 0xF0` -> `0xF0E0D0C0`

When loaded as 16-bit halfwords:
- Halfword at `ipt+0`:  `0x1000`
- Halfword at `ipt+2`:  `0x3020`
- Halfword at `ipt+4`:  `0x5040`
- Halfword at `ipt+6`:  `0x7060`
- Halfword at `ipt+8`:  `0x9080`
- Halfword at `ipt+10`: `0xB0A0`
- Halfword at `ipt+12`: `0xD0C0`
- Halfword at `ipt+14`: `0xF0E0`

---

### Question 2a (8 pts): Task 1 Printout

```asm
task1:
    ldrd    r2, r3, [r0, #8]!    @ Pre-indexed: r0 = r0 + 8, then load
    strd    r2, r3, [r1, #0]     @ Store double word
    bx      lr
```

**Step-by-step:**

1. `ldrd r2, r3, [r0, #8]!` - This is a **pre-indexed** LDRD instruction:
   - First, update `r0`: `r0 = r0 + 8` = address of `ipt + 8`
   - Then load: `r2 = word at [r0]` = word at `ipt+8` = **0xB0A09080**
   - And: `r3 = word at [r0+4]` = word at `ipt+12` = **0xF0E0D0C0**

2. `strd r2, r3, [r1, #0]`:
   - `opt[0] = r2 = 0xB0A09080`
   - `opt[1] = r3 = 0xF0E0D0C0`

**Answer:**
```
Out1 = 0xB0A09080, Out2 = 0xF0E0D0C0
```

---

### Question 2b (14 pts): Task 2 Printout and Register Values

```asm
task2:
    ldrsb   r2, [r0, #4]!     @ Pre-indexed signed byte load
    ldrsb   r3, [r0, #4]!     @ Pre-indexed signed byte load
    strd    r2, r3, [r1, #0]
    bx      lr
```

**Step-by-step:**

1. `ldrsb r2, [r0, #4]!` - **Pre-indexed** signed byte load:
   - First, `r0 = r0 + 4` = address of `ipt + 4`
   - Load signed byte at `[r0]` = byte at `ipt+4` = `0x40` = `0100 0000`
   - Bit 7 = 0, so sign-extend to 32 bits: `r2 = 0x00000040`

2. `ldrsb r3, [r0, #4]!`:
   - First, `r0 = r0 + 4` = address of `ipt + 8`
   - Load signed byte at `[r0]` = byte at `ipt+8` = `0x80` = `1000 0000`
   - Bit 7 = 1, so sign-extend to 32 bits: `r3 = 0xFFFFFF80`

3. `strd r2, r3, [r1, #0]`:
   - `opt[0] = 0x00000040`
   - `opt[1] = 0xFFFFFF80`

**Printout:**
```
Out1 = 0x40, Out2 = 0xFFFFFF80
```

**Register values** (assuming r0 = 0x20001010, r1 = 0x20001040 initially):
- `r0 = 0x20001010 + 4 + 4 = 0x20001018`
- `r1 = 0x20001040` (unchanged, no writeback on the STRD)

---

### Question 2c (14 pts): Task 3 Printout and Register Values

```asm
task3:
    ldrsh   r2, [r0], #10    @ Post-indexed signed halfword load
    ldrsh   r3, [r0], #4     @ Post-indexed signed halfword load
    strd    r2, r3, [r1, #0]
    bx      lr
```

**Step-by-step:**

1. `ldrsh r2, [r0], #10` - **Post-indexed** signed halfword load:
   - First, load signed halfword at `[r0]` = halfword at `ipt+0` = `0x1000`
   - Bit 15 = 0, so sign-extend to 32 bits: `r2 = 0x00001000`
   - Then, `r0 = r0 + 10` = address of `ipt + 10`

2. `ldrsh r3, [r0], #4`:
   - Load signed halfword at `[r0]` = halfword at `ipt+10` = `0xB0A0`
   - Bit 15 = 1, so sign-extend to 32 bits: `r3 = 0xFFFFB0A0`
   - Then, `r0 = r0 + 4` = address of `ipt + 14`

3. `strd r2, r3, [r1, #0]`:
   - `opt[0] = 0x00001000`
   - `opt[1] = 0xFFFFB0A0`

**Printout:**
```
Out1 = 0x1000, Out2 = 0xFFFFB0A0
```

**Register values** (assuming r0 = 0x20001010, r1 = 0x20001040 initially):
- `r0 = 0x20001010 + 10 + 4 = 0x2000101E`
- `r1 = 0x20001040` (unchanged)

---

### Question 2d (14 pts): Task 4 Printout and Register Values

```asm
task4:
    ldrh    r3, [r0, r2, LSL #1]   @ Register-offset unsigned halfword load
    str     r3, [r1, #0]
    add     r2, #1
    ldrh    r3, [r0, r2, LSL #1]
    str     r3, [r1, #4]
    add     r2, #1
    bx      lr
```

Called as `task4(ipt, opt, 1)`, so: `r0 = ipt`, `r1 = opt`, `r2 = 1`.

**Step-by-step:**

1. `ldrh r3, [r0, r2, LSL #1]`:
   - Effective address = `r0 + r2 * 2` = `ipt + 1*2` = `ipt + 2`
   - Load unsigned halfword at `ipt+2` = `0x3020`
   - `r3 = 0x00003020` (zero-extended by LDRH)

2. `str r3, [r1, #0]`: `opt[0] = 0x00003020`

3. `add r2, #1`: `r2 = 2`

4. `ldrh r3, [r0, r2, LSL #1]`:
   - Effective address = `r0 + r2 * 2` = `ipt + 2*2` = `ipt + 4`
   - Load unsigned halfword at `ipt+4` = `0x5040`
   - `r3 = 0x00005040`

5. `str r3, [r1, #4]`: `opt[1] = 0x00005040`

6. `add r2, #1`: `r2 = 3`

**Printout:**
```
Out1 = 0x3020, Out2 = 0x5040
```

**Register values after Task 4:**
- `r2 = 0x00000003`
- `r3 = 0x00005040`

---

### Question 2e (24 pts): Equivalent C Code for Each Task

**Task 1 C equivalent (6 pts):**

```c
// Task 1: ldrd r2, r3, [r0, #8]! / strd r2, r3, [r1, #0]
// Loads 8 bytes from ipt+8 and stores them into opt[0] and opt[1]
int32_t *iptr1 = (int32_t *)ipt;
int32_t *optr1 = (int32_t *)opt;
*optr1 = *(iptr1 + 2);           // opt[0] = word at ipt+8
*(optr1 + 1) = *(iptr1 + 3);     // opt[1] = word at ipt+12
```

Or equivalently using 64-bit pointers:
```c
int64_t *iptr1 = (int64_t *)ipt;
int64_t *optr1 = (int64_t *)opt;
*optr1 = *(iptr1 + 1);           // copies 8 bytes from ipt+8 to opt
```

**Task 2 C equivalent (6 pts):**

```c
// Task 2: ldrsb r2, [r0, #4]! / ldrsb r3, [r0, #4]!
// Loads signed bytes from ipt+4 and ipt+8, sign-extends to 32-bit
int8_t *iptr2 = (int8_t *)ipt;
int32_t *optr2 = (int32_t *)opt;
iptr2 += 4;                       // pre-index: r0 = r0 + 4
*optr2 = (int32_t)*iptr2;         // sign-extend byte at ipt+4
iptr2 += 4;                       // pre-index: r0 = r0 + 4
*(optr2 + 1) = (int32_t)*iptr2;   // sign-extend byte at ipt+8
```

**Task 3 C equivalent (6 pts):**

```c
// Task 3: ldrsh r2, [r0], #10 / ldrsh r3, [r0], #4
// Loads signed halfwords from ipt+0 and ipt+10, sign-extends to 32-bit
int16_t *iptr3 = (int16_t *)ipt;
int32_t *optr3 = (int32_t *)opt;
*optr3 = (int32_t)*iptr3;               // sign-extend halfword at ipt+0
*(optr3 + 1) = (int32_t)*(iptr3 + 5);   // sign-extend halfword at ipt+10
```

Note: `iptr3 + 5` means offset of `5 * sizeof(int16_t) = 10` bytes, matching the post-indexed `#10` offset.

**Task 4 C equivalent (6 pts):**

```c
// Task 4: ldrh r3, [r0, r2, LSL #1] with r2 starting at 1
// Loads unsigned halfwords using register-offset addressing
uint16_t *iptr4 = (uint16_t *)ipt;
int32_t *optr4 = (int32_t *)opt;
int i = 1;
*optr4 = (int32_t)*(iptr4 + i);         // halfword at ipt + i*2
i++;
*(optr4 + 1) = (int32_t)*(iptr4 + i);   // halfword at ipt + i*2
i++;
```

Note: `LDRH` with `r2, LSL #1` means the offset is `r2 * 2` bytes, which matches pointer arithmetic on `uint16_t *` (each element is 2 bytes), so `*(iptr4 + i)` naturally computes `ipt + i * 2`.
