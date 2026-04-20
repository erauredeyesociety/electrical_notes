# HW 12 - Solutions

## Problem 1

### Setup

The algorithm walks a null-terminated string three characters at a time. For each group of three, the last two characters are swapped (i.e., at indices `i+1` and `i+2` of the trio); the first character of the trio is left alone. If the string runs out before a complete trio is seen, no further swap happens. The return value is the number of trios successfully swapped.

Per the HW 12 examples:

| Input   | Output   | Return |
|---------|----------|--------|
| `h`     | `h`      | 0      |
| `he`    | `he`     | 0      |
| `hel`   | `hle`    | 1      |
| `helo`  | `hleo`   | 1      |
| `hello` | `hlelo`  | 1      |
| `hellow`| `hlelwo` | 2      |

This is the same pattern as Lctr 27 Exercise 1 (swap the adjacent two chars of each trio), so we follow the `while`-loop and `while (1)`-with-`break` structure developed there.

### Part 1 (20 pts) — C Implementation

A compact `while (1) { ... break; ... }` structure fits this problem because we do not know the string length in advance and we must stop as soon as we fail to read three non-null characters. For each pass:

1. Read the first char of the trio (`c1`). If it is `\0`, stop — no trio.
2. Read the second char (`c2`). If it is `\0`, stop — no trio (and keep `c1` where it is).
3. Read the third char (`c3`). If it is `\0`, stop — incomplete trio (still no swap).
4. Otherwise, write `c3` into the position of `c2`, and `c2` into the position of `c3`; increment `pair_swapped`.

```c
int mp_swap_last_2_chars_in_3_in_str_c(char *str) {
    int pair_swapped = 0;
    while (1) {
        char c1 = *str++;                       // advance past char 1 of trio
        if (c1 == 0) { break; }
        char c2 = *str++;                       // advance past char 2 of trio
        if (c2 == 0) { break; }
        char c3 = *str++;                       // advance past char 3 of trio
        if (c3 == 0) { break; }                 // incomplete trio, no swap
        *(str - 2) = c3;                        // char at (c2's slot) <- c3
        *(str - 1) = c2;                        // char at (c3's slot) <- c2
        pair_swapped++;
    }
    return pair_swapped;
}
```

**Trace check:**

- `hel`: reads `h`, `e`, `l`; none are 0 → write `l` to slot of `e`, `e` to slot of `l` → `hle`. Next pass reads `\0` → break. Return 1. ✔
- `hello`: first pass same as above → `hle`. Second pass reads `l`, `o`, `\0` → break (incomplete trio; the earlier trio is preserved). String at this point is `hlelo`. Return 1. ✔
- `hellow`: first pass → `hle`; second pass reads `l`, `o`, `w`, none 0 → swap → `hlelwo`. Third pass reads `\0` → break. Return 2. ✔
- `he`: reads `h`, `e`, `\0` → break. Return 0. ✔

---

### Part 2 (20 pts) — ASM Translation

#### Register Mapping (AAPCS)

For `int mp_swap_last_2_chars_in_3_in_str_s(char *str)`:

| Register | Usage                                  |
|----------|----------------------------------------|
| `r0`     | `str` (cursor; return value at end)    |
| `r1`     | `c1` (first char of trio)              |
| `r2`     | `c2` (second char of trio)             |
| `r3`     | `c3` (third char of trio)              |
| `r12`    | `pair_swapped` accumulator             |

`r1`–`r3` and `r12` are scratch under AAPCS (Lctr 23), so no push/pop is needed. We hold the running `pair_swapped` in `r12` during the loop and move it to `r0` just before return (since `r0` is being used as the cursor inside the loop). All chars are `char` (byte), so we use `LDRB` / `STRB`. A zero-byte test is a natural fit for `CBZ` (Lctr 25 / Lctr 27 Example 1b).

#### Per-loop-section translation plan

| C statement                       | ASM                                     |
|-----------------------------------|-----------------------------------------|
| `c1 = *str++;`                    | `ldrb r1, [r0], #1`  (post-indexed)     |
| `if (c1 == 0) break;`             | `cbz  r1, ..._end`                      |
| `c2 = *str++;`                    | `ldrb r2, [r0], #1`                     |
| `if (c2 == 0) break;`             | `cbz  r2, ..._end`                      |
| `c3 = *str++;`                    | `ldrb r3, [r0], #1`                     |
| `if (c3 == 0) break;`             | `cbz  r3, ..._end`                      |
| `*(str - 2) = c3;`                | `strb r3, [r0, #-2]`                    |
| `*(str - 1) = c2;`                | `strb r2, [r0, #-1]`                    |
| `pair_swapped++;`                 | `add  r12, r12, #1`                     |
| loop back                         | `b    ..._lp`                           |

#### Complete ASM listing

```asm
    .global mp_swap_last_2_chars_in_3_in_str_s
    .text

@ int mp_swap_last_2_chars_in_3_in_str_s(char *str);
@   Regs: str -> r0
@   Regs: c1 -> r1, c2 -> r2, c3 -> r3, pair_swapped -> r12
mp_swap_last_2_chars_in_3_in_str_s:
    mov     r12, #0                 @ pair_swapped = 0
mp_swap_last_2_chars_in_3_in_str_s_lp:
    ldrb    r1, [r0], #1            @ c1 = *str++;           (post-indexed)
    cbz     r1, mp_swap_last_2_chars_in_3_in_str_s_end   @ if c1 == 0, break
    ldrb    r2, [r0], #1            @ c2 = *str++;
    cbz     r2, mp_swap_last_2_chars_in_3_in_str_s_end   @ if c2 == 0, break
    ldrb    r3, [r0], #1            @ c3 = *str++;
    cbz     r3, mp_swap_last_2_chars_in_3_in_str_s_end   @ if c3 == 0, break
        strb    r3, [r0, #-2]       @ *(str - 2) = c3;       (c2's old slot)
        strb    r2, [r0, #-1]       @ *(str - 1) = c2;       (c3's old slot)
        add     r12, r12, #1        @ pair_swapped++;
    b       mp_swap_last_2_chars_in_3_in_str_s_lp
mp_swap_last_2_chars_in_3_in_str_s_end:
    mov     r0, r12                 @ return pair_swapped
    bx      lr
```

#### Sanity check

- **Post-indexed `LDRB ..., [r0], #1`** implements `*str++` exactly — the old address is dereferenced and then `str` advances by `sizeof(char) = 1` (Lctr 20; used identically in Lctr 26 Example 10 and Lctr 27 Example 1b).
- **`CBZ r1, end`** avoids the `cmp r1, #0` + `beq end` pair on a fresh byte load. `CBZ`/`CBNZ` are unsigned zero tests only — perfect here since a null terminator is the byte `0x00`. `CBZ` cannot appear inside an IT block (Lctr 24 / Lctr 25), which is fine — we are not using conditional execution.
- **`STRB r3, [r0, #-2]`** is a plain base-plus-negative-offset store (Lctr 20). After the third `LDRB`, `r0` points one byte past the third char of the trio, so offsets `-2` and `-1` address the 2nd and 3rd chars of that trio. No writeback (`!`) is used — we do not want to modify `r0`.
- **Accumulator in `r12`** (the IP register) is legal as scratch under AAPCS (Lctr 23) and frees us from pushing `r4` for a single local.
- **Early-exit correctness:** All three `CBZ`s jump to the common `_end` label, so a null terminator at any position of the trio produces the current `pair_swapped` — exactly matching the C.
- **String-termination invariant preserved:** `STRB` writes over bytes that were already part of the trio (both non-zero); the null terminator at the end of the original string is never overwritten.

---

## Problem 2

### Setup

We are given the lower-to-upper string copy function:

```c
void mp_str_cpy_2_caps_while_c(char *dst, char *src) {
    char ch = *src++;
    while (ch) {
        ch -= 0x20;
        *dst++ = ch;
        ch = *src++;
    }
    *dst++ = ch;
}
```

Note two things about the given C code:

1. The assignment `ch = *src++` is **repeated** — once before the loop (priming read) and once inside the loop body (update). This is the classic "read before test" shape of the `while` loop from Lctr 26 Example 8.
2. After the loop exits, `*dst++ = ch` writes the null terminator to `dst`. Because the loop exit condition is `ch == 0`, this last store copies the `\0` byte and properly terminates the destination string.

Character conversion `ch -= 0x20` maps lowercase ASCII (`'a' = 0x61`, …, `'z' = 0x7A`) to uppercase ASCII (`'A' = 0x41`, …, `'Z' = 0x5A`). The `\0` byte (`0x00`) must never be converted — and indeed, the `while (ch)` guard ensures the subtraction only runs on non-null bytes.

### Register Mapping (AAPCS) — shared by all three parts

For `mp_str_cpy_2_caps_while_*(char *dst, char *src)`:

| Register | Usage                      |
|----------|----------------------------|
| `r0`     | `dst` (cursor)             |
| `r1`     | `src` (cursor)             |
| `r2`     | `ch` (working byte)        |

Return type is `void`, so `r0` is free to be clobbered. All three registers are scratch under AAPCS. No push/pop is needed.

---

### Part 1 (30 pts) — ASM Translation of the `while` version

#### Per-loop-section translation plan

Direct one-to-one mapping of the C (same shape as Lctr 26 Example 10, left column):

| C statement           | ASM                       |
|-----------------------|---------------------------|
| `ch = *src++;`        | `ldrb r2, [r1], #1`       |
| `while (ch) { ... }`  | `cbz  r2, ..._end_body`   |
| `ch -= 0x20;`         | `sub  r2, r2, #0x20`      |
| `*dst++ = ch;`        | `strb r2, [r0], #1`       |
| `ch = *src++;`        | `ldrb r2, [r1], #1`       |
| loop back             | `b    ..._lp`             |
| `*dst++ = ch;` (post) | `strb r2, [r0], #1`       |

The post-loop `*dst++ = ch` stores the null terminator. Writeback (`#1`) on the final `STRB` is harmless — `r0` dies at function exit.

#### Complete ASM listing

```asm
    .global mp_str_cpy_2_caps_while_s
    .text

@ void mp_str_cpy_2_caps_while_s(char *dst, char *src);
@   Regs: dst -> r0, src -> r1, ch -> r2
mp_str_cpy_2_caps_while_s:
    ldrb    r2, [r1], #1            @ ch = *src++;           (priming read)
mp_str_cpy_2_caps_while_s_lp:
    cbz     r2, mp_str_cpy_2_caps_while_s_end   @ while (ch)
        sub     r2, r2, #0x20       @ ch -= 0x20;           ('a'->'A', etc.)
        strb    r2, [r0], #1        @ *dst++ = ch;
        ldrb    r2, [r1], #1        @ ch = *src++;
    b       mp_str_cpy_2_caps_while_s_lp
mp_str_cpy_2_caps_while_s_end:
    strb    r2, [r0], #1            @ *dst++ = ch;           (writes '\0')
    bx      lr
```

#### Sanity check

- **`CBZ r2, _end`** is the natural translation of `while (ch)` against a freshly-loaded byte — it tests if `ch == 0` without setting any flags (Lctr 25, Lctr 26 Example 7).
- **Post-indexed `LDRB`/`STRB` with `#1`** implement `*src++` and `*dst++` atomically (Lctr 20; Lctr 26 Example 10).
- **`SUB r2, r2, #0x20`** — `0x20` is an encodable Thumb-2 modified immediate. Note that only 8 bits of `r2` are meaningful (we loaded with `LDRB`, which zero-extends), so even if `r2` were later used as a 32-bit value the arithmetic is still correct for any ASCII lowercase input.
- **The trailing `*dst++ = ch`** correctly writes `\0` because the loop exit guarantees `ch == 0` at the top of `_end`. This matches the behavior of the given C code literally.
- **Repetition cost:** The two `LDRB r2, [r1], #1` instructions (priming + update) are the "code repetition" the HW 12 Part 2 refactor addresses — this is identical to the Lctr 27 discussion of `while (1)` with `break`.

---

### Part 2 (10 pts) — `while (1)` with `break` in C

We can fold the priming read and the in-loop update into a single read at the top of a `while (1)` body, and exit with `break` once we see the null terminator. This removes the duplication and mirrors Lctr 27 Example 1a (the `mp_swap_pairs_in_str_break` pattern).

```c
void mp_str_cpy_2_caps_while_brk_c(char *dst, char *src) {
    while (1) {
        char ch = *src++;
        if (ch == 0) {
            *dst++ = ch;            // write the '\0' terminator
            break;
        }
        ch -= 0x20;
        *dst++ = ch;
    }
}
```

**Trace check against the `while` version:**

- For a non-null byte, both versions do: read → subtract `0x20` → store → loop.
- For the null byte, both versions store `0` to `*dst` exactly once and then exit.

So the observable behavior (bytes written into `dst`, and final `src`/`dst` positions) is identical to the original. Only the source shape has changed — there is now exactly one `ch = *src++` and one `*dst++ = ch`-for-the-terminator pair.

---

### Part 3 (20 pts) — ASM Translation of the `while`-with-`break` version

#### Per-loop-section translation plan

Directly mirrors the refactored C (same shape as Lctr 27 Example 1b, the `mp_swap_pairs_in_str_break_s` listing):

| C statement          | ASM                           |
|----------------------|-------------------------------|
| `while (1) {`        | (just the label)              |
| `ch = *src++;`       | `ldrb r2, [r1], #1`           |
| `if (ch == 0) { *dst++ = ch; break; }` | `cbz r2, ..._end`   (followed by `strb r2, [r0], #1` at `_end`) |
| `ch -= 0x20;`        | `sub  r2, r2, #0x20`          |
| `*dst++ = ch;`       | `strb r2, [r0], #1`           |
| loop back            | `b    ..._lp`                 |

Because a null-terminator store still has to happen after `break`, we put the `STRB r2, [r0], #1` at the exit label. `r2` at `_end` is guaranteed zero by `CBZ`.

#### Complete ASM listing

```asm
    .global mp_str_cpy_2_caps_while_brk_s
    .text

@ void mp_str_cpy_2_caps_while_brk_s(char *dst, char *src);
@   Regs: dst -> r0, src -> r1, ch -> r2
mp_str_cpy_2_caps_while_brk_s:
mp_str_cpy_2_caps_while_brk_s_lp:
    ldrb    r2, [r1], #1            @ ch = *src++;
    cbz     r2, mp_str_cpy_2_caps_while_brk_s_end   @ if (ch == 0) break;
        sub     r2, r2, #0x20       @ ch -= 0x20;
        strb    r2, [r0], #1        @ *dst++ = ch;
    b       mp_str_cpy_2_caps_while_brk_s_lp
mp_str_cpy_2_caps_while_brk_s_end:
    strb    r2, [r0], #1            @ *dst++ = ch;           (writes '\0')
    bx      lr
```

#### Sanity check

- **Only one `LDRB`** in the whole function — the "repetition" has been eliminated (Lctr 27 Sec 27.2 explicitly calls this out as the benefit of `while (1) { ... break; }`).
- **`CBZ r2, _end`** implements the `if (ch == 0) break;` idiom directly. Per Lctr 24 / Lctr 25, `CBZ`/`CBNZ` cannot appear inside an IT block, but that restriction does not apply here — we are using them as plain conditional branches inside a loop.
- **The null-byte store lives at `_end`** because the `break`-path in C writes `*dst++ = ch` before jumping out. Putting the `STRB` at the loop-exit label keeps the implementation one-to-one with the refactored C and avoids duplicating the instruction.
- **Byte counts vs Part 1:** Part 1 had three `LDRB`s of text (the priming read and the in-loop read, both `ldrb r2, [r1], #1`, plus the trailing terminator `strb`). Part 3 has only one `LDRB` and one `STRB` inside the loop, plus the `_end` `STRB`. Net savings: one `LDRB` per function (small, but exactly the refactor's point).
- **Post-indexed writeback on the terminator `STRB`** is harmless — `r0` is dead after the store.
