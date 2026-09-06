"""Is the extracted text FAITHFUL? -- the axis character count cannot see.

`textlayer.py` answers "is there text?" by counting characters per page. That
question has a dangerous blind spot: a page whose prose is intact but whose
rendered equations were shredded into unordered fragments scores `ok`, and gets
routed *away* from further processing while its load-bearing content is
unusable. Measured on a 47-page born-digital LaTeX PDF: 47/47 pages `ok`,
verdict `text-layer-sufficient`, every displayed equation destroyed.

This module carries the second axis. It runs cheap, model-free, PyMuPDF-only
detectors over the extracted string and reports, per page, WHICH corruption was
seen -- never a bare boolean, because a reader who cannot see the evidence
cannot check the call, and because the next detector needs somewhere to go.

The repair for a suspect page is NOT OCR. The glyphs are already present with
correct coordinates; a vision model would spend GPU recovering what is already
in the file and return a worse answer. Suspect means "re-extract with layout
awareness, or look at the page image" -- a different remedy from `sparse`.

One qualification, added with detector 4: `unmapped-glyphs` reports characters
whose Unicode mapping is missing, and for THOSE the page image does still
carry the shape. Re-rendering can recover a lambda that arrives as an empty
box; it cannot recover a reading order. The per-detector line in `WHY` says so,
because a blanket "OCR is not the repair" is only true of the other three.

Design and the sweeps behind every constant:
docs/plans/structural-faithfulness.md
Detectors 3 and 4, their benign list, and the independent re-derivation of
every count in it: docs/findings/recall-was-a-symbol-test-not-a-run-length.md
(§ 5)
"""

from __future__ import annotations

import re
from dataclasses import dataclass

INTACT = "intact"
SUSPECT = "suspect"


@dataclass(frozen=True)
class Signal:
    """One detector's outcome on one page, with the evidence for it.

    Every detector reports on every page, fired or not, so the roll-call is
    complete and a `suspect` verdict can always be traced to a named cause.
    """

    name: str
    fired: bool
    detail: str


# --------------------------------------------------------------------------
# Detector 1 -- letter spacing. Not new: this fired on 51 documents already
# and fed NOTHING, a footnote attached to no verdict and no page. It is a
# faithfulness signal, so it belongs here rather than dangling on its own.
# --------------------------------------------------------------------------

# Some encoders emit one glyph per text run, so extraction yields
# "C o m p u t e r  O r g a n i z a t i o n". Detected, not silently repaired:
# collapsing it is guesswork and would corrupt legitimately spaced text.
#
# The pattern was `(?:\b\w\s){6,}`, and it was wrong in two ways that only
# became visible once it fed a verdict instead of a footnote. Measured over
# 441 documents / 7,155 pages on 2026-09-05:
#
#   (?:\b\w\s){6,}            51 docs / 154 pages  -- the corpus-census number
#   (?:\b\w[^\S\n]){6,}        5 docs /  11 pages
#   (?:\b[^\W\d_][^\S\n]){6,}  3 docs /   9 pages  -- all genuine
#
# `\s` matches a NEWLINE, so a plot's tick labels or an enumerate marker set,
# extracted one per line as "1\n2\n3\n4\n5\n6", scored as a corrupt text
# layer: 46 of the 51 documents fired on nothing else. And `\w` matches a
# digit, which kept a horizontal axis "1 2 3 4 5 6" firing after that.
# Requiring six consecutive LETTERS separated by HORIZONTAL space leaves
# exactly the artefact the detector is named for. All three of its existing
# regression tests are unchanged and still pass.
#
# Cost: a rotated axis label extracted vertically ("C\no\nn\nt\nr\no\nl",
# seen in the NASA SE handbook) is no longer caught. That is a *vertical*
# letter-spacing detector and needs to tell a word from a tick sequence --
# a separate detector, open question 3 in the plan, not a wider regex here.
_SPACED_RE = re.compile(r"(?:\b[^\W\d_][^\S\n]){6,}")


def is_letter_spaced(text: str) -> bool:
    """True when extraction produced one-glyph-per-run spacing artefacts."""
    return bool(_SPACED_RE.search(text))


def _letter_spacing(text: str) -> str | None:
    m = _SPACED_RE.search(text)
    return None if m is None else f"one glyph per text run: {m.group(0)[:40]!r}"


# --------------------------------------------------------------------------
# Detector 2 -- shredded lines. A 2-D layout (matrix, stacked fraction, cases
# brace, summation with limits) flattened by reading-order extraction into a
# column of fragments. On the fixture's page 7 a 3x3 intrinsic matrix becomes
# 32 consecutive one- and two-character lines.
# --------------------------------------------------------------------------

# Swept over {3,4,5,6,8} against fixture recall vs a 1,475-page control corpus
# (all of cesc_470, cec_320, stat_412, none of which should fire). 4 is the
# knee: 3 -> 4 buys two more true positives for one extra control page; 4 -> 5
# multiplies control documents by 7 for two. See the plan for the table.
#
# That control corpus premise was RE-MEASURED on 2026-09-06 and is wrong: 44 of
# the 49 pages it now flags in cec_320 / cesc_470 are real -- `cases` braces,
# summation limits, `\underbrace`, flattened fractions in LaTeX-set homework.
# The number below is unchanged because a max-chars sweep needs its own labelled
# increment, which this session did not draw. Priced, so nobody re-derives it:
# raising it to 8 (with the strong-symbolic rule below) costs +232 corpus pages
# and recovers 4 more of the 12 hand-labelled recall misses -- which are blocked
# by THIS constant, not by the run length. Measurement:
# docs/findings/recall-was-a-symbol-test-not-a-run-length.md
_SHRED_MAX_CHARS = 4

# Swept DOWN over {4,3,2} on 2026-09-06 against 161 hand-labelled ground-truth
# pages plus 75 newly hand-labelled pages drawn at random from the corpus
# increment each step adds. Reweighted strict precision / estimated true
# positives over 459 documents / 7,198 pages:
#
#   min_run   corpus pages   strict precision      TP   recall
#     4 (was)          416   84.8% [72%, 92%]     353    35.3%
#     3                677   84.2% [74%, 91%]     570    57.1%
#     2               1213   59.4% [61%, 78%]     720    72.1%
#     2 + strong       732   93.1% [85%, 96%]     681    68.2%
#
# Alone, 2 is the trade the plan warned about: the increment it adds over 3 is
# 536 pages that hand-label 28% genuine (17 of 25 are Wingdings bullet columns
# in one handbook and assembly-listing gutters). It is the `_is_strong` rule
# below that pays for it, by killing exactly those two classes -- with it, 2
# beats the shipped 4 on BOTH axes.
_SHRED_MIN_RUN = 2

# Fraction of a run's lines that must carry symbolic content. Swept over
# {0, 0.1, 0.25, 0.3, 0.4, 0.5}: 0.25 keeps all 10 originally-measured fixture
# pages, 0.3 loses 3 of them, and below 0.25 the ruler-scale and axis-tick
# false positives return.
_SHRED_MIN_SYMBOLIC = 0.25

# Character classes that mean "this fragment is part of an expression".
# PUA is load-bearing: Computer Modern's big delimiters (U+F8F1..U+F8F4 are
# \left\{ pieces) have no Unicode mapping and arrive as PUA code points.
# C0 controls are the same failure for other math glyphs.
_SYMBOLIC_RANGES = (
    (0x0000, 0x0008), (0x000B, 0x001F),   # unmapped glyphs, emitted raw
    (0x00B0, 0x00BF), (0x00D7, 0x00D7), (0x00F7, 0x00F7),
    (0x02B0, 0x02FF),                     # modifier letters: \tilde, \hat
    (0x0370, 0x03FF),                     # Greek
    (0x2070, 0x209F),                     # sub/superscripts
    (0x2100, 0x214F),                     # letterlike
    (0x2190, 0x21FF),                     # arrows
    (0x2200, 0x22FF),                     # mathematical operators
    (0x2300, 0x23FF),                     # misc technical, big brackets
    (0x27C0, 0x27EF), (0x2980, 0x29FF), (0x2A00, 0x2AFF),
    (0xE000, 0xF8FF),                     # Private Use Area
    (0x1D400, 0x1D7FF),                   # mathematical alphanumerics
)

# A bare numeral is NOT symbolic, even carrying U+2212 MINUS. Without this
# rejection, plot axis ticks (0.2 0.4 0.6 -2) and \lstlisting line-number
# gutters (5 . 6 . 7 . 8 .) pass as mathematics -- measured, and it was the
# single largest source of false positives.
_NUMERAL_RE = re.compile(r"^[+\-−]?\d+(?:[.,]\d+)?[.,)]?$")


def _is_strong(line: str) -> bool:
    """Does this fragment carry an actual MATHEMATICAL character?

    The character-range half of `_is_symbolic`, without its two fallbacks. It
    is separate because those fallbacks -- "a lone ASCII letter" and "contains
    an `=`" -- are precisely what the two commonest false-positive classes look
    like, and a run made only of them is not evidence of anything:

      z / z          a Wingdings list bullet that maps to ASCII `z`, twice per
                     wrapped bullet. 1 document, and 10 of 25 sampled pages in
                     the min_run 3 -> 2 increment.
      16 / 17 / b    an assembly listing's line-number gutter plus the `b`
                     branch opcode -- the same escape as the hard misfire the
                     ground-truth sample found (`252 / // / 253 / v`).
      14 / =         a C operator-precedence table.

    Requiring at least one strong line in every run, measured 2026-09-06 over
    236 hand-labelled pages:

      setting              corpus pages   strict precision      TP   recall
      min_run 4 (the old value)     416   84.8% [72%, 92%]     353    35.3%
      min_run 2, no rule           1213   59.4% [61%, 78%]     720    72.1%
      min_run 2, this rule          732   93.1% [85%, 96%]     681    68.2%

    It costs, and the cost is measured: of 46 labelled pages the shipped
    detector flags, it drops 6 -- 5 `partial` (a figure axis, a decision tree,
    a 34x34 traceability matrix arriving as 123 lines of `X`) and 1 misfire,
    and NO strict hit. Broad precision therefore falls 98% -> 95% while strict
    precision rises. Non-mathematical 2-D loss is what is given up.

    `=` was measured as a third tier and rejected: admitting a bare `=` line as
    strong takes precision 93.1% -> 85.4% for +2 estimated true positives.
    A long-run escape (`>= 20 lines regardless`) was measured and rejected too:
    it recovers 6 pages and lowers strict precision to 92.0%.
    """
    # Strip the DECLARED-BENIGN glyphs first. Without this, `_is_strong` and
    # `unmapped_glyphs` (~220 lines below) contradict each other: the same
    # U+F0B7 / U+F070 / U+F06C that the benign list calls decorative -- Office
    # bullets, 1,514 + 1,016 + 366 occurrences -- land inside `_SYMBOLIC_RANGES`
    # and count here as proof of mathematics. One detector cannot call a glyph
    # a bullet while another calls it an integral sign.
    #
    # Measured 2026-09-06 over the whole corpus: 732 -> 729 shredded-lines
    # pages. All 3 removed are non-mathematical -- two PowerPoint lecture
    # outlines and a systems-engineering guidebook -- so this is a precision
    # gain, not a recall cost. Found by the independent replication pass:
    # docs/findings/precision-replicates-the-priced-cost-does-not-2026-09-06.md
    line = "".join(ch for ch in line if ord(ch) not in _BENIGN_GLYPHS)
    if not line or _NUMERAL_RE.match(line):
        return False
    return any(any(lo <= ord(ch) <= hi for lo, hi in _SYMBOLIC_RANGES)
               for ch in line)


def _is_symbolic(line: str) -> bool:
    """Does this short fragment look like part of an expression, not a label?"""
    if not line or _NUMERAL_RE.match(line):
        return False
    if _is_strong(line):
        return True
    if len(line) == 1 and line.isascii() and line.isalpha():
        return True          # a lone variable: u, v, X, i
    return "=" in line


def _shred_runs(text: str) -> list[list[str]]:
    """Maximal runs of consecutive short lines. Blank lines break a run --
    counting them inflates the signal on any page with vertical whitespace."""
    runs: list[list[str]] = []
    current: list[str] = []
    for raw in text.split("\n"):
        line = raw.strip()
        if line and len(line) <= _SHRED_MAX_CHARS:
            current.append(line)
            continue
        if len(current) >= _SHRED_MIN_RUN:
            runs.append(current)
        current = []
    if len(current) >= _SHRED_MIN_RUN:
        runs.append(current)
    return runs


def shredded_run(text: str) -> list[str] | None:
    """The first run that looks like a flattened expression, or None.

    Two independent gates, and both are needed. The RATIO rejects a long
    numeric gutter; the STRONG test rejects a short run of lone ASCII letters.
    At `_SHRED_MIN_RUN = 2` the ratio alone is nearly vacuous -- one symbolic
    line in two already clears 0.25 -- so without `_is_strong` the run length
    could not be lowered at all.
    """
    for run in _shred_runs(text):
        if not any(_is_strong(line) for line in run):
            continue
        symbolic = sum(1 for line in run if _is_symbolic(line))
        if symbolic / len(run) >= _SHRED_MIN_SYMBOLIC:
            return run
    return None


def _shredded_lines(text: str) -> str | None:
    run = shredded_run(text)
    if run is None:
        return None
    shown = " / ".join(run[:8]) + (" ..." if len(run) > 8 else "")
    return f"{len(run)} stacked fragments: {shown}"


# --------------------------------------------------------------------------
# Detector 3 -- vertical letter spacing. The cost the horizontal detector
# above paid when its `\s` was tightened to `[^\S\n]`: a rotated label whose
# glyphs extract one per LINE ("C\no\nn\nt\nr\no\nl", the arrows of figure
# 6.4-4 in the NASA SE handbook) stopped being caught by name.
#
# Widening the regex back is the wrong repair and would re-open the measured
# 17x overcount -- "0\n1\n2\n3" is a plot's axis, not a shredded word. The
# separating question is WORD versus LABEL, and `shredded-lines` already
# answers the numeric half of it by rejecting bare numerals; this answers the
# alphabetic half the same way, by rejecting things that are not words.
#
# It used to add NO page: a run of six single-letter lines was also a run of
# short lines whose every line `_is_symbolic` called a lone variable, so this
# detector was a strict subset of `shredded-lines` and contributed the NAME
# rather than the page. That changed on 2026-09-06, when `_is_strong` stopped
# `shredded-lines` accepting a column of bare ASCII letters -- measured over
# 459 documents / 7,198 pages, all FOUR of this detector's pages are now pages
# it is the ONLY signal on. It became independent evidence without being
# touched. docs/findings/recall-was-a-symbol-test-not-a-run-length.md § 5.
# --------------------------------------------------------------------------

# Six, the same run length the horizontal detector uses, and measured: 5
# admits a column of 'o's in a cesc_410 handwriting deck, 4 admits an AE318
# table's `a b c c` row labels, and 10 loses `Control` / `Identify` /
# `Analyze`. Over 448 documents / 7,187 pages the sweep 4/5/6/7/8/10 gives
# 6 / 5 / 4 / 4 / 4 / 2 flagged pages, and only from 6 up are they all real.
_VERT_MIN_RUN = 6

# A line that is exactly one letter. `[^\W\d_]` is the horizontal detector's
# own class -- a digit is not a letter, so "0\n1\n2\n3\n4\n5" cannot match and
# the axis-tick regression cannot return through this door either.
_VERT_RE = re.compile(r"(?:^[^\W\d_]$\n?){%d,}" % _VERT_MIN_RUN, re.M)

# `y` counts as a vowel: without it "System" reads as a 4-consonant run.
_VOWELS = frozenset("aeiouy")


def _looks_like_a_word(run: str) -> bool:
    """Is this column of letters a shredded WORD, or a column of labels?

    Three tests, each paid for by a measured false positive among the 26
    pages the run test alone flags -- 22 of which are not words:

      case shape       kills `ABCDEFGH`, `MMMMEEEE`, `NkBARkkk` (15 pages)
      not an A-Z run   kills `abcdefgh`, a table's lettered row labels
                       (7 pages) -- the alphabetic twin of the numeric
                       gutter `shredded-lines` already rejects
      no 4+ consonants kills `abnnss`, an optics formula's subscripts

    Survivors, corpus-wide: Control, Identify, Analyze, Sustaining, System,
    Management, Operation, Enginee -- one document, four pages, no others.
    """
    if not (run.islower() or run.istitle()):
        return False
    low = run.lower()
    if all(a < b for a, b in zip(low, low[1:])):
        return False
    consonants = 0
    for ch in low:
        consonants = 0 if ch in _VOWELS else consonants + 1
        if consonants >= 4:
            return False
    return True


def vertical_run(text: str) -> str | None:
    """The first column of single letters that spells a word, or None."""
    for m in _VERT_RE.finditer(text):
        word = "".join(m.group(0).split())
        if _looks_like_a_word(word):
            return word
    return None


def _vertical_letter_spacing(text: str) -> str | None:
    word = vertical_run(text)
    if word is None:
        return None
    return f"one letter per line: {'/'.join(word)!r} reads as {word!r}"


# --------------------------------------------------------------------------
# Detector 4 -- unmapped glyphs. Code points the extractor could NOT map to
# Unicode, so the reader gets an empty box where a character was: Private Use
# Area and C0 controls. Deferred by the plan pending a benign list, because
# the raw signal's commonest corpus trigger is an ordinary bullet.
#
# Unlike the other three, this one is not a LAYOUT fault -- the page image
# still carries the glyph, so re-rendering can recover it.
# --------------------------------------------------------------------------

# Same ranges `_SYMBOLIC_RANGES` already treats as unmapped math. Tab and
# newline are excluded; carriage return would be in (0x0B, 0x1F) but PyMuPDF
# emits none in 7,187 corpus pages, so the two definitions coincide exactly.
_UNMAPPED_RANGES = ((0x0000, 0x0008), (0x000B, 0x001F), (0xE000, 0xF8FF))

# THE BENIGN LIST, built by ranking all 89 Private-Use and control code
# points in the corpus by frequency and RENDERING each one's glyph bbox to
# see what it is on the page -- not from a font spec. The top of that ranking:
#
#   U+F0B7  1,514  SymbolMT      filled bullet         BENIGN, 164 pages
#   U+0017  1,437  Calibri       the "ti" ligature     SIGNAL, breaks words
#   U+F070  1,016  Wingdings     square/triangle (99%) BENIGN, 424 pages
#   U+F06C    366  Wingdings     round bullet   (95%)  BENIGN, 357 pages
#   U+F8F4    344  txexs/CMEX10  \left\{ extension     SIGNAL
#   U+0001    186  CMEX10        \left( , big          SIGNAL
#
# The cut falls after the third and nowhere else: those three are the Office
# dingbat block, 92% of its corpus volume, and a bullet reaching the reader
# as a box costs nothing -- the line break already says "list item". Below
# them the ranking is mathematics. Full table and hand-labels:
# docs/findings/recall-was-a-symbol-test-not-a-run-length.md § 5.1.
#
# Priced, not hidden: the list silences 901 pages of which 9 are genuine --
# Symbol-font lambda and pi wear the same code points as Wingdings bullets
# (28 occurrences against 2,868). The font separates them and the text does
# not, and `signals()` takes a string. 99.0% of what is silenced is furniture.
#
# Deliberately NOT benign, though both are furniture where they appear:
# U+0007 and U+0008, invisible tab leaders in two systems-engineering
# handbooks (21 pages). In CMEX10's own encoding 0x07 is `\rceil` and 0x08 is
# `\{` -- suppressing them corpus-wide would blind this detector to the very
# `cases` brace it exists to catch, to spare two handbooks.
_BENIGN_GLYPHS = frozenset({0xF0B7, 0xF070, 0xF06C})


def unmapped_glyphs(text: str) -> dict[int, int]:
    """Unmapped code points on the page, minus the benign list, with counts."""
    found: dict[int, int] = {}
    for ch in text:
        code = ord(ch)
        if code in _BENIGN_GLYPHS:
            continue
        if any(lo <= code <= hi for lo, hi in _UNMAPPED_RANGES):
            found[code] = found.get(code, 0) + 1
    return found


def _unmapped(text: str) -> str | None:
    found = unmapped_glyphs(text)
    if not found:
        return None
    ranked = sorted(found.items(), key=lambda kv: (-kv[1], kv[0]))
    named = ", ".join(f"U+{c:04X}x{n}" for c, n in ranked[:6])
    first = min(text.index(chr(c)) for c, _ in ranked)
    context = text[max(0, first - 20):first + 20].replace("\n", " ")
    return (f"{sum(found.values())} unmapped glyph(s): {named}"
            f"{' ...' if len(ranked) > 6 else ''} — {context!r}")


# --------------------------------------------------------------------------
# The registry. Adding a detector is one entry here -- it does not touch
# PageText, DocText, the CLI, or any existing test.
# --------------------------------------------------------------------------

# Each detector brings its own one-line explanation, so a report never has to
# guess which corruption it is describing -- the wording was wrong for exactly
# one release of this module, saying "2-D structure was flattened" on a page
# where only letter-spacing had fired.
_DETECTORS = (
    ("letter-spaced", _letter_spacing,
     "one glyph per text run — `C o m p u t e r`"),
    ("shredded-lines", _shredded_lines,
     "a 2-D layout flattened into a column of fragments — a matrix, a stacked "
     "fraction, a `cases` brace"),
    ("vertical-letter-spaced", _vertical_letter_spacing,
     "one letter per line — a rotated label extracted downwards, `C/o/n/t/r/o/l`"),
    ("unmapped-glyphs", _unmapped,
     "a glyph the extractor could not map to Unicode — a big delimiter, Greek "
     "letter or ligature reaching the reader as an empty box; alone among "
     "these signals, the page image still carries it"),
)

NAMES = tuple(name for name, _, _ in _DETECTORS)
WHY = {name: why for name, _, why in _DETECTORS}


def signals(text: str) -> tuple[Signal, ...]:
    """Run every detector. Always returns one Signal per detector."""
    out = []
    for name, detect, _why in _DETECTORS:
        detail = detect(text) if text else None
        out.append(Signal(name=name, fired=detail is not None, detail=detail or ""))
    return tuple(out)


def classify(page_signals: tuple[Signal, ...]) -> str:
    """A page is suspect if ANY detector fired.

    An OR, never an average and never an AND. The two shipped detectors
    co-fire on only 49 of 463 flagged pages across the corpus -- they catch
    unrelated corruptions, so an AND would find almost nothing and a blended
    score would hide the one thing a reviewer can act on: which one fired.
    """
    return SUSPECT if any(s.fired for s in page_signals) else INTACT
