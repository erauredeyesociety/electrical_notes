# CEC 315 — Exam 1 Quick-Reference Notes (Lectures 2–8)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Purpose:** Quick-reference cheat sheet / study notes for Exam 1.

---

## Formula Tables

### Signal Transformations (CT)

| Operation | Expression | Effect |
|---|---|---|
| Time shift | $x(t-t_0)$ | Delay by $t_0>0$; advance by $t_0<0$ |
| Time reversal | $x(-t)$ | Mirror about $t=0$ |
| Time scaling | $x(at)$, $a>0$ | Compress if $a>1$; stretch if $a<1$ |
| Combined | $x(at-b)=x(a(t-b/a))$ | Shift by $b/a$, then scale by $a$ |
| Even part | $x_e(t)=\tfrac12[x(t)+x(-t)]$ | Symmetric |
| Odd part | $x_o(t)=\tfrac12[x(t)-x(-t)]$ | Anti-symmetric |

### Signal Energy and Power

| Quantity | CT | DT |
|---|---|---|
| Energy $E_\infty$ | $\int_{-\infty}^\infty \lvert x(t)\rvert^2 dt$ | $\sum_{n=-\infty}^\infty \lvert x[n]\rvert^2$ |
| Power $P_\infty$ | $\lim\frac{1}{2T}\int_{-T}^T \lvert x\rvert^2 dt$ | $\lim\frac{1}{2N+1}\sum_{-N}^N \lvert x\rvert^2$ |
| Finite-energy | $E_\infty<\infty$, $P_\infty=0$ | — |
| Finite-power | $P_\infty<\infty$, $E_\infty=\infty$ (e.g., sinusoid) | — |

### Complex Numbers and Euler

| Identity | Formula |
|---|---|
| Euler | $e^{j\phi}=\cos\phi+j\sin\phi$ |
| Inverse (cos) | $\cos\phi=\tfrac12(e^{j\phi}+e^{-j\phi})$ |
| Inverse (sin) | $\sin\phi=\tfrac{1}{2j}(e^{j\phi}-e^{-j\phi})$ |
| Polar / rect | $re^{j\theta}=r\cos\theta+jr\sin\theta$ |
| Magnitude | $r=\sqrt{a^2+b^2}$ |
| Angle | $\theta=\mathrm{atan2}(b,a)$ |
| Multiplication | magnitudes multiply, angles add |
| Division | magnitudes divide, angles subtract |
| CT sinusoid | $A\cos(\omega_0 t+\theta)$, $T_0=2\pi/|\omega_0|$ |
| Complex amplitude | $X_C=Ae^{j\theta}$ |
| DT periodicity | $\cos(\omega_0 n)$ periodic iff $\omega_0/(2\pi)\in\mathbb Q$ |
| Specials | $1=e^{j0}$, $j=e^{j\pi/2}$, $-1=e^{j\pi}$, $-j=e^{-j\pi/2}$ |

### Fundamental Functions

| Function | CT | DT |
|---|---|---|
| Impulse | $\delta(t)$: $\int\delta\,dt=1$ | $\delta[n]=1$ if $n=0$ |
| Step | $u(t)=1$ if $t>0$ | $u[n]=1$ if $n\ge 0$ |
| Ramp | $r(t)=tu(t)$ | $r[n]=nu[n]$ |
| $\delta\leftrightarrow u$ | $\delta=du/dt$; $u=\int\delta$ | $\delta[n]=u[n]-u[n-1]$ |
| Sifting (integral) | $\int x(\tau)\delta(\tau-t_0)d\tau=x(t_0)$ | $\sum_k x[k]\delta[k-n_0]=x[n_0]$ |
| Sampling (mult.) | $x(t)\delta(t-t_0)=x(t_0)\delta(t-t_0)$ | $x[n]\delta[n-k]=x[k]\delta[n-k]$ |
| Impulse scaling | $\delta(at)=\delta(t)/\lvert a\rvert$ | — |
| Doublet | $x(t)*\delta'(t)=dx/dt$ | — |

### CT ↔ DT Analogues (Systems)

| Concept | CT | DT |
|---|---|---|
| Signal decomposition | $x(t)=\int x(\tau)\delta(t-\tau)d\tau$ | $x[n]=\sum_k x[k]\delta[n-k]$ |
| Impulse response | $h(t)=T\{\delta(t)\}$ | $h[n]=T\{\delta[n]\}$ |
| Convolution | $y(t)=\int x(\tau)h(t-\tau)d\tau$ | $y[n]=\sum_k x[k]h[n-k]$ |
| Identity | $x*\delta=x$ | $x*\delta=x$ |
| Delay | $x*\delta(t-t_0)=x(t-t_0)$ | $x*\delta[n-n_0]=x[n-n_0]$ |
| Step response | $s(t)=\int_{-\infty}^t h(\tau)d\tau$ | $s[n]=\sum_{k\le n}h[k]$ |
| $h\leftrightarrow s$ | $h(t)=ds/dt$ | $h[n]=s[n]-s[n-1]$ |
| Memoryless | $h(t)=K\delta(t)$ | $h[n]=K\delta[n]$ |
| Causal | $h(t)=0$ for $t<0$ | $h[n]=0$ for $n<0$ |
| BIBO stable | $\int \lvert h\rvert dt<\infty$ | $\sum \lvert h[n]\rvert<\infty$ |
| Output length (finite) | — | $N+M-1$ |

### Convolution Properties

| Property | Statement |
|---|---|
| Commutative | $x*h=h*x$ |
| Associative (cascade) | $(x*h_1)*h_2=x*(h_1*h_2)$; $h_{\text{eq}}=h_1*h_2$ |
| Distributive (parallel) | $x*(h_1+h_2)=x*h_1+x*h_2$; $h_{\text{eq}}=h_1+h_2$ |
| Identity | $x*\delta=x$ |
| Delay | $x*\delta(t-t_0)=x(t-t_0)$ |
| Total area | $\int y\,dt = (\int x\,dt)(\int h\,dt)$ |
| Total sum (DT) | $\sum y = (\sum x)(\sum h)$ |

### Standard Convolution Results

| Pair | Result |
|---|---|
| Rect $*$ rect (same width) | Triangle |
| Rect $*$ rect (different widths) | Trapezoid |
| $u(t)*u(t)$ | $t u(t)=r(t)$ |
| $e^{-at}u(t)*u(t)$ | $\tfrac{1}{a}(1-e^{-at})u(t)$ |
| $e^{-at}u(t)*e^{-bt}u(t)$, $a\ne b$ | $\tfrac{1}{b-a}(e^{-at}-e^{-bt})u(t)$ |
| $u[n]*u[n]$ | $(n+1)u[n]$ |
| $\alpha^n u[n]*u[n]$ | $\dfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$ |

### First-Order Systems

| Quantity | CT | DT |
|---|---|---|
| Standard form | $\dfrac{dy}{dt}+ay=bx$ | $y[n]=\alpha y[n-1]+bx[n]$ |
| Impulse response | $h(t)=be^{-at}u(t)$ | $h[n]=b\alpha^n u[n]$ |
| Stability | $a>0$ | $|\alpha|<1$ |
| Step response | $(b/a)(1-e^{-at})u(t)$ | $b\dfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$ |

### Singularity Chain

$$r(t)=tu(t)\xrightarrow{d/dt}u(t)\xrightarrow{d/dt}\delta(t)\xrightarrow{d/dt}\delta'(t)$$

Reverse arrows via integration $\int_{-\infty}^t$.

---

## Per-Lecture Reference

### Lecture 2 — Signal Definitions and Transformations
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr02-sig-def-tran.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr02_signal_definitions_transformations.md`
- **Textbook:** Oppenheim §1.1–1.2 (pp. 1–13)

**Key ideas:**
- CT $x(t)$ vs. DT $x[n]$; DT arises from sampling $x[n]=x(nT_s)$.
- Energy ($\int|x|^2$) vs. power ($\lim\frac{1}{2T}\int|x|^2$); classify signals into three groups.
- Time shift / reversal / scaling; for $x(at-b)$ rewrite as $x(a(t-b/a))$.
- Periodicity: $T_0$ or $N_0$ smallest positive value such that $x=x(\cdot+T_0)$.
- Even/odd decomposition: $x_e=\tfrac12(x+x(-))$, $x_o=\tfrac12(x-x(-))$.

### Lecture 3 — Complex Exponentials and Sinusoidal Signals
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr03-complex-nums-exp-n-sinusoidal-sigs.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr03_complex_exponential_sinusoidal.md`
- **Textbook:** §1.3 (pp. 14–26)

**Key ideas:**
- Rectangular $a+jb$ vs. polar $re^{j\theta}$; $r=\sqrt{a^2+b^2}$, $\theta=\mathrm{atan2}(b,a)$.
- Euler $e^{j\phi}=\cos\phi+j\sin\phi$; derive trig identities by expanding $e^{j(\alpha\pm\beta)}$.
- CT sinusoid $A\cos(\omega_0 t+\theta)$ with period $T_0=2\pi/|\omega_0|$; complex amplitude $X_C=Ae^{j\theta}$.
- Real exponentials $Ce^{at}$: grow if $a>0$; decay if $a<0$.
- DT quirks: $\cos(\omega_0 n)$ periodic only if $\omega_0/(2\pi)\in\mathbb Q$; $e^{j(\omega_0+2\pi)n}=e^{j\omega_0 n}$.

### Lecture 4 — Key Functions and System Basics
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr04-key-fns-n-sys-basics.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr04_key_functions_system_basics.md`
- **Textbook:** §1.4–1.5 (pp. 30–43)

**Key ideas:**
- DT $\delta[n]$, $u[n]$; $\delta=u[n]-u[n-1]$; $u=\sum_{m\le n}\delta[m]$.
- CT Dirac $\delta(t)$: unit-area spike; $\delta=du/dt$; $u=\int_{-\infty}^t\delta d\tau$.
- Sifting (integral) yields a number; sampling (multiplication) yields a scaled impulse. **Don't confuse.**
- Any signal is a (weighted) sum / integral of shifted impulses.
- System basics: impulse response, series / parallel / feedback interconnections.

### Lecture 5 — Basic System Properties
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr05-basic-sys-properties.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr05_basic_system_properties.md`
- **Textbook:** §1.6 (pp. 44–55)

**Key ideas:**
- Six properties: memoryless, invertible, causal, stable, time-invariant, linear.
- **Linear:** superposition (additivity + homogeneity). Necessary: zero-in → zero-out.
- **Time-invariant:** explicit $t$ or $n$ in the equation is the red flag.
- **Causal (LTI):** $h=0$ for $t<0$ (or $n<0$).
- **BIBO stable (LTI):** $\int|h|<\infty$ or $\sum|h[n]|<\infty$.
- LTI systems are the only class we have the full toolkit for (convolution, transforms).

### Lecture 6 — DT LTI Convolution
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr06-dt-lti-convolution.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr06_dt_lti_convolution.md`
- **Textbook:** §2.1 (pp. 76–96)

**Key ideas:**
- Derive $y[n]=\sum_k x[k]h[n-k]$ by decomposing $x$ into impulses and applying linearity + time-invariance.
- Flip-and-slide: flip $h$, shift by $n$, multiply, sum.
- Output length (finite): $N+M-1$. Sanity: $(\sum x)(\sum h)=\sum y$.
- Properties: commutative, associative ($\Rightarrow$ cascade $h_1*h_2$), distributive ($\Rightarrow$ parallel $h_1+h_2$).
- Standard results: $x*\delta[n-n_0]=x[n-n_0]$; $\alpha^n u[n]*u[n]=\tfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$.

### Lecture 7 — CT LTI Properties and Convolution
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr07-ct-lti-properties.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr07_ct_lti_properties.md`
- **Textbook:** §2.2–2.3 (pp. 97–115)

**Key ideas:**
- Convolution integral $y(t)=\int x(\tau)h(t-\tau)d\tau$; same derivation as DT.
- Graphical method: find supports, flip-shift, identify overlap regions, write case-by-case integrals.
- LTI properties from $h(t)$: memoryless $\Leftrightarrow h=K\delta$; causal $\Leftrightarrow h=0$ for $t<0$; BIBO stable $\Leftrightarrow \int|h|<\infty$.
- Step response $s(t)=\int_{-\infty}^t h(\tau)d\tau$; $h(t)=ds/dt$.
- Causality and stability are independent.

### Lecture 8 — Difference / Differential Equations and Singularity Functions
- **PDF:** `/home/devel/electrical_notes/content/cec_315/all_lectures/cec315-lctr08-diff-eqns-singularity.pdf`
- **Summary:** `/home/devel/electrical_notes/content/cec_315/lecture_summaries/lctr08_diff_eqns_singularity.md`
- **Textbook:** §2.4–2.5 (pp. 116–140)

**Key ideas:**
- CT first order $dy/dt+ay=bx$: $h(t)=be^{-at}u(t)$; stable iff $a>0$.
- DT first order $y[n]=\alpha y[n-1]+bx[n]$: $h[n]=b\alpha^n u[n]$; stable iff $|\alpha|<1$.
- Find CT $h$ by homogeneous solution + jump condition across $t=0$; DT by iteration from initial rest.
- Singularity family: $r\to u\to\delta\to\delta'$ by $d/dt$; integration reverses.
- Impulse scaling: $\delta(at)=\delta(t)/|a|$; sampling: $x(t)\delta(t-t_0)=x(t_0)\delta(t-t_0)$; doublet: $x*\delta'=dx/dt$.

---

## Pitfalls and Tricky Edge Cases

### Signal and Transform Pitfalls
1. **Affine $\ne$ linear.** Always test zero-in / zero-out.
2. **Transformation order.** For $x(at-b)$, rewrite as $x(a(t-b/a))$ and shift by $b/a$, not $b$.
3. **DT periodicity.** Not every DT sinusoid is periodic; need $\omega_0/(2\pi)\in\mathbb Q$.
4. **Explicit $t$ or $n$ coefficient $\Rightarrow$ time-varying.** Examples: $tx(t)$, $nx[n]$, $x(2t)$.

### Sifting / Sampling Pitfalls
5. **Sifting is an integral; sampling is multiplication.** They look similar but produce different kinds of objects (number vs. scaled impulse).
6. **Check limits.** If $t_0$ is outside the integration range, $\int x(t)\delta(t-t_0)dt=0$.
7. **$(t+1)\delta(t)=\delta(t)$**, not $1$. Product with an impulse evaluates the smooth factor at the impulse location.

### Convolution Pitfalls
8. **Forget to flip.** Convolution is $h(t-\tau)$, meaning flip first then shift.
9. **Wrong limits.** Only integrate/sum where both signals are nonzero. Sketch!
10. **BIBO needs $|h|$.** $\int h\,dt$ without absolute value does *not* measure stability.
11. **Cascade vs. parallel.** Series $\to h_1*h_2$; parallel $\to h_1+h_2$.
12. **Output length (DT).** $N+M-1$, not $\max(N,M)$.

### LTI Property Pitfalls
13. **Causality vs. stability independence.** $e^{2t}u(t)$ is causal but unstable; $e^t u(-t)$ is stable but non-causal.
14. **Memoryless LTI $\Rightarrow h=K\delta$.** Anything with even a tiny decay has memory.
15. **DT stability is magnitude.** $\alpha=-0.9$ is stable ($|\alpha|=0.9<1$), even though on the negative real axis.

### Differential / Difference Equation Pitfalls
16. **Sign of $a$ in $h=e^{-at}u(t)$.** From $dy/dt+ay=bx$ you get $e^{-at}$, not $e^{+at}$. Stable iff $a>0$.
17. **Missing $u(t)$ or $u[n]$.** Causal impulse responses *must* include the step to enforce zero for $t<0$.
18. **Initial rest.** Default for diff-eqn problems unless stated: $y(0^-)=0$, or $y[n]=0$ for $n<0$.
19. **Jump condition.** From $dy/dt+ay=\delta(t)$, integrating across 0 gives $h(0^+)-h(0^-)=1$, not 0.

### Singularity Function Pitfalls
20. **$\delta(at)=\delta(t)/|a|$**, with absolute value. Compressing doubles the "height," but area stays 1.
21. **Integrating $\delta'$ under the integral.** Doublet is distributional: $\int x(t)\delta'(t-t_0)dt=-x'(t_0)$.
22. **Ramp vs. step vs. impulse chain.** Memorize the differentiation arrow: $r\to u\to\delta\to\delta'$.

---

*Prepared for CEC 315 Exam 1 — Spring 2026.*
