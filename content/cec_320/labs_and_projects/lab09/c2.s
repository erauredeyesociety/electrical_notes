    .section .text
    .syntax unified

    .align

    .weak   mp_max_ab_i_s
    .type   mp_max_ab_i_s, %function
    .weak   mp_range_square_sum_standard_while_s
    .type   mp_range_square_sum_standard_while_s, %function


@ int mp_max_ab_i_c(int a, int b) {
@     if (a >= b) {
@         return a;
@     } else {
@         return b;
@     }
@ }
@ int mp_max_ab_i_s(int a, int b)
@   Input:
@     * a -> r0
@     * b -> r1
@   Output:
@     * r0
mp_max_ab_i_s:
    cmp     r0, r1                  @ compare a and b (signed)
    bge     mp_max_ab_i_s_end_if    @ if a >= b, keep r0 (= a)
    mov     r0, r1                  @ else return b
mp_max_ab_i_s_end_if:
    bx      lr


@ int64_t mp_range_square_sum_standard_while_c(int s, int e) {
@     int64_t sum = 0;
@     int64_t i = s;
@     while (i <= e) {
@         sum += i*i;
@         i++;
@     }
@     return sum;
@ }
@ int64_t mp_range_square_sum_standard_while_s(int s, int e)
@   Input:
@     * s -> r0 (will be used as i)
@     * e -> r1
@   Output:
@     * r1:r0
@   Others:
@     * sum_low_word -> r2, sum_high_word -> r3
mp_range_square_sum_standard_while_s:
    push    {r4, r5, lr}
    mov     r2, #0                  @ sum_low_word  = 0
    mov     r3, #0                  @ sum_high_word = 0
                                    @ r0 already holds i = s
loop_sq_s:
    cmp     r0, r1                  @ compare i and e (signed)
    bgt     end_sq_s                @ if i > e, exit loop
    smull   r4, r5, r0, r0          @ r5:r4 = (int64_t)i * i  (signed)
    adds    r2, r2, r4              @ sum_low  += r4  (sets carry)
    adc     r3, r3, r5              @ sum_high += r5 + carry
    add     r0, r0, #1              @ i++
    b       loop_sq_s
end_sq_s:
    mov     r0, r2                  @ return low word in r0
    mov     r1, r3                  @ return high word in r1
    pop     {r4, r5, pc}            @ return sum

    .end                    @ end of the file
