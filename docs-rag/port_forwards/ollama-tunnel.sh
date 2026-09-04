#!/usr/bin/env bash
# ollama-tunnel.sh — SSH port-forward from this host to the Ollama API on pwnstar.
#
# Adapted from rh-tunnel.sh (sys301_minesweeper) and carrying the same doctrine:
# an ssh PID being alive PROVES NOTHING. The forward is only WORKING when a real
# HTTP request through the local port returns a known-correct response.
#
# THE EXTRA HAZARD HERE, which rh-tunnel.sh does not have:
#   This host runs its OWN Ollama on 127.0.0.1:11434. A naive health check
#   ("does /api/tags return 200?") passes against the LOCAL daemon just as
#   happily as against the remote one. If the tunnel dies and something rebinds
#   the port -- or if the local port is misconfigured to 11434 -- a liveness
#   check would report WORKING while every subsequent query silently hit the
#   wrong machine, which has ONE embedding model and no generation model at all.
#
#   So the probe asserts a model that ONLY THE REMOTE HAS (RH_SENTINEL_MODEL).
#   Local Ollama serves only nomic-embed-text; pwnstar serves qwen3.5:9b. A
#   response lacking the sentinel is treated as STALE, not as a pass.
#
# Read-only against pwnstar. Never runs a git mutation. Never `pkill ssh`.
#
# Subcommands: up | down | status | restart | models

set -euo pipefail

# ---------------------------------------------------------------- configuration (env-overridable)
OL_SSH_HOST="${OL_SSH_HOST:-10.231.80.91}"        # pwnstar, over ZeroTier
OL_SSH_USER="${OL_SSH_USER:-devel}"
OL_SSH_KEY="${OL_SSH_KEY:-$HOME/.ssh/id_git}"
OL_REMOTE_PORT="${OL_REMOTE_PORT:-11434}"         # Ollama on pwnstar
OL_LOCAL_PORT="${OL_LOCAL_PORT:-11435}"           # NOT 11434 -- that is local Ollama
OL_HEALTH_PATH="${OL_HEALTH_PATH:-/api/tags}"
# The discriminator. A model the LOCAL daemon does not have, so a response from
# the wrong Ollama cannot masquerade as a healthy tunnel.
OL_SENTINEL_MODEL="${OL_SENTINEL_MODEL:-qwen3.5:9b}"

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/.ollama-tunnel.pid"
LOCAL_FILE="$SCRIPT_DIR/.ollama-tunnel.local"     # "<local-port> <remote-port>"

EX_WORKING=0; EX_STALE=2; EX_DOWN=3; EX_UNKNOWN=4; EX_USAGE=64

SSH_OPTS=(
  -o BatchMode=yes
  -o ConnectTimeout=10
  -o ServerAliveInterval=15
  -o ServerAliveCountMax=3
  -o ExitOnForwardFailure=yes
  -o IdentitiesOnly=yes
  -o StrictHostKeyChecking=accept-new
)
[[ -r "$OL_SSH_KEY" ]] && SSH_OPTS+=(-i "$OL_SSH_KEY") || true

log()  { printf '%s\n' "$*" >&2; }
warn() { printf 'WARN: %s\n' "$*" >&2; }
die()  { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

port_in_use() { ss -tlnH "sport = :$1" 2>/dev/null | grep -q .; }

pick_local_port() {
  local p="$OL_LOCAL_PORT"
  for _ in $(seq 1 40); do
    port_in_use "$p" || { printf '%s' "$p"; return 0; }
    p=$((p + 1))
  done
  die "no free local port in ${OL_LOCAL_PORT}..$((OL_LOCAL_PORT + 39))"
}

# --------------------------------------------------------------------------------------- probe
# 200 AND the sentinel model present. Anything else is a failure, including a
# perfectly healthy response from the WRONG Ollama.
probe_local() {
  local port="$1" out code body
  command -v curl >/dev/null 2>&1 || return 3
  out="$(timeout 20 curl -sS --max-time 15 -o - -w $'\n%{http_code}' \
         "http://127.0.0.1:${port}${OL_HEALTH_PATH}" 2>/dev/null)" || return 1
  code="${out##*$'\n'}"; body="${out%$'\n'*}"
  [[ "$code" == "200" ]] || return 1
  grep -qF "$OL_SENTINEL_MODEL" <<<"$body" || return 2   # 2 = wrong Ollama
  return 0
}

tunnel_cmdline_pattern() { printf -- '-L %s:localhost:%s' "$1" "$2"; }

pid_is_our_tunnel() {
  local pid="$1" want; want="$(tunnel_cmdline_pattern "$2" "$3")"
  [[ -n "$pid" && -d "/proc/$pid" ]] || return 1
  local cmd; cmd="$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null || true)"
  [[ "$cmd" == ssh\ * ]] || return 1        # argv[0] must BE ssh, not `timeout ssh ...`
  [[ "$cmd" == *"$want"* ]] || return 1
  [[ "$cmd" == *"${OL_SSH_USER}@${OL_SSH_HOST}"* ]] || return 1
  return 0
}

read_state() {
  TUN_PID=""; TUN_LOCAL=""; TUN_REMOTE=""
  [[ -s "$PID_FILE" ]] && TUN_PID="$(cat "$PID_FILE" 2>/dev/null || true)"
  [[ -s "$LOCAL_FILE" ]] && { read -r TUN_LOCAL TUN_REMOTE < "$LOCAL_FILE" || true; }
  TUN_LOCAL="${TUN_LOCAL:-}"; TUN_REMOTE="${TUN_REMOTE:-}"
}

kill_our_tunnel() {
  read_state
  if [[ -z "$TUN_PID" ]]; then rm -f "$LOCAL_FILE"; log "no pidfile — nothing of ours to kill"; return 0; fi
  if pid_is_our_tunnel "$TUN_PID" "$TUN_LOCAL" "$TUN_REMOTE"; then
    log "killing our ssh tunnel pid=$TUN_PID (-L ${TUN_LOCAL}:localhost:${TUN_REMOTE})"
    kill -TERM "$TUN_PID" 2>/dev/null || true
    for _ in $(seq 1 10); do [[ -d "/proc/$TUN_PID" ]] || break; sleep 0.5; done
    [[ -d "/proc/$TUN_PID" ]] && { warn "pid $TUN_PID ignored SIGTERM; SIGKILL"; kill -KILL "$TUN_PID" 2>/dev/null || true; }
  else
    warn "pid $TUN_PID is NOT our tunnel (gone, or PID reused) — leaving it alone"
  fi
  rm -f "$PID_FILE" "$LOCAL_FILE"
}

cmd_up() {
  local rc=0
  cmd_status --quiet || rc=$?
  if (( rc == EX_WORKING )); then
    read_state; log "already WORKING on http://127.0.0.1:${TUN_LOCAL} (pid $TUN_PID) — nothing changed"
    return $EX_WORKING
  fi
  (( rc == EX_STALE )) && { log "existing tunnel is STALE — tearing down first"; kill_our_tunnel; } || {
    read_state; [[ -n "${TUN_PID:-}" ]] && kill_our_tunnel || true; }

  local local_port; local_port="$(pick_local_port)"
  [[ "$local_port" == "$OL_LOCAL_PORT" ]] || log "local port $OL_LOCAL_PORT busy; using $local_port"
  if [[ "$local_port" == "11434" ]]; then
    die "refusing to bind 11434 — that is LOCAL Ollama; a tunnel there would shadow it"
  fi

  log "ssh -f -N -L ${local_port}:localhost:${OL_REMOTE_PORT} ${OL_SSH_USER}@${OL_SSH_HOST}"
  timeout 30 ssh -f -N -L "${local_port}:localhost:${OL_REMOTE_PORT}" "${SSH_OPTS[@]}" \
      "${OL_SSH_USER}@${OL_SSH_HOST}" \
    || die "ssh failed to establish the forward (host unreachable, key rejected, or port in use)"

  local pid=""
  for _ in $(seq 1 10); do
    pid="$(pgrep -u "$(id -u)" -f "^ssh .*-L ${local_port}:localhost:${OL_REMOTE_PORT} .*${OL_SSH_USER}@${OL_SSH_HOST}" | head -n1 || true)"
    [[ -n "$pid" ]] && break
    sleep 0.5
  done
  [[ -n "$pid" ]] || die "forward launched but its PID could not be identified — refusing to track an unknown process"

  printf '%s\n' "$pid" > "$PID_FILE"
  printf '%s %s\n' "$local_port" "$OL_REMOTE_PORT" > "$LOCAL_FILE"

  local prc=0; probe_local "$local_port" || prc=$?
  case "$prc" in
    0) log "STATUS: WORKING — http://127.0.0.1:${local_port} -> ${OL_SSH_HOST}:${OL_REMOTE_PORT} (pid $pid)"
       return $EX_WORKING ;;
    2) warn "the port answered but WITHOUT ${OL_SENTINEL_MODEL} — that is not pwnstar's Ollama. Tearing down."
       kill_our_tunnel; return $EX_STALE ;;
    *) warn "forward came up but the health probe FAILED — tearing down rather than reporting a pass"
       kill_our_tunnel; log "STATUS: DOWN"; return $EX_DOWN ;;
  esac
}

cmd_down() { kill_our_tunnel; log "STATUS: DOWN"; return 0; }

cmd_status() {
  local quiet="${1:-}"
  read_state
  local say=log; [[ "$quiet" == "--quiet" ]] && say=:

  if [[ -z "${TUN_PID:-}" || -z "${TUN_LOCAL:-}" ]]; then
    $say "STATUS: DOWN — no tracked tunnel (${PID_FILE} absent or empty)"
    [[ "$quiet" == "--quiet" ]] || echo "DOWN"; return $EX_DOWN
  fi
  if ! pid_is_our_tunnel "$TUN_PID" "$TUN_LOCAL" "${TUN_REMOTE:-}"; then
    $say "STATUS: DOWN — pid ${TUN_PID} is not our tunnel any more (exited, or PID reused)"
    [[ "$quiet" == "--quiet" ]] || echo "DOWN"; return $EX_DOWN
  fi

  local rc=0; probe_local "$TUN_LOCAL" || rc=$?
  case "$rc" in
    0) $say "STATUS: WORKING — pid ${TUN_PID}, http://127.0.0.1:${TUN_LOCAL}${OL_HEALTH_PATH} returned 200 + ${OL_SENTINEL_MODEL}"
       [[ "$quiet" == "--quiet" ]] || echo "WORKING"; return $EX_WORKING ;;
    2) $say "STATUS: STALE — 127.0.0.1:${TUN_LOCAL} answered but WITHOUT ${OL_SENTINEL_MODEL}. That is the WRONG Ollama (probably this host's own). Repair: $0 restart"
       [[ "$quiet" == "--quiet" ]] || echo "STALE"; return $EX_STALE ;;
    3) $say "STATUS: UNKNOWN — curl is missing, so the tunnel cannot be proven. Liveness of pid ${TUN_PID} is NOT proof."
       [[ "$quiet" == "--quiet" ]] || echo "UNKNOWN"; return $EX_UNKNOWN ;;
    *) $say "STATUS: STALE — pid ${TUN_PID} is alive but nothing usable answers on 127.0.0.1:${TUN_LOCAL}. Repair: $0 restart"
       [[ "$quiet" == "--quiet" ]] || echo "STALE"; return $EX_STALE ;;
  esac
}

cmd_restart() { kill_our_tunnel; cmd_up; }

# List the models reachable THROUGH THE TUNNEL, so the output cannot be local Ollama's.
cmd_models() {
  read_state
  [[ -n "${TUN_LOCAL:-}" ]] || die "no tunnel — run: $0 up"
  # No f-strings here: nested quotes inside an f-string expression are a syntax
  # error before Python 3.12, and this must run on whatever python3 is present.
  curl -s -m 15 "http://127.0.0.1:${TUN_LOCAL}/api/tags" \
    | python3 -c 'import sys,json
d = json.load(sys.stdin)
for m in d.get("models", []):
    det  = m.get("details", {})
    caps = ",".join(m.get("capabilities", [])) or "-"
    print("  %-24s %6s  %5.2f GB  %s" % (
        m["name"], det.get("parameter_size", "?"), m["size"] / 1e9, caps))'
}

usage() {
  cat >&2 <<EOF
usage: $0 {up|down|status|restart|models}

  up        establish the forward (idempotent; repairs a STALE tunnel first)
  down      kill ONLY our tracked ssh process and clear state
  status    print WORKING / STALE / DOWN / UNKNOWN; exit 0 only for WORKING
  restart   down + up
  models    list models reachable through the tunnel

The probe asserts ${OL_SENTINEL_MODEL} is present, because this host runs its own
Ollama on 11434 and a 200 from the wrong daemon must not count as a pass.

env: OL_SSH_HOST=$OL_SSH_HOST OL_SSH_USER=$OL_SSH_USER OL_SSH_KEY=$OL_SSH_KEY
     OL_LOCAL_PORT=$OL_LOCAL_PORT OL_REMOTE_PORT=$OL_REMOTE_PORT
     OL_SENTINEL_MODEL=$OL_SENTINEL_MODEL
exit codes: 0 WORKING · 2 STALE · 3 DOWN · 4 UNKNOWN · 64 usage
EOF
  exit $EX_USAGE
}

case "${1:-}" in
  up)      shift; cmd_up "$@" ;;
  down)    shift; cmd_down "$@" ;;
  status)  shift; cmd_status "$@" ;;
  restart) shift; cmd_restart "$@" ;;
  models)  shift; cmd_models "$@" ;;
  *)       usage ;;
esac
