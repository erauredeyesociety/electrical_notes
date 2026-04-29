#!/usr/bin/env bash
# Build script for CEC 320 final-exam cheatsheet.
#
# Default: produces a single combined 14-page document.
#
# Usage:
#   ./build.sh                     # build combined cheatsheet (default)
#   ./build.sh --pdf               # also compile to PDF via tectonic
#   ./build.sh combined            # explicit; same as default
#   ./build.sh part1               # legacy: just part 1 (6 pages)
#   ./build.sh part2               # legacy: just part 2 (8 pages)
#   ./build.sh combined part1 part2 --pdf   # build all three + compile
#
# The combined build concatenates _preamble.tex + every .tex in part1/
# (alphabetic) + every .tex in part2/ (alphabetic) + _footer.tex into
# ../final_exam_cheatsheet.tex. Target = 14 pages.
#
# Part-only builds use _preamble_partN.tex and produce
# ../final_exam_cheatsheet_partN.tex (kept for printing front-and-back).
#
# Partials are pure content fragments (no \documentclass, no \begin{document},
# no \begin{multicols*}). They contain \section{}, \subsection{}, etc.
# Filename ordering is alphabetic; prefix with NN_ to control order.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="$(cd "$DIR/.." && pwd)"

ARGS=("$@")
PDF=0
TARGETS=()
for arg in "${ARGS[@]}"; do
  case "$arg" in
    --pdf) PDF=1 ;;
    combined|part1|part2) TARGETS+=("$arg") ;;
    *) echo "Unknown arg: $arg" >&2; exit 1 ;;
  esac
done
if [ ${#TARGETS[@]} -eq 0 ]; then
  TARGETS=(combined)
fi

# Print partial files (skip files starting with _) in alphabetic order.
list_partials() {
  local d="$1"
  if [ ! -d "$d" ]; then return; fi
  for f in $(LC_ALL=C ls "$d"/*.tex 2>/dev/null | sort); do
    case "$(basename "$f")" in _*) continue ;; esac
    echo "$f"
  done
}

count_partials() {
  list_partials "$1" | wc -l
}

build_combined() {
  local out="$OUT_DIR/final_exam_cheatsheet.tex"
  local preamble="$DIR/_preamble.tex"
  local footer="$DIR/_footer.tex"

  if [ ! -f "$preamble" ]; then
    echo "Missing preamble: $preamble" >&2; exit 1
  fi

  local n1 n2 total
  n1=$(count_partials "$DIR/part1")
  n2=$(count_partials "$DIR/part2")
  total=$((n1 + n2))
  echo "Building combined -> $out  (part1: $n1, part2: $n2, total: $total)"

  {
    cat "$preamble"
    echo
    while IFS= read -r f; do
      [ -z "$f" ] && continue
      echo "% ----- part1/$(basename "$f") -----"
      cat "$f"
      echo
    done < <(list_partials "$DIR/part1")
    while IFS= read -r f; do
      [ -z "$f" ] && continue
      echo "% ----- part2/$(basename "$f") -----"
      cat "$f"
      echo
    done < <(list_partials "$DIR/part2")
    cat "$footer"
  } > "$out"
  echo "  wrote $out ($(wc -l < "$out") lines)"

  maybe_compile "$out" "final_exam_cheatsheet"
}

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

  local n
  n=$(count_partials "$partials_dir")
  echo "Building $part -> $out  ($n partials)"

  {
    cat "$preamble"
    echo
    while IFS= read -r f; do
      [ -z "$f" ] && continue
      echo "% ----- $part/$(basename "$f") -----"
      cat "$f"
      echo
    done < <(list_partials "$partials_dir")
    cat "$footer"
  } > "$out"
  echo "  wrote $out ($(wc -l < "$out") lines)"

  maybe_compile "$out" "final_exam_cheatsheet_${part}"
}

maybe_compile() {
  local tex="$1"
  local stem="$2"
  if [ "$PDF" -ne 1 ]; then return; fi
  local TECTONIC=""
  if [ -x "$HOME/bin/tectonic" ]; then
    TECTONIC="$HOME/bin/tectonic"
  elif command -v tectonic >/dev/null 2>&1; then
    TECTONIC="$(command -v tectonic)"
  else
    echo "  (tectonic not found; skip PDF)" >&2
    return
  fi
  echo "  compiling with tectonic..."
  local logfile="/tmp/${stem}_tectonic.log"
  "$TECTONIC" -X compile "$tex" -o /tmp >"$logfile" 2>&1 || true

  # ---- overfull-hbox stats (visual horizontal overflow) ----
  local n_overfull max_overfull_pt
  n_overfull=$(grep -c "Overfull \\\\hbox" "$logfile" || true)
  if [ -n "${n_overfull:-}" ] && [ "$n_overfull" -gt 0 ]; then
    max_overfull_pt=$(grep -oE "Overfull \\\\hbox \([0-9]+\.[0-9]+pt" "$logfile" \
      | grep -oE "[0-9]+\.[0-9]+" | sort -rn | head -1)
    # count runs that exceed common severity thresholds
    local n_severe n_egregious
    n_severe=$(grep -oE "Overfull \\\\hbox \([0-9]+\.[0-9]+pt" "$logfile" \
      | grep -oE "[0-9]+\.[0-9]+" \
      | awk '$1>=20 {n++} END{print n+0}')
    n_egregious=$(grep -oE "Overfull \\\\hbox \([0-9]+\.[0-9]+pt" "$logfile" \
      | grep -oE "[0-9]+\.[0-9]+" \
      | awk '$1>=50 {n++} END{print n+0}')
    echo "  overfull \\hbox: $n_overfull total, max=${max_overfull_pt}pt, ${n_severe} >=20pt, ${n_egregious} >=50pt (visual overlap risk)"
  else
    echo "  overfull \\hbox: 0 (clean horizontal layout)"
  fi

  # ---- page count via PyMuPDF (fitz) if available ----
  if command -v python3 >/dev/null 2>&1 && python3 -c "import fitz" 2>/dev/null; then
    local pdf="/tmp/${stem}.pdf"
    if [ -f "$pdf" ]; then
      python3 -c "import fitz; d=fitz.open('$pdf'); print('  pages:', d.page_count)" 2>/dev/null || true
    else
      echo "  (PDF not produced — compile likely failed; tail of log:)"
      tail -10 "$logfile"
    fi
  fi
}

for t in "${TARGETS[@]}"; do
  case "$t" in
    combined) build_combined ;;
    part1|part2) build_part "$t" ;;
  esac
done

echo "Done."
