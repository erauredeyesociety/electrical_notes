# CEC 315 HW6 — Official Solutions — Z-Transform (Lectures 19-21)

**Course:** CEC 315 — Signals and Systems
**Semester:** Spring 2026
**Instructor:** Rogelio Gracia Otalvaro
**Topic:** The z-Transform: Definition, Inversion, Properties, and System Analysis

> This document is the **official instructor solution set**, faithfully transcribed from `hw_practice_problems/hw-lctr19-21-solutions.pdf` (12 pages). It is provided alongside the earlier student-made file `hw6_solutions.md` for side-by-side comparison. Final answers are boxed; Regions of Convergence (ROC) are explicitly stated for every z-transform.

**Useful pairs used throughout:**

$$a^{n}u[n] \;\zt\; \dfrac{1}{1-az^{-1}}, \quad \text{ROC: } |z|>|a|.$$

$$-a^{n}u[-n-1] \;\zt\; \dfrac{1}{1-az^{-1}}, \quad \text{ROC: } |z|<|a|.$$

$$n\,a^{n}u[n] \;\zt\; \dfrac{az^{-1}}{(1-az^{-1})^{2}}, \quad \text{ROC: } |z|>|a|.$$

$$\delta[n-k] \;\zt\; z^{-k}.$$

$$r^{n}\cos(\omega_0 n)\,u[n] \;\zt\; \dfrac{1-r\cos\omega_0\,z^{-1}}{1-2r\cos\omega_0\,z^{-1}+r^{2}z^{-2}}, \quad \text{ROC: } |z|>r.$$

(We write $\zt$ for $\xleftrightarrow{\mathcal{Z}}$.)

---

## Problem 1: Computing z-Transforms and ROCs

### Part (a): $x_1[n] = 5\,(0.7)^{n}\,u[n]$

Using the pair $a^{n}u[n]\zt\dfrac{1}{1-az^{-1}}$ with $a=0.7$:

$$\boxed{\,X_1(z)=\dfrac{5}{1-0.7\,z^{-1}}, \qquad |z|>0.7\,}$$

Pole at $z=0.7$.

**Check at $z=1$:** $X_1(1)=\dfrac{5}{1-0.7}=\dfrac{5}{0.3}=\dfrac{50}{3}$.

---

### Part (b): $x_2[n] = -(4)^{n}\,u[-n-1]$

Using the pair $-a^{n}u[-n-1]\zt\dfrac{1}{1-az^{-1}}$ with $a=4$, ROC $|z|<|a|$:

$$\boxed{\,X_2(z)=\dfrac{1}{1-4\,z^{-1}}, \qquad |z|<4\,}$$

Pole at $z=4$.

**Check at $z=1$:** $X_2(1)=\dfrac{1}{1-4}=-\dfrac{1}{3}$.

**Direct verification:**
$$\sum_{n=-\infty}^{-1}-(4)^{n}=-\sum_{m=1}^{\infty}4^{-m}=-\dfrac{1/4}{1-1/4}=-\dfrac{1}{3}. \; \checkmark$$

---

### Part (c): $x_3[n] = 3\,\delta[n] - 2\,\delta[n-1] + \delta[n-4]$

Using $\delta[n-k]\zt z^{-k}$:

$$\boxed{\,X_3(z)=3-2\,z^{-1}+z^{-4}, \qquad |z|>0\,}$$

This is a finite-duration sequence (polynomial in $z^{-1}$). ROC is all $z\neq 0$.

**Check at $z=1$:** $X_3(1)=3-2+1=2=3-2+0+0+1$. $\checkmark$

---

### Part (d): $x_4[n] = n\,(0.5)^{n}\,u[n]$

Using $n\,a^{n}u[n]\zt\dfrac{az^{-1}}{(1-az^{-1})^{2}}$ with $a=0.5$:

$$\boxed{\,X_4(z)=\dfrac{0.5\,z^{-1}}{(1-0.5\,z^{-1})^{2}}, \qquad |z|>0.5\,}$$

Double pole at $z=0.5$, zero at $z=0$.

**Check at $z=1$:** $X_4(1)=\dfrac{0.5}{(0.5)^{2}}=\dfrac{0.5}{0.25}=2$.

**Direct:** $\sum_{n=0}^{\infty}n(0.5)^{n}=\dfrac{0.5}{(1-0.5)^{2}}=2$. $\checkmark$

---

### Part (e): $x_5[n] = 2\,(0.3)^{n}\,u[n] + 4\,(0.9)^{n}\,u[n]$

**Step 1 — transform each term:**

$$\dfrac{2}{1-0.3\,z^{-1}},\;|z|>0.3 \qquad\text{and}\qquad \dfrac{4}{1-0.9\,z^{-1}},\;|z|>0.9.$$

**Step 2 — common denominator:**

$$X_5(z)=\dfrac{2(1-0.9\,z^{-1})+4(1-0.3\,z^{-1})}{(1-0.3\,z^{-1})(1-0.9\,z^{-1})}=\dfrac{6-3.0\,z^{-1}}{(1-0.3\,z^{-1})(1-0.9\,z^{-1})}.$$

ROC: $|z|>0.3 \cap |z|>0.9 = |z|>0.9$.

$$\boxed{\,X_5(z)=\dfrac{6-3\,z^{-1}}{(1-0.3\,z^{-1})(1-0.9\,z^{-1})}, \qquad |z|>0.9\,}$$

**Poles:** $z=0.3$ and $z=0.9$. **Zero:** $6-3z^{-1}=0 \Rightarrow z=0.5$.

**Check at $z=1$:** $X_5(1)=\dfrac{6-3}{(0.7)(0.1)}=\dfrac{3}{0.07}=\dfrac{300}{7}\approx 42.86$.

**Direct:** $\dfrac{2}{0.7}+\dfrac{4}{0.1}=\dfrac{20}{7}+40=\dfrac{300}{7}$. $\checkmark$

---

### Part (f): $x_6[n] = (0.6)^{n}\,u[n] - 3\,(2)^{n}\,u[-n-1]$

**Step 1 — transform each term separately:**

- $(0.6)^{n}u[n]\zt\dfrac{1}{1-0.6\,z^{-1}},\;|z|>0.6$.
- For the second term, write $-3(2)^{n}u[-n-1]=3\bigl[-(2)^{n}u[-n-1]\bigr]$. Since $-(2)^{n}u[-n-1]\zt\dfrac{1}{1-2z^{-1}}$ with ROC $|z|<2$, we get $\dfrac{3}{1-2\,z^{-1}},\;|z|<2$.

**Step 2 — combine:**

$$X_6(z)=\dfrac{1}{1-0.6\,z^{-1}}+\dfrac{3}{1-2\,z^{-1}}.$$

ROC: $|z|>0.6 \cap |z|<2 = \{z:0.6<|z|<2\}$ — an **annulus**.

$$\boxed{\,X_6(z)=\dfrac{1}{1-0.6\,z^{-1}}+\dfrac{3}{1-2\,z^{-1}}, \qquad 0.6<|z|<2\,}$$

**DTFT existence:** The unit circle $|z|=1$ satisfies $0.6<1<2$, so it lies inside the ROC. Therefore the **DTFT exists**. $\checkmark$

---

### Part (g): $x_7[n] = (0.8)^{n}\cos(0.25\pi n)\,u[n]$

Apply the table pair with $r=0.8$ and $\omega_0=0.25\pi$:

$$r\cos\omega_0=0.8\cdot\tfrac{\sqrt{2}}{2}\approx 0.5657, \quad 2r\cos\omega_0\approx 1.1314, \quad r^{2}=0.64.$$

$$\boxed{\,X_7(z)=\dfrac{1-0.5657\,z^{-1}}{1-1.1314\,z^{-1}+0.64\,z^{-2}}, \qquad |z|>0.8\,}$$

**Poles** (complex conjugate pair): $z = 0.8\,e^{\pm j0.25\pi}$ — i.e. magnitude $r=0.8$, angle $\pm 45^{\circ}$.

**Pole radius:** $r=0.8$.
**Oscillation frequency:** $\omega_0=0.25\pi$ rad/sample.

**DTFT existence:** All poles have $|z|=0.8<1$, so the ROC $|z|>0.8$ contains the unit circle. **DTFT exists.** $\checkmark$

---

### Part (h): Sanity checks at $z=1$

All checks were performed inline above. The rule $X(1)=\sum_{n}x[n]$ holds because $z^{-n}\big|_{z=1}=1$ for all $n$.

| Signal | $X(1)$ | $\sum x[n]$ | match |
|--------|--------|-------------|-------|
| (a) | $50/3\approx 16.67$ | $50/3$ | $\checkmark$ |
| (b) | $-1/3$ | $-1/3$ | $\checkmark$ |
| (c) | $2$ | $2$ | $\checkmark$ |
| (d) | $2$ | $2$ | $\checkmark$ |
| (e) | $300/7\approx 42.86$ | $300/7$ | $\checkmark$ |
| (f) | $\dfrac{1}{0.4}+\dfrac{3}{-1}=2.5-3=-0.5$ | $-0.5$ | $\checkmark$ |
| (g) | $\dfrac{1-0.5657}{1-1.1314+0.64}\approx 0.854$ | $\approx 0.854$ | $\checkmark$ |

---

## Problem 2: Inverse z-Transform via Partial Fractions

### Part (a): Distinct real poles, causal

Given: $X(z)=\dfrac{1+3z^{-1}}{(1-0.2z^{-1})(1-0.6z^{-1})}$, ROC $|z|>0.6$.

**Step 1 — partial fractions:**

$$\dfrac{1+3z^{-1}}{(1-0.2z^{-1})(1-0.6z^{-1})}=\dfrac{A}{1-0.2z^{-1}}+\dfrac{B}{1-0.6z^{-1}}.$$

- Set $z^{-1}=1/0.2=5$: $1+15=A(1-3)\Rightarrow 16=-2A \Rightarrow A=-8$.
- Set $z^{-1}=1/0.6=5/3$: $1+5=B(1-1/3) \Rightarrow 6=(2/3)B \Rightarrow B=9$.

**Step 2 — directions from ROC:** Poles at $|z|=0.2$ and $|z|=0.6$. The ROC $|z|>0.6$ lies outside both pole circles, so both terms are **right-sided**.

**Step 3 — invert:**

$$\boxed{\,x[n]=\bigl[-8\,(0.2)^{n}+9\,(0.6)^{n}\bigr]\,u[n]\,}$$

**Check:** $x[0]=-8+9=1$. Initial-value theorem: $\lim_{z\to\infty}X(z)=\dfrac{1}{1}=1$. $\checkmark$

---

### Part (b): Two-sided signal (annular ROC)

Given: $X(z)=\dfrac{4}{(1-0.5z^{-1})(1-3z^{-1})}$, ROC $0.5<|z|<3$.

**Step 1 — partial fractions:**

$$\dfrac{4}{(1-0.5z^{-1})(1-3z^{-1})}=\dfrac{A}{1-0.5z^{-1}}+\dfrac{B}{1-3z^{-1}}.$$

- Set $z^{-1}=2$: $4=A(1-6)=-5A\Rightarrow A=-\dfrac{4}{5}$.
- Set $z^{-1}=1/3$: $4=B(1-1/6)=(5/6)B\Rightarrow B=\dfrac{24}{5}$.

**Step 2 — assign directions from the annular ROC $0.5<|z|<3$:**

- Pole at $z=0.5$: ROC is **outside** this pole $\Rightarrow$ right-sided.
- Pole at $z=3$: ROC is **inside** this pole $\Rightarrow$ left-sided.

**Step 3 — invert:**

- $\dfrac{-4/5}{1-0.5z^{-1}}$ (right-sided) $\longrightarrow -\dfrac{4}{5}(0.5)^{n}u[n]$.
- $\dfrac{24/5}{1-3z^{-1}}$ (left-sided) $\longrightarrow -\dfrac{24}{5}(3)^{n}u[-n-1]$.

$$\boxed{\,x[n]=-\dfrac{4}{5}\,(0.5)^{n}\,u[n]-\dfrac{24}{5}\,(3)^{n}\,u[-n-1]\,}$$

**Key point.** The left-sided inversion uses $\dfrac{B}{1-az^{-1}}$ with ROC $|z|<|a|$ inverting to $-B\,a^{n}u[-n-1]$. The negative sign is *part of the pair itself*, so $B=24/5$ produces $-(24/5)(3)^{n}u[-n-1]$.

---

### Part (c): Repeated poles

Given: $X(z)=\dfrac{z^{-1}}{(1-0.5z^{-1})^{2}}$, ROC $|z|>0.5$.

Using $n\,a^{n}u[n]\zt\dfrac{az^{-1}}{(1-az^{-1})^{2}}$ with $a=0.5$, we rewrite:

$$X(z)=\dfrac{z^{-1}}{(1-0.5z^{-1})^{2}}=\dfrac{1}{0.5}\cdot\dfrac{0.5\,z^{-1}}{(1-0.5z^{-1})^{2}}=2\cdot\dfrac{0.5\,z^{-1}}{(1-0.5z^{-1})^{2}}.$$

$$\boxed{\,x[n]=2\,n\,(0.5)^{n}\,u[n]\,}$$

**Check:** $x[0]=0$, $x[1]=2(1)(0.5)=1$, $x[2]=2(2)(0.25)=1$. Initial-value theorem gives $\lim_{z\to\infty}X(z)=0$, consistent with $x[0]=0$. $\checkmark$

---

### Part (d): Complex conjugate poles

Given: $X(z)=\dfrac{1-0.9\cos(0.3\pi)\,z^{-1}}{1-2(0.9)\cos(0.3\pi)\,z^{-1}+0.81\,z^{-2}}$, ROC $|z|>0.9$.

Comparing with the standard pair
$$\dfrac{1-r\cos\omega_0\,z^{-1}}{1-2r\cos\omega_0\,z^{-1}+r^{2}z^{-2}}\;\zt\;r^{n}\cos(\omega_0 n)\,u[n],$$
we identify $r=0.9$, $\omega_0=0.3\pi$, $r^{2}=0.81$. $\checkmark$

Poles at $z=0.9\,e^{\pm j0.3\pi}$, both with $|z|=0.9<1$.

$$\boxed{\,x[n]=(0.9)^{n}\cos(0.3\pi n)\,u[n]\,}$$

This is a damped discrete-time sinusoid: the $(0.9)^{n}$ envelope decays because $r<1$, and the oscillation frequency is $\omega_0=0.3\pi$ rad/sample.

---

## Problem 3: z-Transform Properties

### Part (a): Time shifting

Given: $(0.8)^{n}u[n]\zt\dfrac{1}{1-0.8z^{-1}},\;|z|>0.8$. By the time-shift property $x[n-2]\zt z^{-2}X(z)$:

$$\boxed{\,Y(z)=\dfrac{z^{-2}}{1-0.8\,z^{-1}}, \qquad |z|>0.8\,}$$

**Zeros at $z=0$:** Writing $Y(z)=\dfrac{z^{-2}}{1-0.8z^{-1}}=\dfrac{1}{z^{2}-0.8z}=\dfrac{1}{z(z-0.8)}$, there is one pole at $z=0.8$ and one pole at $z=0$ (after accounting for cancellation). In the $z^{-1}$ form, the numerator $z^{-2}$ contributes **2 zeros at $z=0$**; one is cancelled by a pole introduced at $z=0$ from the shift, leaving, in the $z$-form, zeros at $z=\infty$ (two of them, since the numerator degree is less than the denominator degree by 2).

---

### Part (b): z-domain scaling

Given: $u[n]\zt\dfrac{1}{1-z^{-1}},\;|z|>1$.

Scaling property: $z_0^{n}x[n]\zt X(z/z_0)$. Set $z_0=0.5$:

$$(0.5)^{n}u[n]\;\zt\;\dfrac{1}{1-(z/0.5)^{-1}}=\dfrac{1}{1-0.5\,z^{-1}}.$$

ROC: $|z/0.5|>1\Rightarrow |z|>0.5$.

$$\boxed{\,(0.5)^{n}u[n]\;\zt\;\dfrac{1}{1-0.5\,z^{-1}}, \qquad |z|>0.5\,}$$

Matches the standard pair with $a=0.5$. $\checkmark$

---

### Part (c): Convolution property

$h_1[n]=(0.3)^{n}u[n]$, $h_2[n]=(0.7)^{n}u[n]$.

**(i)** $H_1(z)=\dfrac{1}{1-0.3z^{-1}},\;|z|>0.3$. $H_2(z)=\dfrac{1}{1-0.7z^{-1}},\;|z|>0.7$.

**(ii)** $H(z)=H_1(z)H_2(z)=\dfrac{1}{(1-0.3z^{-1})(1-0.7z^{-1})},\;|z|>0.7$.

**(iii) Partial fractions:**

$$\dfrac{1}{(1-0.3z^{-1})(1-0.7z^{-1})}=\dfrac{A}{1-0.3z^{-1}}+\dfrac{B}{1-0.7z^{-1}}.$$

- Set $z^{-1}=10/3$: $1=A(1-7/3)=A(-4/3)\Rightarrow A=-3/4$.
- Set $z^{-1}=10/7$: $1=B(1-3/7)=B(4/7)\Rightarrow B=7/4$.

$$\boxed{\,h[n]=\Bigl[-\dfrac{3}{4}(0.3)^{n}+\dfrac{7}{4}(0.7)^{n}\Bigr]\,u[n]\,}$$

**(iv) Direct-convolution check:**

- $h[0]=h_1[0]h_2[0]=1\cdot 1=1$. From formula: $-3/4+7/4=4/4=1$. $\checkmark$
- $h[1]=h_1[0]h_2[1]+h_1[1]h_2[0]=1\cdot 0.7+0.3\cdot 1=1.0$. From formula: $-0.75(0.3)+1.75(0.7)=-0.225+1.225=1.0$. $\checkmark$

---

### Part (d): Initial-value theorem and full inversion

Given: $X(z)=\dfrac{3-z^{-1}}{(1-0.4z^{-1})(1+0.5z^{-1})}$, $|z|>0.5$.

**(i) Initial value:** $x[0]=\lim_{z\to\infty}X(z)=\dfrac{3-0}{(1-0)(1+0)}=3$.

$$\boxed{\,x[0]=3\,}$$

**(ii) Partial fractions.** Poles at $z=0.4$ and $z=-0.5$.

$$\dfrac{3-z^{-1}}{(1-0.4z^{-1})(1+0.5z^{-1})}=\dfrac{A}{1-0.4z^{-1}}+\dfrac{B}{1+0.5z^{-1}}.$$

- Set $z^{-1}=1/0.4=2.5$: $3-2.5=A(1+1.25)=2.25A\Rightarrow A=0.5/2.25=2/9$.
- Set $z^{-1}=-1/0.5=-2$: $3+2=B(1+0.8)=1.8B\Rightarrow B=5/1.8=25/9$.

$$x[n]=\dfrac{2}{9}(0.4)^{n}u[n]+\dfrac{25}{9}(-0.5)^{n}u[n].$$

Check: $x[0]=2/9+25/9=27/9=3$. $\checkmark$

**(iii)** $x[1]=\dfrac{2}{9}(0.4)+\dfrac{25}{9}(-0.5)=\dfrac{0.8}{9}-\dfrac{12.5}{9}=\dfrac{-11.7}{9}=-1.3$.

$x[2]=\dfrac{2}{9}(0.16)+\dfrac{25}{9}(0.25)=\dfrac{0.32+6.25}{9}=\dfrac{6.57}{9}\approx 0.73$.

---

## Problem 4: System Analysis with $H(z)$

System: $y[n]-0.9\,y[n-1]+0.18\,y[n-2]=x[n]$.

### Part (a): System function

Replacing delays with $z^{-k}$:

$$(1-0.9z^{-1}+0.18z^{-2})Y(z)=X(z).$$

Factor $z^{2}-0.9z+0.18=0 \Rightarrow z=\dfrac{0.9\pm\sqrt{0.81-0.72}}{2}=\dfrac{0.9\pm 0.3}{2}$, giving poles at $z=0.6$ and $z=0.3$. No finite zeros (numerator is 1).

$$\boxed{\,H(z)=\dfrac{1}{(1-0.6z^{-1})(1-0.3z^{-1})}, \qquad |z|>0.6 \text{ (causal)}\,}$$

### Part (b): Stability

Both poles satisfy $|0.6|<1$ and $|0.3|<1$. Since the system is causal with all poles strictly inside the unit circle, it is **BIBO stable.** $\checkmark$

### Part (c): Impulse response

$$\dfrac{1}{(1-0.6z^{-1})(1-0.3z^{-1})}=\dfrac{A}{1-0.6z^{-1}}+\dfrac{B}{1-0.3z^{-1}}.$$

- Set $z^{-1}=5/3$: $1=A(1-0.5)=0.5A\Rightarrow A=2$.
- Set $z^{-1}=10/3$: $1=B(1-2)=-B\Rightarrow B=-1$.

$$\boxed{\,h[n]=\bigl[2(0.6)^{n}-(0.3)^{n}\bigr]\,u[n]\,}$$

Check: $h[0]=2-1=1$ $\checkmark$ (coefficient of $x[n]$ in the ODE is 1).

### Part (d): Output for input $(0.5)^{n}u[n]$

**(i)** $X(z)=\dfrac{1}{1-0.5z^{-1}},\;|z|>0.5$. Then

$$Y(z)=\dfrac{1}{(1-0.6z^{-1})(1-0.3z^{-1})(1-0.5z^{-1})},\quad |z|>0.6.$$

**(ii) Partial fractions:**

$$\dfrac{1}{(1-0.6z^{-1})(1-0.3z^{-1})(1-0.5z^{-1})}=\dfrac{A}{1-0.6z^{-1}}+\dfrac{B}{1-0.3z^{-1}}+\dfrac{C}{1-0.5z^{-1}}.$$

- Set $z^{-1}=5/3$: $1=A(1-0.5)(1-5/6)=A(0.5)(1/6)=A/12 \Rightarrow A=12$.
- Set $z^{-1}=10/3$: $1=B(1-2)(1-5/3)=B(-1)(-2/3)=2B/3\Rightarrow B=3/2$.
- Set $z^{-1}=2$: $1=C(1-1.2)(1-0.6)=C(-0.2)(0.4)=-0.08C\Rightarrow C=-12.5$.

Check: $A+B+C=12+1.5-12.5=1=Y(\infty)=y[0]$. From ODE with zero ICs, $y[0]=x[0]=1$. $\checkmark$

$$\boxed{\,y[n]=\bigl[12\,(0.6)^{n}+1.5\,(0.3)^{n}-12.5\,(0.5)^{n}\bigr]\,u[n]\,}$$

**(iii) Verify:**

- $y[0]=12+1.5-12.5=1$. From ODE: $y[0]=0.9\cdot 0-0.18\cdot 0+x[0]=1$. $\checkmark$
- $y[1]=12(0.6)+1.5(0.3)-12.5(0.5)=7.2+0.45-6.25=1.4$. From ODE: $y[1]=0.9\,y[0]-0.18\cdot 0+x[1]=0.9(1)+0.5=1.4$. $\checkmark$

### Part (e): Stability of $G(z)=\dfrac{1}{1-1.5z^{-1}}$

Pole at $z=1.5$, **outside** the unit circle ($|1.5|>1$).

- **If causal:** ROC is $|z|>1.5$. The unit circle $|z|=1$ is *not* in the ROC. System is **unstable**. Impulse response $g[n]=(1.5)^{n}u[n]$ grows without bound. **DTFT does not exist.**
- **If anti-causal (left-sided):** ROC is $|z|<1.5$. The unit circle *is* in the ROC. System is **BIBO stable**. Impulse response $g[n]=-(1.5)^{n}u[-n-1]$ decays as $n\to-\infty$. **DTFT exists.**

**Key Point.** This parallels the Laplace result from Problem 4(e) of the Lectures 16-18 homework: a pole outside the unit circle makes a causal system unstable but is compatible with a stable anti-causal system. The ROC determines stability, not the pole location alone.

---

## Problem 5: The Unilateral z-Transform

### Part (a): First-Order with IC

System: $y[n]-0.8\,y[n-1]=(0.5)^{n}u[n]$, $y[-1]=3$.

**(i) Unilateral z-transform.** Using $\mathcal{Z}_u\{y[n-1]\}=z^{-1}Y(z)+y[-1]$:

Left side: $Y(z)-0.8\bigl[z^{-1}Y(z)+y[-1]\bigr]=Y(z)-0.8z^{-1}Y(z)-0.8(3)=(1-0.8z^{-1})Y(z)-2.4$.

Right side: $\dfrac{1}{1-0.5z^{-1}}$.

**(ii) Solve for $Y(z)$:**

$$(1-0.8z^{-1})Y(z)=\dfrac{1}{1-0.5z^{-1}}+2.4,$$

$$Y(z)=\dfrac{1}{(1-0.5z^{-1})(1-0.8z^{-1})}+\dfrac{2.4}{1-0.8z^{-1}}.$$

**(iii) Partial fractions on the first term:**

$$\dfrac{1}{(1-0.5z^{-1})(1-0.8z^{-1})}=\dfrac{A}{1-0.5z^{-1}}+\dfrac{B}{1-0.8z^{-1}}.$$

- Set $z^{-1}=2$: $1=A(1-1.6)=-0.6A\Rightarrow A=-5/3$.
- Set $z^{-1}=1.25$: $1=B(1-0.625)=0.375B\Rightarrow B=8/3$.

So

$$Y(z)=\dfrac{-5/3}{1-0.5z^{-1}}+\dfrac{8/3}{1-0.8z^{-1}}+\dfrac{2.4}{1-0.8z^{-1}}=\dfrac{-5/3}{1-0.5z^{-1}}+\dfrac{8/3+12/5}{1-0.8z^{-1}}.$$

Since $8/3+12/5=40/15+36/15=76/15$:

$$\boxed{\,y[n]=\Bigl[-\dfrac{5}{3}(0.5)^{n}+\dfrac{76}{15}(0.8)^{n}\Bigr]\,u[n]\,}$$

**(iv) Verify:**

- $y[0]=-5/3+76/15=-25/15+76/15=51/15=17/5=3.4$. From ODE: $y[0]=0.8\,y[-1]+x[0]=0.8(3)+1=3.4$. $\checkmark$
- $y[1]=-5/3\,(0.5)+76/15\,(0.8)=-5/6+60.8/15\approx -0.833+4.053=3.22$. From ODE: $y[1]=0.8\,y[0]+x[1]=0.8(3.4)+0.5=2.72+0.5=3.22$. $\checkmark$

---

### Part (b): Second-Order Zero-Input

System: $y[n]-0.5\,y[n-1]-0.06\,y[n-2]=0$, $y[-1]=5$, $y[-2]=0$.

**(i) Unilateral z-transform:**

$$\mathcal{Z}_u\{y[n-1]\}=z^{-1}Y+y[-1]=z^{-1}Y+5,$$
$$\mathcal{Z}_u\{y[n-2]\}=z^{-2}Y+y[-2]+y[-1]z^{-1}=z^{-2}Y+0+5z^{-1}.$$

Substitute:

$$Y-0.5(z^{-1}Y+5)-0.06(z^{-2}Y+5z^{-1})=0,$$

$$(1-0.5z^{-1}-0.06z^{-2})Y=2.5+0.3z^{-1}.$$

Factor: $z^{2}-0.5z-0.06=0\Rightarrow z=\dfrac{0.5\pm\sqrt{0.25+0.24}}{2}=\dfrac{0.5\pm 0.7}{2}$, so poles at $z=0.6$ and $z=-0.1$.

$$Y(z)=\dfrac{2.5+0.3z^{-1}}{(1-0.6z^{-1})(1+0.1z^{-1})}.$$

**Partial fractions:**

$$\dfrac{2.5+0.3z^{-1}}{(1-0.6z^{-1})(1+0.1z^{-1})}=\dfrac{A}{1-0.6z^{-1}}+\dfrac{B}{1+0.1z^{-1}}.$$

- Set $z^{-1}=5/3$: $2.5+0.5=A(1+1/6)=(7/6)A\Rightarrow 3=(7/6)A\Rightarrow A=18/7$.
- Set $z^{-1}=-10$: $2.5-3=B(1+6)=7B\Rightarrow -0.5=7B\Rightarrow B=-1/14$.

$$\boxed{\,y[n]=\Bigl[\dfrac{18}{7}(0.6)^{n}-\dfrac{1}{14}(-0.1)^{n}\Bigr]\,u[n]\,}$$

**Verify:** $y[0]=18/7-1/14=36/14-1/14=35/14=2.5$. From ODE: $y[0]=0.5\,y[-1]+0.06\,y[-2]=0.5(5)+0=2.5$. $\checkmark$

**(iii)** The input is zero, so this is a **pure zero-input response** (ZIR): the output is entirely due to the initial conditions $y[-1]=5$ and $y[-2]=0$.

---

### Part (c): ZSR/ZIR Decomposition for Part (a)

From part (a): $Y(z)=\dfrac{1}{(1-0.5z^{-1})(1-0.8z^{-1})}+\dfrac{2.4}{1-0.8z^{-1}}$.

**Zero-state response** (set $y[-1]=0$, keep input):

$$Y_{\text{ZS}}(z)=\dfrac{1}{(1-0.5z^{-1})(1-0.8z^{-1})}.$$

From the partial fractions computed in part (a): $A=-5/3$, $B=8/3$.

$$\boxed{\,y_{\text{ZS}}[n]=\Bigl[-\dfrac{5}{3}(0.5)^{n}+\dfrac{8}{3}(0.8)^{n}\Bigr]\,u[n]\,}$$

**Zero-input response** (set input to 0, keep $y[-1]=3$):

$$(1-0.8z^{-1})Y_{\text{ZI}}=2.4 \;\Rightarrow\; Y_{\text{ZI}}(z)=\dfrac{2.4}{1-0.8z^{-1}}.$$

$$\boxed{\,y_{\text{ZI}}[n]=2.4\,(0.8)^{n}\,u[n]\,}$$

**Verify the sum:**

$$y_{\text{ZS}}+y_{\text{ZI}}=\Bigl[-\dfrac{5}{3}(0.5)^{n}+\dfrac{8}{3}(0.8)^{n}+2.4(0.8)^{n}\Bigr]u[n]=\Bigl[-\dfrac{5}{3}(0.5)^{n}+\Bigl(\dfrac{8}{3}+\dfrac{12}{5}\Bigr)(0.8)^{n}\Bigr]u[n],$$

with $\dfrac{8}{3}+\dfrac{12}{5}=\dfrac{40+36}{15}=\dfrac{76}{15}$. This matches the total $y[n]$ from part (a). $\checkmark$

**Key Point.** The ZSR starts at $y_{\text{ZS}}[0]=-5/3+8/3=1=x[0]$ (as if the system started at rest). The ZIR starts at $y_{\text{ZI}}[0]=2.4$ (the effect of the IC). Their sum gives $y[0]=1+2.4=3.4$, matching the ODE check.

---

## Problem Index

- **Problem 1.** Compute the z-transform and ROC for seven signals (causal geometric, anti-causal geometric, delta combinations, $n\cdot a^{n}u[n]$, sum of two geometrics as a rational function, a two-sided signal, and a damped cosine), then verify $X(1)=\sum x[n]$.
- **Problem 2.** Inverse z-transforms via partial fractions: distinct real poles causal, distinct real poles two-sided (annular ROC), repeated poles, and complex-conjugate poles (damped cosine).
- **Problem 3.** z-transform properties — time shifting, z-domain scaling, convolution (cascade), and the initial-value theorem.
- **Problem 4.** Second-order causal LTI difference equation: $H(z)$, BIBO stability, $h[n]$, driven output with $(0.5)^{n}u[n]$, and a second system with a pole outside the unit circle under causal vs. anti-causal assumptions.
- **Problem 5.** Unilateral z-transform — first-order with nonzero IC, second-order zero-input response, and ZSR/ZIR decomposition.

---

## Notes on Discrepancies (vs. earlier `hw6_solutions.md`)

The earlier student-made solution file is in strong agreement with the official set. A few minor observations:

1. **Problem 3(a) — zeros at $z=0$.** The student file states cleanly that the shift introduces *two zeros at $z=0$*. The official file initially writes this in the $z^{-1}$ form, then walks through the cancellation with the pole $z=0$ introduced by the $z^{-2}$ factor and concludes the two extra zeros live at $z=\infty$ in the $z$-form. Both descriptions are equivalent; the official answer is more pedantic but the student answer is cleaner.
2. **Problem 4(c) — impulse response form.** Both solutions give $h[n]=\bigl[2(0.6)^{n}-(0.3)^{n}\bigr]u[n]$; the student version wrote the same content as $-(0.3)^{n}+2(0.6)^{n}$. No numerical difference.
3. **Problem 5(b) — sign on the $(-0.1)^{n}$ term.** The official solution writes $y[n]=\tfrac{18}{7}(0.6)^{n}-\tfrac{1}{14}(-0.1)^{n}$ whereas the student solution wrote $+(-1/14)(-0.1)^{n}=-\tfrac{1}{14}(-0.1)^{n}$. These are the **same expression** (a minus sign in front of $1/14$). $y[0]=18/7-1/14=35/14=2.5$ matches the ODE check in both files.
4. **Problem 1(e) — zero at $z=0$.** The student file claims an additional zero at $z=0$ "from $z^{-1}$ terms"; the official file only lists the finite zero at $z=0.5$. The official reading is cleaner: the rational function $\dfrac{6-3z^{-1}}{(1-0.3z^{-1})(1-0.9z^{-1})}$ has one finite zero at $z=0.5$ and (when rewritten in positive powers of $z$) one zero at $z=\infty$; there is no finite zero at $z=0$. The student file's claim is incorrect on this point.

Aside from these small clarifications, every boxed answer matches.
