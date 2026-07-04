# STAT 412 — Answer-Key Findings & Conventions

Applies to **every assignment folder** — homeworks (`HW01`, `HW02`, …) and
quizzes (`QZ01`, `QZ02`, `QZ03`, …) alike. Read this before working any
question. Throughout, `<DIR>` is the assignment folder (e.g. `HW03`, `QZ03`) and
`<tag>` is its lowercase short name (e.g. `hw03`, `qz03`). The lessons here were
learned building HW01–HW04 and QZ03–QZ04; keep adding to it so each new
assignment starts ahead. The reusable **method/formula** sections come first;
the per-assignment **mapping** sections at the bottom are the running log.

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
- Note in the assignment's mapping section which question each loose table feeds,
  and that the matching `qN.md` prompt is still awaited.
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

## Stats conventions

- "Variance"/"standard deviation" of a sample = **sample** formula (÷ n−1) unless
  the prompt says population. Note the population value too if ambiguous.
- Round exactly as the prompt states (2 d.p., 4 d.p., …). Verify every numeric
  answer with Python before writing it.
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

## QZ03 mapping (June 20, 2026 — complete, 7 questions)

- QZ03 is a **quiz** (Q1--Q7). Layout: `q1.md`--`q7.md` clean prompts,
  `QZ03/solutions/q01.tex`--`q07.tex` worked partials,
  `QZ03/stat412_qz03_answer_key.tex` standalone answer-only sheet.
- The original screenshots arrived as seven timestamped grabs; they were
  normalized to `1.png`--`7.png` in question order. The capture order matched
  question order, **confirmed by the reference tables**: the 5th grab is the
  gamma problem (matches `5.md`) and the 7th is the normal problem (`7.md`).
- Reference tables: `5.md` = Incomplete Gamma Function (cumulative $F(x;\alpha)$
  for $\beta=1$; rows $x$, columns $\alpha=1\ldots10$ — enter at $x/\beta$);
  `7.md` = standard-normal table.
- All seven fields were blank (a quiz to solve), so every answer is computed and
  Python-verified, not platform-confirmed. Answers:
  Q1 $\operatorname{Var}=\tfrac1{72}$, $\sigma=\tfrac{\sqrt2}{12}$;
  Q2 $P(Y>2)=e^{-4/7}\approx0.5647$;
  Q3 $2000\cdot\tfrac{27}{19}\approx\$2842$;
  Q4 (a) $\tfrac{72}{95}$, (b) $\tfrac{57}{95}=\tfrac35$;
  Q5 gamma $\alpha=6,\beta=100$, $P(T<500)=F(5;6)=0.384$;
  Q6 exponential mean $\tfrac{1000}{3}\approx333.33$ hr;
  Q7 normal $10$th percentile $35000+(-1.28)(2600)=31{,}672$ mi (exact $z$: $31{,}668$).
- Lesson reinforced: **a loose reference table pins the question type and even
  the question number** before any prompt arrives (here `5.md`/`7.md` predicted
  Q5 gamma / Q7 normal, which the screenshots then confirmed).

## QZ04 mapping (June 23, 2026 — complete, 9 questions)

- QZ04 is a nine-question quiz on joint distributions, covariance, transformed
  means/variances, continuous moments, conditional densities, and Chebyshev.
  Layout: clean `q1.md`--`q9.md`,
  standalone worked `solutions/q01.tex`--`q09.tex`, and the standalone concise
  `stat412_qz04_answer_key.tex`.
- The nine timestamped screenshots were normalized chronologically to
  `1.png`--`9.png`; the capture order exactly matched Q1--Q9. Raw HTML in all
  nine Markdown files supplied the accessible question text and choices, then
  was removed after transcription.
- Every field was blank, so all answers are computed and verified rather than
  platform-confirmed.
- A second-pass audit checked the solutions against the Chapter 3--4 course
  transcripts and authoritative probability references, then independently
  checked every joint/marginal/conditional density for normalization and every
  nontrivial probability with both exact symbolic integration and numerical
  quadrature. No answer values changed. The audit did restore all visible
  multiple-choice distractors to Q2, Q5, Q7, and Q9 and their worked-solution
  problem statements, because a standalone problem must preserve the complete
  prompt rather than only the correct choice.
- A later polish pass expanded the worked-solution integral steps in Q2, Q3,
  Q4, Q5, Q7, and Q9: show the integrand expansion, the antiderivative with
  limits, and the key fraction/decimal simplification. The answer-only key
  intentionally stayed terse. Inventory showed no root-level changes because
  nested `solutions/` files are outside the snapshot scope; brace-balance and
  `git diff --check` passed.
- Answers:
  Q1 $\operatorname{Var}(-4X+6Y-8)=180$;
  Q2 (a) $875/2187$, (b) $h(y)=12y(1-y)^2$ on $0\le y\le1$,
  (c) $16/49$;
  Q3 $\operatorname{Var}=1/72$, $\sigma=\sqrt2/12$;
  Q4 Choice A, $E(Y)=9$, $E(Y^2)=247/3$, $\operatorname{Var}(Y)=4/3$;
  Q5 Choice A with $f(x\mid y)=3x^2/(3-y)^3$,
  $P(X>0.3\mid Y=1.7)=2170/2197\approx0.987711$;
  Q6 $E(Z)=18.8$, $\operatorname{Var}(Z)=80.36$;
  Q7 Choice A $g(x)=(10x+4)/9$, Choice B $h(y)=(8y+5)/9$,
  $P(X<1/3)=17/81$;
  Q8 symmetric Chebyshev lower-tail bound $12.5\%$;
  Q9 Choice C $g(y,z)=6y^2z/25$, Choice C $h(y)=3y^2$,
  (c) $91/900$, (d) $9/64$.
- Q1 reinforces the dependent-variable variance formula:
  \[
  \operatorname{Var}(aX+bY+c)
  =a^2\sigma_X^2+b^2\sigma_Y^2+2ab\sigma_{XY}.
  \]
  Keep the signs inside $2ab\sigma_{XY}$; here the covariance contribution is
  negative.
- Q8 again uses the course convention that a symmetric distribution halves the
  two-tail Chebyshev bound. A cutoff two standard deviations below the mean
  gives one-tail probability at most
  $\tfrac12(1/2^2)=1/8=12.5\%$.
- For a conditional continuous probability such as Q9(d), constants involving
  the fixed conditioning values cancel. Normalize only the remaining
  $x$-dependent kernel; here it is proportional to $x$ on $0<x<2$.

## HW04 mapping (June 20, 2026 — joint distributions, 17 questions)

- HW04 is the **joint-distributions** chapter: marginals, conditionals,
  independence, covariance, correlation, expectation/variance of linear
  combinations, and Chebyshev.
- 17 timestamped screenshots, normalized to `1.png`--`17.png` in chronological =
  question order. Labeled extras the user supplied: `q2-2.png` (the joint table
  for Q2), and `q5.md` / `q8.md` (joint tables the user typed for Q5 and Q8 ---
  these were expanded into the full `q5.md`/`q8.md` prompts, table preserved).
- Pasted HTML later filled in several later parts. **Newly resolved:**
  Q8(b) $E(XY)=E(X)E(Y)=7.28$ (independent); Q10(b) $E(X-Y)=0$; Q11(b)
  $\operatorname{Var}(X+3Y-5)=5.25+9(5.25)=52.5$; Q12(a) confirmed by dropdowns
  (``are not / is not / $g(x)h(y)$ / marginal distributions''; the functions
  themselves are the marginal densities); Q14(b)
  $P(|X-4|<3)\ge 1-\tfrac49=\tfrac59$ (complement ⇒ Chebyshev gives a *lower*
  bound). That wave still lacked Q1(b--d), Q10(c), Q12(b--d), and Q14(c--d);
  the next bullet records the later additions.
- A later HTML wave resolved two more prompts: Q10(c) asks for $E(XY)$, giving
  $E(X)E(Y)=12.5^2=156.25$ because the dice are independent; Q14(c) asks for
  $P(-1<X<9)=P(|X-4|<5)\ge21/25$. Both fields were blank, so these are computed
  but not platform-confirmed.
- The June 23 HTML wave exposed Q1(b), Q12(b), Q14(d), and Q17's next proof
  dropdown. Q1(b) is $P(X>6,Y\le5)=23/126$. Q12(b) gives
  $E(X+Y)=5/4$ and $E(XY)=3/8$. Q14(d) solves
  $4/c^2=0.04$, so $c=10$. The only still-uncaptured prompts are Q1(c)--(d)
  and Q12(c)--(d) at that stage.
- A subsequent June 23 wave platform-confirmed Q1(b) $=23/126$ and both Q12(b)
  answers, $5/4$ and $3/8$. It exposed Q1(c), giving
  $P(X>Y)=66/126=11/21$, and Q12(c), giving
  $\operatorname{Var}(X)=59/720$, $\operatorname{Var}(Y)=1/15$, and
  $\operatorname{Cov}(X,Y)=-1/72$. At that stage, only Q1(d) and Q12(d)
  remained uncaptured.
  Q4's new paste merely showed its blank part-(b) field.
- The next wave platform-confirmed Q1(c) $=11/21$ and exposed Q1(d):
  $P(X+Y=13)=f(7,6)=13/126$. Q1 is now complete. Q12's paste was only a
  truncated repeat of part (a), so Q12(d) remains the sole uncaptured HW04
  prompt.
- The final captured Q12 part asks for $\operatorname{Var}(X+Y)$. The attempted
  $-1/72$ was rejected because that is only the covariance. Include the cross
  term:
  \[
  \operatorname{Var}(X+Y)=\frac{59}{720}+\frac1{15}
  +2\left(-\frac1{72}\right)=\frac{29}{240}.
  \]
  Q12(a)--(c) are platform-confirmed, and all supplied HW04 prompts are now
  captured.
- Q4's HTML showed Choice C selected without a correct grade. That choice
  confuses the joint density with the conditional density. The correct response
  is Choice A with $f(x\mid y)=2x/(2-y)^2$.
- Q17's first dropdown asks for the general formula
  $\rho_{XY}=\sigma_{XY}/(\sigma_X\sigma_Y)$; only after substitution does it
  reduce to $b/|b|$. Its next dropdown asks for covariance:
  $\sigma_{XY}=E[(X-\mu_X)(Y-\mu_Y)]=E(XY)-\mu_X\mu_Y$. The HTML did not
  preserve that dropdown's option list, so match whichever equivalent form is
  shown. Then use $\sigma_{XY}=b\sigma_X^2$ and $\sigma_Y=|b|\sigma_X$.
  A later incorrect-feedback hint emphasized the standard-deviation step:
  first obtain $\operatorname{Var}(Y)=b^2\sigma_X^2$, then
  $\sigma_Y=\sqrt{b^2\sigma_X^2}=|b|\sigma_X$. Never use $b\sigma_X$ when
  $b<0$.
  The full Q17 sequence is now visible: select
  $\sigma_{XY}/(\sigma_X\sigma_Y)$,
  $E[(X-\mu_X)(Y-\mu_Y)]$, $b\sigma_X^2$, and finally
  $\boxed{\sqrt{b^2\sigma_X^2}}$. Although
  $\sqrt{b^2\sigma_X^2}=|b|\sigma_X$ mathematically, the dropdown does not
  offer the absolute-value form; simplify only after making the square-root
  selection. All four formula selections were later platform-confirmed.
  Q17's multiple-choice step is **Choice A**, $\rho_{XY}=b/|b|$.
  Its last four sign dropdowns are, in order,
  **negative / positive / positive / positive**: for $b<0$, $b$ is negative
  but $|b|$ is positive; for $b>0$, both are positive.
- **Q6 ``Try again'' was a format rejection, not a wrong value.** The decimal
  $-0.5477$ was rejected because the prompt says ``exact answer, using
  radicals''; the accepted form is $-\sqrt{30}/10$. The generic ``That's
  incorrect'' dialogs on Q1, Q4, Q15 likewise carried no values (they restate
  definitions) --- the computed answers were right; enter them as exact
  fractions.
- Q6's on-screen joint table is behind an icon (not captured) but is fully
  determined by the multivariate hypergeometric (3 oranges, 2 apples, 2 bananas,
  choose 6).
- Core formulas used: marginal $g(x)=\sum_y/\int f$; conditional
  $f(y\mid x)=f(x,y)/g(x)$; independence iff $f=g(x)h(y)$ on a rectangular
  support; $\operatorname{Cov}=E(XY)-E(X)E(Y)$;
  $\rho=\operatorname{Cov}/(\sigma_X\sigma_Y)$;
  $\operatorname{Var}(aX+bY+c)=a^2\sigma_X^2+b^2\sigma_Y^2$ (independent);
  discrete uniform on $1..n$ has variance $\tfrac{n^2-1}{12}$; Chebyshev
  $P(|X-\mu|\ge k\sigma)\le 1/k^2$.
- Two judgment calls worth remembering:
  - **Q13 Chebyshev with a stated ``symmetric'' assumption ⇒ halve the bound.**
    660 hrs is $4\sigma$ below; one-tail $\le \tfrac{1}{2k^2}=\tfrac1{32}=3.125\%$
    (not $1/16$). The ``assume symmetric'' phrasing is the tell.
  - **A density that factors over a rectangular support ⇒ independent ⇒
    $\rho=0$** (Q16, $f=\tfrac{64y}{5x^3}$) --- don't grind through the integrals.
- Answers (all Python-verified; blank fields are computed, not confirmed):
  Q1 (a) $\tfrac{11}{42}$, (b) $\tfrac{23}{126}$,
  (c) $\tfrac{11}{21}$, (d) $\tfrac{13}{126}$;
  Q2 $g=0.3/0.7$, $h=0.26/0.49/0.25$; Q3 $\tfrac58$;
  Q4 not-indep, $\tfrac{45}{49}$; Q5 $0.045$; Q6 $-\tfrac{\sqrt{30}}{10}$;
  Q7 $\tfrac12$; Q8 (a) $3.8$, (b) $7.28$; Q9 $708$;
  Q10 (a) $25$, (b) $0$, (c) $156.25$; Q11 (a) $89.25$, (b) $52.5$;
  Q12 (a) not independent, (b) $\tfrac54,\tfrac38$,
  (c) $\tfrac{59}{720},\tfrac1{15},-\tfrac1{72}$,
  (d) $\tfrac{29}{240}$; Q13 $3.125\%$;
  Q14 (a) $\le\tfrac49$, (b) $\ge\tfrac59$, (c) $\ge\tfrac{21}{25}$,
  (d) $10$;
  Q15 $-\tfrac2{75}$; Q16 $0$;
  Q17 select $\tfrac{\sigma_{XY}}{\sigma_X\sigma_Y}$, then covariance
  $E[(X-\mu_X)(Y-\mu_Y)]$ (or $E(XY)-\mu_X\mu_Y$), then
  $\rho=\tfrac{b}{|b|}$.

## HW03 screenshot mapping (June 20, 2026 capture)

- The normalized original wave is `1.png` through `20.png`.
- Continuation screenshots currently include `3-2.png`, `3-3.png`, `11-2.png`,
  `13-2.png`, `14-2.png`, and `18-2.png`.
- `3-3.png` is **grading feedback**, not a new prompt: MyStatLab accepted
  $f(x)\ge0$ for all $x\in\mathbb{R}$ on Q3(a) and rejected $f(x)>0$ for $x>1$.
  Always re-read a grading screenshot before trusting a $>$/$\ge$ or domain
  blank.
- Q13 is now complete: parts (a)--(c) are all captured. Q13(c) (shorter than
  26.5 cm) computes to $0.0122$.
- Q14 is a **five-part** problem (a)--(e), all now captured. Q14(c) (misses
  coffee) $=1-P(15<T<25)$; MyStatLab recorded $0.6817$ (exact) as correct, so
  report $0.6817$ (table-rounded $0.6834$ is the alternative). Q14(d) (slowest
  15\% = 85th percentile) $=27+z_{0.85}(4.3)$: exact $z=1.0364\Rightarrow 31.457$
  min (table $z=1.04\Rightarrow 31.472$). Q14(e) is binomial: each trip
  independently takes $\ge\tfrac12$ hr with $p=0.2420$ (part a), so
  $P(2\text{ of }3)=\binom32(0.2420)^2(0.7580)\approx0.1332$. (d) and (e) had
  blank fields, so not yet platform-confirmed.
- Q11 is complete (a)--(e). Q11(c) (beta parameters of $f(y)=12(1-y)^{11}$):
  matching $\tfrac{1}{B(\alpha,\beta)}y^{\alpha-1}(1-y)^{\beta-1}$ gives
  $\alpha=1$, $\beta=12$ --- **graded correct**. Q11(d) (beta mean)
  $=\tfrac1{13}\approx0.0769$. Q11(e) (beta variance, round to **six** d.p.)
  $=\tfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}=\tfrac{12}{2366}
  \approx0.005072$. (d) and (e) had blank fields, so not yet platform-confirmed.
- **All HW03 prompts (Q1--Q20, every part) are now captured.** No prompts remain
  pending.
- A pasted "That's incorrect" feedback dialog (seen earlier on Q14) is only
  MyStatLab's generic z-table explanation --- it names no part and gives no
  value. Treat it as a signal to re-verify method/rounding, not as an answer
  source. (Q14(c) was later confirmed correct at $0.6817$ anyway.)
- When a screenshot header says "complete parts (a) through (e)," transcribe the
  full part count even if only some parts are visible; do not silently shorten
  it to the visible subset (Q14 was wrongly recorded as (a)--(c)).
- For HW03 Q16, MyStatLab's displayed conclusion compares the requested
  $P(Y>10)$ directly with the stated $0.35$ threshold. Use the platform-expected
  dropdown answer ``would'' with $P(Y>10)=0.2865$, even though the prose about a
  repair \emph{before} ten years is conceptually awkward.
- HW03 uses `q1.md` through `q20.md` for clean prompts and
  `solutions/q01.tex` through `solutions/q20.tex` for standalone worked
  solutions. `HW03/stat412_hw03_answer_key.tex` is the standalone answer-only
  sheet.

## HW02 screenshot mapping (June 20, 2026 capture)

- The normalized original wave is `1.png` through `17.png`.
- `13-2.png` is continuation material for Question 13.
- Supplemental files `11.md`, `13.md`, and `14.md` contain cumulative Poisson
  tables. The original large table transcriptions formerly stored in `q6.md`
  and `q8.md` were reference data; the clean `q6.md` and `q8.md` now contain
  the actual problem prompts.
- Question 13 is now complete: parts (a)--(c) are all captured (the part (c)
  prompt arrived as pasted HTML). Q13(c) (at least 5 accidents, Poisson
  $\lambda=5$) computes to $P(X\ge5)=1-0.4405=0.5595$; its MyStatLab field was
  still blank, so it is not yet platform-confirmed.
- HW02 uses `q1.md` through `q17.md` for clean prompts and
  `solutions/q01.tex` through `solutions/q17.tex` for standalone worked
  solutions. `HW02/stat412_hw02_answer_key.tex` is the standalone answer-only
  sheet.
