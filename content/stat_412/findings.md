# STAT 412 — Answer-Key Findings & Conventions

Applies to **all** homeworks (HW01, HW02, HW03, …). Read this before working any
question. (Supersedes the per-HW notes; the lessons here were learned building HW01.)

## Deliverables & layout

- One **paste-ready LaTeX answer key per homework**, living in that homework's
  folder so `\includegraphics` paths resolve: `HW0X/stat412_hw0X_answer_key.tex`.
- The shared preamble is `content/stat_412/stat412_preamble.tex` — inline it into
  each final key (so the file is self-contained for Overleaf) and set the title/
  `\lhead` per homework.
- **Every question must also exist as a clean `qNN.md`** in its HW folder — never
  leave a question as only a screenshot. Transcribe the full prompt (all parts,
  data, answer options) to markdown; convert any HTML table to a markdown table.

## Screenshot → data extraction

- MyStatLab data lives in HTML as `aria-label="X.XX"` attributes in document order
  (ids `var_N`, `aset_/bset_`, `S1`…). `grep -oE 'aria-label="[0-9.]+"'` to pull
  them; already-answered fields show the correct value in their `aria-label`.
- When the question is **only a PNG**, read the image and transcribe the prompt +
  data by eye; then verify any numbers you'll compute with a quick Python check.
- Multi-screenshot questions: filenames like `qN-a.png … qN-d.png` (answer
  options) or `qN-1.png/qN-2.png` (prompt continued / data table). Read them all.

## Identifying the right plot (dotplot/boxplot/histogram multiple-choice)

- Use **extreme values as fingerprints**: the overall min and max each belong to a
  known group/color; repeated values make stacks of known height. Only one option
  matches both extremes and the stacking. An isolated max far from the cluster is
  often the decisive tell. Zoom with ImageMagick (`convert in.png -crop WxH+X+Y
  +repage -resize 300% out.png`) when unsure.
- Screenshots carry StatCrunch chrome (a "Dot plot X" title, gray border, zoom
  buttons on the right). **Crop it off** before `\includegraphics`; keep axis +
  legend. For 480×270 grabs, `-crop 349x182+5+50` worked. Save cropped copies as
  `qN_<role>_<label>.png` (role ∈ dotplot|boxplot|histogram|data|output).

## Building charts — use Python, NOT LaTeX

- When a question asks you to **construct** a chart (histogram/boxplot/etc.) write
  a small reproducible `qNN_<chart>.py` (matplotlib, installed 3.10) that emits a
  PNG, then `\includegraphics` it. Do **not** draw charts with pgfplots/tikz.
- For a multiple-choice "which chart is correct," also state the distinguishing
  shape (modality, tallest bar's class, tail/skew) so the option can be matched
  even without its screenshots. Relative-freq histogram class width 0.5 fit the
  teacher-salary data.

## Stats conventions

- "Variance"/"standard deviation" of a sample = **sample** formula (÷ n−1) unless
  the prompt says population. Note the population value too if ambiguous.
- Round exactly as the prompt states (2 d.p., 4 d.p., …). Verify every numeric
  answer with Python before writing it.
- When MyStatLab marks an entered answer wrong, suspect a user typo before
  re-deriving (happened once: 2.3 vs 2.233).

## LaTeX gotchas (all confirmed)

- Pin floats with `[H]` (package `float`) so steps stay in reading order.
- A `tcolorbox` (answerbox) immediately after a `[H]` float overflows ~144 pt —
  put a `\noindent` text paragraph between the float and the box.
- Long cells in an `l` column don't wrap → use `p{0.62\textwidth}`.
- A 10–12-term sum in a fraction numerator overflows → write "Sum $=X$, so"
  then a short `\[\bar x = X/n\]`.
- An inline `\texttt{file\_name.py}` (underscore) is one unbreakable word and
  overflows at a line end — keep such filenames out of justified prose.
- A wide data table (many columns + long row labels) → wrap the `tabular` in
  `\resizebox{\textwidth}{!}{ ... }`.
- **Build-check only** with `tectonic -o /tmp/<dir> file.tex`; check for `error`
  and `Overfull`. Do not render PDFs to PNG to eyeball.

## Per-question LaTeX fragment shape (what each agent emits)

```
\section{<short descriptive title>}
\subsection*{Problem}  <prompt + data table>
\subsection*{Part (a) — ...}  <steps>  \begin{answerbox} \textbf{Answer (a):} ... \end{answerbox}
... (more parts) ...
```
No preamble, no `\begin{document}` in a fragment — the assembler supplies those.
