#!/usr/bin/env python3
"""
cheatsheet_fitter.py

Fit a LaTeX cheatsheet onto a user-specified page budget (default 2 landscape
letter pages, 2 columns).  The tool parses the body of the tex file into a
list of "chunks" (section + following content), estimates each chunk's
rendered height at various base font sizes, then uses greedy
first-fit-decreasing bin packing to drop those chunks into page/column slots.
The largest base font size that fits within the budget is chosen, and a new
.tex file is emitted with explicit \\columnbreak / \\newpage markers and
per-chunk adjustbox scaling / rotation where required.

Heuristic only.  Expect a few percent error versus the real pdflatex render.
The goal is ordering + a good starting point, not a pixel-accurate layout.

Design notes:
- Stdlib only (argparse, dataclasses, pathlib, re, sys).
- Python 3.10+ syntax.
- Page size assumed landscape-letter 11 x 8.5 in by default.
- Defensive parsing: unknown blocks become "rawblob" chunks and are placed
  whole without attempting to resize them.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants and heuristic weights
# ---------------------------------------------------------------------------

PT_PER_IN = 72.0

# Default page geometry (landscape letter, tight margins)
DEFAULT_PAGE_WIDTH_IN = 11.0
DEFAULT_PAGE_HEIGHT_IN = 8.5
DEFAULT_MARGIN_IN = 0.25
DEFAULT_COLSEP_IN = 0.3

# Line-equivalents for various content events
W_SECTION = 2.0           # \section* heading: title line + spacing above
W_SUBSECTION = 1.3
W_DISPLAY_MATH = 1.8      # each \[...\] or display env
W_TABLE_ROW = 1.15        # each tabular row
W_ITEM = 1.1              # each \item
W_PROSE_LINE = 1.0
W_CENTER_BLOCK = 1.5
W_MINIPAGE_OVERHEAD = 0.5
W_BLANK_BETWEEN_CHUNKS = 0.5

# Approximate char-per-line: at 10pt in a 5-inch column, ~60 chars fit.
# Scale linearly in inverse font size and directly in column width.
BASE_CHARS_PER_LINE = 60.0
BASE_FONT_PT = 10.0
BASE_COL_WIDTH_IN = 5.0


# ---------------------------------------------------------------------------
# Utility: line height, chars per line
# ---------------------------------------------------------------------------

def line_height_in(font_pt: float) -> float:
    """Baseline skip at a given font size.  1.15 * font, converted pt -> in."""
    return (1.15 * font_pt) / PT_PER_IN


def chars_per_line(font_pt: float, col_width_in: float) -> float:
    return BASE_CHARS_PER_LINE * (BASE_FONT_PT / font_pt) * (col_width_in / BASE_COL_WIDTH_IN)


def col_width(page_width_in: float, margin_in: float, cols: int,
              colsep_in: float = DEFAULT_COLSEP_IN) -> float:
    return (page_width_in - 2 * margin_in - (cols - 1) * colsep_in) / cols


# ---------------------------------------------------------------------------
# Chunk dataclass
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    """One structural unit of the cheatsheet body."""
    title: str                          # e.g. 'Laplace Pairs' or '<prose>'
    body: str                           # raw latex text including section line
    kind: str = "mixed"                 # 'section', 'prose', 'rawblob', 'preamble_body'
    # Dimension hints (filled in during measurement)
    line_equiv: float = 0.0             # line-equivalents at base font
    width_in: float = 0.0               # widest content within
    max_row_chars: int = 0              # longest plain-text row for width estimate
    has_oversized_table: bool = False   # flagged when declared width > col width
    oversized_kind: str = ""            # 'table-wide', 'equation-wide', 'verbatim'
    hard_break_after: bool = False      # chunk ends with \newpage in source
    source_index: int = 0               # original order

    # Packing result (filled during pack step)
    scale: float = 1.0                  # adjustbox scale factor applied
    rotate: bool = False                # rotated 90
    split_of: int | None = None         # parent index if split
    placed_slot: tuple[int, int] | None = None   # (page, column)

    def height_at(self, font_pt: float) -> float:
        """Return estimated rendered height in inches at the given font size."""
        # linear scaling from base font to target; line_equiv already includes
        # per-chunk vertical spacing.
        return self.line_equiv * line_height_in(font_pt)

    def width_required_in(self, font_pt: float) -> float:
        """Return approximate natural width needed in inches at font size."""
        # Use max_row_chars and BASE_CHARS_PER_LINE / font_pt relationship.
        if self.max_row_chars <= 0:
            return 0.0
        # chars * (pt per char) -> inches.  ~0.5 char-widths per pt at default
        # font (rough serif average).  Scale with font.
        avg_char_in = (font_pt / PT_PER_IN) * 0.5
        return self.max_row_chars * avg_char_in


# ---------------------------------------------------------------------------
# Parsing: split preamble + body + document tail
# ---------------------------------------------------------------------------

@dataclass
class Parsed:
    preamble: str
    body_prefix: str        # everything from \begin{document} up to first section
    chunks: list[Chunk]
    body_suffix: str        # trailing \end{multicols*}\n\end{document} etc.


def split_preamble_and_body(text: str) -> tuple[str, str, str]:
    """Split into (preamble, body, tail).  body is between \\begin{document}
    and \\end{document} (inclusive of \\begin{multicols*} wrappers — those we
    will regenerate, so we surface them as part of the tail/prefix).
    """
    m_begin = re.search(r"\\begin\{document\}", text)
    m_end = re.search(r"\\end\{document\}", text)
    if not m_begin or not m_end:
        raise ValueError(
            "Input tex file is missing \\begin{document} or \\end{document}")
    preamble = text[:m_begin.end()]
    body = text[m_begin.end():m_end.start()]
    tail = text[m_end.start():]
    return preamble, body, tail


_SECTION_RE = re.compile(r"^\s*\\section\*?\{[^}]*\}", re.MULTILINE)


def split_body_into_chunks(body: str) -> tuple[str, list[str], str]:
    """Split the document body into (prefix, [section_block_strings], suffix).

    The prefix captures content BEFORE the first \\section (e.g. a \\begin
    {multicols*} line).  The suffix captures content AFTER the last chunk's
    natural end (e.g. \\end{multicols*}).  Each section block is the text
    from one \\section line up to (but not including) the next one.
    """
    # Find all section positions
    matches = list(_SECTION_RE.finditer(body))
    if not matches:
        return body, [], ""

    prefix = body[:matches[0].start()]
    chunks = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        # Trim trailing \end{multicols*} (etc.) from final chunk; keep it in suffix.
        chunks.append(body[start:end])

    suffix = ""
    # If last chunk contains \end{multicols*} (or similar body-closer), split it off.
    last = chunks[-1]
    m_close = re.search(r"\n\s*\\end\{multicols\*?\}\s*$", last)
    if m_close:
        chunks[-1] = last[:m_close.start()].rstrip() + "\n"
        suffix = last[m_close.start():]
    return prefix, chunks, suffix


# ---------------------------------------------------------------------------
# Chunk measurement
# ---------------------------------------------------------------------------

_ENV_DISPLAY = ("equation", r"equation\*", "align", r"align\*",
                "gather", r"gather\*", "multline", r"multline\*")


def _strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def _count_display_math(text: str) -> int:
    count = 0
    count += len(re.findall(r"\\\[.*?\\\]", text, flags=re.DOTALL))
    count += len(re.findall(r"\$\$.*?\$\$", text, flags=re.DOTALL))
    for env in _ENV_DISPLAY:
        count += len(re.findall(
            r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}",
            text, flags=re.DOTALL))
    return count


def _strip_display_math(text: str) -> str:
    text = re.sub(r"\\\[.*?\\\]", "", text, flags=re.DOTALL)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    for env in _ENV_DISPLAY:
        text = re.sub(
            r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}", "",
            text, flags=re.DOTALL)
    return text


_TAB_RE = re.compile(
    r"\\begin\{(tabular|tabularx|tabularray|longtable)\}"
    r"(\*?\{[^}]*\})?"      # optional * and width/spec
    r"\{([^}]*)\}"          # required column spec
    r"(.*?)\\end\{\1\}",
    flags=re.DOTALL,
)


def _extract_tables(text: str) -> tuple[list[dict], str]:
    """Pull tabular environments out.  Return (tables, text-with-tables-gone).

    Each dict: {rows, cols, spec, declared_width_in, max_row_chars}
    """
    tables = []

    def _on_match(m: re.Match) -> str:
        spec = m.group(3)
        body = m.group(4)
        rows = body.count("\\\\") + 1
        cols = _count_spec_cols(spec)
        declared_w = _declared_width_from_spec(spec)
        max_row = _longest_table_row_chars(body)
        tables.append({
            "rows": rows,
            "cols": cols,
            "spec": spec,
            "declared_width_in": declared_w,
            "max_row_chars": max_row,
        })
        return "\n<TABULAR_SENTINEL>\n"

    new_text = _TAB_RE.sub(_on_match, text)
    return tables, new_text


def _count_spec_cols(spec: str) -> int:
    s = re.sub(r"@\{[^}]*\}", "", spec)      # drop @{...}
    s = re.sub(r"\*\{\d+\}\{[^}]*\}", "c", s)  # collapse *{n}{...}
    s = re.sub(r"[|>]\s*", "", s)
    s = re.sub(r"p\{[^}]*\}", "p", s)
    s = re.sub(r"m\{[^}]*\}", "m", s)
    s = re.sub(r"b\{[^}]*\}", "b", s)
    return sum(1 for ch in s if ch in "lcrpmbXsS")


def _declared_width_from_spec(spec: str) -> float:
    """Sum explicit p{X.Yin} column widths.  Returns 0 if none declared."""
    total = 0.0
    for m in re.finditer(r"[pmb]\{([\d.]+)(in|cm|mm|pt)\}", spec):
        val = float(m.group(1))
        unit = m.group(2)
        if unit == "in":
            total += val
        elif unit == "cm":
            total += val / 2.54
        elif unit == "mm":
            total += val / 25.4
        elif unit == "pt":
            total += val / PT_PER_IN
    return total


def _longest_table_row_chars(body: str) -> int:
    """Longest row when latex commands are stripped.  Rough width gauge."""
    longest = 0
    for row in body.split("\\\\"):
        plain = re.sub(r"\\[a-zA-Z]+\*?(\{[^{}]*\})?", "", row)
        plain = re.sub(r"[{}]", "", plain)
        plain = re.sub(r"\s+", " ", plain).strip()
        longest = max(longest, len(plain))
    return longest


def _count_items(text: str) -> int:
    return len(re.findall(r"\\item\b", text))


def _count_sections(text: str) -> int:
    return len(re.findall(r"\\section\*?\{", text))


def _count_subsections(text: str) -> int:
    return len(re.findall(r"\\subsection\*?\{", text))


def _estimate_prose_lines(text: str, cpl: float) -> float:
    # remove \items, command invocations, braces
    t = re.sub(r"\\item\b", "", text)
    t = re.sub(r"\\[a-zA-Z]+\*?(\{[^{}]*\})?", " ", t)
    t = re.sub(r"[{}]", " ", t)
    t = t.replace("\\\\", "\n")
    prose_lines = 0.0
    for line in t.split("\n"):
        s = line.strip()
        if not s:
            continue
        prose_lines += max(1.0, len(s) / cpl)
    return prose_lines


def _chunk_has_twoup(text: str) -> bool:
    return r"\twoup" in text or r"\begin{minipage}" in text


def measure_chunk(chunk: Chunk, font_pt: float, col_width_in: float) -> None:
    """Populate chunk.line_equiv, chunk.width_in and related flags for a given
    measurement font size.  Width is reported at this font size; line_equiv
    is logically font-agnostic (we convert to height with height_at later).
    """
    text = _strip_comments(chunk.body)

    cpl = chars_per_line(font_pt, col_width_in)
    line_equiv = 0.0

    # Sections / subsections
    line_equiv += _count_sections(text) * W_SECTION
    line_equiv += _count_subsections(text) * W_SUBSECTION

    # Display math
    line_equiv += _count_display_math(text) * W_DISPLAY_MATH
    text_no_dm = _strip_display_math(text)

    # Tables
    tables, text_no_tab = _extract_tables(text_no_dm)
    oversized = False
    oversized_kind = ""
    declared_max = 0.0
    max_row_chars = 0
    for t in tables:
        rows = t["rows"]
        line_equiv += rows * W_TABLE_ROW
        if t["declared_width_in"] > 0:
            # Column spec requests a fixed physical width.  Compare with slot.
            declared_max = max(declared_max, t["declared_width_in"])
            if t["declared_width_in"] > col_width_in + 0.02:
                oversized = True
                oversized_kind = "table-wide"
        # Track max row width from plain content
        avg_char_in = (font_pt / PT_PER_IN) * 0.5
        row_in = t["max_row_chars"] * avg_char_in
        if row_in > col_width_in + 0.05 and not oversized:
            oversized = True
            oversized_kind = "table-wide"
        max_row_chars = max(max_row_chars, t["max_row_chars"])

    # Items (after sentinel swap)
    line_equiv += _count_items(text_no_tab) * W_ITEM

    # Center blocks
    line_equiv += len(re.findall(r"\\begin\{center\}", text_no_tab)) * W_CENTER_BLOCK

    # Minipage / twoup overhead
    n_mp = len(re.findall(r"\\begin\{minipage\}", text_no_tab))
    n_tw = len(re.findall(r"\\twoup\b", text_no_tab))
    line_equiv += (n_mp + n_tw) * W_MINIPAGE_OVERHEAD

    # Remaining prose (after stripping sentinels and item markers)
    prose = text_no_tab
    prose = prose.replace("<TABULAR_SENTINEL>", "")
    prose_lines = _estimate_prose_lines(prose, cpl)
    line_equiv += prose_lines * W_PROSE_LINE

    # Overhead between chunks
    line_equiv += W_BLANK_BETWEEN_CHUNKS

    # Width: max of declared_max and estimated widest prose run
    est_width = declared_max
    if max_row_chars > 0:
        avg_char_in = (font_pt / PT_PER_IN) * 0.5
        est_width = max(est_width, max_row_chars * avg_char_in)

    chunk.line_equiv = line_equiv
    chunk.width_in = est_width
    chunk.max_row_chars = max_row_chars
    chunk.has_oversized_table = oversized
    chunk.oversized_kind = oversized_kind


# ---------------------------------------------------------------------------
# Parsing entry point
# ---------------------------------------------------------------------------

def parse_tex(text: str) -> Parsed:
    preamble, body, tail = split_preamble_and_body(text)
    prefix, raw_chunks, suffix = split_body_into_chunks(body)

    chunks: list[Chunk] = []
    for i, raw in enumerate(raw_chunks):
        m = re.match(r"\s*\\section\*?\{([^}]*)\}", raw)
        title = m.group(1) if m else f"chunk{i}"
        # Mark chunks with an explicit pagebreak inside as hard-break
        hard_break = bool(re.search(r"\\newpage\b|\\pagebreak\b", raw))
        kind = "section"
        # If a chunk's body (after heading) contains nothing but \end tokens or
        # weird stuff we don't recognize, still treat as section; only truly
        # unparseable blobs (no section, no plain structure) are rawblob.
        c = Chunk(title=title, body=raw, kind=kind,
                  hard_break_after=hard_break, source_index=i)
        chunks.append(c)

    return Parsed(preamble=preamble, body_prefix=prefix,
                  chunks=chunks, body_suffix=suffix + tail)


# ---------------------------------------------------------------------------
# Packing
# ---------------------------------------------------------------------------

@dataclass
class Slot:
    page: int
    col: int
    capacity_in: float
    used_in: float = 0.0
    chunks: list[Chunk] = field(default_factory=list)

    @property
    def remaining(self) -> float:
        return self.capacity_in - self.used_in


@dataclass
class PackResult:
    font_pt: float
    slots: list[Slot]
    ok: bool
    unfit: list[Chunk]
    notes: list[str]


def _make_slots(pages: int, cols: int, capacity_in: float) -> list[Slot]:
    return [Slot(page=p, col=c, capacity_in=capacity_in)
            for p in range(pages) for c in range(cols)]


def _try_shrink_chunk(c: Chunk, font_pt: float, col_width_in: float,
                     col_height_in: float) -> bool:
    """If chunk is oversized in width, try to mark adjustbox scale factor.
    Returns True if we found a usable scale, False otherwise.
    """
    if c.width_in <= col_width_in + 0.02 and not c.has_oversized_table:
        return True
    if c.width_in <= 0:
        return True
    factor = min(1.0, (col_width_in - 0.05) / max(c.width_in, 0.01))
    # Don't shrink below 0.65; legibility gets bad.
    if factor < 0.65:
        return False
    c.scale = factor
    # Scaling also reduces height by roughly the same factor
    return True


def _try_rotate_chunk(c: Chunk, font_pt: float, col_width_in: float,
                     col_height_in: float) -> bool:
    """Swap width and height and see if rotated chunk fits."""
    h = c.height_at(font_pt)
    # After 90 rotation the chunk's width becomes h and height becomes width_in
    if h < col_width_in and c.width_in < col_height_in:
        c.rotate = True
        return True
    return False


def pack(parsed: Parsed, pages: int, cols: int,
         page_width_in: float, page_height_in: float,
         margin_in: float, font_pt: float) -> PackResult:
    """Greedy first-fit-decreasing pack, returning a PackResult."""
    colw = col_width(page_width_in, margin_in, cols)
    colh = page_height_in - 2 * margin_in

    # Measure every chunk at this font size
    for c in parsed.chunks:
        measure_chunk(c, font_pt, colw)
        # Reset packing state
        c.scale = 1.0
        c.rotate = False
        c.placed_slot = None

    slots = _make_slots(pages, cols, colh)
    unfit: list[Chunk] = []
    notes: list[str] = []

    # Sort by estimated height descending (stable on source index for ties)
    sort_order = sorted(parsed.chunks,
                        key=lambda c: (-c.height_at(font_pt), c.source_index))

    for c in sort_order:
        need_h = c.height_at(font_pt)

        # If chunk is too wide, attempt scale; scale reduces height as well.
        if c.has_oversized_table or c.width_in > colw + 0.02:
            scaled = _try_shrink_chunk(c, font_pt, colw, colh)
            if not scaled:
                # Try rotation as fallback
                if _try_rotate_chunk(c, font_pt, colw, colh):
                    notes.append(f"rotated: {c.title}")
                else:
                    notes.append(
                        f"oversized, could not shrink/rotate: {c.title}")
                    unfit.append(c)
                    continue
            else:
                if c.scale < 1.0:
                    notes.append(
                        f"scaled x{c.scale:.2f}: {c.title}")
            need_h = c.height_at(font_pt) * c.scale  # scaled chunk shorter too

        # If chunk by itself is taller than a full column, no single slot fits.
        if need_h > colh + 0.001:
            # Try scaling down by height if we have width headroom
            if c.scale == 1.0 and need_h / colh < 1.4:
                fh = colh / need_h
                if fh >= 0.7:
                    c.scale = fh
                    need_h = need_h * fh
                    notes.append(
                        f"height-scaled x{c.scale:.2f}: {c.title}")
                else:
                    notes.append(f"too tall for any single column: {c.title}")
                    unfit.append(c)
                    continue
            else:
                notes.append(f"too tall for any single column: {c.title}")
                unfit.append(c)
                continue

        # Pick the slot with the most remaining room that can fit this chunk.
        candidates = [s for s in slots if s.remaining + 0.001 >= need_h]
        if not candidates:
            unfit.append(c)
            continue
        # First-fit-decreasing: greedy chooses the slot with LEAST remaining
        # room that still fits (to pack tight).  When no slot can hold it, use
        # least remaining as secondary.
        best = min(candidates, key=lambda s: s.remaining)
        best.used_in += need_h
        best.chunks.append(c)
        c.placed_slot = (best.page, best.col)

    ok = not unfit
    return PackResult(font_pt=font_pt, slots=slots, ok=ok,
                      unfit=unfit, notes=notes)


# ---------------------------------------------------------------------------
# Font-size search
# ---------------------------------------------------------------------------

def find_best_font(parsed: Parsed, pages: int, cols: int,
                   page_width_in: float, page_height_in: float,
                   margin_in: float,
                   max_font: float, min_font: float) -> PackResult:
    """Search font sizes from max downward in 1pt decrements; return the first
    (largest) one that packs all chunks.  If none works, return the result at
    min_font so the caller can see what didn't fit.
    """
    font = max_font
    last_result: PackResult | None = None
    while font >= min_font - 0.001:
        result = pack(parsed, pages, cols,
                      page_width_in, page_height_in, margin_in, font)
        last_result = result
        if result.ok:
            return result
        font -= 1.0
    assert last_result is not None
    return last_result


# ---------------------------------------------------------------------------
# Rendering output tex
# ---------------------------------------------------------------------------

def _ensure_adjustbox_in_preamble(preamble: str) -> str:
    if r"\usepackage{adjustbox}" in preamble or r"\usepackage[" in preamble and "adjustbox" in preamble:
        return preamble
    # Insert just before \begin{document}
    return preamble.replace(
        r"\begin{document}",
        "\\usepackage{adjustbox}\n\\begin{document}",
        1,
    )


def _wrap_chunk(c: Chunk) -> str:
    body = c.body.rstrip() + "\n"
    if c.rotate:
        body = ("\\begin{adjustbox}{angle=90}\n" + body.rstrip() +
                "\n\\end{adjustbox}\n")
    elif c.scale < 0.999:
        body = (f"\\begin{{adjustbox}}{{max width=\\columnwidth,"
                f"scale={c.scale:.3f}}}\n"
                + body.rstrip() + "\n\\end{adjustbox}\n")
    return body


def render(parsed: Parsed, result: PackResult, pages: int, cols: int,
           original_preamble: str) -> str:
    """Produce a new tex string with chunks arranged per the packing.

    We preserve the original preamble verbatim (plus adjustbox if any chunk
    needed it), then emit \\begin{multicols*}{cols} followed by chunk bodies
    separated by \\columnbreak / \\newpage in the order dictated by pack.
    """
    needs_adjustbox = any(
        (c.scale < 0.999 or c.rotate) for c in parsed.chunks)
    preamble = original_preamble
    if needs_adjustbox:
        preamble = _ensure_adjustbox_in_preamble(preamble)

    # Build the body.  We honor the slot order: all chunks in (page, col)
    # order, separated by \columnbreak at column boundaries and \newpage at
    # page boundaries.  Inside a slot, chunks are in source order (we sort
    # them back to source_index for reading flow).
    lines: list[str] = []
    lines.append("\\begin{multicols*}{%d}" % cols)
    # Suppress column-balancing quirks by adding \raggedcolumns
    lines.append("\\raggedcolumns")

    # Re-arrange slot contents in source order for readability
    for s in result.slots:
        s.chunks.sort(key=lambda c: c.source_index)

    for s_idx, s in enumerate(result.slots):
        if s_idx > 0:
            if s.col == 0:
                lines.append("\\newpage")
            else:
                lines.append("\\columnbreak")
        if not s.chunks:
            # Emit an empty placeholder so the column break still flushes
            lines.append("% (empty slot)")
            lines.append("\\mbox{}")
            continue
        for c in s.chunks:
            lines.append(_wrap_chunk(c).rstrip())
            lines.append("")  # blank line between chunks

    lines.append("\\end{multicols*}")
    body_str = "\n".join(lines) + "\n"

    # Stitch preamble + body + \end{document}
    # preamble already includes \begin{document}
    return preamble + "\n" + body_str + "\\end{document}\n"


# ---------------------------------------------------------------------------
# CLI reporting
# ---------------------------------------------------------------------------

def summarize(parsed: Parsed, result: PackResult, pages: int, cols: int,
              colw: float, colh: float) -> str:
    lines: list[str] = []
    lines.append(f"Parsed {len(parsed.chunks)} chunk(s) from input.")
    lines.append(f"Page grid: {pages} page(s) x {cols} column(s) "
                 f"= {pages*cols} slot(s).")
    lines.append(f"Column size: {colw:.2f} in wide x {colh:.2f} in tall.")
    lines.append(f"Chosen font: {result.font_pt:.0f} pt "
                 f"(fit={'OK' if result.ok else 'FAILED'}).")
    lines.append("")
    lines.append("Chunk dimensions at chosen font:")
    lines.append(f"  {'idx':>3} {'h(in)':>7} {'w(in)':>6} "
                 f"{'scale':>5} {'rot':>4} {'slot':>6}  title")
    for c in parsed.chunks:
        h = c.height_at(result.font_pt) * c.scale
        slot_str = (f"p{c.placed_slot[0]}c{c.placed_slot[1]}"
                    if c.placed_slot is not None else "----")
        rot = "yes" if c.rotate else ""
        lines.append(
            f"  {c.source_index:>3} {h:>7.2f} {c.width_in:>6.2f} "
            f"{c.scale:>5.2f} {rot:>4} {slot_str:>6}  {c.title}")
    lines.append("")
    lines.append("Slot usage:")
    for s in result.slots:
        fill = s.used_in / s.capacity_in if s.capacity_in > 0 else 0
        lines.append(
            f"  page {s.page} col {s.col}: "
            f"{s.used_in:.2f}/{s.capacity_in:.2f} in "
            f"({fill*100:.0f}% full), {len(s.chunks)} chunk(s)")
    if result.unfit:
        lines.append("")
        lines.append("UNPLACED CHUNKS:")
        for c in result.unfit:
            lines.append(f"  - {c.title} (h={c.height_at(result.font_pt):.2f} in, "
                         f"w={c.width_in:.2f} in, "
                         f"oversized={c.has_oversized_table})")
    if result.notes:
        lines.append("")
        lines.append("Notes:")
        for n in result.notes:
            lines.append(f"  - {n}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="Fit a LaTeX cheatsheet onto a fixed page budget.")
    ap.add_argument("input", type=Path, help="Input .tex file")
    ap.add_argument("--pages", type=int, default=2, help="Page budget")
    ap.add_argument("--cols", type=int, default=2, help="Columns per page")
    ap.add_argument("--max-font", type=float, default=14.0,
                    help="Max base font size to try (pt)")
    ap.add_argument("--min-font", type=float, default=8.0,
                    help="Min base font size to try (pt)")
    ap.add_argument("--output", type=Path, default=None,
                    help="Output .tex file (default: <input>_fitted.tex)")
    ap.add_argument("--page-width", type=float, default=DEFAULT_PAGE_WIDTH_IN,
                    help="Page width in inches (default 11, landscape letter)")
    ap.add_argument("--page-height", type=float, default=DEFAULT_PAGE_HEIGHT_IN,
                    help="Page height in inches (default 8.5, landscape letter)")
    ap.add_argument("--margin", type=float, default=DEFAULT_MARGIN_IN,
                    help="Margin in inches (default 0.25)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Do not write output, just report the plan")
    args = ap.parse_args(argv)

    if not args.input.is_file():
        print(f"input not found: {args.input}", file=sys.stderr)
        return 1

    text = args.input.read_text(encoding="utf-8")
    try:
        parsed = parse_tex(text)
    except ValueError as e:
        print(f"parse error: {e}", file=sys.stderr)
        return 2

    result = find_best_font(parsed, args.pages, args.cols,
                            args.page_width, args.page_height,
                            args.margin, args.max_font, args.min_font)

    colw = col_width(args.page_width, args.margin, args.cols)
    colh = args.page_height - 2 * args.margin
    print(summarize(parsed, result, args.pages, args.cols, colw, colh))

    if args.dry_run:
        return 0 if result.ok else 3

    out_path = args.output or args.input.with_name(
        args.input.stem + "_fitted.tex")
    out_text = render(parsed, result, args.pages, args.cols, parsed.preamble)
    out_path.write_text(out_text, encoding="utf-8")
    print(f"\nwrote: {out_path}")
    return 0 if result.ok else 3


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
