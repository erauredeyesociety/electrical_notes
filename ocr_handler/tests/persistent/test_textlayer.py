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
    for cmd in ("inspect", "text", "check"):
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


# --------------------------------------------------------------------------
# Structural faithfulness -- the SECOND axis. Density answers "is there text?";
# these answer "is the text a faithful rendering of the page?". The defect they
# guard: a 47-page LaTeX PDF whose every equation was shredded scored `ok` on
# all 47 pages, and got routed AWAY from further processing.
# Design: docs/plans/structural-faithfulness.md
# --------------------------------------------------------------------------

# A 3x3 matrix equation as PyMuPDF actually extracts one -- reading order, so
# the 2-D layout arrives as a column of fragments. Shaped after fixture page 7
# of dual_camera_3d_localization_tutorial.pdf, the retained regression case,
# but written in WinAnsi: a synthetic PDF is drawn in base-14 Helvetica, so a
# literal lambda or a Computer Modern bracket piece round-trips as "?" and the
# fixture would be testing the font rather than the detector. Measured, so the
# next author does not retry it: of the characters this fixture would want,
# Helvetica draws only the Latin-1 block -- `°±²³µ·×÷` survive a round trip,
# `λ Σ ∞ − ∫ U+F8EE` all come back as "?".
#
# The `×` is load-bearing and is NOT decoration. Since the 2026-09-06 sweep
# (docs/findings/recall-was-a-symbol-test-not-a-run-length.md)
# a run must carry at least one genuine
# mathematical character; a column of lone ASCII letters is a Wingdings bullet
# list or an assembly gutter and is deliberately no longer suspect. On the real
# page that character is the PUA bracket piece -- see the verbatim fixture
# below, which is string-level precisely because no synthetic PDF can carry it.
FLATTENED_MATRIX = "\n".join([
    "with (cx, cy) the principal point, the calibration matrix K is",
    "w", "u", "v", "1", "=", "f", "s", "x", "0", "f", "y",
    "0", "0", "1", "×", "X", "Y", "Z", ",",
    "The skew s accounts for non-perpendicular sensor axes and is zero for",
    "every modern focal-plane array; fix s = 0 and do not estimate it.",
])

# Verbatim from that fixture page -- U+03BB and the Computer Modern big-bracket
# pieces at U+F8EE/U+F8F0, which have no Unicode mapping and arrive as PUA.
# String-level, because no synthetic PDF can carry these glyphs.
FLATTENED_MATRIX_VERBATIM = "\n".join([
    "with (cx, cy) the principal point, in homogeneous form,",
    "\u03bb", "\uf8ee", "\uf8f0", "u", "v", "1", "\uf8f9", "\uf8fb=",
    "\uf8ee", "\uf8f0", "fx", "s", "cx", "0",
    "The skew s accounts for non-perpendicular sensor axes and is zero.",
])

# The measured false-positive class: a listing's line-number gutter and a
# plot's axis ticks. Same SHAPE as the matrix above -- a column of very short
# lines -- and it must not fire. Real: cec_320 hw11, cec_315 lecture plots.
NUMERIC_GUTTER = "\n".join([
    "Listing 1 shows the branch sequence used by the solution below.",
    "5", ".", "6", ".", "7", ".", "8", ".", "9", ".", "10", ".", "11",
    "0.2", "0.4", "0.6", "0.8", "1.0", "1.2", "\u22122", "\u22121", "2",
    "The gutter above is line numbering, and the row after it is an axis.",
])

# The second measured false-positive class, and the one that decided the
# 2026-09-06 run-length sweep. Both are verbatim in shape from the corpus:
# a Wingdings list bullet that maps to ASCII `z` and lands twice per wrapped
# bullet (NASA-Systems-Engineering-Handbook-2007.pdf, 10 of 25 sampled pages in
# the min_run 3 -> 2 increment), and an assembly listing's line-number gutter
# whose `b` is the branch opcode (cec_320 lectures). Every line here is one
# `_is_symbolic` accepts -- a lone ASCII letter or a bare numeral -- and none is
# a mathematical character, which is exactly what separates them.
LONE_LETTER_COLUMN = "\n".join([
    "Several additional factors should be considered when selecting an option:",
    "z", "z", "Heritage of the product;",
    "z", "z", "Critical or noncritical application;",
    "15", "beq", "mp_letter_grade_case_f", "16", "17", "b",
    "The listing above is a branch table and the column above it is a bullet.",
])

# A flattened fraction as it actually arrives: TWO short lines, not four. This
# is the shape the run length was lowered to reach -- an integral's limits, a
# numerator over a denominator -- and it is why `_SHRED_MIN_RUN` is 2.
FLATTENED_FRACTION = "\n".join([
    "By a change of variables the convolution integral can also be written",
    "y(t) =", "Z ∞", "−∞", "x(t − τ)h(τ) dτ",
    "which shows that convolution is commutative.",
])

PLAIN_PROSE = (
    "The inside of a computer: control unit, datapath, and registers. "
    "Every instruction is fetched, decoded, executed and retired in order. "
) * 6


def test_flattened_matrix_page_is_structurally_suspect():
    """THE false negative. A page of intact prose whose displayed matrix was
    shredded into one- and two-character lines is not a healthy page."""
    sigs = textlayer.structure.signals(FLATTENED_MATRIX)
    assert textlayer.structure.classify(sigs) == textlayer.SUSPECT
    fired = [s.name for s in sigs if s.fired]
    assert fired == ["shredded-lines"]


def test_unicode_and_pua_math_glyphs_count_as_symbolic():
    """Computer Modern's big delimiters have NO Unicode mapping and arrive as
    Private-Use-Area code points -- the reader gets an unreadable box. Treating
    PUA and Greek as symbolic is what catches a flattened bracketed matrix."""
    sigs = textlayer.structure.signals(FLATTENED_MATRIX_VERBATIM)
    assert textlayer.structure.classify(sigs) == textlayer.SUSPECT
    # Both fire, and that is the point: the PUA brackets are simultaneously
    # the reason the run counts as symbolic and an unmapped glyph in their own
    # right. Two named causes on one page beats one blended score.
    assert [s.name for s in sigs if s.fired] == ["shredded-lines", "unmapped-glyphs"]


def test_prose_page_is_not_structurally_suspect():
    """Guards the false-positive direction. A detector that flags everything
    routes nothing, which is exactly as useless as one that flags nothing."""
    sigs = textlayer.structure.signals(PLAIN_PROSE)
    assert textlayer.structure.classify(sigs) == textlayer.INTACT


def test_numeric_gutter_is_not_structurally_suspect():
    """Line numbers and axis ticks have the same SHAPE as a flattened matrix.
    Only the symbolic-content test separates them, and without it the detector
    fired on 97 documents, mostly wrong."""
    sigs = textlayer.structure.signals(NUMERIC_GUTTER)
    assert textlayer.structure.classify(sigs) == textlayer.INTACT


def test_two_line_flattened_fraction_is_suspect():
    """The recall gap this run length was lowered to close. A flattened
    fraction or an integral's limits make TWO short lines, not four, and the
    ground-truth sample measured the detector missing displayed mathematics on
    six unflagged pages in seven. `_SHRED_MIN_RUN = 2` is what reaches them;
    guard it, because 4 was the shipped value for a release."""
    sigs = textlayer.structure.signals(FLATTENED_FRACTION)
    assert textlayer.structure.classify(sigs) == textlayer.SUSPECT
    assert [s.name for s in sigs if s.fired] == ["shredded-lines"]


def test_lone_letter_column_is_not_structurally_suspect():
    """What PAYS for the run length above, and the direction that matters.
    A Wingdings bullet that maps to `z`, and an assembly gutter whose `b` is a
    branch opcode, are both columns of short lines that `_is_symbolic` accepts
    as lone variables. Without the strong-symbolic rule, lowering the run
    length to 2 takes strict precision from 85% to 59%; with it, precision
    RISES to 93%. If this test ever fails, that trade has been undone."""
    sigs = textlayer.structure.signals(LONE_LETTER_COLUMN)
    assert textlayer.structure.classify(sigs) == textlayer.INTACT


def test_a_bare_equals_line_is_not_strong_enough_on_its_own():
    """Measured as a third tier and rejected: admitting a bare `=` line as
    mathematical costs 8 points of strict precision (93.1% -> 85.4%) for two
    estimated true positives, because a C operator-precedence table is a
    column of `14` / `=` / `13` / `? :`."""
    operator_table = "\n".join([
        "The table below reproduces C's operator precedence for reference.",
        "13", "? :", "Ternary conditional", "14", "=", "Simple assignment",
        "Both columns above are a precedence table, not an equation.",
    ])
    sigs = textlayer.structure.signals(operator_table)
    assert textlayer.structure.classify(sigs) == textlayer.INTACT


def test_suspect_page_is_not_routed_to_ocr(tmp_path):
    """The two axes have DIFFERENT repairs. A suspect page's glyphs are already
    in the file with correct coordinates; sending it to a model would spend GPU
    recovering what is present and return a worse answer."""
    pdf = _make_pdf(tmp_path / "flat.pdf", [FLATTENED_MATRIX + PLAIN_PROSE])
    page = textlayer.extract(pdf).pages[0]
    assert page.suspect
    assert not page.needs_ocr


def test_structural_suspicion_does_not_change_the_density_verdict(tmp_path):
    """The new axis is additive. `verdict`, `ocr_pages` and `needs_ocr` are
    consumed by pdfops, by cli.py and by an external caller in
    content/cesc_470/md_notes/README.md, and must not shift."""
    pdf = _make_pdf(tmp_path / "flat.pdf", [FLATTENED_MATRIX + PLAIN_PROSE])
    doc = textlayer.extract(pdf)
    assert doc.pages[0].verdict == "ok"
    assert doc.verdict == "text-layer-sufficient"
    assert doc.ocr_pages == []
    assert doc.suspect_pages == [1]


def test_every_page_carries_every_signal(tmp_path):
    """Evidence, not a boolean. A silent detector and an absent one differ, so
    a clean page still reports the full roll-call and every detector's name."""
    pdf = _make_pdf(tmp_path / "clean.pdf", [PLAIN_PROSE])
    page = textlayer.extract(pdf).pages[0]
    assert [s.name for s in page.signals] == list(textlayer.structure.NAMES)
    assert not any(s.fired for s in page.signals)
    assert page.fired == ()


def test_suspect_signal_carries_checkable_evidence(tmp_path):
    """A verdict a reader cannot check is a verdict they have to trust."""
    pdf = _make_pdf(tmp_path / "flat.pdf", [FLATTENED_MATRIX + PLAIN_PROSE])
    page = textlayer.extract(pdf).pages[0]
    detail = next(s.detail for s in page.signals if s.fired)
    assert "fragments" in detail
    assert "u / v" in detail        # the evidence itself, not a restatement


def test_document_structure_verdict_bands_none_some_all(tmp_path):
    """A document 21% suspect is not one suspect throughout, and the two must
    not read the same. Mirrors the density verdict's none/some/all banding."""
    flat = FLATTENED_MATRIX + PLAIN_PROSE
    clean = _make_pdf(tmp_path / "a.pdf", [PLAIN_PROSE, PLAIN_PROSE])
    some = _make_pdf(tmp_path / "b.pdf", [PLAIN_PROSE, flat])
    every = _make_pdf(tmp_path / "c.pdf", [flat, flat])
    assert textlayer.extract(clean).structure_verdict == "structure-intact"
    assert textlayer.extract(some).structure_verdict == "structure-suspect-partial"
    assert textlayer.extract(every).structure_verdict == "structure-suspect"


def test_letter_spacing_is_a_structural_signal():
    """It fired on real documents already and fed NOTHING -- a footnote wired
    to no verdict and no page. That orphan is what the axis absorbs."""
    sigs = textlayer.structure.signals("C o m p u t e r  O r g a n i z a t i o n")
    assert textlayer.structure.classify(sigs) == textlayer.SUSPECT
    assert [s.name for s in sigs if s.fired] == ["letter-spaced"]


def test_letter_spacing_ignores_a_column_of_tick_labels():
    """`\\s` matches a newline, so a plot's ticks extracted one per line scored
    as a corrupt text layer: 46 of 51 flagged documents fired on nothing else.
    Letter-spacing is a HORIZONTAL artefact by definition."""
    assert not textlayer.is_letter_spaced("1\n2\n3\n4\n5\n6\n7\n8\n")
    assert not textlayer.is_letter_spaced("a\nb\nc\nd\ne\nf\ng\nh\n")


def test_signal_counts_lists_silent_detectors_too(tmp_path):
    pdf = _make_pdf(tmp_path / "flat.pdf", [FLATTENED_MATRIX + PLAIN_PROSE])
    counts = textlayer.extract(pdf).signal_counts
    assert counts == {
        "letter-spaced": 0,
        "shredded-lines": 1,
        "vertical-letter-spaced": 0,
        "unmapped-glyphs": 0,
    }


def test_markdown_warns_that_ocr_is_not_the_repair(tmp_path):
    """A transcript whose equations are rubble must say so, and must not send
    the reader to the expensive tool that cannot help."""
    pdf = _make_pdf(tmp_path / "flat.pdf", [FLATTENED_MATRIX + PLAIN_PROSE])
    md = textlayer.to_markdown(textlayer.extract(pdf))
    assert "structure-suspect" in md
    assert "shredded-lines" in md
    assert "OCR is not the repair" in md


def test_cli_inspect_reports_the_structural_axis(tmp_path):
    from typer.testing import CliRunner
    from ocr_handler.cli import app

    pdf = _make_pdf(tmp_path / "flat.pdf", [FLATTENED_MATRIX + PLAIN_PROSE])
    result = CliRunner().invoke(app, ["inspect", str(pdf)])
    assert result.exit_code == 0
    assert "text-layer-sufficient" in result.stdout      # density unchanged
    assert "structure-suspect" in result.stdout
    assert "OCR is NOT the repair" in result.stdout


def test_cli_inspect_stays_quiet_on_a_clean_document(tmp_path):
    """The 214 text-layer-sufficient documents must not gain a warning line."""
    from typer.testing import CliRunner
    from ocr_handler.cli import app

    pdf = _make_pdf(tmp_path / "clean.pdf", [PLAIN_PROSE])
    result = CliRunner().invoke(app, ["inspect", str(pdf)])
    assert result.exit_code == 0
    assert "structure" not in result.stdout


# --------------------------------------------------------------------------
# Detector 3 -- VERTICAL letter spacing. The gap the horizontal detector left
# behind when its `\s` was tightened to `[^\S\n]` to stop a plot's tick labels
# scoring as corruption (51 documents -> 3, a 17x overcount). Widening the
# regex back is not the repair; telling a word from a label is.
# Design: docs/findings/recall-was-a-symbol-test-not-a-run-length.md § 5
# --------------------------------------------------------------------------

# Verbatim from the arrows of figure 6.4-4, NASA-Systems-Engineering-Handbook
# -2007.pdf page 160: each glyph is rotated separately, so reading-order
# extraction returns one letter per LINE.
ROTATED_LABEL = "Continuous risk management\nC\no\nn\nt\nr\no\nl\nIdentify the risk"

# The measured false-positive classes, same SHAPE, all real: a plot's axis
# ticks, a table's lettered row labels (sys_304, 7 pages), an all-caps matrix
# header (NASA page 72), and a flattened variable name (sys_304 fuzzy sets).
VERTICAL_LABELS = [
    "0\n1\n2\n3\n4\n5\n6\n7\n",             # axis ticks -- digits, never letters
    "a\nb\nc\nd\ne\nf\ng\nh\n",             # lettered row labels: an A-Z run
    "A\nB\nC\nD\nE\nF\nG\nH\n",             # the same, capitalised
    "M\nM\nM\nM\nE\nE\nE\nE\n",             # a matrix header block
    "N\nk\nB\nA\nR\nk\nk\nk\n",             # a flattened variable name
    "a\nb\nn\nn\ns\ns\n",                   # optics subscripts n_a n_b s s'
]


def test_vertical_letter_spacing_is_a_structural_signal():
    """`C\\no\\nn\\nt\\nr\\no\\nl` -- a rotated figure label extracted
    downwards. Named in the plan as the cost of fixing the horizontal
    detector, and left open until a word could be told from a tick.

    It used to co-fire with `shredded-lines` on every page, and was described
    as adding naming rather than recall. That is no longer true, and the change
    that made it untrue is the 2026-09-06 strong-symbolic rule: a column of
    lone ASCII letters carries no mathematical character, so `shredded-lines`
    now correctly declines it. Measured over 459 documents / 7,198 pages, all
    FOUR of this detector's pages are now pages it is the only signal on --
    it went from a strict subset of `shredded-lines` to independent evidence.
    This test asserts that, because if `shredded-lines` ever reclaims these
    pages it means the lone-letter escape has come back."""
    sigs = textlayer.structure.signals(ROTATED_LABEL)
    assert textlayer.structure.classify(sigs) == textlayer.SUSPECT
    assert [s.name for s in sigs if s.fired] == ["vertical-letter-spaced"]


def test_vertical_letter_spacing_ignores_labels_that_are_not_words():
    """The direction that matters. Each of these is a real page in the corpus
    and none of them is a shredded word; a detector that flagged them would be
    the `\\s`-matches-newline bug wearing a new name."""
    for label in VERTICAL_LABELS:
        fired = [x.name for x in textlayer.structure.signals(label) if x.fired]
        assert "vertical-letter-spaced" not in fired, label


def test_vertical_detection_does_not_widen_the_horizontal_regex():
    """`is_letter_spaced` is public API with three callers and its own
    regressions. The vertical case is a SEPARATE detector precisely so that
    pattern stays exactly as tight as it was measured to need to be."""
    assert not textlayer.is_letter_spaced(ROTATED_LABEL)
    assert textlayer.is_letter_spaced("C o m p u t e r  O r g a n i z a t i o n")


def test_vertical_signal_carries_the_reassembled_word():
    """Evidence a reader can check: the run AND what it spells."""
    detail = next(s.detail for s in textlayer.structure.signals(ROTATED_LABEL)
                  if s.name == "vertical-letter-spaced")
    assert "Control" in detail


# --------------------------------------------------------------------------
# Detector 4 -- UNMAPPED GLYPHS. Code points the extractor could not map to
# Unicode, so the reader gets an empty box. Deferred by the plan pending a
# benign list; the list is three code points, built by frequency census plus
# rendering each candidate's bbox.
# --------------------------------------------------------------------------

# Verbatim from cec_320/lectures/mp-he-lctr25 page 2: Computer Modern's
# \left\{ arrives as its three construction pieces, so the `cases` environment
# reaches the reader as a column of boxes.
CASES_BRACE = (
    "We define the ReLU activation function as\n"
    "a(x) =\n"
    "\uf8f1\uf8f4\uf8f4\uf8f2\n"
    "\uf8f4\uf8f4\uf8f4\uf8f3\n"
    "0, x is negative, x, otherwise. Implement it in assembly below.\n"
)

# The reason the detector was NOT shipped with the plan: the corpus's single
# commonest unmapped code point is an ordinary PowerPoint bullet, 1,514 times.
SYMBOL_BULLETS = "\n".join(
    f"\uf0b7 Requirements are allocated to the next level of the architecture "
    f"and verified against item {n} of the specification." for n in range(1, 9)
)


def test_unmapped_big_delimiter_is_a_structural_signal():
    """U+F8F1..U+F8F4 are Computer Modern's `\\left\\{` pieces. A `cases`
    brace that reaches the reader as boxes is not a faithful rendering."""
    sigs = textlayer.structure.signals(CASES_BRACE)
    assert textlayer.structure.classify(sigs) == textlayer.SUSPECT
    assert "unmapped-glyphs" in [s.name for s in sigs if s.fired]


def test_symbol_font_bullets_are_benign():
    """1,514 occurrences on 164 pages of one guidebook, and nothing is wrong:
    the line break already says 'list item'. This page fires nothing."""
    sigs = textlayer.structure.signals(SYMBOL_BULLETS)
    assert textlayer.structure.classify(sigs) == textlayer.INTACT


def test_measured_bullets_are_benign_and_the_mathematics_is_not():
    """A benign list is a decision, not a detail: every entry silences real
    pages. These three are the Office dingbat block's whole corpus volume;
    the fourth-ranked code point is already mathematics."""
    for bullet in ("\uf0b7", "\uf070", "\uf06c"):
        assert not textlayer.structure.unmapped_glyphs(f"item {bullet} item")
    for glyph in ("\uf8f4", "\uf074", "\u0001"):
        assert textlayer.structure.unmapped_glyphs(f"item {glyph} item")


def test_cmex_brace_code_points_stay_off_the_benign_list():
    """U+0007 and U+0008 are invisible tab leaders in two SE handbooks -- and
    in CMEX10's own encoding they are `\\rceil` and `\\{`. Suppressing them to
    quiet 21 pages would blind the detector to the brace it exists to catch."""
    assert textlayer.structure.unmapped_glyphs("y = \u0008x + 1\u0007")


def test_unmapped_evidence_names_the_code_point():
    """A verdict a reader cannot check is one they have to trust. The detail
    carries the code point so it can be looked up, and the text around it."""
    detail = next(s.detail for s in textlayer.structure.signals(CASES_BRACE)
                  if s.name == "unmapped-glyphs")
    assert "U+F8F1" in detail
    assert "a(x)" in detail


def test_prose_fires_none_of_the_four_detectors():
    """Four detectors is four chances to flag a clean page. The 6,409 pages
    the corpus pass leaves alone are the ones that make the other 778 mean
    something."""
    sigs = textlayer.structure.signals(PLAIN_PROSE)
    assert len(sigs) == 4
    assert textlayer.structure.classify(sigs) == textlayer.INTACT


def test_a_glyph_the_benign_list_calls_decorative_is_not_evidence_of_mathematics():
    """`_is_strong` and `unmapped_glyphs` must not contradict each other.

    U+F0B7 / U+F070 / U+F06C are Office bullets. `unmapped_glyphs` declares them
    benign (1,514 + 1,016 + 366 occurrences corpus-wide); they also fall inside
    `_SYMBOLIC_RANGES`, so before 2026-09-06 `_is_strong` counted the same glyph
    as proof of mathematics. One detector cannot call a glyph a bullet while
    another calls it an integral sign.
    """
    from ocr_handler import structure

    for code in structure._BENIGN_GLYPHS:
        assert not structure._is_strong(chr(code)), (
            f"U+{code:04X} is on the benign list but counts as strong")

    # The real Computer Modern brace pieces must still count -- this guard must
    # not become "ignore the whole Private Use Area".
    assert structure._is_strong("\uf8f1"), "CM \\left\\{ piece must stay strong"


def test_a_run_of_office_bullets_alone_does_not_fire_shredded_lines():
    """The corpus effect of the guard above: 732 -> 729 pages, all three of the
    removed ones non-mathematical (two PowerPoint outlines, one SE guidebook)."""
    from ocr_handler import structure

    bullets = "\n".join("\uf0b7" for _ in range(6))
    fired = [s.name for s in structure.signals(bullets) if s.fired]
    assert "shredded-lines" not in fired, f"bullets alone fired: {fired}"
