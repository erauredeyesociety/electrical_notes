# In-Class Assignment — `mp_swap` in ARM Assembly

**Course:** CEC 320 — Microprocessors (Spring 2026)
**Topic:** Mixed C & ASM, pointer increments, byte load/store (Lctrs 14, 20–22)

---

## 1. The Reference C Function

```c
void mp_swap_c(char *str) {
    while (1) {
        char ch1 = *str++;
        char ch2 = *str++;
        if (ch1 == 0 || ch2 == 0) {
            break;
        }
        *(str - 1) = ch1;
        *(str - 2) = ch2;
    }
}
```

### What it does

The function walks a null-terminated C string and **swaps every adjacent pair
of characters**:

- `"ABCD"` → `"BADC"`
- `"ABC"`  → `"BAC"` (odd length — last char is left alone because `ch2` is
  the terminator, so the loop exits *before* the swap runs)
- `""`     → `""` (first `ch1` is already 0)

### Why the pointer arithmetic looks weird

After `ch1 = *str++; ch2 = *str++;` the pointer has already moved **two past**
the two bytes we just read. So:

| Expression      | Targets the byte that held … |
|-----------------|------------------------------|
| `*(str - 1)`    | `ch2`                        |
| `*(str - 2)`    | `ch1`                        |

Writing `ch1` into the `ch2` slot and `ch2` into the `ch1` slot is the swap.

### Subtle behavior to preserve in ASM

Both reads happen **before** either zero check. Our ASM must follow the same
order so it matches the reference C for every input.

---

## 2. Register Plan

Per AAPCS (Lctr 14 / 23):

| Register | Holds                                   | Notes                 |
|----------|-----------------------------------------|-----------------------|
| `r0`     | `str` (function argument, walks forward)| Caller-saved          |
| `r1`     | `ch1` (byte)                            | Scratch, caller-saved |
| `r2`     | `ch2` (byte)                            | Scratch, caller-saved |

Only caller-saved registers are used, so **no `push`/`pop`** of `r4–r11` or
`lr` is required. We return with a plain `bx lr`.

---

## 3. Instruction Mapping (C → ASM)

Every instruction used below comes from the Lctr 14–25 course deck:

| C statement              | ASM                      | Reference lecture                       |
|--------------------------|--------------------------|-----------------------------------------|
| `ch1 = *str++;`          | `ldrb r1, [r0], #1`      | Lctr 20 (post-indexed LDR), Lctr 22 (ptr incr) |
| `ch2 = *str++;`          | `ldrb r2, [r0], #1`      | same                                    |
| `if (ch1 == 0)`          | `cmp r1, #0` / `beq ...` | Lctr 18 (NZCV), Lctr 19 (CCS + branch)  |
| `if (ch2 == 0)`          | `cmp r2, #0` / `beq ...` | same                                    |
| `*(str - 1) = ch1;`      | `strb r1, [r0, #-1]`     | Lctr 20 (immediate-offset STR)          |
| `*(str - 2) = ch2;`      | `strb r2, [r0, #-2]`     | same                                    |
| unconditional loop back  | `b loop`                 | Lctr 19                                 |
| `return;`                | `bx lr`                  | Lctr 14                                 |

Two notes on the choices above:

1. **`ldrb` / `strb`, not `ldr` / `str`.** `char` is one byte on the
   Cortex-M4, so byte-width load/store is required — a word load would
   read three extra bytes of the string.
2. **Post-indexed `[r0], #1`** is the exact ASM idiom for `*p++` introduced in
   Lctr 22 §22.2.1.1 and §22.4.1.1. Using it makes the C-to-ASM mapping line
   up one-for-one.
3. **Negative immediate offsets `[r0, #-1]` / `[r0, #-2]`** are legal Thumb-2
   encodings (STRB T3 form) and directly express `*(str - 1)` / `*(str - 2)`
   without a separate `sub`.

---

## 4. ASM Solution

```asm
@ void mp_swap_s(char *str);
@
@ Register usage:
@   r0 -> str  (walks forward through the string)
@   r1 -> ch1  (byte temporary)
@   r2 -> ch2  (byte temporary)

        .syntax unified
        .thumb
        .global mp_swap_s

mp_swap_s:
mp_swap_loop:
        ldrb    r1, [r0], #1        @ ch1 = *str++;
        ldrb    r2, [r0], #1        @ ch2 = *str++;

        cmp     r1, #0              @ if (ch1 == 0)
        beq     mp_swap_done        @     break;
        cmp     r2, #0              @ if (ch2 == 0)
        beq     mp_swap_done        @     break;

        strb    r1, [r0, #-1]       @ *(str - 1) = ch1;
        strb    r2, [r0, #-2]       @ *(str - 2) = ch2;

        b       mp_swap_loop        @ while (1)

mp_swap_done:
        bx      lr                  @ return
```

---

## 5. Dry Run — `"ABCD\0"`

Memory layout (addresses relative to the start of the string):

```
 offset : 0   1   2   3   4
 byte   : 'A' 'B' 'C' 'D' '\0'
```

| Step | Instruction             | r0 after | r1 | r2 | Memory                  |
|------|-------------------------|----------|----|----|-------------------------|
| 1    | `ldrb r1, [r0], #1`     | 1        | 'A'| –  | `A B C D \0`            |
| 2    | `ldrb r2, [r0], #1`     | 2        | 'A'|'B' | `A B C D \0`            |
| 3    | `cmp r1,#0; beq`        | 2        | 'A'|'B' | not taken               |
| 4    | `cmp r2,#0; beq`        | 2        | 'A'|'B' | not taken               |
| 5    | `strb r1, [r0, #-1]`    | 2        | 'A'|'B' | `A A C D \0` (byte 1 ← 'A') |
| 6    | `strb r2, [r0, #-2]`    | 2        | 'A'|'B' | `B A C D \0` (byte 0 ← 'B') |
| 7    | `ldrb r1, [r0], #1`     | 3        | 'C'|'B' | `B A C D \0`            |
| 8    | `ldrb r2, [r0], #1`     | 4        | 'C'|'D' | `B A C D \0`            |
| 9    | swap stores             | 4        | 'C'|'D' | `B A D C \0`            |
| 10   | `ldrb r1, [r0], #1`     | 5        | '\0'|'D'| –                      |
| 11   | `ldrb r2, [r0], #1`     | 6        | '\0'| ?  | (reads past NUL — matches the C)|
| 12   | `cmp r1,#0; beq`        | –        | –  | –  | branch to `mp_swap_done`|

Final string: **`"BADC\0"`** ✔

---

## 6. In-Class Demo Trace — `"fined\0"` → `"ifend\0"`

This is the input the instructor walked through in class. The confusing part
was keeping track of which letter is `ch1` and which is `ch2`, because after
the two post-increments the pointer is already **two bytes past** the pair
being swapped.

**The rule:** for every iteration, `ch1` is the **left** byte of the pair
(read first, lower address) and `ch2` is the **right** byte (read second,
higher address). The stores then write:

- `*(str - 1) = ch1` — the **right** slot gets `ch1` (the old left byte)
- `*(str - 2) = ch2` — the **left** slot gets `ch2` (the old right byte)

So within each pair, the left and right letters simply trade places.

Starting memory:

```
 offset : 0   1   2   3   4   5
 byte   : 'f' 'i' 'n' 'e' 'd' '\0'
```

| Iter | `ch1` (left)        | `ch2` (right)       | `r0` after reads | Stores                          | String after   |
|------|---------------------|---------------------|------------------|---------------------------------|----------------|
| 1    | `'f'` from offset 0 | `'i'` from offset 1 | 2                | byte 1 ← `'f'`, byte 0 ← `'i'`  | `i f n e d \0` |
| 2    | `'n'` from offset 2 | `'e'` from offset 3 | 4                | byte 3 ← `'n'`, byte 2 ← `'e'`  | `i f e n d \0` |
| 3    | `'d'` from offset 4 | `'\0'` from offset 5| 6                | `cmp r2, #0` / `beq` → **break**| `i f e n d \0` |

Final string: **`"ifend"`** ✔

The `d` is left alone in iteration 3 because its "pair partner" is the
null terminator. The second `cmp r2, #0; beq mp_swap_done` fires *before*
the `strb` instructions run, so neither byte at offsets 4 or 5 is touched.
This is exactly how the odd-length case from section 7 below works — the
null terminator acts as the missing right-hand partner and gracefully ends
the loop.

---

## 7. Odd-Length Check — `"ABC\0"`

```
 offset : 0   1   2   3
 byte   : 'A' 'B' 'C' '\0'
```

First iteration swaps bytes 0 and 1 → `"BAC\0"`. On the second iteration
`ldrb` loads `ch1 = 'C'` then `ch2 = '\0'`; the second `cmp`/`beq` exits the
loop **before** the stores run, so `'C'` and the terminator are left in place.
Final string: **`"BAC\0"`** ✔

---

## 7. Summary

- The function is a pairwise byte-swap over a null-terminated string,
  implemented with post-indexed byte loads and negative-offset byte stores —
  a direct transcription of Lctr 22's `*p++` idiom into the byte-width forms
  from Lctr 20.
- Only `r0–r2` are touched, so no stack frame is needed and the return is a
  single `bx lr`.
- The ASM preserves the C semantics exactly, including the "both reads before
  either zero check" ordering that keeps odd-length strings working.
