# Complete Linear Circuit Analysis Cheat Sheet

## 1. Laplace Transform Fundamentals

### Definition
$$F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty f(t)e^{-st} dt \quad \text{where } s = \sigma + j\omega$$

### Common Transform Pairs

| Time Domain $f(t)$ | s-Domain $F(s)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $u(t)$ | $\frac{1}{s}$ |
| $t$ | $\frac{1}{s^2}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\frac{1}{s-a}$ |
| $te^{at}$ | $\frac{1}{(s-a)^2}$ |
| $\cos(\omega t)$ | $\frac{s}{s^2+\omega^2}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2+\omega^2}$ |
| $e^{-at}\cos(\omega t)$ | $\frac{s+a}{(s+a)^2+\omega^2}$ |
| $e^{-at}\sin(\omega t)$ | $\frac{\omega}{(s+a)^2+\omega^2}$ |

### Essential Properties

**Linearity:**
$$\mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)$$

**Frequency Shift:**
$$\mathcal{L}\{e^{-at}f(t)\} = F(s+a)$$

**Time Shift:**
$$\mathcal{L}\{f(t-T)u(t-T)\} = e^{-sT}F(s)$$

**Differentiation (CRITICAL):**
$$\mathcal{L}\left\{\frac{df}{dt}\right\} = sF(s) - f(0^-)$$
$$\mathcal{L}\left\{\frac{d^2f}{dt^2}\right\} = s^2F(s) - sf(0^-) - f'(0^-)$$

**Integration:**
$$\mathcal{L}\left\{\int_0^t f(\tau)d\tau\right\} = \frac{1}{s}F(s)$$

---

## 2. s-Domain Circuit Elements

### Element Impedances

| Element | Time Domain | s-Domain Impedance | Initial Condition Model |
|---------|-------------|-------------------|------------------------|
| Resistor | $v = Ri$ | $Z_R = R$ | None |
| Capacitor | $i = C\frac{dv}{dt}$ | $Z_C = \frac{1}{sC}$ | Series: $\frac{v_c(0^-)}{s}$<br>Parallel: $Cv_c(0^-)$ |
| Inductor | $v = L\frac{di}{dt}$ | $Z_L = sL$ | Series: $Li_L(0^-)$ |

### Kirchhoff's Laws in s-Domain
- **KVL:** $\sum V_i(s) = 0$ (around closed loops)
- **KCL:** $\sum I_i(s) = 0$ (at nodes)

---

## 3. Circuit Response Components

### Total Response Breakdown
$$\text{Total Response} = \text{ZIR} + \text{ZSR}$$

**Zero-Input Response (ZIR):**
- Caused by initial conditions only (stored energy)
- No external sources
- Purely natural response

**Zero-State Response (ZSR):**
- Caused by external inputs only
- All initial conditions = 0
- Contains natural + forced response

### Natural vs Forced Response

**Natural Response:**
- From poles of $H(s)$ (network function)
- Circuit's inherent modes
- Independent of input type
- Determined by R, L, C values

**Forced Response:**
- From poles of input signal $V_{in}(s)$
- Same frequency as input
- Amplitude scaled by $H(s)$ at input frequency

---

## 4. Network Functions (Transfer Functions)

### Definition
$$H(s) = \frac{\text{Output}(s)}{\text{Input}(s)} \quad \text{[with ALL initial conditions = 0]}$$

### Types
1. **Transfer Function:** $H(s) = \frac{V_{out}(s)}{V_{in}(s)}$ or $\frac{I_{out}(s)}{I_{in}(s)}$ (different ports)
2. **Driving-Point Impedance:** $Z(s) = \frac{V(s)}{I(s)}$ (same port)
3. **Driving-Point Admittance:** $Y(s) = \frac{I(s)}{V(s)} = \frac{1}{Z(s)}$ (same port)

### Rational Function Form
$$H(s) = \frac{N(s)}{D(s)} = \frac{a_m s^m + a_{m-1}s^{m-1} + \cdots + a_0}{b_n s^n + b_{n-1}s^{n-1} + \cdots + b_0}$$

---

## 5. Poles and Zeros

### Definitions

**ZEROS:** Solutions to $N(s) = 0$ (numerator roots)
- Frequencies where $H(s) = 0$
- Signals at these frequencies are **blocked** from output
- Correspond to **input side** of differential equation

**POLES:** Solutions to $D(s) = 0$ (denominator roots, characteristic equation)
- Frequencies where $H(s) \to \infty$
- Determine **natural response** modes
- Always present in output
- Correspond to **output side** of differential equation

### Pole-Response Relationships

| Pole Location | Time Response | Stability |
|---------------|---------------|-----------|
| Real: $s = -\alpha$ ($\alpha > 0$) | $ke^{-\alpha t}$ (decay) | Stable |
| Real: $s = +\alpha$ | $ke^{+\alpha t}$ (growth) | Unstable |
| Complex: $s = -\alpha \pm j\omega_d$ | $Ae^{-\alpha t}\cos(\omega_d t + \phi)$ | Stable if $\alpha > 0$ |
| Imaginary: $s = \pm j\omega_0$ | $A\cos(\omega_0 t + \phi)$ | Marginally stable |
| Origin: $s = 0$ | $k$ (constant/step) | Marginally stable |

**Stability Rule:** System is stable if ALL poles have $\text{Re}(s) < 0$ (left half-plane)

### Resonance Condition
When **input frequency = pole frequency**: Output term becomes $t \cdot e^{st}$ (grows with time)

---

## 6. Inverse Laplace Transform via Partial Fraction Expansion

### Terminology
- **PRF (Proper Rational Function):** Numerator degree < denominator degree
- **IRF (Improper Rational Function):** Numerator degree \geq denominator degree

### Case 1: Distinct Real Poles

**PFE Setup:**
$$F(s) = \frac{k_1}{s-p_1} + \frac{k_2}{s-p_2} + \cdots + \frac{k_n}{s-p_n}$$

**Cover-Up Method for Residue $k_i$:**
$$k_i = \left[(s-p_i)F(s)\right]_{s=p_i}$$

**Time Domain:**
$$f(t) = \sum_{i=1}^{n} k_i e^{p_i t} u(t)$$

### Case 2: Complex Conjugate Poles

**Poles:** $s = -\alpha \pm j\beta$

**PFE:**
$$F(s) = \frac{k}{s-(-\alpha+j\beta)} + \frac{k^*}{s-(-\alpha-j\beta)} + \text{(other terms)}$$

**Time Domain:**
$$f(t) = 2|k|e^{-\alpha t}\cos(\beta t + \angle k)u(t) + \text{(other terms)}$$

**Alternative (Real Form):**
$$f(t) = e^{-\alpha t}[A\cos(\beta t) + B\sin(\beta t)]u(t)$$
where $A = 2\text{Re}\{k\}$, $B = -2\text{Im}\{k\}$

### Case 3: Repeated Poles

**Pole at $s = p$ with multiplicity $m$:**

**PFE:**
$$F(s) = \frac{k_m}{(s-p)^m} + \frac{k_{m-1}}{(s-p)^{m-1}} + \cdots + \frac{k_1}{s-p} + \text{(other terms)}$$

**Residue Formulas:**
$$k_m = \left[(s-p)^m F(s)\right]_{s=p}$$
$$k_{m-1} = \left[\frac{d}{ds}(s-p)^m F(s)\right]_{s=p}$$
$$k_{m-j} = \left[\frac{1}{j!}\frac{d^j}{ds^j}(s-p)^m F(s)\right]_{s=p}$$

**Time Domain:**
$$f(t) = \left[k_m\frac{t^{m-1}}{(m-1)!} + k_{m-1}\frac{t^{m-2}}{(m-2)!} + \cdots + k_1\right]e^{pt}u(t) + \text{(other terms)}$$

### Case 4: Improper Rational Functions

**If numerator degree \geq denominator degree:**
1. Perform polynomial long division: $F(s) = Q(s) + \frac{R(s)}{D(s)}$
2. Apply PFE to proper fraction $\frac{R(s)}{D(s)}$
3. Transform polynomial terms: $\mathcal{L}^{-1}\{s^n\} = \delta^{(n)}(t)$ (derivatives of impulse)

### Case 5: Delayed Functions

$$\mathcal{L}^{-1}\{F(s)e^{-sT}\} = f(t-T)u(t-T)$$

---

## 7. Initial and Final Value Theorems

### Initial Value Theorem (IVT)
$$f(0^+) = \lim_{s \to \infty} sF(s)$$

**Requirements:** $F(s)$ must be PRF (proper rational function)

### Final Value Theorem (FVT)
$$f(\infty) = \lim_{s \to 0} sF(s)$$

**Requirements:** ALL poles of $sF(s)$ must have $\text{Re}(s) < 0$ (left half-plane)

**⚠️ Warning:** FVT is invalid if poles exist at $s = 0$ or in right half-plane

---

## 8. Step-by-Step Problem-Solving Procedures

### A. Finding Network Function H(s) from Circuit

1. **Transform** all elements to s-domain: $R$, $\frac{1}{sC}$, $sL$
2. **Zero ALL initial conditions** (voltage sources → short, current sources → open)
3. **Transform input sources** to s-domain
4. **Define** input and output variables
5. **Apply circuit analysis:**
   - Voltage/current divider
   - Series/parallel combinations
   - Nodal analysis (KCL)
   - Mesh analysis (KVL)
6. **Form** $H(s) = \frac{\text{Output}(s)}{\text{Input}(s)}$
7. **Simplify** to rational function form

### B. Finding Poles and Zeros

1. Express $H(s) = \frac{N(s)}{D(s)}$ in polynomial form
2. **Find Zeros:** Set $N(s) = 0$, solve for $s$
   - 1st order: $s = -\frac{b}{a}$
   - 2nd order: $s = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$
   - Higher: Factor or numerical methods
3. **Find Poles:** Set $D(s) = 0$, solve for $s$ (same methods)
4. **Check discriminant** ($\Delta = b^2 - 4ac$) for 2nd order:
   - $\Delta > 0$: Two real poles
   - $\Delta = 0$: Repeated real pole
   - $\Delta < 0$: Complex conjugate pair

### C. Finding Time Response via Inverse Laplace

1. **Calculate** $V_{out}(s) = H(s) \cdot V_{in}(s)$
2. **Check** if PRF or IRF
   - If IRF: Perform long division first
3. **Factor denominator** completely to find ALL poles
4. **Setup PFE** based on pole types (distinct, complex, repeated)
5. **Find residues:**
   - Simple poles: Cover-up method
   - Complex poles: Cover-up, then convert to magnitude/angle
   - Repeated poles: Derivative method
6. **Inverse transform** each term
7. **Add $u(t)$** to ensure causality
8. **Identify components:**
   - Terms from $H(s)$ poles = Natural response
   - Terms from $V_{in}(s)$ poles = Forced response

### D. Converting H(s) to Differential Equation

1. **Start with** $H(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{N(s)}{D(s)}$
2. **Cross-multiply:** $V_{out}(s) \cdot D(s) = V_{in}(s) \cdot N(s)$
3. **Replace** $s$ operators:
   - $s \to \frac{d}{dt}$
   - $s^2 \to \frac{d^2}{dt^2}$
   - $s^n \to \frac{d^n}{dt^n}$
4. **Write ODE:**
$$D\left(\frac{d}{dt}\right) v_{out}(t) = N\left(\frac{d}{dt}\right) v_{in}(t)$$

**Key:** Denominator (poles) → output side (left), Numerator (zeros) → input side (right)

### E. Solving Differential Equations with Laplace

1. **Take Laplace transform** of entire equation
2. **Apply differentiation property:** $\mathcal{L}\{f^{(n)}\} = s^n F(s) - s^{n-1}f(0^-) - \cdots - f^{(n-1)}(0^-)$
3. **Substitute** known initial conditions
4. **Solve algebraically** for $F(s)$
5. **Apply inverse Laplace** (PFE + residues)
6. **Verify** using IVT/FVT if applicable

### F. Complete Circuit Analysis with Initial Conditions

1. **Analyze $t < 0$ circuit:** Find $v_C(0^-)$ and $i_L(0^-)$
2. **Draw s-domain circuit for $t \geq 0$:**
   - Replace elements with impedances
   - Add initial condition sources:
     - Capacitor: $\frac{v_c(0^-)}{s}$ in series with $\frac{1}{sC}$
     - Inductor: $Li_L(0^-)$ in series with $sL$
   - Transform input sources
3. **Apply circuit analysis** (KVL, KCL, nodal, mesh) in s-domain
4. **Solve** for desired $V(s)$ or $I(s)$
5. **Apply inverse Laplace transform**
6. **(Optional) Verify** with IVT: $v(0^+)$ or FVT: $v(\infty)$

---

## 9. Problem-Solving Decision Tree

### When given a CIRCUIT:
1. Need $H(s)$? → Procedure A (zero ICs!)
2. Need poles/zeros? → First find $H(s)$, then Procedure B
3. Need time response? → Find $H(s)$, then Procedure C
4. Have initial conditions? → Procedure F

### When given H(s):
1. Need poles/zeros? → Procedure B
2. Need differential equation? → Procedure D
3. Need time response? → Procedure C (need input too)

### When given DIFFERENTIAL EQUATION:
1. Need $H(s)$? → Laplace transform both sides, solve for Output/Input
2. Need solution? → Procedure E
3. Need poles/zeros? → First get $H(s)$, then Procedure B

---

## 10. Critical Reminders & Common Mistakes

### Must Remember
✓ **Always zero initial conditions** when finding $H(s)$
✓ $H(s)$ describes **ZSR only**, not ZIR
✓ **Include $u(t)$** in all time-domain responses
✓ Complex poles **always come in conjugate pairs**
✓ Check **FVT applicability** before using (poles must be in left half-plane)
✓ **Factor denominator completely** before PFE

### Common Errors
✗ Wrong impedances: $C$ is $\frac{1}{sC}$ NOT $sC$; $L$ is $sL$ NOT $\frac{1}{sL}$
✗ Confusing poles (denominator) with zeros (numerator)
✗ Using FVT when poles at origin or in right half-plane
✗ Forgetting initial condition sources in s-domain circuit
✗ Not checking if PRF before applying IVT
✗ Mixing up natural (from $H(s)$ poles) vs forced (from input poles) response
✗ Incorrect signs on initial condition sources

---

## 11. Quick Reference Table

### s-Domain Impedances
$$Z_R = R \qquad Z_C = \frac{1}{sC} \qquad Z_L = sL$$

### Network Function
$$H(s) = \frac{N(s)}{D(s)} = \frac{\text{Output}(s)}{\text{Input}(s)} \quad \text{[ICs = 0]}$$

### Poles and Zeros
$$\text{Zeros: } N(s) = 0 \qquad \text{Poles: } D(s) = 0$$

### Value Theorems
$$f(0^+) = \lim_{s \to \infty} sF(s) \quad \text{(PRF only)}$$
$$f(\infty) = \lim_{s \to 0} sF(s) \quad \text{(stable only)}$$

### Cover-Up Method
$$k_i = \left[(s-p_i)F(s)\right]_{s=p_i}$$

### Complex Pole Response
$$\text{Poles at } s = -\alpha \pm j\beta \implies f(t) = 2|k|e^{-\alpha t}\cos(\beta t + \angle k)u(t)$$

### Differentiation Property
$$\mathcal{L}\left\{\frac{df}{dt}\right\} = sF(s) - f(0^-)$$

---

## 12. Analysis Workflow Summary

**Circuit → Network Function:**
1. Transform to s-domain
2. Zero ICs
3. Circuit analysis
4. Form $H(s) = \frac{\text{Out}}{\text{In}}$

**H(s) → Poles/Zeros:**
1. Express as $\frac{N(s)}{D(s)}$
2. $N(s) = 0$ → zeros
3. $D(s) = 0$ → poles

**s-Domain → Time Domain:**
1. Check PRF/IRF
2. Factor denominator
3. Setup PFE
4. Find residues (cover-up)
5. Inverse transform
6. Add $u(t)$

**H(s) → Differential Equation:**
1. Cross-multiply
2. Replace $s \to \frac{d}{dt}$
3. Write ODE

**System Stability:**
- Check all poles
- All $\text{Re}(s) < 0$ → Stable
- Any $\text{Re}(s) \geq 0$ → Unstable