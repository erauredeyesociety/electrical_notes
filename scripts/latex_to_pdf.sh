#!/usr/bin/env bash
set -e

# -----------------------------
# Config
# -----------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ZIP_FILE="$SCRIPT_DIR/Resume___CV.zip"
WORKDIR="$SCRIPT_DIR/.resume_build"
OUTDIR="$SCRIPT_DIR/static/pdfs"

# -----------------------------
# Function to check commands
# -----------------------------
check_command() {
    local cmd=$1
    local pkg=$2
    if ! command -v "$cmd" &> /dev/null; then
        echo "[!] Required command '$cmd' not found."
        echo "    On Ubuntu/Debian, install it with: sudo apt install $pkg"
        echo "    On RedHat/CentOS, install it with: sudo yum install $pkg"
        exit 1
    fi
}

# -----------------------------
# Function to inject hyperref settings
# -----------------------------
inject_hyperref_settings() {
    local tex_file=$1
    
    echo "[*] Configuring hyperref settings in $(basename "$tex_file")..."
    
    # Check if hyperref is already loaded
    if grep -q '\\usepackage{hyperref}' "$tex_file"; then
        # Remove existing hyperref line
        sed -i '/\\usepackage{hyperref}/d' "$tex_file"
    fi
    
    # Check if hypersetup already exists
    if grep -q '\\hypersetup{' "$tex_file"; then
        # Remove existing hypersetup block (multi-line)
        sed -i '/\\hypersetup{/,/^}/d' "$tex_file"
    fi
    
    # Find the line number after \usepackage declarations
    # We'll insert our hyperref config right after the last \usepackage
    local insert_line=$(grep -n '\\usepackage' "$tex_file" | tail -1 | cut -d: -f1)
    
    if [ -z "$insert_line" ]; then
        # If no usepackage found, insert after \documentclass
        insert_line=$(grep -n '\\documentclass' "$tex_file" | head -1 | cut -d: -f1)
    fi
    
    # Increment to insert after the line
    insert_line=$((insert_line + 1))
    
    # Create temporary file with hyperref configuration
    local temp_file="${tex_file}.tmp"
    local doc_title=$(basename "$tex_file" .tex | tr '[:lower:]' '[:upper:]')
    
    # Build the file with injected hyperref config
    head -n "$((insert_line - 1))" "$tex_file" > "$temp_file"
    
    cat >> "$temp_file" << 'EOF'
% Hyperlink configuration - auto-injected by compile script
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=blue,
    pdfnewwindow=true,
    pdftitle={Gatlin Nelson - Resume},
    pdfauthor={Gatlin Nelson},
    pdfsubject={Resume and CV},
    pdfkeywords={Cybersecurity, Computer Engineering, Research}
}
EOF
    
    tail -n +"$insert_line" "$tex_file" >> "$temp_file"
    
    # Replace original with modified version
    mv "$temp_file" "$tex_file"
}

# -----------------------------
# Check required commands
# -----------------------------
check_command pdflatex texlive-latex-base
check_command unzip unzip
check_command find findutils
check_command sed sed

# -----------------------------
# Prepare directories
# -----------------------------
rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"
mkdir -p "$OUTDIR"

# -----------------------------
# Extract ZIP
# -----------------------------
if [ ! -f "$ZIP_FILE" ]; then
    echo "[!] ZIP file $ZIP_FILE not found. Please place it in the script directory."
    exit 1
fi

echo "[*] Extracting $ZIP_FILE..."
unzip -q "$ZIP_FILE" -d "$WORKDIR"

# -----------------------------
# Remove all *.Identifier files recursively
# -----------------------------
echo "[*] Removing any *.Identifier files..."
find "$WORKDIR" -type f -name "*.Identifier" -exec rm -f {} +

# -----------------------------
# Function to backup existing PDF
# -----------------------------
backup_pdf() {
    local pdf_path=$1
    local base_name="${pdf_path%.pdf}"
    
    if [ ! -f "$pdf_path" ]; then
        return 0  # No file to backup
    fi
    
    # Check if .bak exists
    if [ ! -f "${base_name}.bak" ]; then
        mv "$pdf_path" "${base_name}.bak"
        echo "[*] Backed up $(basename "$pdf_path") → $(basename "${base_name}.bak")"
    else
        # Find next available .bakN number
        local counter=1
        while [ -f "${base_name}.bak${counter}" ]; do
            counter=$((counter + 1))
        done
        mv "$pdf_path" "${base_name}.bak${counter}"
        echo "[*] Backed up $(basename "$pdf_path") → $(basename "${base_name}.bak${counter}")"
    fi
}

# -----------------------------
# Compile .tex files
# -----------------------------
for TEX_FILE in resume.tex cv.tex; do
    TEX_PATH="$WORKDIR/$TEX_FILE"
    if [ -f "$TEX_PATH" ]; then
        PDF_NAME="${TEX_FILE%.tex}.pdf"
        PDF_OUTPUT="$OUTDIR/$PDF_NAME"
        
        # Backup existing PDF if it exists
        backup_pdf "$PDF_OUTPUT"
        
        # Inject hyperref settings before compiling
        inject_hyperref_settings "$TEX_PATH"
        
        echo "[*] Compiling $TEX_FILE → $PDF_NAME (maximum resolution)"
        
        # Set maximum PDF resolution (1200 DPI for absolute crispness)
        export PDFTEX_DPI=1200
        
        # First pass - with maximum quality settings
        pdflatex -interaction=nonstopmode \
                 -output-directory="$WORKDIR" \
                 -output-format=pdf \
                 "$TEX_PATH" > /dev/null 2>&1
        
        # Second pass (for proper hyperlinks and references)
        pdflatex -interaction=nonstopmode \
                 -output-directory="$WORKDIR" \
                 -output-format=pdf \
                 "$TEX_PATH" > /dev/null 2>&1
        
        # Unset the environment variable
        unset PDFTEX_DPI
        
        # Move compiled PDF to output directory
        if [ -f "$WORKDIR/$PDF_NAME" ]; then
            mv "$WORKDIR/$PDF_NAME" "$PDF_OUTPUT"
            echo "[✓] Successfully compiled $PDF_NAME"
        else
            echo "[!] Failed to compile $PDF_NAME"
        fi
    else
        echo "[!] $TEX_FILE not found in ZIP, skipping."
    fi
done

# -----------------------------
# Cleanup temporary files
# -----------------------------
echo "[*] Cleaning up temporary files..."
rm -rf "$WORKDIR"

# -----------------------------
# Summary
# -----------------------------
echo ""
echo "════════════════════════════════════════"
echo "  ✓ Compilation Complete"
echo "════════════════════════════════════════"
echo "PDFs are available in: $OUTDIR"
echo ""
ls -lh "$OUTDIR"/*.pdf 2>/dev/null || echo "No PDFs found."
echo ""