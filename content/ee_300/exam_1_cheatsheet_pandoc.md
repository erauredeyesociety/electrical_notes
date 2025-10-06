# Comprehensive Laplace Transform Cheat Sheet for Linear Circuit Analysis

## Table of Contents
1. [Laplace Transform Fundamentals](#laplace-transform-fundamentals)
2. [Six Essential Properties](#six-essential-properties)
3. [Inverse Laplace Transform](#inverse-laplace-transform)
4. [Circuit Analysis with Laplace](#circuit-analysis-with-laplace)
5. [Initial and Final Value Theorems](#initial-and-final-value-theorems)
6. [Step-by-Step Problem Solving Guide](#step-by-step-problem-solving-guide)

---

## Laplace Transform Fundamentals

### Definition
The Laplace Transform converts time-domain functions $f(t)$ into s-domain functions $F(s)$:

$$F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty f(t)e^{-st} dt$$

where $s = \sigma + j\omega$ is a complex variable.

### Why Use Laplace Transforms?
- **Converts differential equations → algebraic equations**
- **Handles initial conditions automatically**
- **Simplifies circuit analysis dramatically**

### Common Laplace Transform Pairs

| Time Domain $f(t)$ | S-Domain $F(s)$ | ROC (Region of Convergence) |
|---|---|---|
| $\delta(t)$ (unit impulse) | $1$ | All $s$ |
| $u(t)$ (unit step) | $\frac{1}{s}$ | $\text{Re}(s) > 0$ |
| $t$ (unit ramp) | $\frac{1}{s^2}$ | $\text{Re}(s) > 0$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ | $\text{Re}(s) > 0$ |
| $e^{at}$ | $\frac{1}{s-a}$ | $\text{Re}(s) > a$ |
| $te^{at}$ | $\frac{1}{(s-a)^2}$ | $\text{Re}(s) > a$ |
| $\cos(\omega t)$ | $\frac{s}{s^2+\omega^2}$ | $\text{Re}(s) > 0$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2+\omega^2}$ | $\text{Re}(s) > 0$ |
| $e^{-at}\cos(\omega t)$ | $\frac{s+a}{(s+a)^2+\omega^2}$ | $\text{Re}(s) > -a$ |
| $e^{-at}\sin(\omega t)$ | $\frac{\omega}{(s+a)^2+\omega^2}$ | $\text{Re}(s) > -a$ |

### Poles and Zeros
- **Poles**: Values of $s$ where $F(s) \to \infty$ (denominator = 0)
- **Zeros**: Values of $s$ where $F(s) = 0$ (numerator = 0)
- Poles determine the **nature of the time response** (exponential decay, oscillation, etc.)

---

## Six Essential Properties

### 1. Linearity
$$\mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)$$

**Use this to**: Break complex functions into simpler parts and transform each separately.

### 2. Frequency Shift (Multiply by $e^{-at}$)
$$\mathcal{L}\{e^{-at}f(t)\} = F(s+a)$$

**Use this to**: Handle exponential envelopes. Replace $s$ with $s+a$ in $F(s)$.

**Example**: 
$$\mathcal{L}\{e^{-2t}\cos(3t)\} = \frac{s+2}{(s+2)^2+9}$$

### 3. Time Shift (Delay Property)
$$\mathcal{L}\{f(t-T)u(t-T)\} = e^{-sT}F(s)$$

**Use this to**: Handle delayed signals. The term $e^{-sT}$ indicates a delay of $T$ seconds.

### 4. Differentiation Property **CRITICAL FOR CIRCUITS**
$$\mathcal{L}\left\{\frac{df}{dt}\right\} = sF(s) - f(0^-)$$

$$\mathcal{L}\left\{\frac{d^2f}{dt^2}\right\} = s^2F(s) - sf(0^-) - f'(0^-)$$

**Use this to**: Transform differential equations. Initial conditions appear as source terms!

### 5. Integration Property
$$\mathcal{L}\left\{\int_0^t f(\tau)d\tau\right\} = \frac{1}{s}F(s)$$

**Use this to**: Handle integrals in your equations (less common in basic circuit analysis).

### 6. Multiply by $t$ Property
$$\mathcal{L}\{tf(t)\} = -\frac{dF(s)}{ds}$$

**Use this to**: Handle terms multiplied by $t$, or deal with multiple-order poles in inverse transforms.

---

## Inverse Laplace Transform

### Goal
Convert $F(s)$ back to $f(t)$ using **Partial Fraction Expansion (PFE)**.

### Terminology
- **PRF (Proper Rational Function)**: Order of numerator < order of denominator
- **IRF (Improper Rational Function)**: Order of numerator \geq order of denominator

### General Form After PFE
$$F(s) = \frac{k_1}{s-p_1} + \frac{k_2}{s-p_2} + \cdots + \frac{k_n}{s-p_n}$$

where:
- $p_i$ = pole locations (determine exponential rates)
- $k_i$ = residues (determine weights/amplitudes)

### Case 1: Distinct Real Poles

**PFE Form**:
$$F(s) = \frac{k_1}{s-p_1} + \frac{k_2}{s-p_2} + \cdots + \frac{k_n}{s-p_n}$$

**Time Domain**:
$$f(t) = k_1e^{p_1t}u(t) + k_2e^{p_2t}u(t) + \cdots + k_ne^{p_nt}u(t)$$

**Finding Residues: Cover-Up Method**

The cover-up method is a quick technique for finding residues in partial fraction expansion.

**Basic Principle**: To find residue $k_i$ for pole at $s = p_i$:

$$k_i = \left.(s-p_i)F(s)\right|_{s=p_i}$$

**Step-by-Step Procedure**:

1. **Multiply** both sides of $F(s)$ by the factor $(s-p_i)$ corresponding to the pole you're solving for
2. **"Cover up"** (mentally or physically) the factor $(s-p_i)$ in the original denominator
3. **Substitute** $s = p_i$ into what remains
4. **Evaluate** the expression to get $k_i$

**Why It Works**: Multiplying by $(s-p_i)$ cancels that factor in the denominator. When we set $s = p_i$, all other fractions in the PFE become zero (they have $(s-p_i)$ in their numerators), leaving only $k_i$.

**Detailed Example**:
$$F(s) = \frac{3s+5}{(s+1)(s+2)}$$

Set up PFE:
$$\frac{3s+5}{(s+1)(s+2)} = \frac{k_1}{s+1} + \frac{k_2}{s+2}$$

**Find $k_1$ (pole at $s=-1$)**:
1. Multiply by $(s+1)$:
   $$k_1 + \frac{k_2(s+1)}{s+2} = \frac{3s+5}{s+2}$$
   
2. Set $s = -1$ (the second term vanishes):
   $$k_1 = \frac{3(-1)+5}{(-1)+2} = \frac{2}{1} = 2$$

**Find $k_2$ (pole at $s=-2$)**:
1. Multiply by $(s+2)$:
   $$\frac{k_1(s+2)}{s+1} + k_2 = \frac{3s+5}{s+1}$$
   
2. Set $s = -2$ (the first term vanishes):
   $$k_2 = \frac{3(-2)+5}{(-2)+1} = \frac{-1}{-1} = 1$$

**Result**: $f(t) = 2e^{-t}u(t) + e^{-2t}u(t)$

**Practical Shortcut** (the actual "cover-up"):

For $F(s) = \frac{N(s)}{(s-p_1)(s-p_2)...(s-p_n)}$

To find $k_i$:
- Cover up $(s-p_i)$ in the denominator
- Replace all remaining $s$ with $p_i$
- Calculate the result

**Visual Example**:
$$F(s) = \frac{10}{(s+2)(s+3)(s+5)}$$

Find $k_2$ at $s = -3$:
- Cover up $(s+3)$ in denominator: $\frac{10}{(s+2)(s+5)}$
- Substitute $s = -3$: $\frac{10}{(-3+2)(-3+5)} = \frac{10}{(-1)(2)} = -5$

**Three-Pole Example**:
$$F(s) = \frac{s+7}{(s+1)(s+2)(s+4)}$$

Find all residues:

$k_1$ at $s=-1$:
$$k_1 = \frac{(-1)+7}{(-1+2)(-1+4)} = \frac{6}{(1)(3)} = 2$$

$k_2$ at $s=-2$:
$$k_2 = \frac{(-2)+7}{(-2+1)(-2+4)} = \frac{5}{(-1)(2)} = -\frac{5}{2}$$

$k_3$ at $s=-4$:
$$k_3 = \frac{(-4)+7}{(-4+1)(-4+2)} = \frac{3}{(-3)(-2)} = \frac{1}{2}$$

**Answer**: 
$$f(t) = \left[2e^{-t} - \frac{5}{2}e^{-2t} + \frac{1}{2}e^{-4t}\right]u(t)$$

**Important Notes**:
- Cover-up method **only works for distinct (simple) poles**
- For repeated poles, use the derivative method (see Case 3)
- For complex poles, you can use cover-up but will get complex residues (see Case 2)
- Always verify: multiply out your PFE to check it equals the original $F(s)$

### Case 2: Complex Conjugate Poles

**PFE Form** (poles at $s = -\alpha \pm j\beta$):
$$F(s) = \frac{k}{s-(-\alpha+j\beta)} + \frac{k^*}{s-(-\alpha-j\beta)}$$

where $k$ and $k^*$ are complex conjugates.

**Time Domain**:
$$f(t) = 2|k|e^{-\alpha t}\cos(\beta t + \angle k)u(t)$$

**Steps**:
1. Find residue $k$ at one pole using cover-up method
2. Express $k$ in polar form: $k = |k|e^{j\angle k}$
3. Apply formula above

**Alternative Form** (using real coefficients):
$$f(t) = e^{-\alpha t}[A\cos(\beta t) + B\sin(\beta t)]u(t)$$

where:
- $A = 2\text{Re}\{k\}$
- $B = -2\text{Im}\{k\}$

### Case 3: Multiple-Order Poles

**PFE Form** (pole at $s=p_1$ with multiplicity $m$):
$$F(s) = \frac{k_{1m}}{(s-p_1)^m} + \frac{k_{1(m-1)}}{(s-p_1)^{m-1}} + \cdots + \frac{k_{11}}{s-p_1} + \text{(other poles)}$$

**Time Domain**:
$$f(t) = \left[k_{1m}\frac{t^{m-1}}{(m-1)!} + k_{1(m-1)}\frac{t^{m-2}}{(m-2)!} + \cdots + k_{11}\right]e^{p_1t}u(t) + \text{(other terms)}$$

**Finding Residues - Method 1: Matching Coefficients**
1. Find highest-order residue $k_{1m}$ using cover-up method
2. Multiply both sides by $(s-p_1)^m$
3. Expand and match coefficients of powers of $s$

**Finding Residues - Method 2: n-to-1-Order-Poles**
For highest order residue:
$$k_{1m} = \left.(s-p_1)^m F(s)\right|_{s=p_1}$$

For next lower order:
$$k_{1(m-1)} = \left.\frac{d}{ds}\left[(s-p_1)^m F(s)\right]\right|_{s=p_1}$$

And so on with higher derivatives.

### Case 4: Improper Rational Functions (IRF)

**If numerator order \geq denominator order**:

1. **Perform long division** first
2. Write as: $F(s) = Q(s) + \frac{R(s)}{D(s)}$
3. Apply PFE to the proper fraction $\frac{R(s)}{D(s)}$
4. Inverse transform polynomial terms:
   - $\mathcal{L}^{-1}\{1\} = \delta(t)$ (impulse)
   - $\mathcal{L}^{-1}\{s\} = \delta'(t)$ (derivative of impulse)

### Case 5: Delayed Functions ($e^{-sT}$ terms)

$$\mathcal{L}^{-1}\{F(s)e^{-sT}\} = f(t-T)u(t-T)$$

The function is delayed by $T$ seconds and is zero for $t < T$.

---

## Circuit Analysis with Laplace

### S-Domain Component Models

| Component | Time Domain | S-Domain Impedance | Initial Condition Handling |
|---|---|---|---|
| **Resistor** | $v(t) = Ri(t)$ | $Z_R = R$ | None |
| **Inductor** | $v(t) = L\frac{di}{dt}$ | $Z_L = sL$ | Voltage source $Li(0^-)$ in series |
| **Capacitor** | $i(t) = C\frac{dv}{dt}$ | $Z_C = \frac{1}{sC}$ | Voltage source $\frac{v(0^-)}{s}$ in series OR current source $Cv(0^-)$ in parallel |

### Inductor S-Domain Model (Detailed)

**Circuit representation with initial condition**:
```
    Li(0-)   +    sL
  ----[+|-]----[====]----
   (voltage      (impedance)
    source)
```

**Equation**: $V_L(s) = sLI(s) - Li(0^-)$

### Capacitor S-Domain Model (Detailed)

**Series representation**:
```
   v(0-)/s   +    1/sC
  ----[+|-]----[====]----
   (voltage      (impedance)
    source)
```

**Parallel representation**:
```
      1/sC        Cv(0-)
  ----[====]----[--|>]----
   (impedance)  (current
                 source)
```

**Equation**: $I_C(s) = sCV(s) - Cv(0^-)$

### Kirchhoff's Laws in S-Domain

**KVL (Kirchhoff's Voltage Law)**:
$$\sum V_i(s) = 0$$

Sum of voltages around any closed loop equals zero (same as time domain, but with $V(s)$).

**KCL (Kirchhoff's Current Law)**:
$$\sum I_i(s) = 0$$

Sum of currents entering a node equals sum leaving (same as time domain, but with $I(s)$).

### Zero-Input Response (ZIR) and Zero-State Response (ZSR)

**Total Response**:
$$y(t) = y_{ZIR}(t) + y_{ZSR}(t)$$

- **ZIR**: Response due to initial conditions only (no external input)
- **ZSR**: Response due to external input only (zero initial conditions)

---

## Initial and Final Value Theorems

### Initial Value Theorem (IVT)

$$f(0^+) = \lim_{s \to \infty} sF(s)$$

**Requirements**:
- $F(s)$ must be a **Proper Rational Function (PRF)**
- If IRF, IVT gives $\infty$ (not useful)

**Use**: Quickly find initial value without doing full inverse transform.

### Final Value Theorem (FVT)

$$f(\infty) = \lim_{s \to 0} sF(s)$$

**Requirements**:
- All poles of $sF(s)$ must have $\text{Re}(s) < 0$ (lie in left half-plane)
- If poles on imaginary axis or right half-plane, FVT is **NOT APPLICABLE**

**Use**: Quickly find steady-state value without doing full inverse transform.

**Common Mistake**: Applying FVT when poles are at $s=0$ or in right half-plane. Always check pole locations of $sF(s)$ first!

---

## Step-by-Step Problem Solving Guide

### Problem Type 1: Find Laplace Transform of $f(t)$

**Steps**:
1. **Break down** $f(t)$ into simpler additive terms (use linearity)
2. **Identify** if any special properties apply:
   - Exponential envelope → frequency shift property
   - Time delay → delay property
   - Derivative → differentiation property
3. **Apply** standard transforms from table
4. **Combine** results

**Example**: Find $\mathcal{L}\{e^{-2t}\sin(3t) + t^2\}$

Solution:
- Term 1: $\mathcal{L}\{e^{-2t}\sin(3t)\}$ → Use frequency shift: replace $s$ with $s+2$ in $\mathcal{L}\{\sin(3t)\}$
  - $\mathcal{L}\{\sin(3t)\} = \frac{3}{s^2+9}$
  - $\mathcal{L}\{e^{-2t}\sin(3t)\} = \frac{3}{(s+2)^2+9}$
- Term 2: $\mathcal{L}\{t^2\} = \frac{2!}{s^3} = \frac{2}{s^3}$
- **Answer**: $F(s) = \frac{3}{(s+2)^2+9} + \frac{2}{s^3}$

### Problem Type 2: Find Inverse Laplace Transform of $F(s)$

**Steps**:
1. **Check if PRF or IRF**
   - If IRF: Do long division first
2. **Factor denominator** completely to find all poles
3. **Set up PFE** based on pole types:
   - Distinct real poles → simple fractions
   - Complex conjugate poles → pair of conjugate fractions
   - Multiple-order poles → multiple fractions with increasing powers
4. **Find residues** using cover-up method (or other methods for multiple poles)
5. **Write time-domain expression** using inverse transform formulas
6. **Include $u(t)$** for causality

**Example**: Find $\mathcal{L}^{-1}\left\{\frac{2s+10}{s^2+3s+2}\right\}$

Solution:
1. Check: PRF (numerator order 1 < denominator order 2) $\checkmark$
2. Factor: $s^2+3s+2 = (s+1)(s+2)$
3. PFE: $\frac{2s+10}{(s+1)(s+2)} = \frac{k_1}{s+1} + \frac{k_2}{s+2}$
4. Find residues:
   - $k_1 = \left.\frac{2s+10}{s+2}\right|_{s=-1} = \frac{2(-1)+10}{-1+2} = \frac{8}{1} = 8$
   - $k_2 = \left.\frac{2s+10}{s+1}\right|_{s=-2} = \frac{2(-2)+10}{-2+1} = \frac{6}{-1} = -6$
5. **Answer**: $f(t) = 8e^{-t}u(t) - 6e^{-2t}u(t)$

### Problem Type 3: Solve Differential Equation with Initial Conditions

**Steps**:
1. **Take Laplace transform** of entire equation (term by term)
2. **Apply differentiation property**: $\mathcal{L}\{f'\} = sF(s) - f(0^-)$
3. **Substitute** known initial conditions
4. **Solve algebraically** for $F(s)$
5. **Apply inverse transform** (PFE + cover-up method)

**Example**: Solve $\frac{dy}{dt} + 3y = e^{-t}$ with $y(0^-) = 2$

Solution:
1. Transform: $\mathcal{L}\{y'\} + 3\mathcal{L}\{y\} = \mathcal{L}\{e^{-t}\}$
2. Apply property: $sY(s) - y(0^-) + 3Y(s) = \frac{1}{s+1}$
3. Substitute: $sY(s) - 2 + 3Y(s) = \frac{1}{s+1}$
4. Solve:
   - $(s+3)Y(s) = \frac{1}{s+1} + 2$
   - $Y(s) = \frac{1}{(s+1)(s+3)} + \frac{2}{s+3}$
   - $Y(s) = \frac{1 + 2(s+1)}{(s+1)(s+3)} = \frac{2s+3}{(s+1)(s+3)}$
5. PFE and inverse transform to get $y(t)$

### Problem Type 4: Analyze Circuit with Laplace

**Steps**:
1. **Draw circuit for $t < 0$**: Find initial conditions $i_L(0^-), v_C(0^-)$
2. **Draw s-domain circuit for $t \geq 0$**:
   - Replace $R$ with $R$
   - Replace $L$ with $sL$ and series voltage source $Li(0^-)$
   - Replace $C$ with $\frac{1}{sC}$ and series voltage source $\frac{v(0^-)}{s}$
   - Transform sources to s-domain
3. **Apply circuit analysis** (KVL, KCL, node/mesh analysis) in s-domain
4. **Solve for desired $V(s)$ or $I(s)$**
5. **Apply inverse transform** to get time-domain response
6. **(Optional) Verify** using initial/final value theorems

**Example: RL Circuit**

Given: $R = 10\Omega$, $L = 1H$, $i_L(0^-) = 0.5A$, step input $v_s(t) = 5u(t)V$

Find: $i_L(t)$ for $t \geq 0$

Solution:
1. Initial condition: $i_L(0^-) = 0.5A$
2. S-domain circuit:
   - Voltage source: $V_s(s) = \frac{5}{s}$
   - Series elements: $Li(0^-) = 1(0.5) = 0.5V$, $sL = s$, $R = 10$
3. KVL: $\frac{5}{s} = 0.5 + sI_L(s) + 10I_L(s)$
4. Solve: 
   - $\frac{5}{s} - 0.5 = (s+10)I_L(s)$
   - $I_L(s) = \frac{5-0.5s}{s(s+10)} = \frac{5-0.5s}{s(s+10)}$
5. Apply PFE and inverse transform

### Problem Type 5: Apply Initial/Final Value Theorems

**Steps**:
1. **Form $sF(s)$**
2. **For IVT**: 
   - Check if PRF
   - Calculate $\lim_{s \to \infty} sF(s)$
3. **For FVT**:
   - Check poles of $sF(s)$ (must all be in left half-plane)
   - If valid, calculate $\lim_{s \to 0} sF(s)$
4. **(Optional) Verify** by finding $f(t)$ and evaluating at $t=0^+$ or $t=\infty$

---

## Quick Reference Formulas

### Transform Pairs (Most Common)
$$\begin{aligned}
\mathcal{L}\{u(t)\} &= \frac{1}{s} \\
\mathcal{L}\{e^{at}\} &= \frac{1}{s-a} \\
\mathcal{L}\{\sin(\omega t)\} &= \frac{\omega}{s^2+\omega^2} \\
\mathcal{L}\{\cos(\omega t)\} &= \frac{s}{s^2+\omega^2} \\
\mathcal{L}\{t^n\} &= \frac{n!}{s^{n+1}}
\end{aligned}$$

### Properties (Most Used)
$$\begin{aligned}
\mathcal{L}\{af + bg\} &= aF + bG \\
\mathcal{L}\{e^{at}f(t)\} &= F(s-a) \\
\mathcal{L}\{f'\} &= sF(s) - f(0^-) \\
\mathcal{L}\{f(t-T)u(t-T)\} &= e^{-sT}F(s)
\end{aligned}$$

### Inverse Transforms (By Pole Type)
$$\begin{aligned}
\mathcal{L}^{-1}\left\{\frac{1}{s-p}\right\} &= e^{pt}u(t) \\
\mathcal{L}^{-1}\left\{\frac{1}{(s-p)^2}\right\} &= te^{pt}u(t) \\
\mathcal{L}^{-1}\left\{\frac{k}{s+\alpha-j\beta} + \frac{k^*}{s+\alpha+j\beta}\right\} &= 2|k|e^{-\alpha t}\cos(\beta t + \angle k)u(t)
\end{aligned}$$

### Value Theorems
$$\begin{aligned}
f(0^+) &= \lim_{s \to \infty} sF(s) \quad \text{(PRF only)} \\
f(\infty) &= \lim_{s \to 0} sF(s) \quad \text{(stable systems only)}
\end{aligned}$$

---

## Common Mistakes to Avoid

1. [X] **Forgetting initial conditions** when using differentiation property
2. [X] **Not checking if FVT is applicable** (poles in right half-plane)
3. [X] **Missing the $u(t)$ in time-domain answers**
4. [X] **Incorrect sign on initial condition voltage/current sources**
5. [X] **Not factoring denominator completely** before PFE
6. [X] **Using IVT on improper rational functions**
7. [X] **Forgetting to perform long division** for IRFs before PFE
8. [X] **Not checking your answer** with IVT/FVT when possible

---

This cheat sheet covers all major topics for Laplace transform analysis in linear circuits. Practice each problem type systematically, and always verify your answers when possible!