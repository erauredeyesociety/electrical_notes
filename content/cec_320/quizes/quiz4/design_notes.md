# Quiz 4 Cheatsheet — Design Notes

## v1 (`qz4_cheatsheet_v1.tex`)

- 3 columns, 8pt landscape letter, 0.3" margins
- Content = direct port of `qz4_cheatsheet.md`
- AAPCS table swapped from `tabularx` to itemize after two overflow fixes

## v2 (current `qz4_cheatsheet.tex`)

Target: **more HW examples, 2 pages total**.

Layout changes:

- **4 columns** via `multicols*`
- Margins tightened to 0.2in
- `\raggedcolumns` so uneven column balance is allowed (helps fit)
- Global `\scriptsize` inside multicols; code at `\scriptsize` ttfamily
- `titlesec` spacing pushed to minimum (3pt above section, 0.5pt below)
- Added `\ex{...}` macro for worked HW problems — small red "Ex." label

Content added (beyond v1):

- **New section "Sign-Extension Pitfalls"** (LDRSB/LDRSH traps from HW10 P2)
- HW9 P1 — full 5-line LDR trace (was only 2 bullets in v1)
- HW9 P2 both mp_task1 AND mp_task2 (v1 only had task1)
- HW10 P2 T1--T4 (v1 only mentioned T1 and T4)
- HW11 P1 all three parts (PL / NL / CEX) for same C function
- HW11 P2 P2 cascade AND P3 CEX-with-short-circuit
- HW11 P3 P1 (OR) AND P3 P2 (CEX)
- HW12 P1 full swap-last-2-of-3 ASM
- HW12 P2 P1 (plain while) AND P3 (while(1)+break) side-by-side

Known risks (can't verify — no LaTeX compiler locally):

- `extarticle` smallest size is 8pt; `\scriptsize` reduces to ~6pt but body stays 8pt.
- 4 landscape columns at letter with 0.2" margins ≈ 2.55" per column. Longest lstlisting lines (~40 chars at scriptsize ttfamily) should fit.
- "2 pages" is aspirational — may spill to 3. If it does, likely drops:
  1. **ASM Quick Ref section** (most redundant with LDR/STR Matrix)
  2. **while-using-CEX subsection** (rarely used pattern)
  3. HW9 P1 trace could shrink to 2 key lines instead of 5

## v3 additions (fill 2 remaining cols)

Mined `summaries/cec320-cls-note-collection (2).pdf` (and companion PDF) for reference material NOT already on the sheet. Added 9 new sections:

1. **Barrel Shifter / Op2** — three Op2 forms; GNU quirk (dest reg required); RRX; shifted-Op2 scaling idioms (`add r1,r0,r0,lsl #1 = 3*r0`) with signed-vs-unsigned rule (LSR→unsigned, ASR→signed, LSL→both).
2. **Flags & Flag-Setters** — APSR bit positions, S-suffix rule, MUL/DIV flag behavior, CMP/CMN/TST/TEQ table with "HiLow unSun" mnemonic, APSR read/write syntax.
3. **LDR Pseudo Resolution** — 8/16/32-bit dispatch to MOV.W / MOVW / literal pool; MOVW vs MOVT.
4. **More Bitwise / Multiply** — ORN, BIC, BFC, BFI, MUL/MLA/MLS, UMULL/SMULL, UDIV/SDIV.
5. **Registers & Exception** — low/high banking, xPSR parts, HW auto-stack of {R0–R3, R12, LR, PC, PSR}.
6. **Directives & File Header** — canonical `.section .text / .syntax unified / .thumb / .global / .type %function` skeleton plus `.word / .byte / .asciz / .weak / .thumb_set`.
7. **Instructor Idioms / Style** — label conventions, function-header comment block, `pop {r4,pc}` preferred over `bx lr`, FUT/CFN/AFN/UTF test naming, ITTTT = 4-cond max.
8. **Glossary** — CCS, CEX, Op2, CP range, NUT, OUT, FUT, Pseudo LDR, Leaf/Stem, AAPCS.
9. **Last-Minute Traps** — 9 bullets of exam-trap material (sign-ext, no STRD reg-offset, CBZ-in-IT illegal, cond-B last slot only, cmp-of-neg-imm → CMN, prefix-`++` needs write-back, pointer arith scaling, ADD vs ADDS, ASR vs LSR).

## Feedback captured

- v1 AAPCS `tabularx` with `\linewidth` overflowed column in multicols* --- `\linewidth` resolves to full textwidth there, not column width. Fix: either use `\columnwidth` or drop the table entirely. Used itemize.
- User wants HW solutions visible on cheatsheet for pattern-matching during the quiz.
- **Verbatim-in-macro-arg is illegal.** First v2 had `\ex{...}` as a command; putting a `lstlisting` block inside a macro argument breaks Overleaf with "extra }" and "can't use macro-parameter character # in horizontal mode" errors (verbatim envs grab `#` literally, but in a macro arg `#` is reserved). Fix: converted `\ex` to an environment `\newenvironment{ex}{...}{...}`. Now all 18 worked HW examples use `\begin{ex}...\end{ex}` and lstlistings nest correctly.
