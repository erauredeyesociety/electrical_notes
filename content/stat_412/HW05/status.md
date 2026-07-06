# HW05 Status Notes

This file is the assignment-local map/status log. Keep detailed HW05 mapping
here rather than in `../findings.md`.

## Screenshot wave

The initial timestamp screenshot wave was normalized in chronological order to:

- `1.png` through `20.png`

OCR drafts were generated in `tmp/ocr_*.txt`; `tmp/` is ignored except for its
`.gitignore`.

## Supporting Markdown/reference files

- `2.md`: phosphate data table for Question 2.
- `5.md`: GPA data list for Question 5.
- `6.md`, `9.md`, `10.md`, `11.md`, `12.md`, `13.md`, `14.md`, `15.md`,
  `16.md`, `17.md`, `18.md`, `19.md`, `20.md`: standard normal table reference
  data.

Clean prompt files were created as `q1.md` through `q20.md`.

## Captured/pending parts

The visible screenshots mostly show the first answer field. When a screenshot
header says there are later parts but the actual later prompts are hidden, those
parts are marked pending instead of being invented.

Pending hidden prompts: none for the currently supplied context.

Solved from visible prompts:

- Q1 all visible requested statistics and center-choice dropdowns:
  greater than / less than / median.
- Q2 parts (a)--(c).
- Q3 parts (a)--(b).
- Q4 parts (a)--(b).
- Q5 standard deviation.
- Q6--Q9 visible prompts.
- Q10 parts (a)--(c).
- Q11 parts (a)--(c).
- Q12 visible prompt.
- Q13 parts (a)--(c), because all three were visible in the prompt.
- Q14--Q15 visible prompts.
- Q16 parts (a)--(b), because both were visible in the prompt.
- Q17--Q19 parts (a)--(b).
- Q20 visible prompt.

## Normal-table convention

For questions with standard-normal table links, worked solutions show the
rounded z-score/table calculation as the entry value. Exact calculator values
may differ slightly in the last digit. Q20 uses the linked standard-normal
table. The target central probability $0.975$ gives upper cumulative area
$0.9875$, which is the table value at $z=2.24$, so the platform answer is
$n=\lceil(2.24/0.05)^2\rceil=2008$.

## Q1 re-audit note

After a user concern about Q1, the screenshot was zoomed and re-read. The data
line clearly shows the nine observations:

`9, 16, 13, 10, 4, 68, 20, 9, 14`

The value is `68`, not `6`, and the pasted HTML confirms the mean `18.11` and
median `13` were accepted. The bad attempt was the mode: `68` was selected, but
the correct mode is `9` because `9` occurs twice.
