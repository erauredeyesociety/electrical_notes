# Port forwards

Tunnels this repo's tooling depends on. **Run `./status-all.sh` before assuming
anything is reachable.**

## ⚠ err0r runs NO local Ollama

Operator decision, 2026-09-05 — see
[`../../docs/decisions/0002-no-local-ollama-on-err0r.md`](../../docs/decisions/0002-no-local-ollama-on-err0r.md).
Models live on remote hosts and reach us through these tunnels. **A local
embedding model is not an exception.**

If no tunnel is up, **say so** — do not start a local server to compensate.
That fallback is what makes the machine unusable.

```sh
./skytracker-ollama-tunnel.sh up      # THE DEFAULT — nomic-embed-text + qwen3:14b
./ollama-guard.sh                     # is anything violating the rule?
./status-all.sh                       # everything at once
```

---

## The one rule

**A live ssh process is not evidence the tunnel works.** A forward to a dead remote accepts TCP all
day and serves nothing; ZeroTier can drop and leave a half-open socket behind. Every check here makes
a real HTTP request and asserts the *body*, never just the status code. This was demonstrated, not
assumed — see [the source runbook](~/sys301_minesweeper/docs/runbooks/researchhub-tunnel.md), where a
decoy forward to the remote Redis port made `nc -z` succeed while `status` still correctly said STALE.

---

## Two remote Ollamas — do not confuse them

Both answer `/api/tags` with HTTP 200, so a naive health check passes against
whichever happens to be listening and queries silently hit the wrong machine.
Each script asserts a **sentinel model** only its host carries.

| Port | Host | Models | Use it for |
| --- | --- | --- | --- |
| `11435` | **skytracker** `155.31.130.52` | `nomic-embed-text`, `qwen3:14b` | **THE DEFAULT.** Embeddings + generation for docs-rag. Needs the ERAU VPN. |
| `11436` | pwnstar `10.231.80.91` | `qwen3.5:9b` (vision), `qwen3:4b`, `qwen3:1.7b`, `llama3.2:3b`, `all-minilm`, `nomic-embed-text` | The only **vision** model — but see the warning below |
| ~~`11434`~~ | ~~local~~ | — | **Nothing. err0r runs no Ollama.** |

`docs-rag/.env` points at `host.docker.internal:11435`. Measured after the
switch: the stack went from `degraded / llm:false` (local had no generation
model) to **`healthy / llm:true`**, so moving off local made it strictly better.

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

### `:11435` — the default, and the two-bind trap

`skytracker-ollama-tunnel.sh` owns this one. It opens **two** forwards, and the
second is the one people forget:

```sh
-L 11435:localhost:11434                # for processes on this host
-L 172.17.0.1:11435:localhost:11434     # for CONTAINERS
```

docs-rag runs in Docker and reaches the host as `host.docker.internal`, which
resolves to the Docker bridge. **A tunnel bound only to `127.0.0.1` is invisible
from inside a container** — the stack comes up, embedding calls fail, and the
ingest reports zero documents with no obvious cause. Verify from a container's
point of view, not just the host's:

```sh
docker run --rm --add-host=host.docker.internal:host-gateway curlimages/curl \
  -s http://host.docker.internal:11435/api/tags | head -c 120
```

Its sentinel is `qwen3:14b`, which only skytracker carries.

### Why `ollama-tunnel.sh` lands on `11436`

It auto-bumps when its preferred port is taken and says so; `:11435` is normally
held by the skytracker tunnel. The port actually in use is the first field of
`.ollama-tunnel.local`:

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

### What its corpus is actually good for — measured 2026-09-06

Ranked results are **not uniformly relevant**, and the difference is by topic, not by phrasing:

| Query axis | Result |
| --- | --- |
| Models, papers, benchmarks | **Strong.** "handwritten mathematical expression recognition open models" returned Uni-MuMER, MathWriting, OmniHandwritingOCR, two HMER surveys and a bidirectionally-trained-transformer paper — 13 hits, nearly all on-topic |
| Software tooling / engineering practice | **Noisy.** "detecting corrupted PDF text layer extraction" returned gold-trading forum threads and Windows support pages; only 2 of 10 hits were software at all |

So: use it for the **model and paper axis**, and corroborate anything it says about tooling. A thin
result on a tooling question is weak evidence of no prior art, not proof of it.

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

`.rh-port` · `.rh-tunnel.pid` · `.rh-tunnel.local` · `.ollama-tunnel.pid` · `.ollama-tunnel.local` · `.skytracker-ollama.pid`

---

**Source:** adapted from `~/sys301_minesweeper/scripts/`, whose runbook carries the full verification
record. `ollama-tunnel.sh`, `skytracker-ollama-tunnel.sh`, `ollama-guard.sh` and `status-all.sh` are new here.
