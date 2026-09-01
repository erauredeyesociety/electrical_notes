#!/usr/bin/env bash
# Render lab report .tex files to PDF.
#
# AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.
#
#   tools/render_reports.sh          # every labNN/*.tex
#   tools/render_reports.sh lab00    # one lab
#
# THIS IS THE ONLY SCRIPT THAT RENDERS PDFs. make_submission.sh --figures
# calls this rather than invoking tectonic itself, so there is one place where
# rendering behaviour lives and one place to fix it.
#
# PDFs are KEPT. They are gitignored (lab*/report*.pdf), so they never bloat
# the repo, and keeping them means the built report is there when you want to
# read or submit it without a rebuild.
#
# Uses tectonic -- self-contained, no TeX Live install, fetches packages on
# demand and caches them. First run for a new package set needs network.

set -uo pipefail

TARGET=""
for arg in "$@"; do
    case "$arg" in
        -*) echo "unknown option: $arg" >&2; exit 2 ;;
        *)  TARGET="${arg%/}" ;;
    esac
done

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v tectonic >/dev/null 2>&1; then
    cat >&2 <<'EOF'
error: tectonic not found.

Install (no root, no TeX Live):
    curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh
    mv tectonic ~/.local/bin/

Alternative: `sudo apt install texlive-latex-recommended texlive-latex-extra`
then swap tectonic for pdflatex below.
EOF
    exit 1
fi

if [[ -n "$TARGET" ]]; then
    mapfile -t TEX < <(find "$TARGET" -maxdepth 1 -name '*.tex' 2>/dev/null | sort)
else
    mapfile -t TEX < <(find . -maxdepth 2 -path './lab*' -name '*.tex' 2>/dev/null | sort)
fi

if [[ ${#TEX[@]} -eq 0 ]]; then
    echo "No .tex files found${TARGET:+ under $TARGET}."
    echo "Start one from reference_docs/report_template.tex"
    exit 0
fi

fails=0
for f in "${TEX[@]}"; do
    dir="$(dirname "$f")"
    base="$(basename "$f" .tex)"
    printf '%-44s ' "$f"

    # Run inside the .tex's own folder so relative \includegraphics{figs/...}
    # resolves the same way Overleaf would.
    if (cd "$dir" && tectonic "$base.tex") >/tmp/render_$$.log 2>&1; then
        echo "OK  -> $dir/$base.pdf"
    else
        echo "FAIL"
        sed 's/^/    /' /tmp/render_$$.log | tail -20
        fails=$((fails + 1))
    fi
    rm -f /tmp/render_$$.log
done

echo
if [[ $fails -gt 0 ]]; then
    echo "$fails file(s) failed to render."
    echo "Missing figures? figs/ is gitignored -- generate them first:"
    echo "  cd dsp26 && MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN"
    exit 1
fi

echo "All rendered. PDFs kept (gitignored)."
