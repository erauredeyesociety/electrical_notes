#!/bin/bash

# Usage: ./fit_pdf.sh /path/to/article.md
FILE="$1"

if [[ ! -f "$FILE" ]]; then
    echo "File not found: $FILE"
    exit 1
fi

# Extract directory and filename
DIR=$(dirname "$FILE")
BASENAME=$(basename "$FILE")
OUTPUT="${BASENAME%.md}.pdf"

# Change to the file's directory
cd "$DIR" || { echo "Failed to cd $DIR"; exit 1; }

# Initial settings
FONT=10.0       # starting font size in pt
MARGIN=0.5      # starting margin in inches
MIN_FONT=1.0
MIN_MARGIN=0.1

# Step sizes for each iteration
FONT_STEP=1.5
MARGIN_STEP=0.05

while true; do
    echo "Trying font=${FONT}pt, margin=${MARGIN}in ..."

    # Generate PDF with landscape + two columns
    pandoc "$BASENAME" \
        -o "$OUTPUT" \
        --pdf-engine=xelatex \
        -V fontsize=${FONT}pt \
        -V geometry:margin=${MARGIN}in \
        --variable graphics=true \
        --variable image-scale=0.7 \
        -V geometry:landscape \
        -V twocolumn \
        -V columnsep=0.2in \
        -V linkcolor=blue \
        -V header-includes="\usepackage{titlesec}\titlespacing*{\section}{0pt}{2pt}{2pt}\newcommand{\pmV}{\pm V}" \
        --from markdown+yaml_metadata_block+tex_math_dollars

    # Check if PDF was created
    if [[ ! -f "$OUTPUT" ]]; then
        echo "Error producing PDF."
        # Continue trying with smaller settings rather than exit
    else
        # Check number of pages
        if ! command -v pdfinfo &> /dev/null; then
            echo "pdfinfo command not found. Install poppler-utils."
            exit 1
        fi

        PAGES=$(pdfinfo "$OUTPUT" | grep Pages | awk '{print $2}')
        echo "Generated PDF has $PAGES page(s)"

        if [[ "$PAGES" -le 2 ]]; then
            echo "Success! PDF fits on 2 pages."
            break
        fi

        # Delete oversized PDF
        rm -f "$OUTPUT"
    fi

    # Reduce font/margin
    FONT=$(echo "$FONT - $FONT_STEP" | bc)
    MARGIN=$(echo "$MARGIN - $MARGIN_STEP" | bc)

    # Stop if minimums reached
    FONT_OK=$(echo "$FONT >= $MIN_FONT" | bc)
    MARGIN_OK=$(echo "$MARGIN >= $MIN_MARGIN" | bc)

    if [[ "$FONT_OK" -eq 0 || "$MARGIN_OK" -eq 0 ]]; then
        echo "Cannot fit file into 2 pages with minimum font/margin limits!"
        exit 1
    fi
done

echo "Final settings: FONT=${FONT}pt, MARGIN=${MARGIN}in"
echo "PDF saved as: $DIR/$OUTPUT"