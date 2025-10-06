#!/bin/bash

# Fix LaTeX rendering issues in markdown files

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