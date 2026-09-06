#!/usr/bin/env bash
# skytracker-ollama-tunnel.sh — forward the skytracker server's Ollama to here.
#
#   ./skytracker-ollama-tunnel.sh up | down | status | restart | models
#
# THIS IS THE DEFAULT OLLAMA FOR THIS MACHINE. err0r runs no local Ollama
# (docs/decisions/0002-no-local-ollama-on-err0r.md); models live on the
# skytracker server and reach us through this tunnel.
#
# ── TWO -L FLAGS, AND WHY THE SECOND ONE MATTERS ─────────────────────────────
#   -L 11435:localhost:11434              for processes on this host
#   -L 172.17.0.1:11435:localhost:11434   for CONTAINERS
#
#   docs-rag runs in Docker and reaches the host as `host.docker.internal`,
#   which resolves to the Docker bridge (172.17.0.1). A tunnel bound only to
#   127.0.0.1 is invisible from inside a container: the stack comes up, the
#   embedding calls fail, and the ingest reports zero documents without an
#   obvious cause. Both binds, always.
#
# ── STALENESS ────────────────────────────────────────────────────────────────
#   An ssh PID being alive proves nothing: a forward to a dead remote accepts
#   TCP all day and serves nothing. `status` makes a real HTTP request AND
#   asserts a model only this host carries, so a reply from some other Ollama
#   cannot pass.
#
# Requires the ERAU VPN (the route to 155.31.0.0/16). Read-only on the remote.

set -uo pipefail

SK_SSH_HOST="${SK_SSH_HOST:-155.31.130.52}"
SK_SSH_USER="${SK_SSH_USER:-skytracker-dev}"
SK_SSH_KEY="${SK_SSH_KEY:-$HOME/.ssh/id_git}"
SK_LOCAL_PORT="${SK_LOCAL_PORT:-11435}"
SK_REMOTE_PORT="${SK_REMOTE_PORT:-11434}"
SK_BRIDGE="${SK_BRIDGE:-172.17.0.1}"          # docker bridge, for containers
# A model only the skytracker host has. Proves we reached the RIGHT Ollama.
SK_SENTINEL="${SK_SENTINEL:-qwen3:14b}"
ERAU_ROUTE='155.31.0.0/16'

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/.skytracker-ollama.pid"

EX_WORKING=0; EX_STALE=2; EX_DOWN=3; EX_UNKNOWN=4; EX_USAGE=64

SSH_OPTS=(
  -o BatchMode=yes -o ConnectTimeout=10
  -o ServerAliveInterval=15 -o ServerAliveCountMax=3
  -o ExitOnForwardFailure=yes -o IdentitiesOnly=yes
  -o StrictHostKeyChecking=accept-new
)
[[ -r "$SK_SSH_KEY" ]] && SSH_OPTS+=(-i "$SK_SSH_KEY") || true

log()  { printf '%s\n' "$*" >&2; }
warn() { printf 'WARN: %s\n' "$*" >&2; }
die()  { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

# Capture THEN grep. `ip route | grep -q` under `set -o pipefail` races: grep -q
# exits on first match, ip route dies of SIGPIPE, pipefail calls the pipeline
# failed. Measured 18/40 false negatives on this box -- it looks like a flapping
# VPN rather than a scripting bug, which is how it was first misdiagnosed.
vpn_up() {
    local routes; routes="$(ip route 2>/dev/null)"
    grep -q "^${ERAU_ROUTE} dev tun" <<<"$routes"
}

probe() {  # 200 AND the sentinel model
    local port="$1" out code body
    command -v curl >/dev/null 2>&1 || return 3
    out="$(timeout 20 curl -sS --max-time 15 -o - -w $'\n%{http_code}' \
           "http://127.0.0.1:${port}/api/tags" 2>/dev/null)" || return 1
    code="${out##*$'\n'}"; body="${out%$'\n'*}"
    [[ "$code" == "200" ]] || return 1
    grep -qF "$SK_SENTINEL" <<<"$body" || return 2   # wrong Ollama
    return 0
}

pid_is_ours() {
    local pid="$1"
    [[ -n "$pid" && -d "/proc/$pid" ]] || return 1
    local cmd; cmd="$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null || true)"
    [[ "$cmd" == ssh\ * ]] || return 1
    [[ "$cmd" == *"-L ${SK_LOCAL_PORT}:localhost:${SK_REMOTE_PORT}"* ]] || return 1
    [[ "$cmd" == *"${SK_SSH_USER}@${SK_SSH_HOST}"* ]] || return 1
    return 0
}

kill_ours() {
    local pid=""; [[ -s "$PID_FILE" ]] && pid="$(cat "$PID_FILE")"
    if [[ -z "$pid" ]]; then log "no pidfile — nothing of ours to kill"; return 0; fi
    if pid_is_ours "$pid"; then
        log "killing our tunnel pid=$pid"
        kill -TERM "$pid" 2>/dev/null || true
        for _ in $(seq 1 10); do [[ -d "/proc/$pid" ]] || break; sleep 0.5; done
        [[ -d "/proc/$pid" ]] && kill -KILL "$pid" 2>/dev/null || true
    else
        # NEVER pkill ssh -- the operator has their own sessions open.
        warn "pid $pid is not our tunnel (gone, or PID reused) — leaving it alone"
    fi
    rm -f "$PID_FILE"
}

cmd_status() {
    local quiet="${1:-}"; local say=log; [[ "$quiet" == "--quiet" ]] && say=:
    local pid=""; [[ -s "$PID_FILE" ]] && pid="$(cat "$PID_FILE")"

    # An untracked tunnel (started by hand, or by a previous session) is still a
    # working tunnel. Report it rather than pretending nothing is there.
    if [[ -z "$pid" ]] || ! pid_is_ours "$pid"; then
        if probe "$SK_LOCAL_PORT"; then
            $say "STATUS: WORKING (untracked) — something else established :${SK_LOCAL_PORT}"
            [[ "$quiet" == "--quiet" ]] || echo "WORKING"; return $EX_WORKING
        fi
        $say "STATUS: DOWN — no tracked tunnel and nothing answering on :${SK_LOCAL_PORT}"
        [[ "$quiet" == "--quiet" ]] || echo "DOWN"; return $EX_DOWN
    fi

    local rc=0; probe "$SK_LOCAL_PORT" || rc=$?
    case "$rc" in
      0) $say "STATUS: WORKING — pid ${pid}, :${SK_LOCAL_PORT} serves ${SK_SENTINEL}"
         [[ "$quiet" == "--quiet" ]] || echo "WORKING"; return $EX_WORKING ;;
      2) $say "STATUS: STALE — :${SK_LOCAL_PORT} answered WITHOUT ${SK_SENTINEL}: wrong Ollama. Repair: $0 restart"
         [[ "$quiet" == "--quiet" ]] || echo "STALE"; return $EX_STALE ;;
      3) $say "STATUS: UNKNOWN — curl missing; pid liveness is NOT proof"
         [[ "$quiet" == "--quiet" ]] || echo "UNKNOWN"; return $EX_UNKNOWN ;;
      *) $say "STATUS: STALE — pid ${pid} alive but nothing usable answers. Repair: $0 restart"
         [[ "$quiet" == "--quiet" ]] || echo "STALE"; return $EX_STALE ;;
    esac
}

cmd_up() {
    local rc=0; cmd_status --quiet || rc=$?
    if (( rc == EX_WORKING )); then log "already WORKING on :${SK_LOCAL_PORT} — nothing changed"; return 0; fi
    (( rc == EX_STALE )) && { log "STALE — tearing down first"; kill_ours; }

    vpn_up || die "ERAU VPN is DOWN — ${SK_SSH_HOST} is unreachable without it.
       Bring the VPN up and re-run. Do NOT start a local ollama to compensate."

    if ss -tlnH "sport = :${SK_LOCAL_PORT}" 2>/dev/null | grep -q .; then
        die "port ${SK_LOCAL_PORT} is already bound by something we do not track.
       Inspect with: ss -tlnp | grep ${SK_LOCAL_PORT}"
    fi

    log "ssh -f -N -L ${SK_LOCAL_PORT}:localhost:${SK_REMOTE_PORT} -L ${SK_BRIDGE}:${SK_LOCAL_PORT}:localhost:${SK_REMOTE_PORT} ${SK_SSH_USER}@${SK_SSH_HOST}"
    timeout 30 ssh -f -N \
        -L "${SK_LOCAL_PORT}:localhost:${SK_REMOTE_PORT}" \
        -L "${SK_BRIDGE}:${SK_LOCAL_PORT}:localhost:${SK_REMOTE_PORT}" \
        "${SSH_OPTS[@]}" "${SK_SSH_USER}@${SK_SSH_HOST}" \
      || die "ssh failed to establish the forward (host unreachable, key rejected, or port in use)"

    local pid=""
    for _ in $(seq 1 10); do
        # ^ssh anchors to the ssh process, not the `timeout ssh ...` wrapper.
        pid="$(pgrep -u "$(id -u)" -f "^ssh .*-L ${SK_LOCAL_PORT}:localhost:${SK_REMOTE_PORT} .*${SK_SSH_USER}@${SK_SSH_HOST}" | head -n1 || true)"
        [[ -n "$pid" ]] && break; sleep 0.5
    done
    [[ -n "$pid" ]] || die "forward launched but its PID could not be identified — refusing to track an unknown process"
    printf '%s\n' "$pid" > "$PID_FILE"

    local prc=0; probe "$SK_LOCAL_PORT" || prc=$?
    case "$prc" in
      0) log "STATUS: WORKING — http://127.0.0.1:${SK_LOCAL_PORT} and ${SK_BRIDGE}:${SK_LOCAL_PORT} (pid $pid)"; return 0 ;;
      2) warn "answered WITHOUT ${SK_SENTINEL} — not the skytracker Ollama. Tearing down."; kill_ours; return $EX_STALE ;;
      *) warn "forward came up but the probe FAILED — tearing down rather than reporting a pass"; kill_ours; return $EX_DOWN ;;
    esac
}

cmd_models() {
    probe "$SK_LOCAL_PORT" || die "tunnel not working — run: $0 up"
    curl -s -m 15 "http://127.0.0.1:${SK_LOCAL_PORT}/api/tags" | python3 -c '
import sys, json
for m in json.load(sys.stdin).get("models", []):
    d = m.get("details", {})
    print("  %-26s %6s %6.2f GB" % (m["name"], d.get("parameter_size","?"), m["size"]/1e9))'
}

usage() {
    cat >&2 <<EOF
usage: $0 {up|down|status|restart|models}

Forwards the skytracker server's Ollama to :${SK_LOCAL_PORT} on this host AND on
the Docker bridge (${SK_BRIDGE}), so containers can reach it too.

This machine runs NO local Ollama. If this tunnel is down, say so — do not
start a local server to compensate.

env: SK_SSH_HOST=$SK_SSH_HOST SK_SSH_USER=$SK_SSH_USER SK_LOCAL_PORT=$SK_LOCAL_PORT
     SK_SENTINEL=$SK_SENTINEL
exit: 0 WORKING · 2 STALE · 3 DOWN · 4 UNKNOWN · 64 usage
EOF
    exit $EX_USAGE
}

case "${1:-}" in
  up)      shift; cmd_up "$@" ;;
  down)    shift; kill_ours; log "STATUS: DOWN" ;;
  status)  shift; cmd_status "$@" ;;
  restart) shift; kill_ours; cmd_up ;;
  models)  shift; cmd_models "$@" ;;
  *)       usage ;;
esac
