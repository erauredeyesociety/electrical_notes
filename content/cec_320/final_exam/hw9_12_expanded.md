# HW 9-12 Expanded (Final Exam Cheatsheet Addendum)

Complements `hw_solutions_summary.md` with per-part traces/annotations.

---

## HW 9 P1 — Full R4 trace

| Line | ASM | Addr loaded | R4 after | Rn after |
|------|-----|-------------|----------|----------|
| 1 | `ldr r4, =0x20000000` | — | 0x20000000 | — |
| 2 | `ldr r0, [r4, #4]` | 0x20000004 | unchanged | R0=0x07060504 |
| 3 | `ldr r1, [r4, #2]!` | 0x20000002 | 0x20000002 | R1=0x05040302 |
| 4 | `ldr r2, [r4], #4` | 0x20000002 | 0x20000006 | R2=0x05040302 |
| 5 | `ldr r3, [r4]` | 0x20000006 | unchanged | R3=0x09080706 |

Pre-index loads from NEW R4; post-index from OLD R4.

## HW 9 P2 — Two prototypes

- `mp_task1(int16_t*, int32_t*)`: LDRSH post-index `#4` skips every OTHER halfword, sign-extends.
- `mp_task2(uint16_t*, int32_t*)`: LDRH pre-index `#2` reads consecutive halfwords starting at idx 1, zero-extends.

Stride `#4` vs `#2` combined with pre/post gives very different patterns.

## HW 9 P3 — Four tasks, BEFORE → AFTER register state

Entry: R0=0x20001010 (ipt), R1=0x20001040 (opt). Words: ipt+0=0x30201000, +4=0x70605040, +8=0xB0A09080, +12=0xF0E0D0C0.

**T1: basic offset (R0 unchanged).** `ldr r2,[r0,#4]`→0x70605040; `ldr r2,[r0,#0xC]`→0xF0E0D0C0. After: R0=0x20001010, R2=0xF0E0D0C0.

**T2: pre-index `#4`! x2.** `ldr r2,[r0,#4]!` (R0=0x...14, r2=0x70605040); `ldr r2,[r0,#4]!` (R0=0x...18, r2=0xB0A09080). After: R0=0x20001018, R2=0xB0A09080.

**T3: post-index `#4` x2.** `ldr r2,[r0],#4` (r2=0x30201000, R0→0x...14); `ldr r2,[r0],#4` (r2=0x70605040, R0→0x...18). After: R0=0x20001018, R2=0x70605040.

**T4: register-offset (r2=1 at entry).**
```asm
ldr r3, [r0, r2, lsl #2]   @ ipt+4, r3=0x70605040
add r2, #1                  @ r2=2
ldr r3, [r0, r2, lsl #2]   @ ipt+8, r3=0xB0A09080
add r2, #1                  @ r2=3
```
Before→After: R0=0x20001010 (unchanged), R2 1→3, R3=0xB0A09080. `[Rb,Ri,LSL #n]` = typed array index with `n=log2(elem_size)`.

---

## HW 10 P1 — Full 4-line trace

Array: `uint8_t my_arr[i]=2*i` at 0x20000100. `p8a=0x20000100`, `p8b=0x2000010C`.

| Line | RHS | Mem change | p8a after | p8b after |
|------|-----|------------|-----------|-----------|
| 4: `*p8b++=*(p8a+2)` | read 0x102→0x04 | 0x10C ← 0x04 | 0x100 | 0x10D |
| 5: `*p8b++=++*(p8a+4)` | read 0x104=0x08, inc→0x09, writeback | 0x104: 0x08→0x09; 0x10D ← 0x09 | 0x100 | 0x10E |
| 6: `*p8b++=++*p8a++` | read 0x100=0x00 (old), inc→0x01, writeback to 0x100 | 0x100: 0x00→0x01; 0x10E ← 0x01 | 0x101 | 0x10F |
| 7: `*p8b++=*p8a++` | read 0x101→0x02 | 0x10F ← 0x02 | 0x102 | 0x110 |

**Line 6 ASM (trickiest):**
```asm
ldrb r2, [r0], #1     @ r2=*p8a, R0 advances
add  r2, r2, #1
strb r2, [r0, #-1]    @ writeback to OLD p8a
strb r2, [r1], #1
```

Postfix-on-ptr + prefix-on-value: post-index LDRB then STRB `#-1` to hit original address. `++*(p+k)` needs explicit STRB writeback.

## HW 10 P2 — Four tasks, full LDRD/LDRSB/LDRSH

Same `ipt[i]=i<<4`. Entry R0=0x20001010, R1=0x20001040.

**T1 LDRD pre-index (8 bytes → 2 regs).** `ldrd r2,r3,[r0,#8]!` sets R0=0x...18, r2=word@ipt+8=0xB0A09080, r3=word@ipt+12=0xF0E0D0C0.

**T2 LDRSB pre-index (sign-extend!).** `ldrsb r2,[r0,#4]!` → R0=0x...14, byte@ipt+4=0x40 (bit7=0) → r2=0x00000040. `ldrsb r3,[r0,#4]!` → R0=0x...18, byte@ipt+8=0x80 (bit7=1) → r3=0xFFFFFF80.

**T3 LDRSH post-index, odd stride.** `ldrsh r2,[r0],#10` → hw@ipt+0=0x1000 → r2=0x00001000, R0+=10. `ldrsh r3,[r0],#4` → hw@ipt+10=0xB0A0 (bit15=1) → r3=0xFFFFB0A0, R0+=4. After R0=0x2000101E (unaligned!).

**T4 LDRH register-offset (zero-extend).** `ldrh r3,[r0,r2,LSL #1]` with r2=1 → ipt+2, r3=0x00003020; bump r2→2, reload → r3=0x00005040; bump r2→3.

Sign bits: 0x80 (byte)/0x8000 (hw). LSL#n: #1 hw, #2 word, #3 dword.

---

## HW 11 P1 — `x_cmp_y_load` three forms

C: `if (x>y) return (int32_t)*(++ptrA)*2; else return *(ptrB++)/2;` (signed x,y; int16_t *ptrA; int32_t *ptrB)

R0=x, R1=y, R2=ptrA, R3=ptrB. Then: `ldrsh r0,[r2,#2]!` + `lsl #1`. Else: `ldr r0,[r3],#4` + `asr #1` (signed).

**PL (BGT matches C; else first):** `cmp r0,r1` / `bgt then` / *else block (ldr+asr)* / `b end` / *then block (ldrsh+lsl)* / `end: bx lr`

**NL (BLE inverse; then first — reads like C):** `cmp r0,r1` / `ble else_` / *then block* / `b end` / *else block* / `end: bx lr`

**CEX (ITTEE le — no branches):**
```asm
    cmp r0, r1
    ittee le
    ldrle   r0, [r3], #4      @ T: else
    asrle   r0, r0, #1        @ T
    ldrshgt r0, [r2, #2]!     @ E: then
    lslgt   r0, r0, #1        @ E
    bx lr
```
CCS in `IT..` = NL cond; T match, E inverse. Conditional pre/post-idx LDRs legal in IT.

## HW 11 P2 — `mathf` piecewise (-10/+10/2x)

`f(x) = -10 if x<-5; +10 if x>=5; 2x otherwise.`

### C
```c
if (x < -5) y = -10;
else if (x >= 5) y = 10;
else y = 2*x;
```

### CMP chain
```asm
    cmp r0, #-5           @ assembled as CMN r0, #5
    bge elseif
    ldr r0, =-10
    b   end
elseif:
    cmp r0, #5
    blt else_
    ldr r0, =10
    b   end
else_:
    lsl r0, r0, #1
end: bx lr
```

### CEX (chained ITT + ITE; stash in R1 to preserve x)
```asm
    cmp r0, #-5
    itt lt
    ldrlt r1, =-10        @ T1
    blt   end             @ T2: conditional B — LEGAL only as last IT slot
    cmp r0, #5
    ite ge
    ldrge r1, =10         @ T
    lsllt r1, r0, #1      @ E: 2*x (uses original x in r0)
end: mov r0, r1
     bx lr
```

Conditional B allowed ONLY as last IT slot. Stage result in R1 so R0 (=x) survives 2nd CMP.

## HW 11 P3 — Compound OR `x<=20 || x>=25`

C: `if (x<=20 || x>=25) return (int32_t)*++ptrA*4; else return *++ptrB/4;` (signed x; uint16_t *ptrA; uint32_t *ptrB → LSR not ASR!)

R0=x, R1=ptrA, R2=ptrB. Then: `ldrh r0,[r1,#2]!` + `lsl #2`. Else: `ldr r0,[r2,#4]!` + `lsr #2`.

### CMP short-circuit (both sub-tests → same _then)
```asm
    cmp r0, #20
    ble then        @ 1st OR true
    cmp r0, #25
    bge then        @ 2nd OR true
    b   else_       @ both false
then:  ldrh r0, [r1, #2]!
       lsl  r0, r0, #2
       b    end
else_: ldr  r0, [r2, #4]!
       lsr  r0, r0, #2
end:   bx lr
```

### CEX (1st test = plain BGT; 2nd = full ITTEE)
```asm
    cmp r0, #20
    bgt check25       @ 1st sub-test can't sit in IT (cond B only at end)
    ldrh r0, [r1, #2]!    @ x<=20 → then
    lsl  r0, r0, #2
    bx   lr
check25:
    cmp r0, #25
    ittee ge
    ldrhge  r0, [r1, #2]!    @ T: then
    lslge   r0, r0, #2       @ T
    ldrlt   r0, [r2, #4]!    @ E: else
    lsrlt   r0, r0, #2       @ E
    bx lr
```

Unsigned `/4` on uint32_t → LSR. 1st of 2 OR sub-tests must be plain branch; only final fan-out packs into ITTEE.

---

## HW 12 P1 — Swap last 2 of each trio

Walks 3 chars at a time; if all non-null, swap at (i+1,i+2). Return trios swapped.

```c
int mp_swap_last_2_chars_in_3_in_str_c(char *str) {
    int n = 0;
    while (1) {
        char c1=*str++; if (!c1) break;
        char c2=*str++; if (!c2) break;
        char c3=*str++; if (!c3) break;
        *(str-2)=c3; *(str-1)=c2; n++;
    }
    return n;
}
```

ASM (R12 accumulator avoids push/pop):
```asm
    mov r12, #0
lp: ldrb r1, [r0], #1
    cbz  r1, end
    ldrb r2, [r0], #1
    cbz  r2, end
    ldrb r3, [r0], #1
    cbz  r3, end
    strb r3, [r0, #-2]     @ after 3 post-inc LDRBs, 2nd/3rd live at -2/-1
    strb r2, [r0, #-1]
    add  r12, r12, #1
    b    lp
end: mov r0, r12
     bx  lr
```

Test: `"hellow"`→`"hlelwo"`,ret 2. `"hello"`→`"hlelo"`,ret 1 (2nd pass l,o,\0 breaks). CBZ on fresh byte beats CMP+BEQ; CBZ illegal inside IT. R12 (IP) scratch under AAPCS.

## HW 12 P2 — lowercase→uppercase, two forms

Given C (priming + duplicate in-loop read):
```c
void mp_str_cpy_2_caps_while_c(char *dst, char *src) {
    char ch = *src++;
    while (ch) { ch -= 0x20; *dst++ = ch; ch = *src++; }
    *dst++ = ch;               // writes '\0'
}
```

**Part 1 ASM (while — two LDRB texts):**
```asm
    ldrb r2, [r1], #1            @ priming
lp: cbz  r2, end
    sub  r2, r2, #0x20
    strb r2, [r0], #1
    ldrb r2, [r1], #1            @ update (duplicate)
    b    lp
end: strb r2, [r0], #1            @ '\0' (r2=0 via CBZ)
     bx   lr
```

**Part 2 C refactored (while(1)+break):**
```c
while (1) {
    char ch = *src++;
    if (ch == 0) { *dst++ = ch; break; }
    ch -= 0x20; *dst++ = ch;
}
```

**Part 3 ASM (single LDRB text):**
```asm
lp: ldrb r2, [r1], #1
    cbz  r2, end                  @ deferred '\0' at end
    sub  r2, r2, #0x20
    strb r2, [r0], #1
    b    lp
end: strb r2, [r0], #1            @ '\0'
     bx   lr
```

Both: N+1 dynamic LDRB executions; refactor removes one source line. Terminator STRB at `_end` works because CBZ guarantees r2=0.

---

## Cross-cutting

- **Sign-ext:** LDRSB `0x80→0xFFFFFF80`; LDRSH `0x8000→0xFFFF8000`; LDRB/LDRH zero-extend.
- **Signed vs unsigned:** CCS (GT/LE vs HI/LS), shift (ASR vs LSR), load (SB/SH vs B/H).
- **IT rules:** max 4; CCS = NL cond; T match, E inverse; cond B only last slot; no CBZ inside.
- **Pre-idx `!`=`*++p`; post-idx `,#n`=`*p++`.** Both OK in IT.
- **Scratch:** R0-R3, R12 caller-saved — use R12 as loop accumulator to skip push/pop.
