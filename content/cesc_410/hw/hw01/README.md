# HW1 — Basic signals/systems and convolution

**Fall 2026** · source: `dsphw26-hw1.pdf` · **130 pts total**

Six problems. Each has its own `.tex` with full step-by-step work;
[`hw01_solutions.tex`](hw01_solutions.tex) is the condensed answers-only version.

```sh
# from the REPO ROOT; the shared tooling takes repo-relative paths
docs/latex/build_tex.sh  content/cesc_410/hw/hw01           # build-check everything
docs/latex/build_tex.sh  content/cesc_410/hw/hw01 --keep    # ...and keep the PDFs
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01          # self-contained Overleaf copies
```

All seven files build, and all seven flatten to `hw01/overleaf/` and compile
standalone from there — verified by running `tectonic` on each flattened copy,
not just by flattening successfully. `overleaf/` is gitignored and regenerable.

`../tools/build_tex.sh hw01` still works and takes paths relative to
`content/cesc_410/hw/`, but the shared checker is the one to use.

---

## Problems

| # | File | LO | Pts | Topic | Status |
| --- | --- | --- | ---: | --- | --- |
| 1 | [`p01_phasor_form.tex`](p01_phasor_form.tex) | LO01 | 20 | Phasor form of 4 voltage sources | ✅ |
| 2 | [`p02_phasor_arithmetic.tex`](p02_phasor_arithmetic.tex) | LO01 | 10 | Sum/difference via phasors | ✅ |
| 3 | [`p03_signal_transformations.tex`](p03_signal_transformations.tex) | LO02 | 20 | Plot $x[n]$, $x[n-2]$, $x[-n]$, $x[2-n]$ | ✅ |
| 4 | [`p04_periodicity.tex`](p04_periodicity.tex) | LO03 | 20 | Periodicity + fundamental period ×4 | ✅ |
| 5 | [`p05_system_properties.tex`](p05_system_properties.tex) | LO04 | 40 | Linear/TI/causal/BIBO for 5 systems | ✅ |
| 6 | [`p06_convolution.tex`](p06_convolution.tex) | LO05 | 20 | $a^n u[n] \ast a^n u[n]$ by flip-slide-sum | ✅ |
| | | | **130** | | |

Point total matches the handout's stated 130 — nothing missed.

---

## ⚠ Two transcription traps in this handout

**1. The handout numbers the last problem "Prob 1" a second time.** There is no
Prob 6 in the PDF; the convolution problem is labelled Prob 1 (LO05). Files use a
continuous index (`p06_`) so they sort correctly, and both `p06` and the
solutions document note the discrepancy on their face.

**2. `pdftotext` flattens fractions and misreads two problems.** Verified against
the rendered page at 400 dpi, not the text layer:

| `pdftotext` says | Actually is | Why it matters |
| --- | --- | --- |
| `cos( 6π n)` | $\cos\!\big(\tfrac{\pi}{6}n\big)$ | $\cos(6\pi n) = 1$ for all integer $n$ — a constant, not a signal |
| `e^{j(πn/ 8)}` with a stray `√` | $e^{j(\pi n/\sqrt{8})}$ | The $\sqrt{\ }$ is the whole point of part 4: it makes the signal **aperiodic** |

**Do not trust `tools/course_text.py --grep` for equations in this handout.** It
reads the same broken text layer. Render the region and look at it.

---

## Answers at a glance

| # | Result |
| --- | --- |
| 1 | $\phasor{10}{-75°}$, $\phasor{15}{15°}$, $\phasor{12}{75°}$, $\phasor{8}{165°}$ |
| 2 | $5\sqrt{13}\angle-18.69°$ ; $3\sqrt{21}\angle-34.11°$ |
| 3 | Samples $\{1,\ 0.866,\ 0.5,\ 0\}$ relocated to supports $[0,3]$, $[2,5]$, $[-3,0]$, $[-1,2]$ |
| 4 | Periodic $N_0=16$ ; periodic $N_0=18$ ; **not** periodic ; **not** periodic |
| 5 | Only $T_a$ is BIBO-unstable; only $T_c$, $T_d$ are non-causal |
| 6 | $y[n] = (n+1)a^n u[n]$ |

## Verification

Every numeric answer was checked computationally, not just re-derived:

- **P1** — each phasor reconstructed and compared to the original over a full
  $\omega t$ sweep: max error $\approx 10^{-14}$.
- **P2** — magnitudes confirmed exact ($\sqrt{325} = 5\sqrt{13}$,
  $\sqrt{189} = 3\sqrt{21}$) by two independent routes: component arithmetic, and
  geometry (the phasors are $90°$ apart in part 1; law of cosines in part 2).
- **P4** — brute-force search for $N \le 10{,}000$ satisfying
  $\omega_0 N = 2\pi k$: found 16 and 18, found none for part 4.
- **P6** — `np.convolve` vs $(n+1)a^n$ for $a = 0.5,\ 2.0,\ -0.7$ over $n < 40$:
  max error $0$, $0$, and $1.1\times10^{-16}$.

---

## Submission

**Unconfirmed — [Human-only](../prompt.md#human-only).** No code and no zip for
this assignment (unlike the labs); most likely a single PDF to Canvas. Confirm
whether the per-problem work is submitted or only the solutions document before
turning anything in. See [`../reference_docs/submission.md`](../reference_docs/submission.md).
