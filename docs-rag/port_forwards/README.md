# Port forwards

Tunnels this repo's tooling depends on. **Run `./status-all.sh` before assuming anything is reachable.**

```sh
./status-all.sh              # is everything actually usable?
./rh-tunnel.sh restart       # repair ResearchHub
./ollama-tunnel.sh restart   # repair pwnstar Ollama
./ollama-tunnel.sh models    # what pwnstar can run
```

`status-all.sh` exits 0 only when every check passes, so it is scriptable.

---

## The one rule

**A live ssh process is not evidence the tunnel works.** A forward to a dead remote accepts TCP all
day and serves nothing; ZeroTier can drop and leave a half-open socket behind. Every check here makes
a real HTTP request and asserts the *body*, never just the status code. This was demonstrated, not
assumed — see [the source runbook](~/sys301_minesweeper/docs/runbooks/researchhub-tunnel.md), where a
decoy forward to the remote Redis port made `nc -z` succeed while `status` still correctly said STALE.

---

## Three Ollama daemons — do not confuse them

This is the trap. All three answer `/api/tags` with HTTP 200, so a naive health check passes against
whichever one happens to be listening, and queries silently hit the wrong machine.

| Port | Host | Models | Use it for |
| --- | --- | --- | --- |
| `11434` | **local** (this machine) | `nomic-embed-text` only | Embeddings. **No generation model at all.** |
| `11435` | skytracker `155.31.130.52` | `nomic-embed-text`, `qwen3:14b` | Owned by skytracker's stack — see below |
| `11436` | **pwnstar** `10.231.80.91` | `qwen3.5:9b` (vision), `qwen3:4b`, `qwen3:1.7b`, `llama3.2:3b`, `all-minilm`, `nomic-embed-text` | Generation, and the only **vision** model — but see the warning below |

### ⚠ pwnstar is NOT a bigger GPU

The obvious assumption — remote host, therefore more VRAM — is **wrong**, and it
was made here before anyone checked:

| | This laptop | pwnstar |
| --- | --- | --- |
| GPU | RTX 3060 Laptop | **RTX 2060** (older) |
| Total VRAM | 6144 MiB | **6144 MiB — the same** |
| Typically in use | ~1.9 GB | **~4.8 GB** |
| Free | ~4.3 GB | **~1.3 GB** |

It is also heavily loaded (swap exhausted, load averages in the tens). Measured:
`qwen3.5:9b` runs there with only ~1.4 GB resident in VRAM — i.e. mostly on CPU
— at a 4096-token context, taking **~200 s** for one page-sized prompt, while a
200 dpi page is ~3,950 tokens.

**So the tunnel does not lift the 6 GB ceiling on model choice.** It is worth
having for the vision capability and as a correctness cross-check, not for
throughput or for running models that will not fit locally. Verify before
relying on it:

```sh
ssh devel@10.231.80.91 'nvidia-smi --query-gpu=name,memory.total,memory.used --format=csv'
```

`ollama-tunnel.sh` defends against the confusion by asserting a **sentinel model** (`qwen3.5:9b`) that
only pwnstar has. A 200 from the wrong daemon is reported **STALE**, not WORKING. Verified by pointing
the probe at local Ollama: it returned rc=2 (wrong-Ollama) rather than passing.

The script also refuses to bind `11434` outright, since a tunnel there would shadow local Ollama.

> **`:11435` is not ours.** It was established by skytracker's tooling
> (`ssh … -L 11435:localhost:11434 -L 172.17.0.1:11435:… skytracker-dev@155.31.130.52`) and is bound
> to the Docker bridge for containers. `ollama-tunnel.sh` will not touch it — it picks the next free
> port instead, which is why ours landed on **11436**. Do not kill it to "free up" 11435.

### Why `11436` and not `11435`

`ollama-tunnel.sh up` auto-bumps when its preferred port is taken, and says so. The port actually in
use is the first field of `.ollama-tunnel.local`:

```sh
P=$(cut -d' ' -f1 .ollama-tunnel.local)
```

---

## ResearchHub

`:5347` → `researchhub-api` on pwnstar. Health is `{"status":"healthy"}` at `/health`; Swagger at
`/docs`. Query it with `./rh-query.sh "your question"`, which preflights the tunnel and **repairs a
stale one automatically**, so an empty result never gets confused with a dead tunnel.

Exit codes name the fault: `3` TUNNEL_DOWN · `4` REMOTE_UNHEALTHY (ResearchHub is down — *do not touch
the tunnel*) · `5` QUERY_FAILED.

Known broken server-side: `/api/integration/kb/search` returns HTTP 500. Not our machine, not our bug.

---

## Prerequisites

- `zerotier-one` **active**, this host on `10.231.80.x` (currently `10.231.80.161`). If ZeroTier is
  down, every pwnstar forward fails. `status-all.sh` checks this first and says so.
- `~/.ssh/id_git` readable and **not** passphrase-protected — the scripts use `BatchMode=yes` and fail
  fast rather than hanging on a prompt.
- Remote login is `devel` for pwnstar.

## Safety properties

- **Never `pkill ssh`.** `down` kills only the PID in `.ollama-tunnel.pid` / `.rh-tunnel.pid`, and only
  after re-reading `/proc/<pid>/cmdline` to confirm it is still an ssh with our exact forward spec and
  destination. A foreign or recycled PID is **left alive**.
- All pwnstar commands are **read-only**. pwnstar also runs `cars-demo-13`, `engineer360`, `palletai`
  and others: touch none of them.
- If a forward comes up but its probe fails, it is **torn down** rather than reported as a pass.

## State files (gitignored)

`.rh-port` · `.rh-tunnel.pid` · `.rh-tunnel.local` · `.ollama-tunnel.pid` · `.ollama-tunnel.local`

---

**Source:** adapted from `~/sys301_minesweeper/scripts/`, whose runbook carries the full verification
record. `ollama-tunnel.sh` and `status-all.sh` are new here.
