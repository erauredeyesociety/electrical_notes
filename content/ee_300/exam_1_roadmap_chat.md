# Comprehensive Circuit Analysis with Laplace Transform Roadmap (With Equations)

---

## I. Laplace Transform (LT) Fundamentals and Properties

### Use in the Course

* Converts differential equations (time-domain) into algebraic equations (s-domain).
* Simplifies circuit and system analysis.

### Subtopics to Familiarize

* Definition:

$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty f(t)e^{-st} dt
$$

* Poles & zeros, s-plane concepts
* Relationship to Fourier transform (transient vs. steady-state)
* Six key properties (linearity, time/frequency shifts, differentiation, integration, multiply-by-t)

### Common LT Transforms

$$
\begin{aligned}
\mathcal{L}\{1\} &= \frac{1}{s}, & s>0 \\
\mathcal{L}\{e^{at}\} &= \frac{1}{s-a}, & s>a \\
\mathcal{L}\{\cos(\omega t)\} &= \frac{s}{s^2+\omega^2} \\
\mathcal{L}\{\sin(\omega t)\} &= \frac{\omega}{s^2+\omega^2} \\
\mathcal{L}\{t^n\} &= \frac{n!}{s^{n+1}}, & n = 0,1,2,...
\end{aligned}
$$

### Six Key Properties

1. **Linearity:** $\mathcal{L}\{af(t)+bg(t)\} = aF(s)+bG(s)$
2. **Frequency shift:** $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$
3. **Time shift (delay by T):** $\mathcal{L}\{f(t-T)u(t-T)\} = e^{-sT}F(s)$
4. **Differentiation:**
   $\mathcal{L}\{f'(t)\} = sF(s)-f(0^-)$
   $\mathcal{L}\{f^{(n)}(t)\} = s^n F(s)-s^{n-1}f(0^-)-...-f^{(n-1)}(0^-)$
5. **Integration:** $\mathcal{L}\{\int_0^t f(\tau)d\tau\} = \frac{1}{s} F(s)$
6. **Multiply by t:** $\mathcal{L}\{t f(t)\} = -\frac{dF(s)}{ds}$

### Step-by-Step Methodology

1. Break function into additive terms (linearity).
2. Apply known transforms or LT properties.
3. Handle exponentials, derivatives, or delays explicitly.
4. Express final result as $F(s)$.

---

## II. Inverse Laplace Transform (ILT)

### Use in the Course

* Converts $s$-domain solutions back to time-domain.
* Uses Partial Fraction Expansion (PFE) for rational functions.

### Subtopics to Familiarize

* PRF vs IRF (proper vs improper)
* Partial fraction expansion (PFE)
* Poles & residues
* Cover-up method for distinct real poles
* Complex conjugate poles → sinusoidal response
* Multiple-order poles → t^n \* e^{pt} terms
* Delay property: $\mathcal{L}^{-1}\{F(s)e^{-sT}\} = f(t-T)u(t-T)$

### Step-by-Step Methodology

1. Handle IRF via long division: $F(s) = Q(s) + R(s)/D(s)$
2. Factor denominator, identify all poles
3. Calculate residues $k_i$
4. Apply ILT:

   * Distinct real poles: $f(t)=\sum k_i e^{p_i t}u(t)$
   * Complex poles: $f(t)=2|k| e^{\alpha t} \cos(\beta t+\angle k) u(t)$
   * Repeated poles: $f(t)=\frac{t^{m-1}}{(m-1)!} e^{pt} u(t)$
5. Include delay terms: $f(t-T) u(t-T)$

---

## III. Laplace Transform for Differential Equations & Circuit Analysis

### Use in the Course

* Transform circuit differential equations into algebraic equations
* Includes initial conditions via s-domain equivalents

### S-Domain Models

$$
\begin{aligned}
Z_R &= R \\
Z_L &= sL, & \text{with } i(0^-) \to \text{voltage source } L i(0^-) \text{ in series} \\
Z_C &= \frac{1}{sC}, & v(0^-) \to \text{current source } Cv(0^-)s \text{ or } v(0^-)/s
\end{aligned}
$$

### Zero-Input and Zero-State Response

$$
y(t) = y_{ZIR}(t) + y_{ZSR}(t)
$$

* **ZIR:** Response due to initial energy (no external input)
* **ZSR:** Response due to external input (zero initial conditions)

### Differential Equation → S-Domain Example

$$
L \frac{di}{dt} + Ri = v(t)
$$

$$
(sL+R) I(s) - L i(0^-) = V(s)
$$

* Solve for $I(s)$, then apply ILT

### Step-by-Step Methodology

1. Derive differential equation, note t<0 response (initial voltage/current).
2. Transform equation or circuit to s-domain.
3. Apply initial conditions.
4. Solve algebraic equation in s-domain.
5. Apply PFE + ILT to get time-domain response.
6. Combine ZIR + ZSR for full solution.

---

## IV. Initial and Final Value Properties (IVP/FVP)

### Use in the Course

* Quickly compute starting and steady-state values without full ILT

### Formulas

* **Initial Value Theorem (IVT):**

$$
f(0^+) = \lim_{s\to\infty} s F(s), \quad F(s) \text{ PRF only}
$$

* **Final Value Theorem (FVT):**

$$
f(\infty) = \lim_{s\to 0} s F(s), \quad \text{if all poles of } sF(s) \text{ lie in } \Re(s)<0
$$

### Step-by-Step Methodology

1. Form $sF(s)$
2. Apply IVT: $\lim_{s\to\infty} sF(s)$
3. Check poles of $sF(s)$ for FVT applicability
4. Apply FVT: $\lim_{s\to 0} sF(s)$ if valid

---

```mermaid
flowchart TD
    A[Time-Domain Function f(t)] --> B[Laplace Transform F(s)]
    B --> C[S-Domain Circuit or Differential Equation]
    C --> D[Apply Initial Conditions]
    D --> E[Solve Algebraic Equation for Output V(s) / I(s)]
    E --> F[Partial Fraction Expansion / Simplify F(s)]
    F --> G[Inverse Laplace Transform f(t)]
    G --> H{Response Type}
    H --> H1[Zero-State Response (ZSR)]
    H --> H2[Zero-Input Response (ZIR)]
    H1 --> I[Combine ZIR + ZSR]
    H2 --> I
    I --> J[Final Time-Domain Solution f(t)]
    J --> K{Initial / Final Values?}
    K --> L[Initial Value: f(0^+) = lim(s→∞) sF(s)]
    K --> M[Final Value: f(∞) = lim(s→0) sF(s)]

```
