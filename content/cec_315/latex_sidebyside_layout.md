# LaTeX Side-by-Side Layouts: Tables Left, Prose Right

Companion to `latex_density_tips.md` and `latex_layout_tips.md`. Scope:
landscape-letter cheatsheet, ~15 narrow tables + ~15 prose/list blocks.
Goal: tables flush-left (no wrapped cells), prose fills whitespace to the
right. Overleaf + pdfLaTeX, stock CTAN. `multicols*{2}` (current) flows
top-to-bottom per column and leaves unfillable gaps under short tables.

---

## 1. `wrapfig` (`wraptable` / `wrapfigure`)

Declare a narrow float; prose after it fills the notch.

```latex
\usepackage{wrapfig}
\begin{wraptable}[N]{l}{2.4in}   % [N]=lines to reserve; l=left
  \begin{tabular}{@{}l l@{}} ... \end{tabular}
\end{wraptable}
Prose paragraph that wraps to the right of the table.
```

**Failure modes** (per the manual and well-known bug reports):

- `itemize`/`enumerate` adjacent to a wrap break the indent and overlap the
  table. Manual warns directly.
- `\section` between the float and the wrapped prose resets indentation.
- Page breaks: float splits, or prose ends and the notch persists into the
  next paragraph.
- **Inside `multicol`: unsupported**; silently mis-places.
- Footnotes reorder unpredictably near wrap floats.
- Prose shorter than table: next block lands INSIDE the notch and overlaps.
- Omitting `[N]` means `wrapfig` guesses height; guesses are often wrong.

**Verdict: CONDITIONAL.** Fine for a one-off sidebar in plain prose. **Not
viable** as the primary layout for 15 tables.

Sources: [wrapfig manual](https://texdoc.org/serve/wrapfig/0),
[Overleaf wrap](https://www.overleaf.com/learn/latex/Wrapping_text_around_figures).

---

## 2. `wrapfig2` (modern replacement)

Exists — Claudio Beccari's 2021+ replacement, same API. Fixes height
accounting, cooperates with `tcolorbox`/modern floats, better page-break
handling, adds a `parboxed` option for cleaner vertical spacing.

```latex
\usepackage{wrapfig2}
\begin{wraptable}{l}{2.4in}[2]   % [2] = hanging lines; differs from wrapfig
  ...
\end{wraptable}
```

Does **not** fix `multicol` incompatibility or "prose shorter than table".

**Verdict: CONDITIONAL — prefer over `wrapfig`** when you must wrap.

Source: [wrapfig2 on CTAN](https://ctan.org/pkg/wrapfig2).

---

## 3. `paracol`

Two parallel streams with independent content and column breaks. You
`\switchcolumn` between them mid-document.

```latex
\usepackage{paracol}
\columnratio{0.25}               % 0.25 * 10in = 2.5in left, 7.5in right
\setlength{\columnsep}{0.25in}

\begin{paracol}{2}
  \begin{tabular}{@{}l l@{}} ... \end{tabular}
  \switchcolumn                  % jump to right stream
  Prose block; sits in right column at its own height (no wrapping).
  \switchcolumn*                 % starred = resync to max height
  \begin{tabular}{@{}l l@{}} ... \end{tabular}
  \switchcolumn
  More prose.
\end{paracol}
```

Key features for this problem:

- Asymmetric 2.5 in / 7.5 in split via `\columnratio`.
- `\switchcolumn*` synchronizes vertical position (next content starts at
  max of the two current heights). Solves "match heights across pairs"
  natively.
- Content flows across page breaks cleanly.
- Each column has its own footnotes, floats, sections.

**Pitfalls**:

- Do NOT mix with `multicol` in the same document.
- `\switchcolumn` without `*` lets columns drift vertically until you sync.
- Some packages (`hyperref`, `titlesec`) need load-order care.
- No "text wraps around a table" — prose stays in its column (for this use
  case, a feature).

**Verdict: RECOMMEND.** Overrides the hint in `latex_density_tips.md` §2
("avoid paracol unless bilingual") — that applied to a simple flowed
cheatsheet; the side-by-side problem is paracol's purpose.

Sources: [paracol](https://ctan.org/pkg/paracol),
[paracol manual](https://mirrors.ctan.org/macros/latex/contrib/paracol/paracol-doc.pdf).

---

## 4. `picins`

Late-1980s in-paragraph picture inserts via `\parpic`; requires explicit
reserved box dimensions (eliminates wrapfig's height-guess failures).

```latex
\usepackage{picins}
\parpic(2.4in,1in)[l]{\begin{tabular}{@{}l l@{}} ... \end{tabular}}
Prose flows to the right.
```

**Pitfalls**: patches LaTeX paragraph-builder internals that `microtype`,
`enumitem`, and `hyperref` also touch → cryptic errors. No maintenance
since ~2010. German-only manual. Same list/page-break pitfalls as wrapfig.

**Verdict: AVOID.** `wrapfig2` fills the niche; `picins` is a liability.

Source: [picins on CTAN](https://ctan.org/pkg/picins).

---

## 5. Custom `\sideblock{TABLE}{PROSE}` via paired minipages

Home-grown macro; each block is self-contained and stacks vertically.

```latex
\newcommand{\sideblock}[2]{%
  \par\noindent
  \begin{minipage}[t]{2.4in}#1\end{minipage}\hfill
  \begin{minipage}[t]{7.2in}#2\end{minipage}\par\medskip}

\sideblock{\begin{tabular}{@{}l l@{}} ... \end{tabular}}{%
  Prose. Longer than the table? Right minipage extends; whitespace sits
  under the short table (acceptable — the goal was filling whitespace to
  the RIGHT, not below). Next \sideblock starts below the taller of the
  two.}
```

**Asymmetric heights**:

- Prose > table: desired behavior. Whitespace under the table is fine.
- Table > prose: whitespace below the prose inside the pair. Mitigate by
  writing longer prose, or by stacking two small prose items in the right
  minipage.

**Pitfalls**:

- **Unbreakable**: a single `\sideblock` taller than remaining page floats
  entirely to the next page, leaving a gap. Keep each block under ~4 in.
- No prose flow between blocks — each pair is independent.
- Manual width tuning.

**Verdict: RECOMMEND** as the simplest correct approach when you don't
want `paracol`'s load-order sensitivities.

Sources: [minipage pairing](https://texblog.org/2007/08/01/placing-figurestables-side-by-side-minipage/),
[matched-height](https://latex.org/forum/viewtopic.php?t=29060).

---

## 6. `multicol` + `\columnbreak` for left=tables, right=prose

Cannot work cleanly:

- `multicol` does not support unequal column widths (no `\columnratio`
  equivalent).
- Flow is top-to-bottom per column — putting all tables first then
  `\columnbreak` then all prose destroys the table-to-prose pairing.
- No primitive to say "this block goes in column 1". `\columnbreak` only
  ends the current column.

No package automates paired two-column layout on top of `multicol`. The
closest primitive is `paracol` (§3).

**Verdict: AVOID.**

---

## 7. Asymmetric `geometry` margin + `\marginpar` for tables

Wide left margin; tables live in the margin.

```latex
\usepackage[letterpaper,landscape,
  left=2.7in,right=0.35in,top=0.35in,bottom=0.35in,
  marginparwidth=2.2in,marginparsep=0.15in,reversemarginpar]{geometry}

\marginpar{\begin{tabular}{@{}l l@{}} ... \end{tabular}}
Prose to the right.
```

**Pitfalls**:

- `\marginpar` is a FLOAT — LaTeX shifts it vertically to avoid overlap
  with other margin items. With 15 tables, collisions and "marginpar
  moved" warnings are guaranteed.
- Hard limit of `\marginparwidth`; overflow gets clipped or bleeds.
- Margin content does not count toward page-fill — pages look short.
- Alignment with source paragraph drifts under heavy use.

A "custom env" that reserves a left region is equivalent to re-implementing
`\sideblock` (§5) or `paracol` (§3). Go there directly.

**Verdict: AVOID** for >3 margin items.

---

## 8. Anti-patterns — look good once, break at scale

- **`wraptable` inside `multicols*`**: fine on page 1, overlaps on page 2.
  Manual explicitly forbids.
- **`\noindent\tabular ... \hspace ... prose`**: prose wraps only on the
  first line; subsequent lines start at the left margin UNDER the table.
- **`\vspace{-1.2in}` after each table** to pull prose up: works on page 1,
  breaks catastrophically the moment earlier content changes height.
- **Nested `\hangindent` per paragraph**: `\hangindent` resets at `\par`.
  Unmaintainable for multi-paragraph prose beside a tall table.
- **`tcolorbox` `sidebyside` as a layout primitive**: fine as a call-out,
  too heavy and visually noisy for 15 blocks.
- **`floatflt`**: deprecated, removed from many distributions.
- **`cuted` / `strip`**: span columns for single blocks — opposite of this
  problem's need.

**Common thread**: anything relying on TeX's paragraph builder to flow
around a shape (wrapfig, picins, hangindent) breaks at page boundaries and
near non-prose. Anything using paired `minipage` or `paracol` bypasses the
paragraph builder and is robust.

---

## Decision tree

```text
Whole document is side-by-side table/prose?
├─ YES:
│  ├─ Need sync'd heights + flow across page breaks?  → paracol (§3)
│  └─ Independent short pairs, < 4in each?            → \sideblock (§5)
└─ NO, just a sidebar in mostly-prose:
   ├─ Real prose flow, float as sidebar?              → wrapfig2 (§2) w/ [N]
   └─ Wide margin + ≤ 3 items?                        → \marginpar (§7)
```

For a landscape-letter cheatsheet with 15 tables + 15 prose blocks:
**paracol** if you want continuous cross-page flow; **`\sideblock`** if
each pair is self-contained.

---

## Prototype sketch (Overleaf-compilable)

```latex
\documentclass[9pt,landscape]{extarticle}
\usepackage[letterpaper,landscape,margin=0.35in]{geometry}
\usepackage{paracol}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{booktabs,array,tabularx}
\usepackage[inline]{enumitem}
\usepackage{titlesec}
\usepackage{microtype}
\usepackage{parskip}

\pagestyle{empty}
\setlist{nosep,leftmargin=*,labelsep=0.3em}
\titleformat{\section}{\normalfont\bfseries\small}{}{0pt}{}
\titlespacing*{\section}{0pt}{4pt}{1pt}
\renewcommand{\arraystretch}{1.02}
\setlength{\parskip}{1pt}
\setlength{\parindent}{0pt}
\setlength{\abovedisplayskip}{2pt}
\setlength{\belowdisplayskip}{2pt}

\columnratio{0.25}             % 2.5in left, 7.5in right on 10in textwidth
\setlength{\columnsep}{0.25in}

\begin{document}
\begin{paracol}{2}

\section*{Laplace pairs}
\begin{tabular}{@{}l l@{}}
  \toprule $x(t)$ & $X(s)$ \\ \midrule
  $\delta(t)$   & $1$       \\
  $u(t)$        & $1/s$     \\
  $e^{-at}u(t)$ & $1/(s+a)$ \\
  \bottomrule
\end{tabular}

\switchcolumn
\section*{ROC and causality}
ROC is a vertical strip in the $s$-plane that never contains a pole. A
causal signal has $\mathrm{Re}\{s\} > \sigma_{\max}$; stability requires
the $j\omega$-axis to lie inside the ROC, equivalent to all poles having
negative real part.

\switchcolumn*                 % resync to max height before next pair

\begin{tabular}{@{}l l@{}}
  \toprule DT pole & stability \\ \midrule
  $|p|<1$ & stable   \\
  $|p|=1$ & marginal \\
  $|p|>1$ & unstable \\
  \bottomrule
\end{tabular}

\switchcolumn
For DT systems, stability is determined relative to the unit circle. The
bilinear transform $s = \tfrac{2}{T}\tfrac{z-1}{z+1}$ maps the left
half-plane to the interior of the unit circle, preserving stability
across CT/DT conversions.

\switchcolumn*
\end{paracol}
\end{document}
```

Add more pairs by repeating the `\switchcolumn` / `\switchcolumn*`
alternation. Page breaks handled automatically.
