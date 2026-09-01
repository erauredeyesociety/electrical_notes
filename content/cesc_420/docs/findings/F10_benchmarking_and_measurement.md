# F10 · Benchmarking and Performance Measurement

Supports [IR-23](../01_idea_register.md#ir-23--performance-benchmarking-and-instrumentation-harness) and [DR-05](../03_decision_record.md#dr-05--benchmarking-is-measurement-not-simulation). This is the evidence base for the proposal's claim that *network throughput, delay and computational effort* are what make heterogeneous coordination hard.

Several numbers below come from **experiments run on a 2026 Intel i7-11370H during this research pass**, not from literature. They are marked *(measured)* and are reproducible.

---

## The framing, graded

The team's position: *"Benchmarking is NOT simulation. Simulation predicts; benchmarking MEASURES real compiled code on real hardware. Simulation can only reveal large improvements because hardware speed is uncertain. Big-O does not tell you actual throughput."*

### Where it is right — and sharper than stated

**Big-O cannot predict throughput.** Formally: big-O is defined up to an unspecified multiplicative constant *and* an unspecified threshold n₀, so it is incapable of predicting throughput at any specific N. But say *"big-O does not tell you actual throughput"* — not *"big-O is not useful."* The stronger version invites an advisor to dismiss the thesis with one counterexample.

**And there's a sharper version available for a swarm specifically:** at 4–10 agents, N is so small that asymptotic terms never dominate. **At swarm scale, complexity class is not merely insufficient — it is irrelevant.** Measured constants (cache behaviour, allocator, DDS serialization, radio ACK turnaround) determine everything.

Measured evidence, all on the same machine:

| Experiment | Result |
| --- | --- |
| Linear scan Θ(n) vs branchy binary search Θ(log n) | **Linear wins at every n ≤ 128**; crossover at n ≈ 150–160. 2.8× faster at n=16 |
| Per-step cost | Linear scan **165 ps/element** (~0.7 cycles) vs binary search **5.3–7.9 ns/step** — a ~40× constant-factor gap invisible to complexity analysis |
| Array vs linked-list traversal, both Θ(N) | At N=10⁷: **0.38 ns vs 121.7 ns per element — 322× for identical asymptotics** |
| …decomposed | Sequential linked list 1.53 ns (4×, pure pointer indirection); shuffling link order adds a further **~80× (pure cache/TLB miss)** |
| Merge sort with insertion-sort base case | Fastest at cutoff k = 48–64 — **a 21% win from deliberately using a Θ(N²) algorithm** — while pure insertion sort was 181× slower |

**The swarm-specific ones matter most:**

- **All-pairs collision checks, identical Θ(N²): 95.7 ms (pure Python) vs 4.10 ms (NumPy) at N=512 — 23×.** And **at N=4 the ordering inverts** (Python 5.3 µs beats NumPy 9.6 µs, array-call overhead dominating). Big-O ranks both pairs identical. *At the team's real N, language and vectorization matter more than algorithm choice.*
- **A KD-tree gives no benefit over naive Θ(N²) until N=16**, and is marginally *slower* at N=4–8. **Don't add a spatial index for a 4–8 drone swarm** — added code, added failure modes, zero measured speedup.
- k-NN queries cross over at **N ≈ 48**. Brute force is the correct engineering choice below that.

**Simulation genuinely cannot resolve small deltas** — and there is a strong citation for it. Mytkowicz et al. found the *same measurement bias inside the m5 O3CPU cycle-accurate simulator* whose full source they could read, with bzip2's O3 speedup ranging 0.8–1.1 across link orders. **Simulation does not escape measurement bias; it replaces an uncertain real system with an uncertain modelled one.**

### Where it needs qualifying — five points

**1. A benchmark measures a *system*, not a program.** Source + compiler + flags + link order + libc + kernel + governor + thermal state + concurrent tenants + environment size. *(measured)* Sweeping an **unused** environment variable from 0 to 2047 bytes — a variable nothing reads — produced an **11.7% spread** (6.554 ms → 7.323 ms), pinned, best-of-30. State this in the SRS up front; it turns the thesis from an overclaim into a rigorous position.

**2. "Benchmarking MEASURES" is only true if the measurement is unbiased.** The critical distinction the framing misses is **bias vs noise: more repetitions shrink noise as 1/√n but do not shrink bias at all.** A tight confidence interval is fully compatible with a wrong answer. Mytkowicz's own causal-analysis pass rejected the authors' initial conclusion for perlbench — careful researchers publishing at ASPLOS got it wrong on their own data.

**3. The dichotomy is fidelity, not predict-vs-measure.** A cycle-accurate simulator *measures a model* and inherits its biases. Reframing the axis as **model fidelity** makes the thesis unattackable.

**4. Simulation wins on repeatability, observability and sample size — and this one bites hard.** The required repetition counts below are **78–318 runs** for a 1–2% claim. **You cannot fly a swarm 300 times; you can simulate it 300 times.** The methodology must be a *hybrid*, not a rejection of simulation. This is the strongest argument against the absolutist reading of [DR-02](../03_decision_record.md#dr-02--semester-1-favors-real-hardware-over-simulation).

**5. Benchmarking has a failure mode simulation does not: measuring the wrong thing perfectly.** A flawless p50 microbenchmark of an ArUco pose solver says nothing about whether a drone crashes — that is a p99.9-under-contention question. **Precision without validity** is how a rigorous-looking capstone still fails at demo time.

Plus one boundary specific to this project: **host benchmarks do not predict STM32F405 performance.** Flash wait states, the ART accelerator, single-precision-only FPU and DMA contention change the constants entirely. Any algorithm selected on laptop benchmarks must be **re-benchmarked on the Cortex-M4** before the selection is defensible.

---

## The three experiments to run first

These are cheap, produce midterm-demo artifacts, and prove the team understands measurement.

### 1. Dead-code elimination — the 138,000× error

*(measured)* With `gcc -O2`, a 200-million-iteration loop whose result was discarded was **deleted entirely**: 0.000001 s vs 0.127438 s when the result was consumed.

**Any microbenchmark that computes a value and drops it reports near-zero time and looks like a spectacular optimization.** Defeating it requires protecting **both ends** — `DoNotOptimize` on outputs *and* opaque inputs, or the compiler constant-folds the whole computation. Half-protected benchmarks (output guarded, input a literal) are the most common way a student benchmark silently measures nothing.

*Note `ClobberMemory()` is a separate tool for side-effect-on-buffer work, GNU/MSVC only, and block-scope memory must be escaped with `DoNotOptimize` first. Rust's `black_box` is documented as **best-effort** — programs "cannot rely on black_box for correctness."*

⚠ Barriers are not free or neutral: forcing a value to memory inserts a store the shipped code would not contain. For sub-microsecond kernels the barrier can be a double-digit fraction of the measurement — **an end-to-end measurement should always be the tiebreaker.**

### 2. Sequential vs interleaved A/B — the one-line fix worth the most

*(measured)* With A and B being **literally the same compiled function**:

| Design | Result |
| --- | --- |
| All of A, then all of B | **−3.83%, 95% CI [−4.66%, −3.00%]** — excludes zero, "statistically significant" |
| Interleaved A,B,A,B… same process | **−0.04%, 95% CI [−1.09%, +1.01%]** — correctly straddles zero |

**A textbook significant result manufactured entirely out of thermal drift.** And running all of A then all of B is exactly the design a capstone team naturally uses when comparing two planners.

**Interleaved paired measurement is a one-line harness change that eliminates the largest single source of false positives in the entire test plan.**

### 3. The environment-size sweep — and an honest disagreement

Sweep an unused env var 0…2048 bytes, shuffle link order, report the spread. **If the claimed improvement is smaller than the sweep's spread, there is no result.**

> ⚠ **Two agents in this research pass disagreed on the same machine.** One measured an **11.7% spread** from an unused environment variable on one workload; the other **did not reproduce it** on a different workload (68.61 → 68.63 ns with a 3 KB variable) against a 1.6–1.9% pinned noise floor.
>
> **Report this honestly.** Cite Mytkowicz for the *mechanism and methodology*, not as a guaranteed reproduction — and run the sweep on *your own* workload rather than assuming either outcome. A stated failed replication reads as rigour.

---

## Statistical rigor

### Which statistic, and why it depends on the question

**The mean is the wrong headline.** Execution-time distributions are hard-bounded below by the intrinsic cost and unbounded above — every interruption only adds time — so they are right-skewed. Reporting mean ± stddev implies a symmetric Gaussian the data provably is not, and **understates worst-case control-loop latency.**

But "always report percentiles" is not right either. Chen & Revels argue for the **minimum** as the robust location estimator, showing the distribution of the minimum across trials is unimodal while that of the mean is bimodal and drifts.

**The reconciliation — decide which question you are asking:**

| Question | Statistic |
| --- | --- |
| "Did my optimization help?" (intrinsic cost of the computation) | **Minimum or median** |
| "Will the drone miss a deadline?" (delivered service latency) | **p95 / p99 / max** |

The swarm is a deadline-driven control system, so **SRS non-behavioral requirements go as tail percentiles, while optimization A/B comparisons use minimum or median.**

*(measured)* On an untuned Linux laptop, a fixed 20-million-iteration kernel over 300 reps: median 12.28 ms, **p95 13.21, p99 15.13, max 16.94, CV 4.56%** — max/median = 1.38×.

### How many runs — derivable, not guessable

> **n = (1.96 · CV / p)²** for a ±p% half-width 95% CI on the mean.

At the measured CV = 4.5%:

| Target precision | Runs needed |
| --- | ---: |
| ±0.5% | 312 |
| ±1% | 78 |
| ±2% | 20 |
| ±5% | 4 |

> **n = 2(z_α/2 + z_β)² · CV² / d² per arm** for an A/B comparison.

| True difference to detect (80% power) | Runs per arm |
| --- | ---: |
| 1% | 318 |
| 2% | 80 |
| 5% | 13 |

**A 1% claim is a 600-run experiment the team will not do.** Either tune the machine to cut CV, or only make claims larger than 5%.

**And tuning beats repetition, because n scales with CV².** Halving CV from 4.5% to 2.25% cuts required runs by **4×**. *An hour spent tuning the ground station buys more statistical power than a night of extra runs.*

**Pinning alone is not enough.** *(measured)* `taskset -c 3` cut CV only from 4.56% to 4.02% and p99 from 15.13 to 13.83 ms — because pinning does not stop frequency scaling, turbo, thermal drift, or the SMT sibling on the same physical core. **A team that pins and declares victory will still publish noise.**

### Tests and thresholds

- **n ≥ 30 → normal-approximation CI; n < 30 → Student's t.** If the CI on the *difference* of two means includes zero, the difference is not significant (Georges et al.).
- **More than two alternatives → ANOVA**, not repeated pairwise t-tests, which inflate the false-positive rate.
- **"Best of 30" (the SPEC reporting rule) can be misleading** — it reports one lucky execution alongside many unimpressive ones.
- Google Benchmark's `compare.py` uses **Mann-Whitney U**, documented to need **≥9 repetitions** to be meaningful. A U-test on 3 reps is decoration.
- **Separate statistical from practical significance.** Criterion does this with two independent knobs: `significance_level` (0.05, the hypothesis test) and `noise_threshold` (0.01 — changes under 1% ignored even when statistically significant). **This is exactly the pattern the System Test Plan's pass/fail criteria need: a threshold on effect size, plus a separate threshold on confidence.**
- **Use median/MAD, not mean/stddev, for outlier detection** when the distribution is skewed — hyperfine uses a modified Z-score with MAD.
- **Warn about outliers, keep them.** Criterion classifies by Tukey fences (mild >1.5×IQR, severe >3×IQR) but retains them. **Silently discarding outliers is exactly how a real-time system's deadline misses get hidden.**

### Variance sources to control

pyperf's `system tune` is a ready-made, citable checklist: performance governor, `scaling_min_freq` to max, stop `irqbalance` and set IRQ affinity, `perf_event_max_sample_rate=1`, disable Turbo via `intel_pstate/no_turbo`, and *verify the power cable is connected*. It also **checks** `isolcpus`, `rcu_nocbs`, and — notably — that ASLR is at **full** randomization.

> **Pick an ASLR strategy consciously and state it.** pyperf keeps ASLR **on** (randomize the layout so bias averages out); `setarch -R` freezes one layout for repeatability at the cost of making the result specific to that arbitrary layout. **Mixing them — freeze a layout, then generalize the result — is precisely Mytkowicz's error.**

⚠ `chrt` is the one mitigation that can hang the machine: an SCHED_FIFO task spinning without yielding starves the system. **Use `chrt -f 80` on an isolated core, not `chrt -f 99` on a shared one.**

Also: cold-start effects are large enough that hyperfine has a dedicated `SlowInitialRun` warning. The ROS 2 / Crazyswarm2 stack has enormous first-call costs — DDS discovery, Python imports, page-faulting shared libraries — that will dominate an un-warmed measurement. And **branch-predictor and cache warming make repeated-identical-input microbenchmarks optimistic**: an ArUco decode benchmarked on one frame looks faster than it ever will on a live stream.

---

## Measurement toolchain, by layer

### On the drone (STM32F405)

| Tool | Measures | Effort |
| --- | --- | --- |
| **`Task dump` / SYSLOAD** (cfclient Console tab) | Per-FreeRTOS-task CPU load % and stack remaining | **trivial — already shipped** |
| **DWT CYCCNT** | Exact CPU cycles | low |
| **GPIO toggle + logic analyzer** | Ground-truth routine start/end, ~zero probe effect | low |

**Start with `Task dump`.** It is zero-effort baseline evidence of *on-drone computational effort* — one of the three quantities the problem statement names — available **before writing any code.**

**DWT CYCCNT setup:** set `TRCENA` (bit 24) in `DEMCR` at `0xE000EDFC`, then `CYCCNTENA` in `DWT_CTRL` at `0xE0001000`, read at `0xE0001004`. **It is disabled after reset** — the enable sequence must run in init or every reading is zero. ⚠ It is 32-bit, so at 168 MHz it **wraps every ~25.6 s**; a naive end-minus-start silently produces a wrapped interval on anything longer, e.g. a whole flight.

**The GPIO method is the ground truth** — one BSRR store, a few cycles of probe effect, and no dependence on the software under test being correct. **The team already built exactly this in CEC 320 Lab04** (direct BSRR access, 3-channel logic analyzer sampling), so it is citable prior work rather than a new capability.

### On the ground station

| Tool | Measures | Effort |
| --- | --- | --- |
| **hyperfine** | Whole-command wall clock; ≥10 runs, ≥3 s, shell-overhead calibration, MAD outlier detection | **trivial** |
| **perf stat** | Cycles, instructions, IPC, cache misses, branch misses, **context switches, CPU migrations** | low |
| **cyclictest** (rt-tests) | Kernel scheduling latency — **the floor under any timing claim** | trivial |
| Google Benchmark | In-process C++ microbenchmarks; auto iteration count; reports CV | low |
| pytest-benchmark | Python: the ArUco/OpenCV pipeline and Crazyswarm2 glue | low |
| **pyperf system tune** | Nothing directly — puts the machine in a low-variance state | trivial |

**Run `cyclictest` once, first.** If its max latency is 3 ms, no node on that box can promise a 1 ms deadline no matter how fast the code is. **Run it before writing any latency requirement.**

**`perf stat`'s `context-switches` and `cpu-migrations` are the cheapest way to prove a run was interrupted** — record them alongside every timing result as evidence of validity.

⚠ **pytest-benchmark traps:** GC is **enabled** by default (`disable_gc=False`) so a benchmark can be interrupted by a GC pause from unrelated earlier allocations, and **warmup is off** by default on Linux. Pass `--benchmark-disable-gc` and `--benchmark-warmup=on`.

⚠ Google Benchmark emits *"CPU scaling is enabled, the benchmark real time measurements may be noisy"* — which is the **default state of any untuned laptop**. Act on the warning; don't ignore it.

Criterion.rs's defaults are a sane citable parameter set even if the team never writes Rust: `sample_size=100`, `measurement_time=5s`, `warm_up_time=3s`, `nresamples=100_000`, `confidence_level=0.95`, `noise_threshold=0.01`. Its **linear-regression slope estimation** (per-iteration time as the slope of total time vs iteration count) is the correct technique for anything near timer resolution — a single quaternion update or CRTP packet encode.

### Across ROS 2 — and the citable authority

**REP-2014, "Benchmarking performance in ROS 2"**, is an official public-domain ROS Enhancement Proposal that **defines message latency (publish → callback invocation), execution latency, throughput in messages/s and bytes/s, jitter, and performance-per-watt.**

> **This gives the SRS a citable authority for the exact metric definitions the problem statement names.** "Delay" and "throughput" become defined terms instead of vague ones.

REP-2014 recommends a **grey-box** approach via LTTng through `ros2_tracing`, using tracepoints already compiled into the ROS 2 core — no instrumentation code needed. **Measured overhead is 0.0033 ms (3.3 µs) average**, negligible against a ~10 ms control period, **so tracing can stay on during real flights without invalidating them.**

Named tools: **Apex.AI `performance_test`** (pub/sub latency and throughput), `ros2_latency_evaluation`, **`ros2_timer_latency_measurement`** (real-time-safe jitter — useful specifically for the jitter number the SRS needs, which no other listed tool reports directly), and `buildfarm_perf_tests`.

⚠ **`performance_test` measures the DDS/ROS 2 transport, not the Crazyradio link** — it cannot tell you anything about the air interface, **which is where the throughput problem actually lives.** That has to be measured separately ([F04](F04_network_and_latency.md)).

---

## Turning measurement into graded documents

**Anatomy of a measurable non-functional requirement:** stimulus + measured quantity + threshold + **condition** + **percentile**.

| Bad | Good |
| --- | --- |
| "The system shall be fast" | "The ground station shall publish a formation setpoint to each agent at 10 Hz with **p99** end-to-end latency below **X ms** with **N agents active**, measured over **≥20 trials** with the RF environment logged" |
| "Formation error shall be small" | "RMS inter-agent distance error shall remain below **0.10 m** over t ∈ [20 s, 60 s], reported as mean ± sd **plus maximum**, over **N = 20 trials**" |
| "Packet loss shall be low" | "**Consecutive-drop burst length** shall not exceed **k** packets at the 99th percentile, per RFC 7680 with Tmax stated" |

**A threshold without a stated measurement condition is not testable.** And note the third row: [F04](F04_network_and_latency.md) shows burst length, not average rate, is what breaks formation control.

**Feed the CV numbers back into the pass/fail margin.** *(measured)* A pinned binary showed 1.6–1.9% sd; unpinned, 3.6% with max/min 1.21. **Any timing criterion tighter than ~10% will fail randomly.** Every timing test must pin the core and report a median over ≥20 runs.

### Empirical scaling — and the two pitfalls

Fitting measured runtime vs N to candidate curves is legitimate, with caveats:

⚠ **Too narrow an N range.** *(measured)* Fitting SciPy's O(N³) Hungarian assignment gives exponent **b = 0.79 over N=4..16**, 1.46 over N=4..64, and only ~2.44 over N=16..2048. **The textbook exponent 3 is never recovered anywhere in the practical range** — using an algorithm the team will actually run for task assignment.

⚠ **Cache cliffs fabricate exponents.** *(measured)* Binary search is Θ(log n) at every n, yet a power-law fit gives **b = 0.167 in-cache and b = 0.498 once the array exceeds the 12 MiB L3** — the same algorithm, two apparent exponents, **neither logarithmic.** Cost per level rose from 5.3–7.9 ns in-cache to 22.5 / 33.8 / 75.7 ns at 16 / 64 / 256 MiB — a 10–14× constant-factor change from the memory hierarchy alone.

⚠ **The doubling method provably cannot distinguish Θ(N) from Θ(N log N)** — log factors vanish into the fitted constant. **The traceability matrix must not claim to have "verified O(N) scaling."** Honest wording: *"measured exponent 1.0 ± x over N = a..b."*

**The honest positive result:** complexity analysis *is* quantitatively predictive **within one memory regime** — t = 8.29·log₂(n) − 19.0 ns fit the in-cache data with 6.7 ns RMS residual, versus **377 ns (56× worse)** for the same form fitted across the L3 boundary. **State the regime.**

**Corroboration worth citing:** Khuong & Morin (ACM JEA 2017) measured the same cliffs at n=2¹⁶ (L2) and n=2²¹ (L3), and report branch-free binary search is **~2× faster at n=2¹⁶ but ~45% slower at n=2³⁰** — an optimization whose *sign flips* with input size.

**A primary source on your own disk:** libstdc++ hard-codes `enum { _S_threshold = 16 };` in `bits/stl_algo.h` — `std::sort` literally switches to insertion sort below 16 elements. *(measured)* But the tuned cutoff on the test machine was **48–64, not 16**, because the constant depends on the comparator, surrounding algorithm and CPU. **The cutoff must be benchmarked; it cannot be looked up.**

### Where this lands in the deliverables

| Deliverable | What measurement supplies |
| --- | --- |
| Proposal, Problem Statement (24%) | Converts throughput/delay/computational-effort assertions into cited, measured claims |
| SRS, Non-behavioral Requirements | Every threshold with a percentile and a measurement condition; REP-2014 for definitions |
| System Test Plan | Benchmarks **are** the test cases for performance requirements; traceability matrix rows |
| **Midterm (15% prototyping evidence)** | **Latency histograms and the A/B-interleaving demo — no flight required** |
| Final (Results 5%, Lessons Learned 10%) | Measured before/after, and the failed replication stated openly |

---

## Open

- **No published CV exists for Crazyradio round-trip latency or CRTP throughput under multi-drone contention.** This must be measured, and it is **likely the dominant variance source in the whole system** — far exceeding the ~4.5% CPU-side CV. It is also a genuinely novel measurement.
- **REP-2014 covers single-node and single-graph ROS 2 benchmarking. It defines no methodology for multi-robot or swarm-scale benchmarking**, so *"how many flights constitutes valid evidence"* has no standard answer — derive it from your own measured CV using the formulas above.
- DWT CYCCNT read overhead on the STM32F405 is unpublished — **time an empty read pair** before trusting fine-grained numbers.
- The timer resolution behind the Crazyflie SYSLOAD load percentages is undocumented; treat it as coarse attribution, not precise timing.
- Whether `ros2_tracing`/LTTng ship prebuilt for the chosen ROS 2 distro is unverified — on some distro/kernel combinations LTTng needs kernel modules built, moving the effort estimate from medium to high.
- Whether the environment-size bias reproduces on ARM ground-station hardware is unknown; Mytkowicz tested only x86 and one simulator.

---

## References

1. T. Mytkowicz, A. Diwan, M. Hauswirth, P. F. Sweeney, "Producing Wrong Data Without Doing Anything Obviously Wrong!," *ASPLOS '09*, pp. 265–276. doi:10.1145/1508244.1508275 — **measurement bias; setup randomization; bias inside the simulator**
2. A. Georges, D. Buytaert, L. Eeckhout, "Statistically Rigorous Java Performance Evaluation," *OOPSLA 2007*, pp. 57–76. — CIs, difference-of-means, ANOVA, the best-of-30 critique
3. J. Chen, J. Revels, "Robust benchmarking in noisy environments," MIT CSAIL, arXiv:1608.04295, 2016. — the minimum as robust location estimator
4. **REP-2014, "Benchmarking performance in ROS 2,"** ROS Enhancement Proposal (public domain). — **metric definitions for the SRS**
5. C. Bedard, I. Lütkebohle, M. Dagenais, "ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2," *IEEE RA-L* 7(3):6511–6518, 2022. arXiv:2201.00393 — the 3.3 µs overhead figure
6. P.-V. Khuong, P. Morin, "Array Layouts for Comparison-Based Searching," *ACM JEA*, 2017. arXiv:1509.05053 — cache cliffs; the sign-flipping optimization
7. Google Benchmark, *User Guide* and *Tools* documentation. — `DoNotOptimize`/`ClobberMemory`; Mann-Whitney U and the ≥9-repetition rule
8. D. Peter, *hyperfine* README and source. — defaults; MAD modified Z-score (Iglewicz & Hoaglin 1993); `welch_ttest.py`, `advanced_statistics.py`
9. B. Heisler, *Criterion.rs* book (analysis.html). — regression slope estimation; Tukey fences; statistical vs practical significance
10. I. C. Marieș, *pytest-benchmark 5.2.3* documentation. — defaults including `disable_gc=False`, `warmup=False`
11. V. Stinner et al., *pyperf 2.10 — "Tune the system for benchmarks."* — **the Linux tuning checklist**
12. ARM, *ARMv7-M Architecture Reference Manual* (DWT/DEMCR); E. Styger, "Cycle Counting on ARM Cortex-M with DWT," MCU on Eclipse, 2017.
13. Bitcraze AB, "Debug Tools in the Client Console Tab," 2022. — the SYSLOAD Task dump
14. Rust standard library, `std::hint::black_box` documentation. — the "best-effort" caveat
15. R. Sedgewick, K. Wayne, *Algorithms*, 4th ed. — the doubling hypothesis and its limits
16. libstdc++ `bits/stl_algo.h`, GCC 11.4 — `_S_threshold = 16`
17. Own replication experiments, 2026-08-31, Intel i7-11370H, gcc 11.4. — DCE 138,000×; CV 4.56% unpinned / 4.02% pinned; sequential vs interleaved A/B; the 11.7% environment sweep **and its non-reproduction on a second workload**

---

**Related:** [`F04_network_and_latency.md`](F04_network_and_latency.md) · [`F02_formation_control.md`](F02_formation_control.md) · [`F09_simulation_and_compute.md`](F09_simulation_and_compute.md) · [`../01_idea_register.md`](../01_idea_register.md) · [`../../INDEX.md`](../../INDEX.md)
