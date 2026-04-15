# CEC 315 — Exam 3 Quick-Reference Notes (Lectures 16–23)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Purpose:** Quick-reference cheat sheet / study notes for Exam 3.

---

## Formula Tables

### Laplace Transform Pairs (Causal)

| $x(t)$ | $X(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $\delta(t-t_0)$ | $e^{-st_0}$ | all $s$ |
| $u(t)$ | $\dfrac{1}{s}$ | $\operatorname{Re}\{s\}>0$ |
| $tu(t)$ | $\dfrac{1}{s^2}$ | $\operatorname{Re}\{s\}>0$ |
| $\dfrac{t^{n-1}}{(n-1)!}u(t)$ | $\dfrac{1}{s^n}$ | $\operatorname{Re}\{s\}>0$ |
| $e^{-at}u(t)$ | $\dfrac{1}{s+a}$ | $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$ |
| $te^{-at}u(t)$ | $\dfrac{1}{(s+a)^2}$ | $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$ |
| $\dfrac{t^{n-1}}{(n-1)!}e^{-at}u(t)$ | $\dfrac{1}{(s+a)^n}$ | $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$ |
| $\cos(\omega_0 t)u(t)$ | $\dfrac{s}{s^2+\omega_0^2}$ | $\operatorname{Re}\{s\}>0$ |
| $\sin(\omega_0 t)u(t)$ | $\dfrac{\omega_0}{s^2+\omega_0^2}$ | $\operatorname{Re}\{s\}>0$ |
| $e^{-at}\cos(\omega_d t)u(t)$ | $\dfrac{s+a}{(s+a)^2+\omega_d^2}$ | $\operatorname{Re}\{s\}>-a$ |
| $e^{-at}\sin(\omega_d t)u(t)$ | $\dfrac{\omega_d}{(s+a)^2+\omega_d^2}$ | $\operatorname{Re}\{s\}>-a$ |
| $-e^{-at}u(-t)$ | $\dfrac{1}{s+a}$ | $\operatorname{Re}\{s\}<-\operatorname{Re}\{a\}$ |

### Laplace Properties

| Property | Time | $s$-Domain |
|---|---|---|
| Linearity | $ax+by$ | $aX+bY$ |
| Time shift | $x(t-t_0)$ | $e^{-st_0}X(s)$ |
| $s$-shift | $e^{s_0 t}x(t)$ | $X(s-s_0)$ |
| Scaling | $x(at)$, $a>0$ | $X(s/a)/a$ |
| Convolution | $x*y$ | $XY$ |
| Differentiation (bil.) | $dx/dt$ | $sX$ |
| Differentiation (unil.) | $dx/dt$ | $sX-x(0^-)$ |
| 2nd derivative (unil.) | $d^2x/dt^2$ | $s^2X - sx(0^-) - x'(0^-)$ |
| Integration | $\int x\,d\tau$ | $X/s$ |
| $s$-differentiation | $-tx(t)$ | $dX/ds$ |
| IVT | $x(0^+)$ | $\lim_{s\to\infty}sX(s)$ |
| FVT | $x(\infty)$ | $\lim_{s\to 0}sX(s)$ (if valid) |

### Z-Transform Pairs

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $\delta[n-k]$ | $z^{-k}$ | $|z|>0$ |
| $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $|z|>1$ |
| $a^n u[n]$ | $\dfrac{1}{1-az^{-1}}$ | $|z|>|a|$ |
| $-a^n u[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $|z|<|a|$ |
| $na^n u[n]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $|z|>|a|$ |
| $(n+1)a^n u[n]$ | $\dfrac{1}{(1-az^{-1})^2}$ | $|z|>|a|$ |
| $r^n\cos(\omega_0 n)u[n]$ | $\dfrac{1-r\cos\omega_0 z^{-1}}{1-2r\cos\omega_0 z^{-1}+r^2 z^{-2}}$ | $|z|>r$ |
| $r^n\sin(\omega_0 n)u[n]$ | $\dfrac{r\sin\omega_0 z^{-1}}{1-2r\cos\omega_0 z^{-1}+r^2 z^{-2}}$ | $|z|>r$ |

### Z-Transform Properties

| Property | Sequence | z-Domain |
|---|---|---|
| Linearity | $ax_1+bx_2$ | $aX_1+bX_2$ |
| Time shift | $x[n-n_0]$ | $z^{-n_0}X$ |
| z-scaling | $z_0^n x[n]$ | $X(z/z_0)$ |
| Time reversal | $x[-n]$ | $X(z^{-1})$ |
| Convolution | $x_1*x_2$ | $X_1 X_2$ |
| $z$-differentiation | $nx[n]$ | $-z\,dX/dz$ |
| First difference | $x[n]-x[n-1]$ | $(1-z^{-1})X$ |
| Accumulation | $\sum_{k\le n}x[k]$ | $X/(1-z^{-1})$ |
| Unilateral shift | $x[n-1]$ | $z^{-1}X+x[-1]$ |
| Unilateral shift-2 | $x[n-2]$ | $z^{-2}X + x[-1]z^{-1}+x[-2]$ |
| IVT | $x[0]$ | $\lim_{z\to\infty}X(z)$ |
| FVT | $x[\infty]$ | $\lim_{z\to 1}(1-z^{-1})X(z)$ |

---

## Per-Lecture Reference

### Lecture 16 — Laplace Transform and ROC
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr16-laplace-transform-roc.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr16_laplace_transform_roc.md`
- **Textbook:** Oppenheim §9.0–9.2 (pp. 654–670)

**Key ideas:**
- $X(s) = \int_{-\infty}^\infty x(t)e^{-st}dt$, with $s=\sigma+j\omega$.
- ROC is a vertical strip in the $s$-plane, never containing poles.
- Same $X(s)$, different ROC $\Rightarrow$ different signals (right- vs. left-sided).
- Right-sided $\Rightarrow$ ROC right of rightmost pole; left-sided $\Rightarrow$ ROC left of leftmost pole; two-sided $\Rightarrow$ strip between poles.
- FT exists iff $j\omega$-axis $\subset$ ROC.

### Lecture 17 — Inverse Laplace and Properties
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr17-inverse-laplace-properties.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr17_inverse_laplace_properties.md`
- **Textbook:** §9.3–9.6 (pp. 670–692)

**Key ideas:**
- Practical inversion = partial fractions + table.
- ROC $\Rightarrow$ direction of each term (right-sided vs. left-sided).
- Repeated poles of order $n$ $\Rightarrow$ $n$ terms $\frac{B_k}{(s-p)^k}$, $k=1,\ldots,n$.
- Complex conjugate poles $\Rightarrow$ complete the square, use $e^{-at}\cos/\sin$ pairs.
- Properties: linearity, time/shift, $s$-shift, convolution ($*$ $\to$ $\cdot$), differentiation $\to$ multiply by $s$.

### Lecture 18 — System Analysis via Unilateral Laplace
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr18_system_analysis_unilateral_laplace.md`
- **Textbook:** §9.7–9.9 (pp. 693–720)

**Key ideas:**
- $H(s) = Y(s)/X(s)$ from an ODE by $d^k/dt^k\to s^k$ (zero ICs).
- Causal + stable $\Leftrightarrow$ all poles in open LHP.
- Block diagrams: series $\to\times$, parallel $\to+$, feedback $\to H/(1+GH)$.
- Unilateral: $\mathcal{L}_u\{y'\} = sY - y(0^-)$, $\mathcal{L}_u\{y''\} = s^2 Y - s y(0^-)-y'(0^-)$.
- Total response = ZSR (from input) + ZIR (from ICs).

### Lecture 19 — Z-Transform and ROC
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr19-z-transform-roc.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr19_z_transform_roc.md`
- **Textbook:** §10.0–10.2 (pp. 741–757)

**Key ideas:**
- $X(z) = \sum_n x[n] z^{-n}$, $z = re^{j\omega}$.
- Unit circle $|z|=1$ replaces the $j\omega$-axis.
- ROC is annular ring; right-sided $\to$ exterior; left-sided $\to$ interior.
- DTFT exists iff unit circle $\subset$ ROC.
- CT/DT parallel: LHP $\to$ inside unit circle.

### Lecture 20 — Inverse Z-Transform and Properties
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr20-inverse-z-transform-properties.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr20_inverse_z_transform_properties.md`
- **Textbook:** §10.3–10.6 (pp. 757–774)

**Key ideas:**
- Partial fractions in $z^{-1}$ (not $z$!).
- ROC outside pole $\to$ right-sided $d^n u[n]$; inside $\to$ left-sided $-d^n u[-n-1]$.
- Complex poles at $re^{\pm j\omega_0}$ $\to$ damped sinusoid $r^n\cos/\sin(\omega_0 n)$.
- $z^{-1}$ is the unit-delay operator; basis of digital filter block diagrams.
- IVT (simple): $x[0]=\lim_{z\to\infty}X(z)$. FVT: $x[\infty]=\lim_{z\to 1}(1-z^{-1})X(z)$.

### Lecture 21 — System Analysis via Unilateral Z
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr21-system-analysis-unilateral-z.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr21_system_analysis_unilateral_z.md`
- **Textbook:** §10.7–10.9 (pp. 774–796)

**Key ideas:**
- $H(z) = Y/X$ from a difference equation by $y[n-k]\to z^{-k}Y$ (zero ICs).
- Causal + stable $\Leftrightarrow$ all poles inside unit circle ($|p_i|<1$).
- Unilateral shift: $x[n-1] \to z^{-1}X + x[-1]$ (note **plus**!).
- $z^{-1}$ block = one memory element in DSP.
- ZSR + ZIR decomposition works identically to CT.

### Lecture 22 — Sampling
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr22-sampling.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr22_sampling.md`
- **Textbook:** Ch. 7 (pp. 514–555)

**Key ideas:**
- Sampling in time $\to$ spectrum replication in frequency: $X_p(j\omega) = \frac{1}{T}\sum_k X(j(\omega-k\omega_s))$.
- Sampling theorem: $\omega_s > 2\omega_M$ (strict!).
- Ideal reconstruction uses LPF with gain $T$ + sinc interpolation.
- Aliasing is **irreversible**; use anti-aliasing filter before sampling.
- $\Omega = \omega T$ relates DT and CT frequencies.

### Lecture 23 — Linear Feedback Systems
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr23-linear-feedback-systems.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr23_linear_feedback_systems.md`
- **Textbook:** Ch. 11 §11.0–11.5 (pp. 816–866)

**Key ideas:**
- Closed-loop formula: $Q(s) = H/(1+GH)$. Characteristic equation: $1+GH=0$.
- Block diagram rules: cascade ($\times$), parallel ($+$), feedback.
- Feedback can stabilize unstable plants and reduce sensitivity.
- Nyquist criterion (open-loop stable version): closed-loop stable iff Nyquist plot does not encircle $-1/K$.
- Gain margin: dB below 0 dB at $\omega_1$ where $\angle GH = -180°$.
- Phase margin: degrees above $-180°$ at $\omega_2$ where $|GH| = 0$ dB.
- Both margins positive $\Rightarrow$ stable. $\tau_\text{max} = \text{PM}/\omega_2$.

---

## Pitfalls and Tricky Edge Cases

### Transform Pitfalls
1. **Always state the ROC.** $1/(s+3)$ is ambiguous without it.
2. **ROC — not pole sign — picks the direction** in partial-fraction inversion.
3. **Repeated poles need ALL orders.** $(s+1)^3$ $\Rightarrow$ terms $1/(s+1), 1/(s+1)^2, 1/(s+1)^3$.
4. **Complex poles:** complete the square, use trig pairs; don't split into complex partial fractions.
5. **Poles of $1/(1-az^{-1})$ are at $z=a$,** not $1/a$.
6. **Partial fractions in Z:** always work in $z^{-1}$, not $z$.

### Unilateral Transform Sign Conventions
- Laplace unilateral diff: $\mathcal{L}_u\{y'\} = sY - y(0^-)$ (minus).
- Z unilateral shift: $\mathcal{Z}_u\{y[n-1]\} = z^{-1}Y + y[-1]$ (plus).

### Stability Confusions
- CT: open LHP ($\operatorname{Re}\{s\}<0$). DT: interior of unit circle ($|z|<1$).
- $z=-0.9$ is stable (magnitude 0.9), even though on negative real axis.
- Marginally stable: poles on $j\omega$-axis (CT) or unit circle (DT) $\Rightarrow$ **not** BIBO stable.
- RHP zeros $\neq$ instability (only poles matter).

### Final-Value Theorem Traps
- Only valid if $sX(s)$ / $(1-z^{-1})X(z)$ has all poles strictly in open LHP / inside unit circle.
- If signal oscillates or grows, FVT gives meaningless result.

### Sampling Traps
- $\omega_s = 2\omega_M$ is **not** sufficient (Example 22.3).
- Mixing Hz and rad/s causes $2\pi$ errors.
- Aliasing is irreversible; anti-aliasing must happen before sampling.
- Squaring a signal **doubles** the bandwidth.
- Reconstruction LPF has gain $T$ (to cancel the $1/T$ replica scaling).
- Nyquist rate of $x(t-a) = $ same. Nyquist rate of $x(2t) = 2\times$ original.

### Feedback / Margin Traps
- Negative feedback $\to 1+GH$; positive feedback $\to 1-GH$.
- Open-loop poles (of $GH$) $\neq$ closed-loop poles (roots of $1+KGH=0$).
- GM read on magnitude plot at $\omega_1$ (where $\angle GH = -180°$).
- PM read on phase plot at $\omega_2$ (where $|GH| = 0$ dB).
- Feedback does **not** always stabilize (too much gain can push poles into RHP).
- First-order plants have infinite gain margin (phase never reaches $-180°$).
- Max tolerable delay: $\tau_{\max} = \text{PM (rad)}/\omega_2$.

### General ROC Reminders
- ROC never contains poles.
- ROC of right-sided: right of rightmost pole (CT) / outside outermost pole (DT).
- ROC of left-sided: left of leftmost pole (CT) / inside innermost pole (DT).
- ROC of two-sided: strip/annular ring between consecutive pole lines/circles; may be empty.
- Finite-duration: entire plane (except possibly $z=0,\infty$).

---

*Prepared for CEC 315 Exam 3 — Spring 2026.*
