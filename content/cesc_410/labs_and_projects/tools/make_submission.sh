#!/usr/bin/env bash
# Build a submission zip containing ONLY lab code, with comments stripped.
#
# AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.
#
#   tools/make_submission.sh lab00 nelson-gatlin
#     -> lab00/dsp26-lab00-nelson-gatlin.zip
#
#   --figures         package the REPORT + FIGURES instead of code. Renders
#                     labNN/report.tex via tools/render_reports.sh, then zips
#                     the PDF, the .tex/.md source and the PNGs. Use when a
#                     lab asks for figures rather than code -- Lab 0 does.
#   --keep-comments   skip stripping (submit the working copy as-is)
#   --strip-all       also remove DEVIATION FROM HANDOUT markers (see below)
#
# Pipeline:
#   1. copy dsp26/ to a staging dir  (the working tree is never modified)
#   2. strip comments and docstrings via tools/strip_comments.py
#   3. prepend a header block to each .py naming course/lab/author/date
#   4. zip, print the file list, delete staging
#
# READ THIS BEFORE USING: reference_docs/submission_requirements.md
# What each lab actually requires is NOT uniform -- some labs may want only
# figures, others code, others a report. Confirm per lab.

set -euo pipefail

STRIP=1
STRIP_ALL=0
FIGURES=0
ARGS=()
for a in "$@"; do
    case "$a" in
        --figures)       FIGURES=1 ;;
        --keep-comments) STRIP=0 ;;
        --strip-all)     STRIP_ALL=1 ;;
        -*) echo "unknown option: $a" >&2; exit 2 ;;
        *)  ARGS+=("$a") ;;
    esac
done

if [[ ${#ARGS[@]} -ne 2 ]]; then
    cat >&2 <<'EOF'
usage: make_submission.sh [--figures] [--keep-comments] [--strip-all] <lab> <lastname-firstname>
  code:            make_submission.sh lab01 nelson-gatlin
  report+figures:  make_submission.sh lab00 nelson-gatlin --figures
EOF
    exit 2
fi

LAB="${ARGS[0]%/}"
WHO="${ARGS[1]}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

[[ -d "$LAB"   ]] || { echo "error: no such lab folder: $LAB" >&2; exit 1; }
[[ -d "dsp26" ]] || { echo "error: dsp26/ not found in $ROOT" >&2; exit 1; }

LABNUM="${LAB#lab}"; LABNUM="${LABNUM#0}"; LABNUM="${LABNUM:-0}"
DATE="$(date +%Y-%m-%d)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

# ===========================================================================
# --figures: report + images, no code. What Lab 0 asks for.
# ===========================================================================
if [[ $FIGURES -eq 1 ]]; then
    FIGS="$LAB/figs"
    [[ -d "$FIGS" ]] || {
        echo "error: $FIGS not found. Generate figures first:" >&2
        echo "  cd dsp26 && MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../$LAB" >&2
        exit 1
    }
    shopt -s nullglob
    PNGS=("$FIGS"/*.png)
    shopt -u nullglob
    [[ ${#PNGS[@]} -gt 0 ]] || { echo "error: no PNGs in $FIGS" >&2; exit 1; }

    # Delegate to render_reports.sh -- it is the only script that renders,
    # so rendering behaviour lives in exactly one place.
    if [[ -f "$LAB/report.tex" ]]; then
        if ! "$ROOT/tools/render_reports.sh" "$LAB"; then
            echo "error: report failed to render -- fix it before packaging" >&2
            exit 1
        fi
        echo
    fi

    PKG="$STAGE/$LAB-$WHO"
    mkdir -p "$PKG/figs"
    cp "${PNGS[@]}" "$PKG/figs/"
    for f in report.pdf report.tex report.md; do
        [[ -f "$LAB/$f" ]] && cp "$LAB/$f" "$PKG/"
    done

    # Strip LaTeX comment-only lines. A submitted document must not carry
    # notes about our tooling; comment-only lines are where those collect.
    # Trailing comments are left alone -- a '%' at end of line suppresses a
    # space in LaTeX, so removing it would change the rendering.
    [[ -f "$PKG/report.tex" ]] && \
        uv run --project dsp26 python tools/strip_comments.py \
            "$PKG/report.tex" -o "$PKG/report.tex"

    # Hard guard: nothing naming our automation may ship. This is the check
    # that actually enforces the boundary -- the strip above is just the tidy.
    if uv run --project dsp26 python - "$PKG" <<'GUARD'
import sys
from pathlib import Path
sys.path.insert(0, "tools")
from strip_comments import find_tooling_refs
bad = []
for p in Path(sys.argv[1]).rglob("*"):
    if p.is_file() and p.suffix in {".tex", ".md", ".txt", ".py"}:
        for ln, text in find_tooling_refs(p.read_text(errors="replace")):
            bad.append(f"  {p.name}:{ln}: {text.strip()[:80]}")
if bad:
    print("Tooling references found in files about to be submitted:")
    print("\n".join(bad))
    sys.exit(1)
GUARD
    then :; else
        echo "error: refusing to package -- remove the lines above" >&2
        exit 1
    fi

    OUT="$ROOT/$LAB/$LAB-figures-$WHO.zip"
    rm -f "$OUT"
    (cd "$STAGE" && zip -r "$OUT" "$LAB-$WHO" > /dev/null)

    echo "Wrote $OUT"
    echo
    echo "Contents:"
    unzip -l "$OUT" | awk 'NR>3 && NF>=4 {print "  " $4}' | grep -v '/$' || true
    echo
    echo "Size: $(du -h "$OUT" | cut -f1)"
    echo
    echo "Report + figures only -- no code. Confirm that is what this lab wants:"
    echo "  reference_docs/submission_requirements.md"
    exit 0
fi

# ---- 1. stage a copy; the working tree is never touched --------------------
mkdir -p "$STAGE/dsp26"
for item in pyproject.toml uv.lock .python-version README.md src; do
    [[ -e "dsp26/$item" ]] && cp -r "dsp26/$item" "$STAGE/dsp26/"
done
find "$STAGE" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true

# ---- 2. strip comments -----------------------------------------------------
if [[ $STRIP -eq 1 ]]; then
    echo "Stripping comments..."
    EXTRA=()
    [[ $STRIP_ALL -eq 1 ]] && EXTRA+=(--strip-all)
    TMPSRC="$(mktemp -d)"
    if ! uv run --project dsp26 python tools/strip_comments.py \
            "$STAGE/dsp26/src" -o "$TMPSRC" "${EXTRA[@]}"; then
        echo "error: stripping failed -- aborting rather than shipping bad code" >&2
        rm -rf "$TMPSRC"; exit 1
    fi
    rm -rf "$STAGE/dsp26/src" && mv "$TMPSRC" "$STAGE/dsp26/src"
    echo
else
    echo "Keeping comments (--keep-comments)."
    echo
fi

# ---- 3. prepend an identifying header to each .py --------------------------
# Every submitted file says which course, lab, and author it belongs to.
while IFS= read -r f; do
    hdr="$(mktemp)"
    cat > "$hdr" <<EOF
# CESC 410L -- Lab ${LABNUM}
# ${WHO}
# ${DATE}
EOF
    # Keep a shebang first if the file has one.
    if head -1 "$f" | grep -q '^#!'; then
        { head -1 "$f"; cat "$hdr"; tail -n +2 "$f"; } > "$f.new"
    else
        { cat "$hdr"; echo; cat "$f"; } > "$f.new"
    fi
    mv "$f.new" "$f"
    rm -f "$hdr"
done < <(find "$STAGE/dsp26/src" -name '*.py')

# ---- 4. zip ----------------------------------------------------------------
OUT="$ROOT/$LAB/dsp26-$LAB-$WHO.zip"
rm -f "$OUT"
(cd "$STAGE" && zip -r "$OUT" dsp26 -x '*/__pycache__/*' '*.pyc' > /dev/null)

echo "Wrote $OUT"
echo
echo "Contents:"
unzip -l "$OUT" | awk 'NR>3 && NF>=4 {print "  " $4}' | grep -v '/$' || true
echo
echo "Size: $(du -h "$OUT" | cut -f1)"
echo
if [[ $STRIP_ALL -eq 1 ]]; then
    echo "WARNING: --strip-all removed DEVIATION FROM HANDOUT markers."
    echo "         Modified handout code is shipping with no disclosure."
    echo
fi
# COMPOSITION REPORT. A file list tells you what is in the zip; it does not tell
# you what the zip mostly IS. Lab 1's was 93% uv.lock and 1.8% the PREVIOUS
# lab's code, against 4.3% of the work being graded -- and the list above looked
# perfectly reasonable. See docs/directives/coursework-solutions.md, section
# "Read the handout's own deliverables section before deciding what to submit".
echo "What this archive actually consists of:"
unzip -l "$OUT" | awk -v lab="$LAB" '
    NR>3 && NF>=4 && $1 ~ /^[0-9]+$/ {
        size=$1; path=$4; total+=size
        if (path ~ /uv\.lock$/)              key="uv.lock (dependency lockfile)"
        else if (path ~ /lab[0-9]+_/) {
            n=path; sub(/.*\/lab/,"lab",n); sub(/\/.*/,"",n); key=n "/"
        }
        else                                 key="project scaffolding"
        b[key]+=size
    }
    END {
        # Largest share first, TOTAL last. Sorting outside awk put TOTAL in the
        # middle, which buried the number the report exists to show.
        n = 0
        for (k in b) { keys[++n] = k }
        for (i = 1; i < n; i++)
            for (j = i+1; j <= n; j++)
                if (b[keys[j]] > b[keys[i]]) { tmp=keys[i]; keys[i]=keys[j]; keys[j]=tmp }
        for (i = 1; i <= n; i++)
            printf "  %-34s %9d B  %5.1f%%\n", keys[i], b[keys[i]], 100*b[keys[i]]/total
        printf "  %-34s %9d B\n", "TOTAL", total
    }' 
echo
echo "⚠ If most of this is not the work being graded, ask whether it should ship at all."
echo
echo "Check the list above: lab code only -- no .venv, no tools/, no caches."
echo "Then confirm this lab actually wants code submitted. READ THE HANDOUT'S OWN"
echo "deliverables section -- not the task descriptions, the submission list:"
echo "  grep -inE 'submit|deliverab|artifact' <labNN>/<handout>.md"
echo "  reference_docs/submission_requirements.md"
