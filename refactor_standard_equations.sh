#!/bin/bash

# --- Step 1: Fix Unicode math symbols and superscripts for LaTeX ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Fixing Unicode symbols in $file ..."
        sed -i -E \
            -e 's/≈/\\approx/g' \
            -e 's/∼/\\sim/g' \
            -e 's/≥/$\\geq$/g' \
            -e 's/⩾/$\\geq$/g' \
            -e 's/≤/$\\leq$/g' \
            -e 's/⩽/$\\leq$/g' \
            -e 's/±/\\pm/g' \
            -e 's/⁻/-/g' \
            -e 's/⁺/+/g' \
            -e 's/✓/[CHECK]/g' \
            -e 's/✗/[X]/g' \
            -e 's/×/\\times/g' \
            -e 's/❌/[X]/g' \
            "$file"
        echo "Fixed Unicode symbols in $file"
    fi
done

# --- Step 2: Wrap bare LaTeX math commands that appear in regular text ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Wrapping bare LaTeX commands in $file ..."
        # Fix bare \geq, \leq that aren't already in math mode
        perl -i -pe 's/(?<!\$)\\geq(?!\$)/\$\\geq\$/g' "$file"
        perl -i -pe 's/(?<!\$)\\leq(?!\$)/\$\\leq\$/g' "$file"
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

# --- Step 4: Fix multiline \[ ... $$ patterns ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Fixing multiline patterns in $file ..."
        perl -0777 -i -pe 's/\\\[\n(.*?)\n\$\$/\$\$\n$1\n\$\$/gs' "$file"
    fi
done

echo "All Markdown files processed successfully."