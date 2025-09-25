#!/bin/bash

# --- Step 1: Fix Unicode math symbols for LaTeX ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Fixing Unicode symbols in $file ..."
        sed -i -E \
            -e 's/[≈∼]/\\approx/g' \
            -e 's/[≥⩾]/\\geq/g' \
            -e 's/[≤⩽]/\\leq/g' \
            -e 's/±/\\pm/g' \
            "$file"
        echo "Fixed Unicode symbols in $file"
    fi
done

# --- Step 2: Normalize math delimiters ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Normalizing math delimiters in $file ..."
        sed -i -E \
            -e 's/\\\((.*?)\\\)/$\1$/g' \
            -e 's/\\\[(.*?)\\\]/$$\1$$/g' \
            -e 's/\\\[(.*?)\$\$/$$\1$$/g' \
            -e 's/\$\$(.*)\\\]/$$\1$$/g' \
            -e 's/^\$\$\s*/$$/g' \
            -e 's/\s*\$\$$/$$/g' \
            "$file"
    fi
done

# --- Step 3: Fix multiline \[ ... $$ patterns ---
find . -type f -name "*.md" | while read -r file; do
    if [[ -s "$file" ]]; then
        echo "Fixing multiline patterns in $file ..."
        perl -0777 -i -pe 's/\\\[\n(.*?)\n\$\$/\$\$\n$1\n\$\$/gs' "$file"
    fi
done

echo "All Markdown files processed successfully."
