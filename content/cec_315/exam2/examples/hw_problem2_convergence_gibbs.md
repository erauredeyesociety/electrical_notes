# Problem 2: CT Fourier Series Convergence and Gibbs Phenomenon

## Setup

**Given:** Odd square wave, $T = 2\pi$, $x(t) = +1$ for $0 < t < \pi$, $x(t) = -1$ for $-\pi < t < 0$.

## Part (a): Dirichlet Conditions

1. **Absolute integrability:** $\int_{-\pi}^{\pi} |x(t)|\,dt = \int_{-\pi}^{\pi} 1\,dt = 2\pi < \infty$ ✓
2. **Bounded variation:** Signal is piecewise constant, zero maxima/minima ✓
3. **Finite discontinuities:** Two jumps per period at $t = 0$ and $t = \pm\pi$, each of size 2 ✓

All satisfied → FS converges.

At discontinuities, FS converges to **midpoint**:

$$x_{FS}(0) = \frac{x(0^-) + x(0^+)}{2} = \frac{-1+1}{2} = 0$$

## Part (b): Convergence at Specific Points

- At $t = 0$ (discontinuity): $x_{FS}(0) = 0$ (midpoint)
- At $t = \pi/2$ (continuity): $x_{FS}(\pi/2) = x(\pi/2) = 1$ (exact value)

Three-term approximation at $\pi/2$:

$$x_3(\pi/2) = \frac{4}{\pi}\left[1 + \frac{-1}{3} + \frac{1}{5}\right] = \frac{4}{\pi} \cdot \frac{13}{15} \approx 1.103$$

Overshoots by ~10.3%. With more terms, this converges to 1.

## Part (c): Partial Sums and Gibbs

The odd square wave FS has only odd harmonics (sine terms):

$$x_1(t) = \frac{4}{\pi}\sin(t)$$

$$x_3(t) = \frac{4}{\pi}\left[\sin(t) + \frac{\sin(3t)}{3} + \frac{\sin(5t)}{5}\right]$$

**Gibbs overshoot:**
- Near each jump, partial sums overshoot by ~**8.9%** of jump height
- Overshoot does **not** disappear as $N \to \infty$
- Region narrows but peak stays at ~9%
- A finite sum of smooth sinusoids cannot reproduce a discontinuity

## Part (d): Smoothness vs Spectral Decay

| Signal | Decay | Smoothness |
|---|---|---|
| Square wave | $|a_k| \sim 1/k$ | Discontinuous |
| Triangular wave | $|a_k| \sim 1/k^2$ | Continuous, but $dx/dt$ discontinuous |

**Rule:** If the $m$th derivative is the first discontinuous one, coefficients decay as $1/k^{m+1}$.
