    .section .text
    .syntax unified
    
    .align

    .global task1_func_s
    .type   task1_func_s, %function

    .global task3_func_s
    .type   task3_func_s, %function


@ Convert a big endian word to a little endian one
@ void task1_func_s(uint32_t *x) 
@   Regs: *x -> r0; temp -> r1
task1_func_s:
    ldr     r1, [r0] 
    strb    r1, [r0, #3]
    lsr     r1, r1, #8
    strb    r1, [r0, #2]
    lsr     r1, r1, #8
    strb    r1, [r0, #1]
    lsr     r1, r1, #8
    strb    r1, [r0, #0]
    bx      lr 


@ Write an assembly function to copy a source string to a destination one 
@ by exploring the ending 0 of the source which has to be copied to the 
@ destination. 
@
@ void task3_func_s(char *src, char *dst);
@   Regs: *src -> r0; *dst -> r1, ch -> r2
task3_func_s:
task3_func_s_loop:
    ldrb    r2, [r0], #1           @ ch = *src++
    strb    r2, [r1], #1           @ *dst++ = ch
    cmp     r2, #0                 @ ch == '\0' ?
    bne     task3_func_s_loop      @ if not null, continue
    bx      lr

    .end
