CEC 320 HW 9. LDR and STR Instructions                                                Spring 2026

Total points: 160

---

## Prob 1. (40 pts)

Assume the 16 1-BYTE values starting from address 0x2000_0000 are increasing numbers from 0, 1, 2, to 15. Consider the running of the following assembly code line-by-line sequentially:

        ldr     r4, =0x20000000     @ (1)
        ldr     r0, [r4, #4]        @ (2)
        ldr     r1, [r4, #2]!       @ (3)
        ldr     r2, [r4], #4        @ (4)
        ldr     r3, [r4]            @ (5)

**Part 1.** (8 pts) Draw the memory map similar to that of Example 1 of Lctr 20 but with FOUR columns, each for a byte, Byte 0 to Byte 3, in a row. Each element should be a byte in TWO-digit hexadecimal. For example, if you have 11, you should write it as 0x0B.

**Part 2.** (32 pts total) Determine the following based on the memory map:

a. (4 pts) the value of R4 after running (1).

b. (8 pts) the values of R0 and R4 after running (2).

c. (8 pts) the values of R1 and R4 after running (3).

d. (8 pts) the value of R2 and R4 after running (4).

e. (4 pts) the value of R3 after running (5).

---

## Prob 2. (40 pts)

Assume we are given code snippets below for two ASM functions, mp_task1 and mp_task2:

        mp_task1:                       |       mp_task2:
            ldrsh r2, [r0], #4          |           ldrh  r2, [r0, #2]!
            str   r2, [r1, #0]          |           str   r2, [r1, #0]
            ldrsh r3, [r0], #4          |           ldrh  r3, [r0, #2]!
            str   r3, [r1, #4]          |           str   r3, [r1, #4]
            bx    lr                    |           bx    lr

Assume the above functions are called in the C program which has the following code

    int16_t  *p16s = arr_s;  // arr_s, a signed input array defined somewhere
    uint16_t *p16u = arr_u;  // arr_u, an unsigned input array defined somewhere
    int      *p32  = arr_32; // arr_32 is an output array defined somewhere

Read the above code carefully and guess the functionalities of them. Then do the following:

1. (20 pts, 10 each function) (a, 3 pts) Determine the number of parameters of the function; (b, 4 pts) Provide the prototypes of the above two functions in the C program; (c, 3 pts) Give a calling example. (Note that you can use some of the above defined variables when creating the calling examples. You can also use constants in the calling examples. If you need to see examples of calling examples, take a look at test code of the class demo project.)

2. (20 pts, 10 each) Write the C code to finish the functionalities of the above two assembly functions. Note that the values of the above pointers may be changed during your operation. You need to reset them after each task if needed. For example, if you have changed the value of p16s, you can run p16s = arr_s again to reset p16s before use it again. (No need to write the C code in functions; just write C code in the after the last line of code where the pointers are defined in the given code above.)

---

## Prob 3. (80 pts)

Assume we are given code snippets below:

**C code:**

    // Functions defined in a .s file
    extern void mp_task1(uint8_t *pIpt, int32_t *pOup);
    extern void mp_task2(uint8_t *pIpt, int32_t *pOup);
    extern void mp_task3(uint8_t *pIpt, int32_t *pOup);
    extern void mp_task4(uint8_t *pIpt, int32_t *pOup, int i);

    // Global variable
    uint8_t ipt[16];       // Input data
    int32_t opt[4];        // Output data

    int main(void) {
        for (int i = 0; i < 16; i++) {
            ipt[i] = i<<4;
        }

        mp_task1(ipt, opt);
        printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

        mp_task2(ipt, opt);
        printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

        mp_task3(ipt, opt);
        printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

        mp_task4(ipt, opt, 1);
        printf("Out1 = 0x%X, Out2 = 0x%X\n", opt[0], opt[1]);

        while (1);
    }

**Assembly code:**

    mp_task1:
        ldr     r2, [r0, #4]
        str     r2, [r1, #0]
        ldr     r2, [r0, #0xC]
        str     r2, [r1, #4]
        bx      lr

    mp_task2:
        ldr     r2, [r0, #4]!
        str     r2, [r1, #0]
        ldr     r2, [r0, #4]!
        str     r2, [r1, #4]
        bx      lr

    mp_task3:
        ldr     r2, [r0], #4
        str     r2, [r1, #0]
        ldr     r2, [r0], #4
        str     r2, [r1, #4]
        bx      lr

    mp_task4:
        ldr     r3, [r0, r2, lsl #2]
        str     r3, [r1, #0]
        add     r2, #1
        ldr     r3, [r0, r2, lsl #2]
        str     r3, [r1, #4]
        add     r2, #1
        bx      lr

You may have noticed that the ALL pointers in the assembly functions are pointers to 32-bit numbers although some of them are defined as pointers of 8-bit numbers. Please follow the assembly's intention.

**Part 1.** (8 pts) Draw the memory map similar to that of Example 1 of Lctr 20 but with FOUR columns, each for a byte, Byte 0 to Byte 3, in a row. Each element should be a byte in TWO-digit hexadecimal. For example, if you have 11, you should write it as 0x0B. Note that we are not given the specific address of ipt. The address of the memory can be labeled in a form based on ipt, such as ipt + 0 and ipt + 4.

**Part 2.** Determine the following (without running the program first):

a. (8 pts) the printout after running Task 1 (the 2-line of code for mp_task1).

b. (16 pts) the printout after running Task 2 and the values in R0 and R1 in hexadecimal after running Task 2 assuming their values are 0x20001010 and 0x20001040, respectively, when the function is called.

c. (16 pts) the printout after running Task 3 and the values in R0 and R1 in hexadecimal after running Task 3 assuming their values are 0x20001010 and 0x20001040, respectively, when the function is called.

d. (16 pts) the printout after running Task 4 and the values in R2 and R3 in hexadecimal after running Task 4.

e. (16 pts, 4 pts each) the corresponding C code for each task.
