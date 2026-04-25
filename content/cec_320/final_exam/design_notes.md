# CEC 320 Final Exam Cheatsheet — Design Notes

## Final layout: 2 separate documents (14 pages total)

- **Part 1** (`final_exam_cheatsheet_part1.tex`) — **6 pages** (even, prints clean front/back)
- **Part 2** (`final_exam_cheatsheet_part2.tex`) — **8 pages** (even, prints clean front/back)

Both documents use the same LaTeX format (4-col landscape, 0.18in margins, scriptsize body, lstlistings for ASM/C). Identical macros (`\asm`, `\cee`) and tag environments (`\begin{hwp}`, `\begin{qp}`, `\begin{ex}`, `\begin{reg}`).

Page-count verified locally via `tectonic` (a static-binary LaTeX compiler at `~/bin/tectonic`) + PyMuPDF page-count check. Rendered PDFs are NOT committed — compile from source as needed.

## Part 1 (6 pages) content map

ARM ASM programming meat (Lectures 14-27, HW 5-12, this semester's quizzes).

- Lectures 14-27 recall bullets
- Q-format fixed-point (HW5)
- Arithmetic instructions (HW6) — ADDS/ADC, SUBS/SBC, modulo, SMLAL/UMLAL/MLA/MLS
- EABI arg passing + sign/zero ext at call site
- Stack + PUSH/POP rules
- Barrel shifter Op2 + scaling idioms
- Bitwise logic (HW7) — BIC/ORR/EOR/ORN/MVN/BFC/BFI
- NZCV flag computation (HW8)
- CCS table + HiLow unSun mnemonic
- LDR/STR matrix + addressing modes
- C pointer → ASM translation
- Sign-extension pitfalls
- Inc/dec patterns
- Function calls / AAPCS
- IT blocks + CBZ/CBNZ
- If/if-else (PL/NL/CEX)
- Loops (while / do-while / for / while(1)+break)
- break/continue/switch
- **Quiz 4 (Spring 2026, qz-26a)** — full problem-by-problem solutions
- Practice Quiz (qz-25b prior semester) — additional practice
- Quiz 6a worksheet
- ASM quick ref + directives
- Pattern catalog (C → ASM)
- Common recipes
- HW Coverage Map
- Full HW11/HW12 walkthroughs side-by-side
- HW5/HW6/HW7 walkthroughs (compact)
- HW8 walkthrough (NZCV + CCS drills)
- HW9 P3 four-task tasks
- Common ASM-file skeleton
- Number-format speed tables
- Memory regions (F412/G431)
- Endianness drills
- C-ASM Pitfall Quiz
- Last-Minute Traps (extended)

## Part 2 (8 pages) content map

Early-semester material + STM32 peripheral reference + extended worked examples.

**Part A — Early Lectures (L2-9, 13):**
- L2: UART (baud math, framing, parity, STM32 default)
- L3: MCU arch + pipeline + memory map
- L4: Two's complement + endianness + C type widths
- L5: Pointers + Unity unit testing
- L6: GPIO (modes, register map, base addresses)
- L7: Bitwise + direct GPIO + BSRR atomic
- L8: Exceptions + NVIC (IRQn, vector table, NVIC regs)
- L9: Preemption + EXTI + FSM
- L13: Real numbers (IEEE 754 single/half, Q-format preview)

**Part B — HW1-4 solutions:**
- HW1 (UART, pipeline, binary)
- HW2 (TC, endianness, pointers, Unity)
- HW3 (GPIO + bitwise)
- HW4 (NVIC + EXTI)

**Part C — Peripheral reference:**
- GPIO_TypeDef offsets + common ops
- NVIC layout
- EXTI + SYSCFG
- USART register highlights
- SysTick + TIM + ADC + DMA

**Part D — C language:**
- Operator precedence
- Bit-banding (SRAM + peripheral aliases)
- Bit-twiddle idioms
- Type promotion + UB watchlist
- Inline ASM with GCC syntax
- Build system (linker + startup)

**Part E-G — Extended worked examples:**
- HW1 P3 pipeline math
- HW2 P3 endianness
- HW2 P6 union aliasing
- HW3 bit-field replace
- HW4 EXTI configuration trace
- 7 practice problems (pipeline, TC, GPIO, NVIC, memory map, fixed-point, pointers)

**Part H-I — System internals:**
- Vector table layout
- Reset handler ASM
- Linker script sketch
- ASM-writing workflow + reading-ASM workflow
- ASM patterns vocabulary

**Part J — Extended HW walkthroughs:**
- HW1 deep walkthrough
- HW2 5-bit TC drills
- HW3 register access mapping
- HW4 priority + nested ISR

**Part K-N — Reference + practice:**
- ASM-to-C reverse-engineering drills
- C-to-ASM translation drills
- Stack frame drawings
- Cortex-M4 quick specs (extended)
- Vector table (G4 partial)
- Exam-day error hit-list
- IEEE 754 worked examples
- Q-format drills
- Number conversion drills
- Boolean algebra refresher
- Useful macros and constants
- Common driver patterns
- Cycle counts by instruction
- Calling-convention details
- HAL vs direct register
- ARM instruction encoding
- HAL init pattern
- Saturating arithmetic
- NVIC priority math
- Vector table override
- Flash wait states
- Boot sequence

## Source extracts (markdown reference)

These are the per-topic data extracts agents produced and were used to write the LaTeX files. They remain in the folder for reference / future updates.

- `early_lectures_extract.md` — Lectures 2-9, 13 (411 lines)
- `hw1_4_extracts.md` — HW1-4 problems + solutions (192 lines)
- `hw5_hw6_extracts.md` — HW5/6 (101 lines)
- `hw7_hw8_extracts.md` — HW7/8 (196 lines)
- `hw9_12_expanded.md` — HW9-12 expanded register-state traces (280 lines)
- `lectures_condensed.md` — Lectures 14-27 condensed bullets (104 lines)
- `quiz3_quiz4_extracts.md` — Quiz 3 + 4 (qz-25b prior) + 6a (174 lines)
- `quiz4_2026_solutions.md` — **THIS semester's Quiz 4 (qz-26a)** with full solutions (152 lines)

## Compile / verify locally

```bash
~/bin/tectonic -X compile final_exam_cheatsheet_part1.tex -o /tmp
~/bin/tectonic -X compile final_exam_cheatsheet_part2.tex -o /tmp
python3 -c "import fitz; print(fitz.open('/tmp/final_exam_cheatsheet_part1.pdf').page_count)"
# 6
python3 -c "import fitz; print(fitz.open('/tmp/final_exam_cheatsheet_part2.pdf').page_count)"
# 8
```

(Tectonic auto-fetches needed TeX Live packages on first run; subsequent runs are instant.)

For Overleaf: just paste the .tex contents into a new project. Default `pdflatex` engine works.

## Workflow log

1. Three parallel agents extracted HW5-6, HW7-8, quiz3+quiz4 problems.
2. Built initial 3-page cheatsheet (Part 1 v0).
3. Two more agents pulled HW9-12 expanded + lecture 14-27 highlights.
4. Extended Part 1 to 7 pages.
5. After user feedback, **trimmed Part 1 to 6 pages** by removing redundant sections (Top-20 patterns, one-liner cheats, switch variants, calling-convention templates, operator precedence, bit-banding -- those moved to Part 2).
6. After user uploaded the 2026 Quiz 4 solution PDF, an agent extracted those problems; Part 1's old Quiz 4 section was replaced with the actual semester-current content; the older qz-25b material was kept as "Practice Quiz (Prior Sem qz-25b)" for additional drilling.
7. Spawned 2 parallel agents for Part 2 source: early-lecture extract (411 lines) + HW1-4 extracts (192 lines).
8. Built Part 2 fresh at 8 pages (matched 6 + 8 = 14 split for clean-print front/back).

## Known issues (minor)

- A few `Underfull \hbox` / `Overfull \hbox` warnings in both parts. None affect readability at compile dpi.
- Trim-comments (`% [TRIM-Part1] ...` / `% [MOVE-Part2] ...`) in Part 1 mark sections that were moved out; Part 2's section comments mark which content was migrated in.
