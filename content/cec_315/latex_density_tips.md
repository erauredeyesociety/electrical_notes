# LaTeX Density Tricks for Cheatsheets

A field manual for packing the most content per page into LaTeX cheatsheets
while keeping them legible. Focused on techniques that compile cleanly on
Overleaf with stock CTAN packages. Written for a signals & systems
cheatsheet but applies to any dense reference doc.

## 1. Paper setup: landscape + tight margins

**Why.** Letter landscape with 0.3 - 0.5 in margins gives you ~40 percent more
usable area than default portrait. The `geometry` package is the clean way to
set both at once; do not hand-roll `\textwidth`/`\oddsidemargin`.

```latex
\documentclass[10pt,landscape]{article}
\usepackage[letterpaper,landscape,margin=0.4in,includefoot=false]{geometry}
% Or for absolute max density:
% \usepackage[letterpaper,landscape,top=0.3in,bottom=0.3in,
%             left=0.3in,right=0.3in]{geometry}
\pagestyle{empty}     % kill header/footer; reclaim ~0.5 in vertical
```

If you need a landscape page inside a portrait doc, use `pdflscape`
(rotates the on-screen PDF page itself, not just the content).

Sources: [Overleaf page size & margins](https://www.overleaf.com/learn/latex/Page_size_and_margins),
[geometry package](https://texdoc.org/serve/geometry.pdf/0).

## 2. Multi-column layouts

**Why.** Two or three narrow columns beat one wide column for scanning short
formulas. The right tool is `multicol` (or `multicols*` for un-balanced
columns).

```latex
\usepackage{multicol}
\setlength{\columnsep}{0.3in}      % gap between columns
\setlength{\columnseprule}{0.2pt}  % hairline separator; set 0pt for none
\raggedcolumns                      % don't stretch last page to balance

\begin{multicols*}{3}              % * = unbalanced (fills top-down)
  ... content ...
  \columnbreak                     % force break into next column
  ...
\end{multicols*}
```

- `multicols` (no star): balances columns - good for print, last page looks
  tidy.
- `multicols*`: fills top-down; best for cheatsheets where you want content
  to read in order and not float.
- Avoid `paracol` unless you literally need side-by-side parallel text (e.g.
  English / translation). It is heavier and less battle-tested on Overleaf
  than `multicol`.
- `\columnbreak` nudges the breaker; don't fight it - if a section spills,
  move a small item up first.

Sources: [Overleaf multicol](https://www.overleaf.com/learn/latex/Multiple_columns),
[multicol manual](https://texdoc.org/serve/multicol/0).

## 3. Smaller base font: `extarticle`

**Why.** Stock `article` caps out at 10 pt. `extarticle` (from `extsizes`,
bundled with TeX Live and on Overleaf) supports 8 pt, 9 pt, 14 pt, 17 pt, 20
pt. Dropping from 10 pt to 9 pt buys you roughly one extra column of content
per page without hurting math rendering.

```latex
\documentclass[9pt,landscape]{extarticle}
```

In-doc shrinkage for a specific section - use declarative sizes:

```latex
{\footnotesize ... dense table ...}     % 8pt @ 9pt base
{\scriptsize  ... citations / notes ...} % 7pt @ 8pt base
% Reserve \tiny (5pt) for disclaimers; math is barely legible.
```

`\fontsize{8}{9.5}\selectfont` sets 8 pt text at 9.5 pt baseline for
fine-grained control. Always follow with `\selectfont`.

Sources: [extsizes on CTAN](https://ctan.org/tex-archive/macros/latex/contrib/extsizes),
[Overleaf font sizes](https://www.overleaf.com/learn/latex/Font_sizes%2C_families%2C_and_styles).

## 4. Microtype (adopt unconditionally)

**Why.** `microtype` enables character protrusion and font expansion, which
subtly tightens lines so fewer break too early. On dense cheatsheets you
routinely save 1 - 3 lines of reflow per column. Zero config for pdfLaTeX.

```latex
\usepackage{microtype}   % done. Seriously.
```

Overleaf supports this out of the box with pdfLaTeX; if you're using XeLaTeX
or LuaLaTeX, protrusion still works but expansion is limited. No action
needed for a standard cheatsheet.

Source: [microtype on CTAN](https://ctan.org/pkg/microtype?lang=en).

## 5. Compact section headings with `titlesec`

**Why.** Default `\section` eats 20+ pt of whitespace above and below. On a
cheatsheet that is catastrophic - collapse it.

```latex
\usepackage{titlesec}
\titleformat{\section}{\normalfont\bfseries\small}{}{0pt}{}
\titlespacing*{\section}{0pt}{4pt}{1pt}
\titleformat{\subsection}{\normalfont\bfseries\footnotesize}{}{0pt}{}
\titlespacing*{\subsection}{0pt}{3pt}{1pt}
```

- Starred `\titlespacing*` kills the following-paragraph indent.
- Arguments: `{left}{before}{after}` in pt or ex.
- The `[compact]` class option (`\usepackage[compact]{titlesec}`) is a quick
  blunt instrument; `\titlespacing*` gives finer control.

Sources: [CUED LaTeX squeezing space](https://help.eng.cam.ac.uk/cued-latex/latex-squeezing-space/),
[Hyndman squeezing space](https://robjhyndman.com/hyndsight/squeezing-space-with-latex/).

## 6. Compact lists with `enumitem`

**Why.** Default `itemize` / `enumerate` put ~6 pt between every item and
~\parskip above and below the list. On a page of 40 items that is half a
column wasted.

```latex
\usepackage{enumitem}
\setlist{nosep,leftmargin=*,labelsep=0.3em}   % global default

% Or per-environment:
\begin{itemize}[nosep,leftmargin=1.1em]
  \item tight
  \item tight
\end{itemize}
```

- `nosep` = `topsep=0pt,partopsep=0pt,parsep=0pt,itemsep=0pt`.
- `leftmargin=*` makes the label the margin (no dead left-gutter).
- Inline lists (write items comma-separated in running text) with the
  `inline` option save the most space for short lists:

```latex
\usepackage[inline]{enumitem}
Poles, zeros, and ROC:
\begin{itemize*}[label={},afterlabel={}]
  \item pole \item zero \item ROC
\end{itemize*}
```

Sources: [enumitem manual](https://ctan.math.illinois.edu/macros/latex/contrib/enumitem/enumitem.pdf),
[Overleaf Lists](https://www.overleaf.com/learn/latex/Lists).

## 7. Tight tables: booktabs + column-spec tricks

**Why.** `booktabs` rules look professional AND let you drop vertical rules
(which force extra padding). Killing the cell-edge whitespace with `@{}` on
the outer columns buys another few mm per row. `\arraystretch < 1` tightens
row height.

```latex
\usepackage{booktabs}
\usepackage{array}
\renewcommand{\arraystretch}{1.05}    % 1.0 = default; 0.95 is aggressive

\begin{tabular}{@{}l l l@{}}          % @{} removes outer padding
  \toprule
  $x(t)$            & $X(s)$              & ROC          \\
  \midrule
  $\delta(t)$       & $1$                 & all $s$      \\
  $u(t)$            & $1/s$               & $\Re\{s\}>0$ \\
  $e^{-at}u(t)$     & $\tfrac{1}{s+a}$    & $\Re\{s\}>-a$\\
  \bottomrule
\end{tabular}
```

For auto-sized columns to a fixed width, use `tabularx` with `X` columns:

```latex
\usepackage{tabularx}
\begin{tabularx}{\linewidth}{@{}l X l@{}}
  ... let middle column absorb slack ...
\end{tabularx}
```

`tabularray` is the modern LaTeX3 answer (keys like `stretch=0.9`, no need
for `\arraystretch` gymnastics). It is on Overleaf and stable, but the
learning curve is real; for a cheatsheet the booktabs combo above is enough.

Sources: [LaTeX Table Tricks (Robson)](https://people-ece.vse.gmu.edu/~hayes/Resources/TableTricks.pdf),
[booktabs docs](https://ctan.org/pkg/booktabs).

## 8. Math spacing: kill display skips, use `\tfrac`

**Why.** Default `\abovedisplayskip` and `\belowdisplayskip` are each 12 pt
plus glue. On a cheatsheet with 20 displayed equations, that is roughly a
full column of empty space.

```latex
\setlength{\abovedisplayskip}{2pt plus 1pt minus 1pt}
\setlength{\belowdisplayskip}{2pt plus 1pt minus 1pt}
\setlength{\abovedisplayshortskip}{1pt plus 1pt minus 1pt}
\setlength{\belowdisplayshortskip}{1pt plus 1pt minus 1pt}
```

For persistence across size-changes (`\footnotesize` resets the skips),
add to `\normalsize` and friends:

```latex
\makeatletter
\g@addto@macro\normalsize{%
  \setlength\abovedisplayskip{2pt}%
  \setlength\belowdisplayskip{2pt}%
  \setlength\abovedisplayshortskip{1pt}%
  \setlength\belowdisplayshortskip{1pt}%
}
\makeatother
```

Inline math tricks:

- `\tfrac{a}{b}` instead of `\frac` inline - text-style fraction, doesn't
  blow up line height.
- `\dfrac{a}{b}` only where you want a display-style fraction inside inline
  math (rare on cheatsheets).
- `\substack{k=1 \\ k \ne j}` for multi-line sub/superscripts without the
  overhead of a full `\begin{array}`.
- `$...$` over `\[...\]` whenever the math fits on the line.
- Stack narrow equations with `aligned` inside one `$...$` or one display
  block, not successive `\[...\]`:

```latex
\[\begin{aligned}
  H(s) &= \tfrac{1}{s+a} \\
  |H(j\omega)| &= \tfrac{1}{\sqrt{a^2+\omega^2}}
\end{aligned}\]
```

Sources: [Overleaf \abovedisplayskip](https://www.overleaf.com/learn/latex/%5Cabovedisplayskip_and_related_commands),
[fraction commands](https://sascha-frank.com/fractions.html).

## 9. Side-by-side mini-blocks with `minipage`

**Why.** Two narrow tables next to each other use vertical space more
efficiently than one wide table or two stacked tables. Works inside a
`multicols` column too.

```latex
\noindent
\begin{minipage}[t]{0.48\linewidth}
  \begin{tabular}{@{}l l@{}}
    \toprule
    CT pole & stability \\
    \midrule
    $\Re\{p\}<0$ & stable \\
    $\Re\{p\}>0$ & unstable \\
    \bottomrule
  \end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.48\linewidth}
  \begin{tabular}{@{}l l@{}}
    \toprule
    DT pole & stability \\
    \midrule
    $|p|<1$ & stable \\
    $|p|>1$ & unstable \\
    \bottomrule
  \end{tabular}
\end{minipage}
```

- Use `[t]` alignment so tops line up.
- No blank line between minipages or TeX inserts a paragraph break.
- Widths must sum to < 1.0 of `\linewidth` to leave room for the gutter.

Source: [Placing tables side-by-side](https://texblog.org/2007/08/01/placing-figurestables-side-by-side-minipage/).

## 10. Mix prose, tables, and bullets deliberately

**Why.** A column of pure prose creates grey slabs the eye slides off.
Alternate formats every 3 - 6 lines. Good pattern:

1. Bold lead-in + 1-sentence definition.
2. Table of cases / pairs.
3. Bullet list of gotchas.
4. One or two displayed key equations.
5. Repeat.

Concretely, break up long prose with inline math and bold keywords:

```latex
\textbf{ROC:} vertical strip in the $s$-plane; never contains poles.
\textbf{Causal:} $\Re\{s\} > \sigma_{\max}$. \textbf{Stable:} $j\omega$-axis
$\subset$ ROC.
```

This reads faster than a 3-line paragraph and occupies less space.

## 11. Overleaf-specific notes

- All packages listed here are in the Overleaf TeX Live distribution. No
  manual install required.
- Set Overleaf compiler to **pdfLaTeX** - fastest, full `microtype` support,
  no Unicode-font gymnastics needed.
- If the cheatsheet overflows to a new page by a few lines, check the
  "Logs and output files" pane for `Overfull`/`Underfull` warnings before
  randomly shrinking things - usually one bad `\columnbreak` or a single
  long equation is the cause.
- Draft mode in Overleaf disables `microtype` automatically for faster
  compiles; remember to switch it off before the final PDF.

Source: [LODE Publishing on Overleaf Optimizer](https://lodepublishing.com/blog/the-overleaf-optimizer-intelligent-latex-compilation-for-speed-and-quality/).

## 12. Common pitfalls that waste space

- **`\\[2ex]` or blank lines after every section.** `\parskip=1pt` +
  `titlesec` spacing is plenty; stop adding manual glue.
- **Full `\begin{equation}` blocks with labels** you never reference.
  Use `\[ ... \]` instead; one less line of whitespace and no equation
  number sticking into the gutter.
- **`\begin{center} ... \end{center}`** adds vertical space. Use
  `{\centering ... \par}` or `\centerline{...}` to center without the
  padding.
- **Vertical rules (`|`) in tables.** Forces extra cell padding and looks
  bad. `booktabs` philosophy: horizontal rules only.
- **Redundant `\noindent`** when `\parindent=0pt` is already set globally.
- **`\newpage` or `\clearpage`** forcing white space. On a 2-page
  cheatsheet, let `multicols*` flow naturally.
- **Orphan headings** at column bottoms. Move the heading down with a
  `\columnbreak` before it, or use `\needspace{3\baselineskip}` (from
  `needspace` package) to require minimum space below.
- **Huge `\tiny` walls of text.** 5 pt is unreadable under exam stress.
  Floor is `\scriptsize` (7 pt at 9 pt base).
- **Using `array` or `matrix` as a list substitute.** Bullets with
  `enumitem` + `nosep` are smaller and kern correctly.
- **Fighting `multicols` balancing.** If last page looks ugly, use
  `multicols*` and `\raggedcolumns`; do not insert `\vfill` hacks.

## 13. Starter preamble for a dense cheatsheet

Copy-paste and tune. Compiles with pdfLaTeX on Overleaf.

```latex
\documentclass[9pt,landscape]{extarticle}

% ---- page geometry ----
\usepackage[letterpaper,landscape,margin=0.35in]{geometry}
\pagestyle{empty}

% ---- columns ----
\usepackage{multicol}
\setlength{\columnsep}{0.3in}
\setlength{\columnseprule}{0.2pt}

% ---- math ----
\usepackage{amsmath, amssymb, mathtools}
\setlength{\abovedisplayskip}{2pt plus 1pt minus 1pt}
\setlength{\belowdisplayskip}{2pt plus 1pt minus 1pt}
\setlength{\abovedisplayshortskip}{1pt plus 1pt minus 1pt}
\setlength{\belowdisplayshortskip}{1pt plus 1pt minus 1pt}
\makeatletter
\g@addto@macro\normalsize{%
  \setlength\abovedisplayskip{2pt}%
  \setlength\belowdisplayskip{2pt}%
  \setlength\abovedisplayshortskip{1pt}%
  \setlength\belowdisplayshortskip{1pt}%
}
\makeatother

% ---- tables ----
\usepackage{booktabs}
\usepackage{array}
\usepackage{tabularx}
\renewcommand{\arraystretch}{1.02}

% ---- lists ----
\usepackage[inline]{enumitem}
\setlist{nosep,leftmargin=*,labelsep=0.3em}

% ---- headings ----
\usepackage{titlesec}
\titleformat{\section}{\normalfont\bfseries\small}{}{0pt}{}
\titlespacing*{\section}{0pt}{4pt}{1pt}
\titleformat{\subsection}{\normalfont\bfseries\footnotesize}{}{0pt}{}
\titlespacing*{\subsection}{0pt}{3pt}{1pt}

% ---- typography ----
\usepackage{microtype}
\usepackage{parskip}
\setlength{\parskip}{1pt}
\setlength{\parindent}{0pt}

% ---- shorthands ----
\renewcommand{\Re}{\operatorname{Re}}
\DeclareMathOperator{\sinc}{sinc}

\begin{document}
\begin{center}\textbf{Course --- Exam Cheatsheet}\end{center}

\begin{multicols*}{3}
  \raggedcolumns
  \section*{First topic}
  ... content ...
\end{multicols*}
\end{document}
```

## Quick checklist before submitting

- [ ] Landscape + `geometry` margins <= 0.4 in.
- [ ] `extarticle` at 9 pt (or `article` 10 pt with `\footnotesize` bulk).
- [ ] `microtype` loaded.
- [ ] `titlesec` heading spacing collapsed.
- [ ] `enumitem` global `nosep`.
- [ ] `\abovedisplayskip` / `\belowdisplayskip` reduced.
- [ ] `booktabs` tables, no vertical rules, `@{}` on outer columns.
- [ ] `\tfrac` inline; `\[...\]` over `equation`.
- [ ] No `\begin{center}`, no stray `\\[...]`, no `\newpage`.
- [ ] Visual rhythm: alternate prose / table / bullets every few lines.
