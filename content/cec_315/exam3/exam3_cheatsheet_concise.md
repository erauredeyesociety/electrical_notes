# CEC 315 — Exam 3 Concise Cheatsheet (Lec 16–23)

One-page distillation. See [exam3_cheatsheet.md](exam3_cheatsheet.md) for the full comprehensive version.

## Definitions & ROC Essentials

| | Forward | FT exists iff |
|---|---|---|
| Laplace | $X(s)=\int x(t)e^{-st}dt$ | $j\omega$-axis $\subset$ ROC |
| Z | $X(z)=\sum x[n]z^{-n}$ | unit circle $\subset$ ROC |

ROC rules: never contains poles; right-sided $\Rightarrow$ $\sigma>\sigma_{\max}$ / $|z|>r_{\max}$; left $\Rightarrow$ reverse; two-sided $\Rightarrow$ strip / annulus. **Causal + stable** $\Leftrightarrow$ poles in LHP (CT) / inside unit circle (DT).

## Must-Know Transform Pairs

**Laplace (causal):** $\delta\to 1$; $u\to 1/s$; $e^{-at}u\to\tfrac{1}{s+a}$; $te^{-at}u\to\tfrac{1}{(s+a)^2}$; $\cos\omega_0 t\,u\to\tfrac{s}{s^2+\omega_0^2}$; $\sin\omega_0 t\,u\to\tfrac{\omega_0}{s^2+\omega_0^2}$; $e^{-at}\cos\omega_d t\,u\to\tfrac{s+a}{(s+a)^2+\omega_d^2}$; $\delta(t-t_0)\to e^{-st_0}$. Anti-causal: $-e^{-at}u(-t)\to\tfrac{1}{s+a}$, $\sigma<-a$.

**Z (causal):** $\delta[n]\to 1$; $u[n]\to\tfrac{1}{1-z^{-1}}$; $a^nu[n]\to\tfrac{1}{1-az^{-1}}$, $|z|>|a|$; $na^nu[n]\to\tfrac{az^{-1}}{(1-az^{-1})^2}$; $\delta[n-k]\to z^{-k}$; $r^n\cos(\Omega_0 n)u[n]\to\tfrac{1-r\cos\Omega_0 z^{-1}}{1-2r\cos\Omega_0 z^{-1}+r^2z^{-2}}$. Anti-causal: $-a^nu[-n-1]\to\tfrac{1}{1-az^{-1}}$, $|z|<|a|$.

## Key Properties

Linearity; convolution $\leftrightarrow$ product; $e^{s_0t}x\to X(s-s_0)$; $x(t-t_0)\to e^{-st_0}X(s)$; $-tx\to dX/ds$; $x[n-n_0]\to z^{-n_0}X$; $z_0^n x[n]\to X(z/z_0)$; $nx[n]\to -z\,dX/dz$.

**IVT / FVT:** $x(0^+)=\lim_{s\to\infty}sX$; $x(\infty)=\lim_{s\to 0}sX$ (valid iff $sX$ poles all in LHP). $x[0]=\lim_{z\to\infty}X$; $x[\infty]=\lim_{z\to 1}(1-z^{-1})X$.

## Unilateral (ICs) — sign traps

**Laplace (MINUS):** $y'\to sY-y(0^-)$; $y''\to s^2Y-sy(0^-)-y'(0^-)$.

**Z (PLUS):** $y[n-1]\to z^{-1}Y+y[-1]$; $y[n-2]\to z^{-2}Y+z^{-1}y[-1]+y[-2]$.

**Total response** = ZSR (input only, IC=0) + ZIR (IC only, input=0).

## PFE Recipe

Distinct: $\sum A_k/(s-p_k)$, $A_k=(s-p_k)X(s)|_{s=p_k}$.
Repeated order $r$ at $p$: $\sum_{k=1}^{r}B_k/(s-p)^k$, $B_k=\tfrac{1}{(r-k)!}\tfrac{d^{r-k}}{ds^{r-k}}[(s-p)^r X]|_{s=p}$; pair $\tfrac{1}{(s+a)^k}\leftrightarrow \tfrac{t^{k-1}}{(k-1)!}e^{-at}u$.
Complex-conj: complete the square $(s+a)^2+\omega_d^2$; use $\cos/\sin$ pairs.
**Z:** always in $z^{-1}$; long-divide first if improper. ROC picks direction per pole.

## Sampling

$X_p(j\omega)=\tfrac{1}{T}\sum_k X(j(\omega-k\omega_s))$, $\omega_s=2\pi/T$. Theorem: $\omega_s>2\omega_M$ (**strict**); Nyquist rate $=2\omega_M$. Reconstruction: LPF gain $T$, cutoff $\in(\omega_M,\omega_s-\omega_M)$; $x_r(t)=\sum x(nT)\mathrm{sinc}((t-nT)/T)$. **Aliased frequency:** $|f_s-f_0|$ for $f_s/2<f_0<f_s$ (sign $\Rightarrow$ reversed direction). Aliasing irreversible $\Rightarrow$ anti-alias LPF BEFORE sampler. $\omega_s=2\omega_M$ not sufficient. ZOH droop: $H_0(j\omega)=\tfrac{2\sin(\omega T/2)}{\omega}e^{-j\omega T/2}$. $x(t-t_0)$ preserves Nyquist rate; $x(at)$ scales it by $|a|$.

## Feedback

$T=\dfrac{G}{1+GH}$ (neg), $\dfrac{G}{1-GH}$ (pos). Closed-loop poles $=$ roots of $1+GH=0$. **Cascade** $\cdot$, **parallel** $+$, **nested**: reduce innermost loop first. Instability iff $GH=-1$ (0 dB + $-180^\circ$).

$\mathrm{PM}=180^\circ+\angle GH(\omega_{gc})$ at $|GH|=0$ dB.
$\mathrm{GM}_\mathrm{dB}=-|GH(\omega_{pc})|_\mathrm{dB}$ at $\angle GH=-180^\circ$.
Both $>0 \Rightarrow$ stable; max delay $\tau_{\max}=\mathrm{PM}_\mathrm{rad}/\omega_{gc}$. Nyquist: plot $GH(j\omega)$; no encirclement of $-1/K$ $\Rightarrow$ stable (open-loop stable case).

## Top Traps

- Always state the ROC; same $X$ + different ROC $=$ different signals.
- Unilateral Laplace: **minus** $y(0^-)$. Unilateral Z: **plus** $y[-1]$.
- Repeated pole order $n$ needs $n$ PFE terms.
- DT stability: $|a|<1$, not $a<1$ (pole at $z=-0.9$ IS stable).
- FVT invalid if system unstable or has poles on $j\omega$/unit circle.
- Strict $\omega_s>2\omega_M$, not $\ge$.
- Aliasing is irreversible — AAF before the sampler, never after.
- GM from magnitude at $-180^\circ$ freq; PM from phase at 0-dB freq — don't swap.
- First-order plant: $\mathrm{GM}=\infty$ (phase never hits $-180^\circ$).
