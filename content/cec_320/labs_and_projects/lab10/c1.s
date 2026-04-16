    .section .text
    .syntax unified

    .align

    .global mp_reg_offset_load_s
    .type   mp_reg_offset_load_s, %function

    .global mp_store_for_different_types_s
    .type   mp_store_for_different_types_s, %function

    .global mp_various_pseudo_ldr_s
    .type   mp_various_pseudo_ldr_s, %function

    .global mp_init_mem_block_s1
    .type   mp_init_mem_block_s1, %function
    .global mp_init_mem_block_s2
    .type   mp_init_mem_block_s2, %function

    .global mp_array_abs_sum_var_ptr_s
    .type   mp_array_abs_sum_var_ptr_s, %function
    .global mp_array_abs_sum_cst_ptr_s
    .type   mp_array_abs_sum_cst_ptr_s, %function

    .global mp_array_pos_sum_cst_ptr_s
    .type   mp_array_pos_sum_cst_ptr_s, %function

    .include "ge1s_asm_macros.s"


@ void mp_reg_offset_load_s(R1toR6_t *pR1toR6)
@   Input:
@     * Ra -> r0 (Address)
@   Output:
@     * None
mp_reg_offset_load_s:
    push    {r4-r6, lr}         @ Push the related Regs in stack
    initialize_r1_to_r6_local   @ Initialization for stressing the changes

    @ Set values to the address registers
    ldr     r1, =0x20000204
    ldr     r2, =2

    store_r1_to_r6_local 0  @ Store the registers before operations

    @ Read via using LDR    @ Load instruction of the problem
    ldr       r3, [r1, r2, lsl #2]
    ldrsb     r4, [r1, r2, lsl #1]
    ldrsh     r5, [r1, r2, lsl #2]
    ldrsh     r6, [r1, #6]!
    ldrh      r2, [r1, r2, lsl #1]

    store_r1_to_r6_local 24 @ Store the registers after operations
    pop     {r4-r6, pc}     @ Restore the values of Regs and return


@ void mp_store_for_different_types_c(uint32_t *p32, int i, int var32) {
@     *(p32 + i) = var32;
@     *((uint16_t *)p32 + i) = var32;
@     *((uint8_t *)p32 + i) = var32;
@ }

@ void mp_store_for_different_types_s(uint32_t *p32, int i, int var32);
@   Input:
@     * p32 -> r0       The pointer to uint32_t
@     * i -> r1         The number for an index
@     * var32 -> r2     The number for storing
@   Output:
@     * None

mp_store_for_different_types_s:
    str     r2, [r0, r1, lsl #2] @ Write 32 bits at address = (p32 + 4*i)
    strh    r2, [r0, r1, lsl #1] @ Write 16 bits at address = (p32 + 2*i)
    strb    r2, [r0, r1]         @ Write 8 bits at address = (p32 + i)
    bx      lr


mp_various_pseudo_ldr_s:
    push    {r4-r6, lr}         @ Push the related Regs in stack
    initialize_r1_to_r6_local   @ Initialization for stressing the changes

    store_r1_to_r6_local 0  @ Store the registers before operations

    ldr     r1, =0xEE
    ldr     r2, =0xBEEF
    ldr     r3, =0xDEADBEEF
    ldr     r4, =mp_various_pseudo_ldr_s

    store_r1_to_r6_local 24 @ Store the registers after operations
    pop     {r4-r6, pc}     @ Restore the values of Regs and return


@ void mp_init_mem_block_c1(uint8_t *pArr, int n) {
@     for (int i = 0; i < n; i++) {
@         *pArr++ = 0x70 + (i << 1);
@     }
@ }

@ void mp_init_mem_block_s1(uint8_t *pArr, int n);
@   Input:
@     * pArr -> r0  The pointer to uint8_t
@     * n -> r1     The number of bytes to initialize
@   Output:
@     * None
@   Other registers:
@     * i -> r2, 0x70 -> r3
@     * (0x70 + (i << 1)) -> r4

mp_init_mem_block_s1:
    push    {r4, lr}
    ldr     r2, =0      @ i = 0;
    ldr     r3, =0x70

mpmp_init_mem_block_s1_loop:
    cmp     r2, r1
    bge     mpmp_init_mem_block_s1_end
    add     r4, r3, r2, lsl #1
    strb    r4, [r0], #1        @ We can change the pointer
    add     r2, #1
    b       mpmp_init_mem_block_s1_loop

mpmp_init_mem_block_s1_end:
    pop     {r4, pc}


@ void mp_init_mem_block_c2(uint8_t *const pArr, int n) {
@     for (int i = 0; i < n; i++) {
@         *(pArr + i) = 0x71 + (i << 1);
@     }
@ }

@ void mp_init_mem_block_s2(uint8_t *const pArr, int n);
@   Input:
@     * pArr -> r0  The pointer to uint8_t
@     * n -> r1     The number of bytes to initialize
@   Output:
@     * None
@   Other registers:
@     * i -> r2, 0x71 -> r3
@     * (0x71 + (i << 1)) -> r4

mp_init_mem_block_s2:
    push    {r4, lr}
    ldr     r2, =0      @ i = 0;
    ldr     r3, =0x71

mpmp_init_mem_block_s2_loop:
    cmp     r2, r1
    bge     mpmp_init_mem_block_s2_end
    add     r4, r3, r2, lsl #1
    strb    r4, [r0, r2]        @ We can use an index variable
    add     r2, #1
    b       mpmp_init_mem_block_s2_loop

mpmp_init_mem_block_s2_end:
    pop     {r4, pc}


@ int mp_array_abs_sum_var_ptr_s(int *pArr, int n)
mp_array_abs_sum_var_ptr_s:
    push    {r4, lr}
    ldr     r2, =0   @ sum = 0
    ldr     r3, =0   @ i = 0

mp_array_abs_sum_var_ptr_s_loop:
    cmp     r3, r1
    bge     mp_array_abs_sum_var_ptr_s_loop_end
    ldr     r4, [r0], #4           @ temp = *pArr++
    cmp     r4, #0                 @ temp < 0 ?
    bge     mp_array_abs_sum_var_ptr_s_loop_sum
    rsb     r4, r4, #0             @ temp = -temp
mp_array_abs_sum_var_ptr_s_loop_sum:
    add     r2, r2, r4             @ sum += temp
    add     r3, r3, #1             @ i++
    b       mp_array_abs_sum_var_ptr_s_loop

mp_array_abs_sum_var_ptr_s_loop_end:
    mov     r0, r2                 @ return sum
    pop     {r4, pc}               @ return sum


mp_array_abs_sum_cst_ptr_s:
    push    {r4, lr}
    ldr     r2, =0
    ldr     r3, =0

mp_array_abs_sum_cst_ptr_s_loop:
    cmp     r3, r1
    bge     mp_array_abs_sum_cst_ptr_s_loop_end
    ldr     r4, [r0, r3, lsl #2]       @ temp = *(pArr+i)
    cmp     r4, #0
    bge     mp_array_abs_sum_cst_ptr_s_loop_sum
    rsb     r4, r4, #0
mp_array_abs_sum_cst_ptr_s_loop_sum:
    add     r2, r2, r4
    add     r3, r3, #1
    b       mp_array_abs_sum_cst_ptr_s_loop

mp_array_abs_sum_cst_ptr_s_loop_end:
    mov     r0, r2
    pop     {r4, pc}


@ int mp_array_pos_sum_cst_ptr_s(int *const pArr, int n)
@   Sum only the positive (>= 0) elements of pArr[0..n-1].
@   Skips negatives entirely (no rsb / no add).
mp_array_pos_sum_cst_ptr_s:
    push    {r4, lr}
    ldr     r2, =0                      @ sum = 0
    ldr     r3, =0                      @ i = 0

mp_array_pos_sum_cst_ptr_s_loop:
    cmp     r3, r1                      @ i < n ?
    bge     mp_array_pos_sum_cst_ptr_s_loop_end
    ldr     r4, [r0, r3, lsl #2]        @ temp = *(pArr + i)
    cmp     r4, #0                      @ temp < 0 ?
    blt     mp_array_pos_sum_cst_ptr_s_loop_next   @ skip negatives
    add     r2, r2, r4                  @ sum += temp
mp_array_pos_sum_cst_ptr_s_loop_next:
    add     r3, r3, #1                  @ i++
    b       mp_array_pos_sum_cst_ptr_s_loop

mp_array_pos_sum_cst_ptr_s_loop_end:
    mov     r0, r2                      @ return sum
    pop     {r4, pc}


    .end
