#!/usr/bin/env bash
# ollama-guard.sh — enforce: NO OLLAMA ON err0r. Remote instances only.
#
#   ./ollama-guard.sh            check; exit 0 only if compliant
#   ./ollama-guard.sh --enforce  check, and STOP any local ollama found
#   ./ollama-guard.sh --vpn      print ERAU VPN state and exit (0 up / 3 down)
#
# ─────────────────────────────────────────────────────────────────────────────
# THE RULE — operator decision, 2026-09-05
#
#   Ollama does not run on this machine. Not on the CPU, and not on the GPU.
#   err0r is the operator's daily driver; an Ollama server here competes with
#   their real work (ArduPilot SITL, browsers, editors) for both CPU and the
#   6 GB card.
#
#   Models run on REMOTE hosts, reached through the tunnels in this folder:
#     :11435  skytracker  155.31.130.52   (needs the ERAU VPN)
#     :11436  pwnstar     10.231.80.91    (needs ZeroTier)
#
#   Anything needing embeddings or generation points at a tunnel. If no tunnel
#   is up, SAY SO -- do not start a local server to compensate. That fallback is
#   what makes the machine unusable, and it is the specific thing this guard
#   exists to prevent.
#
#   Earlier versions of this file allowed a local embedding model "because
#   docs-rag needs one". That exception is withdrawn: the same tunnels serve
#   nomic-embed-text, so there is no case left for a local server.
# ─────────────────────────────────────────────────────────────────────────────

set -uo pipefail

ENFORCE=0; VPN_ONLY=0
for a in "$@"; do
    case "$a" in
        --enforce) ENFORCE=1 ;;
        --vpn)     VPN_ONLY=1 ;;
        -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
        *) echo "unknown option: $a" >&2; exit 2 ;;
    esac
done

ERAU_ROUTE='155.31.0.0/16'

# NOTE: capture, THEN grep. Never `ip route | grep -q` under `set -o pipefail`:
# grep -q exits on first match, ip route dies of SIGPIPE, and pipefail reports
# the whole pipeline as failed. Measured on this box: 18 of 40 runs returned a
# FALSE "VPN down". The bug is timing-dependent, so it looks like a flapping
# link rather than a scripting error.
vpn_up() {
    local routes
    routes="$(ip route 2>/dev/null)"
    grep -q "^${ERAU_ROUTE} dev tun" <<<"$routes"
}

vpn_state() {
    if vpn_up; then
        local addr routes
        routes="$(ip -brief addr show tun0 2>/dev/null)"
        addr="$(awk '{print $3}' <<<"$routes")"
        echo "UP (tun0 ${addr:-?})"
    else
        echo "DOWN"
    fi
}

if (( VPN_ONLY )); then
    echo "ERAU VPN: $(vpn_state)"
    vpn_up && exit 0 || exit 3
fi

echo "ERAU VPN: $(vpn_state)"

# --- rule check: is anything ollama-shaped alive locally? --------------------
procs="$(ps -eo pid,args 2>/dev/null | grep -E '[o]llama serve|[o]llama_llama_server' || true)"
listen="$(ss -tlnH 2>/dev/null | grep -E ':11434\b' || true)"

if [[ -z "$procs" && -z "$listen" ]]; then
    echo "local ollama: NOT RUNNING — compliant"
else
    echo "local ollama: ⛔ RUNNING — violates the no-local-ollama rule"
    [[ -n "$procs"  ]] && sed 's/^/    /' <<<"$procs"
    [[ -n "$listen" ]] && echo "    listening: $(awk '{print $4}' <<<"$listen" | tr '\n' ' ')"
    if (( ENFORCE )); then
        echo "  stopping..."
        pkill -TERM -f 'ollama serve' 2>/dev/null || true
        pkill -TERM -f 'ollama_llama_server' 2>/dev/null || true
        sleep 3
        pkill -KILL -f 'ollama serve' 2>/dev/null || true
        pkill -KILL -f 'ollama_llama_server' 2>/dev/null || true
        pkill -TERM -f 'socat.*11434' 2>/dev/null || true
        echo "  stopped. Re-run to confirm."
    else
        echo "  re-run with --enforce to stop it."
    fi
    exit 1
fi

# --- where models actually live ----------------------------------------------
echo "remote ollama tunnels:"
any_up=0
for spec in "11435 skytracker(155.31.130.52) ERAU-VPN" "11436 pwnstar(10.231.80.91) ZeroTier"; do
    port="${spec%% *}"; rest="${spec#* }"
    code="$(curl -s -m 6 -o /dev/null -w '%{http_code}' "http://127.0.0.1:${port}/api/tags" 2>/dev/null)"
    if [[ "$code" == "200" ]]; then
        printf '  :%s  UP    %s\n' "$port" "$rest"; any_up=1
    else
        printf '  :%s  DOWN  %s\n' "$port" "$rest"
    fi
done

if (( ! any_up )); then
    echo
    echo "⚠ NO remote Ollama is reachable. Nothing needing embeddings or"
    echo "  generation can run right now. Bring a tunnel up:"
    echo "    ./ollama-tunnel.sh up          # pwnstar  (ZeroTier)"
    if ! vpn_up; then
        echo "  The ERAU VPN is DOWN, so :11435 (skytracker) is unreachable"
        echo "  until it is back."
    fi
    echo "  DO NOT start a local ollama to compensate."
    exit 4
fi
exit 0
