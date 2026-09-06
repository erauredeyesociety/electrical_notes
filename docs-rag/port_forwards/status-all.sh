#!/usr/bin/env bash
# status-all.sh — one command that says whether every forward this repo depends
# on is actually usable. Run it before assuming anything is reachable.
#
# It asserts RESPONSE CONTENT, never process liveness. An ssh PID being alive is
# not evidence: a forward to a dead remote accepts TCP all day and serves
# nothing. Every row below is a real HTTP request with an asserted body.
#
#   ./status-all.sh          human-readable table
#   ./status-all.sh --quiet  exit code only (0 = everything WORKING)

set -uo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
QUIET=0; [[ "${1:-}" == "--quiet" ]] && QUIET=1

fails=0
say() { (( QUIET )) || printf '%s\n' "$*"; }

# check_optional <label> <url> <must-contain> <why> -- reports, never fails the run.
check_optional() {
    local label="$1" url="$2" want="$3" why="$4" out code body
    out="$(timeout 20 curl -sS --max-time 15 -o - -w $'\n%{http_code}' "$url" 2>/dev/null)"
    code="${out##*$'\n'}"; body="${out%$'\n'*}"
    if [[ "$code" == "200" ]] && grep -qF "$want" <<<"$body"; then
        say "  $(printf '%-34s' "$label") WORKING"
    else
        say "  $(printf '%-34s' "$label") down — $why"
    fi
    return 0
}

# check <label> <url> <must-contain>
check() {
    local label="$1" url="$2" want="$3" out code body
    out="$(timeout 20 curl -sS --max-time 15 -o - -w $'\n%{http_code}' "$url" 2>/dev/null)"
    code="${out##*$'\n'}"; body="${out%$'\n'*}"
    if [[ "$code" != "200" ]]; then
        say "  $(printf '%-34s' "$label") DOWN      (http=${code:-none})"; fails=$((fails+1)); return 1
    fi
    if ! grep -qF "$want" <<<"$body"; then
        say "  $(printf '%-34s' "$label") STALE     (200, but no '${want}' — wrong service)"
        fails=$((fails+1)); return 1
    fi
    say "  $(printf '%-34s' "$label") WORKING"
    return 0
}

say ""
say "ZeroTier / VPN"
if systemctl is-active --quiet zerotier-one 2>/dev/null; then
    zt="$(ip -4 addr show 2>/dev/null | grep -oE 'inet 10\.231\.[0-9.]+' | head -1)"
    say "  $(printf '%-34s' 'zerotier-one') ${zt:-active, no 10.231.x addr}"
else
    say "  $(printf '%-34s' 'zerotier-one') INACTIVE  — pwnstar forwards cannot work"; fails=$((fails+1))
fi

say ""
say "ResearchHub (pwnstar 10.231.80.91)"
# pwnstar is intentionally SHUT DOWN as of 2026-09-05 (operator, relayed via
# the skytracker session). ResearchHub runs there, so DOWN is EXPECTED, not a
# bug -- fail open to docs-rag + web. Same for the :11436 ollama below.
# Ollama comes from skytracker (:11435) directly, never via pwnstar.
check_optional "researchhub  :5347/health" "http://127.0.0.1:5347/health" '"status":"healthy"' "pwnstar is shut down; expected" 

say ""
say "Ollama — remote only; local must be absent"
# err0r runs NO local Ollama (docs/decisions/0002). :11434 must be SILENT --
# anything answering there is a violation, so it is checked inversely.
if curl -s -m 4 -o /dev/null "http://127.0.0.1:11434/api/tags" 2>/dev/null; then
    say "  $(printf '%-34s' 'local :11434') ⛔ RUNNING — must not be; see ollama-guard.sh"
    fails=$((fails+1))
else
    say "  $(printf '%-34s' 'local :11434') absent (correct)"
fi
check "skytracker   :11435 qwen3:14b"    "http://127.0.0.1:11435/api/tags" 'qwen3:14b'
check_optional "pwnstar      :11436 qwen3.5:9b" "http://127.0.0.1:11436/api/tags" 'qwen3.5:9b' "pwnstar is shut down; expected" 

say ""
if (( fails == 0 )); then
    say "All forwards WORKING."
else
    say "${fails} check(s) not working."
    say ""
    say "Repair:"
    say "  ${SCRIPT_DIR}/rh-tunnel.sh restart        # researchhub"
    say "  ${SCRIPT_DIR}/skytracker-ollama-tunnel.sh up   # DEFAULT ollama (:11435)"
    say "  ${SCRIPT_DIR}/ollama-tunnel.sh restart         # pwnstar ollama (:11436)"

fi
say ""
exit $(( fails > 0 ))
