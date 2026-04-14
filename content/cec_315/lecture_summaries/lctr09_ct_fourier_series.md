# Lecture 9: Continuous-Time Fourier Series (CTFS)

## The Big Idea

Any periodic signal can be decomposed into a sum of harmonically related complex exponentials. Complex exponentials are **eigenfunctions** of LTI systems -- they pass through unchanged in frequency, only scaled in amplitude and shifted in phase.

## Periodic Signals

A signal is periodic if $x(t) = x(t + T)$ for all $t$, where $T$ is the fundamental period and $\omega_0 = 2\pi/T$ is the fundamental frequency.

## The Eigenfunction Property

For an LTI system with impulse response $h(t)$:

$$e^{st} \longrightarrow H(s) \cdot e^{st}$$

where the **system function** is:

$$H(s) = \int_{-\infty}^{\infty} h(\tau) e^{-s\tau} d\tau$$

The output is the same exponential scaled by $H(s)$. The frequency does **not** change.

For frequency analysis, set $s = j\omega$:

$$H(j\omega) = \int_{-\infty}^{\infty} h(\tau) e^{-j\omega\tau} d\tau$$

## The CTFS Pair

### Synthesis Equation (frequency -> time)

$$x(t) = \sum_{k=-\infty}^{\infty} a_k \, e^{jk\omega_0 t}$$

### Analysis Equation (time -> frequency)

$$a_k = \frac{1}{T} \int_T x(t) \, e^{-jk\omega_0 t} \, dt$$

### DC Component

$$a_0 = \frac{1}{T} \int_T x(t) \, dt = \text{average value of } x(t)$$

## How to Compute FS Coefficients

1. Identify $T$ and $\omega_0 = 2\pi/T$
2. Compute $a_0$ (average value)
3. Set up the analysis integral for general $a_k$
4. Integrate only over intervals where $x(t) \neq 0$
5. Evaluate and simplify

## Conjugate Symmetry (Real Signals)

If $x(t)$ is real-valued:
- $a_{-k} = a_k^*$ (conjugate symmetry)
- $|a_{-k}| = |a_k|$ (even magnitude spectrum)
- $\angle a_{-k} = -\angle a_k$ (odd phase spectrum)
