# Problem 1: Eigenfunction Property & CT Fourier Series Coefficients

## Part (a): Eigenfunction Property

**Given:** $h(t) = e^{-4t}u(t)$, input $x(t) = \cos(3t)$

### Step 1: Compute $H(j3)$

Since $h(t)$ is causal (lower limit is 0):

$$H(j3) = \int_0^{\infty} e^{-4\tau} e^{-j3\tau} d\tau = \int_0^{\infty} e^{-(4+j3)\tau} d\tau = \frac{1}{4+j3}$$

### Step 2: Rectangular form

Multiply by conjugate $(4-j3)/(4-j3)$:

$$H(j3) = \frac{4-j3}{16+9} = \frac{4}{25} - j\frac{3}{25}$$

### Step 3: Polar form

$$|H(j3)| = \frac{1}{\sqrt{4^2+3^2}} = \frac{1}{5} = 0.2$$

$$\angle H(j3) = -\arctan(3/4) = -36.87°$$

### Step 4: Output

By eigenfunction property, $\cos(3t)$ exits as the same cosine, scaled and phase-shifted:

$$\boxed{y(t) = 0.2\cos(3t - 36.87°)}$$

**Key point:** Frequency did NOT change. Only amplitude (scaled to 0.2) and phase (shifted by -36.87°).

---

## Part (b): Fourier Series Coefficients

**Given:** $x(t)$ periodic with $T=4$, $x(t) = 3$ for $0 \leq t < 1$, $x(t) = 0$ for $1 \leq t < 4$.

### Fundamental frequency

$$\omega_0 = \frac{2\pi}{T} = \frac{\pi}{2} \text{ rad/s}$$

### DC coefficient

$$a_0 = \frac{1}{4}\int_0^1 3\,dt = \frac{3}{4} = 0.75$$

### General $a_k$ ($k \neq 0$)

$$a_k = \frac{1}{4}\int_0^1 3\,e^{-jk(\pi/2)t}\,dt = \frac{3}{4}\left[\frac{e^{-jk(\pi/2)t}}{-jk\pi/2}\right]_0^1 = \frac{3}{2jk\pi}(1-e^{-jk\pi/2})$$

### Numerical values

**$k=1$:** $e^{-j\pi/2} = -j$, so $a_1 = \frac{3(1+j)}{2j\pi} \cdot \frac{-j}{-j} = \frac{3(1-j)}{2\pi}$
- $|a_1| = \frac{3\sqrt{2}}{2\pi} \approx 0.675$, $\angle a_1 = -45°$

**$k=2$:** $e^{-j\pi} = -1$, so $a_2 = \frac{3 \cdot 2}{4j\pi} = \frac{-3j}{2\pi}$
- $|a_2| = \frac{3}{2\pi} \approx 0.477$, $\angle a_2 = -90°$

### Part (c): Conjugate Symmetry Verification

Computed $a_{-1} = \frac{3(1+j)}{2\pi}$ and $a_1^* = \left(\frac{3(1-j)}{2\pi}\right)^* = \frac{3(1+j)}{2\pi}$

$a_{-1} = a_1^*$ confirmed. This holds for **any real-valued signal**.
