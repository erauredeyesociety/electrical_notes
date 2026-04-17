% LaTeX Layout Tips for Dense Cheatsheets

Companion to `latex_density_tips.md`. That file *shrinks*; this one
*packs* - rotation, fit-scaling, breaking out of `multicol`, minipage
pairs, for when blocks are the wrong *shape* for their column. Scope:
Overleaf + pdfLaTeX, stock CTAN.

## 1. Rotating elements

**Why + when.** A 3.5 in table won't fit a 3 in column but fits a 5 in
slot rotated 90 degrees. Use when a block is wider than any column you
could realistically create.

```latex
\usepackage{graphicx}       % \rotatebox
\usepackage{rotating}       % sidewaystable float

\rotatebox{90}{\begin{tabular}{@{}l l l@{}} ... \end{tabular}}

\begin{sidewaystable}       % full-page rotated float
  \begin{tabular}{...} ... \end{tabular}
\end{sidewaystable}
```

- `\rotatebox{90}{...}` (`graphicx`): inline, keeps content in flow.
- `sidewaystable` / `sidewaysfigure` (`rotating`): whole-page float.
- `pdflscape` (Section 10): one landscape PDF page in a portrait doc.

**Pitfall.** `\rotatebox` inside `multicols` doesn't reserve height
correctly - TeX sees the pre-rotation bounding box. Wrap in `\parbox`
with explicit height or `\makebox[0pt]` + `\vspace`. Rotation is a
readability tax; reserve for reference tables, never prose.

Sources: [rotating](https://texdoc.org/serve/rotating/0),
[LaTeX/Rotations](https://en.wikibooks.org/wiki/LaTeX/Rotations).

---

## 2. Scaling to fit

**Why + when.** Block is 5 - 10% too wide and you need a one-knob fix.
`adjustbox` with `max width` is the best idiom: shrinks only if needed,
leaves content untouched otherwise.

```latex
\usepackage{adjustbox}
\begin{adjustbox}{max width=\columnwidth}
  \begin{tabular}{@{}p{3in} p{1.7in}@{}} ... \end{tabular}
\end{adjustbox}
```

- `\scalebox{0.9}{...}` - fixed factor.
- `\resizebox{\columnwidth}{!}{...}` - scale to exact width, `!` keeps
  aspect. Always shrinks or grows; no "only if needed" gating.
- `adjustbox` `max width=\columnwidth` - conditional shrink. Preferred.

**Pitfall.** Scaling math blurs exponents and makes fonts mismatch
neighboring text. **Never scale equations or inline math** - drop a font
size or rewrite instead. Safe on tabular rows of plain text.

Sources: [adjustbox](https://ctan.org/pkg/adjustbox),
[resizebox ref](https://latexref.xyz/_005cresizebox.html).

---

## 3. Breaking out of multicol

**Why + when.** A block wider than one column but narrower than the page
won't fit *anywhere* in `multicols*{2}`. Close the env, drop the wide
block, reopen.

```latex
\end{multicols*}

\noindent\begin{tabular}{@{}p{2.8in} p{2.8in} p{2.2in}@{}}
  ... full-width block ...
\end{tabular}

\begin{multicols*}{2}
  \raggedcolumns
  ... resume ...
```

**Pitfall.** Closing and reopening `multicols*` can leave a half-empty
column above the wide block (mid-page break). Fixes:

- Place the wide block at page top or bottom (no slack around it).
- `\columnbreak` just before `\end{multicols*}` forces a flush.
- `\begin{table*}` / `\begin{figure*}` (star-forms) span full page *without*
  closing `multicols`; plain `table`/`figure` floats error inside
  `multicols` and are forbidden.

Sources: [multicol manual](https://texdoc.org/serve/multicol/0),
[Overleaf multicol](https://www.overleaf.com/learn/latex/Multiple_columns).

---

## 4. Side-by-side blocks

**Why + when.** Two narrow tables stacked waste right-side slack in each.
Tile them with `minipage` + `\hfill`. **Biggest-ROI fix for the
"table is narrower than column" problem.**

```latex
\noindent
\begin{minipage}[t]{0.48\columnwidth}
  \begin{tabular}{@{}l l@{}}
    \toprule CT & stab. \\ \midrule
    Re<0 & stable \\ \bottomrule
  \end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{0.48\columnwidth}
  \begin{tabular}{@{}l l@{}} ... \end{tabular}
\end{minipage}
```

- `minipage` + `\hfill` - default choice, works inside `multicols`.
- `paracol` - for parallel streams with independent column breaks
  (bilingual text). Overkill here.
- `subcaption` - only if you need sub-labels (a), (b).

**Pitfall.** A blank line between `\end{minipage}` and next
`\begin{minipage}` inserts a paragraph break - they stack vertically
instead of tiling. Widths must sum to less than 1.0 to leave gutter room.
Use `[t]` on both; default `[c]` centers on baseline, misaligning tops.

Source: [minipage side-by-side](https://texblog.org/2007/08/01/placing-figurestables-side-by-side-minipage/).

---

## 5. Intelligent floats (wrapfigure / marginpar)

**Why + when.** `wrapfigure` / `wraptable` let prose flow around a narrow
float. **Payoff is modest on a cheatsheet** - it helps when you have real
paragraph prose; not when you have formulas and tables.

```latex
\usepackage{wrapfig}
\begin{wraptable}{r}{2.2in}
  \begin{tabular}{@{}l l@{}} ... \end{tabular}
\end{wraptable}
Prose that flows around the table on the left ...
```

**Pitfall.** `wrapfig` breaks near:

- List environments (`itemize`, `enumerate`) - manual warns directly.
- Section headings and displayed equations.
- Page breaks (visible gaps, collisions).
- Inside `multicols` - often misbehaves.

`\marginpar` requires fat margins; on a 0.25 in-margin cheatsheet the
margin is effectively zero. Skip.

Sources: [wrapfig manual](https://texdoc.org/serve/wrapfig/0),
[Overleaf wrap](https://www.overleaf.com/learn/latex/Wrapping_text_around_figures).

---

## 6. Column balancing and gaps

**Why + when.** Ugly vertical gaps between paragraphs inside `multicols`
are usually *forced balancing* stretching glue to equalize column
heights. Fix with `\raggedcolumns`.

```latex
\begin{multicols*}{2}
  \raggedcolumns                % columns can end at different heights
  ... content ...
  \columnbreak                  % hard force break
  ...
\end{multicols*}
```

- `\raggedcolumns` (inside env) - allow uneven column bottoms. **Single
  biggest fix for "why are there huge gaps"**.
- `\flushcolumns` - default; aligns both top and bottom baselines, which
  creates the gaps you're seeing.
- `\columnbreak` - force break. `multicol` manual notes it acts more like
  `\newpage` than `\pagebreak` - use sparingly, once per page max.
- `\setcounter{unbalance}{3}` - bias left column 3 lines longer.

**Pitfall.** `multicols` (no star) balances by design; use
`multicols*` with `\raggedcolumns` for cheatsheets where last page is
naturally short.

Source: [multicol manual](https://texdoc.org/serve/multicol/0).

---

## 7. Tight-fit tables: exact column width

**Why + when.** Default `tabular` auto-sizes columns to widest cell,
producing either (a) table narrower than column (right-side whitespace)
or (b) table wider than column (overflow). **Tell TeX the exact width.**

```latex
% (a) tabularx: X columns expand to fill a fixed total
\usepackage{tabularx}
\begin{tabularx}{\columnwidth}{@{}l X l@{}}
  \toprule Topic & Description & Ref \\
  \midrule ... \bottomrule
\end{tabularx}

% (b) manual p{} columns summing to \columnwidth
\begin{tabular}{@{}p{1.2in} p{2.0in} p{1.6in}@{}} ... \end{tabular}

% (c) tabularray - modern LaTeX3, best syntax, steeper curve
\begin{tblr}{width=\columnwidth, colspec={X[1,l] X[2,l] X[1,l]}} ... \end{tblr}
```

**Pitfall.** With `p{}` columns, `\tabcolsep` (~6 pt each side) is added
*between* columns. Use `@{}` on outer columns to kill edge padding;
widths then sum cleanly to `\columnwidth`. Middle columns can use
`@{\hspace{2pt}}` to reduce but keep separation.

`tabularx` with one `X` column absorbing slack is the fastest "no
whitespace, no overflow" route.

Sources: [tabularx](https://texdoc.org/serve/tabularx/0),
[Fixed-width FAQ](https://texfaq.org/FAQ-fixwidtab).

---

## 8. Width-matched multi-table pairing

**Why + when.** Section 4's minipage pair aligns tops. If you also want
**matched heights** (for visual rhythm or so the next block starts flat),
set a fixed height on both minipages.

```latex
\begin{minipage}[t][1.8in][t]{0.48\columnwidth}
  \begin{tabular}{@{}l l@{}} ... \end{tabular}
\end{minipage}\hfill
\begin{minipage}[t][1.8in][t]{0.48\columnwidth}
  \begin{tabular}{@{}l l@{}} ... \end{tabular}
\end{minipage}
```

Optional args are `[outer-align][height][inner-align]`. `[t][1.8in][t]`
means top-align the box and top-align content inside (overflow grows
downward; short content leaves whitespace below).

No stock "auto-match height" package; trick is `\settoheight` across two
passes. For cheatsheets, eyeball and hard-code.

**Pitfall.** Over-specify height and short content looks buggy (padding
gap). Under-specify and content collides with the next block.

Source: [equal-height side-by-side](https://latex.org/forum/viewtopic.php?t=29060).

---

## 9. Horizontal space reclamation

**Why + when.** Block is *almost* fitting (0.1 - 0.2 in over). Push it
leftward past the column margin.

```latex
\noindent\hspace*{-0.1in}%
\begin{tabular}{@{}p{3.0in} p{1.8in}@{}} ... \end{tabular}
```

- `\hspace{-Xin}` back-spaces (negative length).
- `\hspace*{...}` survives line breaks; use at start of line.
- `@{\hspace{-2pt}}` in a column spec eats inter-column padding.
- `\hfill` - positive infinite glue; absorbs slack in minipage pairs.

**Pitfall.** In `multicols`, pushing leftward can collide with
`\columnseprule` or the adjacent column. Check the PDF visually (log
won't warn). If you're fighting negative hspace on every block, you
need a smaller font or more columns, not a bandaid.

Sources: [hspace ref](https://latexref.xyz/_005chspace.html),
[narrower table margins](https://latex.org/forum/viewtopic.php?t=2579).

---

## 10. Landscape pages inside portrait (`pdflscape`)

**Why + when.** Cheatsheet is already landscape; this is for the
*reverse* case - a mostly-portrait doc with one landscape reference page.

```latex
\usepackage{pdflscape}
\begin{landscape}
  \begin{tabular}{...wide...} ... \end{tabular}
\end{landscape}
```

`pdflscape` sets PDF `/Rotate` so viewers show the page correctly. Plain
`lscape` only rotates text on the page (page itself stays portrait -
sideways when read on screen). Use `pdflscape` for on-screen; either for
print.

**Pitfall.** Headers/footers rotate with the content. No package mixes
portrait and landscape *on the same page*; rotate individual blocks with
`\rotatebox` (Section 1) instead. For landscape cheatsheets, set
`landscape` in the class/geometry options from the start - don't try to
rotate one page of a portrait doc to simulate a cheatsheet.

Sources: [pdflscape](https://ctan.org/pkg/pdflscape),
[TeX FAQ landscape](https://texfaq.org/FAQ-landscape).

---

## Decision tree

### Block is TOO WIDE for the column

1. **< 10% over**: `adjustbox` `max width=\columnwidth` (Section 2). Not
   for math.
2. **Table, barely over**: switch to `tabularx` with `X` column, add
   `@{}` on outer columns so widths sum clean (Section 7).
3. **Still over, but less than half a column**: `\noindent\hspace*{-0.1in}`
   leftward bleed (Section 9). Check visually.
4. **Wider than column, narrower than page**: close `multicols*`, drop
   full-page block, reopen (Section 3). Place at page top/bottom.
5. **Wider than page or many columns**: `\rotatebox{90}` or
   `sidewaystable` (Section 1), or `pdflscape` page (Section 10).

### Block is TOO TALL for the column

1. Split into `minipage` pair, tile side-by-side (Section 4) - cuts
   height ~in half. **Highest ROI.**
2. Split into two tables with matched heights (Section 8).
3. `\columnbreak` to push to a fresh column if orphaned at a bottom.
4. Reconsider the form: inline `itemize*` (density tips Section 6) may
   use 60% less vertical for the same info.

### Block is TOO NARROW (right-side whitespace)

1. **Convert to `tabularx` with `X` absorbing slack** (Section 7).
2. **Pair with another narrow block via `minipage` + `\hfill`**
   (Section 4). Top ROI for this problem.
3. Widen one `p{}` column to sum to `\columnwidth`.
4. Add a useful third column (cross-ref, page, example) to soak slack.

### Columns have vertical gaps

1. Add `\raggedcolumns` inside `multicols*` (Section 6). Fix 90% of
   cases.
2. Remove stray `\vspace`, `\\[2ex]`, blank lines before headings.
3. Switch `multicols` (balanced) -> `multicols*` (unbalanced).
4. List gaps: check `enumitem` global `nosep`.

### Content won't fit at all

1. Drop font: 10pt -> 9pt -> 8pt (density tips Section 3).
2. Shrink margins (density tips Section 1).
3. Add a column: `multicols*{3}`.
4. Cut low-value prose; keep tables and key equations.
5. Accept a second page. Legible 2-page > `\tiny` 1-page.
