"""Command line interface.

ONE place that turns PDFs into text, for every course. Individual course
folders should call this rather than growing their own extractor -- there were
already two divergent ones (cesc_410/hw/tools/course_text.py using pdftotext,
cpsc_462/tools/extract_notes.py using PyMuPDF) that disagreed about what
counts as a usable text layer.

    ocr-handler inspect FILE.pdf              is OCR even needed?
    ocr-handler text    FILE.pdf -o OUT/      extract the text layer
    ocr-handler text    FILE.pdf --format txt

The two halves are deliberately separate commands, because they cost wildly
different amounts: reading a text layer is milliseconds, OCR is seconds per
page on a GPU. Always `inspect` first -- a document that is already
`text-layer-sufficient` needs no OCR, and running it anyway would be slower
AND worse than the bytes already in the file.
"""

from __future__ import annotations

from pathlib import Path

import typer

from . import textlayer

app = typer.Typer(add_completion=False, help=__doc__)


def _parse_pages(spec: str | None) -> list[int] | None:
    """'1-5,9' -> [1,2,3,4,5,9]. None means every page."""
    if not spec:
        return None
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        elif part:
            out.append(int(part))
    return sorted(set(out))


@app.command()
def inspect(
    pdf: Path = typer.Argument(..., exists=True, dir_okay=False),
    pages: str = typer.Option(None, "--pages", "-p", help="e.g. 1-10,15"),
) -> None:
    """Report whether the text layer is usable, per page. Runs no OCR."""
    doc = textlayer.extract(pdf, _parse_pages(pages))
    typer.echo(f"{pdf.name}: {len(doc.pages)} pages, "
               f"{doc.total_chars:,} chars ({doc.chars_per_page:.0f}/page)")
    typer.echo(f"verdict: {doc.verdict}")
    counts = {v: sum(1 for p in doc.pages if p.verdict == v)
              for v in ("ok", "sparse", "empty")}
    typer.echo(f"  ok {counts['ok']}   sparse {counts['sparse']}   empty {counts['empty']}")
    if doc.ocr_pages:
        shown = ", ".join(map(str, doc.ocr_pages[:30]))
        typer.echo(f"  pages needing OCR: {shown}"
                   + (f" (+{len(doc.ocr_pages)-30} more)" if len(doc.ocr_pages) > 30 else ""))
    if any(textlayer.is_letter_spaced(p.text) for p in doc.pages):
        typer.echo("  ! letter-spacing artefacts detected (one glyph per text run)")


@app.command()
def text(
    pdf: Path = typer.Argument(..., exists=True, dir_okay=False),
    out: Path = typer.Option(None, "--out", "-o", help="output directory"),
    fmt: str = typer.Option("md", "--format", "-f", help="md | txt"),
    pages: str = typer.Option(None, "--pages", "-p", help="e.g. 1-10,15"),
) -> None:
    """Extract the text layer. Writes to OUT, or stdout if OUT is omitted."""
    if fmt not in ("md", "txt"):
        raise typer.BadParameter("--format must be md or txt")
    doc = textlayer.extract(pdf, _parse_pages(pages))
    body = textlayer.to_markdown(doc) if fmt == "md" else textlayer.to_text(doc)

    if out is None:
        typer.echo(body)
        return
    out.mkdir(parents=True, exist_ok=True)
    slug = pdf.stem.lower()
    for ch in " &()":
        slug = slug.replace(ch, "_")
    slug = "_".join(filter(None, slug.split("_")))
    dest = out / f"{slug}.{fmt}"
    dest.write_text(body, encoding="utf-8")
    typer.echo(f"{dest}  ({dest.stat().st_size/1024:.0f} KB, verdict: {doc.verdict})")
    if doc.ocr_pages:
        typer.echo(f"  ⚠ {len(doc.ocr_pages)}/{len(doc.pages)} pages need OCR "
                   f"— this file carries only what the text layer had")


@app.command()
def version() -> None:
    """Print the version."""
    typer.echo("ocr-handler 0.1.0")


def main() -> None:
    """Entry point declared in pyproject.toml ([project.scripts])."""
    app()


if __name__ == "__main__":
    main()
