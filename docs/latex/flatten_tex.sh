#!/usr/bin/env bash
# flatten_tex.sh — inline every \input so one .tex stands alone. For Overleaf.
#
# AUTOMATION -- never submitted, and never referenced from the output.
#
#   docs/latex/flatten_tex.sh content/cesc_470/hw/hw01/p08_target_clock_rate.tex
#   docs/latex/flatten_tex.sh content/cesc_470/hw/hw01            whole assignment
#   docs/latex/flatten_tex.sh content/cesc_470/hw/hw01 -o /tmp/overleaf
#
# WHY THIS EXISTS
#   Local files input the shared preamble by relative path:
#       \input{../../../../docs/latex/coursework_preamble.tex}
#   That is right for this repo -- one preamble, no drift. It is IMPOSSIBLE in
#   Overleaf: a project is self-contained, so a path climbing above the project
#   root cannot resolve, and the compile dies with
#       LaTeX Error: File `../../../../docs/latex/coursework_preamble.tex' not found.
#   Uploading the preamble by hand works but has to be redone per project and
#   re-synced whenever the shared file changes.
#
#   So: keep \input for local work, flatten on the way out.
#
# WHAT IT DOES
#   - Recursively inlines \input{...} / \include{...} (depth-limited).
#   - Strips comment-only lines that name a tool, script, or repo path, because
#     the doctrine forbids tooling references in a submitted document.
#   - Leaves everything else byte-for-byte alone.
#
# Output goes to <dir>/overleaf/ by default, which is gitignored.

set -uo pipefail

MAX_DEPTH=8
OUT=""
TARGET=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -o|--out) OUT="$2"; shift 2 ;;
        -h|--help) sed -n '2,32p' "$0"; exit 0 ;;
        -*) echo "unknown option: $1" >&2; exit 2 ;;
        *) TARGET="${1%/}"; shift ;;
    esac
done
[[ -n "$TARGET" ]] || { echo "usage: flatten_tex.sh <file.tex|dir> [-o OUTDIR]" >&2; exit 2; }

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

# Comment-only lines mentioning any of these are dropped from the output.
# Matches the packaging guard used by the lab tooling: a submitted document must
# not name the scripts that produced it.
TOOLING_RE='(build_tex\.sh|flatten_tex\.sh|new_tex\.sh|make_submission|strip_comments|check_artifacts|course_text\.py|prepare_corpus|ocr-handler|docs/latex/|docs/directives/|reference_docs/|tools/)'

# inline <file> <depth> -- emit file with \input/\include resolved.
# depth 0 is the file the user named; depth >0 is an inlined preamble.
#
# Comment handling differs by depth, on purpose. An inlined preamble's comments
# are entirely about THIS repo's toolchain -- paths, doctrine, build commands --
# none of which mean anything in Overleaf. Stripping them line-by-line left
# sentences cut in half, so at depth >0 every comment-only line goes. The user's
# own file (depth 0) keeps its comments, minus any that name tooling.
inline() {
    local f="$1" depth="$2" dir
    if (( depth > MAX_DEPTH )); then
        echo "% [flatten: max depth reached at ${f}]" ; return
    fi
    dir="$(dirname "$f")"
    # Read with IFS= and -r so whitespace and backslashes survive intact.
    while IFS= read -r line || [[ -n "$line" ]]; do
        # An \input on a line of its own (optionally indented). Anything else --
        # \input mid-sentence, or inside a comment -- is passed through, since
        # rewriting it could change meaning.
        if [[ "$line" =~ ^[[:space:]]*\\(input|include)\{([^}]+)\}[[:space:]]*$ ]]; then
            local target="${BASH_REMATCH[2]}"
            [[ "$target" == *.tex ]] || target="${target}.tex"
            local resolved="${dir}/${target}"
            if [[ -f "$resolved" ]]; then
                printf '%% ─── inlined: %s ───\n' "$(basename "$target")"
                inline "$resolved" $((depth + 1))
                printf '%% ─── end inlined ───\n'
            else
                echo "warning: cannot resolve ${target} from ${dir}" >&2
                printf '%s\n' "$line"
            fi
            continue
        fi
        # Comment-only lines. A trailing comment after real content is left
        # alone -- removing it could change spacing.
        if [[ "$line" =~ ^[[:space:]]*% ]]; then
            # Inlined preamble: drop all of them (see the note above inline()).
            (( depth > 0 )) && continue
            # User's own file: drop only those naming tooling.
            [[ "$line" =~ $TOOLING_RE ]] && continue
        fi
        printf '%s\n' "$line"
    done < "$f"
}

flatten_one() {
    local src="$1" outdir="$2" dest
    mkdir -p "$outdir"
    dest="${outdir}/$(basename "$src")"
    {
        # Deliberately NO repo path here. Naming the source as
        # "content/<course>/labs_and_projects/..." would put a repo path into a
        # document that may be submitted -- the exact thing the no-tooling rule
        # forbids, emitted by the tool that enforces it elsewhere. The basename
        # is enough to find the source and carries no path.
        printf '%% Self-contained: preamble inlined, no external \\input.\n'
        printf '%% Generated copy of %s -- edit the original, not this.\n\n' "$(basename "$src")"
        inline "$src" 0
    } > "$dest"

    # A leaked \input means the output is NOT self-contained and will fail in
    # Overleaf exactly as the original did. Fail loudly rather than ship it.
    if grep -qE '^[[:space:]]*\\(input|include)\{' "$dest"; then
        echo "  FAIL  $(basename "$src") -- unresolved \\input remains:" >&2
        grep -nE '^[[:space:]]*\\(input|include)\{' "$dest" | sed 's/^/        /' >&2
        return 1
    fi
    printf '  %-46s -> %s (%s KB)\n' "$(basename "$src")" "$dest" \
        "$(( $(stat -c%s "$dest") / 1024 ))"
}

if [[ -f "$TARGET" ]]; then
    FILES=("$TARGET"); DEFAULT_OUT="$(dirname "$TARGET")/overleaf"
elif [[ -d "$TARGET" ]]; then
    mapfile -t FILES < <(find "$TARGET" -maxdepth 1 -name '*.tex' | sort)
    DEFAULT_OUT="$TARGET/overleaf"
else
    echo "error: no such file or folder: $TARGET" >&2; exit 1
fi
[[ ${#FILES[@]} -gt 0 ]] || { echo "no .tex found under $TARGET"; exit 0; }
OUT="${OUT:-$DEFAULT_OUT}"

fails=0
for f in "${FILES[@]}"; do
    flatten_one "$f" "$OUT" || fails=$((fails + 1))
done

echo
if (( fails )); then
    echo "$fails file(s) failed to flatten." >&2; exit 1
fi
echo "Self-contained copies in: $OUT"
echo "Upload or paste one into Overleaf -- it needs no other file."
