"""Regression floor for the SHIPPED command path.

The existing floor (test_backbone.py) covers `pdfops` and `ink`. `cli.py`
imports neither -- it imports `textlayer` -- so until this file existed the
command the operator actually runs had zero coverage. That gap was found by an
audit, not by a failure, which is exactly the kind of thing a floor is for.

These tests build their own PDFs in-process rather than depending on course
material, so they run on any machine. That matters: 5 of the 7 backbone tests
skip without the lecture PDFs, leaving 2 real tests on a clean checkout.
"""

from __future__ import annotations

import pytest

from ocr_handler import textlayer


def _make_pdf(path, pages: list[str]):
    """Write a small PDF whose pages carry the given text.

    Uses insert_textbox, not insert_text: the latter draws ONE unwrapped line,
    so a long string runs off the page edge and only the visible ~97 chars end
    up in the text layer -- which silently made 'dense' pages classify as
    'sparse' and broke four tests before this was fixed.
    """
    import pymupdf

    doc = pymupdf.open()
    for body in pages:
        page = doc.new_page()
        if body:
            rect = pymupdf.Rect(50, 50, page.rect.width - 50, page.rect.height - 50)
            leftover = page.insert_textbox(rect, body, fontsize=9)
            assert leftover >= 0, "fixture text did not fit on the page"
    doc.save(path)
    doc.close()
    return path


# --------------------------------------------------------------------------
# Classification -- the decision that routes pages to an expensive GPU model.
# --------------------------------------------------------------------------

def test_dense_page_is_ok_and_needs_no_ocr(tmp_path):
    pdf = _make_pdf(tmp_path / "dense.pdf", ["word " * 200])
    doc = textlayer.extract(pdf)
    assert doc.pages[0].verdict == "ok"
    assert not doc.pages[0].needs_ocr
    assert doc.verdict == "text-layer-sufficient"
    assert doc.ocr_pages == []


def test_blank_page_is_empty_and_needs_ocr(tmp_path):
    pdf = _make_pdf(tmp_path / "blank.pdf", [""])
    doc = textlayer.extract(pdf)
    assert doc.pages[0].verdict == "empty"
    assert doc.pages[0].needs_ocr
    assert doc.verdict == "ocr-required"


def test_mixed_document_reports_partial_and_names_the_pages(tmp_path):
    """The whole point of the module: aim OCR at the pages that need it."""
    pdf = _make_pdf(tmp_path / "mixed.pdf", ["word " * 200, "", "word " * 200, "x"])
    doc = textlayer.extract(pdf)
    assert doc.verdict == "ocr-partial"
    # 1-based, and only the thin pages.
    assert doc.ocr_pages == [2, 4]


def test_sparse_sits_between_empty_and_ok(tmp_path):
    """A page just under the gate is 'sparse', not 'empty' -- they differ:
    sparse pages have salvageable text, empty ones have nothing to merge."""
    body = "x" * (textlayer.SPARSE_CHARS - 100)
    pdf = _make_pdf(tmp_path / "sparse.pdf", [body])
    doc = textlayer.extract(pdf)
    assert doc.pages[0].verdict == "sparse"
    assert doc.pages[0].needs_ocr


def test_threshold_is_a_single_source_of_truth():
    """pdfops must not carry its own copy. Two independent 400s is the exact
    divergence this project exists to eliminate."""
    from ocr_handler import pdfops
    assert pdfops.TEXT_LAYER_MIN_CHARS is textlayer.SPARSE_CHARS


# --------------------------------------------------------------------------
# Letter-spacing detection -- the artefact that makes a DENSE page untrustworthy.
# --------------------------------------------------------------------------

def test_detects_letter_spacing_artefact():
    """'C o m p u t e r  O r g a n i z a t i o n' -- one glyph per text run.
    Real: CESC 470 Module 01 page 1, and 8 of 76 cec_315 lecture PDFs."""
    assert textlayer.is_letter_spaced("C o m p u t e r  O r g a n i z a t i o n")


def test_normal_prose_is_not_flagged_as_letter_spaced():
    """Guards the false-positive direction. Without this the detector could be
    trivially 'improved' into flagging everything."""
    assert not textlayer.is_letter_spaced(
        "The inside of a computer: control unit, datapath, and registers."
    )


def test_short_spaced_run_is_not_flagged():
    """'a b c' is legitimate (an itemisation, an axis label). The detector
    requires a run of 6+ single characters before it fires."""
    assert not textlayer.is_letter_spaced("a b c and then normal words follow here")


# --------------------------------------------------------------------------
# Rendering -- the gap annotation must survive into the output.
# --------------------------------------------------------------------------

def test_markdown_warns_when_pages_need_ocr(tmp_path):
    """A transcript that silently omits 62 unreadable pages is worse than no
    transcript: the reader cannot tell what is missing."""
    pdf = _make_pdf(tmp_path / "mixed.pdf", ["word " * 200, ""])
    md = textlayer.to_markdown(textlayer.extract(pdf))
    assert "ocr-partial" in md
    assert "no text layer" in md.lower()


def test_markdown_has_a_page_marker_for_every_page(tmp_path):
    pdf = _make_pdf(tmp_path / "three.pdf", ["a" * 500, "b" * 500, "c" * 500])
    md = textlayer.to_markdown(textlayer.extract(pdf))
    for n in (1, 2, 3):
        assert f"## Page {n}" in md


def test_page_selection_is_one_based(tmp_path):
    """Off-by-one here would silently transcribe the wrong page."""
    pdf = _make_pdf(tmp_path / "sel.pdf", ["AAA" * 200, "BBB" * 200, "CCC" * 200])
    doc = textlayer.extract(pdf, pages=[2])
    assert len(doc.pages) == 1
    assert doc.pages[0].page == 2
    assert "BBB" in doc.pages[0].text


def test_out_of_range_pages_are_ignored_not_fatal(tmp_path):
    pdf = _make_pdf(tmp_path / "one.pdf", ["x" * 500])
    doc = textlayer.extract(pdf, pages=[1, 99])
    assert [p.page for p in doc.pages] == [1]


# --------------------------------------------------------------------------
# CLI -- it is the deliverable; docstrings on commands are load-bearing.
# --------------------------------------------------------------------------

def test_cli_exposes_the_documented_commands():
    from typer.testing import CliRunner
    from ocr_handler.cli import app

    result = CliRunner().invoke(app, ["--help"])
    assert result.exit_code == 0
    for cmd in ("inspect", "text"):
        assert cmd in result.stdout


def test_cli_inspect_reports_a_verdict(tmp_path):
    from typer.testing import CliRunner
    from ocr_handler.cli import app

    pdf = _make_pdf(tmp_path / "d.pdf", ["word " * 200])
    result = CliRunner().invoke(app, ["inspect", str(pdf)])
    assert result.exit_code == 0
    assert "text-layer-sufficient" in result.stdout


def test_cli_text_rejects_an_unknown_format(tmp_path):
    """--format is validated rather than silently producing an empty file."""
    from typer.testing import CliRunner
    from ocr_handler.cli import app

    pdf = _make_pdf(tmp_path / "d.pdf", ["word " * 200])
    result = CliRunner().invoke(app, ["text", str(pdf), "--format", "pdf"])
    assert result.exit_code != 0
