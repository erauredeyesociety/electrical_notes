# HW 10 - C Pointers and LDR/STR Instructions and Function Call

## Problem 1 (60 pts)

Assume the address of a 16-element `uint8_t` array `my_arr` is `0x2000_0100`, and the values are given in the table below.

| Address       | Byte 0 | Byte 1 |
|---------------|--------|--------|
| 0x2000_0100   | 0x00   | 0x02   |
| 0x2000_0102   | 0x04   | 0x06   |
| 0x2000_0104   | 0x08   | 0x0A   |
| 0x2000_0106   | 0x0C   | 0x0E   |
| 0x2000_0108   | 0x10   | 0x12   |
| 0x2000_010A   | 0x14   | 0x16   |

Assume we run the following code:

```c
uint8_t *p8a = (uint8_t *)0x20000100;
uint8_t *p8b = (uint8_t *)0x2000010C;

*p8b++ = *(p8a + 2);        // Line 4
*p8b++ = ++*(p8a + 4);      // Line 5
*p8b++ = ++*p8a++;           // Line 6
*p8b++ = *p8a++;             // Line 7
```

### Part 1 (10 pts)
Determine the addresses and values that have been **changed by the right-side expressions** of the statements in lines 4 to 7. For example, if we run `*p8b = ++*++p8a` as the first line of runnable code, then the value at address `0x2000_0101` would change from 0x02 to 0x03.

### Part 2 (20 pts)
Determine the four 8-bit values in memory starting at address `0x2000_010C` after running the above code.

### Part 3 (30 pts)
Write the code in lines 4 to 7 in an assembly function with the following prototype and call instance:

```c
void my_fn(uint8_t *pa, uint8_t *pb);
my_fn(p8a, p8b);
```

(5 pts for lines 4 and 7 each; 10 pts for lines 5 and 6 each)

---

## Problem 2 (74 pts)

Assume we are given the following code snippets:

### Part A: C Code

```c
// Prototype of functions defined in a .s file
extern void task1(uint8_t *pIpt, int32_t *pOup);
extern void task2(uint8_t *pIpt, int32_t *pOup);
extern void task3(uint8_t *pIpt, int32_t *pOup);
extern void task4(uint8_t *pIpt, int32_t *pOup, int i);

// Global variable
uint8_t ipt[16];    // Input data
int32_t opt[4];     // Output data

int main(void) {
    for (int i = 0; i < 16; i++) {
        ipt[i] = i << 4;
    }

    // Task 1.
    task1(ipt, opt);
    printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

    // Task 2.
    task2(ipt, opt);
    printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

    // Task 3.
    task3(ipt, opt);
    printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

    // Task 4.
    task4(ipt, opt, 1);
    printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

    while (1);
}
```

### Part B: Assembly Code

```asm
task1:
    ldrd    r2, r3, [r0, #8]!
    strd    r2, r3, [r1, #0]
    bx      lr

task2:
    ldrsb   r2, [r0, #4]!
    ldrsb   r3, [r0, #4]!
    strd    r2, r3, [r1, #0]
    bx      lr

task3:
    ldrsh   r2, [r0], #10
    ldrsh   r3, [r0], #4
    strd    r2, r3, [r1, #0]
    bx      lr

task4:
    ldrh    r3, [r0, r2, LSL #1]
    str     r3, [r1, #0]
    add     r2, #1
    ldrh    r3, [r0, r2, LSL #1]
    str     r3, [r1, #4]
    add     r2, #1
    bx      lr

    .end
```

### Question 2a (8 pts)
What will be the printout after Task 1?

### Question 2b (14 pts)
What will be the printout after Task 2 and what will be the values in `r0` and `r1` in hexadecimal after running Task 2, assuming their values are `0x20001010` and `0x20001040`, respectively, before running the first line of code in function Task2?

### Question 2c (14 pts)
What will be the printout after Task 3 and what will be the values in `r0` and `r1` in hexadecimal after running Task 3, assuming their values are `0x20001010` and `0x20001040`, respectively, before running the first line of code in function Task3?

### Question 2d (14 pts)
What will be the printout after Task 4 and what will be the values in `r2` and `r3` in hexadecimal after running Task 4?

### Question 2e (24 pts)
What will be the corresponding C code for each task if all the tasks are listed in the same function? Note:
- If all the tasks are listed in the same function, we cannot change the values of `ipt` and `opt` in each task; otherwise, the results will be totally different. Define new pointers and work on those.
- You don't have to write the C code with data in the 64-bit format. As long as we have the same result, it will be ok.
