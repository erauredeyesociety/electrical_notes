"""Regression floor for M2: ONE classifier, ONE intermediate, four views.

Every test here builds its own PDF in-process, so the floor holds on a machine
with none of the course material. That is not a nicety: 5 of the 7 backbone
tests skip without the lecture PDFs.

What these guard, in order:

  * the convergence -- `pdfops` must not grow a second classifier back
  * the routing rules that decide whether a GPU is spent at all
  * the four `--mode` gates, and that the unbuilt three FAIL rather than
    quietly returning the text layer under another name
  * `emit`'s output bytes, which are a must-not-break invariant (roadmap M2)
"""

from __future__ import annotations

import json

import pytest
from typer.testing import CliRunner

from ocr_handler import emit, pdfops, recognize, textlayer
from ocr_handler.cli import app


def _pdf(path, pages):
    """Write a PDF. Each page is `(text, n_images, n_drawings)`.

    insert_textbox, not insert_text: the latter draws ONE unwrapped line, so a
    long string runs off the page and only the visible ~97 characters reach
    the text layer.
    """
    import pymupdf

    doc = pymupdf.open()
    for body, n_img, n_draw in pages:
        page = doc.new_page()
        if body:
            rect = pymupdf.Rect(50, 50, page.rect.width - 50, page.rect.height - 400)
            assert page.insert_textbox(rect, body, fontsize=9) >= 0, "text did not fit"
        for i in range(n_img):
            pix = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, 8, 8), False)
            pix.clear_with(90 + i)
            page.insert_image(pymupdf.Rect(50 + 20 * i, 700, 66 + 20 * i, 716),
                              pixmap=pix)
        for i in range(n_draw):
            page.draw_line(pymupdf.Point(50, 600 + i), pymupdf.Point(300, 600 + i))
    doc.save(path)
    doc.close()
    return path


DENSE = "word " * 200      # comfortably over SPARSE_CHARS
THIN = "x " * 40           # comfortably under it, and over EMPTY_CHARS


# --------------------------------------------------------------------------
# 1 -- ONE classifier. `pdfops` used to carry a second implementation of this
# question on a second PDF library (poppler, via subprocess), with its own
# 400. Converging it changed 428 of 7,187 corpus pages; the measurement is in
# docs/findings/one-classifier-2026-09-06.md. Nothing may re-introduce it.
# --------------------------------------------------------------------------

def test_threshold_is_a_single_source_of_truth():
    """Two independent 400s is the exact divergence this project ends."""
    assert pdfops.TEXT_LAYER_MIN_CHARS is textlayer.SPARSE_CHARS


def test_pdfops_classification_is_textlayers_classification(tmp_path):
    """`pdfops.inspect_all` must be a VIEW of `textlayer.extract`, not a
    second opinion. If these ever disagree, two classifiers are live again."""
    pdf = _pdf(tmp_path / "mixed.pdf",
               [(DENSE, 0, 0), (THIN, 1, 0), ("", 0, 0), (DENSE, 2, 3)])
    infos = pdfops.inspect_all(pdf)
    pages = textlayer.extract(pdf).pages
    assert [i.number for i in infos] == [p.page for p in pages]
    assert [i.chars for i in infos] == [p.chars for p in pages]
    assert [i.images for i in infos] == [p.images for p in pages]
    assert [i.has_text_layer for i in infos] == [not p.needs_ocr for p in pages]


def test_no_poppler_subprocess_on_the_classification_path(tmp_path, monkeypatch):
    """ADR-0001: PyMuPDF is the only PDF library. The classifier must not
    shell out, so the tool keeps working where poppler is not installed."""
    def explode(*a, **k):                       # pragma: no cover - must not run
        raise AssertionError("classification shelled out to poppler")

    monkeypatch.setattr(pdfops, "_run", explode)
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0), ("", 0, 0)])
    assert [i.kind for i in pdfops.inspect_all(pdf)] == ["text", "blank"]
    assert pdfops.page_count(pdf) == 2
    assert pdfops.page_text(pdf, 1).startswith("word")
    pdfops.producer(pdf)                        # metadata, also PyMuPDF now


# --------------------------------------------------------------------------
# 2 -- The routing rules. These decide whether a GPU second is spent.
# --------------------------------------------------------------------------

def test_document_verdict_matches_page_verdicts(tmp_path):
    """The invariant: all `ok` => sufficient; none `ok` => required; else
    partial. Consumed by cli.py, by pdfops and by an external caller in
    content/cesc_470/md_notes/README.md."""
    every = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0), (DENSE, 0, 0)])
    none = _pdf(tmp_path / "b.pdf", [("", 0, 0), (THIN, 0, 0)])
    some = _pdf(tmp_path / "c.pdf", [(DENSE, 0, 0), (THIN, 0, 0)])
    for pdf, expected in ((every, "text-layer-sufficient"),
                          (none, "ocr-required"), (some, "ocr-partial")):
        doc = textlayer.extract(pdf)
        assert doc.verdict == expected
        assert (doc.ocr_pages == []) == (expected == "text-layer-sufficient")
        assert (len(doc.ocr_pages) == len(doc.pages)) == (expected == "ocr-required")


def test_blank_pages_are_never_sent_to_ocr(tmp_path):
    """The one measured rule that SAVES work. A page with no text, no images
    and no vector paths has nothing on it; rendering it and loading a model is
    pure waste, and it must be refused before any render."""
    pdf = _pdf(tmp_path / "blank.pdf", [("", 0, 0), (THIN, 1, 0)])
    doc = textlayer.extract(pdf)
    assert doc.pages[0].skip_reason == "no content"
    assert doc.blank_pages == [1]
    assert doc.ocr_candidates == [2]            # the page with an image, only
    assert 1 in doc.ocr_pages                   # still counted as thin, though


def test_a_vector_only_page_is_not_blank(tmp_path):
    """The correction that put `drawings` in `PageText`, and the direction
    that loses content. Testing images alone called 405 corpus pages blank
    that carry vector drawings -- lctr22-exercise.pdf page 1 is 0 characters,
    0 images, 1,837 paths and 8.9% non-white pixels at 72 dpi. Skipping those
    would silently discard whole pages."""
    pdf = _pdf(tmp_path / "vector.pdf", [("", 0, 12)])
    page = textlayer.extract(pdf).pages[0]
    assert page.images == 0
    assert page.drawings == 12
    assert page.skip_reason is None, "a page of vector content is not blank"
    assert pdfops.inspect(pdf, 1).kind == "image"


def test_drawings_are_not_measured_where_they_cannot_change_an_answer(tmp_path):
    """Lazy on purpose, and the laziness is visible rather than faked.
    Measured over 7,187 pages: eager get_drawings costs 83.4 s against a 15.8 s
    text pass; lazy get_cdrawings costs 2.2 s. Where it was not taken the
    field is None, never 0 -- a count not taken and a count of zero differ."""
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 5), (THIN, 0, 5), (THIN, 1, 5)])
    pages = textlayer.extract(pdf).pages
    assert pages[0].drawings is None, "an ok page can never be skipped"
    assert pages[1].drawings == 5, "thin + no image is where it decides"
    assert pages[2].drawings is None, "an image already proves there is content"


def test_ocr_never_silently_replaces_a_clean_text_layer(tmp_path):
    """The founding rule (ADR-0003), as a contract test. An `ok` page is never
    an OCR candidate, whatever else is on it."""
    pdf = _pdf(tmp_path / "rich.pdf", [(DENSE, 3, 20)])
    doc = textlayer.extract(pdf)
    assert doc.pages[0].verdict == "ok"
    assert not doc.pages[0].needs_ocr
    assert doc.ocr_candidates == []
    assert pdfops.inspect(pdf, 1).kind == "text"


# --------------------------------------------------------------------------
# 3 -- The four modes. The three unbuilt ones must FAIL, not return empty.
# --------------------------------------------------------------------------

def test_recognition_refuses_instead_of_returning_nothing(tmp_path):
    """Returning "" would be indistinguishable from a blank page, which is
    exactly the conflation docs/plans/text-layer-first.md section 7 forbids."""
    assert not recognize.available()
    with pytest.raises(recognize.EngineUnavailable):
        recognize.recognize(tmp_path / "nope.pdf", 1)


@pytest.mark.parametrize("mode", ["ocr", "both"])
def test_ocr_modes_fail_loudly_and_write_nothing(tmp_path, mode):
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0)])
    out = tmp_path / "out"
    result = CliRunner().invoke(app, ["extract", str(pdf), "--mode", mode,
                                      "-o", str(out)])
    assert result.exit_code == 1, "a mode that cannot run must not exit 0"
    assert "no recognition engine is selected" in result.output
    assert "0004" in result.output, "the refusal must name the open decision"
    assert not out.exists(), "a failed run must not write a half-answer"


def test_auto_refuses_when_a_page_actually_needs_a_model(tmp_path):
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0), (THIN, 2, 0)])
    result = CliRunner().invoke(app, ["extract", str(pdf), "--mode", "auto"])
    assert result.exit_code == 1
    assert "1 of 2 requested page(s)" in result.output


def test_auto_succeeds_when_no_page_needs_a_model(tmp_path):
    """`auto` is 'OCR only where the text layer failed'. Where it failed
    nowhere, the run is complete WITHOUT a model and claiming otherwise would
    be dishonest in the other direction. Half the corpus (214/430 documents)
    is this case."""
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0), (DENSE, 0, 0)])
    result = CliRunner().invoke(app, ["extract", str(pdf), "--mode", "auto"])
    assert result.exit_code == 0
    assert "# a" in result.output


def test_auto_reports_blank_pages_it_declined_to_render(tmp_path):
    """Case 1 of the three 'OCR returned nothing' cases gets its own line."""
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0), ("", 0, 0)])
    result = CliRunner().invoke(app, ["extract", str(pdf), "--mode", "auto"])
    assert result.exit_code == 0
    assert "1 page(s) skipped (blank" in result.output


def test_the_text_verb_is_gone(tmp_path):
    """`text` became `extract --mode text`. Keeping both would put the CLI at
    five verbs of the five docs/scope.md allows, for one capability."""
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0)])
    assert CliRunner().invoke(app, ["text", str(pdf)]).exit_code != 0
    assert CliRunner().invoke(app, ["extract", str(pdf)]).exit_code == 0


def test_unknown_mode_and_format_are_refused(tmp_path):
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0)])
    for args in (["--mode", "magic"], ["--format", "docx"]):
        assert CliRunner().invoke(app, ["extract", str(pdf), *args]).exit_code != 0


# --------------------------------------------------------------------------
# 4 -- One intermediate, four views. `to_markdown`/`to_text` moved into
# `emit` and their bytes must not have moved with them.
# --------------------------------------------------------------------------

def test_textlayer_still_exports_the_renderers(tmp_path):
    """They are the shipped names with existing callers; a refactor should not
    churn them."""
    assert textlayer.to_markdown is emit.to_markdown
    assert textlayer.to_text is emit.to_text


def test_extract_text_mode_is_byte_stable(tmp_path):
    """Golden master, transcribed verbatim rather than pointed at.

    This is the promise that lets the three per-course scripts be deleted:
    that `extract --mode text` produces a known, stable, honest artifact. It
    was also verified across all 448 corpus documents by SHA-256 before and
    after the M2 refactor -- md and txt identical on every one.
    """
    pdf = _pdf(tmp_path / "sample.pdf", [("Hello world.", 0, 0)])
    doc = textlayer.extract(pdf)
    assert emit.to_markdown(doc) == (
        "# sample\n"
        "\n"
        "*Text layer of `sample.pdf` — 1 pages, 12 chars (12/page).*\n"
        "\n"
        "> ⚠ **1 of 1 pages have little or no text layer** — verdict "
        "`ocr-required`.\n"
        "> Pages: 1.\n"
        "> Their content is in images. What follows is only what the PDF "
        "itself carries; run OCR to recover the rest.\n"
        "\n"
        "\n"
        "---\n"
        "\n"
        "## Page 1  *(empty, 0 image(s))*\n"
        "\n"
        "Hello world.\n"
    )
    assert emit.to_text(doc) == "=== page 1 (empty) ===\nHello world.\n"


def test_every_format_renders_and_carries_the_gap_warning(tmp_path):
    """The header block is the honesty contract with a reader who never opens
    the intermediate, so it has to survive into every view, not just Markdown."""
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0), (THIN, 1, 0)])
    doc = textlayer.extract(pdf)
    assert set(emit.FORMATS) == {"md", "txt", "tex", "json"}
    for fmt in ("md", "tex"):
        assert "ocr-partial" in emit.render(doc, fmt), fmt
    assert emit.render(doc, "json").count("\n") == 2       # one record per page


def test_latex_escapes_rather_than_repairs(tmp_path):
    """Escaping is lossless and mechanical; docs/scope.md's permanent ban is on
    silently *repairing* text. Every character the PDF carried must survive."""
    assert emit.tex_escape(r"50% of a_b & {c} $d$ #e ~f ^g \h") == (
        r"50\% of a\_b \& \{c\} \$d\$ \#e \textasciitilde{}f "
        r"\textasciicircum{}g \textbackslash{}h")
    # A letter-spacing artefact is REPORTED, never collapsed.
    pdf = _pdf(tmp_path / "a.pdf", [("C o m p u t e r  O r g a n i z a t i o n", 0, 0)])
    tex = emit.to_latex(textlayer.extract(pdf))
    assert "C o m p u t e r" in tex
    assert "letter-spaced" in tex


def test_jsonl_record_always_says_what_was_chosen_and_why(tmp_path):
    """A tool that picks one text over another without saying why is the
    system that does not tell the truth about itself."""
    pdf = _pdf(tmp_path / "a.pdf", [(DENSE, 0, 0), ("", 0, 0), (THIN, 1, 0)])
    recs = [json.loads(line)
            for line in emit.to_jsonl(textlayer.extract(pdf)).splitlines()]
    assert [r["page"] for r in recs] == [1, 2, 3]
    for r in recs:
        assert r["chosen"] == "text"
        assert r["reason"], "every record, every mode"
    assert recs[1]["skipped"] == "no content"
    assert "skipped" not in recs[2], "a page with an image is not blank"
    # Only the text variant exists: ADR-0005 leaves the OCR half's
    # representation an open decision and nothing here presumes it.
    assert set(recs[0]["variants"]) == {"text"}


def test_json_output_is_written_as_the_plans_intermediate(tmp_path):
    pdf = _pdf(tmp_path / "Some Doc (1).pdf", [(DENSE, 0, 0)])
    out = tmp_path / "out"
    result = CliRunner().invoke(app, ["extract", str(pdf), "-f", "json",
                                      "-o", str(out)])
    assert result.exit_code == 0
    assert (out / "some_doc_1.pages.jsonl").is_file()
