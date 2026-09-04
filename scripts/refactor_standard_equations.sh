#!/bin/bash

# Fix LaTeX rendering issues in markdown files.
#
# ⚠ DESTRUCTIVE AND UNSCOPED. Every step below is `find . -name "*.md"` piped
# into `perl -i` — an IN-PLACE rewrite of every markdown file at or below the
# CURRENT WORKING DIRECTORY, with no backup and no dry run.
#
# Run from the repo root today it would rewrite ~750 .md files across all 15
# course folders, docs/, ocr_handler/docs/ and docs-rag/ — including the twelve
# older courses that are explicitly frozen (docs/directives/coursework-solutions.md).
#
# The guard below makes that accident impossible without meaning it. It does NOT
# change what the script does when you do mean it:
#
#     ./scripts/refactor_standard_equations.sh --yes-rewrite-in-place
#
# Prefer running it from the ONE folder you want rewritten, not the repo root.
# Added 2026-09-04 after an audit flagged it; the transformations are untouched.

if [[ "${1:-}" != "--yes-rewrite-in-place" ]]; then
    cat >&2 <<EOF
REFUSING TO RUN — this rewrites every *.md at or below $(pwd) in place.

  files that would be touched: $(find . -type f -name '*.md' 2>/dev/null | wc -l)

There is no backup and no dry run. If that is genuinely what you want:

    $0 --yes-rewrite-in-place

Safer: cd into the single folder you want changed first.
EOF
    exit 2
fi

# --- Step 1: Remove problematic $ symbols around comparison operators in math mode ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Removing nested $ symbols in $file ..."
        # Remove $ around \geq and \leq when inside math delimiters
        perl -i -pe 's/\$\\geq\$/\\geq/g' "$file"
        perl -i -pe 's/\$\\leq\$/\\leq/g' "$file"
        perl -i -pe 's/\$\\times\$/\\times/g' "$file"
        perl -i -pe 's/\$\\pm\$/\\pm/g' "$file"
        perl -i -pe 's/\$\\approx\$/\\approx/g' "$file"
    fi
done

# --- Step 2: Convert Unicode symbols to LaTeX (WITHOUT wrapping in $) ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Converting Unicode symbols in $file ..."
        sed -i -E \
            -e 's/≈/\\approx/g' \
            -e 's/∼/\\sim/g' \
            -e 's/≥/\\geq/g' \
            -e 's/⩾/\\geq/g' \
            -e 's/≤/\\leq/g' \
            -e 's/⩽/\\leq/g' \
            -e 's/±/\\pm/g' \
            -e 's/×/\\times/g' \
            -e 's/⁻/-/g' \
            -e 's/⁺/+/g' \
            "$file"
    fi
done

# --- Step 3: Normalize math delimiters ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Normalizing math delimiters in $file ..."
        sed -i -E \
            -e 's/\\\((.*?)\\\)/$\1$/g' \
            -e 's/\\\[(.*?)\\\]/$$\1$$/g' \
            "$file"
    fi
done

echo "All Markdown files processed successfully."