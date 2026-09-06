#!/usr/bin/env python3
"""Check that every relative Markdown link under this course resolves on disk.

AUTOMATION -- never submitted.

    ./check_links.py              check every .md under content/cpsc_462/
    ./check_links.py path.md ...  check only the files named

Exit status is 1 if any link is broken, so this can gate a commit.

WHY THIS EXISTS
    A broken link in prompt.md is silent: nothing renders it, nothing builds it,
    and the next reader just follows a path that is not there. Eyeballing a link
    table does not catch a renamed folder. This does.

WHAT COUNTS AS A LINK
    Inline links  [text](target)  and image links  ![alt](target).
    A target may be angle-bracketed --  [text](<a (b).pdf>)  -- which is the
    ONLY way to write a target containing spaces or parentheses. Bare targets
    with parentheses in them are reported as ambiguous rather than resolved,
    because the regex genuinely cannot tell where such a target ends.

WHAT IS SKIPPED
    http://, https://, mailto:, and pure #anchors -- nothing on disk to check.
    Fenced code blocks and inline `code spans`, because a link written inside
    one is not a link: it renders as literal text. Documentation that shows the
    WRONG way to write a link -- as this course's findings.md does -- would
    otherwise be reported for the very mistake it is warning about.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
COURSE = HERE.parent

# [text](...) / ![alt](...) -- everything up to the first ")". Deliberately
# permissive: the destination is classified afterwards, so a target that is
# malformed (an unbracketed space, a stray parenthesis) is REPORTED rather than
# silently skipped. A regex that only matched well-formed links would quietly
# ignore exactly the mistake this script exists to catch.
# The <...> branch comes FIRST so a correctly bracketed target containing a
# ")" -- <a (b).pdf> -- is not truncated at that ")".
LINK_RE = re.compile(r"!?\[[^\]]*\]\((\s*<[^>]*>\s*|[^)]*)\)?")

# [text](<a (b).pdf>) -- the only correct way to write a target with parens.
ANGLE_RE = re.compile(r"^\s*<([^>]*)>\s*$")
# [text](foo.pdf "Title") -- a bare target with an optional quoted title.
BARE_RE = re.compile(r"^\s*(\S+)(?:\s+\"[^\"]*\")?\s*$")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "ftp://", "#")

FENCE_RE = re.compile(r"^\s*(```|~~~)")
# One or more backticks, then the shortest run up to the same number again.
CODE_SPAN_RE = re.compile(r"(`+)(?:(?!\1).)*?\1")


def links_in(path: Path):
    """Yield (line_no, target, kind) where kind is angle / bare / malformed."""
    text = path.read_text(encoding="utf-8", errors="replace")
    in_fence = False
    for n, raw in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # Blank out inline code spans, keeping the line length so column-free
        # reporting stays honest and nested brackets cannot leak out.
        line = CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), raw)
        for m in LINK_RE.finditer(line):
            inner = m.group(1)
            if not inner.strip():
                continue
            angle = ANGLE_RE.match(inner)
            if angle:
                yield n, angle.group(1), "angle"
                continue
            bare = BARE_RE.match(inner)
            if bare:
                yield n, bare.group(1), "bare"
                continue
            # Whitespace with no quoted title, or an unbalanced paren: this is
            # not a valid inline link at all and needs <angle brackets>.
            yield n, inner.strip(), "malformed"


def main(argv: list[str]) -> int:
    if argv:
        files = [Path(a).resolve() for a in argv]
    else:
        files = sorted(p for p in COURSE.rglob("*.md") if ".git" not in p.parts)
    if not files:
        print("no .md files to check")
        return 0

    broken, ambiguous, checked = [], [], 0

    for f in files:
        for n, target, kind in links_in(f):
            if target.startswith(SKIP_PREFIXES):
                continue
            if kind == "malformed":
                checked += 1
                ambiguous.append((f, n, target))
                continue
            # Strip a trailing #anchor -- it addresses a heading, not a file.
            clean = unquote(target.split("#", 1)[0])
            if not clean:
                continue
            resolved = (f.parent / clean).resolve()
            checked += 1
            if not resolved.exists():
                broken.append((f, n, target, resolved))

    rel = lambda p: p.relative_to(COURSE.parent.parent) if COURSE.parent.parent in p.parents else p  # noqa: E731

    for f, n, target, resolved in broken:
        print(f"BROKEN  {rel(f)}:{n}  ->  {target}")
        print(f"        resolves to {resolved}")
    for f, n, target in ambiguous:
        print(f"AMBIG   {rel(f)}:{n}  ->  {target}   (wrap in <angle brackets>)")

    print(f"\n{checked} relative link(s) checked in {len(files)} file(s); "
          f"{len(broken)} broken, {len(ambiguous)} ambiguous.")
    return 1 if broken or ambiguous else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
