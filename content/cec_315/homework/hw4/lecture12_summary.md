# Lecture 12: Continuous-Time and Discrete-Time Fourier Transforms

## 1. Motivation: From Fourier Series to Fourier Transform

The Fourier Series handles **periodic** signals by decomposing them into harmonically related sinusoids. But most real-world signals are **aperiodic** (pulses, transients, one-time events). The Fourier Transform extends spectral analysis to aperiodic signals.

**Core Idea:** Treat an aperiodic signal as a periodic signal whose period $T \to \infty$. As $T$ increases:
- The fundamental frequency $\omega_0 = 2\pi/T \to 0$
- Harmonic frequencies $k\omega_0$ become more densely packed
- The discrete spectrum becomes a **continuous** spectrum
- The FS coefficients $a_k$ become infinitesimal, but the **envelope** $T \cdot a_k$ approaches a smooth function $X(j\omega)$

## 2. CT Fourier Transform (CTFT)

### Analysis (Forward Transform)
$$X(j\omega) = \int_{-\infty}^{\infty} x(t) \, e^{-j\omega t} \, dt$$

- Input: time-domain signal $x(t)$
- Output: frequency-domain representation $X(j\omega)$, a **continuous** function of $\omega$
- $X(j\omega)$ is generally complex-valued

### Synthesis (Inverse Transform)
$$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) \, e^{j\omega t} \, d\omega$$

- The $1/(2\pi)$ factor appears in the inverse (Oppenheim convention)
- Reconstructs $x(t)$ by superposition of complex exponentials at all frequencies

### Convergence (Dirichlet Conditions for FT)
The CTFT exists if:
1. $x(t)$ is absolutely integrable: $\int_{-\infty}^{\infty} |x(t)| \, dt < \infty$
2. Finite number of maxima/minima and discontinuities in any finite interval

**Note:** Periodic signals and signals like $u(t)$ don't satisfy condition 1, but their FTs can be defined using impulse functions $\delta(\omega)$.

## 3. Basic CTFT Pairs

### One-Sided Decaying Exponential
$$x(t) = e^{-at}u(t), \quad a > 0$$

$$X(j\omega) = \int_0^{\infty} e^{-at} e^{-j\omega t} \, dt = \int_0^{\infty} e^{-(a+j\omega)t} \, dt = \frac{1}{a + j\omega}$$

**Key identity used:** $\int_0^{\infty} e^{-\alpha t} \, dt = \frac{1}{\alpha}$ for $\text{Re}(\alpha) > 0$

- Magnitude: $|X(j\omega)| = \frac{1}{\sqrt{a^2 + \omega^2}}$
- Phase: $\angle X(j\omega) = -\arctan(\omega/a)$
- Sanity check: $X(j0) = 1/a = \int_0^{\infty} e^{-at} \, dt$ ✓

### Two-Sided Decaying Exponential
$$x(t) = e^{-a|t|}, \quad a > 0$$

$$X(j\omega) = \frac{2a}{a^2 + \omega^2}$$

- Real and even (because $x(t)$ is real and even)
- Purely real spectrum — no imaginary part, zero phase

### Rectangular Pulse
$$x(t) = \begin{cases} 1 & |t| \leq T_1 \\ 0 & |t| > T_1 \end{cases}$$

$$X(j\omega) = \frac{2\sin(\omega T_1)}{\omega} = 2T_1 \, \text{sinc}\left(\frac{\omega T_1}{\pi}\right)$$

**Sinc conventions:**
- Oppenheim (used in this course): $\text{sinc}(\theta) = \frac{\sin(\pi\theta)}{\pi\theta}$
- Some texts: $\text{sinc}(\theta) = \frac{\sin(\theta)}{\theta}$

- First zero crossing at $\omega = \pi/T_1$
- Wider pulse → narrower main lobe (inverse relationship between time and frequency widths)

### Impulse Function
$$x(t) = \delta(t) \implies X(j\omega) = 1$$

- An impulse contains **all frequencies equally** — flat spectrum
- Inverse: $\delta(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{j\omega t} \, d\omega$

### Constant Signal
$$x(t) = 1 \implies X(j\omega) = 2\pi\delta(\omega)$$

- A constant has zero frequency content everywhere except DC
- Obtained via duality from the impulse pair

## 4. FT of Periodic Signals

A periodic signal $x(t) = \sum_k a_k e^{jk\omega_0 t}$ has the FT:

$$X(j\omega) = \sum_{k=-\infty}^{\infty} 2\pi a_k \, \delta(\omega - k\omega_0)$$

- Each harmonic produces an impulse in the frequency domain
- Impulse area = $2\pi a_k$
- This unifies FS and FT: periodic signals have **discrete** spectra (impulse trains), aperiodic signals have **continuous** spectra

## 5. Discrete-Time Fourier Transform (DTFT)

### Derivation from DT Fourier Series
Same limiting argument: take a periodic DT signal with period $N$, let $N \to \infty$.

### Analysis (Forward)
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j\omega n}$$

### Synthesis (Inverse)
$$x[n] = \frac{1}{2\pi} \int_{2\pi} X(e^{j\omega}) \, e^{j\omega n} \, d\omega$$

### Key Properties of DTFT
1. **Periodic in $\omega$ with period $2\pi$**: $X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$
   - Because $e^{-j(\omega+2\pi)n} = e^{-j\omega n} \cdot e^{-j2\pi n} = e^{-j\omega n}$ for integer $n$
   - Only need to specify $X(e^{j\omega})$ over one period, e.g., $-\pi < \omega \leq \pi$
2. **Convergence**: Requires $\sum |x[n]| < \infty$ (absolute summability)

## 6. Basic DTFT Pairs

### One-Sided Exponential
$$x[n] = a^n u[n], \quad |a| < 1$$

$$X(e^{j\omega}) = \sum_{n=0}^{\infty} (ae^{-j\omega})^n = \frac{1}{1 - ae^{-j\omega}}$$

Using geometric series formula $\sum_{n=0}^{\infty} r^n = \frac{1}{1-r}$ for $|r| < 1$.

- Sanity check: $X(e^{j0}) = \frac{1}{1-a} = \sum_{n=0}^{\infty} a^n$ ✓

### Finite-Length Sequence
For a finite sequence, the DTFT is always a finite sum (always converges).

### Unit Impulse
$$x[n] = \delta[n] \implies X(e^{j\omega}) = 1$$

## 7. CT vs DT Fourier Transform Summary

| Feature | CTFT | DTFT |
|---|---|---|
| Transform variable | $\omega$ (continuous, $-\infty$ to $\infty$) | $\omega$ (continuous, periodic with $2\pi$) |
| Forward transform | Integral over $t$ | Sum over $n$ |
| Inverse transform | Integral over $\omega$ (with $1/2\pi$) | Integral over one $2\pi$ period (with $1/2\pi$) |
| Convergence | Absolute integrability | Absolute summability |
| Spectrum | Generally aperiodic | Always $2\pi$-periodic |

## 8. Sanity Check Strategy

**Universal check:** The value at $\omega = 0$ should equal the total "mass" of the signal:
- CT: $X(j0) = \int_{-\infty}^{\infty} x(t) \, dt$
- DT: $X(e^{j0}) = \sum_{n=-\infty}^{\infty} x[n]$

This is the single most useful verification tool for any FT computation.
