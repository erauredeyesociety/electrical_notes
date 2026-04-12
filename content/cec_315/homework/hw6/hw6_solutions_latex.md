# CEC 315 HW6 Solutions — Z-Transform (Lectures 19-21)

---

## Problem 1: Computing Z-Transforms and ROCs

### (a) $x_1[n] = 5(0.7)^n u[n]$

Using the pair $a^n u[n] \leftrightarrow \frac{1}{1 - a z^{-1}}, \quad |z| > |a|$ with $a = 0.7$:

$$\boxed{X_1(z) = \frac{5}{1 - 0.7\,z^{-1}}, \quad \text{ROC: } |z| > 0.7}$$

### (b) $x_2[n] = -(4)^n u[-n-1]$

Using the pair $-a^n u[-n-1] \leftrightarrow \frac{1}{1 - a z^{-1}}, \quad |z| < |a|$ with $a = 4$:

$$\boxed{X_2(z) = \frac{1}{1 - 4\,z^{-1}}, \quad \text{ROC: } |z| < 4}$$

### (c) $x_3[n] = 3\,\delta[n] - 2\,\delta[n-1] + \delta[n-4]$

Using $\delta[n-k] \leftrightarrow z^{-k}$:

$$\boxed{X_3(z) = 3 - 2z^{-1} + z^{-4}, \quad \text{ROC: } |z| > 0}$$

### (d) $x_4[n] = n(0.5)^n u[n]$

Using the pair $n\,a^n u[n] \leftrightarrow \frac{a\,z^{-1}}{(1 - a\,z^{-1})^2}, \quad |z| > |a|$ with $a = 0.5$:

$$\boxed{X_4(z) = \frac{0.5\,z^{-1}}{(1 - 0.5\,z^{-1})^2}, \quad \text{ROC: } |z| > 0.5}$$

### (e) $x_5[n] = 2(0.3)^n u[n] + 4(0.9)^n u[n]$

Each term separately:

$$\frac{2}{1 - 0.3\,z^{-1}} + \frac{4}{1 - 0.9\,z^{-1}}$$

Combine over common denominator $(1 - 0.3z^{-1})(1 - 0.9z^{-1})$:

$$\text{Num} = 2(1 - 0.9z^{-1}) + 4(1 - 0.3z^{-1}) = 6 - 3z^{-1}$$

$$\boxed{X_5(z) = \frac{6 - 3z^{-1}}{(1 - 0.3z^{-1})(1 - 0.9z^{-1})}, \quad \text{ROC: } |z| > 0.9}$$

Poles: $z = 0.3,\; z = 0.9$. Zero: $6 - 3z^{-1} = 0 \Rightarrow z = 0.5$. Also a zero at $z = 0$.

### (f) $x_6[n] = (0.6)^n u[n] - 3(2)^n u[-n-1]$

First term: $\frac{1}{1 - 0.6z^{-1}},\; |z| > 0.6$. Second term: $-3(2)^n u[-n-1] \to \frac{3}{1 - 2z^{-1}},\; |z| < 2$.

$$X_6(z) = \frac{1}{1 - 0.6z^{-1}} + \frac{3}{1 - 2z^{-1}} = \frac{4 - 3.8z^{-1}}{(1 - 0.6z^{-1})(1 - 2z^{-1})}$$

$$\boxed{\text{ROC: } 0.6 < |z| < 2}$$

DTFT exists? Since $0.6 < 1 < 2$, the unit circle is in the ROC. **Yes, the DTFT exists.**

### (g) $x_7[n] = (0.8)^n \cos(0.25\pi\,n)\,u[n]$

Using $r^n \cos(\omega_0 n)\,u[n] \leftrightarrow \frac{1 - r\cos(\omega_0)\,z^{-1}}{1 - 2r\cos(\omega_0)\,z^{-1} + r^2 z^{-2}}$ with $r = 0.8$, $\omega_0 = 0.25\pi$:

$$\cos(0.25\pi) = \frac{\sqrt{2}}{2} \approx 0.7071, \quad r\cos\omega_0 = 0.5657, \quad r^2 = 0.64$$

$$\boxed{X_7(z) = \frac{1 - 0.5657\,z^{-1}}{1 - 1.1314\,z^{-1} + 0.64\,z^{-2}}, \quad \text{ROC: } |z| > 0.8}$$

Poles: $z = 0.8\,e^{\pm j\,0.25\pi}$ (polar form: $|z| = 0.8$, angle $= \pm 45°$).

Pole radius: $r = 0.8$. Oscillation frequency: $\omega_0 = 0.25\pi$ rad/sample.

DTFT exists? $|z| = 0.8 < 1$, so ROC includes unit circle. **Yes.**

### (h) Evaluate $X(z)$ at $z = 1$

At $z = 1$, $z^{-1} = 1$, so $X(1) = \sum_n x[n]$.

| Part | $X(1)$ | Verification |
|------|--------|-------------|
| (a) | $\frac{5}{1 - 0.7} = \frac{5}{0.3} = 16.667$ | $\sum 5(0.7)^n = 16.667$ ✓ |
| (b) | $\frac{1}{1-4} = -\frac{1}{3}$ | $-\sum_{m=1}^{\infty}(1/4)^m = -1/3$ ✓ |
| (c) | $3 - 2 + 1 = 2$ | Direct sum $= 2$ ✓ |
| (d) | $\frac{0.5}{(0.5)^2} = 2$ | $\sum n(0.5)^n = 2$ ✓ |
| (e) | $\frac{3}{0.07} = 42.857$ | $\frac{2}{0.7} + \frac{4}{0.1} = 42.857$ ✓ |
| (f) | $\frac{0.2}{-0.4} = -0.5$ | $2.5 + (-3) = -0.5$ ✓ |
| (g) | $\frac{0.4343}{0.5086} = 0.854$ | Matches ✓ |

---

## Problem 2: Inverse Z-Transform

### (a) Distinct real poles, causal

$$X(z) = \frac{1 + 3z^{-1}}{(1 - 0.2z^{-1})(1 - 0.6z^{-1})}, \quad |z| > 0.6$$

Partial fractions: $X(z) = \frac{A}{1 - 0.2z^{-1}} + \frac{B}{1 - 0.6z^{-1}}$

$$1 + 3z^{-1} = A(1 - 0.6z^{-1}) + B(1 - 0.2z^{-1})$$

Set $z^{-1} = 5$: $16 = -2A \Rightarrow A = -8$

Set $z^{-1} = 5/3$: $6 = \frac{2B}{3} \Rightarrow B = 9$

$$\boxed{x[n] = -8(0.2)^n u[n] + 9(0.6)^n u[n]}$$

### (b) Distinct real poles, two-sided

$$X(z) = \frac{4}{(1 - 0.5z^{-1})(1 - 3z^{-1})}, \quad 0.5 < |z| < 3$$

$A/(1 - 0.5z^{-1}) + B/(1 - 3z^{-1})$

Set $z^{-1} = 2$: $4 = -5A \Rightarrow A = -0.8$

Set $z^{-1} = 1/3$: $4 = \frac{5B}{6} \Rightarrow B = 4.8$

ROC $0.5 < |z| < 3$:
- Pole at $z=0.5$: ROC outside $\Rightarrow$ right-sided
- Pole at $z=3$: ROC inside $\Rightarrow$ left-sided (negative sign)

$$\boxed{x[n] = -0.8(0.5)^n u[n] - 4.8(3)^n u[-n-1]}$$

### (c) Repeated poles

$$X(z) = \frac{z^{-1}}{(1 - 0.5z^{-1})^2}, \quad |z| > 0.5$$

Using $n\,a^n u[n] \leftrightarrow \frac{az^{-1}}{(1 - az^{-1})^2}$ with $a = 0.5$:

$$X(z) = \frac{1}{0.5}\cdot\frac{0.5\,z^{-1}}{(1 - 0.5z^{-1})^2} = 2\cdot\frac{0.5\,z^{-1}}{(1 - 0.5z^{-1})^2}$$

$$\boxed{x[n] = 2\,n\,(0.5)^n u[n]}$$

### (d) Complex conjugate poles

$$X(z) = \frac{1 - 0.9\cos(0.3\pi)\,z^{-1}}{1 - 2(0.9)\cos(0.3\pi)\,z^{-1} + 0.81\,z^{-2}}, \quad |z| > 0.9$$

Matches the pair $r^n\cos(\omega_0 n)\,u[n]$ with $r = 0.9$, $\omega_0 = 0.3\pi$.

$$\boxed{x[n] = (0.9)^n \cos(0.3\pi\,n)\,u[n]}$$

Poles: $z = 0.9\,e^{\pm j\,0.3\pi}$ (magnitude $0.9$, angle $\pm 54°$).

---

## Problem 3: Z-Transform Properties

### (a) Time shifting

Given $x[n] = (0.8)^n u[n] \leftrightarrow \frac{1}{1 - 0.8z^{-1}}$. Then $y[n] = x[n-2] = (0.8)^{n-2}u[n-2]$.

$$\boxed{Y(z) = z^{-2}\cdot\frac{1}{1 - 0.8z^{-1}} = \frac{z^{-2}}{1 - 0.8z^{-1}}, \quad \text{ROC: } |z| > 0.8}$$

The factor $z^{-2}$ introduces **2 zeros at $z = 0$**.

### (b) Z-domain scaling

Given $u[n] \leftrightarrow \frac{1}{1 - z^{-1}},\; |z| > 1$. Using $z_0^n x[n] \leftrightarrow X(z/z_0)$ with $z_0 = 0.5$:

$$F(z) = X\!\left(\frac{z}{0.5}\right) = \frac{1}{1 - (z/0.5)^{-1}} = \frac{1}{1 - 0.5z^{-1}}, \quad \text{ROC: } |z| > 0.5$$

Matches the standard pair $a^n u[n]$ with $a = 0.5$. ✓

### (c) Convolution property

$h_1[n] = (0.3)^n u[n]$, $h_2[n] = (0.7)^n u[n]$

**(i)** $H_1(z) = \frac{1}{1 - 0.3z^{-1}}$, $H_2(z) = \frac{1}{1 - 0.7z^{-1}}$

**(ii)** $H(z) = \frac{1}{(1 - 0.3z^{-1})(1 - 0.7z^{-1})}, \quad |z| > 0.7$

**(iii)** Partial fractions: $1 = A(1 - 0.7z^{-1}) + B(1 - 0.3z^{-1})$

$z^{-1} = 10/3$: $A = -3/4$. $\quad z^{-1} = 10/7$: $B = 7/4$.

$$\boxed{h[n] = -\tfrac{3}{4}(0.3)^n u[n] + \tfrac{7}{4}(0.7)^n u[n]}$$

**(iv)** Verify:

$h[0] = -0.75 + 1.75 = 1.0$. Direct: $h_1[0]\cdot h_2[0] = 1$. ✓

$h[1] = -0.225 + 1.225 = 1.0$. Direct: $h_1[0]h_2[1] + h_1[1]h_2[0] = 0.7 + 0.3 = 1.0$. ✓

### (d) Initial-value theorem

$$X(z) = \frac{3 - z^{-1}}{(1 - 0.4z^{-1})(1 + 0.5z^{-1})}, \quad |z| > 0.5$$

**(i)** $x[0] = \lim_{z\to\infty} X(z) = \frac{3}{1\cdot 1} = 3$

**(ii)** Partial fractions: $3 - z^{-1} = A(1 + 0.5z^{-1}) + B(1 - 0.4z^{-1})$

$z^{-1} = 2.5$: $0.5 = 2.25A \Rightarrow A = \frac{2}{9}$

$z^{-1} = -2$: $5 = 1.8B \Rightarrow B = \frac{25}{9}$

$$x[n] = \tfrac{2}{9}(0.4)^n u[n] + \tfrac{25}{9}(-0.5)^n u[n]$$

Verify: $x[0] = \frac{2}{9} + \frac{25}{9} = \frac{27}{9} = 3$ ✓

**(iii)** $x[1] = \frac{2}{9}(0.4) + \frac{25}{9}(-0.5) = \frac{0.8 - 12.5}{9} = -1.3$

$x[2] = \frac{2}{9}(0.16) + \frac{25}{9}(0.25) = \frac{0.32 + 6.25}{9} = 0.730$

---

## Problem 4: System Analysis with $H(z)$

### Given: $y[n] - 0.9\,y[n-1] + 0.18\,y[n-2] = x[n]$

### (a) System function

$$Y(z)\bigl(1 - 0.9z^{-1} + 0.18z^{-2}\bigr) = X(z)$$

$$\boxed{H(z) = \frac{1}{(1 - 0.3z^{-1})(1 - 0.6z^{-1})}, \quad \text{ROC: } |z| > 0.6}$$

Poles: $z = 0.3$ and $z = 0.6$. No finite zeros.

### (b) BIBO stability

Both poles satisfy $|p_i| < 1$ (inside unit circle). **System is BIBO stable.** ✓

### (c) Impulse response

$1 = A(1 - 0.6z^{-1}) + B(1 - 0.3z^{-1})$

$z^{-1} = 10/3$: $A = -1$. $\quad z^{-1} = 5/3$: $B = 2$.

$$\boxed{h[n] = -(0.3)^n u[n] + 2(0.6)^n u[n]}$$

Check: $h[0] = -1 + 2 = 1 = \delta[0]$ ✓

### (d) Input $x[n] = (0.5)^n u[n]$

**(i)** $Y(z) = \frac{1}{(1 - 0.3z^{-1})(1 - 0.6z^{-1})(1 - 0.5z^{-1})}$

**(ii)** $1 = A(1-0.6z^{-1})(1-0.5z^{-1}) + B(1-0.3z^{-1})(1-0.5z^{-1}) + C(1-0.3z^{-1})(1-0.6z^{-1})$

$z^{-1}=10/3$: $A = 3/2$. $\quad z^{-1}=5/3$: $B = 12$. $\quad z^{-1}=2$: $C = -12.5$.

$$\boxed{y[n] = 1.5(0.3)^n u[n] + 12(0.6)^n u[n] - 12.5(0.5)^n u[n]}$$

**(iii)** $y[0] = 1.5 + 12 - 12.5 = 1.0$. Diff eq: $y[0] = x[0] = 1$. ✓

$y[1] = 0.45 + 7.2 - 6.25 = 1.4$. Diff eq: $y[1] = 0.9(1) + 0.5 = 1.4$. ✓

### (e) $G(z) = \frac{1}{1 - 1.5z^{-1}}$, pole at $z = 1.5$

**Causal** (ROC: $|z| > 1.5$): $g[n] = (1.5)^n u[n]$. Pole outside unit circle $\Rightarrow$ **NOT BIBO stable**. DTFT does not exist.

**Anti-causal** (ROC: $|z| < 1.5$): $g[n] = -(1.5)^n u[-n-1]$. Unit circle $|z|=1$ is inside ROC $\Rightarrow$ **BIBO stable**. DTFT exists.

---

## Problem 5: Unilateral Z-Transform

### (a) First-order with IC

$$y[n] - 0.8\,y[n-1] = (0.5)^n u[n], \quad y[-1] = 3$$

**(i)** Using $\mathcal{Z}_u\{y[n-1]\} = z^{-1}Y(z) + y[-1]$:

$$Y(z) - 0.8\bigl(z^{-1}Y(z) + 3\bigr) = \frac{1}{1 - 0.5z^{-1}}$$

$$Y(z)(1 - 0.8z^{-1}) = \frac{1}{1 - 0.5z^{-1}} + 2.4$$

**(ii)** Combine:

$$Y(z) = \frac{3.4 - 1.2z^{-1}}{(1 - 0.5z^{-1})(1 - 0.8z^{-1})}$$

**(iii)** $3.4 - 1.2z^{-1} = A(1 - 0.8z^{-1}) + B(1 - 0.5z^{-1})$

$z^{-1} = 2$: $A = -5/3$. $\quad z^{-1} = 1.25$: $B = 76/15$.

$$\boxed{y[n] = -\tfrac{5}{3}(0.5)^n u[n] + \tfrac{76}{15}(0.8)^n u[n]}$$

**(iv)** $y[0] = -25/15 + 76/15 = 51/15 = 3.4$. Diff eq: $0.8(3) + 1 = 3.4$. ✓

$y[1] = -0.833 + 4.053 = 3.22$. Diff eq: $0.8(3.4) + 0.5 = 3.22$. ✓

### (b) Second-order, zero-input

$$y[n] - 0.5\,y[n-1] - 0.06\,y[n-2] = 0, \quad y[-1] = 5,\; y[-2] = 0$$

**(i)** $Y(z)(1 - 0.5z^{-1} - 0.06z^{-2}) = 2.5 + 0.3z^{-1}$

**(ii)** Factor: $(1 - 0.6z^{-1})(1 + 0.1z^{-1})$

$2.5 + 0.3z^{-1} = A(1 + 0.1z^{-1}) + B(1 - 0.6z^{-1})$

$z^{-1} = 5/3$: $A = 18/7$. $\quad z^{-1} = -10$: $B = -1/14$.

$$\boxed{y[n] = \tfrac{18}{7}(0.6)^n u[n] - \tfrac{1}{14}(-0.1)^n u[n]}$$

**(iii)** This is the **zero-input response (ZIR)** — input is zero, response comes entirely from initial conditions.

### (c) ZSR/ZIR decomposition for part (a)

**ZSR** (ICs = 0): $Y_{ZS}(z) = \frac{1}{(1 - 0.5z^{-1})(1 - 0.8z^{-1})}$

$$y_{ZS}[n] = -\tfrac{5}{3}(0.5)^n u[n] + \tfrac{8}{3}(0.8)^n u[n]$$

**ZIR** (input = 0): $Y_{ZI}(z) = \frac{2.4}{1 - 0.8z^{-1}}$

$$y_{ZI}[n] = 2.4(0.8)^n u[n]$$

**Verify:**

$$y_{ZS} + y_{ZI} = -\tfrac{5}{3}(0.5)^n u[n] + \left(\tfrac{8}{3} + 2.4\right)(0.8)^n u[n] = -\tfrac{5}{3}(0.5)^n u[n] + \tfrac{76}{15}(0.8)^n u[n]$$

Matches total $y[n]$ from part (a). ✓
