    .section .text
    .syntax unified
    
    .align

    .weak   mp_bit_reverse_n_bit_naive_s
    .type   mp_bit_reverse_n_bit_naive_s, %function
    .global mp_bit_reverse_8_bit_fast_s
    .type   mp_bit_reverse_8_bit_fast_s, %function
    .weak   mp_bit_reverse_16_bit_fast_s
    .type   mp_bit_reverse_16_bit_fast_s, %function


@ uint32_t mp_bit_reverse_n_bit_naive_c(uint32_t x, int n) {
@     // Make sure n is between 2 and 32.
@     int j = n - 1;
@     for (int i = 0; i < n/2; i++, j--) {
@         uint32_t mask_i = 1U << i; 
@         uint32_t mask_j = 1U << j; 
@         uint32_t b_i = (x >> i) & 1U; 
@         uint32_t b_j = (x >> j) & 1U; 
@         x &= ~(mask_i | mask_j);
@         x |= (b_i << j) | (b_j << i);
@     }
@     return x;
@ }
@ uint32_t mp_bit_reverse_n_bit_naive_s(uint32_t x, int n)
@   Input: 
@     * x -> r0, n -> r1
@   Output:
@     * r0 
@   Local vars:
@     * r2 = 1u, r3 = j, r4 = i,
@     * r5 = mask_i, r6 = mask_j,
@     * r7 = b_i, r8 = b_j

mp_bit_reverse_n_bit_naive_s:
    push    {r4-r8, lr}
    ldr     r2, =1            @ 1u
    sub     r3, r1, #1        @ j = N-1
    ldr     r4, =0            @ i = 0
loop_n_s:
    cmp     r4, r1, ASR #1    @ i < N/2 ?
    bge     end_n_s           @ If No, end loop
        lsl     r5, r2, r4    @ mask_i = 1 << i
        lsl     r6, r2, r3    @ mask_j = 1 << j   (FIX: was r4)
        lsr     r7, r0, r4    @ x >> i            (FIX: was r3)
        and     r7, r2        @ b_i
        lsr     r8, r0, r3    @ x >> j
        and     r8, r2        @ b_j
        orr     r5, r6        @ t = mask_i | mask_j
        bic     r0, r5        @ x &= ~t
        lsl     r7, r3        @ b_i << j
        lsl     r8, r4        @ b_j << i
        orr     r7, r8        @ t = (b_i << j) | (b_j << i)
        orr     r0, r7        @ x |= t
    add     r4, #1            @ i++
    sub     r3, #1            @ j--
    b       loop_n_s
end_n_s: 
    pop     {r4-r8, pc}


@ uint8_t mp_bit_reverse_8_bit_fast_c(uint8_t x) {
@     uint32_t y = 0x55;
@     uint32_t z = y & (x >> 1);
@     x &= y;
@     x = z | (x << 1);
@     y = 0x33;
@     z = y & (x >> 2);
@     x &= y;
@     x = z | (x << 2);
@     z = x >> 4;
@     x = z | (x << 4);
@     return x;
@ }
@ uint8_t mp_bit_reverse_8_bit_fast_s(uint8_t x)
@   Input: 
@     * x -> r0 
@   Output:
@     * r0 
@   Local vars:
@     * r1 = y, r2 = z
mp_bit_reverse_8_bit_fast_s:
    ldr     r1, =0x55             @ y = 0x55
    and     r2, r1, r0, lsr #1    @ z=y&(x>>1)
    and     r0, r1                @ x &= y;
    orr     r0, r2, r0, lsl #1    @ x=z|(x<<1);
    ldr     r1, =0x33             @ y = 0x33
    and     r2, r1, r0, lsr #2    @ z=y&(x>>2)
    and     r0, r1                @ x &= y;
    orr     r0, r2, r0, lsl #2    @ x=z|(x<<2);
    lsr     r2, r0, #4            @ z = x >> 4;
    orr     r0, r2, r0, lsl #4    @ x=z|(x<<4);
    ldr     r1, =0xFF             @ 8-bit mask
    and     r0, r1                @ keep 8 bits
    bx      lr 


@ uint16_t mp_bit_reverse_16_bit_fast_c(uint16_t x) {
@     uint32_t y = 0x5555;
@     uint32_t z = y & (x >> 1);
@     x &= y;
@     x = z | (x << 1);
@     y = 0x3333;
@     z = y & (x >> 2);
@     x &= y;
@     x = z | (x << 2);
@     y = 0x0f0f;
@     z = y & (x >> 4);
@     x &= y;
@     x = z | (x << 4);
@     z = x >> 8;
@     x = z | (x << 8);
@     return x;
@ }
@ uint16_t mp_bit_reverse_16_bit_fast_s(uint16_t x)
@   Input: 
@     * x -> r0 
@   Output:
@     * r0 
@   Local vars:
@     * r1 = y, r2 = z
mp_bit_reverse_16_bit_fast_s:
    ldr     r1, =0x5555           @ y = 0x5555
    and     r2, r1, r0, lsr #1    @ z = y & (x >> 1)
    and     r0, r1                @ x &= y
    orr     r0, r2, r0, lsl #1    @ x = z | (x << 1)

    ldr     r1, =0x3333           @ y = 0x3333
    and     r2, r1, r0, lsr #2    @ z = y & (x >> 2)
    and     r0, r1                @ x &= y
    orr     r0, r2, r0, lsl #2    @ x = z | (x << 2)

    ldr     r1, =0x0f0f           @ y = 0x0f0f
    and     r2, r1, r0, lsr #4    @ z = y & (x >> 4)
    and     r0, r1                @ x &= y
    orr     r0, r2, r0, lsl #4    @ x = z | (x << 4)

    lsr     r2, r0, #8            @ z = x >> 8
    orr     r0, r2, r0, lsl #8    @ x = z | (x << 8)

    ldr     r1, =0xFFFF           @ 16-bit mask
    and     r0, r1                @ keep 16 bits
    bx      lr


    .end                    @ end of the file
