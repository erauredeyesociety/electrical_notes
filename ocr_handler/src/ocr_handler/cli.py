"""Command line interface.

ONE place that turns PDFs into text, for every course. Individual course
folders should call this rather than growing their own extractor -- there were
already two divergent ones (cesc_410/hw/tools/course_text.py using pdftotext,
cpsc_462/tools/extract_notes.py using PyMuPDF) that disagreed about what
counts as a usable text layer.

    ocr-handler inspect FILE.pdf              is OCR even needed? is the text faithful?
    ocr-handler extract FILE.pdf -o OUT/      the one extraction verb
    ocr-handler extract FILE.pdf --format txt
    ocr-handler extract FILE.pdf --mode auto  ... and recognise the pages it failed on
    ocr-handler check   READINGS              is a model's LaTeX reading trustworthy?
    ocr-handler check   eq.tex --crop 720x130 ... and what would repair change?

The two halves are deliberately separate commands, because they cost wildly
different amounts: reading a text layer is milliseconds, OCR is seconds per
page on a GPU. Always `inspect` first -- a document that is already
`text-layer-sufficient` needs no OCR, and running it anyway would be slower
AND worse than the bytes already in the file.

`check` is the third free verb and belongs to the same family: it reads a
recorded model output rather than a PDF, and like `inspect` it writes nothing,
loads no model and needs no GPU. Verb count is capped at five by
docs/scope.md; this is the third.
"""

from __future__ import annotations

import difflib
import json
import re
import sys
from pathlib import Path
from typing import NamedTuple

import typer

from . import emit, latex_repair, recognize, textlayer, validity

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
    """Report whether the text layer is usable AND whether it is faithful.

    Two axes, because they have different repairs: density (`ok`/`sparse`/
    `empty`) says whether OCR is needed, structure (`intact`/`suspect`) says
    whether the characters that ARE there survived with their layout. A page
    can be dense and wrong. Runs no OCR and loads no model.
    """
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

    # Second axis: the text is present, but is it FAITHFUL? Printed only when
    # something fired -- the 214 genuinely clean documents must not gain noise.
    if doc.suspect_pages:
        fired = "  ".join(f"{n} {c}" for n, c in doc.signal_counts.items())
        typer.echo(f"  ! {doc.structure_verdict}: {len(doc.suspect_pages)}/"
                   f"{len(doc.pages)} pages  ({fired})")
        shown = ", ".join(map(str, doc.suspect_pages[:30]))
        typer.echo(f"    pages: {shown}"
                   + (f" (+{len(doc.suspect_pages)-30} more)"
                      if len(doc.suspect_pages) > 30 else ""))
        for name, count in doc.signal_counts.items():
            if count:
                typer.echo(f"    {name}: {textlayer.structure.WHY[name]}")
        typer.echo("    the characters are present and correct — OCR is NOT the "
                   "repair; re-extract with layout awareness or read the page image")


_MODES = ("text", "ocr", "both", "auto")


def _slug(pdf: Path) -> str:
    """'Module 01 (1).pdf' -> 'module_01_1'. Unchanged from the `text` verb."""
    slug = pdf.stem.lower()
    for ch in " &()":
        slug = slug.replace(ch, "_")
    return "_".join(filter(None, slug.split("_")))


def _blank_note(doc: textlayer.DocText) -> str:
    """The `N pages skipped (blank)` summary line.

    Case 1 of the three in docs/plans/text-layer-first.md section 7, and it
    gets its own line for the reason that section exists: a genuinely blank
    page and a page where OCR came back empty are different events, and
    reporting them as one is how a broken engine looks like a clean corpus.
    """
    return (f"{len(doc.blank_pages)} page(s) skipped (blank: no text, no "
            f"images, no drawings)")


def _refuse_ocr(mode: str, doc: textlayer.DocText, wanted: list[int]) -> None:
    """Fail loudly for the modes whose OCR half does not exist yet.

    Never return empty as if it had succeeded. A page with three images that
    yields no text is a defect report, not a blank page, and a mode that
    quietly degraded to `--mode text` would produce exactly that lie at scale.
    """
    typer.echo(f"error: --mode {mode} needs recognition, and "
               f"{recognize.UNAVAILABLE}", err=True)
    typer.echo(f"  {len(wanted)} of {len(doc.pages)} requested page(s) would "
               f"have been sent to a model.", err=True)
    if mode == "auto" and doc.blank_pages:
        # `auto` is the only mode that filters. `ocr` and `both` were asked
        # for every requested page and would send the blank ones too.
        typer.echo(f"  {_blank_note(doc)}, and not counted above.", err=True)
    raise typer.Exit(1)


@app.command()
def extract(
    pdf: Path = typer.Argument(..., exists=True, dir_okay=False),
    mode: str = typer.Option("text", "--mode", "-m", help="text | ocr | both | auto"),
    out: Path = typer.Option(None, "--out", "-o", help="output directory"),
    fmt: str = typer.Option("md", "--format", "-f", help="md | txt | tex | json"),
    pages: str = typer.Option(None, "--pages", "-p", help="e.g. 1-10,15"),
) -> None:
    """The one extraction verb. Writes to OUT, or stdout if OUT is omitted.

    `--mode` defaults to `text`: the cheap, safe, no-GPU behaviour is what you
    get by not thinking. `auto` is the better everyday choice but has to be
    asked for, because it can spend minutes on a GPU.

    | mode | what runs |
    | text | text layer only -- the 214 text-layer-sufficient documents |
    | ocr  | recognition on every requested page |
    | both | both, side by side, for deciding whether OCR is worth it |
    | auto | text everywhere; OCR only where the text layer failed |

    **The three OCR modes are not built.** The engine is deliberately
    unchosen (ADR-0004), so they refuse and say so rather than quietly
    returning the text layer under another name. `auto` is the exception, and
    only where it is honestly the whole answer: on a document whose every page
    already has a good text layer there is nothing for a model to do, so it
    succeeds and says how many pages it skipped as blank.
    """
    if mode not in _MODES:
        raise typer.BadParameter(f"--mode must be one of {', '.join(_MODES)}")
    if fmt not in emit.FORMATS:
        raise typer.BadParameter(
            f"--format must be one of {', '.join(emit.FORMATS)}")

    doc = textlayer.extract(pdf, _parse_pages(pages))

    if mode in ("ocr", "both"):
        # Every requested page, by definition of the mode.
        _refuse_ocr(mode, doc, [p.page for p in doc.pages])
    if mode == "auto" and doc.ocr_candidates:
        _refuse_ocr(mode, doc, doc.ocr_candidates)
    if mode == "auto" and doc.blank_pages:
        # `auto` got all the way through, so say what it declined to render.
        # stderr, so `extract ... > out.md` still carries the accounting.
        typer.echo(f"  {_blank_note(doc)}", err=True)

    body = emit.render(doc, fmt)
    if out is None:
        typer.echo(body)
        return
    out.mkdir(parents=True, exist_ok=True)
    # The intermediate keeps the plan's name; the views keep the format's.
    dest = out / (f"{_slug(pdf)}.pages.jsonl" if fmt == "json"
                  else f"{_slug(pdf)}.{fmt}")
    dest.write_text(body, encoding="utf-8")
    typer.echo(f"{dest}  ({dest.stat().st_size/1024:.0f} KB, verdict: {doc.verdict})")
    if doc.ocr_pages:
        typer.echo(f"  ⚠ {len(doc.ocr_pages)}/{len(doc.pages)} pages need OCR "
                   f"— this file carries only what the text layer had")


# --------------------------------------------------------------------------
# `check` -- the equation-reading axis. Same contract as `inspect`: two
# questions, one report, nothing rewritten.
# --------------------------------------------------------------------------

# The two recorded harnesses here disagree about field names: tmp/eval/*/
# results.json writes {name, task, size:[w,h], text}, tmp/eqocr/sweep.json
# writes {case, w, h, raw}. Reading both costs four aliases; refusing one is
# the per-caller divergence this project exists to end (docs/scope.md).
def _record(rec: dict, index: int) -> tuple[str, str, tuple[int, int] | None]:
    """One harness row -> `(label, text, crop)`."""
    label = str(rec.get("name") or rec.get("case") or f"#{index}")
    if rec.get("task"):
        label = f"{label}[{rec['task']}]"
    text = rec.get("text")
    if text is None:
        text = rec.get("raw", "")
    size = rec.get("size")
    if size is None and rec.get("w") and rec.get("h"):
        size = (rec["w"], rec["h"])
    crop = (int(size[0]), int(size[1])) if size else None
    return label, text or "", crop


def _parse_crop(spec: str | None) -> tuple[int, int] | None:
    """'720x130' -> (720, 130), the crop `length-vs-crop` measures against.

    Without it that detector reports that it could not run rather than
    passing silently -- and it is the measured winner (8/10 pathologies, 0
    false positives), so a crop-less check is a weaker one.
    """
    if not spec:
        return None
    m = re.fullmatch(r"\s*(\d+)\s*[xX×]\s*(\d+)\s*", spec)
    if not m:
        raise typer.BadParameter("--crop must be WxH in pixels, e.g. 720x130")
    return int(m.group(1)), int(m.group(2))


def _load_readings(spec: str, crop: tuple[int, int] | None
                   ) -> tuple[str, list[tuple[str, str, tuple[int, int] | None]]]:
    """`(display name, [(label, text, crop), ...])` from a path or from stdin."""
    if spec == "-":
        return "<stdin>", [("<stdin>", sys.stdin.read(), crop)]
    path = Path(spec)
    if not path.is_file():
        raise typer.BadParameter(f"no such file: {spec}")
    if path.suffix == ".json":
        if crop is not None:
            raise typer.BadParameter(
                "--crop is for a single reading; a results.json carries a crop "
                "size per record and overriding all of them would be a lie")
        data = json.loads(path.read_text(encoding="utf-8"))
        rows = data.get("results", []) if isinstance(data, dict) else data
        return path.name, [_record(r, i) for i, r in enumerate(rows)]
    return path.name, [(path.name, path.read_text(encoding="utf-8"), crop)]


# How many suspect (or repaired) readings get their evidence printed in full.
# The largest recorded reading set in this repo is 44 -- tmp/eqocr/sweep.json,
# the padding sweep -- so 10 holds the report to about a screen and the rest
# are counted, the same trade `inspect` makes at 30 pages.
_SHOW = 10


# Characters of context around each changed span. Six carries a whole control
# word (`\qquad`, `\right`) into view -- the unit a reader checks a LaTeX
# repair in -- and merges the three insertions `repair` makes in
# tmp/eval/out_crops/crop_eqline_base into one legible span instead of three
# unreadable `'' -> ' '` lines.
_DIFF_CONTEXT = 6


def _diff_spans(old: str, new: str) -> list[str]:
    """The changed spans with context, so a repair can be CHECKED not trusted.

    A whole-string before/after is unreadable at 500 tokens, and that is how a
    silent post-processor stays silent: upstream changed 4 of this repo's 44
    recorded outputs, all four were damage, and nobody would have seen it.
    """
    spans: list[str] = []
    matcher = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    for group in matcher.get_grouped_opcodes(_DIFF_CONTEXT):
        if len(spans) == _SHOW:
            spans.append("...")
            break
        i1, j1 = group[0][1], group[0][3]
        i2, j2 = group[-1][2], group[-1][4]
        spans.append(f"@{i1} {old[i1:i2]!r} -> {new[j1:j2]!r}")
    return spans


class _Row(NamedTuple):
    """One reading, everything computed about it, and nothing applied to it."""

    label: str
    text: str
    signals: tuple
    verdict: str
    repair: latex_repair.Repair


def _readings_verdict(n_suspect: int, n_total: int) -> str:
    """Bands none/some/all, mirroring `textlayer.DocText.structure_verdict`."""
    if not n_suspect:
        return "readings-plausible"
    return "readings-suspect" if n_suspect == n_total else "readings-suspect-partial"


@app.command()
def check(
    readings: str = typer.Argument(
        ...,
        help="a harness results.json, a file holding one expression, or - for stdin"),
    crop: str = typer.Option(None, "--crop", help="WxH of the crop ONE reading came from"),
    apply_repair: bool = typer.Option(
        False, "--repair", help="emit repaired LaTeX on stdout; the report goes to stderr"),
) -> None:
    """Is a model's LaTeX reading trustworthy, and what would repair change?

    Two axes again, and the same rule `inspect` follows: report, never
    rewrite. Validity (`plausible`/`suspect`) is eight cheap detectors over
    the token stream, and it exists because compile-checking is dead -- 83 of
    84 recorded outputs compiled under tectonic, including 1,113 tokens of
    array garbage read off a whole page. `length-vs-crop` is the measured
    winner, so pass --crop for a single reading; a results.json carries its
    own crop sizes.

    Repair is shown as a per-rule roll-call and a diff of the changed spans,
    and is applied only when you ask with --repair -- conservative by
    construction, because the suite this one is derived from changed 4 of
    this repo's 44 recorded outputs and all four were damage.

    Runs no model, loads no weights, needs no GPU.
    """
    name, items = _load_readings(readings, _parse_crop(crop))
    if not items:
        raise typer.BadParameter(f"{name}: no readings found")

    # The report goes to stderr under --repair so `check x.tex --repair >
    # fixed.tex` still tells the reader what was changed and what is suspect.
    def say(line: str) -> None:
        typer.echo(line, err=apply_repair)

    rows: list[_Row] = []
    for label, text, box in items:
        sigs = validity.signals(text, crop=box)
        rows.append(_Row(label, text, sigs, validity.classify(sigs),
                         latex_repair.repair(text)))

    suspect = [r for r in rows if r.verdict == validity.SUSPECT]
    counts = {n: sum(1 for r in rows for s in r.signals if s.fired and s.name == n)
              for n in validity.NAMES}
    total = sum(len(validity.tokens(r.text)) for r in rows)
    plural = "reading" if len(rows) == 1 else "readings"
    # A one-record results.json still has to name the record: the file it came
    # from is not the crop anyone will go back and look at.
    title = (name if len(rows) > 1 or rows[0].label == name
             else f"{name} — {rows[0].label}")
    say(f"{title}: {len(rows)} {plural}, {total:,} tokens "
        f"({total / len(rows):.0f}/reading)")
    say(f"verdict: {_readings_verdict(len(suspect), len(rows))}")
    say(f"  plausible {len(rows) - len(suspect)}   suspect {len(suspect)}")

    if len(rows) == 1:
        # One reading gets the full roll-call, including the detectors that
        # stayed quiet and the one that could not run -- a report that lists
        # only what fired cannot be checked for what it failed to look at.
        for s in rows[0].signals:
            mark = "!" if s.fired else "·"
            say(f"  {mark} {s.name:24s} {s.detail}".rstrip())
    elif suspect:
        fired = "  ".join(f"{n} {c}" for n, c in counts.items() if c)
        say(f"  ! {len(suspect)}/{len(rows)} readings  ({fired})")
        for row in suspect[:_SHOW]:
            for s in row.signals:
                if s.fired:
                    say(f"    {row.label} — {s.name}: {s.detail}")
        if len(suspect) > _SHOW:
            say(f"    (+{len(suspect) - _SHOW} more)")

    if suspect:
        for detector, count in counts.items():
            if count:
                say(f"    {detector}: {validity.WHY[detector]}")
        say("    nothing here was rewritten — a suspect reading is re-cropped "
            "or re-read, never silently patched; --repair fixes SYNTAX, not a "
            "bad reading")

    changed = [r for r in rows if r.repair.text != r.text]
    if not changed:
        say(f"  repair: no change to any of {len(rows)} {plural}")
    else:
        say(f"  repair would change {len(changed)}/{len(rows)} {plural} "
            f"— shown, not applied (--repair to emit)")
        for row in changed[:_SHOW]:
            say(f"    {row.label}")
            for note in row.repair.notes:
                say(f"      · {note}")
            for span in _diff_spans(row.text, row.repair.text):
                say(f"      {span}")
            if not row.repair.notes:
                say("      ! changed with no rule named — an unexplained repair "
                    "is the defect this module exists to avoid; report it")
        if len(changed) > _SHOW:
            say(f"    (+{len(changed) - _SHOW} more)")

    if apply_repair:
        for row in rows:
            flags = ",".join(s.name for s in row.signals if s.fired)
            if len(rows) > 1 or flags:
                # `%` so the emitted stream is still LaTeX, and so the
                # suspicion travels with the text instead of staying in a
                # terminal the next reader never saw.
                typer.echo(f"% {row.label}"
                           + (f"  [{row.verdict}: {flags}]" if flags else ""))
            typer.echo(row.repair.text)


@app.command()
def version() -> None:
    """Print the version."""
    typer.echo("ocr-handler 0.1.0")


def main() -> None:
    """Entry point declared in pyproject.toml ([project.scripts])."""
    app()


if __name__ == "__main__":
    main()
