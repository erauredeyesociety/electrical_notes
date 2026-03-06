# Problem 4: Discrete-Time Fourier Series

## Setup

**Given:** $x[n]$ periodic with $N = 6$, $x[n] = 1$ for $n = 0,1,2$ and $x[n] = 0$ for $n = 3,4,5$.

## Part (a): DTFS Fundamentals

**DTFS Pair:**

$$a_k = \frac{1}{N} \sum_{n=\langle N \rangle} x[n] \, e^{-jk(2\pi/N)n} \qquad x[n] = \sum_{k=\langle N \rangle} a_k \, e^{jk(2\pi/N)n}$$

Key difference from CT: Only **N distinct** coefficients because $e^{j(k+N)(2\pi/N)n} = e^{jk(2\pi/N)n}$. No convergence issues (finite sum).

## Part (b): Computing Coefficients

$\omega_0 = 2\pi/6 = \pi/3$. Only $n = 0, 1, 2$ contribute (where $x[n] = 1$):

$$a_k = \frac{1}{6}(1 + e^{-jk\pi/3} + e^{-j2k\pi/3})$$

**$k=0$:** $a_0 = \frac{1}{6}(1+1+1) = \frac{1}{2}$

**$k=1$:** $e^{-j\pi/3} = \frac{1}{2} - j\frac{\sqrt{3}}{2}$, $\;e^{-j2\pi/3} = -\frac{1}{2} - j\frac{\sqrt{3}}{2}$

Sum: $1 - j\sqrt{3}$, so $a_1 = \frac{1-j\sqrt{3}}{6}$, $|a_1| = \frac{1}{3}$, $\angle a_1 = -60°$

**$k=2$:** Sum = $1 + (-\frac{1}{2} - j\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + j\frac{\sqrt{3}}{2}) = 0$

$a_2 = 0$

**$k=3$:** $e^{-j\pi} = -1$, $e^{-j2\pi} = 1$. Sum = $1 + (-1) + 1 = 1$

$a_3 = \frac{1}{6}$, $|a_3| = \frac{1}{6}$, $\angle a_3 = 0°$

## Part (c): Periodicity of Coefficients

Since $a_{k+N} = a_k$ with $N = 6$:

$$a_4 = a_{-2} = a_2^* = 0$$

$$a_5 = a_{-1} = a_1^* = \frac{1+j\sqrt{3}}{6}, \quad |a_5| = \frac{1}{3}$$

**Why periodic?** Because $e^{j(k+N)(2\pi/N)n} = e^{jk(2\pi/N)n} \cdot e^{j2\pi n} = e^{jk(2\pi/N)n}$ for integer $n$.

## Part (d): Parseval's Verification

**Time domain:**
$$\frac{1}{N}\sum_{n=0}^{5} |x[n]|^2 = \frac{1}{6}(1+1+1+0+0+0) = \frac{1}{2}$$

**Frequency domain:**
$$\sum_{k=0}^{5} |a_k|^2 = \frac{1}{4} + \frac{1}{9} + 0 + \frac{1}{36} + 0 + \frac{1}{9} = \frac{9+4+1+4}{36} = \frac{18}{36} = \frac{1}{2} \quad ✓$$
