#!/usr/bin/env bash
# new_tex.sh — scaffold a new problem file with the right preamble inputs.
#
# AUTOMATION -- never submitted.
#
#   docs/latex/new_tex.sh content/cesc_470/hw/hw02 3 clock-rate --pts "15 pts"
#   docs/latex/new_tex.sh content/cesc_410/hw/hw02 1 phasors --pts "20 pts" --lo LO01
#   docs/latex/new_tex.sh content/cesc_470/hw/hw02 --solutions        the answer sheet
#
# WHY THIS EXISTS
#   The two \input lines are the only fiddly part of a new file, and both are
#   easy to get wrong by hand:
#     1. The number of ../ depends on how deep the file sits. From
#        content/<course>/<kind>/<kind>NN/ it is four. Get it wrong and the
#        build fails with "File ... not found" -- the same error Overleaf gives.
#     2. The macros file is named per course.
#   This computes both from the target path instead of trusting a count.
#
# Writes <dir>/pNN_<slug>.tex from the five-section template, and refuses to
# overwrite an existing file.
#
# For Overleaf, flatten afterwards -- a relative \input above the project root
# cannot resolve there:  docs/latex/flatten_tex.sh <dir>

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

DIR=""; NUM=""; SLUG=""; PTS=""; LO=""; TITLE=""; SOLUTIONS=0
while [[ $# -gt 0 ]]; do
    case "$1" in
        --pts)   PTS="$2"; shift 2 ;;
        --lo)    LO="$2"; shift 2 ;;
        --title) TITLE="$2"; shift 2 ;;
        --solutions) SOLUTIONS=1; shift ;;
        -h|--help) sed -n '2,26p' "$0"; exit 0 ;;
        -*) echo "unknown option: $1" >&2; exit 2 ;;
        *)  if   [[ -z "$DIR"  ]]; then DIR="${1%/}"
            elif [[ -z "$NUM"  ]]; then NUM="$1"
            elif [[ -z "$SLUG" ]]; then SLUG="$1"
            else echo "unexpected argument: $1" >&2; exit 2; fi
            shift ;;
    esac
done

[[ -n "$DIR" ]] || { echo "usage: new_tex.sh <assignment-dir> <N> <slug> [--pts P] [--lo LO] [--title T]" >&2; exit 2; }
cd "$ROOT"
[[ -d "$DIR" ]] || { echo "error: no such folder: $DIR (create it first)" >&2; exit 1; }

# --- work out how many ../ reach the repo root, by counting path components ---
# Counted, not assumed. content/cesc_470/hw/hw01 -> 4 components -> ../../../../
depth=$(awk -F/ '{c=0; for(i=1;i<=NF;i++) if($i!="") c++; print c}' <<<"$DIR")
up=""; for ((i = 0; i < depth; i++)); do up+="../"; done
PREAMBLE="${up}docs/latex/coursework_preamble.tex"

[[ -f "${DIR}/${PREAMBLE}" ]] || {
    echo "error: computed preamble path does not resolve:" >&2
    echo "       ${DIR}/${PREAMBLE}" >&2
    echo "       (is ${DIR} inside the repo?)" >&2
    exit 1
}

# --- find this course's macros file -------------------------------------------
COURSE="$(awk -F/ '{print $2}' <<<"$DIR")"          # content/<course>/...
MACROS_REL=""

# Walk UP from the assignment folder looking for reference_docs/*_macros.tex.
# Walking up rather than probing one fixed "../reference_docs" means an
# assignment nested deeper (content/<course>/hw/exams/exam1) still finds the
# course's macros instead of failing -- the layout is not assumed.
probe="$DIR"
while [[ "$probe" != "." && "$probe" != "/" && -n "$probe" ]]; do
    found="$(find "$probe" -maxdepth 2 -path '*/reference_docs/*_macros.tex' 2>/dev/null | sort | head -1)"
    if [[ -n "$found" ]]; then
        MACROS_REL="$(realpath --relative-to="$DIR" "$found")"
        break
    fi
    probe="$(dirname "$probe")"
done

if [[ -z "$MACROS_REL" ]]; then
    echo "error: no reference_docs/*_macros.tex found at or above ${DIR}." >&2
    echo "       Expected content/${COURSE}/reference_docs/${COURSE}_macros.tex" >&2
    echo "       Create it (see docs/latex/INDEX.md) and re-run." >&2
    exit 1
fi

# Two macros files for one course is a silent-wrong-answer bug: the walk above
# takes the NEAREST, so hw/ and qz/ would compile against different notation
# with no error anywhere. Warn loudly -- the doctrine is one file per course.
mapfile -t ALL_MACROS < <(find "content/${COURSE}" -path '*/reference_docs/*_macros.tex' 2>/dev/null | sort)
if (( ${#ALL_MACROS[@]} > 1 )); then
    {
        echo "WARNING: ${#ALL_MACROS[@]} macros files for course '${COURSE}':"
        printf '           %s\n' "${ALL_MACROS[@]}"
        echo "         Only the NEAREST is used here: ${MACROS_REL}"
        echo "         Doctrine is ONE per course, at content/${COURSE}/reference_docs/."
        echo "         Two files means hw/ and qz/ can silently diverge."
    } >&2
fi

# --- header line: 4-arg form when the course states a learning outcome ---------
if [[ $SOLUTIONS -eq 1 ]]; then
    KIND="$(basename "$DIR")"                        # hw01 / qz03 / exam1
    DEST="${DIR}/${KIND}_solutions.tex"
    HEADER=""
else
    [[ -n "$NUM" && -n "$SLUG" ]] || { echo "error: need <N> and <slug> (or --solutions)" >&2; exit 2; }
    printf -v NN '%02d' "$NUM" 2>/dev/null || NN="$NUM"
    DEST="${DIR}/p${NN}_${SLUG//-/_}.tex"
    TITLE="${TITLE:-TODO title}"
    PTS="${PTS:-TODO pts}"
    if [[ -n "$LO" ]]; then
        HEADER="\\problemheaderlo{${NUM}}{${LO}}{${PTS}}{${TITLE}}"
    else
        HEADER="\\problemheader{${NUM}}{${PTS}}{${TITLE}}"
    fi
fi

[[ -e "$DEST" ]] && { echo "error: $DEST already exists -- refusing to overwrite" >&2; exit 1; }

if [[ $SOLUTIONS -eq 1 ]]; then
    cat > "$DEST" <<EOF
\\input{${PREAMBLE}}
\\input{${MACROS_REL}}

% CONDENSED ANSWER SHEET. Final answers only -- no derivations.
% Assembled by lifting the answerbox from each per-problem file.

\\title{\\vspace{-1.5cm}TODO Course --- TODO Assignment Solutions\\\\
       {\\large TODO subtitle}}
\\author{}
\\date{Fall 2026}

\\begin{document}
\\maketitle
\\vspace{-1.0cm}

%---------------------------------------------------------------------------
\\section*{1. TODO \\normalsize(TODO pts)}

TODO -- lift the answerbox contents from p01.

\\end{document}
EOF
else
    cat > "$DEST" <<EOF
\\input{${PREAMBLE}}
\\input{${MACROS_REL}}

\\begin{document}

${HEADER}

\\subsection*{Problem statement}

TODO -- restate the problem. The solution must be readable without the
assignment PDF beside it.

\\subsection*{Approach}

TODO -- the governing formula or principle, with a citation, and why it applies.
Cite the course material by page: \\srcref{Module 01, PDF p55, slide 32}.
Use \\extref{...} only where the course is genuinely silent.

\\subsection*{Work}

TODO -- every step. Substitute numbers before simplifying. Carry units.

%\\begin{trap}
%TODO -- the plausible shortcut that gives the wrong answer.
%\\end{trap}

\\subsection*{Check}

TODO -- verify by an INDEPENDENT route, not a re-read. Recompute it.

\\subsection*{Answer}

\\begin{answerbox}
TODO -- the result, nothing else. This is what the solutions document lifts.
\\end{answerbox}

\\end{document}
EOF
fi

echo "created $DEST"
echo "  preamble: ${PREAMBLE}  (${depth} levels up)"
echo "  macros:   ${MACROS_REL}"
echo
echo "next:"
echo "  docs/latex/build_tex.sh $DEST"
