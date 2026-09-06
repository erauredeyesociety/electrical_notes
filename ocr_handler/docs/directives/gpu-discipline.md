# Directive — GPU discipline

**This machine is the operator's daily driver.** A job that saturates it is not
a slow job, it is a broken one. On 2026-09-05 an evaluation script drove the
load average to **7.4** and nearly crashed the desktop.

---

## The rule

**Every GPU script goes through [`tools/gpu_lock.py`](../../tools/gpu_lock.py).**

```python
from tools.gpu_lock import gpu_session

with gpu_session("paddleocr-vl") as dev:
    model = AutoModelForImageTextToText.from_pretrained(MODEL).to(dev)
```

It caps CPU threads, serialises GPU work behind a lock file, and refuses to
start when the card is already too full.

---

## Why pinning to CUDA is not enough

The 2026-09-05 script was **written correctly**: `.to("cuda")`, CUDA available,
`PYTORCH_CUDA_ALLOC_CONF` set. It still took the machine down, and understanding
why is the whole point of this directive.

**`from_pretrained` does its work on the CPU, before `.to("cuda")` is ever
reached** — deserializing safetensors, converting dtypes. `nvidia-smi` showed
the GPU *idle of it* the entire time it was burning 98% CPU. Loading from a
32 GB HuggingFace cache, with torch defaulting to ~half the cores, alongside
four other agents and an Ollama server, that phase saturated all 8 cores.

> **"It's on the GPU" describes the compute, not the load.** The load phase is
> CPU-bound, unbounded by default, and happens every single run.

---

## The three guards, and what each prevents

| Guard | Default | Prevents |
| --- | --- | --- |
| **Cap CPU threads** | 3 of 8 | The load phase taking the desktop down |
| **Serialise on a lock** | one job | OOM from two jobs on a 6 GB card |
| **Pre-flight free VRAM** | ≥ 3000 MiB | Paying the full CPU load cost, then OOMing |

**Thread caps must be set before torch or numpy are imported** — the thread-pool
environment variables are read at import time, not at call time. `gpu_lock`
does this in `cap_cpu_threads()`; calling it late silently does nothing.

**Serialising is not a slowdown.** This card has 6144 MiB, ~4.3 GB typically
free. Two model jobs do not fit. An earlier session lost a run to an OOM caused
by a concurrent 1318 MiB process. Queued, both finish; parallel, neither does.

---

## Before starting any GPU work

```sh
python3 tools/gpu_lock.py     # free VRAM + who holds the lock
nvidia-smi                    # what is actually resident
uptime                        # load average -- if already >4, wait
```

Ollama counts. It runs on this GPU (~1850 MiB with an embedding model resident)
and is often busy serving the docs-rag ingest.

## If the machine is struggling

```sh
ps -eo pcpu,rss,comm,args --sort=-pcpu | head
```

Kill the offending PID, then stop the agent that spawned it — otherwise it
restarts the job. Killing the process alone is not enough; that was observed on
2026-09-05, where the script came straight back until the agent itself was
stopped.

---

**Related:** [`../../tools/gpu_lock.py`](../../tools/gpu_lock.py) ·
[`INDEX.md`](INDEX.md) ·
[`../research/engine-landscape-2026-09.md`](../research/engine-landscape-2026-09.md)

---

## ⚠ The VRAM pre-flight guard was a no-op on the deployment target — fixed 2026-09-06

`tools/gpu_lock.py`'s `free_vram_mib()` shelled to `nvidia-smi` and returned a bare `None` on any
failure, and `gpu_session` guarded with `if free is not None and free < MIN_FREE_MIB`. So on a host
where the probe failed, **the guard its own docstring promised simply did not run, and nothing said
so.** That is precisely the silent-success failure this project exists to catch, sitting inside its own
safety code.

It matters because the probe **does** fail on the deployment box: the Quadro RTX 5000 host has a
driver/library mismatch (kernel module `580.159.03` vs userspace `nvidia-utils` `580.173.02`), so every
`nvidia-smi` query returns `Failed to initialize NVML`. Measured 2026-09-06.

Two changes:

1. **`torch.cuda.mem_get_info` is tried first**, falling back to `nvidia-smi`. The CUDA path is
   unaffected by a broken NVML — `/dev/nvidia*` are all present and Ollama on that host is verifiably
   100% GPU-resident — so on the target the guard now **actually works** rather than being skipped.
2. **The return type is `(mib, reason)`, and unknown is loud.** `free_vram_mib()` can no longer say
   "unknown" without saying *why*, and `gpu_session` prints
   `!! free VRAM UNKNOWN (<reason>) -- the 3000 MiB guard is NOT running` before proceeding.

It **proceeds** rather than refusing, deliberately: refusing on an unmeasurable host would make the tool
useless on the very machine the head-to-head runs on. But an unguarded run now announces itself, so a
later OOM is not a surprise and nobody reads a silent pass as a checked one.

Found by the engine-backends design pass while reading the module for a different reason —
[../plans/engine-backends.md](../plans/engine-backends.md).
