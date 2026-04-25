# CEC 320 Final Exam Cheatsheet — Design Notes

## Target format
- 7 landscape pages (14 sides if printed double-sided) per instructor's rule
- Format lifted from `quizes/quiz4/qz4_cheatsheet.tex` (best density seen in the class)
- 4-column multicols, landscape letter, 0.18in margins, `\scriptsize` body + code

## Final output
- LaTeX source: `final_exam_cheatsheet.tex` (~2900 lines, 75 sections)
- Compiled PDF: `final_exam_cheatsheet.pdf` — renders **7 pages**, verified locally via `tectonic`
- Column density closely matches quiz4's, so Overleaf should render identically

## Content organization

**Part 0 — Lecture 14-27 recall bullets:** 14 tight bullet lists, one per lecture.

**Part I — Arithmetic, flags, bitwise (HW5-8 / L14-19):**
- Q-format fixed-point (HW5)
- Arithmetic instructions (HW6) — ADDS/ADC, SUBS/SBC, UDIV+MUL/MLS, SMLAL/UMLAL
- EABI arg passing (sign/zero extension)
- Stack + PUSH/POP rules
- Barrel shifter Op2 + shifted-Op2 scaling idioms
- Bitwise logic (HW7) — BIC/ORR/EOR/ORN/MVN + BFC/BFI
- NZCV computation (HW8) — N-bit system procedure, CMP/CMN/TST/TEQ
- CCS table + HiLow unSun mnemonic

**Part II — HW9-12 / L20-27 (bulk of course):**
- LDR/STR matrix + addressing modes (imm / pre-! / post- / reg-offset / LDRD)
- C pointer → ASM translation
- Sign-extension pitfalls
- Inc/dec — values vs pointers
- Function calls / AAPCS
- IT blocks + CBZ/CBNZ rules
- If/if-else — PL / NL / CEX
- Loops (while / do-while / for / while(1)+break)
- break / continue / switch

**Part III — Past quiz problem bank:**
- Quiz 3 all 6 problems (one-liners)
- Quiz 4 all 3 problems (with full solution sketches)
- Quiz 6a all 3 problems

**Part IV — Reference / checklist / traps:**
- ASM quick reference blocks
- Directives / file skeleton
- Registers / exception auto-stack
- Instructor style guide
- Glossary
- C→ASM checklist
- Extended last-minute traps

**Part V — Pattern catalog (C → ASM):**
- Integer arithmetic
- Shifts / scaling
- Bit manipulation
- Memory access
- Flow control

**Part VI — Common recipes:**
- Signed saturate
- Array sum / conditional sum / max
- strlen / strcpy / memcpy
- 64-bit MAC
- Q15 multiply
- Unsigned modulo fallback
- Pointer diff
- Bit-field assign / extract

**Part VII — Full worked HW problems:**
- HW11 P1 three-form side-by-side (PL/NL/CEX)
- HW11 P2 piecewise f(x) three forms
- HW11 P3 compound OR two forms
- HW12 P2 string copy two forms

**Part VIII — Deep-dive walkthroughs:**
- HW5 all 5 problems
- HW6 all 7 problems
- HW7 all 6 problems
- HW8 all 4 problems (NZCV+CCS drills)
- HW9 P3 four-task register-state table
- HW10 P1 four-line memory trace
- HW10 P2 four-task LDRD/LDRSB/LDRSH trace

**Part IX — Reference tables / idiom dumps:**
- Top-20 single-instruction patterns
- LDR pseudo resolution detail
- Cortex-M4 quick specs
- Bit-banding (background)
- Two's complement speed sheet
- Numeric ranges + hex↔dec
- Endianness drills
- Stack drawings
- CCS quick-lookup

**Part X — Strategy / last-mile:**
- Final exam strategy
- Debug pattern recognition
- When-to-use-what
- One-page summary

## Compilation

Local compile (Linux, no system LaTeX):
```bash
~/bin/tectonic -X compile final_exam_cheatsheet.tex -o ./
```

Tectonic downloads the TeX Live packages on first compile (~30s) and caches them.

Verification:
```python
import fitz; print(fitz.open('final_exam_cheatsheet.pdf').page_count)
# 7
```

## Content sources
- `quizes/quiz4/qz4_cheatsheet.tex` + `.md` — baseline format and HW9-12 content
- `quizes/quiz4/hw_solutions_summary.md` — HW9-12 solutions
- `quizes/quiz3/hw_solutions_summary.md` — HW7-8 content
- `quizes/quiz3/lecture_notes_summary.md` — lectures 14-18
- `homework/hw5/hw5-6_claude.md` + `homework/hw6/hw_6.md` — HW5-6 content
- `homework/hw{9-12}/*_solutions.md` — expanded HW9-12 detail
- `quizes/quiz{3,4}/qz*.pdf` — actual quiz problems and solutions
- `lectures/LECTURE_INDEX.md` — lecture topic list

## Workflow log
1. Three parallel agents extracted: HW5-6, HW7-8, quiz3+quiz4 problems.
2. Built initial 3-page cheatsheet with Part 0-IV content.
3. Spawned two more agents for: HW9-12 deep-dive detail + lecture 14-27 highlights.
4. Extended to 7 pages by adding Parts V-X.
5. Fixed two compilation errors: (a) `%function` mid-macro-argument (needed `\%function`), (b) curly braces in `\cee{... \{...\} ...}` in a tabular cell (simplified the flow-control patterns table).

## Known issues (minor)
- A few `Underfull \hbox` and one `Overfull \hbox` warnings. None affect readability at compiled dpi.
- Page 7 final two columns are partly blank — acceptable under the 7-page target.
