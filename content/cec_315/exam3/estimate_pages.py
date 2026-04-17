#!/usr/bin/env python3
"""
Rough LaTeX page-count estimator for a landscape-letter, multi-column cheatsheet.

Heuristic only — NOT a substitute for compiling. Expect ±30% accuracy. The
point is to compare "font 14pt vs 16pt vs 20pt" *relative* page counts before
committing to a compile cycle.

Usage:
    python3 estimate_pages.py <file.tex> [--font SIZE] [--cols N] [--margin IN]

Assumptions:
- Landscape letter: 11 x 8.5 in.
- Usable page height = 8.5 - 2*margin (inches).
- Line height at font F pt ≈ 1.15 * F (pt), converted to inches (1 pt = 1/72 in).
- Content items are weighted as N "line-equivalents":
    * prose paragraph: ~len_chars / chars_per_line, ≥ 1
    * itemize/enumerate item: 1 line each (plus wrap estimate for long items)
    * \\[ ... \\] or $$...$$: 1.8 lines (display math has vertical padding)
    * tabular row: 1.15 lines (booktabs spacing)
    * \\section: 2 lines (heading + space above)
    * \\subsection: 1.3 lines
    * center / title block: 1.5 lines
- Column-wrapped math counted at inline ≈ 1 line.

All multi-column columns are summed first, then divided by N columns to get
page count per-column.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

PT_PER_IN = 72.0
PAGE_WIDTH_IN = 11.0
PAGE_HEIGHT_IN = 8.5

# heuristic weights (in "line equivalents") for various content elements
W_PROSE_PER_LINE = 1.0
W_ITEM = 1.1
W_DISPLAY_MATH = 1.8
W_TABLE_ROW = 1.15
W_SECTION = 2.0
W_SUBSECTION = 1.3
W_CENTER_BLOCK = 1.5
W_NEWPAGE = 9999  # force a page break

# char-per-line multiplier: at 10pt in a 5-inch column, ~60 chars fit per line.
# At F pt in a C-inch column, chars ≈ 60 * (10/F) * (C/5)
def chars_per_line(font_pt: float, col_width_in: float) -> float:
    return 60.0 * (10.0 / font_pt) * (col_width_in / 5.0)


def line_height_in(font_pt: float) -> float:
    return (1.15 * font_pt) / PT_PER_IN


def parse_tex(text: str, chars_per_ln: float) -> float:
    """Return total line-equivalents for the document body."""
    # strip preamble (everything before \begin{document})
    m = re.search(r"\\begin\{document\}", text)
    if m:
        text = text[m.end():]
    m = re.search(r"\\end\{document\}", text)
    if m:
        text = text[:m.start()]

    # strip comments (% to end of line, unless escaped \%)
    text = re.sub(r"(?<!\\)%.*", "", text)

    total = 0.0

    # 1) \section*/\section headings
    n_sec = len(re.findall(r"\\section\*?\{", text))
    total += n_sec * W_SECTION

    # 2) \subsection
    n_sub = len(re.findall(r"\\subsection\*?\{", text))
    total += n_sub * W_SUBSECTION

    # 3) displayed math: \[...\], $$...$$, \begin{equation}, align, gather
    display_blocks = re.findall(r"\\\[.*?\\\]", text, flags=re.DOTALL)
    display_blocks += re.findall(r"\$\$.*?\$\$", text, flags=re.DOTALL)
    for env in ("equation", "align", "align\\*", "gather", "gather\\*"):
        display_blocks += re.findall(
            r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}",
            text, flags=re.DOTALL)
    total += len(display_blocks) * W_DISPLAY_MATH

    # remove display math from prose pass so we don't double-count
    text = re.sub(r"\\\[.*?\\\]", "", text, flags=re.DOTALL)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)

    # 4) tabular environments: count rows (\\ separators)
    for tab in re.findall(r"\\begin\{tabular\}(.*?)\\end\{tabular\}",
                          text, flags=re.DOTALL):
        # count \\ line breaks, +1 for header
        rows = tab.count("\\\\")
        total += (rows + 1) * W_TABLE_ROW
    # remove tabular blocks from further prose accounting
    text = re.sub(r"\\begin\{tabular\}.*?\\end\{tabular\}", "",
                  text, flags=re.DOTALL)

    # 5) itemize/enumerate items
    n_item = len(re.findall(r"\\item\b", text))
    total += n_item * W_ITEM
    # remove \item lines approximately
    text = re.sub(r"\\item\b", "", text)

    # 6) center/title blocks
    n_ctr = len(re.findall(r"\\begin\{center\}", text))
    total += n_ctr * W_CENTER_BLOCK

    # 7) page break / column break
    n_pbreak = len(re.findall(r"\\newpage\b|\\pagebreak\b", text))
    total += n_pbreak * W_NEWPAGE
    n_cbreak = len(re.findall(r"\\columnbreak\b", text))

    # 8) prose: what's left, minus LaTeX commands
    #    Strip remaining \commands{...} for a char-count estimate
    prose = re.sub(r"\\[a-zA-Z]+\*?(\{[^{}]*\})?", " ", text)
    prose = re.sub(r"[{}]", " ", prose)
    prose = re.sub(r"\\\\", "\n", prose)  # line breaks
    # rough prose line count: lines + wrap
    prose_lines = 0
    for line in prose.split("\n"):
        s = line.strip()
        if not s:
            continue
        # count wraps
        prose_lines += max(1, len(s) / chars_per_ln)
    total += prose_lines * W_PROSE_PER_LINE

    return total


def estimate(path: Path, font_pt: float, cols: int, margin_in: float) -> dict:
    text = path.read_text(encoding="utf-8")

    # column width (rough): (page_w - 2*margin - (cols-1)*colsep) / cols
    # colsep is typically ~0.25in
    colsep = 0.25
    col_w = (PAGE_WIDTH_IN - 2 * margin_in - (cols - 1) * colsep) / cols
    cpl = chars_per_line(font_pt, col_w)

    line_eq = parse_tex(text, cpl)
    usable_h = PAGE_HEIGHT_IN - 2 * margin_in
    lines_per_col_page = usable_h / line_height_in(font_pt)
    lines_per_page = lines_per_col_page * cols

    pages = line_eq / lines_per_page
    return {
        "font_pt": font_pt,
        "cols": cols,
        "margin_in": margin_in,
        "col_width_in": round(col_w, 2),
        "chars_per_line": round(cpl, 1),
        "line_height_in": round(line_height_in(font_pt), 3),
        "lines_per_page": round(lines_per_page, 1),
        "line_equivalents": round(line_eq, 1),
        "pages_estimate": round(pages, 2),
        "pages_rounded_up": int(pages) + (0 if pages == int(pages) else 1),
    }


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Rough LaTeX cheatsheet page estimator")
    p.add_argument("file", type=Path, help="Path to .tex file")
    p.add_argument("--font", type=float, default=None, help="Font size pt (override)")
    p.add_argument("--cols", type=int, default=2, help="Number of columns (default 2)")
    p.add_argument("--margin", type=float, default=0.25, help="Margin in inches (default 0.25)")
    p.add_argument("--sweep", action="store_true",
                   help="Sweep font sizes 10-20pt for comparison")
    args = p.parse_args(argv)

    if not args.file.is_file():
        print(f"File not found: {args.file}", file=sys.stderr)
        return 1

    if args.sweep:
        print(f"{'font':>5} {'cols':>5} {'col_w':>6} {'cpl':>6} "
              f"{'lines/pg':>9} {'units':>7} {'pages':>7}")
        for font in (10, 11, 12, 14, 16, 18, 20):
            for cols in (2, 3):
                r = estimate(args.file, float(font), cols, args.margin)
                print(f"{r['font_pt']:>5.0f} {r['cols']:>5} "
                      f"{r['col_width_in']:>6.2f} {r['chars_per_line']:>6.1f} "
                      f"{r['lines_per_page']:>9.1f} {r['line_equivalents']:>7.1f} "
                      f"{r['pages_estimate']:>7.2f}")
    else:
        font = args.font or 10.0
        r = estimate(args.file, font, args.cols, args.margin)
        for k, v in r.items():
            print(f"{k:>20}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
