# STAT 412 — Answer-Key Findings & Conventions

Applies to **every assignment folder** — homeworks (`HW01`, `HW02`, …) and
quizzes (`QZ01`, `QZ02`, `QZ03`, …) alike. Read this before working any
question. Throughout, `<DIR>` is the assignment folder (e.g. `HW03`, `QZ03`) and
`<tag>` is its lowercase short name (e.g. `hw03`, `qz03`). The lessons here were
learned building HW01–HW05 and QZ03–QZ04; keep adding only reusable lessons so
each new assignment starts ahead. Per-assignment maps, answer lists, and status
logs belong inside the assignment folder, not in this global playbook.

## The two LaTeX deliverables (and how they differ)

Every assignment produces **two kinds** of LaTeX. They are *not* the same file
in two styles — they serve different readers and must never blur together.

**1. Worked-solution partials — one per question.**
`<DIR>/solutions/qNN.tex` (e.g. `QZ03/solutions/q05.tex`). These **show the
work**: the rewritten problem, every step (formula → substitution →
intermediate value → result), a short word or two of reasoning, and a boxed
final answer for each part. The reader should learn *how* the problem is solved.
Each partial is **fully standalone** — its own preamble, `\begin{document} …
\end{document}` — so it compiles alone and can be pasted into Overleaf by itself.
This is the format the user values most: keep the explanations and shown work.

**2. Complete answer-only sheet — one per assignment.**
`<DIR>/stat412_<tag>_answer_key.tex` (e.g. `QZ03/stat412_qz03_answer_key.tex`).
This is **just the answers**: a single numbered list, each entry naming the
displayed quantity or choice and giving the final value — **no steps, no
derivation**. It exists so the user can paste one self-contained file into
Overleaf for a quick check or final submission; importing many files is painful,
so it must be **fully standalone — never `\input`/`\include`** another file.

**The difference, stated plainly:** the partials *teach the method with full
steps*; the answer key is a *terse list of final results only*. Do not leak
derivations into the answer key, and do not strip the steps out of the partials.
Each answer-key entry must answer the displayed quantity/choice directly — never
substitute an unlabeled number or a broader related classification.

## Supporting rules for both deliverables

- The shared preamble is `content/stat_412/stat412_preamble.tex`, but it is only
  a source template. Inline the needed preamble into every deliverable; do not
  require Overleaf users to upload or import it.
- **Every question must also exist as a clean `qN.md`** in its assignment folder
  — never leave a question as only a screenshot or raw HTML. Transcribe the full
  prompt (all parts, data, answer options) to markdown; convert any HTML table to
  a markdown table.
- A clean question file is a **faithful transcription, not a summary**. Preserve
  every visible prompt sentence, the exact task being asked, all visible
  subparts, formulas, data, answer choices, units, and rounding/entry
  instructions. Minor punctuation cleanup is fine, but do not replace the
  question with a topic description or shortened paraphrase.
- The `Problem` section of each standalone `solutions/qNN.tex` must contain the
  same complete visible question as its Markdown source. A reader should be able
  to understand and solve the assignment without opening the screenshot.
- The three artifacts for a question — `qN.md`, `solutions/qNN.tex`, and that
  question's entry in the answer key — **move together**. When a part arrives or
  an answer changes, update all three in the same pass so they never disagree.

## Screenshot → data extraction

- MyStatLab data lives in HTML as `aria-label="X.XX"` attributes in document order
  (ids `var_N`, `aset_/bset_`, `S1`…). `grep -oE 'aria-label="[0-9.]+"'` to pull
  them; already-answered fields show the correct value in their `aria-label`.
- **Read the graded state, not just the value.** An input with class
  `... correct disabled` holds an accepted answer in its `aria-label` (e.g.
  `aria-label="0.6817"`); class `... incorrect` flags a wrong attempt; an empty
  field reads `aria-label="enter your response here"` (computed-but-unconfirmed).
  For multiple choice, the chosen radio carries `dijitRadioChecked … correct`
  and an off-screen "Your answer is correct." Use these to know which values are
  platform-confirmed vs. still your own computation. A standalone "That's
  incorrect" **feedback dialog** is generic remediation text — it names no part
  and gives no value; treat it as "re-verify," not as an answer source.
- When the question is **only a PNG**, read the image and transcribe the prompt +
  data by eye; then verify any numbers you'll compute with a quick Python check.
- If OCR is available, use it as the first pass for screenshot-only prompts:
  `tesseract N.png tmp/ocr_N --psm 6`. Treat OCR as a draft, not truth; compare
  against the image for numbers, inequalities, and rounding instructions before
  writing `qN.md`.
- Multi-screenshot questions: filenames like `qN-a.png … qN-d.png` (answer
  options) or `qN-1.png/qN-2.png` (prompt continued / data table). Read them all.
- Number-only names are also supported: `N.png`, `N-2.png`, `N-3.png`, etc.
  Treat every file sharing the same leading question number as material for that
  question. Check the Markdown too: users may paste raw MyStatLab HTML directly
  into `qN.md`; extract its accessible labels, question text, answer choices,
  entered/correct values, and later parts, then replace the raw HTML with clean
  Markdown.
- Normalize each assignment's original screenshot wave to `1.png`, `2.png`, and
  so on in question order. A suffix such as `N-2.png` or `N-3.png` means the
  user later added continuation material for Question N; do not renumber those
  files into the original wave. (A quiz may cover only a subset of numbers — e.g.
  QZ03 references only 5 and 7 — which is fine.)

## Incremental material inventory (this is a multi-turn workflow)

The user feeds material in **waves across many turns** — first some screenshots,
then pasted HTML for a few questions, then later parts (c), (d), (e) of the same
problem, sometimes a grading screenshot. Expect this and plan for it.

- **Always run the inventory script first** when the user says material/context
  was added — do not eyeball the folder:
  `python3 content/stat_412/scripts/material_inventory.py content/stat_412/<DIR>`.
- It reports new/changed/removed files, numbered questions with multiple
  screenshots, Markdown files containing pasted HTML (with a tag count), and
  timestamp screenshots that still need mapping. "Changed `qN.md`" may just be
  your own edits from earlier this session — cross-check with the HTML-tag list
  to see where the user actually pasted something new.
- It writes an ignored snapshot to `<DIR>/.worklogs/material_snapshot.json`, so
  re-running surfaces only the delta. The `.worklogs` directories are git-ignored.
- The inventory snapshot currently watches only **top-level assignment files**
  (`qN.md`, screenshots, loose reference tables, answer-key files). It does
  **not** report edits inside nested directories such as `<DIR>/solutions/`.
  So "Changed files: none" means no new root-level material arrived; it does
  not mean the worked LaTeX partials were untouched.
- After editing nested worked solutions, run a quick local check yourself, e.g.
  brace-balance over `<DIR>/solutions/q*.tex` plus `git diff --check`. If
  `tectonic` is installed, also compile the changed standalone `.tex` files.
- For an unknown problem with several parts, **transcribe the full part count
  from the header immediately** (e.g. "complete parts (a) through (e)") and stub
  the not-yet-visible parts as pending. Never invent a missing subpart; never
  silently shorten the part list to what is currently visible.
- A value computed while its MyStatLab field was still blank is
  **computed-but-not-platform-confirmed** — label it so in all three artifacts
  and call it out to the user, so they re-check it on entry.

## Reference tables vs. question prompts (and "data-before-prompt")

Not every file is a question. A **number-only Markdown file** (`5.md`, `7.md`,
`11.md`, `13.md`, `14.md`, …) is usually a **reference table**, not a prompt:
a standard-normal table, a cumulative-Poisson table, an incomplete-gamma table,
etc. A **clean prompt always lives in `qN.md`** (the `q` prefix). So `5.md` is
reference data *for* Question 5, while `q5.md` is Question 5 itself.

**Expect reference data to arrive before the prompt.** The user may drop the
lookup table for a problem first and the actual question text later — possibly
several turns later, or as a screenshot/pasted HTML. When that happens:

- Do **not** treat the table as the question and do **not** try to "solve"
  anything yet — there is nothing to solve without the prompt.
- Do record what the table implies, so the later prompt is fast to handle:
  an incomplete-gamma table ⇒ a **gamma-distribution** problem; a standard-normal
  table ⇒ a **normal** problem; a cumulative-Poisson table ⇒ a **Poisson**
  problem; binomial sums ⇒ a **binomial** problem.
- Note in the assignment-local status file which question each loose table
  feeds, and that the matching `qN.md` prompt is still awaited.
- Once the prompt arrives, build the usual three artifacts (`qN.md`, the worked
  partial, the answer-key entry) and cite the reference table as a source.

When the prompt eventually comes only as raw MyStatLab HTML, extract its labels/
values and **replace the HTML with clean Markdown** — same as for homeworks.

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

## Project folders (Word/Excel deliverables)

For larger projects such as `MD5_project`, preserve the instructor's original
Word and Excel files. Do **not** edit the downloaded `.docx`/`.xlsx` directly
from Codex; use exported CSVs, Markdown instructions, helper scripts, and
`tmp/` scratch outputs instead. The student can later copy formulas, tables,
and charts into the official Excel/Word submission files.

- Convert instructions into a faithful `project_instructions.md`.
- Create a practical `project_setup_summary.md` with deliverables, formulas,
  interpretation notes, and next actions.
- If Python helps, make scripts read-only with respect to original files and
  write generated samples, summaries, and charts only under `tmp/`.
- Add `tmp/.gitignore` (`*`, `!.gitignore`) so generated project previews stay
  disposable.
- If the Word and Canvas/HTML instructions disagree, prefer the clearer Canvas
  wording when it is consistent with the project context, and document the
  discrepancy.

## Stats conventions

- "Variance"/"standard deviation" of a sample = **sample** formula (÷ n−1) unless
  the prompt says population. Note the population value too if ambiguous.
- Round exactly as the prompt states (2 d.p., 4 d.p., …). Verify every numeric
  answer with Python before writing it.
- For hypothesis-test multiple choice, let the **claim wording choose the
  alternative**, and keep equality in the null. "Changed" or "different" means
  two-sided; "less than/fewer than/below" means left-tailed; "more than/greater
  than/over" means right-tailed. MyStatLab often lists logically backwards
  choices, so choose the option whose null contains equality and whose
  alternative matches the claim.
- **Normal-distribution problems: report z-table rounding, but MyStatLab grades
  with a tolerance band that accepts either the table value or the exact CDF.**
  Round each $z$ to two decimals and use the printed table value as the default
  (HW03 Q14(a) stored $0.2420$ from $z=0.70$, not exact $0.2427$; Q12(a) is
  $0.9525$, not $0.9522$). But the platform also accepted the exact value where
  the student entered it (HW03 Q14(c) stored $0.6817$, the exact figure, not the
  table $0.6834$). The stored "correct" value just reflects what was typed. So:
  when a screenshot shows a graded value, report that; otherwise give the table
  value and note the exact one. Never "fix" the sheet over a last-digit
  difference without re-checking with rounded $z$ first.
- For inverse-normal or sample-size questions that still link the standard
  normal table, choose the nearest table cutoff unless a graded screenshot
  confirms an exact-calculator value. Example pattern: central probability
  $0.975$ gives upper area $0.9875$, table value $z=2.24$.
- When sample means/measurements are **recorded to the nearest tenth**, use
  class boundaries for probability ranges: inclusive $177.1$ to $179.7$ becomes
  $177.05$ to $179.75$; ``below $177.0$'' means recorded values $176.9$ or
  lower, so use cutoff $176.95$.
- When MyStatLab marks an entered answer wrong, suspect a user typo before
  re-deriving (happened once: 2.3 vs 2.233).
- **When a prompt says ``type an exact answer''/``using radicals''/``simplify,''
  the field rejects rounded decimals.** Give the fraction or radical as the
  answer (e.g. HW04 Q6 wanted $-\sqrt{30}/10$ and rejected $-0.5477$; covariance
  fields want $-2/75$, not $-0.0267$). A ``Try again''/``incorrect'' on such a
  field is often a format rejection, not a wrong value --- re-check the requested
  form before re-deriving. Generic ``That's incorrect'' dialogs that merely
  restate a definition carry no answer; treat them as ``re-verify.''

## Solution style — match the course transcripts

The course's lecture videos are transcribed in
`content/stat_412/Chapter1_transcripts.txt` … `Chapter9_transcripts.txt` (Khan
Academy, The Organic Chemistry Tutor, JBstatistics, etc.). **Skim the relevant
chapter before writing worked solutions** so the method and notation match what
the student saw. Continuous-distribution material is in Chapter 3 (density,
normal, exponential, uniform) and Chapter 4 (expectation/variance).

Each worked partial should read **"name the distribution, state its formula,
then plug in"** — a short *Setup* paragraph with the governing formula, then a
*Work* section with labelled steps, then the boxed answer. House conventions
distilled from the transcripts:

- **Probability $=$ area under the density** $=\int_a^b f(x)\,dx$; a single point
  has probability $0$, so $P(X<a)=P(X\le a)$.
- For continuous integrals, show a **little algebra, not just the final
  antiderivative**. Expand simple polynomials when useful, write the
  antiderivative with limits, and show the key evaluated boundary value. Example
  style: $\int 12x(1-x)^2dx=\int(12x-24x^2+12x^3)dx
  =[6x^2-8x^3+3x^4]$. This keeps solutions "plain and simple" while still
  showing enough work to debug an entry.
- **Continuous mean/variance:** $\mu=E(X)=\int x f\,dx$, $E(X^2)=\int x^2 f\,dx$,
  then the shortcut $\operatorname{Var}=E(X^2)-\mu^2$, $\sigma=\sqrt{\operatorname{Var}}$.
- **Exponential:** identify the rate $\lambda=1/\text{mean}$, then use the closed
  forms $P(X>x)=e^{-\lambda x}$ and $P(X<x)=1-e^{-\lambda x}$ instead of
  re-integrating; the mean is $1/\lambda$.
- **Uniform$(A,B)$:** $f=\tfrac1{B-A}$, mean $\tfrac{A+B}{2}$, SD
  $\tfrac{B-A}{\sqrt{12}}$.
- **Normal:** standardize $z=\tfrac{x-\mu}{\sigma}$, read the table as an area;
  for a percentile go backward, $x=\mu+z\sigma$.
- **Gamma is not in the transcripts** — build it from what is: the waiting time
  for the $k$th event in a constant-rate (Poisson) process is gamma with shape
  $\alpha=k$ and scale $\beta=1/\lambda$ (mean gap). The incomplete-gamma table
  is for $\beta=1$, so enter it at $x/\beta$ and read $F(x/\beta;\alpha)$.

## Joint distributions, covariance & Chebyshev (Chapter 4)

Reusable formulas and traps distilled from HW04 and QZ04 (the joint-distribution
chapter). Lead each worked partial with the relevant one, then plug in.

- **Marginals** — sum/integrate *out the other variable*:
  $g(x)=\sum_y f(x,y)$ or $\int f\,dy$; $h(y)=\sum_x f(x,y)$ or $\int f\,dx$.
- **Conditional density** $f(x\mid y)=\dfrac{f(x,y)}{h(y)}$ — the joint over the
  *marginal*, **not** the joint itself (HW04 Q4's wrong ``Choice C'' handed back
  the joint $\tfrac34x$). That the conditional still depends on the conditioning
  variable is exactly what proves dependence.
- For conditional continuous probabilities, explicitly state the conditional
  support and normalize the remaining variable. Constants involving fixed
  conditioning values should cancel; do not carry irrelevant fixed constants
  through a probability integral unless they help show the cancellation.
- **Independence** iff $f(x,y)=g(x)\,h(y)$ for all $(x,y)$ **and** the support is
  a rectangle (each range free of the other variable). A triangular support such
  as $0<y<2-x$ already forces dependence.
- **Factoring shortcut:** if $f$ factors as (function of $x$)(function of $y$)
  on a rectangular support, then $X\perp Y$, so $\operatorname{Cov}=0$ and
  $\rho=0$ — don't integrate (HW04 Q16, $f=\tfrac{64y}{5x^3}$).
- **Covariance** $\sigma_{XY}=E(XY)-\mu_X\mu_Y$, with
  $E(XY)=\sum\sum xy\,f$ or $\iint xy\,f$.
- **$E(XY)=E(X)E(Y)$ only when $X\perp Y$** (HW04 Q8b, Q10c).
- **Correlation** $\rho=\dfrac{\sigma_{XY}}{\sigma_X\sigma_Y}$. For $Y=a+bX$:
  $\operatorname{Cov}(X,Y)=b\sigma_X^2$ and
  $\sigma_Y=\sqrt{b^2\sigma_X^2}=|b|\sigma_X$ (use the absolute value, never
  $b\sigma_X$ when $b<0$), so $\rho=\dfrac{b}{|b|}$ ($+1$ if $b>0$, $-1$ if $b<0$).
- **Variance of a linear combination — the big trap:**
  \[
  \operatorname{Var}(aX+bY+c)=a^2\sigma_X^2+b^2\sigma_Y^2+2ab\,\sigma_{XY}.
  \]
  The additive constant $c$ drops out. If $X\perp Y$ the cross term is $0$
  (so $\operatorname{Var}=a^2\sigma_X^2+b^2\sigma_Y^2$); if they are
  **dependent you must keep $2ab\,\sigma_{XY}$**, signs included (HW04 Q12d:
  $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}$,
  $=\tfrac{29}{240}$, not the bare covariance $-\tfrac1{72}$).
- **Discrete uniform on $1..n$** (an $n$-sided die): mean $\tfrac{n+1}{2}$,
  variance $\tfrac{n^2-1}{12}$.
- **Chebyshev** $P(|X-\mu|\ge k\sigma)\le\dfrac1{k^2}$ (useful only for $k>1$);
  match a deviation $t$ via $t=k\sigma$.
  - Complement is a **lower** bound: $P(|X-\mu|<t)\ge 1-\tfrac1{k^2}$ (HW04 Q14b).
  - ``Find $c$ with $P(|X-\mu|\ge c)\le\alpha$'': solve
    $\tfrac{\sigma^2}{c^2}=\alpha\Rightarrow c=\tfrac{\sigma}{\sqrt\alpha}$
    (HW04 Q14d: $\tfrac{4}{c^2}=0.04\Rightarrow c=10$).
  - **Stated ``symmetric about the mean'' ⇒ halve** the two-tail bound for a
    one-tail question: $P(X\le\mu-k\sigma)\le\tfrac1{2k^2}$ (HW04 Q13 $=3.125\%$;
    QZ04 Q8 $=12.5\%$).

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

## Per-question standalone LaTeX shape

```
\documentclass[11pt]{article}
... inlined packages and answerbox definition ...
\begin{document}
\section{<short descriptive title>}
\subsection*{Problem}  <prompt + data table>
\subsection*{Part (a) — ...}  <steps>  \begin{answerbox} \textbf{Answer (a):} ... \end{answerbox}
... (more parts) ...
\end{document}
```

- Each standalone question file must rewrite the problem, show the essential
  calculation, and end each answered part with an `answerbox`.
- When later screenshots add parts to an existing problem, update that
  question's Markdown, its standalone solution, and the answer-only sheet.
- Never invent a cropped or missing subpart. Add a plainly labeled pending note
  and record which continuation screenshot is still needed.

## Assignment-local status notes

Keep `findings.md` as the durable playbook: conventions, formulas, traps, and
workflow rules that apply across assignments. Do **not** turn it into a map of
every homework/quiz or a running answer list.

When an individual assignment needs a log, put that note in the assignment
folder itself, for example `<DIR>/status.md` or `<DIR>/.worklogs/notes.md`.
The global findings file should only receive a new note when the lesson is
likely to matter again.
