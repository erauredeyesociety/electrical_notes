# CESC 470 — Homework 1

**Fall 2026** · source: [`HW1.pdf`](HW1.pdf) · **due 9/13/2026** · **100 points**

Ten problems. Each has its own `.tex` with full step-by-step work and citations;
[`hw01_solutions.tex`](hw01_solutions.tex) is the condensed answers-only version.

```sh
# from the repo root — paths are repo-relative
docs/latex/build_tex.sh content/cesc_470/hw/hw01           # build-check all
docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep    # ...and keep the PDFs
```

Doctrine: [`docs/directives/coursework-solutions.md`](../../../../docs/directives/coursework-solutions.md)

---

## Problems

| # | File | Pts | Topic | Status |
| --- | --- | ---: | --- | --- |
| 1 | [`p01_five_components.tex`](p01_five_components.tex) | 5 | Five classic components | ✅ |
| 2 | [`p02_von_neumann_tradeoff.tex`](p02_von_neumann_tradeoff.tex) | 10 | Stored-program advantage/disadvantage | ✅ |
| 3 | [`p03_instruction_encodings.tex`](p03_instruction_encodings.tex) | 5 | $2^{32}$ unique instructions | ✅ |
| 4 | [`p04_architecture_vs_organization.tex`](p04_architecture_vs_organization.tex) | 10 | Architecture vs organization | ✅ |
| 5 | [`p05_same_isa_different_org.tex`](p05_same_isa_different_org.tex) | 5 | Same ISA, different organizations | ✅ |
| 6 | [`p06_isa_components.tex`](p06_isa_components.tex) | 3 | Three components of an ISA | ✅ |
| 7 | [`p07_arm_vs_x86.tex`](p07_arm_vs_x86.tex) | 25 | ARM vs x86 — **research question** | ✅ |
| 8 | [`p08_target_clock_rate.tex`](p08_target_clock_rate.tex) | 15 | Target clock rate for Computer B | ✅ |
| 9 | [`p09_cpi_and_execution_time.tex`](p09_cpi_and_execution_time.tex) | 12 | Average CPI (5) + execution time (7) | ✅ |
| 10 | [`p10_amdahl_speedup.tex`](p10_amdahl_speedup.tex) | 10 | Amdahl's law | ✅ |
| | | **100** | | |

**Point total matches the handout's stated 100** — nothing missed.
$5+10+5+10+5+3+25+15+12+10 = 100$.

---

## Answers at a glance

| # | Result |
| --- | --- |
| 1 | Control unit, datapath, memory, input, output (CU + datapath = CPU) |
| 2 | $+$ reprogrammability · $-$ von Neumann bottleneck (shared memory/bus) |
| 3 | $2^{32} = 4{,}294{,}967{,}296$ |
| 4 | Architecture = *what* (ISA + organization); organization = *how* |
| 5 | Desktop vs laptop x86-64 — same binary, different clock/cache/pipeline |
| 6 | Instruction set, register set/storage, addressing modes |
| 7 | ARM: $+$ power, $-$ compatibility · x86: $+$ compatibility, $-$ decode complexity |
| 8 | **1.8 GHz** |
| 9 | (a) CPI $= 1.8$ · (b) $1.8$ ms |
| 10 | **3.57×** achieved; **5×** ceiling |

---

## Verification

Every quantitative answer was recomputed independently, not just re-derived:

- **Q3** — $2^{32} = 4{,}294{,}967{,}296$, cross-checked as $4 \times 1024^3$.
- **Q8** — two independent routes agree on 1.8 GHz: absolute cycle counts
  ($1.08\times10^{10} \to 1.62\times10^{10}$, ÷ 9 s), and pure ratios
  ($600\,\text{MHz} \times 1.5 \times 2$). Substituting back gives exactly 9 s.
  The naive 1.2 GHz is recorded as the trap.
- **Q9** — CPI 1.8 confirmed two ways (fractional weights; and counts, 18/10).
  Execution time confirmed via cycle time *and* via clock rate (1 GHz). Bounds
  check: CPI must lie in $[1,3]$ and below 2 given the mix — 1.8 does.
- **Q10** — 3.5714× confirmed with concrete numbers (100 s → 28 s) as well as
  normalised fractions; ceiling $1/0.2 = 5$ verified as the $n\to\infty$ limit.

---

## ⚠ Q10 is ambiguous — both readings are given

*"If floating-point performance is improved by a factor of 10, what is the
**maximum possible** speedup?"*

- Answering the **stated 10× improvement**: $1/(0.2 + 0.8/10) = 3.57\times$
- Answering **"maximum possible" as the ceiling**: $1/0.2 = 5\times$

Since the problem supplies a specific factor, **3.57× is the answer**, with the
5× ceiling stated alongside. Giving only 5× ignores the data provided; giving
only 3.57× misses what "maximum possible" points at. See
[`p10_amdahl_speedup.tex`](p10_amdahl_speedup.tex).

## Q7 is the only problem needing outside sources

It says *"Research and compare…"*, so the course materials are genuinely silent.
External claims are marked with `\extref{}`, which renders in a different colour
so they are never confused with lecture content. Everything else cites
[`../../Module 01 Introduction to computer technology & ISA (1).pdf`](<../../Module 01 Introduction to computer technology & ISA (1).pdf>)
by PDF page and slide number.

---

## Submission

**Unconfirmed — human-only.** No code and no zip for this assignment. The
syllabus states homework *"must be typed and converted to pdf for submission"*
([`../../cesc_470.pdf`](../../cesc_470.pdf)), so a single PDF to Canvas is the
likely form. Confirm whether the per-problem work is submitted or only the
solutions document before turning anything in.
