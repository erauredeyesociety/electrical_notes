#!/usr/bin/env python3
"""Strip comments and docstrings from Python source for submission.

AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.

Working copies of the lab code carry heavy explanatory comments, which is
what makes them useful to us later. That density is not what you want to hand
in. This produces a clean copy: same code, same behaviour, no commentary.

NEVER mutates the working tree. Reads a file, returns/writes stripped text.

Uses tokenize, not regex. Regex cannot strip Python comments safely -- a '#'
inside a string literal is not a comment:

    url = "https://example.com/#anchor"    # regex would truncate this
    css = "color: #fff"

tokenize knows the difference. So does this.

KEPT BY DEFAULT (see --keep / --strip-all):
  - shebang and encoding lines (functional, not commentary)
  - DEVIATION FROM HANDOUT blocks -- honest disclosure that handout code was
    modified. Dropping them silently ships altered code as if unaltered.
  - the ERAU ID marker

    tools/strip_comments.py path/to/file.py            # to stdout
    tools/strip_comments.py src/ -o /tmp/clean         # whole tree
    tools/strip_comments.py file.py --strip-all        # keep nothing
"""

import argparse
import ast
import io
import re
import shutil
import sys
import tokenize
from pathlib import Path

# Comments matching these survive together with their whole contiguous block.
# Used for disclosure, where the reasoning has to travel with the marker.
BLOCK_KEEP = [
    r"DEVIATION FROM HANDOUT",
]

# Comments matching these survive as a single line only. Markers whose value
# is the marker itself, not the explanation around it.
LINE_KEEP = [
    r"last 4 digits",
]

DEFAULT_KEEP = BLOCK_KEEP + LINE_KEEP

# Functional first-lines that are not commentary.
SHEBANG = re.compile(r"^#!")
ENCODING = re.compile(r"^#.*coding[:=]")


# Decorators whose functions use the docstring as user-visible text rather
# than as commentary. Typer and Click build `--help` from it, so removing it
# silently degrades the CLI -- and the Lab 0 handout tells students to run
# `dsp26 --help`, so that text is part of what the lab demonstrates.
FUNCTIONAL_DOCSTRING_DECORATORS = ("command", "callback")


def _decorator_names(node):
    """Every dotted name appearing in a node's decorator list."""
    names = []
    for dec in getattr(node, "decorator_list", []):
        target = dec.func if isinstance(dec, ast.Call) else dec
        while isinstance(target, ast.Attribute):
            names.append(target.attr)
            target = target.value
        if isinstance(target, ast.Name):
            names.append(target.id)
    return names


def _docstring_line_spans(source: str) -> set:
    """Line numbers (1-based) occupied by docstrings.

    Only the first statement of a module, class, or function counts -- a bare
    string used as a value is an expression, not a docstring, and is left
    alone. Docstrings that a decorator turns into user-visible text are kept.
    """
    spans = set()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return spans

    holders = (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
    for node in ast.walk(tree):
        if not isinstance(node, holders):
            continue
        body = getattr(node, "body", None)
        if not body:
            continue
        first = body[0]
        if (
            isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)
        ):
            # Never strip a docstring that is the only statement -- removing it
            # would leave an empty block and a SyntaxError.
            if len(body) == 1:
                continue
            # Keep docstrings that are functional rather than commentary.
            if any(d in FUNCTIONAL_DOCSTRING_DECORATORS
                   for d in _decorator_names(node)):
                continue
            spans.update(range(first.lineno, (first.end_lineno or first.lineno) + 1))
    return spans


def strip(source: str, keep_patterns=None, strip_all=False,
          keep_docstrings=False) -> str:
    """Return source with comments and docstrings removed."""
    if strip_all:
        keep, block_keep = [], []
    elif keep_patterns:
        keep = [re.compile(p) for p in keep_patterns]
        block_keep = [re.compile(p) for p in BLOCK_KEEP]
    else:
        keep = [re.compile(p) for p in DEFAULT_KEEP]
        block_keep = [re.compile(p) for p in BLOCK_KEEP]

    # Collect every comment token first, so keep-decisions can consider a
    # comment's neighbours rather than each line in isolation.
    # str.splitlines() ALSO breaks on U+000B, U+000C (form feed), U+001C-1E,
    # U+0085, U+2028 and U+2029, but tokenize breaks only on "\n". Mixing the
    # two desynchronises line numbers, so cuts land on the wrong lines --
    # silently deleting a DEVIATION disclosure, leaking comments, or
    # truncating a string. Form feeds appear as section separators in real
    # source, and U+2028 rides along in copy-paste from PDF handouts, which is
    # exactly how handout code reaches us. Split on "\n" everywhere.
    comments = []   # (line, col, text, is_own_line)
    try:
        src_lines = source.split("\n")
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            if tok.type != tokenize.COMMENT:
                continue
            line_no, col = tok.start
            before = src_lines[line_no - 1][:col].strip() if line_no <= len(src_lines) else ""
            comments.append((line_no, col, tok.string, before == ""))
    except (tokenize.TokenError, IndentationError):
        # Unparseable: return unchanged rather than emit broken code.
        return source

    # A keep-match preserves its whole contiguous block of own-line comments,
    # not just the matching line. A DEVIATION marker truncated to its first
    # line would disclose that handout code changed while dropping the reason,
    # which is worse than not marking it at all.
    keep_lines = set()
    own_line = [c for c in comments if c[3]]
    for idx, (line_no, col, text, _) in enumerate(own_line):
        if not any(p.search(text) for p in block_keep):
            continue
        keep_lines.add(line_no)
        # walk backwards and forwards over directly adjacent comment lines
        for step in (-1, 1):
            j, expect = idx + step, line_no + step
            while 0 <= j < len(own_line) and own_line[j][0] == expect and own_line[j][1] == col:
                keep_lines.add(expect)
                j += step
                expect += step

    cuts = {}
    for line_no, col, text, _ in comments:
        if SHEBANG.match(text) and line_no == 1:
            continue
        if ENCODING.match(text) and line_no <= 2:
            continue
        if line_no in keep_lines or any(p.search(text) for p in keep):
            continue
        # Column where the comment starts, so trailing comments can be cut
        # without disturbing the code before them.
        cuts.setdefault(line_no, col)

    doc_lines = set() if keep_docstrings else _docstring_line_spans(source)

    out = []
    for i, line in enumerate(source.split("\n"), start=1):
        if i in doc_lines:
            continue
        if i in cuts:
            line = line[: cuts[i]].rstrip()
            if not line:
                continue          # comment-only line: drop it entirely
        out.append(line.rstrip())

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n\n", text)      # collapse blank-line runs
    text = re.sub(r"\(\n{2,}", "(\n", text)       # tidy after removals
    return text.strip("\n") + "\n"


# Anything naming our tooling must never reach a submitted document.
TOOLING_REF = re.compile(
    r"tools/|make_submission|render_reports|strip_comments|check_artifacts|"
    r"check_inputs|MPLBACKEND|uv run|reference_docs|labs_and_projects"
)


def strip_tex(source: str) -> str:
    """Remove comment-only lines from LaTeX source.

    Deliberately conservative: only lines whose first non-whitespace character
    is an unescaped '%' are removed. TRAILING comments are left alone, because
    in LaTeX a '%' at end of line suppresses the following space and removing
    it changes the output.

    Deleting a comment-only line is safe -- TeX consumes such lines entirely,
    so removing it produces the same result and does not introduce the blank
    line that would start a new paragraph.
    """
    out = []
    for line in source.split("\n"):
        stripped_line = line.lstrip()
        if stripped_line.startswith("%"):
            continue
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.lstrip("\n")


def find_tooling_refs(text: str):
    """Lines mentioning our automation. Used to keep it out of submissions."""
    return [
        (i, ln) for i, ln in enumerate(text.split("\n"), start=1)
        if TOOLING_REF.search(ln)
    ]


def _verify(original: str, stripped: str, name: str) -> bool:
    """Confirm the stripped file still parses and is semantically the same.

    Compares ASTs with docstrings removed. This is the check that makes the
    tool safe to point at code destined for submission.
    """
    try:
        a = ast.parse(original)
        b = ast.parse(stripped)
    except SyntaxError as e:
        print(f"  ERROR {name}: stripped output does not parse: {e}", file=sys.stderr)
        return False

    def norm(tree):
        for node in ast.walk(tree):
            body = getattr(node, "body", None)
            if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef,
                                 ast.AsyncFunctionDef)) and body:
                first = body[0]
                if (isinstance(first, ast.Expr)
                        and isinstance(first.value, ast.Constant)
                        and isinstance(first.value.value, str)
                        and len(body) > 1):
                    node.body = body[1:]
        return ast.dump(tree)

    if norm(a) != norm(b):
        print(f"  ERROR {name}: stripping changed the code, not just comments",
              file=sys.stderr)
        return False

    # Comments carry no AST, so the comparison above cannot see a lost
    # disclosure. Check explicitly that every kept-pattern comment survived.
    for pat in BLOCK_KEEP + LINE_KEEP:
        rx = re.compile(pat)
        before = [ln.strip() for ln in original.split("\n") if rx.search(ln)]
        after = [ln.strip() for ln in stripped.split("\n") if rx.search(ln)]
        if len(before) != len(after):
            print(f"  ERROR {name}: stripping lost a '{pat}' comment "
                  f"({len(before)} -> {len(after)})", file=sys.stderr)
            return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", type=Path, help="file or directory")
    ap.add_argument("-o", "--out", type=Path,
                    help="output dir (required for a directory); else stdout")
    ap.add_argument("--keep", action="append", default=None,
                    metavar="REGEX", help="extra comment pattern to preserve")
    ap.add_argument("--strip-all", action="store_true",
                    help="keep nothing, including DEVIATION markers (see docs)")
    ap.add_argument("--keep-docstrings", action="store_true",
                    help="remove comments only; leave all docstrings intact")
    args = ap.parse_args()

    keep = DEFAULT_KEEP + (args.keep or []) if args.keep else None

    if args.strip_all:
        print("WARNING: --strip-all removes DEVIATION FROM HANDOUT markers.",
              file=sys.stderr)
        print("         Modified handout code will ship with no disclosure.",
              file=sys.stderr)

    if args.path.is_file():
        src = args.path.read_text()
        if args.path.suffix == ".tex":
            out = strip_tex(src)
            if args.out:
                args.out.parent.mkdir(parents=True, exist_ok=True)
                args.out.write_text(out)
            else:
                sys.stdout.write(out)
            return 0
        out = strip(src, keep, args.strip_all, args.keep_docstrings)
        if not _verify(src, out, args.path.name):
            return 1
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(out)
        else:
            sys.stdout.write(out)
        return 0

    if not args.out:
        print("error: -o/--out is required for a directory", file=sys.stderr)
        return 2

    ok = True
    n = 0
    for src_path in sorted(args.path.rglob("*")):
        if any(part in {".venv", "__pycache__", ".git"} for part in src_path.parts):
            continue
        if not src_path.is_file():
            continue
        dst = args.out / src_path.relative_to(args.path)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src_path.suffix == ".tex":
            out = strip_tex(src_path.read_text())
            dst.write_text(out)
            n += 1
            continue
        if src_path.suffix == ".py":
            src = src_path.read_text()
            out = strip(src, keep, args.strip_all, args.keep_docstrings)
            if not _verify(src, out, str(src_path)):
                ok = False
                continue
            dst.write_text(out)
            before, after = len(src.splitlines()), len(out.splitlines())
            print(f"  {src_path.relative_to(args.path)}: {before} -> {after} lines")
            n += 1
        else:
            shutil.copy2(src_path, dst)

    print(f"\n{n} Python file(s) stripped into {args.out}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
