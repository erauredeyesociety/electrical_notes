# CEC 315 — Exam 2 Quick-Reference Notes (Lectures 9–15)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Purpose:** Compact cheat sheet — formula tables, per-lecture key ideas, pitfalls.

---

## Formula Tables

### CT Fourier Series (CTFS)

| Quantity | Formula |
|---|---|
| Synthesis | $\displaystyle x(t)=\sum_k a_k e^{jk\omega_0 t}$ |
| Analysis | $\displaystyle a_k=\frac{1}{T}\int_T x(t)e^{-jk\omega_0 t}dt$ |
| DC | $\displaystyle a_0=\frac{1}{T}\int_T x\,dt$ |
| Fund. freq | $\omega_0=2\pi/T$ |
| Parseval | $\displaystyle\frac{1}{T}\int_T|x|^2dt=\sum_k|a_k|^2$ |

### DT Fourier Series (DTFS, length $N$)

| Quantity | Formula |
|---|---|
| Synthesis | $\displaystyle x[n]=\sum_{k=\langle N\rangle} a_k e^{jk(2\pi/N)n}$ |
| Analysis | $\displaystyle a_k=\frac{1}{N}\sum_{n=\langle N\rangle} x[n]e^{-jk(2\pi/N)n}$ |
| Parseval | $\displaystyle\frac{1}{N}\sum_n|x[n]|^2=\sum_{k=\langle N\rangle}|a_k|^2$ |
| Periodicity | $a_{k+N}=a_k$ |

### CT Fourier Transform (CTFT)

| Quantity | Formula |
|---|---|
| Forward | $\displaystyle X(j\omega)=\int x(t)e^{-j\omega t}dt$ |
| Inverse | $\displaystyle x(t)=\frac{1}{2\pi}\int X(j\omega)e^{j\omega t}d\omega$ |
| Parseval | $\displaystyle\int|x|^2dt=\frac{1}{2\pi}\int|X|^2d\omega$ |

### DT Fourier Transform (DTFT)

| Quantity | Formula |
|---|---|
| Forward | $\displaystyle X(e^{j\omega})=\sum_n x[n]e^{-j\omega n}$ |
| Inverse | $\displaystyle x[n]=\frac{1}{2\pi}\int_{2\pi}X(e^{j\omega})e^{j\omega n}d\omega$ |

### CT FT Pairs (must-know)

| $x(t)$ | $X(j\omega)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $1$ | $2\pi\delta(\omega)$ |
| $u(t)$ | $1/(j\omega)+\pi\delta(\omega)$ |
| $e^{-at}u(t)$, $a>0$ | $\dfrac{1}{a+j\omega}$ |
| $te^{-at}u(t)$, $a>0$ | $\dfrac{1}{(a+j\omega)^2}$ |
| $e^{-a|t|}$, $a>0$ | $\dfrac{2a}{a^2+\omega^2}$ |
| $e^{j\omega_0 t}$ | $2\pi\delta(\omega-\omega_0)$ |
| $\cos\omega_0 t$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ |
| $\sin\omega_0 t$ | $(\pi/j)[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |
| rect width $2T_1$ | $\dfrac{2\sin(\omega T_1)}{\omega}$ |
| $\dfrac{\sin(Wt)}{\pi t}$ | rect on $|\omega|\le W$ |
| Periodic $x$ | $\sum_k 2\pi a_k\delta(\omega-k\omega_0)$ |

### DT FT Pairs (must-know)

| $x[n]$ | $X(e^{j\omega})$ |
|---|---|
| $\delta[n]$ | $1$ |
| $a^n u[n]$, $|a|<1$ | $\dfrac{1}{1-ae^{-j\omega}}$ |
| $(n+1)a^n u[n]$, $|a|<1$ | $\dfrac{1}{(1-ae^{-j\omega})^2}$ |
| $e^{j\omega_0 n}$ | $2\pi\sum_k\delta(\omega-\omega_0-2\pi k)$ |

### CT FT Properties

| Property | Time | Frequency |
|---|---|---|
| Linearity | $ax+by$ | $aX+bY$ |
| Time shift | $x(t-t_0)$ | $e^{-j\omega t_0}X$ |
| Freq shift | $e^{j\omega_0 t}x$ | $X(j(\omega-\omega_0))$ |
| Scaling | $x(at)$ | $X(j\omega/a)/|a|$ |
| Time reversal | $x(-t)$ | $X(-j\omega)$ |
| Differentiation | $dx/dt$ | $j\omega X$ |
| Integration | $\int_{-\infty}^t x\,d\tau$ | $X/(j\omega)+\pi X(0)\delta(\omega)$ |
| Convolution | $x*h$ | $XH$ |
| Multiplication | $xy$ | $(X*Y)/(2\pi)$ |
| Duality | $X(jt)$ | $2\pi x(-\omega)$ |
| Parseval | $\int|x|^2dt$ | $\dfrac{1}{2\pi}\int|X|^2d\omega$ |

### CTFS Properties

| Property | Time | Coefficient |
|---|---|---|
| Linearity | $Ax+By$ | $Aa_k+Bb_k$ |
| Time shift | $x(t-t_0)$ | $a_k e^{-jk\omega_0 t_0}$ |
| Time reversal | $x(-t)$ | $a_{-k}$ |
| Conjugation | $x^*$ | $a_{-k}^*$ |
| Differentiation | $dx/dt$ | $jk\omega_0 a_k$ |
| Real signal | — | $a_{-k}=a_k^*$ |

### Second-Order Standard Form Reference

| Item | Formula |
|---|---|
| Transfer function | $\dfrac{\omega_n^2}{(j\omega)^2+2\zeta\omega_n(j\omega)+\omega_n^2}$ |
| DC gain | $1$ |
| $|H(j\omega_n)|$ | $1/(2\zeta)$ |
| $\angle H(j\omega_n)$ | $-90°$ |
| $\omega_r$ (resonance) | $\omega_n\sqrt{1-2\zeta^2}$, if $\zeta<1/\sqrt2$ |
| Peak $|H|_\max$ | $1/(2\zeta\sqrt{1-\zeta^2})$, if $\zeta<1/\sqrt2$ |
| $\omega_d$ | $\omega_n\sqrt{1-\zeta^2}$, if $\zeta<1$ |
| %OS | $100 e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| $t_p$ | $\pi/\omega_d$ |
| $t_s$ (2%) | $4/(\zeta\omega_n)$ |
| $t_r$ | $1.8/\omega_n$ |
| HF slope | $-40$ dB/dec |

---

## Per-Lecture Reference

### Lecture 9 — CT Fourier Series
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr09-ct-fourier-series.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr09_ct_fourier_series.md`

**Key ideas:**
- $e^{st}$ are eigenfunctions of LTI systems: $e^{st}\to H(s)e^{st}$.
- CTFS = decomposition of periodic $x$ into harmonic exponentials.
- Coefficients $a_k=\frac{1}{T}\int_T x(t)e^{-jk\omega_0 t}dt$; $a_0$ = average.
- Real-signal symmetry: $a_{-k}=a_k^*$.
- Use Euler formulas to read off coefficients by inspection.

### Lecture 10 — Convergence, Properties, DTFS
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr10-convergence-properties-dtfs.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr10_convergence_properties.md`

**Key ideas:**
- Dirichlet: integrable, bounded variation, finite discontinuities; FS converges at continuity; to midpoint at jumps.
- Gibbs phenomenon: ~9% overshoot at jumps, does not vanish with $N$.
- Spectral decay rate reflects smoothness: $|a_k|\sim 1/k^{m+1}$.
- CTFS properties: linearity, time shift (phase only), differentiation ($jk\omega_0$), Parseval.
- DTFS: only $N$ coefficients, periodic, finite sum, no convergence pathology.

### Lecture 11 — Frequency Response and Filtering
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr11-frequency-response-filtering.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr11_frequency_response_filtering.md`

**Key ideas:**
- LTI system acts harmonic-by-harmonic: $b_k=a_k H(jk\omega_0)$.
- $H(j\omega)$ for $h(t)=e^{-at}u(t)$ is $1/(a+j\omega)$, with $\omega_c=a$.
- RC lowpass cutoff: $\omega_c=1/RC$; at $\omega_c$, $|H|=1/\sqrt2$ ($-3$ dB), phase $-45°$.
- Ideal filters are noncausal and unrealizable.
- Bandwidth–rise-time trade-off: $\omega_c t_r\approx\text{const}$.

### Lecture 12 — Fourier Transforms
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr12-fourier-transforms.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr12_fourier_transforms.md`

**Key ideas:**
- FT generalizes CTFS to aperiodic signals (let $T\to\infty$).
- CTFT pair with $1/(2\pi)$ in the inverse; DTFT is $2\pi$-periodic.
- Sanity check: $X(0)=\int x(t)dt$ (total area).
- Periodic signal FT is a weighted impulse train: $\sum 2\pi a_k\delta(\omega-k\omega_0)$.
- Four representations: CTFS/CTFT/DTFS/DTFT; discrete ↔ periodic in the other domain.

### Lecture 13 — FT Properties and Convolution
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr13-ft-properties-convolution.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr13_ft_properties_convolution.md`

**Key ideas:**
- Convolution property is the payoff: $x*h\leftrightarrow XH$.
- Time shift adds phase but preserves magnitude.
- Differentiation $\leftrightarrow j\omega$ (amplifies high frequencies).
- ODEs → algebraic eqs: $d^k/dt^k\to(j\omega)^k$ giving $H(j\omega)=N(j\omega)/D(j\omega)$.
- 4-step pipeline: transform, multiply, PFE, invert.

### Lecture 14 — Magnitude, Phase, Ideal Filters
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr14-magnitude-phase-filters.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr14_magnitude_phase_filters.md`

**Key ideas:**
- $X=|X|e^{j\angle X}$; dB $=20\log_{10}|H|$; $-3$ dB is the standard cutoff.
- Linear phase $\Leftrightarrow$ constant group delay $\Leftrightarrow$ pure time delay.
- Ideal LPF has sinc impulse response $\to$ noncausal, unrealizable.
- Real filters defined by passband/stopband edges, ripple, attenuation, transition band.
- Bandwidth–rise-time trade-off ($\omega_c t_r\approx$ const).

### Lecture 15 — First/Second-Order Systems and Bode Plots
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr15-systems-bode-examples.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr15_systems_bode.md`

**Key ideas:**
- First-order LP $1/(1+j\omega/\omega_c)$: 0 dB flat, $-20$ dB/dec, $-45°$ at $\omega_c$, $-90°$ asymptote.
- Bode building blocks: pole $\to -20$ dB/dec, zero $\to +20$ dB/dec, $(j\omega)^{\pm1}\to\pm 20$ dB/dec across all $\omega$.
- Second-order standard form: DC gain 1, HF slope $-40$ dB/dec, $|H(j\omega_n)|=1/(2\zeta)$, $\angle H(j\omega_n)=-90°$.
- Resonance exists iff $\zeta<1/\sqrt2$; peak $1/(2\zeta\sqrt{1-\zeta^2})$ at $\omega_r=\omega_n\sqrt{1-2\zeta^2}$.
- Step response: %OS $=100 e^{-\pi\zeta/\sqrt{1-\zeta^2}}$; $t_s\approx 4/(\zeta\omega_n)$.

---

## Pitfalls and Tricky Edge Cases

### Fourier Series
1. **Average value $a_0$** — remember it equals the time-average, nothing else.
2. **Time shift preserves $|a_k|$**, changes only phase. Power/energy unchanged.
3. **Differentiation kills DC:** $d_0=0$ always since $jk\omega_0$ has $k=0$.
4. **Real signal $\Rightarrow a_{-k}=a_k^*$** (even $|a_k|$, odd $\angle a_k$). For complex $x$, symmetry does not hold.
5. **Euler expansion is the fastest route** for $\cos/\sin$ sums: $\cos\omega_0 t\to a_{\pm1}=1/2$, others zero.

### Convergence / Gibbs
6. **Gibbs 9% is independent of $N$.** Ripple narrows, peak does not.
7. **Dirichlet conditions are sufficient, not necessary.** Signals violating them often still have FS representations in a weaker sense.
8. **Spectral decay rate matches the first discontinuous derivative**, not the signal itself.

### DTFS
9. **Exactly $N$ coefficients**, not infinitely many. $a_{k+N}=a_k$ means harmonics beyond index $N$ repeat.
10. **No convergence issues in DT** — the synthesis sum is finite.

### Fourier Transform
11. **CTFT sanity:** $X(0)=\int x(t)dt$ is total area; $x(0)=\frac{1}{2\pi}\int X(j\omega)d\omega$.
12. **Frequency shift sign:** multiplying by $e^{j\omega_0 t}$ shifts spectrum to $\omega-\omega_0$ (shift **right**).
13. **$u(t)$ has a $\pi\delta(\omega)$ piece** (from the integration property), not just $1/(j\omega)$.
14. **Parseval constants:** CT FT $\int|x|^2dt=\frac{1}{2\pi}\int|X|^2d\omega$; CTFS $\frac{1}{T}\int|x|^2dt=\sum|a_k|^2$; DTFS $\frac{1}{N}\sum|x|^2=\sum|a_k|^2$; DTFT $\sum|x|^2=\frac{1}{2\pi}\int_{2\pi}|X|^2d\omega$.
15. **Convolution pipeline** is: transform → multiply → partial-fraction on $j\omega$ → invert via known pairs.

### Filters / Bode
16. **Ideal = noncausal = unrealizable.** Always.
17. **First-order $H=1/(a+j\omega)$:** $\omega_c=a$ (the pole). Don't confuse with $1/(1+j\omega/\omega_c)$ standard form.
18. **Second-order at $\omega_n$:** $|H|=1/(2\zeta)$ (not 1). DC gain is 1.
19. **Resonance only for $\zeta<1/\sqrt2$.** Above this, $|H|$ is monotone.
20. **Bode asymptotes are approximations.** At a first-order corner the true value is 3 dB below the broken asymptote line.
21. **Group delay constant $\Leftrightarrow$ linear phase.** Phase *slope* is what matters for delay, not phase value.
22. **Cascade rule:** multiply transfer functions (or add in dB); add phases.
23. **%OS and settling time apply only to the underdamped step response.** Critical/overdamped systems have no overshoot.

### Mixed
24. **Magnitude at $\omega=0$ vs at $\omega_n$ for second-order:** DC gain is 1, $|H(j\omega_n)|=1/(2\zeta)$.
25. **First-order-system phase at cutoff is $-45°$, not $-90°$.**
26. **Do not confuse $\omega_r$ and $\omega_n$** — $\omega_r<\omega_n$ when it exists.

---

*Prepared for CEC 315 Exam 2 — Spring 2026.*
