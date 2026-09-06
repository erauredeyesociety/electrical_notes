"""Regression floor for the equation-reading validity axis.

The load-bearing fact this module exists for: **compile-checking is not a weak
signal, it is no signal.** 83 of 84 recorded UniMERNet outputs compiled under
tectonic, including 1,113 tokens of array garbage read off a whole page. Every
string in `_DEGENERATE` below would typeset without complaint.

Design and the sweeps behind every constant:
docs/plans/latex-repair-and-validity.md § 3.

Self-contained: the strings are abridged transcriptions of the outputs recorded
in `tmp/eqocr/sweep.json` (gitignored), so these run on a clean checkout.
"""

from __future__ import annotations

import json

from ocr_handler import validity
from ocr_handler.structure import Signal
from ocr_handler.validity import PLAUSIBLE, SUSPECT, classify, signals

# Real UniMERNet readings of the fixture equation, at paddings that did not
# reach the neighbouring line. All four are correct.
GOOD = [
    r"= 1 \times 1 ^ { n } ( \cos ( \omega _ { 0 } n ) + j \sin ( \omega _ { 0 } n ) ) .",
    r"= 1 \alpha \vert ^ { n } ( \cos ( w _ { 0 } h ) + j \sin ( w _ { 0 } h ) ) .",
    r"H ( e ^ { j \omega } ) = \sum _ { n = - \infty } ^ { \infty } h [ n ] e ^ { - j \omega n }",
    r"\bar { x } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } x _ { i }",
]

# Known-good coursework LaTeX, typed by hand, compact rather than spaced.
COURSEWORK = [
    r"x_a(t) = 10\sin(\omega t + \pi/12)",
    r"\mathbf{X}_a = 10\angle(-75^\circ)",
    r"y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k]",
    r"\frac{\omega_0}{2\pi} = \frac{\pi/\sqrt{8}}{2\pi} = \frac{1}{2\sqrt{8}}",
    r"\text{CPU time} = \text{IC} \times \text{CPI} \times \text{cycle time}",
    r"S = \frac{1}{(1-f) + f/s}",
]


def _fired(text, crop=None):
    return {s.name for s in signals(text, crop=crop) if s.fired}


# --------------------------------------------------------------------------
# The contract: evidence, not a boolean. Same as structure.py.
# --------------------------------------------------------------------------

def test_every_reading_carries_every_signal():
    for text in GOOD + COURSEWORK:
        got = signals(text)
        assert [s.name for s in got] == list(validity.NAMES)
        assert all(isinstance(s, Signal) for s in got)


def test_a_silent_detector_and_an_absent_one_differ():
    """A detector that could not run says so instead of reporting `clean`."""
    without = {s.name: s for s in signals(GOOD[0])}["length-vs-crop"]
    assert not without.fired and "no crop" in without.detail
    with_crop = {s.name: s for s in signals(GOOD[0], crop=(720, 130))}["length-vs-crop"]
    assert not with_crop.fired and with_crop.detail == ""


def test_a_fired_signal_carries_checkable_evidence():
    for s in signals(r"\cosh " * 40):
        if s.fired:
            assert s.detail, f"{s.name} fired with no evidence"


def test_classify_is_an_or_never_an_average():
    assert classify(signals(GOOD[0], crop=(720, 130))) == PLAUSIBLE
    one = (Signal("a", False, ""), Signal("b", True, "x"))
    assert classify(one) == SUSPECT
    assert classify((Signal("a", False, ""),)) == PLAUSIBLE


def test_every_detector_explains_itself():
    assert set(validity.WHY) == set(validity.NAMES)
    assert all(validity.WHY[n] for n in validity.NAMES)


# --------------------------------------------------------------------------
# The direction that matters most: not flagging good readings.
# --------------------------------------------------------------------------

def test_good_model_readings_are_plausible():
    for text in GOOD:
        assert classify(signals(text)) == PLAUSIBLE, text


def test_known_good_coursework_latex_is_plausible():
    for text in COURSEWORK:
        assert classify(signals(text)) == PLAUSIBLE, text


def test_an_array_column_spec_is_not_a_repeat_loop():
    """`\\begin{array} { l l l l }` is four identical tokens and a normal matrix.

    Every one of the 6 corpus rows the raw run test flagged was a column spec.
    """
    matrix = (r"\begin{array} { c c c c } 1 & 2 & 3 & 4 \\ "
              r"5 & 6 & 7 & 8 \end{array}")
    assert "repeat-loop" not in _fired(matrix)


def test_a_decimal_expansion_is_not_a_repeat_loop():
    """`0.3888888889` is eight identical digits and the correct answer.

    Digits get their own, higher bar -- the same move `structure.py` makes
    when it refuses to call a bare numeral symbolic.
    """
    assert "repeat-loop" not in _fired(r"0.3888888889 = 7/18")
    assert "repeat-loop" not in _fired(r"\IC = 1{,}000{,}000")


def test_a_long_repetitive_but_correct_derivation_is_plausible():
    partial = (r"X(z) = \frac{3(1 - 0.8 z^{-1})}{(1 - 0.4 z^{-1})(1 - 0.8 z^{-1})}"
               r" + \frac{2}{1 - 0.4 z^{-1}}")
    assert classify(signals(partial)) == PLAUSIBLE


# --------------------------------------------------------------------------
# The direction it was built for.
# --------------------------------------------------------------------------

def test_compilable_garbage_is_still_suspect():
    """The headline. This typesets; it is also a decoder loop."""
    loop = (r"\begin{array} { r l } { \Lambda ^ { 2 } } & { = \sinh "
            + r"\cosh " * 8 + r"} \end{array}")
    fired = _fired(loop, crop=(1700, 2200))
    assert fired, "a string a compiler accepts can still be nonsense"
    assert "repeat-loop" in fired


def test_a_decoder_loop_is_caught_by_the_token_run():
    assert "repeat-loop" in _fired(r"x = " + r"\alpha " * 6)


def test_the_blank_paper_hallucination_is_caught():
    """`patho/blank_paper_pad96` -- an empty patch of paper.

    It returned a confident, well-formed, compilable invention, and the
    research doc records that nothing caught it. The repeated-digit run does:
    thirteen consecutive `1`s against a coursework maximum of eight.
    """
    invented = r"\textstyle { \frac { 1 } { 1 1 1 0 \times 1 1 1 1 1 1 1 1 1 1 1 1 1 } }"
    assert "repeat-loop" in _fired(invented)


def test_nothing_was_read():
    assert "empty-reading" in _fired("-")
    assert "empty-reading" in _fired(r"\mp")
    assert "empty-reading" in _fired("")


# `crop_expo_base` read as `formula`, PaddleOCR-VL over a 500x160 crop of the
# un-annotated twin -- tmp/eval/out_crops/results.json, verbatim. Nested empty
# `aligned` environments and nothing else.
CONTENT_FREE = r"\[\begin{aligned}\begin{aligned}\\ &\end{aligned}\\ \end{aligned}\]"
CONTENT_FREE_CROP = (500, 160)


def test_scaffolding_with_nothing_inside_it_is_suspect():
    """The reading seven detectors called `plausible`, and why each was right.

    45 tokens (the tokenisation spends nine on `{aligned}` alone), so
    `empty-reading`'s 5-token floor is far away; variety 0.333 against 0.20;
    no token run of 4; braces, delimiters and environments all balanced;
    14.4 tokens per line-width against a limit of 18. Every one of those is
    correct and the set is collectively wrong, which is why this is an eighth
    detector and not a threshold nudge.
    """
    fired = _fired(CONTENT_FREE, crop=CONTENT_FREE_CROP)
    assert fired == {"content-free"}, "the other seven must stay right"
    assert classify(signals(CONTENT_FREE, crop=CONTENT_FREE_CROP)) == SUSPECT


def test_the_gap_is_not_reachable_by_lowering_the_length_limit():
    """`length-vs-crop` is the wrong axis for it, and the numbers say so.

    14.4 per line-width is ABOVE the highest recorded good reading (13.7,
    `expo/pad+96`), so a limit of 14 would catch this one -- with the margin
    cut from ±4 to 0.35. It also needs a crop, and the same content-free
    string off a wider crop passes at any limit.
    """
    wide = _fired(CONTENT_FREE, crop=(1000, 160))
    assert "length-vs-crop" not in wide, "45 tokens over 6.25 line-widths is 7.2"
    assert "content-free" in wide, "and the content count does not care"


def test_a_short_genuine_equation_is_not_content_free():
    """`x = 1` is a legitimate reading and is exactly three content tokens.

    That is what pins the floor at 3. The environment-wrapped forms matter
    just as much: a model that wraps three real tokens in `aligned` has still
    read something, which is why this detector counts content and does NOT
    take a ratio against the total.
    """
    for text in ("x = 1", r"\[x=1\]", r"\[\begin{aligned}x &= 1\end{aligned}\]",
                 r"\Omega = \omega T", r"\frac{1}{2}", r"\left( x \right)"):
        assert "content-free" not in _fired(text), text


def test_content_free_is_quiet_on_every_good_reading():
    for text in GOOD + COURSEWORK:
        assert "content-free" not in _fired(text), text


def test_content_tokens_keeps_the_mathematics_and_drops_the_layout():
    """The definition the floor of 3 is measured against.

    Font selectors are deliberately NOT scaffolding -- they wrap content that
    is already counted, and dropping them would narrow the margin for nothing.
    """
    assert validity.content_tokens(CONTENT_FREE) == []
    assert validity.content_tokens(r"\begin{array} { l l } a & b \end{array}") == ["a", "b"]
    assert validity.content_tokens(r"\left( \frac{1}{2} \right)") == \
        ["(", r"\frac", "1", "2", ")"]
    assert r"\mathrm" in validity.content_tokens(r"\mathrm{d}x")


def test_a_whole_page_read_into_one_equation_crop_is_suspect():
    """1,113 tokens off a 1700x2200 page crop is absurd on its face.

    A bare token cap cannot say so -- long correct equations and short looping
    ones overlap. The crop is what separates them: an equation crop is one
    line, so `width / height` is how many glyph-heights fit across it.
    """
    long_read = " ".join([r"\frac { a } { b } +"] * 60)
    assert "length-vs-crop" in _fired(long_read, crop=(1700, 2200))
    assert "length-vs-crop" not in _fired(GOOD[0], crop=(720, 130))


def test_low_variety_needs_length_too():
    """`x = y` is three types over three tokens and perfectly fine."""
    assert "token-variety" not in _fired("x = y")
    degenerate = " ".join([r"\sinh \left ( \frac { 2 } { \pi } \right )"] * 12)
    assert "token-variety" in _fired(degenerate)


# --------------------------------------------------------------------------
# Structural counts, reported BEFORE repair.
# --------------------------------------------------------------------------

def test_structural_counts_are_reported_not_silently_fixed():
    """A string needing heavy repair is itself evidence about the reading."""
    broken = r"\left( \frac{1}{2}"
    fired = {s.name: s.detail for s in signals(broken) if s.fired}
    assert "unmatched-delimiters" in fired
    assert r"\left" in fired["unmatched-delimiters"]

    from ocr_handler.latex_repair import repair
    assert repair(broken).text != broken, "repair still happens, afterwards"


def test_brace_and_environment_mismatch_are_separate_signals():
    assert "unbalanced-braces" in _fired(r"\frac{1}{2")
    assert "unmatched-environments" in _fired(r"\begin{cases} x = 1")
    assert "unbalanced-braces" not in _fired(r"\begin{cases} x = 1 \end{cases}")


def test_structural_signals_are_quiet_on_the_recorded_corpus():
    """Measured: 0 of 44 raw model outputs and 0 of 2,967 corpus display rows.

    UniMERNet emits balanced LaTeX. That silence is the same fact that kills
    compile-checking, and it is why these three are kept as tripwires rather
    than promoted.
    """
    structural = {"unbalanced-braces", "unmatched-delimiters", "unmatched-environments"}
    for text in GOOD + COURSEWORK:
        assert not (_fired(text) & structural), text


# --------------------------------------------------------------------------
# Tokenisation and the borrowed constants.
# --------------------------------------------------------------------------

def test_the_token_stream_is_spacing_invariant():
    """The reason for changing the research doc's tokenisation.

    UniMERNet puts a space between every token and a human puts almost none.
    Counting spaces makes the same expression score twice as varied when a
    human typed it, and then no threshold is comparable across corpora.
    """
    spaced = r"\frac { 1 } { 2 }"
    compact = r"\frac{1}{2}"
    assert validity.tokens(spaced) == validity.tokens(compact)
    assert validity.variety_ratio(spaced) == validity.variety_ratio(compact)


def test_a_control_word_and_an_escape_are_each_one_token():
    assert validity.tokens(r"\alpha\{x\\") == [r"\alpha", r"\{", "x", "\\\\"]


def test_tail_repeat_follows_the_documented_scaling():
    """surya/chandra: a 1-character loop needs >16 repeats, a 100-char one >4."""
    prefix = "the quick brown fox " * 3
    assert validity.tail_repeat(prefix + "a" * 17) is not None
    assert validity.tail_repeat(prefix + "a" * 16) is None
    unit = "".join(f"{i:02d}" for i in range(50))     # 100 chars, aperiodic
    assert len(unit) == 100
    assert validity.tail_repeat("x" + unit * 5) is not None
    assert validity.tail_repeat("x" + unit * 4) is None
    assert validity.tail_repeat("the quick brown fox jumps over the lazy dog") is None


def test_tail_repeat_misses_this_models_loops_and_the_token_run_does_not():
    """UniMERNet closes the array after looping, so the tail looks clean.

    Recorded: `patho/whole_page` ends `\\cosh \\cosh \\cosh \\cosh \\cosh
    \\cosh } \\right) } \\end{array} }` -- the loop is six tokens back, and
    surya's tail-anchored check fires on 0 of the 10 recorded pathologies.
    """
    tail_clean = r"a " + r"\cosh " * 6 + r"} \right) } \end{array} }"
    assert validity.tail_repeat(tail_clean) is None
    assert validity.token_run(tail_clean) is not None


# --------------------------------------------------------------------------
# The CLI surface -- `ocr-handler check`. It is the deliverable; until it
# existed neither module was reachable by a user, which
# docs/plans/doctrine-compliance.md flags as an integrity item ("an untested
# CLI"). These test the REPORT, not the detectors: what a reader is shown, and
# what the tool refuses to do to their text without being asked.
#
# Every string below is a verbatim transcription of a recorded model output --
# the crop sweep in `tmp/eqocr/sweep.json` (UniMERNet) and
# `tmp/eval/out_crops/results.json` (PaddleOCR-VL). Both are gitignored, so
# they are copied here rather than read, per the testing directive: a fixture
# that is not in the repository is not a fixture.
# --------------------------------------------------------------------------

# `expo/pad+160`, 780x480 px: the crop was over-padded until it swallowed the
# neighbouring line, and the reading went with it. 38 tokens over 780/480 =
# 1.6 line-widths is 23.4, past the limit of 18.
OVERPADDED = (r"( { \ e \sp \prime \cos \theta } ) \sp n = \frac { \frac { 1 } "
              r"{ 2 } } { e \sp { \frac { 1 } { 2 } \sin \theta } }")
OVERPADDED_CROP = (780, 480)

# `patho/blank_paper_pad96`, 912x322 px: blank paper, read confidently. The
# research doc records this one as caught by nothing.
BLANK_PAPER = r"\textstyle { \frac { 1 } { 1 1 1 0 \times 1 1 1 1 1 1 1 1 1 1 1 1 1 } }"

# `crop_eqline_base` / `smoke_eqline_base`, 720x130 px: a correct reading of an
# un-annotated crop, where `\qquad` marks each blank `ink.py` left. Repair
# spaces the run apart and must SAY that it did.
QQUAD_READING = r"\[=|\alpha|^{n}(\qquad\qquad+j\qquad).\]"

# `crop_expo_ann`, 500x160 px: a correct reading needing no repair at all.
CLEAN_READING = r"\[(e^{j\omega_{0}})^{n}=e^{j\omega_{0}n}\]"


def _run(*args, stdin: str | None = None):
    from typer.testing import CliRunner
    from ocr_handler.cli import app
    return CliRunner().invoke(app, ["check", *args], input=stdin)


def test_cli_check_reports_the_whole_roll_call_for_one_reading():
    """One `Signal` per detector, fired or not -- the contract, on screen.

    A report that lists only what fired cannot be checked for what it failed
    to look at, which is the same reason `structure.py` returns a full
    roll-call instead of a boolean.
    """
    result = _run("-", "--crop", "780x480", stdin=OVERPADDED)
    assert result.exit_code == 0
    for name in validity.NAMES:
        assert name in result.stdout, name


def test_cli_check_says_when_a_detector_could_not_run(tmp_path):
    """`length-vs-crop` is the measured winner (8/10, 0 false positives).

    Without a crop it cannot run, and a roll-call that renders "did not run"
    and "ran and passed" identically is lying about its own coverage.
    """
    eq = tmp_path / "reading.tex"
    eq.write_text(CLEAN_READING, encoding="utf-8")
    assert "not evaluated" in _run(str(eq)).stdout
    assert "not evaluated" not in _run(str(eq), "--crop", "500x160").stdout


def test_cli_check_flags_an_overpadded_crop_as_suspect(tmp_path):
    eq = tmp_path / "reading.tex"
    eq.write_text(OVERPADDED, encoding="utf-8")
    out = _run(str(eq), "--crop", "780x480").stdout
    assert "readings-suspect" in out
    assert "length-vs-crop" in out
    assert "per line-width" in out, "the evidence, not just the verdict"


def test_cli_check_never_rewrites_the_input(tmp_path):
    """Report, let the reader decide -- the rule structural-faithfulness.md
    holds for a suspect page, held here for a suspect reading.

    `--repair` is opt-in and writes to stdout; nothing on disk is touched in
    either direction. The blacklist entry is permanent: silently repairing
    extracted text is out of scope.
    """
    eq = tmp_path / "reading.tex"
    eq.write_text(QQUAD_READING, encoding="utf-8")
    out = _run(str(eq)).stdout
    assert "not applied" in out
    assert eq.read_text(encoding="utf-8") == QQUAD_READING
    _run(str(eq), "--repair")
    assert eq.read_text(encoding="utf-8") == QQUAD_READING


def test_cli_check_names_the_rule_behind_every_change_it_shows(tmp_path):
    """A repair a reader cannot trace to a rule is one they must trust.

    Regression: `repair()` spaced `\\qquad` runs apart and returned an empty
    `notes` tuple, so this reading changed with nothing on the roll-call to
    explain it. Found by running the CLI over the recorded PaddleOCR-VL crop
    outputs in `tmp/eval/out_crops/`.
    """
    eq = tmp_path / "reading.tex"
    eq.write_text(QQUAD_READING, encoding="utf-8")
    out = _run(str(eq)).stdout
    assert "qquad" in out, "the rule that fired must be named"
    assert "->" in out, "and the changed span shown"
    assert "no rule named" not in out


def test_cli_check_is_quiet_about_repair_when_nothing_changed(tmp_path):
    eq = tmp_path / "reading.tex"
    eq.write_text(CLEAN_READING, encoding="utf-8")
    out = _run(str(eq), "--crop", "500x160").stdout
    assert "repair: no change" in out
    assert "would change" not in out


def test_cli_check_repair_writes_latex_to_stdout_and_the_report_to_stderr(tmp_path):
    """So `check x.tex --repair > fixed.tex` still tells the reader what
    happened, instead of losing it into a terminal nobody reads again."""
    eq = tmp_path / "reading.tex"
    eq.write_text(QQUAD_READING, encoding="utf-8")
    result = _run(str(eq), "--repair")
    assert result.exit_code == 0
    assert result.stdout.strip() == r"\[=|\alpha|^{n}(\qquad \qquad +j\qquad ).\]"
    assert "verdict:" in result.stderr


def test_cli_check_repair_carries_the_suspicion_into_its_output(tmp_path):
    """Repaired garbage is still garbage. The warning travels with the text as
    a `%` comment, so the emitted stream is still LaTeX and the next reader
    cannot lose the fact that a detector fired."""
    eq = tmp_path / "reading.tex"
    eq.write_text(BLANK_PAPER, encoding="utf-8")
    out = _run(str(eq), "--crop", "912x322", "--repair").stdout
    assert out.lstrip().startswith("%")
    assert SUSPECT in out
    assert "repeat-loop" in out


def test_cli_check_reads_both_recorded_harness_shapes(tmp_path):
    """`tmp/eval/*/results.json` writes {name, size, text}; `tmp/eqocr/
    sweep.json` writes {case, w, h, raw}. One tool reads both -- disagreeing
    per-caller formats are the divergence this project exists to end."""
    paddle = tmp_path / "results.json"
    paddle.write_text(json.dumps({"results": [
        {"name": "crop_expo_over", "task": "formula",
         "size": list(OVERPADDED_CROP), "text": OVERPADDED}]}), encoding="utf-8")
    unimernet = tmp_path / "sweep.json"
    unimernet.write_text(json.dumps({"results": [
        {"case": "expo/pad+160", "w": OVERPADDED_CROP[0], "h": OVERPADDED_CROP[1],
         "raw": OVERPADDED}]}), encoding="utf-8")

    for path, label in ((paddle, "crop_expo_over[formula]"), (unimernet, "expo/pad+160")):
        out = _run(str(path)).stdout
        assert label in out, path.name
        assert "length-vs-crop" in out, "each shape must yield its crop size"


def test_cli_check_refuses_to_override_the_crop_sizes_in_a_results_json(tmp_path):
    """One `--crop` cannot be true of every record, and a silently wrong crop
    poisons the one detector that needs more than the string."""
    path = tmp_path / "results.json"
    path.write_text(json.dumps({"results": [
        {"name": "a", "size": [720, 130], "text": CLEAN_READING},
        {"name": "b", "size": [500, 160], "text": CLEAN_READING}]}), encoding="utf-8")
    assert _run(str(path), "--crop", "720x130").exit_code != 0


def test_cli_check_no_longer_calls_a_content_free_reading_plausible(tmp_path):
    """The defect the CLI itself found, closed on the surface that found it.

    `check tmp/eval/out_crops/crop_expo_base.formula.txt` reported
    `readings-plausible` on 45 tokens of nested empty `aligned`. That is the
    same failure family as the `textlayer.py` defect this project was built
    around: a page whose prose is intact and whose mathematics is gone,
    scoring `ok`.
    """
    eq = tmp_path / "reading.tex"
    eq.write_text(CONTENT_FREE, encoding="utf-8")
    out = _run(str(eq)).stdout
    assert "readings-suspect" in out
    assert "content-free" in out
    assert "0 content token(s) in 45" in out, "the evidence, not just the verdict"


def test_cli_check_rejects_a_malformed_crop(tmp_path):
    eq = tmp_path / "reading.tex"
    eq.write_text(CLEAN_READING, encoding="utf-8")
    assert _run(str(eq), "--crop", "720").exit_code != 0
    assert _run(str(eq), "--crop", "wide").exit_code != 0
