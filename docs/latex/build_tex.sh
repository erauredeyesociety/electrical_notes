#!/usr/bin/env bash
# Build-check one .tex, or every .tex in an assignment. Deletes the PDF.
#
# AUTOMATION -- never submitted.
#
#   docs/latex/build_tex.sh content/cesc_470/hw/hw01/p01_five_components.tex
#   docs/latex/build_tex.sh content/cesc_470/hw/hw01        every .tex there
#   docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep keep the PDFs
#
# Paths are REPO-RELATIVE. Shared by every course -- doctrine lives in
# docs/directives/coursework-solutions.md
#
# Every per-problem file is standalone (it inputs the shared preamble), so any
# one of them can be checked without building the whole assignment. That is the
# point of the fragment layout: a broken problem is found where it broke.

set -uo pipefail

KEEP=0; TARGET=""
for a in "$@"; do
    case "$a" in
        --keep) KEEP=1 ;;
        -*) echo "unknown option: $a" >&2; exit 2 ;;
        *) TARGET="${a%/}" ;;
    esac
done
[[ -n "$TARGET" ]] || { echo "usage: build_tex.sh <file.tex|hwNN> [--keep]" >&2; exit 2; }

# Repo root: this script lives at docs/latex/, so up two levels.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

command -v tectonic >/dev/null || { echo "error: tectonic not found" >&2; exit 1; }

if [[ -f "$TARGET" ]]; then
    FILES=("$TARGET")
elif [[ -d "$TARGET" ]]; then
    mapfile -t FILES < <(find "$TARGET" -maxdepth 1 -name '*.tex' | sort)
else
    echo "error: no such file or folder: $TARGET" >&2; exit 1
fi
[[ ${#FILES[@]} -gt 0 ]] || { echo "no .tex found under $TARGET"; exit 0; }

fails=0
for f in "${FILES[@]}"; do
    printf '%-46s ' "$f"
    if (cd "$(dirname "$f")" && tectonic "$(basename "$f")") >/tmp/tex_$$.log 2>&1; then
        echo "OK"
        [[ $KEEP -eq 0 ]] && rm -f "${f%.tex}.pdf"
    else
        echo "FAIL"; sed 's/^/    /' /tmp/tex_$$.log | tail -18; fails=$((fails+1))
    fi
    rm -f /tmp/tex_$$.log
done
echo
[[ $fails -gt 0 ]] && { echo "$fails file(s) failed."; exit 1; }
echo "All build."
