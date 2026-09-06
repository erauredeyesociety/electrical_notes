"""Regression floor for the LaTeX repair layer.

Every test here guards a repair that was found *destroying* mathematics in
MinerU's `mineru/model/mfr/utils.py`, the file this module is derived from. The
audit is in docs/plans/latex-repair-and-validity.md § 2; each test names the
upstream behaviour it exists to keep out.

Self-contained: no course material, no model, no PDF.
"""

from __future__ import annotations

from ocr_handler import latex_repair
from ocr_handler.latex_repair import repair


def _fix(s: str) -> str:
    return repair(s).text


# --------------------------------------------------------------------------
# The substitutions that changed meaning.
# --------------------------------------------------------------------------

def test_bar_is_a_mean_not_an_estimate():
    """Upstream line 282 maps `\\Bar` -> `\\hat`: x-bar becomes x-hat.

    A sample mean silently becomes an estimator, and the result renders
    beautifully. This is the whole reason the file was not vendored as-is.
    """
    out = _fix(r"\Bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i")
    assert r"\bar{x}" in out
    assert r"\hat" not in out


def test_capitalised_accents_still_normalise():
    assert _fix(r"\Hat{\theta}") == r"\hat{\theta}"
    assert _fix(r"\Tilde{x}") == r"\tilde{x}"
    assert _fix(r"\Dot{q}") == r"\dot{q}"


def test_every_substitution_stops_at_a_word_boundary():
    """Upstream has no boundary anywhere, so it rewrites longer commands.

    `\\Barbell` -> `\\hatbell` and `\\slashed{D}` -- the Feynman slash, an
    operator in every relativistic QM course -- -> `/ed{D}`.
    """
    assert _fix(r"\Barbell") == r"\Barbell"
    assert _fix(r"\slashed{D}") == r"\slashed{D}"
    assert _fix(r"a \slash b") == "a / b"


def test_textsubscript_becomes_a_subscript_not_nothing():
    """Upstream deletes `\\textsubscript`, so `H\\textsubscript{2}O` -> `H{2}O`."""
    assert _fix(r"H\textsubscript{2}O") == r"H_{2}O"


def test_upright_greek_maps_but_up_relations_do_not():
    """Upstream's `up`-stripper is a suffix guess, not a command list.

    It turns `\\upharpoonright` into `\\harpoonright` and `\\upuparrows` into
    `\\uparrows`, neither of which is a command at all.
    """
    assert _fix(r"\upalpha + \upvarepsilon") == r"\alpha + \varepsilon"
    for survivor in (r"\upharpoonright", r"\upuparrows", r"\upshape",
                     r"\upsilon", r"\uplus", r"\uparrow", r"\updownarrow"):
        assert _fix(survivor) == survivor, survivor


def test_vline_is_left_alone():
    """Upstream maps `\\vline = ` to `\\models `.

    `\\vline` draws a rule inside a table cell. Rewriting it to semantic
    entailment corrupts any array that uses one, to repair an OCR artefact
    that has never been seen in this project's own output.
    """
    assert _fix(r"\begin{array}{c} a \vline = b \end{array}") == \
        r"\begin{array}{c} a \vline = b \end{array}"


# --------------------------------------------------------------------------
# `\left` / `\right` -- upstream's worst failure.
# --------------------------------------------------------------------------

def test_arrow_commands_are_not_delimiters():
    """`(\\\\right)(\\S*)` matches `\\rightarrow`; upstream then deletes it.

    Measured on this repo's own recorded output: `{ \\rightarrow \\chi[n] = ...`
    came back as `{  \\chi[n] = ...`. A transform pair with no arrow.
    """
    for arrow in (r"x[n] \rightarrow X(z)", r"a \leftarrow b",
                  r"a \leftrightarrow b", r"a \rightharpoonup b",
                  r"a \Rightarrow b", r"a \longrightarrow b"):
        assert _fix(arrow) == arrow, arrow


def test_compact_delimiter_group_is_not_annihilated():
    """`\\S*` is greedy to the first space, so upstream ate the expression.

    `\\left(x+1\\right)` came back as the empty string.
    """
    assert _fix(r"\left(x+1\right)") == r"\left(x+1\right)"
    assert _fix(r"\left[x\right]") == r"\left[x\right]"
    assert _fix(r"\left|x\right|") == r"\left|x\right|"


def test_delimiters_missing_from_upstreams_whitelist_survive():
    """Anything off upstream's 21-entry list was replaced by `.`.

    `\\left\\langle x \\right\\rangle` -- an inner product, an expectation --
    came back as `\\left. x \\right.`.
    """
    for expr in (r"\left\langle x \right\rangle",
                 r"\left\vert x \right\vert",
                 r"\left\Vert x \right\Vert",
                 r"\left\lbrace x \right\rbrace",
                 r"\left< x \right>"):
        assert _fix(expr) == expr, expr


def test_evaluation_bar_and_its_subscript_survive():
    """`\\right|_{x=0}` was rewritten to `\\right.`, deleting "evaluated at"."""
    expr = r"\left. \frac{dy}{dx} \right|_{x=0}"
    assert _fix(expr) == expr
    assert _fix(r"\left.\frac{dy}{dx}\right|_{x=0}") == r"\left.\frac{dy}{dx}\right|_{x=0}"


def test_bare_left_gets_a_null_delimiter():
    assert _fix(r"\left \frac{a}{b} \right)") == r"\left. \frac{a}{b} \right)"


def test_unmatched_delimiters_are_padded_not_stripped():
    """Upstream deletes EVERY `\\left`/`\\right` when the counts disagree.

    That restyles the whole expression to fix one delimiter. Padding the short
    side compiles and changes nothing that was read.
    """
    out = repair(r"\left( x")
    assert out.text == r"\left( x \right."
    assert any("padded" in n for n in out.notes)
    assert repair(r"x \right)").text == r"\left. x \right)"


def test_upstreams_strip_branch_is_available_but_off():
    aggressive = repair(r"\left( x", drop_unmatched_delimiters=True)
    assert aggressive.text == "( x"
    assert r"\left" not in aggressive.text


# --------------------------------------------------------------------------
# Spacing commands -- `process_latex`.
# --------------------------------------------------------------------------

def test_spacing_commands_do_not_become_punctuation():
    """Upstream's `\\<char>` -> `\\ <char>` rule turns `\\,` into `\\ ,`.

    A thin space becomes a space plus a literal comma inside the mathematics.
    Measured firing on 2 of the 44 recorded outputs: `\\;` -> `\\ ;` twice and
    `\\!` -> `\\ !` four times in one string.
    """
    for expr in (r"\int_0^1 f(x)\,dx", r"a\;b", r"a\!b", r"a\:b",
                 r"\alpha\,\beta", r"x \\ y"):
        assert _fix(expr) == expr, expr


def test_a_backslash_before_a_digit_is_still_spaced():
    assert _fix(r"\0") == r"\ 0"


def test_qquad_survives_intact():
    """`\\qquad` is the token `ink.py` uses to mark a deliberately blank region."""
    assert _fix(r"a \qquad b") == r"a \qquad b"
    assert _fix(r"\qquadratic") == r"\qquadratic"


# --------------------------------------------------------------------------
# Structure -- the repairs that are actually wanted.
# --------------------------------------------------------------------------

def test_unmatched_braces_are_dropped():
    out = repair("a{b")
    assert out.text == "ab"
    assert any("brace" in n for n in out.notes)
    assert repair("a}b").text == "ab"


def test_brace_scan_is_escape_aware():
    assert latex_repair.brace_balance(r"\{ \}") == (0, 0)
    assert latex_repair.brace_balance(r"{ x") == (1, 0)
    assert latex_repair.brace_balance(r"x }") == (0, 1)
    assert _fix(r"\left\{ x \right\}") == r"\left\{ x \right\}"


def test_missing_environment_end_is_added():
    assert _fix(r"a & b \end{array}") == r"\begin{array}{c} a & b \end{array}"
    assert _fix(r"\begin{cases} x") == r"\begin{cases} x \end{cases}"


def test_align_star_is_padded_at_all():
    """Upstream builds its pattern as `'\\\\begin\\{' + env + '\\}'`.

    For `align*` the `*` is a regex quantifier, so the pattern reads
    `\\begin{alig n*}` and can never match `\\begin{align*}`. The environment
    upstream most wants to fix is the one it silently cannot.
    """
    assert _fix(r"x &= 1 \end{align*}") == r"\begin{align*} x &= 1 \end{align*}"
    assert latex_repair.environment_balance(r"x \end{align*}") == {"align*": (0, 1)}


def test_trailing_backslashes_are_stripped():
    out = repair(r"\frac{1}{2} \\")
    assert out.text == r"\frac{1}{2} "
    assert any("trailing" in n for n in out.notes)


# --------------------------------------------------------------------------
# Contract.
# --------------------------------------------------------------------------

def test_a_clean_expression_is_returned_untouched_and_silent():
    for expr in (r"H(z)=\frac{1}{1-az^{-1}}",
                 r"\bar{x}_n \to \mu",
                 r"\begin{cases} a \\ b \end{cases}",
                 r"\sum_{n=-\infty}^{\infty} h[n] e^{-j\omega n}"):
        out = repair(expr)
        assert out.text == expr, expr
        assert out.notes == (), expr


def test_every_change_is_reported():
    """The invariant: text changed => at least one note naming a rule.

    Regression, found by running the CLI over the recorded PaddleOCR-VL crop
    outputs in `tmp/eval/out_crops/`: `\\qquad` spacing was applied with
    `re.sub` and appended no note, so this reading came back altered with an
    empty roll-call -- the exact silence this module exists to refuse.
    """
    for expr in (r"\Bar{x",
                 r"\[=|\alpha|^{n}(\qquad\qquad+j\qquad).\]",
                 r"\left( x + 1",
                 r"H\textsubscript{2}O"):
        out = repair(expr)
        assert out.text != expr, expr
        assert out.notes, "a repair a reader cannot see is one they must trust"


def test_qquad_spacing_names_its_rule():
    out = repair(r"(\qquad\qquad)")
    assert out.text == r"(\qquad \qquad )"
    assert any("qquad" in n for n in out.notes)


def test_repair_is_idempotent():
    for expr in (r"\left( x", r"a{b", r"x \end{cases}", r"\Bar{y} \\",
                 r"\upalpha \textsubscript{2}"):
        once = repair(expr).text
        assert repair(once).text == once, expr
