# CEC 315 — Exam 3 Cheatsheet (Lec 16–23)

## Transform Definitions

| | Forward | Inverse |
|---|---|---|
| **Bilat. Laplace** | $X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}dt$ | $x(t)=\tfrac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}X(s)e^{st}ds$ |
| **Unilat. Laplace** | $\mathcal{X}(s)=\int_{0^-}^{\infty}x(t)e^{-st}dt$ | (contour, $\sigma$ in ROC) |
| **Bilat. Z** | $X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}$ | $x[n]=\tfrac{1}{2\pi j}\oint X(z)z^{n-1}dz$ |
| **Unilat. Z** | $\mathcal{X}(z)=\sum_{n=0}^{\infty}x[n]z^{-n}$ | (contour in ROC) |

$s=\sigma+j\omega$; $z=re^{j\Omega}$. FT exists iff $j\omega$-axis $\subset$ ROC; DTFT exists iff unit circle $\subset$ ROC.

## Laplace Pairs (causal unless noted)

| $x(t)$ | $X(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $\delta(t-t_0)$ | $e^{-st_0}$ | all $s$ |
| $u(t)$ | $1/s$ | $\operatorname{Re}\{s\}>0$ |
| $tu(t)$ | $1/s^2$ | $\operatorname{Re}\{s\}>0$ |
| $\tfrac{t^{n-1}}{(n-1)!}u(t)$ | $1/s^n$ | $\operatorname{Re}\{s\}>0$ |
| $e^{-at}u(t)$ | $\tfrac{1}{s+a}$ | $\operatorname{Re}\{s\}>-a$ |
| $te^{-at}u(t)$ | $\tfrac{1}{(s+a)^2}$ | $\operatorname{Re}\{s\}>-a$ |
| $\tfrac{t^{n-1}}{(n-1)!}e^{-at}u(t)$ | $\tfrac{1}{(s+a)^n}$ | $\operatorname{Re}\{s\}>-a$ |
| $\cos(\omega_0 t)u(t)$ | $\tfrac{s}{s^2+\omega_0^2}$ | $\operatorname{Re}\{s\}>0$ |
| $\sin(\omega_0 t)u(t)$ | $\tfrac{\omega_0}{s^2+\omega_0^2}$ | $\operatorname{Re}\{s\}>0$ |
| $e^{-at}\cos(\omega_d t)u(t)$ | $\tfrac{s+a}{(s+a)^2+\omega_d^2}$ | $\operatorname{Re}\{s\}>-a$ |
| $e^{-at}\sin(\omega_d t)u(t)$ | $\tfrac{\omega_d}{(s+a)^2+\omega_d^2}$ | $\operatorname{Re}\{s\}>-a$ |
| $-e^{-at}u(-t)$ | $\tfrac{1}{s+a}$ | $\operatorname{Re}\{s\}<-a$ |

## Laplace Properties

| Property | Time | $s$-Domain |
|---|---|---|
| Linearity | $ax+by$ | $aX+bY$; ROC $\supseteq R_x\cap R_y$ |
| Time shift | $x(t-t_0)$ | $e^{-st_0}X(s)$ |
| $s$-shift | $e^{s_0 t}x(t)$ | $X(s-s_0)$ |
| Scaling | $x(at),a\ne 0$ | $\tfrac{1}{\lvert a\rvert}X(s/a)$ |
| Diff. (bilat.) | $x'(t)$ | $sX(s)$ |
| Diff. (unilat.) | $x'(t)$ | $sX-x(0^-)$ |
| 2nd deriv (unilat.) | $x''(t)$ | $s^2X-sx(0^-)-x'(0^-)$ |
| Integration | $\int_{-\infty}^{t}x\,d\tau$ | $X(s)/s$ |
| Diff. in $s$ | $-tx(t)$ | $dX/ds$ |
| Convolution | $x*y$ | $X(s)Y(s)$ |
| **IVT** | $x(0^+)$ | $\lim_{s\to\infty}sX(s)$ |
| **FVT** | $x(\infty)$ | $\lim_{s\to 0}sX(s)$ |

**FVT valid iff** all poles of $sX(s)$ lie strictly in open LHP (else meaningless).

## Laplace ROC Rules

- ROC is a vertical strip, never contains poles.
- **Finite duration** $\Rightarrow$ entire $s$-plane.
- **Right-sided (causal):** $\operatorname{Re}\{s\}>\sigma_{\max}$ (right of rightmost pole).
- **Left-sided (anticausal):** $\operatorname{Re}\{s\}<\sigma_{\min}$.
- **Two-sided:** vertical strip between poles; may be empty.
- **Causal** $\Leftrightarrow$ rational + $M\le N$ + right-sided.
- **BIBO stable** $\Leftrightarrow$ $j\omega$-axis $\in$ ROC.
- **Causal + Stable** $\Leftrightarrow$ all poles $\operatorname{Re}\{p_i\}<0$.

## Z-Transform Pairs

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $\delta[n-k]$ | $z^{-k}$ | $z\ne 0$ ($k>0$) |
| $u[n]$ | $\tfrac{1}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
| $-u[-n-1]$ | $\tfrac{1}{1-z^{-1}}$ | $\lvert z\rvert<1$ |
| $a^n u[n]$ | $\tfrac{1}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $-a^n u[-n-1]$ | $\tfrac{1}{1-az^{-1}}$ | $\lvert z\rvert<\lvert a\rvert$ |
| $na^n u[n]$ | $\tfrac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $(n+1)a^n u[n]$ | $\tfrac{1}{(1-az^{-1})^2}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $\cos(\Omega_0 n)u[n]$ | $\tfrac{1-\cos\Omega_0\,z^{-1}}{1-2\cos\Omega_0\,z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ |
| $\sin(\Omega_0 n)u[n]$ | $\tfrac{\sin\Omega_0\,z^{-1}}{1-2\cos\Omega_0\,z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ |
| $r^n\cos(\Omega_0 n)u[n]$ | $\tfrac{1-r\cos\Omega_0\,z^{-1}}{1-2r\cos\Omega_0\,z^{-1}+r^2z^{-2}}$ | $\lvert z\rvert>r$ |
| $r^n\sin(\Omega_0 n)u[n]$ | $\tfrac{r\sin\Omega_0\,z^{-1}}{1-2r\cos\Omega_0\,z^{-1}+r^2z^{-2}}$ | $\lvert z\rvert>r$ |

## Z Properties

| Property | Sequence | $z$-Domain |
|---|---|---|
| Linearity | $ax_1+bx_2$ | $aX_1+bX_2$ |
| Time shift (bilat.) | $x[n-n_0]$ | $z^{-n_0}X(z)$ |
| $z$-scaling | $z_0^n x[n]$ | $X(z/z_0)$ |
| Time reversal | $x[-n]$ | $X(z^{-1})$ |
| Diff. in $z$ | $nx[n]$ | $-z\,dX/dz$ |
| First diff. | $x[n]-x[n-1]$ | $(1-z^{-1})X$ |
| Accumulation | $\sum_{k\le n}x[k]$ | $X/(1-z^{-1})$ |
| Convolution | $x_1*x_2$ | $X_1 X_2$ |
| **Unilat. shift-1** | $x[n-1]$ | $z^{-1}X+x[-1]$ |
| Unilat. shift-2 | $x[n-2]$ | $z^{-2}X+x[-1]z^{-1}+x[-2]$ |
| **IVT** | $x[0]$ | $\lim_{z\to\infty}X(z)$ |
| **FVT** | $x[\infty]$ | $\lim_{z\to 1}(1-z^{-1})X(z)$ |

**FVT valid iff** all poles of $(1-z^{-1})X(z)$ strictly inside unit circle.

## Z ROC Rules

- ROC is an annulus $r_1<|z|<r_2$, never contains poles.
- **Finite duration** $\Rightarrow$ entire $z$-plane (except possibly $0$ and/or $\infty$).
- **Right-sided (causal):** $|z|>r_{\max}$ (outside outermost pole); includes $z=\infty$ if causal.
- **Left-sided (anticausal):** $|z|<r_{\min}$.
- **Two-sided:** annular ring between poles.
- **BIBO stable** $\Leftrightarrow$ unit circle $\subset$ ROC.
- **Causal + Stable** $\Leftrightarrow$ all poles $|p_i|<1$.
- LHP (CT) $\leftrightarrow$ interior of unit circle (DT).

## Partial Fraction Expansion

**Distinct poles:** $X(s)=\sum_k\tfrac{A_k}{s-p_k}$, $\;A_k=(s-p_k)X(s)\big|_{s=p_k}$.

**Repeated pole** (order $r$ at $p$): $\sum_{k=1}^{r}\tfrac{B_k}{(s-p)^k}$, $\;B_k=\tfrac{1}{(r-k)!}\tfrac{d^{r-k}}{ds^{r-k}}\!\left[(s-p)^r X(s)\right]_{s=p}$.

**Complex conj. pair** $p=-a\pm j\omega_d$: complete the square; use $(s+a)^2+\omega_d^2$ denominator with $\cos/\sin$ pairs.

**Z-transform:** expand in $z^{-1}$, NOT $z$. ROC decides right- vs. left-sided for each term.

**Improper rationals (both $s$- and $z$-domain):** if $\deg(\text{num}) \ge \deg(\text{den})$, long-divide first to split into polynomial + strictly-proper. For **Laplace:** constant remainder $\to \delta(t)$, higher polynomial $\to \delta^{(k)}(t)$ (derivatives of $\delta$); PFE the strictly-proper part. For **Z:** polynomial piece in $z^{-1}$ corresponds to finite-duration samples (scaled $\delta[n-k]$); PFE the strictly-proper part in $z^{-1}$.

## Unilateral System Analysis

**CT (ODE):** $y^{(k)}\to s^kY-\sum_{j=0}^{k-1}s^{k-1-j}y^{(j)}(0^-)$. Solve for $Y(s)=Y_{\text{zs}}+Y_{\text{zi}}$; PFE; invert. $H(s)=Y_{\text{zs}}/X$.

**DT (diff. eq.):** $y[n-k]\to z^{-k}Y+\sum_{m=1}^{k}z^{-(k-m)}y[-m]$. Solve, PFE in $z^{-1}$, invert. $H(z)=Y_{\text{zs}}/X$.

**Total response** = ZSR (ICs$=0$) + ZIR (input$=0$).

## Sampling (Lec 22)

- Impulse train: $p(t)=\sum_n\delta(t-nT)$; $\omega_s=2\pi/T$, $f_s=1/T$.
- $x_p(t)=x(t)p(t)=\sum_n x(nT)\delta(t-nT)$.
- **Sampled spectrum:** $X_p(j\omega)=\tfrac{1}{T}\sum_{k=-\infty}^{\infty}X(j(\omega-k\omega_s))$.
- **Sampling Theorem:** bandlimited to $\omega_M \Rightarrow$ unique recovery iff $\omega_s>2\omega_M$ (strict). Nyquist rate $=2\omega_M$.
- **Aliasing** (undersampled): replicas overlap; $f_{\text{alias}}=|f_s-f_0|$ for $f_0\in(f_s/2,f_s)$; irreversible $\Rightarrow$ use anti-alias LPF first.
- **Ideal reconstruction:** LPF of gain $T$, cutoff $\omega_c\in(\omega_M,\omega_s-\omega_M)$, typically $\omega_s/2$.
- **Sinc interp.:** $x_r(t)=\sum_n x(nT)\,\operatorname{sinc}\!\left(\tfrac{t-nT}{T}\right)$, $\operatorname{sinc}(u)=\tfrac{\sin\pi u}{\pi u}$.
- **ZOH:** conv with rect width $T$; spectrum $H_0(j\omega)=\tfrac{2\sin(\omega T/2)}{\omega}e^{-j\omega T/2}$.
- **C/D mapping:** $\Omega=\omega T$ (rad/sample $=$ rad/s $\times T$).
- **Pitfall:** $\omega_s=2\omega_M$ not sufficient. Shift preserves Nyquist rate; $x(at)$ scales it by $|a|$.
- **Time multiplication $\to$ frequency convolution $\Rightarrow$ bandwidths add:** $x_1(t)x_2(t)$ has bandwidth $\le \omega_{M,1} + \omega_{M,2}$, so Nyquist rate of product $\le 2(\omega_{M,1} + \omega_{M,2})$. Special case: squaring doubles BW.

## Feedback Systems (Lec 23)

**Negative feedback** (forward $G$, feedback $H$):
$$T(s)=\dfrac{G(s)}{1+G(s)H(s)},\quad \text{unity fdbk: }T=\dfrac{G}{1+G}.$$
Positive fdbk: $G/(1-GH)$. Loop gain $L=GH$.

**Closed-loop poles** $=$ roots of $1+L(s)=0$ (characteristic equation). Feedback can stabilize unstable plants but also destabilize; open-loop poles $\ne$ closed-loop poles.

**Nyquist criterion** (plant open-loop stable): closed-loop stable iff Nyquist plot of $L(j\omega)$ does NOT encircle $-1$ (or $-1/K$ for variable gain $K$). General: $N=Z-P$ where $N=$ CW encirclements of $-1$, $P=$ open-loop RHP poles, $Z=$ closed-loop RHP poles; need $Z=0$.

**Gain margin** at $\omega_{180}$ (where $\angle L=-180°$):
$$\mathrm{GM}_{\mathrm{dB}}=-20\log_{10}|L(j\omega_{180})|.$$

**Phase margin** at $\omega_{\text{gc}}$ (where $|L|=1$):
$$\mathrm{PM}=180°+\angle L(j\omega_{\text{gc}}).$$

Both margins $>0\Rightarrow$ stable. Max delay: $\tau_{\max}=\mathrm{PM}_{\text{rad}}/\omega_{\text{gc}}$. First-order plants: $\mathrm{GM}=\infty$ (phase never hits $-180°$).

**Routh-Hurwitz** (for $a_ns^n+\cdots+a_0$): build array; # sign changes in first column $=$ # RHP roots. Necessary (not sufficient) condition: all $a_i>0$ with same sign; missing term $\Rightarrow$ unstable/marginal.

## Procedures (Step-by-Step Recipes)

**Inverse Laplace (causal/two-sided):**

1. Make $X(s)$ proper (polynomial + strictly-proper part) if needed.
2. Factor denominator $\Rightarrow$ PFE in $s$ (distinct, repeated, or complex-conj).
3. For complex-conj pair, **complete the square**: $(s+a)^2+\omega_d^2$.
4. Use ROC to pick right- vs. left-sided for each pole.
5. Look up each term in the pair table; sum.

**Inverse Z (in $z^{-1}$):**

1. If numerator order $\ge$ denominator order, **long-divide** first to pull out a polynomial part (finite-duration).
2. Factor denom; PFE in $z^{-1}$: $\sum A_k/(1-d_k z^{-1})$ + repeated-pole terms.
3. ROC outside $|d_k|$ $\Rightarrow$ right-sided $d_k^n u[n]$; inside $\Rightarrow -d_k^n u[-n-1]$.
4. For complex-conj pair with $p = r e^{\pm j\Omega_0}$: use $r^n\cos/\sin$ pair.

**Unilateral Laplace IVP (ODE + ICs):**

1. Transform: $y^{(k)} \to s^k Y - \sum_{j=0}^{k-1} s^{k-1-j}\,y^{(j)}(0^-)$.
2. Solve algebraically for $Y(s)$; separate $Y_{\text{ZS}}$ (input only) + $Y_{\text{ZI}}$ (ICs only) if asked.
3. PFE; invert.
4. Check $y(0^+)$ vs. given IC; check $y(\infty)$ via FVT if all $sX$ poles in LHP.

**Unilateral Z (difference eqn + ICs):**

1. Transform: $y[n-1]\to z^{-1}Y + y[-1]$; $y[n-2]\to z^{-2}Y + z^{-1}y[-1] + y[-2]$ (**plus** sign).
2. Solve for $Y(z)$; split ZSR / ZIR if asked.
3. PFE in $z^{-1}$; invert.
4. Sanity-check $y[0], y[1]$ from the difference equation directly.

**Block-diagram simplification:**

1. Reduce innermost feedback loop $\to H/(1+GH)$.
2. Replace it with a single block; re-draw.
3. Combine cascades (multiply) and parallel paths (add).
4. Final form: $Q = Y/X$; poles = roots of $1+GH = 0$.

**Aliased-frequency mapping** (pure sinusoid $f_0$, sample rate $f_s$):

- Define principal alias $f_a = |f_0 \bmod f_s|$, then fold: if $f_a > f_s/2$, reflect to $f_s - f_a$.
- Common shortcut for $f_s/2 < f_0 < f_s$: $f_{\text{alias}} = f_s - f_0$.
- In radians: $\omega_{\text{alias}} = \omega_0 - k\omega_s$ chosen so $|\omega_{\text{alias}}| \le \omega_s/2$.
- Sign flip $\Rightarrow$ reversed apparent direction (helicopter blade effect).

**Gain/Phase margin from Bode data:**

1. Read $\omega_{gc}$ at $|GH|=0$ dB $\Rightarrow \mathrm{PM} = 180^\circ + \angle GH(\omega_{gc})$.
2. Read $\omega_{pc}$ at $\angle GH = -180^\circ$ $\Rightarrow \mathrm{GM}_{\mathrm{dB}} = -|GH(\omega_{pc})|_{\mathrm{dB}}$.
3. Stable iff both $> 0$.
4. Max added delay: $\tau_{\max} = \mathrm{PM}_{\mathrm{rad}}/\omega_{gc}$.

## One-Liners / Traps

- $\delta\!\leftrightarrow\!1$; $u(t)\!\leftrightarrow\!1/s$; $e^{-at}u\!\leftrightarrow\!1/(s+a)$.
- $u[n]\!\leftrightarrow\!1/(1-z^{-1})$; $a^nu[n]\!\leftrightarrow\!1/(1-az^{-1})$, $|z|>|a|$.
- Unilat. Laplace diff: $sX-x(0^-)$ (**minus**). Unilat. Z shift: $z^{-1}X+x[-1]$ (**plus**).
- Conv $\leftrightarrow$ multiply. ROC of product $\supseteq$ intersection.
- Causal+Stable $\Leftrightarrow$ LHP poles (CT) / $|p|<1$ (DT).
- Poles of $1/(1-az^{-1})$ are at $z=a$, not $1/a$.
- PFE in Z: use $z^{-1}$, not $z$.
- Always state ROC; same $X(s)$ w/ diff. ROC $=$ diff. signals.
- FVT invalid if growing/oscillating.
- RHP **zero** $\ne$ instability (only poles).
- Marginal poles ($j\omega$-axis / unit circle) $\Rightarrow$ **not** BIBO stable.
- $f_{\text{alias}}=|f_s-f_0|$; $\omega_s>2\omega_M$ strict.
- $T=G/(1+GH)$; char. eq. $1+GH=0$.

## Coverage Checklist (Exam 3 Question Bank → Section)

| Topic / technique | Covered in |
|---|---|
| Compute $X(s)$ for causal/anti-causal/two-sided exponentials, shifted $\delta$, $te^{-at}$, sum of causal exponentials | Laplace Pairs, Laplace ROC |
| Inverse $X(s)$: distinct real, two-sided (annular), repeated, complex-conjugate via completing the square | PFE, Procedures — Inverse Laplace |
| $s$-shift, differentiation, convolution, IVT/FVT | Laplace Properties |
| $H(s)$ from ODE; pole-zero plot; causal vs anti-causal stability of $G(s)=3/(s-1)$ | Laplace ROC, One-Liners |
| Unilateral Laplace IVPs, ZSR/ZIR decomposition | Procedures — Unil. Laplace IVP |
| $X(z)$ for causal/anti-causal geometrics, $\delta[n-k]$, $na^n u[n]$, damped cos, two-sided | Z-Transform Pairs |
| Inverse $X(z)$: distinct, annular ROC, repeated, complex-conj damped cos | PFE, Procedures — Inverse Z |
| Time shift, $z$-scaling, convolution, IVT | Z Properties |
| $H(z)$ from difference eq; BIBO via unit circle; pole at $\|z\|>1$ causal vs anti-causal | Z ROC Rules |
| Unilateral Z with $y[-1],y[-2]$, ZSR/ZIR | Procedures — Unil. Z |
| Nyquist rate, max $T$, $\omega_s>2\omega_M$ strict, $\omega_s=2\omega_M$ failure | Sampling |
| Aliasing of cosines, helicopter-blade fold | Procedures — Aliased-frequency mapping |
| Anti-aliasing filter placement, reconstruction gain $T$, ZOH sinc droop | Sampling |
| Nyquist rate transforms under $x(t-t_0)$ and $x(at)$ | Sampling / One-Liners |
| Block diagram: cascade, parallel, nested feedback $\to Q=H/(1+GH)$ | Feedback, Procedures |
| Closed-loop pole vs $K$, stable range of $K$ (CT and DT) | Feedback |
| GM, PM, stability, max tolerable delay from Bode data | Procedures — GM/PM |
| T/F: negative feedback stabilizes? PM of 60° $\Rightarrow$ stable? Nyquist plot = $GH(j\omega)$? | Feedback, One-Liners |
