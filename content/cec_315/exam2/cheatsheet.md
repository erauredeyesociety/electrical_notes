# Quick Reference Cheat Sheet: CEC 315 Exam 2

## Step-by-Step Procedures

### How to find FS coefficients of a periodic signal

1. Find $T$ and $\omega_0 = 2\pi/T$
2. $a_0 = \frac{1}{T}\int_T x(t)\,dt$ (average value)
3. $a_k = \frac{1}{T}\int_T x(t)e^{-jk\omega_0 t}\,dt$ (integrate only where $x(t) \neq 0$)
4. Simplify using Euler's formula if needed

### How to find LTI output for periodic input

1. Find FS coefficients $\{a_k\}$ of input
2. Find $H(j\omega)$ from $h(t)$
3. Evaluate $H(jk\omega_0)$ at each harmonic
4. Output coefficients: $b_k = a_k \cdot H(jk\omega_0)$
5. Reconstruct: $y(t) = \sum b_k e^{jk\omega_0 t}$

### How to find output using convolution property

1. $X(j\omega) = \mathcal{F}\{x(t)\}$
2. $H(j\omega) = \mathcal{F}\{h(t)\}$
3. $Y(j\omega) = X(j\omega) \cdot H(j\omega)$
4. $y(t) = \mathcal{F}^{-1}\{Y(j\omega)\}$ (use partial fractions + known pairs)

### How to find $H(j\omega)$ from a differential equation

Replace $d^n/dt^n$ with $(j\omega)^n$, then solve $H(j\omega) = Y(j\omega)/X(j\omega)$.

### How to find cutoff frequency (first-order)

For $H(j\omega) = \frac{1}{a+j\omega}$: set $|H(j\omega_c)| = \frac{1}{\sqrt{2}}|H(0)|$ → $\omega_c = a$

## Quick Conversion Formulas

### Complex exponential ↔ trig

$$\cos(\omega t) = \frac{e^{j\omega t} + e^{-j\omega t}}{2} \qquad \sin(\omega t) = \frac{e^{j\omega t} - e^{-j\omega t}}{2j}$$

### Rectangular ↔ polar

$$A + jB = \sqrt{A^2+B^2} \; e^{j\arctan(B/A)}$$

$$|H| = \frac{1}{|a+j\omega|} = \frac{1}{\sqrt{a^2+\omega^2}} \qquad \angle H = -\arctan(\omega/a)$$

## Common Gotchas

- **DC killed by differentiation:** $d_0 = jk\omega_0 a_0|_{k=0} = 0$ always
- **Time shift preserves magnitude:** $|a_k e^{-jk\omega_0 t_0}| = |a_k|$
- **Gibbs overshoot is 9%** regardless of number of terms
- **DTFS has N coefficients** (periodic: $a_{k+N} = a_k$), no convergence issues
- **Ideal filters are noncausal** (sinc extends to $-\infty$)
- $\omega_c$ for $H = 1/(a+j\omega)$ is just $a$ (the pole)
- **Conjugate symmetry** for real signals: $a_{-k} = a_k^*$, $X(-j\omega) = X^*(j\omega)$
- **Parseval's uses $1/2\pi$** in CTFT: $\int|x|^2 dt = \frac{1}{2\pi}\int|X|^2 d\omega$

## Domain Relationships at a Glance

| Operation in Time | Effect in Frequency |
|---|---|
| Shift by $t_0$ | Multiply by $e^{-j\omega t_0}$ (phase change) |
| Scale by $a$ | Scale freq by $1/a$, amplitude by $1/|a|$ |
| Differentiate | Multiply by $j\omega$ (amplifies high freq) |
| Convolve | Multiply spectra |
| Multiply | Convolve spectra ($\div 2\pi$) |

| Operation in Frequency | Effect in Time |
|---|---|
| Shift by $\omega_0$ | Multiply by $e^{j\omega_0 t}$ (modulation) |
| Wider bandwidth | Sharper/faster time response |
| Linear phase | Pure delay (no distortion) |
