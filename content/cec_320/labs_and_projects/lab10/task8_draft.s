@ Lab 10 Task 8 — DRAFT template for mp_array_pos_sum_cst_ptr_s
@
@ ⚠️ THIS IS A PLACEHOLDER. The exact register usage, label naming, and
@ instruction style MUST match the existing mp_array_abs_sum_cst_ptr_s in
@ ge1s_more_ldr_n_str_n_mov_sfns.s. The base project zip was not on disk
@ when this draft was written, so the LLM could not read the original.
@
@ Once the human places ge1s_more_ldr_n_str_n_mov.zip in lab10/ and asks
@ the LLM to continue, the LLM should:
@   1. Read the real mp_array_abs_sum_cst_ptr_s
@   2. Copy/paste it exactly as the manual instructs ("copy and rename")
@   3. Replace the negative-handling branch — instead of negating the value
@      and adding, simply skip the add when the element is negative.
@   4. Append .weak / .type / .global declarations at the top of the file
@      mirroring the existing _abs_sum declarations.
@
@ Sketch of what the new function should look like (typical Cortex-M4 style):
@
@ Assumed signature (verify against the real header):
@   int32_t mp_array_pos_sum_cst_ptr_s(const int32_t *arr, int n);
@   r0 = arr (in), r1 = n (in), r0 = sum (out)
@
@ Approach: walk the array via a const pointer, compare each element to 0,
@ branch past the add when the element is negative, otherwise accumulate.

    .section .text
    .syntax unified
    .align

    .global mp_array_pos_sum_cst_ptr_s
    .type   mp_array_pos_sum_cst_ptr_s, %function

@ int32_t mp_array_pos_sum_cst_ptr_s(const int32_t *arr, int n)
@   Input:
@     * arr -> r0 (const ptr; do not modify the caller's array)
@     * n   -> r1
@   Output:
@     * sum -> r0
@   Local:
@     * r2 = sum accumulator
@     * r3 = loop index i
@     * r4 = current element (callee-saved → push)
mp_array_pos_sum_cst_ptr_s:
    push    {r4, lr}
    mov     r2, #0                  @ sum = 0
    mov     r3, #0                  @ i = 0
loop_pos_sum:
    cmp     r3, r1                  @ i < n ?
    bge     end_pos_sum             @ exit when i >= n
    ldr     r4, [r0, r3, lsl #2]    @ r4 = arr[i] (4-byte stride)
    cmp     r4, #0                  @ test sign
    blt     skip_neg                @ if negative, skip the add
    add     r2, r2, r4              @ sum += arr[i]
skip_neg:
    add     r3, r3, #1              @ i++
    b       loop_pos_sum
end_pos_sum:
    mov     r0, r2                  @ return sum
    pop     {r4, pc}

    .end
