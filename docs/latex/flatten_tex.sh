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
#   - Strips the source's OVERLEAF marker block, which is true of the source and
#     FALSE of the copy -- the copy is the one that DOES compile there.
#   - Leaves everything else byte-for-byte alone.
#   - SKIPS a fragment -- a .tex with no \begin{document}, i.e. a macros file or
#     a tombstone. Flattening one produced a copy headed "Self-contained" that
#     cannot compile, sitting in the very folder a human is told to upload from.
#
# IT ALSO WARNS, non-fatally, about two things it cannot fix for you:
#   - a source with \input and no OVERLEAF marker. That marker is the whole fix
#     for this repo's most-repeated mistake: opening the obvious .tex, uploading
#     it, and getting "File ... not found". The doctrine said so all along, in a
#     document nobody has open at upload time.
#   - an output that still needs image files. Flattening inlines TEXT; an
#     \includegraphics points at a file Overleaf will not have, and dies there
#     the same way the missing preamble did. Upload the images too.
#
# Output goes to <dir>/overleaf/ by default, which is gitignored.

set -uo pipefail

MAX_DEPTH=8
OUT=""
TARGET=""
CHECK=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        -o|--out) OUT="$2"; shift 2 ;;
        -c|--check) CHECK=1; shift ;;
        -h|--help) sed -n '2,42p' "$0"; exit 0 ;;
        -*) echo "unknown option: $1" >&2; exit 2 ;;
        *) TARGET="${1%/}"; shift ;;
    esac
done
if [[ -z "$TARGET" ]]; then
    if (( CHECK )); then
        TARGET="content"          # --check with no target sweeps the whole corpus
    else
        echo "usage: flatten_tex.sh <file.tex|dir> [-o OUTDIR]" >&2
        echo "       flatten_tex.sh --check [dir]     verify copies are current" >&2
        exit 2
    fi
fi

SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

# Comment-only lines mentioning any of these are dropped from the output.
# Matches the packaging guard used by the lab tooling: a submitted document must
# not name the scripts that produced it.
#
# "Overleaf" is on the list for a second reason as well as that one. Every
# source now opens with an OVERLEAF marker block (see MARKER_RE below) saying
# "do not upload THIS file, upload the flattened copy". In the flattened copy
# that warning is not merely a tooling reference -- it is FALSE, because the
# flattened copy is the one that does compile there. So the block has to go,
# and every line of it names Overleaf or a repo path in order to be caught here.
TOOLING_RE='(build_tex\.sh|flatten_tex\.sh|new_tex\.sh|make_submission|strip_comments|check_artifacts|course_text\.py|prepare_corpus|ocr-handler|docs/latex/|docs/directives/|reference_docs/|tools/|[Oo]verleaf|OVERLEAF)'

# The marker a source file must carry so that whoever opens it is told, in the
# file itself, that it cannot be uploaded to Overleaf. Absence is warned about,
# not fatal -- see flatten_one().
MARKER_RE='^[[:space:]]*%.*OVERLEAF'

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

    # Does the SOURCE warn its own reader? This script only ever runs when
    # somebody already knows about the flatten step; the person who does not
    # know opens the .tex, uploads it, and gets "File ... not found". The only
    # thing in front of them at that moment is the file itself, so the file has
    # to carry the warning. Warn here because this is the one tool that walks
    # every source in an assignment -- run it and you find the unmarked ones.
    # Non-fatal on purpose: a missing comment must never block a real flatten.
    if grep -qE '^[[:space:]]*\\(input|include)\{' "$src" \
       && ! grep -qE "$MARKER_RE" "$src"; then
        echo "  WARN  $(basename "$src") -- source has \\input but no OVERLEAF marker comment." >&2
        unmarked=$((unmarked + 1))
    fi

    dest="${outdir}/$(basename "$src")"
    local tmp; tmp="$(mktemp "${TMPDIR:-/tmp}/flatten.XXXXXX")"
    {
        # Deliberately NO repo path here. Naming the source as
        # "content/<course>/labs_and_projects/..." would put a repo path into a
        # document that may be submitted -- the exact thing the no-tooling rule
        # forbids, emitted by the tool that enforces it elsewhere. The basename
        # is enough to find the source and carries no path.
        printf '%% Self-contained: preamble inlined, no external \\input.\n'
        printf '%% Generated copy of %s -- edit the original, not this.\n\n' "$(basename "$src")"
        inline "$src" 0
    } > "$tmp"

    # A FRAGMENT is not a document: no \begin{document}, so nothing can compile
    # it -- a macros file, or the superseded-preamble tombstone. Emitting one
    # put a file headed "Self-contained: preamble inlined" into overleaf/, the
    # one folder a human is pointed at with "upload this". Two files there, one
    # of which dies with "no legal \end found", is exactly the which-file-do-I-
    # upload confusion the marker block exists to end. Skip it, say why, and
    # delete any copy an earlier run left behind.
    # Non-comment \begin{document} only: the tombstone QUOTES the line it tells
    # you to write ("%   \begin{document}"), and a commented one compiles nothing.
    if ! grep -qE '^[^%]*\\begin\{document\}' "$tmp"; then
        rm -f "$tmp"
        if [[ -e "$dest" ]]; then
            rm -f "$dest"
            printf '  %-46s -> removed stale copy (fragment)\n' "$(basename "$src")"
        else
            printf '  %-46s -> skipped: fragment, no \\begin{document}\n' "$(basename "$src")"
        fi
        fragments=$((fragments + 1))
        return 0
    fi
    # mktemp makes the file 0600. Match the source's permissions instead, so a
    # regenerated copy is no less readable than the one it replaced.
    mv "$tmp" "$dest"
    chmod --reference="$src" "$dest" 2>/dev/null || chmod 644 "$dest"

    # A leaked \input means the output is NOT self-contained and will fail in
    # Overleaf exactly as the original did. Fail loudly rather than ship it.
    if grep -qE '^[[:space:]]*\\(input|include)\{' "$dest"; then
        echo "  FAIL  $(basename "$src") -- unresolved \\input remains:" >&2
        grep -nE '^[[:space:]]*\\(input|include)\{' "$dest" | sed 's/^/        /' >&2
        return 1
    fi
    printf '  %-46s -> %s (%s KB)\n' "$(basename "$src")" "$dest" \
        "$(( $(stat -c%s "$dest") / 1024 ))"
    written=$((written + 1))

    # Flattening inlines TEXT. An \includegraphics still points at a file that
    # is not in the Overleaf project, and the compile dies there the same way
    # the missing preamble did -- "Unable to load picture or PDF file". Say so
    # here, because this is where the "self-contained" claim is made.
    # Comments stripped first: "% \includegraphics" in prose is not a dependency,
    # and a NOTE naming a file the document never loads teaches people to ignore
    # NOTEs. Only a real, uncommented \includegraphics counts.
    local figs
    figs="$(sed -E 's/(^|[^\\])%.*/\1/' "$dest" \
            | grep -oE '\\includegraphics(\[[^]]*\])?\{[^}]*\}' \
            | sed -E 's/.*\{([^}]*)\}/        \1/' | sort -u)"
    if [[ -n "$figs" ]]; then
        echo "  NOTE  $(basename "$src") -- also upload its images; \\includegraphics is not inlined:" >&2
        printf '%s\n' "$figs" >&2
        withfigs=$((withfigs + 1))
    fi
}

# ---------------------------------------------------------------------------
# --check: is every committed overleaf/ copy still what the flattener would
# produce today?
#
# WHY THIS EXISTS. Editing a source and forgetting to re-flatten is SILENT. The
# stale copy still compiles, still looks right, and you submit last week's work
# with no error anywhere. That is worse than the "File not found" this script
# was written for, because that one at least tells you.
#
# It compares CONTENT, never timestamps: `touch` must not be able to make a
# stale copy look current. Three faults, all real, all found on the first run:
#   STALE   the source changed since the copy was generated
#   MISSING a document has no copy at all
#   ORPHAN  a copy whose source was renamed or deleted -- it sits there looking
#           uploadable forever, and nothing else would ever mention it
#
# Fragments are skipped for free: flatten_one refuses anything with no
# \begin{document}, so it never emits one and this never expects one.
check_freshness() {
    local root="$1" rc=0 dirs=0
    while IFS= read -r ov; do
        local asn; asn="$(dirname "$ov")"
        dirs=$((dirs + 1))
        local tmp; tmp="$(mktemp -d)"
        # Re-flatten with this same script, so the comparison can never drift
        # from what a real run produces. SELF is absolute: $0 is whatever path
        # the caller typed, and this function runs after `cd "$ROOT"`, so a
        # relative invocation (../../../docs/latex/flatten_tex.sh --check) would
        # no longer resolve -- and the failure is silent, reporting every copy
        # as an ORPHAN because nothing got regenerated to compare against.
        "$SELF" "$asn" -o "$tmp" >/dev/null 2>&1
        local n=0 bad=0
        for f in "$tmp"/*.tex; do
            [[ -e "$f" ]] || continue
            local b cur; b="$(basename "$f")"; cur="$ov/$b"
            n=$((n + 1))
            if [[ ! -f "$cur" ]]; then
                echo "  MISSING  $cur"; bad=1
            elif ! diff -q "$f" "$cur" >/dev/null 2>&1; then
                echo "  STALE    $cur"
                echo "           source changed since this was generated -- re-run:"
                echo "           docs/latex/flatten_tex.sh $asn"
                bad=1
            fi
        done
        for cur in "$ov"/*.tex; do
            [[ -e "$cur" ]] || continue
            local b; b="$(basename "$cur")"
            [[ -f "$tmp/$b" ]] || { echo "  ORPHAN   $cur (no source produces it)"; bad=1; }
        done
        rm -rf "$tmp"
        if (( bad )); then rc=3; else echo "  OK       $asn ($n/$n current)"; fi
    done < <(find "$root" -type d -name overleaf -not -path '*/.venv/*' | sort)

    if (( dirs == 0 )); then
        echo "no overleaf/ folders under $root -- nothing to check"
        return 0
    fi
    if (( rc )); then
        echo >&2
        echo "Stale or missing copies above. Uploading one submits work that does" >&2
        echo "not match the source, and nothing else would tell you." >&2
    fi
    return $rc
}

# --check is answered from overleaf/ folders, not from .tex files beside the
# target, so it must run BEFORE the collection guard below -- a directory whose
# only .tex files live in subfolders would otherwise exit "no .tex found".
if (( CHECK )); then
    check_freshness "$TARGET"
    exit $?
fi

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
unmarked=0
fragments=0
withfigs=0
written=0
for f in "${FILES[@]}"; do
    flatten_one "$f" "$OUT" || fails=$((fails + 1))
done

echo
if (( fails )); then
    echo "$fails file(s) failed to flatten." >&2; exit 1
fi
if (( written == 0 )); then
    # Everything was skipped. Saying "copies are in $OUT" when none were written
    # sends someone to an empty folder to look for a file that is not coming.
    echo "Nothing written: no document among the .tex files given."
    if (( fragments )); then
        echo "(${fragments} fragment(s): no \\begin{document}, so nothing to upload.)"
    fi
    exit 0
fi
echo "Self-contained copies in: $OUT"
# Say "no other file" only when that is true. One \includegraphics makes it a
# lie, and the operator finds out from Overleaf instead of from here.
if (( withfigs )); then
    echo "Upload or paste one into Overleaf -- no other .tex is needed, but the"
    echo "image files listed above must go up with it."
else
    echo "Upload or paste one into Overleaf -- it needs no other file."
fi
if (( fragments )); then
    echo "(${fragments} fragment(s) skipped: no \\begin{document}, so nothing to upload.)"
fi
if (( withfigs )); then
    echo "(${withfigs} file(s) also need their image files uploaded -- see NOTE above.)"
fi

# Advisory only. Exit status is unchanged: this reports a documentation gap in
# the sources, not a fault in the output above, which is correct either way.
if (( unmarked )); then
    {
        echo
        echo "WARNING: ${unmarked} source file(s) above carry no OVERLEAF marker comment."
        echo "         Whoever opens one of those has nothing telling them it cannot be"
        echo "         uploaded, and they will hit \"File ... not found\" -- twice, so far."
        echo "         Add the marker block to the top of each; the canonical text is in"
        echo "         docs/directives/coursework-solutions.md, section \"Overleaf needs a"
        echo "         flattened copy\". new_tex.sh emits it for every new file."
    } >&2
fi
