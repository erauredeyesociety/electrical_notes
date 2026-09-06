#!/usr/bin/env python3
"""One GPU job at a time, and never let model loading eat the whole machine.

    from tools.gpu_lock import gpu_session
    with gpu_session("paddleocr-vl") as dev:
        model = AutoModel.from_pretrained(...).to(dev)

WHY THIS EXISTS
    On 2026-09-05 an evaluation script pinned correctly to CUDA and still drove
    the operator's machine to load average 7.4 and near-crash. It was not a CPU
    fallback -- `from_pretrained` deserializes safetensors and converts dtypes
    ON THE CPU, before `.to("cuda")` is ever reached. Run concurrently with four
    other agents and an Ollama server, that phase saturated all 8 cores. The GPU
    was idle of it the whole time.

    Two things follow, and both are enforced here rather than written down and
    forgotten:

      1. CAP THE CPU DURING LOAD. torch defaults to ~half the cores; on a shared
         desktop that is far too many. This pins it low so a load spike cannot
         take the machine down.
      2. SERIALISE GPU WORK. One job at a time, via a lock file. An earlier
         session already lost a run to an OOM caused by a concurrent 1318 MiB
         process on this 6 GB card. Two jobs do not fit; queueing is not a
         slowdown, it is the only way both finish.

    It also refuses to start when the GPU is already too full to succeed, rather
    than OOMing halfway through and wasting the load time.
"""

from __future__ import annotations

import contextlib
import fcntl
import os
import subprocess
import sys
import time
from pathlib import Path

LOCK = Path(os.environ.get("OCR_GPU_LOCK", "/tmp/ocr_handler_gpu.lock"))

# Leave the desktop responsive. 8 cores here; 3 keeps loading brisk while still
# leaving the machine usable. Override with OCR_CPU_THREADS if a box is idle.
CPU_THREADS = int(os.environ.get("OCR_CPU_THREADS", "3"))

# Minimum free VRAM to even attempt a job, MiB. Below this a load will OOM after
# paying the full CPU cost, which is the worst outcome.
MIN_FREE_MIB = int(os.environ.get("OCR_MIN_FREE_MIB", "3000"))


def cap_cpu_threads(n: int = CPU_THREADS) -> None:
    """Limit CPU parallelism. MUST run before torch/numpy are imported --
    the thread-pool env vars are read at import time, not at call time."""
    for var in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
        os.environ.setdefault(var, str(n))
    # Helps the allocator on a small card; measured worth ~1.1 GiB of peak.
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")


def free_vram_mib() -> tuple[int | None, str]:
    """Free VRAM in MiB, and WHY when it could not be determined.

    Returns `(mib, reason)`. `mib` is None exactly when the probe failed, and
    `reason` then says which way -- never an empty string, because the caller
    has to be able to TELL the user why the guard could not run.

    Two probes, in this order, and the order is the point:

      1. torch's CUDA path (`torch.cuda.mem_get_info`) -- works even when NVML
         is broken, and NVML *is* broken on the deployment box (Quadro RTX 5000:
         kernel module 580.159.03 vs userspace 580.173.02, so every `nvidia-smi`
         query fails while /dev/nvidia* and the CUDA path are fine). Measured
         2026-09-06. Imported lazily: this module must stay importable on a host
         with no torch.
      2. `nvidia-smi` -- the original probe, kept as the fallback for a host
         that has a working NVML but no torch.

    HISTORY, so this is not "simplified" back: this function used to return a
    bare None on failure and `gpu_session` guarded with
    `if free is not None and free < MIN_FREE_MIB`. On any host where the probe
    failed, that check was skipped **silently** -- the guard its own docstring
    promised did not run, and nothing said so. That is the failure this project
    exists to catch, sitting inside its own safety code.
    """
    try:
        import torch  # lazy: a no-torch host must still import this module
        if torch.cuda.is_available():
            free_b, _total_b = torch.cuda.mem_get_info()
            return free_b // (1024 * 1024), "torch.cuda.mem_get_info"
    except Exception as exc:
        torch_why = f"torch probe failed ({type(exc).__name__})"
    else:
        torch_why = "torch present but reports no CUDA device"

    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=memory.free", "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=15)
        if out.returncode != 0:
            err = (out.stderr or "").strip().splitlines()
            return None, f"{torch_why}; nvidia-smi rc={out.returncode}" + (
                f" ({err[0]})" if err else "")
        return int(out.stdout.strip().splitlines()[0]), "nvidia-smi"
    except Exception as exc:
        return None, f"{torch_why}; nvidia-smi unusable ({type(exc).__name__})"


@contextlib.contextmanager
def gpu_session(label: str = "job", wait: bool = True, timeout_s: int = 3600):
    """Hold the GPU lock for the duration, with CPU threads capped.

    Yields the device string to use. Blocks until the lock is free (or fails
    fast with wait=False). Refuses to start if free VRAM is below MIN_FREE_MIB.
    """
    cap_cpu_threads()

    LOCK.touch(exist_ok=True)
    fh = LOCK.open("r+")
    start = time.monotonic()
    while True:
        try:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except BlockingIOError:
            if not wait:
                fh.close()
                raise RuntimeError(
                    f"another GPU job holds {LOCK} -- refusing to run two at once")
            if time.monotonic() - start > timeout_s:
                fh.close()
                raise TimeoutError(f"waited {timeout_s}s for {LOCK}")
            held = fh.read().strip() or "unknown"
            fh.seek(0)
            print(f"[gpu_lock] waiting for '{held}' to finish...", file=sys.stderr)
            time.sleep(10)

    free, how = free_vram_mib()
    if free is None:
        # UNKNOWN IS NOT OK. Proceed -- refusing here would make the tool
        # useless on the deployment box, where NVML is broken -- but say so
        # loudly and name the reason, so a later OOM is not a surprise and
        # nobody reads a silent pass as a checked one.
        print(f"[gpu_lock] !! free VRAM UNKNOWN ({how}) -- the {MIN_FREE_MIB} MiB "
              f"guard is NOT running for '{label}'. An OOM here is unguarded.",
              file=sys.stderr)
    elif free < MIN_FREE_MIB:
        fcntl.flock(fh, fcntl.LOCK_UN); fh.close()
        raise RuntimeError(
            f"only {free} MiB free VRAM (via {how}), need {MIN_FREE_MIB}. Something "
            f"else is using the GPU. Refusing rather than OOMing after paying the "
            f"CPU load cost.")

    fh.seek(0); fh.truncate()
    fh.write(f"{label} pid={os.getpid()} since={time.strftime('%H:%M:%S')}\n")
    fh.flush()
    print(f"[gpu_lock] '{label}' holding the GPU "
          f"({free if free is not None else '?'} MiB free, "
          f"CPU threads capped to {CPU_THREADS})", file=sys.stderr)
    try:
        yield "cuda"
    finally:
        fh.seek(0); fh.truncate(); fh.flush()
        fcntl.flock(fh, fcntl.LOCK_UN)
        fh.close()
        print(f"[gpu_lock] '{label}' released the GPU", file=sys.stderr)


if __name__ == "__main__":
    free, how = free_vram_mib()
    print(f"free VRAM: {free} MiB (via {how})" if free is not None
          else f"free VRAM: UNKNOWN -- {how}\n"
               f"           the {MIN_FREE_MIB} MiB pre-flight guard will NOT run here")
    print(f"lock file: {LOCK} ({'held' if LOCK.exists() and LOCK.read_text().strip() else 'free'})")
    if LOCK.exists() and LOCK.read_text().strip():
        print(f"  holder: {LOCK.read_text().strip()}")
