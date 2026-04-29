# CEC 320 Final Exam Cheatsheet — Design Notes

## Final layout: 2 separate documents (14 pages total)

- **Part 1** (`final_exam_cheatsheet_part1.tex`) — **6 pages** (even, prints clean front/back)
- **Part 2** (`final_exam_cheatsheet_part2.tex`) — **8 pages** (even, prints clean front/back)

Both are 4-column landscape, 0.18in margins, scriptsize body, lstlisting for ASM/C. Macros: `\asm`, `\cee`. Tag environments: `\begin{hwp}` (orange HW), `\begin{qp}` (purple Quiz), `\begin{ex}` (red example), `\begin{reg}` (teal Register).

Page-count verified locally via `tectonic` + PyMuPDF. Rendered PDFs are NOT committed — compile from source.

## Build system

The cheatsheets are now built from PARTIALS via `partials/build.sh`. Each partial is a content fragment (no preamble, no `\documentclass`, no `\begin{multicols*}`) — just `\section{...}` + content. The build script concatenates `_preamble_partN.tex` + every `.tex` in `partN/` (alphabetic order, prefix `NN_` controls order) + `_footer.tex`, producing `final_exam_cheatsheet_partN.tex` next to this file.

```bash
cd content/cec_320/final_exam/
./partials/build.sh                    # builds both parts
./partials/build.sh part1              # part 1 only
./partials/build.sh part1 --pdf        # also compile to PDF
./partials/build.sh --pdf              # build both + compile both PDFs
```

The script auto-detects `~/bin/tectonic` or system `tectonic`. PDFs land in `/tmp/`.

## Part 1 partials (6 pages)

ARM ASM programming meat — Lectures 14–27, HW 5–12, current-semester quizzes.

| File | Content |
|------|---------|
| `01_lectures_14_27.tex` | Recall bullets per lecture (L14–L27) |
| `02_hw05_qformat.tex`   | Q-format fixed-point; HW5 problems |
| `03_hw06_arith_eabi.tex`| Arithmetic instr; EABI calling; PUSH/POP |
| `04_hw07_shifts_logic.tex` | Shifts, Op2, bitwise; HW7 problems |
| `05_hw08_nzcv_ccs.tex`  | NZCV flags, CCS table, branches; HW8 |
| `06_hw09_ldr_str.tex`   | LDR/STR addressing; HW9 traces |
| `07_hw10_ptr_fn_call.tex` | C ptr idioms + AAPCS; HW10 traces |
| `08_hw11_if_flow.tex`   | If/if-else PL/NL/CEX; HW11 walkthroughs |
| `09_hw12_loops.tex`     | While/do-while/for/break; HW12 |
| `10_quiz3.tex`          | Quiz 3 reconstructed problems |
| `11_quiz4_qz26a.tex`    | Quiz 4 (current sem qz-26a) full solutions |

## Part 2 partials (8 pages)

Early-semester material + STM32 peripheral reference + extended worked examples.

| File | Content |
|------|---------|
| `01_lectures_2_9_13.tex` | Early lecture reference (L2–9, L13) |
| `02_hw01_uart_arch.tex`  | HW1 UART/MCU arch/numeric |
| `03_hw02_tc_ptr_unity.tex` | HW2 TC/endianness/pointers/Unity |
| `04_hw03_gpio_bitwise.tex` | HW3 GPIO + bitwise |
| `05_hw04_interrupts.tex` | HW4 NVIC/EXTI/preemption |
| `06_quiz1_uart_arch.tex` | Quiz 1 (prior sem qz-25a) |
| `07_quiz2.tex`           | Quiz 2 (reconstructed from prep notes) |
| `08_peripheral_reference.tex` | STM32 peripheral + C language reference |
| `09_arm_reference.tex`   | ARM ASM quick reference + traps |
| `10_hw1_4_extended_drills.tex` | Extended HW1–4 worked drills + 8 practice problems |
| `11_reverse_eng_internals.tex` | ASM↔C reverse-eng + system internals |
| `12_quiz6a_practice.tex` | Quiz 6a practice (prior-sem qz-25b) |

## Source extracts (markdown reference)

These are the per-topic data extracts agents produced. They remain in the folder for reference / future updates.

- `early_lectures_extract.md` — Lectures 2–9, 13 (411 lines)
- `hw1_4_extracts.md` — HW1–4 problems + solutions (192 lines)
- `hw5_hw6_extracts.md` — HW5/6 (101 lines)
- `hw7_hw8_extracts.md` — HW7/8 (196 lines)
- `hw9_12_expanded.md` — HW9–12 expanded register-state traces (280 lines)
- `lectures_condensed.md` — Lectures 14–27 condensed bullets (104 lines)
- `quiz3_quiz4_extracts.md` — Quiz 3 + 4 (qz-25b prior) + 6a (174 lines)
- `quiz4_2026_solutions.md` — **Current semester** Quiz 4 (qz-26a) full solutions (152 lines)

## Compile / verify locally

```bash
cd content/cec_320/final_exam/
./partials/build.sh --pdf
# Expected: part1 -> 6 pages, part2 -> 8 pages
```

Tectonic auto-fetches needed TeX Live packages on first run; subsequent runs are instant.

For Overleaf: paste the generated `.tex` (full document, not partials) into a new project. Default `pdflatex` engine works.

## Adding new content

To add a new section to either part: drop a new `NN_topic.tex` fragment file into `partials/part1/` or `partials/part2/`. The fragment must:

- NOT include `\documentclass`, `\begin{document}`, `\begin{multicols*}`, or any preamble
- Start directly with `\section{...}`
- Use the available macros: `\asm{}`, `\cee{}`, `\begin{lstlisting}` (language=arm), `\begin{hwp}`, `\begin{qp}`, `\begin{ex}`, `\begin{reg}`
- For ARM mnemonics or C identifiers containing `_`: write `\_` inside `\asm{}`/`\cee{}` (the macros use `\texttt{}` which doesn't auto-escape)
- Avoid `\langle`/`\rangle` (math-mode only)
- Avoid `\\` line breaks inside `\cee{}`/`\asm{}` — close and reopen instead
- Number prefix controls order; `NN_` keeps related material grouped

Then re-run `./partials/build.sh --pdf` and verify the page count.

## Workflow log

1. Initial build was a single 14-page document, then split into parts 1 (6 pp) + 2 (8 pp) with hand-edited TeX files.
2. After feedback about whitespace and gaps, **rebuilt entirely from partials** with one agent per HW (HW1–12), one per quiz (Q1, Q2, Q3, Q4-26a, Q6a-25b), plus reference partials (lectures 14–27, lectures 2–13, ARM reference, peripheral reference, extended HW1–4 drills, reverse-eng + internals).
3. Build script concatenates partials in alphabetic order; preamble/footer files at `partials/_preamble_partN.tex` and `partials/_footer.tex`.
4. Final structure: 11 partials in part1 (6 pp), 12 partials in part2 (8 pp).

## Known issues (minor)

- Several `Underfull \hbox` / `Overfull \hbox` warnings in both parts. None affect readability at compile dpi.
- The `\asm{}`/`\cee{}` macros use `\texttt{}` which doesn't auto-escape underscores — historical content writes `\_` manually; if you copy ASM/C identifiers in, escape underscores.

## Content known to be incomplete (per inventory)

- **Quiz 1**: only 2025 prior-semester solution PDF available; no current-sem Q1 worksheet/PDF
- **Quiz 2**: no problem/solution PDF; reconstructed from prep markdown only
- **Quiz 3**: no standalone problem/solution PDF; reconstructed from cheatsheet markdown
- **Quiz 6a**: only prior-semester (qz-25b) worksheet; no current-sem version

If you find any of these, drop them in `quizes/quizN/` and update the corresponding partial.
