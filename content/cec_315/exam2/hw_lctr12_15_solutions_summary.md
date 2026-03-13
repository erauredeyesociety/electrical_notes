# Homework Solutions Summary: Lectures 12–15 (FT, Properties, Filters, Bode)

---

## Problem 1: CT Fourier Transform — Basic Pairs

### (a) One-Sided Exponential: $x(t) = 3e^{-5t}u(t)$
- $X(j\omega) = 3/(5 + j\omega)$
- $|X| = 3/\sqrt{25+\omega^2}$, $\angle X = -\arctan(\omega/5)$
- Sanity: $X(0) = 3/5 = 0.6 = \int_0^\infty 3e^{-5t}dt$ ✓

### (b) Two-Sided Exponential: $g(t) = 4e^{-2|t|}$
- Split integral at $t = 0$: $G(j\omega) = 4/(2-j\omega) + 4/(2+j\omega) = 16/(4+\omega^2)$
- Purely real (real & even signal → real & even spectrum, zero phase)
- Sanity: $G(0) = 4$ ✓

### (c) Rectangular Pulse: height 2, half-width 3
- $P(j\omega) = 4\sin(3\omega)/\omega$
- $P(0) = 12$ (total area) ✓
- First zeros at $\omega = \pi/3$ and $2\pi/3$

### (d) Sanity Check
$X(0) = \int_{-\infty}^{\infty} x(t)\,dt$ — verified for all three parts

---

## Problem 2: DTFT — Basic Pairs

### (a) $(0.6)^n u[n]$ → $X(e^{j\omega}) = 1/(1 - 0.6e^{-j\omega})$ via geometric series

### (b) Key Values and Spectrum Shape
- $X(e^{j0}) = 2.5$ (DC), $X(e^{j\pi}) = 0.625$ (Nyquist)
- DC > Nyquist → **lowpass** spectrum
- Periodic in $\omega$ with period $2\pi$

### (c) Finite-Length FIR: $h[n] = \{1,2,3,2,1\}$
- $H(e^{j0}) = 9$
- Factor: $H(e^{j\omega}) = e^{-j2\omega}[2\cos(2\omega) + 4\cos(\omega) + 3]$
- **Linear phase** with delay $n_d = 2$ (symmetric coefficients guarantee this)

---

## Problem 3: FT Properties and Convolution

### (a) Time Shift: $y(t) = e^{-3(t-2)}u(t-2)$
- $Y(j\omega) = e^{-j2\omega}/(3+j\omega)$
- $|Y| = |X|$ — time shift doesn't change magnitude, only adds linear phase

### (b) Frequency Shift: $z(t) = e^{-3t}u(t)\cos(10t)$
- $Z(j\omega) = \frac{1}{2}\left[\frac{1}{3+j(\omega-10)} + \frac{1}{3+j(\omega+10)}\right]$
- Spectrum splits into copies at $\pm 10$

### (c) Differentiation: $d/dt[e^{-3t}u(t)] = -3e^{-3t}u(t) + \delta(t)$
- $W(j\omega) = j\omega/(3+j\omega)$ — verified via both direct computation and differentiation property

### (d) Convolution Property with PFE
- $H(j\omega) = 2/(4+j\omega)$, $X(j\omega) = 1/(3+j\omega)$
- $Y = 2/[(3+j\omega)(4+j\omega)]$, PFE: $A = 2$, $B = -2$
- **$y(t) = 2(e^{-3t} - e^{-4t})u(t)$**
- Verified: $y(0) = 0$ ✓, $y(\infty) = 0$ ✓

---

## Problem 4: Systems from Equations

### (a) CT: $y'' + 7y' + 10y = 3x$
- $H(j\omega) = 3/[(j\omega+2)(j\omega+5)]$ — poles at $-2, -5$ → **stable**
- PFE: $H = 1/(j\omega+2) - 1/(j\omega+5)$
- $h(t) = (e^{-2t} - e^{-5t})u(t)$
- DC gain: $|H(0)| = 0.3$, decreasing with $\omega$ → **lowpass**

### (b) DT: $y[n] - 0.5y[n-1] - 0.06y[n-2] = x[n]$
- Poles at $z = 0.6$ and $z = -0.1$, both $|z| < 1$ → **stable**
- PFE: $A = 6/7$, $B = 1/7$
- $h[n] = (6/7)(0.6)^n u[n] + (1/7)(-0.1)^n u[n]$
- DC gain $\approx 2.273$, Nyquist gain $\approx 0.694$ → **lowpass**

---

## Problem 5: Magnitude, Phase, Group Delay

### $H(j\omega) = 1/(1 + j\omega/5)$, $\omega_c = 5$

### (a) Table of Values
| $\omega$ | $|H|$ | dB | Phase |
|---|---|---|---|
| 0 | 1 | 0 | 0° |
| 1 | 0.981 | $-0.17$ | $-11.3°$ |
| 5 | 0.707 | $-3.01$ | $-45°$ |
| 10 | 0.447 | $-6.99$ | $-63.4°$ |
| 50 | 0.0995 | $-20.04$ | $-84.3°$ |

### (b) Group Delay
$\tau(\omega) = 5/(25 + \omega^2)$. $\tau(0) = 0.2$ s, $\tau(5) = 0.1$ s. **Not constant** → nonlinear phase.

### (c) Linear Phase Test — FAILS
At $\omega = 5$: linear phase would give $-57.3°$, actual is $-45°$. Deviation = $12.3°$.

### (d) Two-Tone: $x(t) = \cos(t) + \cos(50t)$
- $y(t) \approx 0.981\cos(t - 11.3°) + 0.0995\cos(50t - 84.3°)$
- High-frequency component attenuated by $\sim 20$ dB relative to low

---

## Problem 6: Second-Order System ($\omega_n = 20$, $\zeta = 0.25$)

- **Underdamped** ($\zeta < 1$), resonance exists ($\zeta < 1/\sqrt{2}$)
- DC: $|H| = 1$ (0 dB); at $\omega_n$: $|H| = 1/(2\zeta) = 2$ (6.02 dB)
- $\omega_r = 18.71$ rad/s, peak $|H| = 2.065$ (6.30 dB)
- %OS = 44.4%, $t_s = 0.8$ s, $\omega_d = 19.36$ rad/s
- Bode: 0 dB flat → $-40$ dB/decade, break at $\omega_n = 20$
