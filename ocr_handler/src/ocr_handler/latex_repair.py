"""Repair the LaTeX an equation model emits -- and refuse the repairs that lie.

UniMERNet's greedy decoder emits *syntactically* valid LaTeX almost always
(measured: 43 of 44 raw outputs compiled under tectonic). What it gets wrong is
*structure* -- a dropped brace, a `\\left` with no `\\right`, an `array` that
never ends. That is what this module fixes, and it fixes nothing else.

Derived from MinerU's `mineru/model/mfr/utils.py`, the post-processor MinerU
applies to every UniMERNet generation. Most of that file was found to be
actively destructive on this project's own recorded output, so the behaviour is
re-derived from its documented rules rather than copied, and every rule that
changed *meaning* rather than formatting was dropped or corrected. Rule-by-rule
audit with the measurements: docs/plans/latex-repair-and-validity.md § 2.
Headline: over the 44 recorded UniMERNet outputs in `tmp/eqocr/sweep.json`,
upstream changed 4 -- and **all four changes were damage**, one of them
deleting a `\\rightarrow` outright.

--------------------------------------------------------------------------
LICENCE -- what applies, and what is owed
--------------------------------------------------------------------------
Upstream: MinerU, `mineru/model/mfr/utils.py`,
`Copyright (c) Opendatalab. All rights reserved.`
https://github.com/opendatalab/MinerU -- licence text in its `LICENSE.md`.

MinerU is **not plain Apache-2.0.** It is the "MinerU Open Source License" =
Apache License 2.0 *plus four additional terms* (read in full 2026-09-06):
(1) a separate commercial licence is required *before* continued use once you
and your affiliates, consolidated, exceed 100 million MAU or USD 20 million
monthly revenue; (2) providing **online services to third parties** based on
MinerU obliges you to say so clearly and prominently, in the interface or in
public documentation; (3) breach of 1 or 2 terminates the licence and every
right under it **automatically, with no notice**; (4) definitions of
"Affiliates" and "Control".

Determination for this project: vendoring is permitted. `electrical_notes` is
one person's coursework -- term 1's thresholds are not in play and no online
service is provided, so term 2 does not attach. Owed under Apache-2.0 § 4 and
discharged here: the copyright notice above, a statement that the file was
changed and how (this docstring plus the audit), and a pointer to the licence.

⚠ The additional terms **travel with this file** and with anything derived from
it. `docs/research/mineru-teardown.md` § 7.4 calls the upstream file
"licence-clean"; § 6.1 of that document gets the detail right and the summary
is the part that is wrong. Term 3 is self-executing, so if this repository ever
becomes a hosted service, term 2's attribution stops being politeness.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

# Structural primitives. `validity.py` imports these to REPORT the counts
# before anything is repaired: a string that needs heavy repair is itself
# evidence about the reading, and silently fixing it destroys that evidence.
#
# `(?![a-zA-Z])` is the whole ballgame. Upstream's COUNT patterns have it; its
# delimiter-REPAIR patterns are `(\\left)(\S*)`/`(\\right)(\S*)`, which match
# `\lefteqn`, `\leftarrow`, `\rightarrow`, `\rightharpoonup` and rewrite them to
# `\left.`/`\right.` -- the counts then disagree and upstream's strip-everything
# branch deletes them. Measured on a real output in this repo:
# `{ \rightarrow \chi[n] = ...` came back as `{  \chi[n] = ...`.

_LEFT_RE = re.compile(r"\\left(?![a-zA-Z])")
_RIGHT_RE = re.compile(r"\\right(?![a-zA-Z])")
_BEGIN_RE = re.compile(r"\\begin\{([A-Za-z]+\*?)\}")
_END_RE = re.compile(r"\\end\{([A-Za-z]+\*?)\}")


def brace_balance(s: str) -> tuple[int, int]:
    """`(unclosed {, unopened })`, escape-aware. Skipping two characters at a
    backslash is equivalent to upstream's count-the-preceding-backslashes
    test: `\\{` is an escape, `\\\\{` leaves a real brace behind."""
    unclosed = unopened = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            unclosed += 1
        elif c == "}":
            if unclosed:
                unclosed -= 1
            else:
                unopened += 1
        i += 1
    return unclosed, unopened


def delimiter_balance(s: str) -> tuple[int, int]:
    """`(count of \\left, count of \\right)`, ignoring `\\leftarrow` etc."""
    return len(_LEFT_RE.findall(s)), len(_RIGHT_RE.findall(s))


def environment_balance(s: str) -> dict[str, tuple[int, int]]:
    """`{env: (begins, ends)}` for every environment whose counts disagree."""
    begins, ends = Counter(_BEGIN_RE.findall(s)), Counter(_END_RE.findall(s))
    return {e: (begins[e], ends[e]) for e in sorted(set(begins) | set(ends))
            if begins[e] != ends[e]}


@dataclass(frozen=True)
class Repair:
    """The repaired string, and one checkable note per change made."""

    text: str
    notes: tuple[str, ...] = ()


def drop_unmatched_braces(s: str) -> tuple[str, int]:
    """Delete `{` and `}` that have no partner. Upstream's algorithm, kept."""
    stack: list[int] = []
    unmatched: set[int] = set()
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            stack.append(i)
        elif c == "}":
            if stack:
                stack.pop()
            else:
                unmatched.add(i)
        i += 1
    unmatched.update(stack)
    if not unmatched:
        return s, 0
    return "".join(c for j, c in enumerate(s) if j not in unmatched), len(unmatched)


# Upstream's whitelist has 21 entries and omits `\langle`, `\rangle`, `\vert`,
# `\Vert`, `\lbrace`, `\rbrace`, `<`, `>`; anything off it is REPLACED by `.`,
# so `\left\langle x \right\rangle` -- an inner product, an expectation -- came
# back as `\left. x \right.`. This list is upstream's union what TeX actually
# accepts, and the repair below only ever *inserts* a `.` where nothing
# follows at all.
_CMD_DELIMS = (
    r"\lmoustache", r"\rmoustache", r"\updownarrow", r"\Updownarrow",
    r"\downarrow", r"\Downarrow", r"\backslash", r"\arrowvert", r"\Arrowvert",
    r"\bracevert", r"\uparrow", r"\Uparrow", r"\lfloor", r"\rfloor",
    r"\lbrace", r"\rbrace", r"\lbrack", r"\rbrack", r"\langle", r"\rangle",
    r"\lgroup", r"\rgroup", r"\lceil", r"\rceil", r"\Vert", r"\vert",
)
_DELIM_RE = re.compile(
    "(?:" + "|".join(re.escape(d) for d in _CMD_DELIMS) + r")(?![a-zA-Z])"
    r"|\\[{}|.]|[.()\[\]{}/|<>]"
)
_LR_CMD_RE = re.compile(r"\\(?:left|right)(?![a-zA-Z])")
_LR_STRIP_RE = re.compile(r"\\(?:left|right)(?![a-zA-Z])[ ]*\.?")


def pad_missing_delimiters(s: str) -> tuple[str, int]:
    """Give a bare `\\left`/`\\right` the `.` TeX requires. Inserts only."""
    out: list[str] = []
    pos = added = 0
    for m in _LR_CMD_RE.finditer(s):
        out.append(s[pos:m.end()])
        rest = s[m.end():]
        lead = len(rest) - len(rest.lstrip(" "))
        if not _DELIM_RE.match(rest, lead):
            out.append(".")
            added += 1
        pos = m.end()
    out.append(s[pos:])
    return "".join(out), added


def balance_delimiters(s: str, *, drop_unmatched: bool = False) -> tuple[str, str | None]:
    """Make the `\\left` and `\\right` counts agree.

    Upstream deletes **every** `\\left`/`\\right` when the counts differ, which
    restyles every delimiter in the expression to fix one. The default here
    pads the short side with an invisible `\\left.`/`\\right.`: it compiles and
    changes nothing that was read. `drop_unmatched=True` reproduces upstream's
    branch, and is off because a mismatch is more useful as a validity signal
    than as a silent edit.
    """
    n_left, n_right = delimiter_balance(s)
    if n_left == n_right:
        return s, None
    if drop_unmatched:
        return _LR_STRIP_RE.sub("", s), f"dropped all delimiters ({n_left}/{n_right})"
    if n_left > n_right:
        return s + r" \right." * (n_left - n_right), f"padded {n_left - n_right} \\right."
    return r"\left. " * (n_right - n_left) + s, f"padded {n_right - n_left} \\left."


# Upstream builds these as `r'\\begin\{' + env + r'\}'`, so for `align*` the `*`
# is a REGEX quantifier: the pattern reads `\begin{alig n*}` and can never match
# `\begin{align*}` -- the environment upstream most wants to fix is the one it
# silently cannot. `re.escape` is the whole fix.
_PADDABLE = ("array", "matrix", "pmatrix", "bmatrix", "vmatrix", "Bmatrix",
             "Vmatrix", "cases", "aligned", "gathered", "align", "align*")
_ARG_RE = {e: re.compile(r"\\begin\{" + re.escape(e) + r"\}\{([^}]*)\}")
           for e in _PADDABLE}


def pad_environments(s: str) -> tuple[str, list[str]]:
    """Insert the missing `\\begin`/`\\end` for the KaTeX-safe math envs."""
    notes: list[str] = []
    balance = environment_balance(s)
    for env in _PADDABLE:
        if env not in balance:
            continue
        begins, ends = balance[env]
        if ends > begins:
            m = _ARG_RE[env].search(s)
            arg = "{" + m.group(1) + "}" if m else ("{c}" if env == "array" else "")
            s = ("\\begin{" + env + "}" + arg + " ") * (ends - begins) + s
            notes.append(f"opened {ends - begins} {env}")
        else:
            s = s + (" \\end{" + env + "}") * (begins - ends)
            notes.append(f"closed {begins - ends} {env}")
    return s, notes


# Upstream's `remove_up_commands` strips `up` from `\up<anything>` unless the
# remainder is in {"arrow", "downarrow", "lus", "silon"} -- a suffix guess, not
# a command list. It turns `\upharpoonright` (a real relation) into
# `\harpoonright` and `\upuparrows` into `\uparrows`, neither a command at all.
# Naming the upright-Greek set is exact. Upright -> italic is a formatting
# change, taken because `upgreek` is rarely loaded downstream and the
# alternative is a document that will not build.
_GREEK = ("varepsilon", "varsigma", "vartheta", "epsilon", "upsilon", "lambda",
          "varphi", "omega", "alpha", "delta", "gamma", "kappa", "sigma",
          "theta", "varpi", "varrho", "beta", "iota", "zeta", "chi", "eta",
          "phi", "psi", "rho", "tau", "mu", "nu", "xi", "pi")
_UPGREEK_RE = re.compile(r"\\up(" + "|".join(_GREEK) + r")(?![a-zA-Z])")

# Wrappers carrying no mathematical content. `\textsubscript` was on upstream's
# list and is NOT here -- deleting it turns `H\textsubscript{2}O` into `H{2}O`,
# a different molecule -- so it is remapped below. `\textcent` was on it too;
# deleting a currency symbol is a content edit, so it is left alone.
_STRIP_RE = re.compile(
    r"\\(?:lefteqn|boldmath|ensuremath|centering|emph|textsl|protect|null|sides)"
    r"(?![a-zA-Z])")

# The audited substitutions: every one is formatting-preserving, and the ones
# that changed meaning are named in the plan doc with the reason they went.
# `(?![a-zA-Z])` on all of them -- upstream has no word boundary anywhere, so
# `\Barbell` became `\hatbell` and `\slashed{D}`, the Feynman slash, `/ed{D}`.
#
# ⚠ Upstream line 282 is `\Bar` -> `\hat`. `\Bar{x}` is x-bar, a MEAN; `\hat{x}`
# is x-hat, an ESTIMATE. Confirmed by running upstream: `\Bar{x} =
# \frac{1}{n}\sum x_i` came back as `\hat{x} = \frac{1}{n}\sum x_i`. In the
# statistics and DSP material this project exists to read, that is a wrong
# answer that renders beautifully. `\bar` is the fix.
_SUBSTITUTIONS = tuple((re.compile(p), r, n) for p, r, n in (
    (r"\\Bar(?![a-zA-Z])", r"\\bar", r"\Bar"),
    (r"\\Hat(?![a-zA-Z])", r"\\hat", r"\Hat"),
    (r"\\Tilde(?![a-zA-Z])", r"\\tilde", r"\Tilde"),
    (r"\\Dot(?![a-zA-Z])", r"\\dot", r"\Dot"),
    (r"\\underbar(?![a-zA-Z])", r"\\underline", r"\underbar"),
    (r"\\slash(?![a-zA-Z])", "/", r"\slash"),
    (r"\\textunderscore(?![a-zA-Z])", r"\\_", r"\textunderscore"),
    (r"\\textsubscript(?![a-zA-Z])", "_", r"\textsubscript"),
    (r"\\vDash(?![a-zA-Z])", r"\\models", r"\vDash"),
    (r"\\sq(?![a-zA-Z])\s+\\sqcup(?![a-zA-Z])", r"\\square", r"\sq \sqcup"),
    (r"\\up(?= )", "\\\\", r"\up "),
    (r"\\textperthousand(?![a-zA-Z])", "\u2030", r"\textperthousand"),
    (r"\\copyright(?![a-zA-Z])", "\u00a9", r"\copyright"),
    (r"\\sun(?![a-zA-Z])", "\u2609", r"\sun"),
    (r"\\fint(?![a-zA-Z])", "\u2a0f", r"\fint"),
))

# Upstream's `process_latex` inserts a space after any backslash whose next
# character is neither in `#$%&~_^|\{}` nor the start of a two-letter command.
# TeX's one-character SPACING commands are neither, so `\,` became `\ ,`: a thin
# space turned into a space plus a literal comma inside the mathematics.
# Measured firing on 2 of the 44 recorded outputs. Narrowed to digits, the only
# case where `\<char>` is certainly not a command.
_STRAY_BACKSLASH_RE = re.compile(r"\\(?=\d)")

# `\qquad` marks a deliberately blank region for `ink.py`, so it must survive
# tokenisation intact. `(?![A-Za-z\s])`, not upstream's `(?!\s)`: `\qquadx` is
# somebody else's command, not `\qquad` plus an `x`.
_QQUAD_RE = re.compile(r"\\qquad(?![A-Za-z\s])")


def normalise_commands(s: str) -> tuple[str, list[str]]:
    """Upright Greek, content-free wrappers, and the audited substitutions."""
    notes: list[str] = []
    out, n = _UPGREEK_RE.subn(r"\\\1", s)
    if n:
        notes.append(f"{n} upright-Greek command(s) mapped to italic")
    out, n = _STRIP_RE.subn("", out)
    if n:
        notes.append(f"{n} content-free wrapper(s) removed")
    for pattern, replacement, name in _SUBSTITUTIONS:
        out, n = pattern.subn(replacement, out)
        if n:
            notes.append(f"{n}x {name}")
    return out, notes


def repair(s: str, *, drop_unmatched_delimiters: bool = False) -> Repair:
    """Repair one model-generated expression, reporting every change made."""
    notes: list[str] = []
    out, dropped = drop_unmatched_braces(s)
    if dropped:
        notes.append(f"dropped {dropped} unmatched brace(s)")
    out, added = pad_missing_delimiters(out)
    if added:
        notes.append(f"gave {added} bare \\left/\\right a `.` delimiter")
    out, note = balance_delimiters(out, drop_unmatched=drop_unmatched_delimiters)
    if note:
        notes.append(note)
    out, env_notes = pad_environments(out)
    notes.extend(env_notes)
    out, cmd_notes = normalise_commands(out)
    notes.extend(cmd_notes)
    out, n = _STRAY_BACKSLASH_RE.subn("\\\\ ", out)
    if n:
        notes.append(f"spaced {n} backslash(es) before a digit")
    out, n = _QQUAD_RE.subn(r"\\qquad ", out)
    if n:
        notes.append(f"spaced {n} \\qquad")
    stripped = out.rstrip("\\")
    if stripped != out:
        notes.append("stripped trailing backslash(es)")
    return Repair(text=stripped, notes=tuple(notes))
