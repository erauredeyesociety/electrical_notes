# Lecture 12: Fourier Transforms (CT and DT)

## From Fourier Series to Fourier Transform

An aperiodic signal is a periodic signal with $T \to \infty$:
- Harmonics $k\omega_0$ become infinitesimally close ($\omega_0 \to 0$)
- Discrete spectrum becomes a **continuous spectrum**
- Sum becomes an integral

## CT Fourier Transform (CTFT) Pair

### Forward Transform (Analysis): time -> frequency

$$X(j\omega) = \int_{-\infty}^{\infty} x(t) \, e^{-j\omega t} \, dt$$

### Inverse Transform (Synthesis): frequency -> time

$$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) \, e^{j\omega t} \, d\omega$$

### Convergence

Same Dirichlet conditions as CTFS, plus absolute integrability:

$$\int_{-\infty}^{\infty} |x(t)| \, dt < \infty$$

## Basic CT FT Pairs

| Signal $x(t)$ | Transform $X(j\omega)$ |
|---|---|
| $e^{-at}u(t), \; a > 0$ | $\dfrac{1}{a + j\omega}$ |
| $e^{-a\|t\|}, \; a > 0$ | $\dfrac{2a}{a^2 + \omega^2}$ |
| $\delta(t)$ | $1$ |
| $1$ | $2\pi\delta(\omega)$ |
| $e^{j\omega_0 t}$ | $2\pi\delta(\omega - \omega_0)$ |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$ |
| $\sin(\omega_0 t)$ | $\frac{\pi}{j}[\delta(\omega - \omega_0) - \delta(\omega + \omega_0)]$ |
| Rectangular pulse (width $T_1$) | $\dfrac{2\sin(\omega T_1)}{\omega} = 2T_1 \text{sinc}\left(\frac{\omega T_1}{\pi}\right)$ |

## FT of Periodic Signals

A periodic signal $x(t) = \sum a_k e^{jk\omega_0 t}$ has FT:

$$X(j\omega) = \sum_{k=-\infty}^{\infty} 2\pi a_k \, \delta(\omega - k\omega_0)$$

The spectrum is a **train of impulses** at harmonic frequencies, weighted by $2\pi a_k$.

## Discrete-Time Fourier Transform (DTFT)

### DTFT Pair

**Forward:**
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j\omega n}$$

**Inverse:**
$$x[n] = \frac{1}{2\pi} \int_{2\pi} X(e^{j\omega}) \, e^{j\omega n} \, d\omega$$

### Key DTFT Properties
- $X(e^{j\omega})$ is always **periodic in $\omega$** with period $2\pi$
- Only need to specify over $[0, 2\pi)$ or $[-\pi, \pi)$

### Basic DT FT Pairs

| Signal $x[n]$ | Transform $X(e^{j\omega})$ |
|---|---|
| $a^n u[n], \; \|a\| < 1$ | $\dfrac{1}{1 - ae^{-j\omega}}$ |
| $\delta[n]$ | $1$ |
| $1$ | $2\pi \sum_k \delta(\omega - 2\pi k)$ |
| $e^{j\omega_0 n}$ | $2\pi \sum_k \delta(\omega - \omega_0 - 2\pi k)$ |

## The Four Fourier Representations

| Signal Type | Time | Frequency | Representation |
|---|---|---|---|
| CT Periodic | Continuous | Discrete | CTFS |
| CT Aperiodic | Continuous | Continuous | CTFT |
| DT Periodic | Discrete | Discrete | DTFS |
| DT Aperiodic | Discrete | Continuous | DTFT |

**Pattern:** Discrete in one domain $\Leftrightarrow$ Periodic in the other domain.
