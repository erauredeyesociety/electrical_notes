# 0002 — No Ollama on err0r. Remote instances only.

**Status:** Accepted · **Date:** 2026-09-05 · **Scope:** this machine (`err0r`), all projects

## Decision

**Ollama does not run on `err0r`. Not on the CPU, and not on the GPU.**

Models run on remote hosts reached through SSH tunnels. If no tunnel is up,
**say so** — do not start a local server to compensate.

**Scope is the `err0r` workstation ONLY — not pwnstar.** pwnstar is the service
host: it runs ollama, docs-rag, ResearchHub and the coordination bus **locally by
design**. This decision constrains err0r, the operator's daily driver. It is not
a fleet-wide ban and must not inhibit local services on pwnstar.
(Scoping clarified by the skytracker_v2 session, 2026-09-05.)

```sh
docs-rag/port_forwards/ollama-guard.sh            # check
docs-rag/port_forwards/ollama-guard.sh --enforce  # check and stop any local server
```

## Context

`err0r` is the operator's daily driver. It runs ArduPilot SITL, browsers, and
editors alongside this work, and has a **6 GB** RTX 3060 Laptop with typically
~4.3 GB free. An Ollama server competes for both the CPU and that card.

Two incidents on 2026-09-05 drove this:

1. An OCR evaluation script — **correctly pinned to CUDA** — took the load
   average to 7.4 and nearly crashed the desktop. `from_pretrained` deserializes
   weights *on the CPU* before `.to("cuda")` is ever reached, and that phase is
   unbounded by default. See
   [`../../ocr_handler/docs/directives/gpu-discipline.md`](../../ocr_handler/docs/directives/gpu-discipline.md).
2. An Ollama server serving docs-rag embeddings sat at ~26% CPU continuously.
   It was genuinely `100% GPU` per `ollama ps` — the CPU was tokenization and
   HTTP overhead, not inference — but the operator's call is that even that
   overhead does not belong on this machine.

**An earlier version of this rule allowed a local embedding model**, on the
grounds that docs-rag needs one. That exception is **withdrawn**: the same
tunnels serve `nomic-embed-text`, so there was never a case for it.

## Where models actually live

| Tunnel | Host | Needs | Carries |
| --- | --- | --- | --- |
| `:11435` | skytracker `155.31.130.52` | **ERAU VPN** | `nomic-embed-text`, `qwen3:14b` |
| `:11436` | pwnstar `10.231.80.91` | ZeroTier | `qwen3.5:9b` (vision), `qwen3:4b`, `llama3.2:3b`, `nomic-embed-text` |

`docs-rag/.env` points at `host.docker.internal:11435`. The skytracker tunnel
binds the Docker bridge as well as `127.0.0.1`, so the container can reach it.

⚠ **pwnstar is not a bigger GPU** — an RTX 2060 with the *same* 6144 MiB, and
typically ~4.8 GB already in use. It is a correctness resource, not a throughput
one. See [`../../docs-rag/port_forwards/README.md`](../../docs-rag/port_forwards/README.md).

## Consequences

- When no tunnel is up, docs-rag **cannot embed**, and that is the correct
  behaviour. Bring a tunnel up; do not work around it.
- `ollama-guard.sh` reports the ERAU VPN state, whether a local server is
  running, and which tunnels are reachable — and exits non-zero for each.
- Any script that wants a model reads `OLLAMA_BASE_URL`. Nothing hardcodes
  `127.0.0.1:11434`.

## A scripting bug this surfaced, worth not repeating

The guard's first VPN check used `ip route | grep -q '^155.31.0.0/16 dev tun'`
under `set -o pipefail`. **It returned a false "VPN down" in 18 of 40 runs.**

`grep -q` exits on its first match, `ip route` then dies of `SIGPIPE`, and
`pipefail` reports the whole pipeline as failed. The failure is timing-
dependent, so it presents as a *flapping VPN* rather than a scripting error —
which is exactly how it was first misread here.

```sh
# WRONG under pipefail — races, silently
ip route | grep -q PATTERN

# RIGHT — capture, then match
routes="$(ip route)"; grep -q PATTERN <<<"$routes"
```

Measured after the fix: 0 of 40 false negatives.

---

**Related:** [`0001-publishing-and-git-are-not-a-concern.md`](0001-publishing-and-git-are-not-a-concern.md) ·
[`../../docs-rag/port_forwards/ollama-guard.sh`](../../docs-rag/port_forwards/ollama-guard.sh) ·
[`../../ocr_handler/docs/directives/gpu-discipline.md`](../../ocr_handler/docs/directives/gpu-discipline.md)
