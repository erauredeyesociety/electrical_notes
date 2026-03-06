# Problem 5: Frequency Response and Filtering

## Setup

**Given:** $h(t) = e^{-3t}u(t)$, input $x(t) = 2 + 4\cos(3t) + 2\cos(9t)$.

## Part (a): Frequency Response $H(j\omega)$

$$H(j\omega) = \int_0^{\infty} e^{-3\tau} e^{-j\omega\tau} d\tau = \frac{1}{3 + j\omega}$$

Cutoff: $\omega_c = a = 3$ rad/s (pole location).

## Part (b): Evaluate at Each Harmonic

Input has frequencies $\omega = 0, 3, 9$:

| $\omega$ (rad/s) | $H(j\omega)$ | $\|H(j\omega)\|$ | $\angle H(j\omega)$ |
|---|---|---|---|
| 0 | $1/3$ | $1/3 \approx 0.333$ | $0°$ |
| 3 | $\frac{1}{3(1+j)}$ | $\frac{1}{3\sqrt{2}} \approx 0.236$ | $-45°$ |
| 9 | $\frac{1}{3(1+j3)}$ | $\frac{1}{3\sqrt{10}} \approx 0.105$ | $-71.57°$ |

## Part (c): Output Signal

Apply eigenfunction property to each component:

**DC** ($\omega = 0$): $2 \times \frac{1}{3} = \frac{2}{3}$

**Fundamental** ($\omega = 3$): $4 \times \frac{1}{3\sqrt{2}}\cos(3t - 45°) = \frac{2\sqrt{2}}{3}\cos(3t-45°)$

**Third harmonic** ($\omega = 9$): $2 \times \frac{1}{3\sqrt{10}}\cos(9t - 71.57°) = \frac{2}{3\sqrt{10}}\cos(9t - 71.57°)$

$$\boxed{y(t) = 0.667 + 0.943\cos(3t-45°) + 0.211\cos(9t-71.57°)}$$

## Part (d): Filtering Interpretation

### Lowpass or highpass?

$|H(j\omega)|$ **decreases** with $\omega$: $0.333 \to 0.236 \to 0.105$

This is a **lowpass filter**.

### Amplitude ratio

$$\frac{|H(j9)|}{|H(j3)|} = \frac{1/\sqrt{10}}{1/\sqrt{2}} = \frac{\sqrt{2}}{\sqrt{10}} = \frac{1}{\sqrt{5}} \approx 0.447$$

The $\omega = 9$ component is attenuated by an additional factor of $1/\sqrt{5}$ relative to $\omega = 3$.

### Cutoff frequency

Set $|H(j\omega_c)| = \frac{1}{\sqrt{2}}|H(0)|$:

$$\frac{1}{\sqrt{9 + \omega_c^2}} = \frac{1}{\sqrt{2}} \cdot \frac{1}{3} \implies \omega_c = 3 \text{ rad/s}$$

Note: $\omega = 3$ is exactly the cutoff, which is why $\angle H(j3) = -45°$.

## Part (e): Effect of the Pole

For $h'(t) = e^{-10t}u(t)$: $H'(j\omega) = \frac{1}{10 + j\omega}$, cutoff $\omega_c' = 10$ rad/s.

**Wider bandwidth** → both $\omega = 3$ and $\omega = 9$ now in passband → output more similar to input.

**General rule:** Increasing $a$ in $h(t) = e^{-at}u(t)$ moves the pole left, widens bandwidth, makes a "less aggressive" lowpass filter.
