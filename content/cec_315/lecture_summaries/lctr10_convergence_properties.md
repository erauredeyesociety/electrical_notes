# Lecture 10: Convergence, Properties, and DTFS

## Dirichlet Conditions for CTFS Convergence

The Fourier series converges for signals satisfying all three:

1. **Absolute integrability:** $\int_T |x(t)| \, dt < \infty$
2. **Bounded variation:** Finite number of maxima/minima per period
3. **Finite discontinuities:** Finite number of finite-jump discontinuities per period

At a **discontinuity**, the FS converges to the midpoint:

$$x_{FS}(t_0) = \frac{x(t_0^-) + x(t_0^+)}{2}$$

## Gibbs Phenomenon

- Near jump discontinuities, finite partial sums exhibit **overshoot ripples**
- Peak overshoot is always ~**9%** of jump height, regardless of number of harmonics
- Overshoot region narrows as $N \to \infty$ but peak amplitude stays at ~9%
- A finite sum of smooth sinusoids **cannot** reproduce a discontinuity

## Smoothness and Spectral Decay

| Signal Type | Spectral Decay | Smoothness |
|---|---|---|
| Jump discontinuity | $\|a_k\| \sim 1/k$ | 0 continuous derivatives |
| Continuous, $dx/dt$ discontinuous | $\|a_k\| \sim 1/k^2$ | 1st derivative discontinuous |
| General: $m$th derivative discontinuous | $\|a_k\| \sim 1/k^{m+1}$ | $m$ continuous derivatives |

**Key insight:** Smoother signals need fewer harmonics for accurate representation.

## CTFS Properties

| Property | Time Domain | Frequency Domain |
|---|---|---|
| Linearity | $Ax(t) + By(t)$ | $Aa_k + Bb_k$ |
| Time Shift | $x(t - t_0)$ | $a_k \, e^{-jk\omega_0 t_0}$ |
| Time Reversal | $x(-t)$ | $a_{-k}$ |
| Conjugation | $x^*(t)$ | $a_{-k}^*$ |
| Differentiation | $dx/dt$ | $jk\omega_0 \, a_k$ |
| Conjugate Symmetry | $x(t)$ real | $a_{-k} = a_k^*$ |

### Parseval's Relation (Average Power)

$$P = \frac{1}{T} \int_T |x(t)|^2 \, dt = \sum_{k=-\infty}^{\infty} |a_k|^2$$

Power is conserved across domains. Each $|a_k|^2$ gives the power in the $k$th harmonic.

## Key Property Implications

- **Time shift** changes phase but NOT magnitude: $|b_k| = |a_k|$, so power is preserved
- **Differentiation** amplifies high frequencies by factor $k$: acts as a highpass operation
- **DC component** ($k=0$) is always killed by differentiation: $d_0 = j(0)\omega_0 a_0 = 0$

## Discrete-Time Fourier Series (DTFS)

### Key Differences from CTFS

| Feature | CTFS | DTFS |
|---|---|---|
| Period | $T$ (continuous) | $N$ (integer samples) |
| Fundamental freq | $\omega_0 = 2\pi/T$ | $\omega_0 = 2\pi/N$ |
| Sum range | $k = -\infty$ to $\infty$ | $k = 0$ to $N-1$ (finite!) |
| Convergence issues | Yes (Dirichlet/Gibbs) | **None** (finite sum) |
| Coefficients | Aperiodic | **Periodic**: $a_{k+N} = a_k$ |

### DTFS Pair

**Synthesis:**
$$x[n] = \sum_{k=\langle N \rangle} a_k \, e^{jk(2\pi/N)n}$$

**Analysis:**
$$a_k = \frac{1}{N} \sum_{n=\langle N \rangle} x[n] \, e^{-jk(2\pi/N)n}$$

### Why Only N Coefficients?

Because $e^{j(k+N)(2\pi/N)n} = e^{jk(2\pi/N)n} \cdot e^{j2\pi n} = e^{jk(2\pi/N)n}$

The $(k+N)$th harmonic is **identical** to the $k$th harmonic. Adding more harmonics beyond $N$ produces no new signals.

### DT Parseval's Relation

$$\frac{1}{N} \sum_{n=\langle N \rangle} |x[n]|^2 = \sum_{k=\langle N \rangle} |a_k|^2$$
