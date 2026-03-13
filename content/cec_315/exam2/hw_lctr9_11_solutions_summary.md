# Homework Solutions Summary: Lectures 9–11 (FS, Convergence, Frequency Response)

---

## Problem 1: Eigenfunction Property and CT Fourier Series Coefficients

### Part (a): Eigenfunction Property
- **Given:** $h(t) = e^{-4t}u(t)$, input $x(t) = \cos(3t)$
- $H(j3) = 1/(4+j3)$, convert: $|H(j3)| = 1/5 = 0.2$, $\angle H(j3) = -\arctan(3/4) = -36.87°$
- **Output:** $y(t) = 0.2\cos(3t - 36.87°)$
- **Key:** Frequency unchanged — only amplitude scaled and phase shifted (eigenfunction property)

### Part (b): Fourier Series Coefficients
- **Given:** $x(t)$ periodic with $T = 4$, $x(t) = 3$ for $0 \leq t < 1$, $x(t) = 0$ for $1 \leq t < 4$
- $\omega_0 = \pi/2$ rad/s
- $a_0 = 3/4 = 0.75$ (DC = average value)
- General: $a_k = \frac{3}{2jk\pi}(1 - e^{-jk\pi/2})$ for $k \neq 0$
- Numerical: $a_1 = 3(1-j)/(2\pi)$, $|a_1| = 3\sqrt{2}/(2\pi) \approx 0.675$, $\angle a_1 = -45°$
- $a_2 = -3j/(2\pi)$, $|a_2| = 3/(2\pi) \approx 0.477$, $\angle a_2 = -90°$

### Part (c): Conjugate Symmetry Verification
- Computed $a_{-1} = 3(1+j)/(2\pi) = a_1^*$ ✓
- Holds for **any real-valued** signal

---

## Problem 2: Convergence and Gibbs Phenomenon

### Part (a): Dirichlet Conditions
- **Given:** Odd square wave, $T = 2\pi$, $x(t) = +1$ for $0 < t < \pi$, $x(t) = -1$ for $-\pi < t < 0$
- All three conditions verified: absolutely integrable, bounded variation, finite discontinuities

### Part (b): Convergence at Specific Points
- At discontinuity $t = 0$: FS converges to midpoint $(−1+1)/2 = 0$
- At continuity $t = \pi/2$: converges to $x(\pi/2) = 1$

### Part (c): Gibbs Phenomenon
- Partial sums: $x_1(t) = (4/\pi)\sin(t)$, $x_3(t) = (4/\pi)[\sin(t) + \sin(3t)/3 + \sin(5t)/5]$
- Three-term approximation at $t = \pi/2$: $\approx 1.103$ (overshoots by ~10.3%)
- **Gibbs overshoot ≈ 9%** of jump height, does NOT vanish as $N \to \infty$
- Ripple narrows but peak persists — finite sum of smooth functions can't reconstruct a discontinuity

### Part (d): Smoothness and Spectral Decay
| Signal | Decay | Smoothness |
|---|---|---|
| Square wave | $\sim 1/k$ | Discontinuous |
| Triangular wave | $\sim 1/k^2$ | Continuous, derivative discontinuous |

- General rule: first discontinuous derivative is $m$th → coefficients decay as $1/k^{m+1}$

---

## Problem 3: CT Fourier Series Properties

**Given:** $x(t)$ real, $T = \pi$, $\omega_0 = 2$, $a_0 = 2$, $a_{\pm 1} = 1$, $a_{\pm 2} = 1/4$, $a_{\pm 3} = 1/9$

### Part (a): Linearity
- FS coefficients of $\sin(2t)$: $b_1 = -j/2$, $b_{-1} = j/2$, all others zero
- For $w(t) = 4x(t) + 6\sin(2t)$: $c_k = 4a_k + 6b_k$
- $c_0 = 8$, $c_1 = 4 - 3j$, $c_{-1} = 4 + 3j$, $c_{\pm 2} = 1$, $c_{\pm 3} = 4/9$

### Part (b): Time-Shifting Property
- $y(t) = x(t - \pi/4)$, so $b_k = a_k e^{-jk\pi/2}$
- $b_0 = 2$, $b_{\pm 1} = \mp j$, $b_{\pm 2} = -1/4$, $b_{\pm 3} = \pm j/9$
- **Magnitude unchanged:** $|b_k| = |a_k|$ for all $k$ — time shift only changes phase
- Same average power by Parseval's

### Part (c): Differentiation Property
- $g(t) = dx/dt$: $d_k = jk\omega_0 a_k = 2jk \cdot a_k$
- $|d_1| = 2$, $|d_2| = 1$, $|d_3| = 2/3$
- Ratio $|d_k|/|a_k| = 2|k|$ grows linearly — differentiation amplifies high frequencies ("sharpens" signal, amplifies noise)

### Part (d): Parseval's Theorem
- $P_x = |a_0|^2 + 2(|a_1|^2 + |a_2|^2 + |a_3|^2) = 4 + 2(1 + 1/16 + 1/81) \approx 6.1497$
- Exact: $P_x = 6 \frac{97}{648}$
- DC fraction: $|a_0|^2/P_x = 4/6.1497 \approx 65\%$

---

## Problem 4: DT Fourier Series

**Given:** $x[n]$ periodic with $N = 6$, one period: $x[n] = 1$ for $n = 0, 1, 2$ and $x[n] = 0$ for $n = 3, 4, 5$

- $\omega_0 = 2\pi/6 = \pi/3$
- $a_k = \frac{1}{6}\sum_{n=0}^{2} e^{-jk(\pi/3)n}$ (only 3 nonzero terms)
- $a_0 = 3/6 = 1/2$
- $a_1 = \frac{1}{6}(1 + e^{-j\pi/3} + e^{-j2\pi/3})$
- Coefficients are periodic: $a_{k+6} = a_k$ (only 6 distinct values)
- Parseval's verified: $(1/6)\sum|x[n]|^2 = 3/6 = 1/2 = \sum|a_k|^2$

---

## Problem 5: Frequency Response and Filtering

**Given:** $h(t) = e^{-3t}u(t)$, so $H(j\omega) = 1/(3 + j\omega)$

### Frequency Response at Harmonics
- Input: multi-frequency periodic signal
- Evaluate $H(jk\omega_0)$ at each harmonic, multiply by input coefficient
- Output coefficients: $b_k = a_k \cdot H(jk\omega_0)$

### Filter Identification
- $|H(j\omega)|$ decreases with $\omega$ → **lowpass filter**
- Cutoff: $\omega_c = 3$ rad/s ($-3$ dB point where $|H| = 1/\sqrt{2}$)
- Higher pole value → wider bandwidth (faster system, less filtering)
