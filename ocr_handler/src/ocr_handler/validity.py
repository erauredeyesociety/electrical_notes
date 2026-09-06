"""Is this equation-model READING trustworthy? -- the axis a compiler cannot see.

The obvious gate is "does the LaTeX compile?". It is not a weak signal, it is
*no* signal. Measured in this repo: **83 of 84 UniMERNet outputs compiled under
tectonic, including 1,113 tokens of array garbage generated from a whole page**
-- matching the CDM authors' published 99.71% render rate for this model. The
decoder was trained on valid LaTeX and emits valid LaTeX whether or not it read
anything. Compile-checking is not in this module and should not be added.

What discriminates is cheap string statistics over the generated token stream,
and the same roll-call contract `structure.py` uses for page faithfulness: one
`Signal` per detector, every time, fired or not, each carrying the evidence a
reader can check. Never a blended score -- the detectors here catch unrelated
failures (a decoder loop, an over-scoped crop, a truncated generation), so an
average would hide the only thing anyone can act on, which is *which* fired.
`Signal` is imported from `structure` rather than redefined so a report can
render both axes with one renderer.

Structural counts are reported, not silently repaired. A string that needs
heavy repair is evidence about the reading; `latex_repair.repair()` exists to
make it compile afterwards, and this module runs BEFORE it.

Constants and the sweeps behind them:
docs/plans/latex-repair-and-validity.md § 3.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .latex_repair import brace_balance, delimiter_balance, environment_balance
from .structure import Signal

PLAUSIBLE = "plausible"
SUSPECT = "suspect"


@dataclass(frozen=True)
class Reading:
    """One model output, and the crop it was generated from if that is known.

    `crop` is `(width_px, height_px)` of the image handed to the model. It is
    optional because a reading can arrive without it; the detector that needs
    it says so in its detail rather than pretending it ran.
    """

    text: str
    crop: tuple[int, int] | None = None


# Tokenisation, fixed once here because every detector depends on it and no
# ratio is comparable across two definitions. A control word is one token, an
# escape (`\\`, `\{`, `\,`) is one, every other non-space character is one.
#
# ⚠ Whitespace is EXCLUDED -- a deliberate change from
# docs/research/equation-ocr-specialists.md § 5, which used `\\[a-zA-Z]+|.` and
# so counted spaces. UniMERNet emits a space between every token and a human
# emits almost none, so that definition scores the same expression twice as
# varied when a human typed it, and no threshold survives crossing corpora --
# which is exactly what validating both directions requires.
_TOKEN_RE = re.compile(r"\\[a-zA-Z]+|\\.|\S")


def tokens(text: str) -> list[str]:
    """The token stream every signal in this module is measured over."""
    return _TOKEN_RE.findall(text)


def variety_ratio(text: str) -> tuple[float, int]:
    """`(distinct token types / total tokens, total tokens)`."""
    toks = tokens(text)
    return (len(set(toks)) / len(toks) if toks else 0.0), len(toks)


# --------------------------------------------------------------------------
# Detector 1 -- token variety. The measured winner, re-measured.
# --------------------------------------------------------------------------

# Swept on the whitespace-free tokenisation above against 84 recorded model
# outputs (10 of them pathological) and 719 known-good coursework equations
# from content/cesc_{410,470}/hw/hw01:
#
#   ratio <   patho   OCR-good FP   corpus display rows (2,967, all of content/)
#   0.20      2/10      0/74          28  (0.94%)
#   0.22      3/10      0/74          42  (1.42%)
#   0.25      4/10      0/74          71  (2.39%)
#   0.30      5/10      0/74         197  (6.64%)
#
# 0.20, and the reason is the roll-call, not the ratio: every pathology 0.25
# would add is ALREADY caught by `length-vs-crop` and `repeat-loop`, so the 43
# extra coursework equations buy nothing. Hand-checked, about a third of the 28
# at 0.20 are corpus-extractor artefacts; the rest are genuine -- a long
# partial-fraction derivation where `z^{-1}` recurs a dozen times really is
# low-variety, and that is this detector's floor.
#
# ⚠ The research doc's headline -- 8/10 caught, 0 false positives in 76 -- does
# NOT reproduce. It was measured with a space-counting tokenisation and only
# against other model outputs; adding a known-good corpus is what moves it.
_VARIETY_MAX = 0.20

# Below this a low ratio is just a short expression: `x = y` is 3 types over
# 3 tokens either way. Inherited from the research doc's rule and re-checked --
# no recorded pathology under 40 tokens is caught by variety at any threshold.
_VARIETY_MIN_TOKENS = 40


def _token_variety(r: Reading) -> str | None:
    ratio, n = variety_ratio(r.text)
    if n <= _VARIETY_MIN_TOKENS or ratio >= _VARIETY_MAX:
        return None
    return f"{len(set(tokens(r.text)))} token types in {n} tokens (ratio {ratio:.3f})"


# --------------------------------------------------------------------------
# Detector 2 -- nothing was read.
# --------------------------------------------------------------------------

# The research doc's second rule. `patho/blank_paper` -- an empty patch of
# paper -- returned the single token `-`.
_MIN_TOKENS = 5


def _empty_reading(r: Reading) -> str | None:
    n = len(tokens(r.text))
    if n >= _MIN_TOKENS:
        return None
    return f"{n} token(s): {r.text.strip()[:40]!r}"


# --------------------------------------------------------------------------
# Detector 3 -- a decoder loop, in either of the two shapes it takes.
# --------------------------------------------------------------------------

# surya/chandra's constants for their tail-anchored repeat check. Their source
# is not in ~/tmp/ocr_repos, so the scaling law is RECONSTRUCTED from the two
# documented data points rather than copied: a 1-character loop needs >16
# repeats and a 100-character loop >4. `base * (1 + scaling / len(unit))` gives
# 16.0 and 4.12, reproducing both.
_REPEAT_WINDOW = 500
_REPEAT_BASE = 4
_REPEAT_SCALING = 3.0

# ⚠ Measured: the tail check fires on **0 of the 10** recorded pathologies --
# its shape is wrong for this model. UniMERNet does not run off the end; it
# loops in the MIDDLE of a `\begin{array}` and then closes the array, so the
# tail reads `... \end{array}` and looks fine. `patho/whole_page` ends
# `\cosh \cosh \cosh \cosh \cosh \cosh } \right) } \end{array} }` -- the loop is
# six tokens back. Kept because it is cheap and is the known-good guard for the
# failure mode another decoder would show; the token-run arm is what fires here.
_RUN_MAX_SYMBOLIC = 4      # coursework max 3 (`}`); patho 4 (`\!`, `}`), 6 (`\cosh`)
_RUN_MAX_NUMERIC = 10      # coursework max 8 (`0.3888888889`); patho 13 (`1`)

_NUMERAL_RE = re.compile(r"^\d$")

# An `array` column spec is layout, not content: `\begin{array} { l l l l }` is
# four identical tokens and a perfectly ordinary four-column matrix. Measured:
# every one of the 6 corpus rows `_RUN_MAX_SYMBOLIC = 4` flagged is a column
# spec (`{c|ccccc}`), none a loop. Same move `structure.py` makes refusing to
# call a bare numeral symbolic. Restricted to the environments that take a
# spec, so it cannot eat a `\begin{cases}`'s first group.
_COLSPEC_RE = re.compile(r"\\begin\{(?:array|tabular\*?|subarray)\}\s*\{[^{}]*\}")


def tail_repeat(text: str) -> tuple[str, int] | None:
    """surya's check: a unit repeated at the very end of the string."""
    tail = text[-_REPEAT_WINDOW:]
    n = len(tail)
    for size in range(1, n // 2 + 1):
        required = _REPEAT_BASE * (1 + _REPEAT_SCALING / size)
        if n // size <= required:
            break          # no unit this long can repeat often enough. Exact,
        unit = tail[-size:]  # not a heuristic: it caps `size` at 100 for n=500.
        count, i = 0, n
        while i >= size and tail[i - size:i] == unit:
            count += 1
            i -= size
        if count > required:
            return unit, count
    return None


def token_run(text: str) -> tuple[str, int] | None:
    """The longest run of one repeated token anywhere, if it is too long.

    Digits get their own, much higher bar for the same reason `structure.py`
    rejects bare numerals: `0.3888888889` is a decimal expansion, not a loop.
    """
    toks = tokens(_COLSPEC_RE.sub("", text))
    best, run = ("", 0), 0
    previous = None
    for tok in toks:
        run = run + 1 if tok == previous else 1
        previous = tok
        if run > best[1]:
            best = (tok, run)
    tok, run = best
    limit = _RUN_MAX_NUMERIC if _NUMERAL_RE.match(tok) else _RUN_MAX_SYMBOLIC
    return best if run >= limit else None


def _repeat_loop(r: Reading) -> str | None:
    hit = tail_repeat(r.text)
    if hit is not None:
        return f"tail repeats {hit[0]!r} x{hit[1]}"
    hit = token_run(r.text)
    if hit is not None:
        return f"token {hit[0]!r} repeated x{hit[1]} consecutively"
    return None


# --------------------------------------------------------------------------
# Detectors 4-6 -- structural counts, BEFORE repair.
# --------------------------------------------------------------------------

# Measured: all three fire on 0 of 44 raw model outputs and 0 of 2,967 corpus
# display rows. They are a silent tripwire here, and that silence IS the
# finding -- the same fact that kills compile-checking, arrived at for free.
# They stay because they cost one regex each, because they make
# `latex_repair`'s work visible instead of silent, and because a detector that
# has never fired is not the same thing as one that is absent.


def _unbalanced_braces(r: Reading) -> str | None:
    unclosed, unopened = brace_balance(r.text)
    if not (unclosed or unopened):
        return None
    return f"{unclosed} unclosed '{{', {unopened} unopened '}}'"


def _unmatched_delimiters(r: Reading) -> str | None:
    left, right = delimiter_balance(r.text)
    return None if left == right else rf"{left} \left vs {right} \right"


def _unmatched_environments(r: Reading) -> str | None:
    bad = environment_balance(r.text)
    if not bad:
        return None
    return ", ".join(f"{env} {b} begin / {e} end" for env, (b, e) in bad.items())


# --------------------------------------------------------------------------
# Detector 7 -- length against the crop it came from.
# --------------------------------------------------------------------------

# 1,113 tokens from one equation crop is absurd on its face, but a bare token
# cap cannot say so -- a long legitimate equation and a short looping one
# overlap completely. The crop is what separates them: an equation crop is ONE
# LINE, so `width / height` is how many glyph-heights fit across it, and a
# faithful reading spends about one token per glyph-height.
#
# Measured over the 34 sweep rows that record their crop size:
#   highest good reading   13.7 tok/line-width (expo/pad+96, a 96 px over-pad)
#   lowest degenerate one  21.6 tok/line-width (eqline/pad+48)
#   worst                 521.0 tok/line-width (patho/whole_page)
# 18 is the midpoint of that gap, catches 8 of the 10 recorded pathologies with
# 0 false positives, and is the best single detector here -- also the only one
# needing anything beyond the string. It assumes one line per crop, which is
# what `crops.py` produces; pass no crop rather than a wrong one.
_MAX_TOKENS_PER_LINE_WIDTH = 18


def _length_vs_crop(r: Reading) -> str | None:
    if r.crop is None:
        return None
    width, height = r.crop
    if width <= 0 or height <= 0:
        return None
    line_widths = max(1.0, width / height)
    n = len(tokens(r.text))
    density = n / line_widths
    if density < _MAX_TOKENS_PER_LINE_WIDTH:
        return None
    return (f"{n} tokens from a {width}x{height} crop "
            f"= {density:.1f} per line-width (limit {_MAX_TOKENS_PER_LINE_WIDTH})")


# --------------------------------------------------------------------------
# Detector 8 -- scaffolding with nothing inside it.
# --------------------------------------------------------------------------

# `empty-reading` counts TOKENS, and 45 tokens of nested empty `aligned` are
# 45 tokens. Recorded -- PaddleOCR-VL, a 500x160 crop of the un-annotated twin
# (`crop_expo_base` in tmp/eval/out_crops/results.json):
#
#   \[\begin{aligned}\begin{aligned}\\ &\end{aligned}\\ \end{aligned}\]
#
# Zero mathematics, and it passed the seven detectors above: 45 tokens (the
# tokenisation of § 3.2 spends nine on `{aligned}` alone), variety 0.333, no
# token run of 4, braces/delimiters/environments all balanced, 14.4 tokens per
# line-width. What separates that from a reading is not how much came back but
# how much of it is mathematics.
#
# ⚠ `length-vs-crop` cannot be re-tuned at this. 14.4 is ABOVE the highest
# recorded good reading (13.7, expo/pad+96), so a limit of 14 would in fact
# catch it -- but the margin collapses from ±4 (13.7 … 18 … 21.6) to 0.35, it
# needs a crop the file-input path does not have, and it is the wrong axis:
# this same reading off a 1000x160 crop scores 7.2 and passes at any limit.
# Measured, not assumed.

# Tokens that carry no mathematics on their own: they group, position, size,
# separate or name. A reading made only of these read nothing. Whole
# `\begin{...}`/`\end{...}` constructs and `array` column specs come out by
# regex first -- the same strip `repeat-loop` already makes, for the same
# reason: an environment name is layout, not content.
_ENV_NAME_RE = re.compile(r"\\(?:begin|end)\s*\{[^{}]*\}")

_SCAFFOLD = frozenset({
    # math-mode delimiters
    r"\[", r"\]", r"\(", r"\)", "$",
    # grouping, cells and rows
    "{", "}", "&", "\\\\", r"\cr", r"\hline", r"\hdashline",
    r"\toprule", r"\midrule", r"\bottomrule", r"\noalign",
    r"\multicolumn", r"\vline",
    # spacing. `\qquad` is here deliberately: it is the token ink.py writes
    # where it removed a region, so a reading made of it is a reading of holes.
    r"\,", r"\;", r"\:", r"\!", "\\ ", r"\quad", r"\qquad",
    r"\thinspace", r"\medspace", r"\thickspace", r"\negthinspace",
    r"\hspace", r"\vspace", r"\enspace", r"\hfill", r"\hskip", r"\vskip",
    r"\smallskip", r"\medskip", r"\bigskip",
    # delimiter sizing -- the delimiter itself still counts, only the size does not
    r"\left", r"\right", r"\middle",
    r"\big", r"\Big", r"\bigg", r"\Bigg", r"\bigm", r"\Bigm",
    r"\bigl", r"\bigr", r"\Bigl", r"\Bigr",
    r"\biggl", r"\biggr", r"\Biggl", r"\Biggr",
    # style selection and numbering
    r"\displaystyle", r"\textstyle", r"\scriptstyle", r"\scriptscriptstyle",
    r"\limits", r"\nolimits", r"\nonumber", r"\notag",
})


def content_tokens(text: str) -> list[str]:
    """`tokens()` with the scaffolding removed -- what was actually READ.

    Font selectors (`\\mathrm`, `\\text`) are deliberately NOT scaffolding:
    they wrap content that is already counted, so dropping them would only
    narrow the margin against short legitimate readings for nothing.
    """
    bare = _ENV_NAME_RE.sub(" ", _COLSPEC_RE.sub(" ", text))
    return [t for t in tokens(bare) if t not in _SCAFFOLD]


# 3, and `x = 1` is what pins it -- the shortest expression anyone would call a
# legitimate reading is exactly three content tokens, so 3 is the largest floor
# that leaves it alone. Swept over 2,508 display-maths rows extracted from all
# 394 `.tex` files in content/ and 146 recorded model readings (the 44
# UniMERNet crops of tmp/eqocr/sweep.json, its 40 background variants, 54 in
# tmp/crops_check/, 8 PaddleOCR-VL records in tmp/eval/out_*/):
#
#   content <   corpus rows (2,508)   model readings (146)
#   3                   0                     4
#   4                   1                     4
#   5                   2                     4
#   6                   4                     4
#
# Raising it buys nothing: all four model readings it catches are caught at 3,
# and the corpus cost is the only thing that moves. The corpus minimum is 3
# (`\boxed{#1}`, an artefact of the measurement's own extractor); the shortest
# GENUINE row is `\Omega = \omega T` at 4.
#
# The four it catches, and this is the whole recall claim: `crop_expo_base`
# read as formula (0 content of 45 tokens -- the reading above, and the only
# one the other seven miss), `crop_expo_base` read as ocr (empty string),
# `patho/blank_paper` (`-`) and `control/expo_base_twin` (`\mp`). The last
# three `empty-reading` already holds.
#
# ⚠ Its floor, stated rather than tuned away: a lone two-entry row vector
# (`\begin{pmatrix} 1 & 2 \end{pmatrix}`) is two content tokens and would fire.
# 0 of the 2,508 corpus rows and 0 of the 146 readings are that short, so it is
# a hypothetical, but it is the shape a false positive would take.
_MIN_CONTENT_TOKENS = 3


def _content_free(r: Reading) -> str | None:
    content = content_tokens(r.text)
    if len(content) >= _MIN_CONTENT_TOKENS:
        return None
    n = len(tokens(r.text))
    tail = f": {' '.join(content)}" if content else " — nothing but scaffolding"
    return f"{len(content)} content token(s) in {n}{tail}"


# --------------------------------------------------------------------------
# The registry. Adding a detector is one entry here.
# --------------------------------------------------------------------------

_DETECTORS = (
    ("token-variety", _token_variety,
     "the same few tokens over and over — a decoder loop, not a reading"),
    ("empty-reading", _empty_reading,
     "almost nothing came back — the crop probably held no ink"),
    ("content-free", _content_free,
     "plenty came back and almost none of it is mathematics — empty environments"),
    ("repeat-loop", _repeat_loop,
     "one unit repeated far past what any expression needs"),
    ("unbalanced-braces", _unbalanced_braces,
     "`{` and `}` do not pair — the generation was truncated or drifted"),
    ("unmatched-delimiters", _unmatched_delimiters,
     r"`\left` and `\right` counts disagree"),
    ("unmatched-environments", _unmatched_environments,
     r"a `\begin{...}` with no `\end{...}`, or the reverse"),
    ("length-vs-crop", _length_vs_crop,
     "far more tokens than one line of mathematics can hold"),
)

NAMES = tuple(name for name, _, _ in _DETECTORS)
WHY = {name: why for name, _, why in _DETECTORS}


def signals(text: str, *, crop: tuple[int, int] | None = None) -> tuple[Signal, ...]:
    """Run every detector over one reading. One `Signal` per detector, always."""
    reading = Reading(text=text, crop=crop)
    out = []
    for name, detect, _why in _DETECTORS:
        detail = detect(reading)
        fired = detail is not None
        if not fired and name == "length-vs-crop" and crop is None:
            # A detector that could not run and one that ran and passed are
            # different facts, and a roll-call that conflates them is lying.
            detail = "not evaluated: no crop size supplied"
        out.append(Signal(name=name, fired=fired, detail=detail or ""))
    return tuple(out)


def classify(reading_signals: tuple[Signal, ...]) -> str:
    """A reading is suspect if ANY detector fired. An OR, never an average."""
    return SUSPECT if any(s.fired for s in reading_signals) else PLAUSIBLE
