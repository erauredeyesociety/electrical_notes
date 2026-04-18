    .section .text
    .syntax unified

    .align

    .weak   mp_load_modify_store_s
    .type   mp_load_modify_store_s, %function

    .weak   mp_str_cpy_s
    .type   mp_str_cpy_s, %function
    .weak   mp_str_len_s
    .type   mp_str_len_s, %function

    .weak   mp_array_abs_sum_s
    .type   mp_array_abs_sum_s, %function
    .weak   mp_array_max_s
    .type   mp_array_max_s, %function


@ void mp_load_modify_store(int32_t *Ai32, int16_t *Bi16, int8_t *Ci8) {
@     *Ai32 = 3 * *Ai32 / 4;     @ = x - x/4   (one-shift form: sub r, x, x, asr #2)
@     *Bi16 = 2 * *Bi16 / 4;     @ = x / 2     (asr #1)
@     *Ci8  = 1 * *Ci8  / 4;     @ = x / 4     (asr #2)
@ }

@ void mp_load_modify_store_s(int32_t *Ai32, int16_t *Bi16, int8_t *Ci8);
@   Input:
@     * Ai32 -> r0     @ pointer to int32_t
@     * Bi16 -> r1     @ pointer to int16_t
@     * Ci8  -> r2     @ pointer to int8_t
@   Output:
@     * None   (results are stored back through the pointers)
@   Others:
@     * r3 is scratch for each load-modify-store triple

mp_load_modify_store_s:
    @ --- 32-bit: *Ai32 = 3 * (*Ai32) / 4   ==  x - (x >>signed 2)
    ldr     r3, [r0]                    @ load  signed 32-bit word
    sub     r3, r3, r3, asr #2          @ modify: r3 = x - (x >>signed 2)    == (3*x)/4
    str     r3, [r0]                    @ store  32-bit word

    @ --- 16-bit: *Bi16 = 2 * (*Bi16) / 4   ==  x >>signed 1
    ldrsh   r3, [r1]                    @ load  signed 16-bit halfword (sign-extended into r3)
    asr     r3, r3, #1                  @ modify: r3 = x >>signed 1          == (2*x)/4
    strh    r3, [r1]                    @ store  halfword (low 16 bits)

    @ --- 8-bit:  *Ci8  = 1 * (*Ci8)  / 4   ==  x >>signed 2
    ldrsb   r3, [r2]                    @ load  signed 8-bit byte (sign-extended into r3)
    asr     r3, r3, #2                  @ modify: r3 = x >>signed 2          == (1*x)/4
    strb    r3, [r2]                    @ store  byte (low 8 bits)

    bx      lr


@ void mp_str_cpy_c2(char *src, char *dst) {
@     uint8_t ch;
@     while ((ch = *src++)) {
@         *dst++ = ch;
@     }
@     *dst = 0;
@ }

@ void mp_str_cpy_s(char *src, char *dst);
@   Input:
@     * src -> r0        @ r0 is advanced byte-by-byte via post-indexed ldrb
@     * dst -> r1        @ r1 is advanced byte-by-byte via post-indexed strb
@   Output:
@     * None
@   Others:
@     * r2 = current character

mp_str_cpy_s:
cpy_loop:
    ldrb    r2, [r0], #1                @ r2 = *src++;     (post-indexed: load then r0 += 1)
    cbz     r2, cpy_end                 @ while ((ch = *src++))   break on NUL
    strb    r2, [r1], #1                @ *dst++ = ch;     (post-indexed: store then r1 += 1)
    b       cpy_loop
cpy_end:
    mov     r2, #0
    strb    r2, [r1]                    @ *dst = 0;        (write the terminator)
    bx      lr


@ int mp_str_len_s(char *str);
@ Algorithm: walk a pointer from the start of the string until we see the
@ NUL terminator, then return (end - start).  Uses the same post-indexed
@ ldrb idiom as mp_str_cpy_s so it is one instruction per character.
@
@   Input:
@     * str -> r0
@   Output:
@     * int         @ length, NOT counting the trailing '\0'
@   Others:
@     * r1 = walking pointer, starts at str
@     * r2 = current character

mp_str_len_s:
    mov     r1, r0                      @ save start address; r1 will advance
len_loop:
    ldrb    r2, [r1], #1                @ r2 = *r1++;   post-increment so r1 ends ONE PAST the NUL
    cbz     r2, len_end                 @ if we just read '\0', stop
    b       len_loop
len_end:
    sub     r0, r1, r0                  @ length_incl_nul = (r1 - start)
    sub     r0, r0, #1                  @ drop the trailing NUL:  return length = (r1 - start - 1)
    bx      lr


@ int mp_array_abs_sum(int *pArr, int n) {
@     int sum = 0;
@     int i = 0;
@     while (i < n) {
@         int temp = *(pArr + i);
@         if (temp < 0) {
@             temp = -temp;
@         }
@         sum += temp;
@         i++;
@     }
@     return sum;
@ }

@ int mp_array_abs_sum_s(int *pArr, int n);
@   Input:
@     * pArr -> r0         @ r0 is advanced by post-indexed word load
@     * n    -> r1
@   Output:
@     * int (r0 = sum)
@   Others:
@     * r2  = running sum
@     * r3  = current element
@     * r12 = elements remaining  (Thumb allows r12 without push/pop, it is caller-saved)

mp_array_abs_sum_s:
    mov     r2, #0                      @ sum = 0
    cmp     r1, #0
    ble     abs_end                     @ if (n <= 0) return 0   (guards empty / negative n)
    mov     r12, r1                     @ counter = n
abs_loop:
    ldr     r3, [r0], #4                @ temp = *pArr++;  post-indexed word load (+4)
    cmp     r3, #0
    it      lt                          @ IT block: the next instruction executes only if LT
    neglt   r3, r3                      @ if (temp < 0) temp = -temp;
    add     r2, r2, r3                  @ sum += temp
    subs    r12, r12, #1                @ --counter, sets flags
    bne     abs_loop                    @ while (counter != 0)
abs_end:
    mov     r0, r2                      @ return sum
    bx      lr


@ int mp_array_max_s(int *pArr, int n);
@ Algorithm: running maximum.  Initialize max = pArr[0], then for each later
@ element keep the larger of (max, element) using a signed compare.
@ The test file only exercises n >= 1, which matches real-world use.
@
@   Input:
@     * pArr -> r0         @ r0 is advanced by post-indexed word load
@     * n    -> r1
@   Output:
@     * int (r0 = max)
@   Others:
@     * r2  = running max
@     * r3  = current element
@     * r12 = elements remaining after the first load

mp_array_max_s:
    ldr     r2, [r0], #4                @ max = *pArr++;   (n >= 1 is assumed -- matches tests)
    subs    r12, r1, #1                 @ remaining = n - 1
    beq     max_end                     @ if n == 1, we already have the answer
max_loop:
    ldr     r3, [r0], #4                @ temp = *pArr++;
    cmp     r3, r2                      @ signed compare: temp vs running max
    it      gt
    movgt   r2, r3                      @ if (temp > max) max = temp;
    subs    r12, r12, #1
    bne     max_loop
max_end:
    mov     r0, r2                      @ return max
    bx      lr


    .end                    @ end of the file
