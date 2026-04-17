# CEC 315 Exam 3 Cheatsheet — Design Notes

Running log of design decisions, applied techniques, known issues, and pending ideas for [exam3_cheatsheet.tex](exam3_cheatsheet.tex). Append new entries at the bottom of each section; don't delete.

See also:

- [latex_density_tips.md](../latex_density_tips.md) — research: density tricks
- [latex_layout_tips.md](../latex_layout_tips.md) — research: layout/rotation/packing tricks
- [latex_sidebyside_layout.md](../latex_sidebyside_layout.md) — research: tables-on-left / prose-on-right patterns (wrapfig vs paracol vs minipage)
- [html_pagination_tips.md](../html_pagination_tips.md) — research: Paged.js, `@page` sizing, index-card printing (may still be in-progress; see file)
- [estimate_pages.py](estimate_pages.py) — page-count heuristic
- [cheatsheet_fitter.py](cheatsheet_fitter.py) — experimental auto-packer

---

## Current design choices

| Decision | Value | Rationale |
| --- | --- | --- |
| Paper | Landscape letter (11 × 8.5 in) | Two-column flow; fits tables + prose side-by-side |
| Margins | 0.25 in | Tight; reclaims edge space |
| Columns | 2 via `multicols*` | Wider columns fit the Z-pair math; 3-col was too narrow |
| Base font | 12pt via `extarticle` | Shrink-proof: 20% larger than standard 10pt cheatsheet; estimator says ~3 pages |
| Column sep | 0.3 in with thin rule | Visual separation without blur |
| Display-math skips | 4 pt above/below | Reclaimed whitespace around `\[ ... \]` |
| Section heading | `\large` bold via `titlesec` | Compact vertical spacing (6 pt/2 pt) |
| List spacing | `nosep`, `itemsep=1pt`, `topsep=1pt` | Kills default `\parskip` padding |
| Array stretch | 1.05 | Slightly more readable than default 1.0 |

## Applied techniques

| Technique | Where | Why it helped |
| --- | --- | --- |
| `\raggedcolumns` | Inside `multicols*` | Prevents forced balancing that creates inter-block gaps |
| `\twoup{}{}` minipage macro | Laplace/Z Properties section | Pairs two narrow 2-col tables side-by-side; kills right-side whitespace |
| `tabularx` with `X` column | Coverage Checklist | `X` absorbs column slack exactly; no wrap/overflow |
| `extarticle` class | Preamble | Enables non-standard font sizes (8, 9, 11, 12, 14, 17, 20) |
| `microtype` | Preamble | Better line-breaking + kerning; modest density win |
| `@{}` column specs | All tables | Remove outer padding |
| `\tfrac` instead of `\frac` | All inline fractions | 30% height reduction in fractions |
| Pull Coverage Checklist back INSIDE `multicols*` | Post-fix | Breaking out of multicols caused an orphan page |

## Known issues

1. **Laplace Pairs table** (line ~75) doesn't use full column width — leaves right-side whitespace within the column. **Fix (applied):** switch to `tabular*{\columnwidth}{@{\extracolsep{\fill}}l l l@{}}` so columns stretch to fill.
   - Same issue was likely on Z Pairs table; same fix applied.

2. **`cheatsheet_fitter.py` width estimator is conservative.** Reports real 4.3in-wide tables as 9.3in wide, causing false "oversized" flags. Workaround: re-run with `--pages 4+` or trust Overleaf render. Needs calibration of width heuristic (char-width × chars vs. actual latex sizing).

3. **Multi-page flow with `\raggedcolumns` + `multicols*`.** Observed: page ~N-1 sometimes has short column (large gap) before page N starts fresh. Not critical for screenshot workflow; flagged as a LaTeX behaviour that can't be fully fixed without hand-tuning `\columnbreak`.

4. **Chrome Ctrl+P fills Letter paper, not 6×4** (v10 HTML). Root cause: `@page size: 6in 4in` is a *hint* — Chrome's print dialog defaults to system paper size and may scale content up to fit. **Workaround:** Ctrl+P → Destination: "Save as PDF" → More settings → Paper size: Custom 6×4 in → Margins: None → Scale: Default → Save. The resulting PDF is a genuine 6×4. For physical print, either (a) save-PDF first then print with "Fit to page" on Letter, or (b) use a printer that accepts 6×4 index cards with the paper tray configured. Not a CSS bug.

## Pending ideas

- **Rotated side labels.** `\rotatebox[origin=c]{90}{\textbf{CT/DT}}` placed in a left minipage next to a wide table, rotated 90° CCW. Demo on "CT vs DT Quick Reference" section. Possible "chapter strip" visual style.
- **Split Laplace Pairs into "fundamental" + "damped sinusoid" blocks.** The damped-sinusoid rows could pair side-by-side with the analogous Z damped-sinusoid block. Structural parallel is visually clean.
- **Typst port.** If LaTeX layout pain continues, Typst offers similar math rendering with a more programmable layout model. Worth a spike if the cheatsheet becomes a long-lived artifact.
- **Color-tinted section boxes.** `mdframed` or `tcolorbox` with subtle tint per major topic (Laplace vs Z vs Sampling vs Feedback). Aids scanning when zoomed-out.
- **Auto page-count CI.** Run `estimate_pages.py` on every edit; flag when >3 pages. Keeps the cheatsheet honest as content is added.

## Edit log

*Append one line per structural change. Short form: date — what — why.*

- 2026-04-16 — Initial 10pt 2-col layout with comprehensive pairs/properties/PFE/sampling/feedback/traps sections.
- 2026-04-16 — Bumped to 20pt, hit 7 pages. Too aggressive.
- 2026-04-16 — Settled on 14pt 2-col, removed title block. ~4 pages.
- 2026-04-16 — Applied `\raggedcolumns`, `\twoup` pairing of L/Z Properties, `tabularx` for Coverage. ~3.5 pages.
- 2026-04-16 — Bumped font down to 12pt, pulled Coverage back into `multicols*`. ~3 pages.
- 2026-04-16 — `tabular*{\columnwidth}` stretch on Laplace Pairs + Z Pairs tables to kill right-side whitespace. Demo rotated side label on CT vs DT table.
- 2026-04-16 — Observed issue: Laplace Pairs column width now stretches, but table is still shorter than column height → vertical whitespace below it within the column. Root cause: `multicols*` flows content vertically; short tables leave unfillable dead space.
- 2026-04-16 — Started prototype [exam3_cheatsheet_v2_sidelayout.tex](exam3_cheatsheet_v2_sidelayout.tex): abandons `multicols`, uses single-column landscape with a `\sideblock{table}{prose}` macro. Tables stack on the left (narrow, ~2.8in), prose flows on the right (~7.3in) filling whitespace. A/B candidate vs the multicol version.
- 2026-04-16 — Research agent delivered [latex_sidebyside_layout.md](../latex_sidebyside_layout.md) (326 lines, 8 techniques + decision tree). Recommends `paracol` over minipage because minipages are unbreakable (orphan risk). wraptable flagged as a trap.
- 2026-04-16 — Built v3 prototype [exam3_cheatsheet_v3_paracol.tex](exam3_cheatsheet_v3_paracol.tex) using `paracol` with `\columnratio{0.26}` and `\switchcolumn*` between 6 table/prose pairs. Handles page breaks cleanly.
- 2026-04-16 — User critique of v3: all tables forced to uniform column width (can't shrink-to-content); prose paragraphs separated by visible `\parskip` gaps (can't flow continuously to match tall tables). v3 relegated to reference.
- 2026-04-16 — Built v4 prototype [exam3_cheatsheet_v4_wraptable.tex](exam3_cheatsheet_v4_wraptable.tex) using `wraptable` with `{0pt}` natural-width argument per table; `\parskip=0pt plus 1pt` for continuous prose flow; `\FloatBarrier` (placeins) between major sections. Each table minimizes its own height, prose genuinely wraps around it.
- 2026-04-16 — Deleted v2, fitted, and allnotes_landscape files (listed in "Deleted versions" above).
- 2026-04-16 — Built v4 prototype with `wraptable {0pt}`. Compile revealed concrete overlaps: Laplace Properties rows collided with Sampling heading; Traps paragraph squeezed between two tables; Feedback GM/PM table landed overlapping adjacent prose. wraptable confirmed unreliable at 6+ tables.
- 2026-04-16 — User directive: "guarantee no overlap first, then arrange." Built v5 ([exam3_cheatsheet_v5_pervar.tex](exam3_cheatsheet_v5_pervar.tex)): one paracol env per section with a per-section `\columnratio` (0.26–0.38). `\needspace{2.8in}` before each section, `\vspace{8pt}` between. Overlap impossible by construction — no floats, deterministic column flow, env close syncs vertical position.
- 2026-04-16 — User feedback on v5: structure is cleanest paracol version yet, but sync-to-max between sections leaves whitespace gaps; titles like "Laplace Properties + System Analysis" protrude. Shortened all titles to one-word headers, reduced inter-section vspace to 4pt.
- 2026-04-16 — Built v6 ([exam3_cheatsheet_v6_triple.tex](exam3_cheatsheet_v6_triple.tex)): 3-column paracol (tables left, prose middle, tables right). Prose is a single continuous stream; tables become reference sidebars. Zero inter-section prose gaps.
- 2026-04-16 — **User confirmed v6 as best layout so far.** Residual feedback: right-side tables should flush to the page's right edge, and prose should spill into the horizontal space left by skinny right tables ("not straight lines going down the sides"). Built v7 ([exam3_cheatsheet_v7_hybrid.tex](exam3_cheatsheet_v7_hybrid.tex)): 2-column paracol, narrow-left for stacked tables + wide-right for prose with `wrapfigure[r]` tables. Prose physically wraps around right-floated tables; skinny tables yield more prose width. v3 and v6 retained as references per user instruction.
- 2026-04-16 — v7 compile uncovered two bugs: (1) Z Props wrapfigure escaped paracol column due to `{0pt}` natural width + wide Shift-2 row; (2) Feedback section ran off bottom of page. Built v8 ([exam3_cheatsheet_v8_hybrid_fixed.tex](exam3_cheatsheet_v8_hybrid_fixed.tex)) with explicit `\wrapwidth = 2.8in` caps on all wrapfigures, Shift-2 row split across two rows, explicit top/bottom margins of 0.25in, and `\raggedbottom`. v7 kept as reference documenting the bug state.
- 2026-04-16 — v8 compile: user reports v8 is "almost indistinguishable from v7" — same Z Props mislocation, same Laplace Props overlap. Confirmed: wrapfig + paracol is structurally incompatible, not tunable. The width cap shifts the bug but doesn't fix the wrong coordinate frame. Saved memory [feedback_latex_wrapfig_paracol.md](../../../../.claude/projects/-home-devel-electrical-notes/memory/feedback_latex_wrapfig_paracol.md) so future sessions don't re-visit this trap.
- 2026-04-16 — Built v9 ([exam3_cheatsheet_v9_v6_rightaligned.tex](exam3_cheatsheet_v9_v6_rightaligned.tex)): reverted to v6's 3-column paracol (user confirmed best structure). Added `\rtable{}` helper that uses `\hfill` + minipage to right-align each right-column table to the page edge. No wrapfigure. Accepts the trade-off that prose can't flow into skinny-table whitespace — that would require escaping LaTeX to HTML.
- 2026-04-17 — User feedback on v9: "orientation is absolutely perfect." Residual issue: whitespace between right-column tables and middle prose; right column ends before prose does. Built v10 LaTeX (deleted): (a) inter-table `\vspace` 6pt → 2pt, (b) moved Top Traps into right sidebar. Section-heading top-spacing 4pt → 3pt.
- 2026-04-17 — v10-LaTeX compile: user reports "no noticeable difference in v10." Confirmed all paracol cosmetic knobs exhausted; the column-independence is fundamental. User directed pivot to HTML.
- 2026-04-17 — Deleted `exam3_cheatsheet_v10_packed.tex`. Built [exam3_cheatsheet_v10.html](exam3_cheatsheet_v10.html) using `float: left` / `float: right` asides for the side stacks; prose in `<main>` physically wraps around the floats. KaTeX for math, `@page` rules for Letter-landscape print at 0.25in margins. Print via browser PDF or headless Chromium; weasyprint requires pre-rendering math via `katex-cli`.
- 2026-04-17 — User feedback on v10 HTML: (1) tiny prose overlap against the Z Pairs table (left side), (2) no visible print-page boundary in the browser preview, (3) wants ability to scale to other page sizes (e.g., 4x6 index card). Applied three refinements in-place:
  - Left aside right-margin 0.15in → 0.22in (breathing room for prose, fixes Z Pairs overlap).
  - Wrapped content in `<div class="page">` with explicit `var(--page-w) x var(--page-h)` dimensions, dashed border + soft shadow, gray body backdrop — shows exact printable area on screen. `@media print` drops the border, shadow, backdrop.
  - Added `:root` CSS variables `--page-w`, `--page-h`, `--page-margin`. Default was Letter landscape.
  - Bonus: fixed-position preview zoom toggle button (screen-only).
- 2026-04-17 — User feedback round 2 on v10 HTML: only 1 page visible (content overflowed and was clipped), preview didn't look like index card, printing went to full letter not index card. First attempt: added Paged.js polyfill + kept float-based asides + set `@page size: 6in 4in`.
- 2026-04-17 — Research agent returned [html_pagination_tips.md](../html_pagination_tips.md) with the critical finding: **Paged.js skips floats during overflow detection** (pagedjs#153). Our float-based `aside.side-left` / `side-right` layout would clip or halt past page 1. Recommendation: replace floats with CSS Grid, Columns, or Flex.
- 2026-04-17 — Rewrote v10 HTML fundamentally. Architecture now:
  - **Content is a stack of `<section>` blocks.** Each section uses `display: grid` with `grid-template-columns: 1.5in 1fr` — narrow table on left, wide prose on right. Variant class `.right-table` swaps to `grid-template-columns: 1fr 1.5in` with `order: 2` on the table child (puts table on the right instead of left).
  - **Sections alternate** left/right table placement for visual rhythm (1 left, 2 right, 3 left, 4 right, 5 left, 6 right).
  - `break-inside: avoid` on each section keeps it whole across a page boundary when possible.
  - Paged.js now sees all content as block-flow (no floats) → overflow detection works → content that doesn't fit on page 1 flows to page 2 automatically.
  - Added `@bottom-right` page number counter (`counter(page) " / " counter(pages)`) via CSS Paged Media.
  - Preview zoom button bumped to 1.6× (6x4 is tiny on screen without zoom).
- 2026-04-17 — **Trade-off accepted:** lose the "prose physically wraps around narrow side tables" behavior from the float version. Gain: multi-page overflow, consistent per-section layout, page numbers, predictable Paged.js compatibility. User-stated priority was multi-page flow to the second page — prose-wrap was the nice-to-have, now dropped.
- 2026-04-17 — User feedback on per-section alternating grid: "it just alternates table on one side then paragraph, then table on the other side — filling up the HTML page, 3 full pages when printed. If anything it is worse." Pivot: drop per-section grid, switch to **two hand-authored `<div class="page">` wrappers**, each a single 3-column CSS Grid (`1.4in 1fr 1.4in`) matching the v6/v9 look. `.page + .page { break-before: page }` forces the hard break. Content manually split: page 1 = Laplace focus, page 2 = Z / Sampling / Feedback / Traps. Prose heavily abbreviated to fit the 6×4 real estate.
- 2026-04-17 — User confirmed two-page grid is "near perfect." Remaining issue: "when I go to print it takes up the whole page in landscape mode in the printer thing." Diagnosis: this is Chrome's default print behavior — `@page size: 6in 4in` is a HINT, not a forced paper size. Chrome honors it only when output is "Save as PDF" OR when the user manually selects a matching paper size in the print dialog. By default, Chrome uses the system's default paper size (Letter) and scales content to fit. Not a CSS bug. Workaround documented in conversation: Ctrl+P → Destination: Save as PDF → More settings → Paper size: Custom 6×4 → Margins: None → Scale: Default → Save.

## Alternative layouts explored

### v3: `paracol` two-stream layout ([exam3_cheatsheet_v3_paracol.tex](exam3_cheatsheet_v3_paracol.tex)) — reference

- Single `\begin{paracol}{2}` with `\columnratio{0.26}` → ~2.65in left (tables) / ~7.45in right (prose).
- `\switchcolumn` jumps between streams mid-document; `\switchcolumn*` resyncs both streams to the max height before the next pair.
- Handles page breaks properly (unlike minipage-based layouts).
- **Critical limitations that motivated v4:**
  - All tables forced to the same column width (~2.65in). Wider tables get wrapped cells; narrow tables waste column space.
  - Prose paragraphs still separated by `\parskip` → visible vertical gaps inside the prose column. Can't flow one continuous paragraph to match tall tables.
- Retained as a reference layout; **not the current recommendation**.

### v4: `wraptable` natural-width layout ([exam3_cheatsheet_v4_wraptable.tex](exam3_cheatsheet_v4_wraptable.tex)) — fragile, deprecated

- Single-column landscape, 11pt `extarticle`. No `multicol`, no `paracol`.
- Each table placed via `\begin{wraptable}[LINES]{l|r}{0pt}` — `{0pt}` = natural content width; prose wraps around it.
- `\parskip` set to `0pt plus 1pt` so prose paragraphs flow without visible inter-block gaps.
- `\FloatBarrier` (from `placeins`) used between major sections to stop wrapped tables from drifting into the next section.
- **Confirmed rendering bugs (from live compile):**
  - `[LINES]` counts mismatch actual table heights → Laplace Properties table bled past its allocated wrap region and overlapped the next section's title.
  - Heading + wraptable collisions: the "Sampling" section title overlapped with the tail rows of the Laplace Properties table.
  - Traps paragraph squeezed between two tables, ending up overlapping both.
  - Last feedback table placed on the right, overlapping the trailing traps paragraph.
- **Verdict:** wraptable's promise of "natural text flow around tables" does not hold up for 6+ tables. Research was right to call it a trap. Kept the file for reference but NOT recommended.

### v5: per-section `paracol` with variable column ratios ([exam3_cheatsheet_v5_pervar.tex](exam3_cheatsheet_v5_pervar.tex))

- Single-column landscape, 11pt `extarticle`. Each section is its own standalone `paracol` environment.
- `\pairsection{ratio}{title}{table}{prose}` macro opens paracol with `\columnratio{ratio}`, places title spanning both, then table (left) + prose (right), then closes paracol.
- Each section can have its own table width:
  - §1 (Laplace Pairs wider 3-col): ratio 0.38
  - §2 (Laplace Properties narrow 2-col): ratio 0.26
  - §3 (Z Pairs medium 3-col): ratio 0.34
  - §4 (Sampling formulas): ratio 0.32
  - §5 (Feedback formulas): ratio 0.28
  - §6 (CT↔DT + Traps): ratio 0.28
- `\parskip=0pt plus 0.5pt` → continuous prose flow (no inter-block gaps, fixing v3's weakness).
- `\needspace{2.8in}` before each section → if < 2.8in of page remains, force page break. Prevents a section getting orphan-split.
- **No-overlap guarantee (structural, not cosmetic):**
  - No floats (no wraptable/wrapfig → no float drift).
  - paracol emits two independent vertical streams inside its env; closes by resetting vertical position to below max(table height, prose height).
  - `\needspace` ensures enough room remains before opening the env.
  - `\vspace{8pt}` separates adjacent sections.
- Trade-off: §6's Top Traps is back as an `itemize` (safe inside a paracol column, unlike inside a wraptable).
- **Known residual issue (user feedback):** because each `paracol` env closes and syncs heights per section, the shorter column of each pair leaves empty space before the next section. When prose > table in a section, the table column ends high and leaves vertical whitespace. Mitigations applied: shortened section titles, reduced inter-section `\vspace` to 4pt.

### v6: 3-column paracol, tables on both sides, prose in middle ([exam3_cheatsheet_v6_triple.tex](exam3_cheatsheet_v6_triple.tex)) — USER CONFIRMED BEST SO FAR

- Single `\begin{paracol}{3}` environment spanning the whole document.
- `\columnratio{0.21,0.58,0.21}` → ~2.15in left / 6.1in middle / 2.15in right on 10.4in text width.
- Left column: Laplace Pairs, Z Pairs, Sampling formulas (table stack).
- Middle column: continuous prose narrative (Transforms & ROC → PFE → System Analysis → Sampling → Feedback → Traps).
- Right column: Laplace Properties, Z Properties, Feedback formulas, CT vs DT (table stack).
- **Key win:** prose flows as ONE continuous stream with zero inter-section vertical gaps — paragraphs pack perfectly.
- **Key trade-off:** tables lose strict pairing with their prose. Tables become reference sidebars; prose is the narrative. Reading order becomes "middle column top-to-bottom; glance sideways to consult tables."
- Narrow table columns (~2.15in) force compact table notation. Some column headers had to be abbreviated (e.g., "Laplace Pairs" → ROC shown as `$\sigma > 0$`).
- User feedback on v6 (2026-04-16): "best yet." Residual wish: right-side tables should align flush to the RIGHT edge of the page; when a right-side table is narrower than the column, prose should be able to extend into the leftover space. See v7.

### v7: 2-column paracol + wrapfigure-right ([exam3_cheatsheet_v7_hybrid.tex](exam3_cheatsheet_v7_hybrid.tex)) — superseded by v8

- 2-column paracol: ~2.1in narrow left (stacked tables) + ~8.1in wide right (prose).
- In the wide right column, right-floated reference tables via `\begin{wrapfigure}[LINES]{r}{0pt}` — prose physically wraps to the left of each. Narrower tables leave MORE prose width; wider tables leave less.
- Directly implements the user's "not straight lines going down the sides" feedback.

**Compile-time bugs observed (user feedback 2026-04-16):**

1. **Z Props table escaped its paracol right column** — showed up near the middle of the page, adjacent to the left-column Z Pairs table.
   - Root cause: `wrapfigure[r]{0pt}` uses natural content width. The Z Props "Shift-2" row contains the wide formula $z^{-2}X+z^{-1}x[-1]+x[-2]$, pushing the table's natural width past a threshold that triggers a known paracol+wrapfig interaction bug: wrapfigure's `\parshape`-based float placement doesn't fully respect paracol's column bounds, so the float falls back to page-level positioning and escapes the column.
   - Fix in v8: cap wrapfigure widths explicitly (`\wrapwidth = 2.8in`) instead of `{0pt}`; split the Shift-2 row across two table rows so the natural width is bounded even before the cap kicks in.

2. **Content runs off the bottom of the page** — the Feedback section's tail bled below the visible print area.
   - Root cause: geometry was `margin=0.3in` on all four sides, but paracol + wrapfigure combined placement can push content past the bottom margin when floats accumulate. Bottom-overflow is not auto-pagination in this layout because paracol's right column accumulates content without the usual `\flushbottom` behavior.
   - Fix in v8: explicit `top=0.25in, bottom=0.25in, left=0.25in, right=0.25in` in `geometry`, plus `\raggedbottom` so LaTeX doesn't stretch to fill.

### v8: v7 with wrapfigure-width-cap and top/bottom margin fixes ([exam3_cheatsheet_v8_hybrid_fixed.tex](exam3_cheatsheet_v8_hybrid_fixed.tex)) — FAILED, retained as reference

- Same 2-column paracol + wrapfigure-right architecture as v7.
- Applied fixes: explicit `\wrapwidth = 2.8in` width caps, Shift-2 split across rows, 0.25in all-side margins, `\raggedbottom`.
- **Outcome:** user-reported that v8 is "almost indistinguishable from v7" — same Z Props mislocation (slightly shifted right but still stranded near the middle of the page), same Laplace Props text overlap at its bottom edge.
- **Root cause (now confirmed, beyond the v7 hypothesis):** `wrapfig` is fundamentally incompatible with `paracol`. `wrapfig` computes its float placement using page-level `\parshape` math that does not know about paracol's virtual columns. Explicit width caps shift the misplacement by a few inches but don't fix the wrong coordinate frame. `[LINES]`-vs-actual-height mismatch is a secondary symptom of the same root cause: wrapfig can't reconcile its line budget with paracol's column rendering.
- **Structural conclusion:** any hybrid paracol + wrapfigure layout is a dead end. Saved a user-memory entry [feedback_latex_wrapfig_paracol.md](../../../../.claude/projects/-home-devel-electrical-notes/memory/feedback_latex_wrapfig_paracol.md) so future iterations don't re-visit this trap.

### v9: v6 + right-aligned right-column tables ([exam3_cheatsheet_v9_v6_rightaligned.tex](exam3_cheatsheet_v9_v6_rightaligned.tex))

- Returns to v6's 3-column paracol architecture. Drops wrapfigure entirely.
- Each right-column table wrapped in an `\rtable{...}` helper: `\hfill` + minipage with right-aligned `\section*{\hfill Title}` and `\hfill\begin{tabular}`. Tables flush to the page's right edge; narrower tables leave visible whitespace to their LEFT (toward the prose).
- Honest trade-off accepted: prose does NOT reclaim that leftover whitespace. To achieve real prose-around-tables flow in LaTeX + variable widths requires wrapfigure, which doesn't cooperate with paracol. The pragmatic path for that is HTML + weasyprint (see "HTML alternative" section below).
- Inherits v8's 0.25in margins on all sides + `\raggedbottom`.
- **User feedback (2026-04-17):** "orientation is absolutely perfect." Residual issue: whitespace between some right-side tables and middle prose; right column runs out of content before prose does, leaving a dead strip at the bottom of the right column. Described as "not able to be flexible" — correct: paracol columns are independent and cannot bleed into each other's unused space.

### v10 LaTeX attempt (deleted)

v10 was first built as a LaTeX file (`exam3_cheatsheet_v10_packed.tex`) that tightened v9's inter-table `\vspace` and moved Top Traps into the right column as a 5th sidebar. **User compile feedback: "no noticeable difference from v9."** Confirmed that within LaTeX's paracol model, every cosmetic knob has now been tried and the remaining whitespace is fundamental to the layout engine (columns are independent; prose cannot bleed into another column's slack). The LaTeX v10 file was deleted; rebuilt as HTML (see v10 HTML below).

### v10 (HTML): two explicit pages, each a 3-column grid ([exam3_cheatsheet_v10.html](exam3_cheatsheet_v10.html)) — CURRENT RECOMMENDATION

After two earlier architectures failed (float + wrap-around → Paged.js can't multi-page; per-section alternating grid → zig-zag that user disliked), v10 landed on deterministic composition: two hand-authored page divs, each a single 3-column grid matching the v6/v9 look the user liked.

- Page size: **6×4 in landscape index card**, enforced via `@page { size: 6in 4in; margin: 0; }` AND explicit `.page { width: 6in; height: 4in; padding: 0.15in; }`. `@page` doesn't eval CSS vars reliably; both must be in sync.
- **Two `<div class="page">` wrappers.** The second has `break-before: page` via adjacent-sibling selector `.page + .page { break-before: page; }` so it starts on a new printed sheet.
- Each page is itself a CSS Grid: `grid-template-columns: 1.4in 1fr 1.4in` — left tables column, middle prose column, right tables column. Same visual as v6/v9 but per-page so it fits a 6×4 card.
- Content split across the two pages:
  - Page 1 (Laplace focus): L = Laplace Pairs; M = Transforms & ROC intro + PFE + sign trap; R = Laplace Props.
  - Page 2 (Z / Sampling / Feedback): L = Z Pairs + Sampling table; M = System Analysis + Sampling + Feedback + Top Traps prose; R = Z Props + Feedback + CT vs DT.
- **KaTeX** for math, loaded first (`window.load`), then Paged.js injected. Paged.js renders both `<div class="page">`s into `.pagedjs_page` frames with dashed border + drop shadow on screen, stripped for print.
- Page numbers in bottom-right via `@page @bottom-right`.
- Preview zoom button (1.6×) — 6×4 is tiny on screen; zoom makes it readable without affecting print.

**Content volume constraint.** A 6×4 page at 6.5pt has limited real estate. The prose has been heavily abbreviated vs. the LaTeX versions (many sentences trimmed to phrases). If content grows, either (a) shrink font further, (b) add a 3rd `<div class="page">`, or (c) upgrade page size to e.g. letter landscape and accept the non-index-card output.

**How to render a PDF:**

1. **Browser print route (easiest):** open `exam3_cheatsheet_v10.html` in Chrome/Firefox, wait for KaTeX to render math, Ctrl/Cmd-P → Save as PDF, paper = Letter Landscape, margins = Default or None.
2. **Headless (reproducible):** `chromium --headless --no-sandbox --print-to-pdf=v10.pdf --no-pdf-header-footer --virtual-time-budget=5000 file://$(pwd)/exam3_cheatsheet_v10.html`
3. **Weasyprint (no JS):** pre-render math with `katex-cli` or `mathjax-node` to replace the live-rendered math with static HTML, then `weasyprint v10.html v10.pdf`. Without prerender, weasyprint ships no JS, so LaTeX-delimited math stays as literal `$...$` text.

**Known trade-offs:**

- Math tightness is slightly looser than LaTeX's native typography (KaTeX spacing is close but not identical).
- Font fallback chain (`Latin Modern Roman` → Computer Modern → CMU Serif → Georgia) means appearance depends on what the viewing machine has installed. For consistent output, pre-embed a font or use a webfont.
- The prose-around-float behavior is what you asked for, but it means the middle prose width *varies* as you scroll down the page. Readers who expect a constant column width will see column shape changes; that's the cost of the flow.

### When to escape LaTeX

If the "prose reclaims whitespace beside narrow right tables" requirement is a must-have (not just a nice-to-have), stop iterating LaTeX layouts and port to HTML:

- CSS Grid with `grid-template-columns: 2in 1fr 2in` gives the same structure.
- `float: right` on individual right-side tables makes prose actually wrap around them.
- Weasyprint or Chromium-headless produces PDF output.
- Math via KaTeX pre-render; less tight than native LaTeX but acceptable for a cheatsheet.

Estimate: ~4–8 hours to port the content; the layout itself is ~20 lines of CSS.

### HTML / CSS alternative (not implemented, for reference)

Everything above is constrained by LaTeX's page model. CSS Grid / Flexbox expresses the user's desired layout trivially:

```css
.page {
  display: grid;
  grid-template-columns: 2in 1fr 2in;
  grid-template-rows: auto;
  gap: 0.2in;
}
.tables-left, .tables-right { display: flex; flex-direction: column; gap: 0.3in; }
.prose { column-count: 1; hyphens: auto; }
```

PDF output options:

- **`weasyprint`** (Python): CSS → PDF. Good CSS Grid support, handles math via MathJax pre-render.
- **`puppeteer-pdf` / Chromium headless**: full CSS support, render via Chrome's print engine.
- **`prince`**: commercial, highest-fidelity print CSS.

Math quality: KaTeX and MathJax render well but are not as tight as LaTeX's native math. For a cheatsheet with dense formulas this is noticeable but not fatal.

Recommendation: if v5 / v6 both disappoint on layout, consider a week-long pivot to HTML + weasyprint; otherwise stay in LaTeX.

### Rejected: minipage-paired `\sideblock`

- Was prototyped as `exam3_cheatsheet_v2_sidelayout.tex`; **deleted** after research showed:
  - Minipages are unbreakable → a tall `\sideblock` orphans entirely to the next page, leaving a visible gap.
  - Doesn't solve the "tables at natural widths" requirement either (each `\sideblock` still imposes a uniform left-column width).

### Deleted versions

- `exam3_cheatsheet_v2_sidelayout.tex` — minipage approach; superseded by v3/v4.
- `exam3_cheatsheet_fitted.tex` — output from early `cheatsheet_fitter.py` run; conservative heuristic, not useful.
- `exam3_allnotes_landscape.tex` — earlier 9pt 3-column dense dump; now stale, superseded by current cheatsheet.

### A/B comparison (current state)

| Candidate | Variable table widths | Continuous prose flow | No-overlap guarantee | Page-break safety |
| --- | --- | --- | --- | --- |
| [multicol (v1)](exam3_cheatsheet.tex) | ✗ (uniform col) | partial | ✓ | ✓ |
| [paracol (v3)](exam3_cheatsheet_v3_paracol.tex) | ✗ (uniform col, doc-wide) | ✗ | ✓ | ✓ |
| [wraptable (v4)](exam3_cheatsheet_v4_wraptable.tex) | ✓ | ✓ | ✗ (observed overlaps) | ⚠ |
| [per-section paracol (v5)](exam3_cheatsheet_v5_pervar.tex) | ✓ (per section) | ✓ | ✓ (structural) | ✓ (`\needspace`) |
| [3-col tables both sides (v6)](exam3_cheatsheet_v6_triple.tex) | ✗ (uniform per side) | ✓ (one stream) | ✓ | ✓ |
| [2-col + wrapfigure-right (v7)](exam3_cheatsheet_v7_hybrid.tex) | ✓ (per table on right) | ✓ | ✗ (Z Props escapes column) | ⚠ (bottom overflow) |
| [v7 fixed (v8)](exam3_cheatsheet_v8_hybrid_fixed.tex) | ✓ (capped) | ✓ | ✗ (wrapfig still escapes; overlap persists) | ✓ (explicit top/bot) |
| [v6 + right-align (v9)](exam3_cheatsheet_v9_v6_rightaligned.tex) | ✗ (uniform per side, flush right) | ✓ | ✓ (no wrapfigure) | ✓ |
| v10-LaTeX (deleted) | ✗ | ✓ | ✓ | no visible difference vs v9 |
| [v10 HTML (CSS floats)](exam3_cheatsheet_v10.html) | ✓ (per table on each side) | ✓ (around floats) | ✓ | ✓ (CSS @page) |

**Go-forward:** compile v5 on Overleaf. If a section has too much vertical whitespace beside a short table, raise that section's ratio (give the table less column, more to prose). If a table bleeds into the prose column, lower the ratio.
