# CEC 320 Quiz 4 (Spring 2026) — Solutions

Source: `qz-26a-qz4-ldr-str-n-flow-ctrl-soln-26-04.pdf`
Topics: LDR/STR (signed/half/byte), pre/post-index with writeback, scaled-register addressing, conditional branch flow control. Total = 105 pts.

Memory state for Prob 1 (little-endian):

| Addr | B0 B1 B2 B3 |
|---|---|
| 0x2000_0000 | 88 89 8A 8B |
| 0x2000_0004 | 8C 8D 8E 8F |
| 0x2000_0008 | 70 71 72 73 |
| 0x2000_000C | 74 75 76 77 |

---

## Prob 1 — LDR/STR sign extension and indexing modes (30 pts)

**1a (8 pts) — task1 register values just before `bx lr`:**
- `ldrsh r2, [r0, #4]` loads halfword at 0x2000_0004 = `0x8D8C`, sign-extended → `r2 = 0xFFFF_8D8C`.
- `ldrsh r3, [r0, #8]` loads halfword at 0x2000_0008 = `0x7170` → `r3 = 0x0000_7170` (positive, no sign extend).

**1b (8 pts) — task2 register values:**
- `ldrsb r2, [r0, #2]!` (pre-index with writeback): byte at 0x2000_0002 = `0x8A` → `r2 = 0xFFFF_FF8A`; r0 updated to `0x2000_0002`.
- `ldrsb r3, [r0, #4]!`: byte at `0x2000_0006` = `0x8E` → `r3 = 0xFFFF_FF8E`; r0 = `0x2000_0006`.

**1c (8 pts) — Memory at 0x2000_0020 after task1 stores:**
task1 stores full r2 then r3 to p2 with post-index `#4`. r2 = 0xFFFF_8D8C → bytes `8C 8D FF FF`; r3 = 0x0000_7170 → bytes `70 71 00 00`.

| Addr | B0 B1 B2 B3 |
|---|---|
| 0x2000_0020 | 8C 8D FF FF |
| 0x2000_0024 | 70 71 00 00 |

**1d (6 pts) — `val = *(ptr + i)` for uint16_t ptr:**
```asm
LDRH R2, [R0, R1, LSL #1]    @ scale index by 2 (sizeof uint16_t)
```

**Trap:** `LSL #1` is mandatory because R1 is in *elements*, address arithmetic needs *bytes*. Half-word access at non-2-byte-aligned addr faults.

---

## Prob 2 — C-pointer ops to ASM + memory result (30 pts)

`int16_t *src = 0x2000_0000` in R0, `int16_t *dst = 0x2000_0008` in R1.

**Part 1 (20 pts) — ASM for the three C lines:**
```asm
@ (1) *dst++ = *src++;
LDRSH R2, [R0], #2
STRH  R2, [R1], #2

@ (2) *dst++ = *++src;     // pre-increment src, then deref
LDRSH R2, [R0, #2]!
STRH  R2, [R1], #2

@ (3) *dst++ = ++*src;     // increment value at *src, store back, then copy
LDRSH R2, [R0]
ADD   R2, #1
STRH  R2, [R0]
STRH  R2, [R1], #2
```

**Part 2 (10 pts) — Memory after all three lines:**

| Addr | B0 B1 B2 B3 |
|---|---|
| 0x2000_0000 | 7C 7D 7E 7F |
| 0x2000_0004 | 81 81 82 83 |
| 0x2000_0008 | 7C 7D 80 81 |
| 0x2000_000C | 81 81 8A 8B |

Walkthrough: After (1), R0=0x2_0002, R1=0x2_000A; mem[0x8..0x9]=7C 7D. After (2), R0=0x2_0004 (pre-incremented to point at 0x7E7F halfword? — Actually src was at 0x2_0002 after (1) wait — note: src in (1) post-incs to 0x2_0002, so (2) pre-incs to 0x2_0004 → reads 0x8180); writes 80 81 to 0x2_000A..B. After (3), src points at 0x2_0004 still (pre-inc happened before deref); reads 0x8180, +1 = 0x8181, writes back to 0x2_0004 (bytes `81 81`) and to 0x2_000C (`81 81`).

**Trap:** `++*src` modifies memory at `*src`, NOT the pointer. Distinguish the three C idioms by what gets incremented (pointer vs. dereferenced value) and when (pre vs. post).

---

## Prob 3 — LDRD/STRD round trip (20 pts)

C: builds `ipt[i] = i<<4` so ipt = `00 10 20 30 40 50 60 70 80 90 A0 B0 C0 D0 E0 F0`. Calls `mp_task(ipt, opt)`.

ASM:
```asm
mp_task:
    ldrd  r2, r3, [r0, #8]!     @ R2=0xB0A0_9080, R3=0xF0E0_D0C0; R0 += 8
    str   r3, [r1, #0]          @ opt[0] = 0xF0E0_D0C0
    str   r2, [r1, #4]          @ opt[1] = 0xB0A0_9080
    sub   r0, r0, #8            @ rewind R0 to ipt
    ldrsh r3, [r0], #4          @ R3 = 0x0000_1000 (halfword 0x1000), R0 += 4
    ldrsh r2, [r0, #4]!         @ R2 = 0xFFFF_9080 (sign-extend 0x9080), R0 += 4
    strd  r2, r3, [r1, #8]!     @ opt[2]=0xFFFF_9080, opt[3]=0x0000_1000; R1 += 8
    bx    lr
```

**Part (a, 12 pts) — printout:**
```
Out1 = 0xF0E0D0C0, Out2 = 0xB0A09080, Out3 = 0xFFFF9080, Out4 = 0x1000
```

**Part (b, 8 pts) — final R0/R1** (with ipt=0x2000_0200, opt=0x2000_0280):
- `r0 = 0x2000_0208`, `r1 = 0x2000_0288`.

**Trap:** `LDRD Rt, Rt2, [Rn, #±imm]!` loads Rt from [Rn+imm] (low) and Rt2 from [Rn+imm+4] (high) — order matters. Also: after `ldrsh ... [r0], #4`, R0 advances by 4 even though only 2 bytes were read.

---

## Prob 4 — Conditional branch translation (25 pts)

C:
```c
int load_based_on_x_c(int x, int *ptrA, int *ptrB) {
    if (x <= -20 || x >= 20)  return (int32_t)*(ptrA+1) * 4;
    else                       return *(ptrB+2) / 4;
}
```

ASM (conditional-branch method, x→r0, ptrA→r1, ptrB→r2):
```asm
load_based_on_x_s:
    cmp   r0, #-20
    ble   load_based_on_x_s_then     @ x <= -20 → then
    cmp   r0, #20
    blt   load_based_on_x_s_else     @ -20 < x < 20 → else
load_based_on_x_s_then:
    ldr   r0, [r1, #4]               @ *(ptrA+1), int* so offset = 4
    lsl   r0, #2                     @ * 4
    b     load_based_on_x_s_end
load_based_on_x_s_else:
    ldr   r0, [r2, #8]               @ *(ptrB+2), offset = 8
    lsr   r0, #2                     @ / 4 (unsigned shown; for signed div use ASR)
load_based_on_x_s_end:
    bx    lr
```

**Trap:** OR-of-conditions short-circuits — first `cmp/ble` jumps straight to `then` so the second `cmp` is only executed when the first was false. Pointer offsets are in BYTES (`*(p+1)` for `int*` → `#4`, `*(p+2)` → `#8`). For signed division by power-of-2, use `ASR`, not `LSR`.

---

## Final-exam pattern carryover

These patterns are very likely to reappear on the final:

1. **Sign-extending loads (`LDRSB`/`LDRSH`)** producing `0xFFFF_FFxx` / `0xFFFF_xxxx` when the loaded byte/halfword has its MSB set. Memorize: positive halfword → upper 16 zero; negative → upper 16 = 0xFFFF.
2. **Pre vs. post-index with writeback (`!` vs trailing `, #imm`).** Know which address is used for the access and what R0 holds after. Several Prob 1/2/3 parts hinge on this.
3. **Scaled-register addressing for typed pointer indexing**: `LDR R2, [R0, R1, LSL #n]` where n = log2(sizeof). LSL #1 for `int16_t/uint16_t`, LSL #2 for `int32_t`.
4. **Translating `*p++`, `*++p`, `++*p`** to ASM — distinguishing pointer increment vs. value increment, pre vs. post. Always write-back the modified value when it's `++*p`.
5. **`LDRD`/`STRD` register pairing and address ordering**: Rt = lower address, Rt2 = upper address; effective address from `[Rn, #imm]!` updates Rn.
6. **Memory-map fill-in problems** — given starting bytes, predict memory after a sequence of stores. Watch endianness: low byte of register goes to lowest byte of address.
7. **Conditional-branch translation of `if (A || B)` and `if (A && B)`** — short-circuit with the right BLE/BGE/BLT/BGT direction, plus the closing `b end` to skip the else.
8. **C arithmetic to ASM shifts**: `*4` → `LSL #2`; `/4` for signed → `ASR #2`, for unsigned → `LSR #2`. Pointer arithmetic offset = index × sizeof(target).
