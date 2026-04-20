# HW 12 - Loops in C and Assembly

Total points: 100

## Problem 1 (40 pts total)

Assume we have a string, for which we need to apply a swap operation to encrypt it. The algorithm is to swap the last 2 chars for every three chars and return the number of pairs swapped. For example:

- For string `h`, there is not enough chars to swap, and the result should still be `h`. Return is 0.
- For string `he`, there is not enough chars to swap, and the result should still be `he`. Return is 0.
- For string `hel`, we have one pair of chars to swap, and the result will be swapped to `hle`. Return is 1.
- For string `helo`, we still have one pair of chars to swap, and the result will be swapped to `hleo`. Return is 1.
- For string `hello`, we still have one pair of chars to swap, and the result will be swapped to `hlelo`. Return is 1.
- For string `hellow`, we will have two pairs of chars to swap, and the result will be swapped to `hlelwo`. Return is 2.

### Part 1 (20 pts) — C Implementation

Write a C function `int mp_swap_last_2_chars_in_3_in_str_c(char *str)` to perform the swap without calling existing function.

### Part 2 (20 pts) — ASM Translation

Translate the above C function to an assembly with a prototype being

```c
int mp_swap_last_2_chars_in_3_in_str_s(char *str);
```

---

## Problem 2 (60 pts total)

Assume we have a string of lower-case letters. Assume also we are given the following C function which is used to copy this string to a new string with all upper-case ones.

```c
void mp_str_cpy_2_caps_while_c(char *dst, char *src) {
    char ch = *src++;
    while (ch) {
        ch -= 0x20;         // 'a' = 0x61, 'A' = 0x41
        *dst++ = ch;
        ch = *src++;
    }
    *dst++ = ch;
}
```

### Part 1 (30 pts) — ASM Translation of the `while` version

Translate the above C function to an assembly with a prototype being

```c
void mp_str_cpy_2_caps_while_s(char *dst, char *src);
```

### Part 2 (10 pts) — `while (1)` with `break` in C

Reimplement the above C function using a `while` loop with `break` to eliminate the repetition code with a prototype being

```c
void mp_str_cpy_2_caps_while_brk_c(char *dst, char *src);
```

### Part 3 (20 pts) — ASM Translation of the `while`-with-`break` version

Translate the `while` with `break` C function to an assembly with a prototype being

```c
void mp_str_cpy_2_caps_while_brk_s(char *dst, char *src);
```
