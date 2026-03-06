# Lecture 13: FT Properties and Convolution

## The Convolution Property (Most Important)

Convolution in time = multiplication in frequency:

$$y(t) = x(t) * h(t) \quad \longleftrightarrow \quad Y(j\omega) = X(j\omega) \cdot H(j\omega)$$

This is the **key payoff** of the frequency domain: replace difficult convolution integrals with simple multiplication.

### Analysis Pipeline

1. Transform input: $x(t) \to X(j\omega)$
2. Multiply: $Y(j\omega) = X(j\omega) \cdot H(j\omega)$
3. Inverse transform: $Y(j\omega) \to y(t)$
4. (Often use partial fractions for step 3)

## The Multiplication Property

Multiplication in time = convolution in frequency (scaled):

$$x(t) \cdot y(t) \quad \longleftrightarrow \quad \frac{1}{2\pi} [X(j\omega) * Y(j\omega)]$$

## CT FT Properties Table

| Property | Time Domain | Frequency Domain |
|---|---|---|
| Linearity | $ax(t) + by(t)$ | $aX(j\omega) + bY(j\omega)$ |
| Time Shift | $x(t - t_0)$ | $e^{-j\omega t_0} X(j\omega)$ |
| Frequency Shift | $e^{j\omega_0 t} x(t)$ | $X(j(\omega - \omega_0))$ |
| Time Scaling | $x(at)$ | $\frac{1}{|a|} X(j\omega/a)$ |
| Time Reversal | $x(-t)$ | $X(-j\omega) = X^*(j\omega)$ if real |
| Conjugation | $x^*(t)$ | $X^*(-j\omega)$ |
| Differentiation (time) | $\frac{d}{dt}x(t)$ | $j\omega \, X(j\omega)$ |
| Integration | $\int_{-\infty}^{t} x(\tau)d\tau$ | $\frac{1}{j\omega}X(j\omega) + \pi X(0)\delta(\omega)$ |
| Convolution | $x(t) * y(t)$ | $X(j\omega) Y(j\omega)$ |
| Multiplication | $x(t) y(t)$ | $\frac{1}{2\pi} X(j\omega) * Y(j\omega)$ |
| Duality | $X(jt)$ | $2\pi x(-\omega)$ |
| Parseval's | $\int|x(t)|^2 dt$ | $= \frac{1}{2\pi}\int|X(j\omega)|^2 d\omega$ |

## Duality

If $x(t) \longleftrightarrow X(j\omega)$, then $X(jt) \longleftrightarrow 2\pi x(-\omega)$.

Swap time and frequency roles to get new transform pairs for free.

## Time Scaling / Time-Frequency Trade-off

$$x(at) \longleftrightarrow \frac{1}{|a|} X(j\omega/a)$$

- **Compress in time** ($|a| > 1$): spectrum **expands** in frequency
- **Stretch in time** ($|a| < 1$): spectrum **compresses** in frequency
- You cannot be simultaneously narrow in both time and frequency

## Conjugate Symmetry (Real Signals)

For real $x(t)$: $X(-j\omega) = X^*(j\omega)$

This means:
- $|X(j\omega)|$ is **even** (symmetric)
- $\angle X(j\omega)$ is **odd** (antisymmetric)
- $\text{Re}\{X(j\omega)\}$ is even
- $\text{Im}\{X(j\omega)\}$ is odd

## Systems from Differential Equations

Replace $d/dt$ with $j\omega$ to convert differential equations to algebraic equations:

$$\sum_k b_k \frac{d^k y}{dt^k} = \sum_k c_k \frac{d^k x}{dt^k} \quad \longrightarrow \quad H(j\omega) = \frac{Y(j\omega)}{X(j\omega)} = \frac{\sum_k c_k (j\omega)^k}{\sum_k b_k (j\omega)^k}$$

## DT Convolution Property

$$y[n] = x[n] * h[n] \quad \longleftrightarrow \quad Y(e^{j\omega}) = X(e^{j\omega}) \cdot H(e^{j\omega})$$

### Systems from Difference Equations

Replace $x[n-k]$ with $e^{-j\omega k} X(e^{j\omega})$:

$$H(e^{j\omega}) = \frac{Y(e^{j\omega})}{X(e^{j\omega})} = \frac{\sum_k c_k e^{-j\omega k}}{\sum_k b_k e^{-j\omega k}}$$
