#!/usr/bin/env bash
# check_pages.sh -- render the v10 HTML via headless Chromium, report page
# count + any JS overflow warnings logged by detectOverflow().
#
# Usage:
#   ./check_pages.sh                       # default: exam3_cheatsheet_v10.html
#   ./check_pages.sh some_other.html
#
# Output:
#   - Page count (from pdfinfo)
#   - Page dimensions
#   - Any OVERFLOW / AUTO_PAGINATE messages captured from the browser console
#   - First ~6 lines of text per page (best-effort; KaTeX math is invisible
#     to pdftotext because it renders as SVG, so pages may appear empty)

set -euo pipefail

HTML="${1:-exam3_cheatsheet_v10.html}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HTML_PATH="$SCRIPT_DIR/$HTML"

if [ ! -f "$HTML_PATH" ]; then
  echo "File not found: $HTML_PATH" >&2
  exit 1
fi

TMPDIR="$(mktemp -d)"
trap "rm -rf $TMPDIR" EXIT
PDF="$TMPDIR/out.pdf"
LOG="$TMPDIR/chrome.log"

echo "=== Rendering $HTML via headless Chromium ==="
# --enable-logging=stderr --v=1 captures console.log/console.warn to stderr.
# --virtual-time-budget gives JS time to run (KaTeX + autoPaginate).
google-chrome \
  --headless \
  --no-sandbox \
  --disable-gpu \
  --no-pdf-header-footer \
  --virtual-time-budget=10000 \
  --enable-logging=stderr \
  --v=1 \
  --print-to-pdf="$PDF" \
  "file://$HTML_PATH" 2>"$LOG"

if [ ! -f "$PDF" ]; then
  echo "Chromium did not produce a PDF." >&2
  exit 1
fi

echo "=== pdfinfo ==="
pdfinfo "$PDF" | grep -E '^(Pages|Page size):'
PAGES=$(pdfinfo "$PDF" | awk '/^Pages:/ {print $2}')
PAGE_SIZE=$(pdfinfo "$PDF" | awk -F': +' '/^Page size:/ {print $2}')

echo
echo "=== JS console messages (overflow warnings, pagination status) ==="
# Chrome's logging prefixes lines with [...INFO:...]; we grep for our
# marker strings and strip the prefix.
grep -E '(AUTO_PAGINATE:|OVERFLOW:)' "$LOG" \
  | sed -E 's|^.*"([^"]+)".*$|\1|; s|^.*:[0-9]+ ||' \
  | sort -u \
  || echo "(no overflow/pagination messages found)"

echo
echo "=== First ~6 lines of text per page (math renders as SVG -> may appear blank) ==="
for ((p=1; p<=PAGES; p++)); do
  echo "--- Page $p ---"
  pdftotext -layout -f "$p" -l "$p" "$PDF" - 2>/dev/null \
    | sed '/^[[:space:]]*$/d' \
    | head -n 6
  echo
done

echo "=== Summary ==="
echo "Input : $HTML"
echo "Pages : $PAGES"
echo "Size  : $PAGE_SIZE"
if grep -q 'OVERFLOW:' "$LOG"; then
  echo "Status: OVERFLOW detected — check console messages above; red outline visible on-screen."
  exit 2
else
  echo "Status: OK (no overflow warnings)"
fi
