#!/usr/bin/env bash
# Build script for CEC 320 final-exam cheatsheets.
#
# Usage:
#   ./build.sh              # builds both parts
#   ./build.sh part1        # just part 1
#   ./build.sh part2        # just part 2
#   ./build.sh part1 --pdf  # also compile to PDF via tectonic
#
# Concatenates _preamble_partN.tex + every .tex in partN/ (alphabetic) + _footer.tex
# Output: ../final_exam_cheatsheet_partN.tex (next to design_notes.md).
#
# Partials are pure content fragments (no \documentclass, no \begin{document},
# no \begin{multicols*}). They contain \section{}, \subsection{}, tables, etc.
# Filename ordering is alphabetic; prefix with NN_ to control order.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="$(cd "$DIR/.." && pwd)"

PARTS_REQUESTED=("$@")
PDF=0
PARTS=()
for arg in "${PARTS_REQUESTED[@]}"; do
  case "$arg" in
    --pdf) PDF=1 ;;
    part1|part2) PARTS+=("$arg") ;;
    *) echo "Unknown arg: $arg" >&2; exit 1 ;;
  esac
done
if [ ${#PARTS[@]} -eq 0 ]; then
  PARTS=(part1 part2)
fi

build_part() {
  local part="$1"
  local out="$OUT_DIR/final_exam_cheatsheet_${part}.tex"
  local preamble="$DIR/_preamble_${part}.tex"
  local footer="$DIR/_footer.tex"
  local partials_dir="$DIR/$part"

  if [ ! -f "$preamble" ]; then
    echo "Missing preamble: $preamble" >&2; exit 1
  fi
  if [ ! -d "$partials_dir" ]; then
    echo "Missing partials dir: $partials_dir" >&2; exit 1
  fi

  echo "Building $part -> $out"
  {
    cat "$preamble"
    echo
    # Concatenate every .tex partial in alphabetic order. Skip files starting with _.
    local found=0
    for f in $(LC_ALL=C ls "$partials_dir"/*.tex 2>/dev/null | sort); do
      base="$(basename "$f")"
      case "$base" in _*) continue ;; esac
      echo "% ----- $base -----"
      cat "$f"
      echo
      found=$((found + 1))
    done
    if [ "$found" -eq 0 ]; then
      echo "% (no partials found)"
    fi
    cat "$footer"
  } > "$out"
  echo "  wrote $out ($(wc -l < "$out") lines, $found partials)"

  if [ "$PDF" -eq 1 ]; then
    if ! command -v ~/bin/tectonic >/dev/null 2>&1 && ! command -v tectonic >/dev/null 2>&1; then
      echo "  (tectonic not found; skip PDF)" >&2
      return
    fi
    local TECTONIC
    TECTONIC="$(command -v ~/bin/tectonic 2>/dev/null || command -v tectonic)"
    echo "  compiling with tectonic..."
    "$TECTONIC" -X compile "$out" -o /tmp 2>&1 | tail -5 || true
    if command -v python3 >/dev/null && python3 -c "import fitz" 2>/dev/null; then
      python3 -c "import fitz; print('  pages:', fitz.open('/tmp/final_exam_cheatsheet_${part}.pdf').page_count)" 2>/dev/null || true
    fi
  fi
}

for p in "${PARTS[@]}"; do
  build_part "$p"
done

echo "Done."
