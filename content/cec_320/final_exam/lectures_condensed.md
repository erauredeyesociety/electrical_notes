# CEC 320 Final Exam — Lectures 14-27 Condensed Highlights

Ultra-tight per-lecture recall bullets. Skips material heavily covered in quiz 4 cheatsheet (LDR/STR matrix, IT blocks, PL/NL/CEX, loops).

---

### Lctr 14 — Mixed C and ASM Programming
- EABI: R0-R3 pass args + return (caller-saved, not preserved); R4-R11 callee-saved (push/pop if used).
- 64-bit arg/return: lower word in R0, upper word in R1 (little-endian).
- Stack = Full Descending: SP points to last pushed item; push decrements SP by 4 per word.
- Multi-register push stores low-numbered regs at LOW addresses regardless of brace order.
- Return: `bx lr` if LR not stacked; `pop {pc}` if LR was pushed (equivalent to `pop {lr}` + `bx lr`).

### Lctr 15 — Arithmetic Instructions
- `ADD/SUB/RSB` (no S) don't touch flags; `ADDS/SUBS` update NZCV. `RSB` exists because Rn must be register.
- `ADC Rn, Op2`: Rn + Op2 + C; `SBC Rn, Op2`: Rn - Op2 + C - 1 (C=1 means no-borrow).
- 64-bit add idiom: `adds r0,r2` / `adc r1,r3` (low word sets C, high word consumes it).
- `MUL/MLA/MLS` (32-bit) — signed/unsigned identical in low 32 bits. `UMULL/SMULL/UMLAL/SMLAL` for 64-bit.
- `UDIV` vs `SDIV` differ; no S version, non-constant cycles. Modulo: `udiv r2,r0,r1` / `mls r0,r1,r2,r0`.

### Lctr 16 — Shift, Rotation, Op2, Q31
- `LSL` both signed/unsigned; `LSR` unsigned-only (0 fill); `ASR` signed-only (sign-bit repeat). Last bit out -> C.
- Op2 three forms: `#imm`, `Rm`, or `Rm, LSL/LSR/ASR #n` (barrel shifter, free with arithmetic).
- When Op2 uses shifted reg, destination canNOT be omitted even if same as Rn.
- Q31 accurate mul (3 instr best): `smull r1,r0,r0,r1` / `lsl r0,#1` / `add r0,r0,r1,lsr #31`.
- Fast Q31 scaling by (2^n+/-1)/2^n via Op2: `add r0,r0,r0,asr #2` = 5/4; `sub r0,r0,r0,asr #3` = 7/8.

### Lctr 17 — Bitwise Logic Instructions
- `MVN` (~), `AND`, `ORR` (|), `EOR` (^). Two with no C equivalent: `BIC Rn,Op2` = Rn & ~Op2; `ORN` = Rn | ~Op2.
- Bit-field: `BFC Rd,#s,#w` clears w bits at pos s; `BFI Rd,Rn,#s,#w` inserts w LSBs of Rn at s.
- Clear bit N idiom: shift 1 by N into mask, then `bic r0, mask` (BIC = AND with NOT).
- Read APSR flag: `MRS r0, apsr` -> special-reg to GP reg; write with `MSR apsr_nzcvq, Rn`.
- Assign bit-field v: build mask `(1<<w)-1 << s`, `bic` target, shift v to pos, `and` with mask, `orr` in.

### Lctr 18 — ARM Processor Status Flags (NZCV)
- N = MSB(result); Z = (result==0); C = unsigned carry/no-borrow; V = signed overflow. Same HW, dual interp.
- Processor doesn't know signed vs unsigned — it always updates BOTH C and V; programmer picks which to trust.
- Unsigned uses {C,N,Z}; signed uses {V,N,Z}.
- C flag on SUB: C=1 if no borrow (Rn >= Op2), C=0 if borrow. (Inverse of intuitive "borrow" naming.)
- N-bit verification trick: shift operands by (32-N), do ADDS, shift back with ASR, read APSR via MRS.

### Lctr 19 — CCS and Conditional Branch
- `CMP Rn, Op2` = SUB without writeback; sets NZCV. `CMN` = add-form (used for `cmp Rn, #-imm`).
- Signed CCS: EQ/NE/GT/GE/LT/LE. Unsigned: EQ/NE/HI/HS(CS)/LO(CC)/LS.
- `HS`=`CS` (C set = unsigned >=); `LO`=`CC` (C clear = unsigned <).
- Rule: signed operands -> signed CCS + ASR for /; unsigned -> unsigned CCS + LSR.
- `cmp r0, #-5` assembled as `CMN r0, #5`; signed CCSs still behave correctly.

### Lctr 20 — Immediate-Offset LDR/STR
- Mnemonic memory aid: `[Ra,#os]` no update; `[Ra,#os]!` update BEFORE (urgent bang); `[Ra],#os` update AFTER.
- LOAD size suffixes: none (word), B (u8), SB (i8), H (u16), SH (i16). STORE has NO sign variant.
- C-to-ASM: `*p++` = post-index; `*++p` = pre-index; `*(p+k)` = basic offset (k * sizeof(elem)).
- STRB stores only low byte of Rv; upper bits ignored (why no signed variant needed).
- Valid offsets typically +/-4095 for word LDR/STR; byte/halfword +/-255 on some forms.

### Lctr 21 — Register-Offset LDR/STR + MOV
- Register-offset: `LDR Rv, [Ra, Ri, LSL #n]` with n=log2(elem size) -> word=2, half=1, byte=0.
- NO writeback form for register-offset (only immediate-offset supports `!` or trailing `#os`).
- Two array iteration idioms: post-index advances pointer; register-offset leaves Ra constant, increments Ri.
- `MOV`: small immediate only; `MOVW` loads 16-bit low; `MOVT` loads 16-bit high (upper halfword).
- Pseudo `LDR Rd, =expr` -> assembler picks MOV / MOVW / literal-pool PC-relative load based on size.

### Lctr 22 — Increment Operations (vars + pointers)
- C precedence trap: postfix `++` is level 1 (LTR, highest); prefix `++`, `*`, `&`, cast all level 2 (RTL).
- `*p++` = deref old p, then p advances; `*++p` = advance p, then deref new.
- `++*p` = load val, add 1, store back (value++, NOT pointer). `++*p++`: post-inc p, but modify mem at OLD addr via `[r0,#-1]`.
- Pointer arithmetic scales by sizeof(elem): p8++ +1, p16++ +2, p32++ +4. Diff on typed ptr -> elements.
- `B[i] = A[i++]++;` is undefined behavior (unsequenced modification of i). Split or use comma operator.

### Lctr 23 — Calling ASM Functions from ASM
- Leaf fn: never BLs another -> `bx lr` suffices, no LR push needed.
- Stem fn: calls another -> MUST `push {lr}` (BL overwrites LR) and `pop {pc}` to return.
- `LDRD Rv_L, Rv_H, [Ra,#os]` loads 8 bytes: low word at low addr, high word at high addr (little-endian).
- NO register-offset form for LDRD/STRD (only basic, pre-, post-index).
- Prep args by type: int32->LDR, int16->LDRSH, uint16->LDRH, int8->LDRSB, uint8->LDRB, int64->LDRD.

### Lctr 24 — Combination Branching + Conditional Execution
- `CBZ Rn, label` / `CBNZ Rn, label`: FORWARD only (~126 byte range), Rn in R0-R7, does NOT read/set flags.
- CBZ/CBNZ perfect after `ldrb` for null-terminator test (loaded byte is flag-neutral).
- IT block = up to 4 conditional instr sharing one cond. Forms: IT, ITT, ITE, ITTT, ITTE, ITEE, ITTEE, ITTTT.
- First IT slot is ALWAYS T (matches cond); later slots T (same) or E (inverse). Instr inside needs explicit CCS.
- Hard bans: CBZ/CBNZ inside IT block (forbidden); conditional branch only in LAST IT slot.

### Lctr 25 — Selection Control (if / if-else / compound)
- PL (positive logic): same-CCS branch to `_then`; else-block laid FIRST. Code reads "backward" from C.
- NL (negative logic): inverse-CCS branch to `_else`; then-block FIRST. Reads closer to C source order.
- if-else-if: chain of CMP + NL-branch exiting each arm; `b end` at arm end to skip remaining cases.
- Compound OR: short-circuit with double CMP -> both tests branch to shared `_then`, fall-through = else.
- Compound AND (De Morgan): both CMPs branch to `_else` on failure; fall-through = then.

### Lctr 26 — C Loops in ASM
- Labels: `<fn>_lp` (top) and `<fn>_end` (exit). `for` and `while` top-tested (0+ iters); `do-while` bottom-tested (>=1 iter).
- `while` common form: test at top with NL-branch to _end, body, update, `b lp`.
- `while` late-check: jump over body on entry, test at bottom — saves one branch per iteration.
- `while` CEX form: `cmp` + `it cond` + conditional B as last slot inside IT (the only conditional-branch-in-IT pattern).
- Priming-read pattern: `ldrb` before loop + `ldrb` inside loop — duplication that Lctr 27's `while(1)+break` eliminates.

### Lctr 27 — Complex Flow (break, continue, switch)
- `break` = forward `b <loop_end>` (or CBZ/CBNZ to end on a value test).
- `continue` in while/do-while = branch to condition test; in `for` = branch to UPDATE expr (so i++ still runs!).
- `while(1) { ...; if(cond) break; }` removes priming-read duplication — single `ldrb` inside loop.
- Switch naive: CMP/BEQ ladder, stacked case labels for fall-through (no code between = fall through).
- `ADR Rd, label` = PC-relative addr load (position-independent). `TBB [Rn, Rm]` jumps `PC = PC+4+2*table[Rm]`; table bytes are `(case_X - first_case)/2` (divided by 2 because Thumb-2 halfword-aligned).
