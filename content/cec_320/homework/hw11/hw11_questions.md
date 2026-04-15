# HW 11 - If-Based Flow Control

Total points: 140

## Problem 1 (40 pts total)

Translate the following C function to ASM functions:

```c
int32_t x_cmp_y_load(int32_t x, int32_t y, int16_t *ptrA, int32_t *ptrB) {
    if (x > y) {
        return (int32_t)*(++ptrA) * 2;
    } else {
        return *(ptrB++) / 2;
    }
}
```

Note that we need to write the assembly function to strictly implement the C statements. Even though the changes to the pointers cannot propagate outside of the function, we still implement their changes in assembly.

### Part 1 (20 pts) — Positive Logic (PL)

Rewrite the above C function in assembly with the following start code. Replace `b..` with the appropriate conditional branch instruction; replace the `.` lines with assembly instructions (need not be one-to-one).

```asm
x_cmp_y_load_pl:        @ PL stands for positive logic
    cmp     r0, r1
    b..     x_cmp_y_load_pl_then
x_cmp_y_load_pl_else:
    .
    .
    .
    .
    .
x_cmp_y_load_pl_then:
    .
    .
    .
    .
x_cmp_y_load_pl_end:
    bx      lr
```

Note: positive logic uses the same logic as the C `if` test, so the `else` code block appears before the `then` code block.

### Part 2 (10 pts) — Negative Logic (NL)

Rewrite the above C function in assembly with the following start code. Replace `b..` with the appropriate conditional branch instruction.

```asm
x_cmp_y_load_nl:        @ NL stands for negative logic
    cmp     r0, r1
    b..     x_cmp_y_load_nl_else
x_cmp_y_load_nl_then:
    .
    .
    .
    .
    .
x_cmp_y_load_nl_else:
    .
    .
    .
    .
x_cmp_y_load_nl_end:
    bx      lr
```

Note: negative logic uses the opposite of the C `if` test, so the `then` code block appears before the `else` code block.

### Part 3 (10 pts) — CEX Approach

Rewrite the above C function in assembly using the CEX (conditional execution) approach with the following start code.

```asm
x_cmp_y_load_cex:       @ CEX: conditional execution
    cmp     r0, r1
    .
    .
    .
    .
    .
    .
    .
    bx      lr
```

Note: use negative logic (opposite of the C `if` test) so the `else` code block follows the `then` code block.

---

## Problem 2 (60 pts, 20 pts each)

Consider a problem implementing the following math function for integer input `x`:

```
         | -10,  x < -5
f(x) =   |  10,  x >= 5
         |  2x,  otherwise
```

### Part 1 (20 pts) — C Implementation

Write a C function to implement the above math function using the prototype below:

```c
int mathf_c(int x);
```

Note: use a simple if-else-if structure.

### Part 2 (20 pts) — CMP Approach

Translate the above C function to assembly using the prototype below:

```c
int mathf_cmp(int x);
```

Note: use the CMP (conditional branch) approach.

### Part 3 (20 pts) — CEX Approach

Translate the above C function to assembly using the prototype below:

```c
int mathf_cex(int x);
```

Note: use the CEX (conditional execution) approach.

---

## Problem 3 (40 pts total, 20 pts each)

Given the following C function for returning a 16-bit or 32-bit value using a pointer:

```c
int32_t load_based_on_x_c(int x, uint16_t *ptrA, uint32_t *ptrB) {
    if (x <= 20 || x >= 25) {
        return (int32_t)*++ptrA * 4;
    } else {
        return *++ptrB / 4;
    }
}
```

### Part 1 (20 pts) — CMP Approach

Rewrite the above C function in assembly using the standard conditional branch–based approach with the function name `load_based_on_x_cmp`.

### Part 2 (20 pts) — CEX Approach

Rewrite the above C function in assembly using as much conditional execution as possible with the function name `load_based_on_x_cex`.
