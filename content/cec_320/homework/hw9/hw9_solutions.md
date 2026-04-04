# CEC 320 HW 9 — LDR and STR Instructions

---

## Prob 1

We are given 16 bytes starting at 0x20000000 with increasing values 0 through 15. We run the following assembly sequentially:

    ldr     r4, =0x20000000     @ (1)
    ldr     r0, [r4, #4]        @ (2)
    ldr     r1, [r4, #2]!       @ (3)
    ldr     r2, [r4], #4        @ (4)
    ldr     r3, [r4]            @ (5)

### Part 1: Memory Map

    Address      | Byte 0 | Byte 1 | Byte 2 | Byte 3
    0x20000000   | 0x00   | 0x01   | 0x02   | 0x03
    0x20000004   | 0x04   | 0x05   | 0x06   | 0x07
    0x20000008   | 0x08   | 0x09   | 0x0A   | 0x0B
    0x2000000C   | 0x0C   | 0x0D   | 0x0E   | 0x0F

### Part 2a: After (1)

Pseudo-instruction loads the constant.

    R4 = 0x20000000

### Part 2b: After (2)

Offset addressing — load from r4+4, r4 unchanged.
Effective address = 0x20000004. Bytes: 0x04, 0x05, 0x06, 0x07.
Little-endian 32-bit word: 0x07060504.

    R0 = 0x07060504
    R4 = 0x20000000  (unchanged)

### Part 2c: After (3)

Pre-index — update r4 first, then load from the new r4.
R4 = 0x20000000 + 2 = 0x20000002.
Bytes at 0x20000002: 0x02, 0x03, 0x04, 0x05. Little-endian: 0x05040302.

    R1 = 0x05040302
    R4 = 0x20000002

### Part 2d: After (4)

Post-index — load from current r4, then update r4.
Load from 0x20000002: same bytes as above, 0x05040302.
Then R4 = 0x20000002 + 4 = 0x20000006.

    R2 = 0x05040302
    R4 = 0x20000006

### Part 2e: After (5)

Simple load from r4 = 0x20000006.
Bytes: 0x06, 0x07, 0x08, 0x09. Little-endian: 0x09080706.

    R3 = 0x09080706

---

## Prob 2

We are given two ASM functions and three C pointer declarations:

    mp_task1:                       mp_task2:
        ldrsh r2, [r0], #4             ldrh  r2, [r0, #2]!
        str   r2, [r1, #0]             str   r2, [r1, #0]
        ldrsh r3, [r0], #4             ldrh  r3, [r0, #2]!
        str   r3, [r1, #4]             str   r3, [r1, #4]
        bx    lr                        bx    lr

    int16_t  *p16s = arr_s;
    uint16_t *p16u = arr_u;
    int      *p32  = arr_32;

### mp_task1

1a. 2 parameters (r0 and r1).

1b. Prototype:

    void mp_task1(int16_t *pSrc, int32_t *pDst);

LDRSH loads a signed halfword and sign-extends to 32 bits, so the source is int16_t*. STR writes 32-bit words, so the destination is int32_t*.

1c. Calling example:

    mp_task1(p16s, p32);

The function loads arr_s[0] sign-extended into p32[0], then advances r0 by 4 bytes (post-index), loads arr_s[2] sign-extended into p32[1], and advances again. The #4 post-index skips every other halfword.

### mp_task2

1a. 2 parameters (r0 and r1).

1b. Prototype:

    void mp_task2(uint16_t *pSrc, int32_t *pDst);

LDRH loads an unsigned halfword and zero-extends to 32 bits, so the source is uint16_t*.

1c. Calling example:

    mp_task2(p16u, p32);

Pre-index #2 advances r0 by 2 bytes before each load, so it skips the first element. Reads arr_u[1] into p32[0] and arr_u[2] into p32[1].

### C code equivalents

mp_task1:

    *p32 = (int32_t)(*p16s);       // arr_s[0] sign-extended to arr_32[0]
    p16s += 2;                      // advance 4 bytes = 2 halfwords
    *(p32 + 1) = (int32_t)(*p16s); // arr_s[2] sign-extended to arr_32[1]
    p16s += 2;

mp_task2:

    p16u += 1;                      // pre-index: advance 2 bytes first
    *p32 = (int32_t)(*p16u);       // arr_u[1] zero-extended to arr_32[0]
    p16u += 1;
    *(p32 + 1) = (int32_t)(*p16u); // arr_u[2] zero-extended to arr_32[1]

---

## Prob 3

We are given ipt[16] initialized as ipt[i] = i << 4, and opt[4] as the output. Four ASM tasks operate on these arrays. Per the problem statement, all pointers in the assembly are treated as 32-bit pointers.

### Part 1: Memory Map

    ipt[0]=0x00  ipt[1]=0x10  ipt[2]=0x20  ipt[3]=0x30
    ipt[4]=0x40  ipt[5]=0x50  ipt[6]=0x60  ipt[7]=0x70
    ipt[8]=0x80  ipt[9]=0x90  ipt[10]=0xA0 ipt[11]=0xB0
    ipt[12]=0xC0 ipt[13]=0xD0 ipt[14]=0xE0 ipt[15]=0xF0

    Address  | Byte 0 | Byte 1 | Byte 2 | Byte 3
    ipt+0    | 0x00   | 0x10   | 0x20   | 0x30
    ipt+4    | 0x40   | 0x50   | 0x60   | 0x70
    ipt+8    | 0x80   | 0x90   | 0xA0   | 0xB0
    ipt+12   | 0xC0   | 0xD0   | 0xE0   | 0xF0

32-bit words (little-endian) at each offset:

    ipt+0  -> 0x30201000
    ipt+4  -> 0x70605040
    ipt+8  -> 0xB0A09080
    ipt+12 -> 0xF0E0D0C0

### Part 2a: Task 1

    ldr r2, [r0, #4]       @ load from ipt+4
    str r2, [r1, #0]       @ opt[0] = 0x70605040
    ldr r2, [r0, #0xC]     @ load from ipt+12
    str r2, [r1, #4]       @ opt[1] = 0xF0E0D0C0

Offset addressing. R0 unchanged.

    Printout: Out1 = 0x70605040, Out2 = 0xF0E0D0C0

### Part 2b: Task 2

R0 = 0x20001010, R1 = 0x20001040 at entry.

    ldr r2, [r0, #4]!      @ pre-index: R0 = 0x20001014, load from ipt+4
    str r2, [r1, #0]       @ opt[0] = 0x70605040
    ldr r2, [r0, #4]!      @ pre-index: R0 = 0x20001018, load from ipt+8
    str r2, [r1, #4]       @ opt[1] = 0xB0A09080

    Printout: Out1 = 0x70605040, Out2 = 0xB0A09080
    R0 = 0x20001018
    R1 = 0x20001040  (unchanged)

### Part 2c: Task 3

R0 = 0x20001010, R1 = 0x20001040 at entry.

    ldr r2, [r0], #4       @ post-index: load from ipt+0 first, then R0 = 0x20001014
    str r2, [r1, #0]       @ opt[0] = 0x30201000
    ldr r2, [r0], #4       @ post-index: load from ipt+4, then R0 = 0x20001018
    str r2, [r1, #4]       @ opt[1] = 0x70605040

    Printout: Out1 = 0x30201000, Out2 = 0x70605040
    R0 = 0x20001018
    R1 = 0x20001040  (unchanged)

### Part 2d: Task 4

R0 = &ipt, R1 = &opt, R2 = 1 (the third argument i=1).

    ldr r3, [r0, r2, lsl #2]   @ load from ipt + (1 << 2) = ipt+4 -> 0x70605040
    str r3, [r1, #0]            @ opt[0] = 0x70605040
    add r2, #1                  @ R2 = 2
    ldr r3, [r0, r2, lsl #2]   @ load from ipt + (2 << 2) = ipt+8 -> 0xB0A09080
    str r3, [r1, #4]            @ opt[1] = 0xB0A09080
    add r2, #1                  @ R2 = 3

Register offset with lsl #2 is array indexing: address = base + index*4.

    Printout: Out1 = 0x70605040, Out2 = 0xB0A09080
    R2 = 0x00000003
    R3 = 0xB0A09080

### Part 2e: C code

Task 1:

    int32_t *p = (int32_t *)ipt;
    opt[0] = p[1];
    opt[1] = p[3];

Task 2:

    int32_t *p = (int32_t *)ipt;
    p++;
    opt[0] = *p;
    p++;
    opt[1] = *p;

Task 3:

    int32_t *p = (int32_t *)ipt;
    opt[0] = *p;
    p++;
    opt[1] = *p;
    p++;

Task 4:

    int32_t *p = (int32_t *)ipt;
    int i = 1;
    opt[0] = p[i];
    i++;
    opt[1] = p[i];
    i++;
