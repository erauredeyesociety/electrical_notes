"""Render ONE intermediate into every output format.

The intermediate is `textlayer.DocText` -- one record per page, carrying the
text, the density verdict, the faithfulness signals and the image/drawing
counts. Markdown, plain text, LaTeX and JSONL are *views* of that record, never
independent extractors. Writing one extractor per format, or extracting to one
format and converting, is how three per-course scripts came to disagree about
what a usable text layer is; this module exists so that cannot happen again.

`to_markdown` and `to_text` moved here from `textlayer.py` UNCHANGED. They are
the reference behaviour -- their output bytes are a must-not-break invariant
(docs/roadmap.md M2) and were verified byte-identical across all 448 corpus
documents before and after the move. `textlayer` re-exports both, so every
existing caller is untouched.

Design: docs/plans/text-layer-first.md sections 4 and 5.
"""

from __future__ import annotations

import json
import re
from typing import TYPE_CHECKING

from . import structure

if TYPE_CHECKING:                      # avoids a textlayer <-> emit import cycle
    from .textlayer import DocText


# --------------------------------------------------------------------------
# Markdown -- the reference view. A consumer who never opens the JSONL reads
# this, so the header block is the project's honesty contract with them.
# --------------------------------------------------------------------------

def to_markdown(doc: DocText, *, include_empty: bool = True) -> str:
    """Render as Markdown with page markers and honest gap annotations."""
    head = [
        f"# {doc.path.stem}",
        "",
        f"*Text layer of `{doc.path.name}` — {len(doc.pages)} pages, "
        f"{doc.total_chars:,} chars ({doc.chars_per_page:.0f}/page).*",
    ]
    if doc.ocr_pages:
        shown = ", ".join(map(str, doc.ocr_pages[:20]))
        more = f" (+{len(doc.ocr_pages)-20} more)" if len(doc.ocr_pages) > 20 else ""
        head += [
            "",
            f"> ⚠ **{len(doc.ocr_pages)} of {len(doc.pages)} pages have little or no "
            f"text layer** — verdict `{doc.verdict}`.",
            f"> Pages: {shown}{more}.",
            "> Their content is in images. What follows is only what the PDF itself "
            "carries; run OCR to recover the rest.",
        ]
    if doc.suspect_pages:
        shown = ", ".join(map(str, doc.suspect_pages[:20]))
        more = (f" (+{len(doc.suspect_pages)-20} more)"
                if len(doc.suspect_pages) > 20 else "")
        fired = ", ".join(f"{n} {c}" for n, c in doc.signal_counts.items() if c)
        head += [
            "",
            f"> ⚠ **{len(doc.suspect_pages)} of {len(doc.pages)} pages carry text that "
            f"may not be FAITHFUL** — verdict `{doc.structure_verdict}` ({fired}).",
            f"> Pages: {shown}{more}.",
        ] + [
            f"> - `{name}` on {count} page(s) — {structure.WHY[name]}."
            for name, count in doc.signal_counts.items() if count
        ] + [
            ">",
            "> **OCR is not the repair** — the glyphs are already in the file with "
            "correct coordinates. Re-extract with layout awareness, or read the page "
            "image. Nothing here is silently rewritten: collapsing the spacing or "
            "re-stacking the fragments is guesswork.",
        ]
    head.append("")

    body: list[str] = []
    for p in doc.pages:
        if p.verdict == "empty" and not include_empty:
            continue
        notes = [] if p.verdict == "ok" else [f"{p.verdict}, {p.images} image(s)"]
        if p.suspect:
            notes.append("structure suspect: " + ", ".join(p.fired))
        tag = f"  *({'; '.join(notes)})*" if notes else ""
        body += ["", "---", "", f"## Page {p.page}{tag}", ""]
        body.append(p.text if p.text else "*(no text layer on this page)*")
    return "\n".join(head + body).rstrip() + "\n"


def to_text(doc: DocText) -> str:
    """Plain text with page markers, for grep."""
    parts = []
    for p in doc.pages:
        mark = p.verdict + (f", {p.structure}" if p.suspect else "")
        parts.append(f"\n=== page {p.page} ({mark}) ===\n")
        parts.append(p.text or "(no text layer)")
    return "".join(parts).strip() + "\n"


# --------------------------------------------------------------------------
# LaTeX -- a FRAGMENT, not a document.
#
# docs/plans/text-layer-first.md open question 4 asks whether `--format tex`
# emits a document or a fragment, and it is not settled. A fragment is the
# REVERSIBLE choice: wrapping one in a preamble is a two-line \documentclass,
# while unwrapping a document means parsing back out of it. Emitting the
# reversible half leaves the operator's decision genuinely open.
# --------------------------------------------------------------------------

# The ten characters TeX will not take literally. `\` must map to a command
# that itself contains braces, so every character is substituted in ONE pass
# rather than sequentially -- a sequential pass re-escapes its own output.
_TEX_ESCAPE = {
    "\\": r"\textbackslash{}",
    "{": r"\{", "}": r"\}",
    "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}
_TEX_RE = re.compile("|".join(re.escape(c) for c in _TEX_ESCAPE))


def tex_escape(s: str) -> str:
    """Make extracted text safe to typeset.

    This is ESCAPING, not repair: it is lossless, mechanical and reversible,
    and without it the format does not parse. docs/scope.md's permanent ban is
    on *silently repairing* extracted text -- collapsing letter spacing,
    de-hyphenating, re-flowing. None of that happens here. Every character
    that reaches the output is the character the PDF carried.
    """
    return _TEX_RE.sub(lambda m: _TEX_ESCAPE[m.group()], s)


def to_latex(doc: DocText) -> str:
    """LaTeX fragment: the same header contract, the same page markers.

    Non-ASCII characters pass through untouched, because on born-digital
    LaTeX the text layer wins outright -- `∑ ∫ 𝜋 𝜔` extract as real
    characters and turning them into control sequences would be a
    transformation, not an extraction (plan section 6, signal 4). The
    consequence is that this needs a Unicode engine: compile with lualatex or
    xelatex plus `unicode-math`. The header says so, in the file.
    """
    out = [
        f"% {doc.path.name} — text layer, extracted by ocr-handler.",
        "% A FRAGMENT: \\input it, or wrap it in a preamble of your own.",
        "% Unicode maths passes through verbatim — compile with lualatex or",
        "% xelatex and \\usepackage{unicode-math}.",
        "",
        f"\\section*{{{tex_escape(doc.path.stem)}}}",
        "",
        f"\\emph{{Text layer of \\texttt{{{tex_escape(doc.path.name)}}} --- "
        f"{len(doc.pages)} pages, {doc.total_chars:,} chars "
        f"({doc.chars_per_page:.0f}/page).}}",
    ]
    # The gap annotations are the honesty contract and must survive into every
    # format, not just the one a reader is most likely to open.
    if doc.ocr_pages:
        shown = ", ".join(map(str, doc.ocr_pages[:20]))
        more = f" (+{len(doc.ocr_pages)-20} more)" if len(doc.ocr_pages) > 20 else ""
        out += [
            "",
            "\\begin{quote}",
            f"\\textbf{{Warning: {len(doc.ocr_pages)} of {len(doc.pages)} pages have "
            f"little or no text layer}} --- verdict \\texttt{{{doc.verdict}}}. "
            f"Pages: {shown}{more}. Their content is in images; what follows is only "
            "what the PDF itself carries.",
            "\\end{quote}",
        ]
    if doc.suspect_pages:
        shown = ", ".join(map(str, doc.suspect_pages[:20]))
        more = (f" (+{len(doc.suspect_pages)-20} more)"
                if len(doc.suspect_pages) > 20 else "")
        fired = ", ".join(f"{n} {c}" for n, c in doc.signal_counts.items() if c)
        out += [
            "",
            "\\begin{quote}",
            f"\\textbf{{Warning: {len(doc.suspect_pages)} of {len(doc.pages)} pages "
            f"carry text that may not be FAITHFUL}} --- verdict "
            f"\\texttt{{{doc.structure_verdict}}} ({tex_escape(fired)}). "
            f"Pages: {shown}{more}. \\textbf{{OCR is not the repair}} --- the glyphs "
            "are already in the file with correct coordinates. Nothing here is "
            "silently rewritten.",
            "\\end{quote}",
        ]
    for p in doc.pages:
        notes = [] if p.verdict == "ok" else [f"{p.verdict}, {p.images} image(s)"]
        if p.suspect:
            notes.append("structure suspect: " + ", ".join(p.fired))
        tag = f" ({tex_escape('; '.join(notes))})" if notes else ""
        out += ["", f"\\subsection*{{Page {p.page}{tag}}}", ""]
        out.append(tex_escape(p.text) if p.text
                   else "\\emph{(no text layer on this page)}")
    return "\n".join(out).rstrip() + "\n"


# --------------------------------------------------------------------------
# JSONL -- the intermediate itself, one record per page.
#
# ADR-0005 is UNDER REVIEW: JSONL versus the `<|det|>` tagged-string format is
# an open operator decision (docs/scope.md open decision 5). What is emitted
# here is deliberately only the half that is not in dispute -- the TEXT
# variant, which no engine's native format was ever a candidate for. There is
# no `ocr` variant and no `agreement` block, so the open question is untouched
# and nothing downstream is built against an unsettled schema.
# --------------------------------------------------------------------------

def page_record(page, *, chosen: str = "text", reason: str = "") -> dict:
    """One page's record, in the plan's section 4 shape.

    `chosen` and `reason` are mandatory on every record in every mode: a tool
    that picks one text over another without saying why is the system that
    does not tell the truth about itself.
    """
    variants = {"text": {"source": "textlayer/pymupdf",
                         "chars": page.chars, "text": page.text}}
    rec = {
        "page": page.page,
        "verdict": page.verdict,
        "chars": page.chars,
        "images": page.images,
        # `null` where the count was not taken -- see PageText.drawings. A
        # measurement that was not made and one that came back zero are
        # different facts and must not print the same.
        "drawings": page.drawings,
        "drawn_images": page.drawn_images,
        "structure": page.structure,
        "signals": list(page.fired),
        "letter_spaced": "letter-spaced" in page.fired,
        "variants": variants,
        "chosen": chosen,
        "reason": reason or _text_only_reason(page),
    }
    if page.skip_reason:
        rec["skipped"] = page.skip_reason
    return rec


def _text_only_reason(page) -> str:
    """Why the text layer was chosen, in the one mode that has no rival."""
    if page.verdict == "ok":
        return f"text layer ok ({page.chars} chars); no recognition needed"
    if page.skip_reason:
        return f"{page.verdict} ({page.chars} chars); {page.skip_reason}"
    return (f"text layer {page.verdict} ({page.chars} chars); content is in "
            f"{page.images or page.drawn_images} image(s) and "
            f"{page.drawings} drawing(s), not recovered in text mode")


def to_jsonl(doc: DocText) -> str:
    """The intermediate as JSONL -- greppable, streamable, one line per page."""
    return "".join(json.dumps(page_record(p), ensure_ascii=False) + "\n"
                   for p in doc.pages)


# Format name -> renderer. The CLI's `--format` values are exactly these keys,
# so adding a format is adding a row here and nothing else.
FORMATS = {"md": to_markdown, "txt": to_text, "tex": to_latex, "json": to_jsonl}


def render(doc: DocText, fmt: str) -> str:
    """Render `doc` in `fmt`. Raises KeyError on an unknown format."""
    return FORMATS[fmt](doc)
