# Comprehensive Poles and Zeros Study Guide

## Part 1: Foundation - ZSR, ZIR, and Network Functions

### Zero-Input Response (ZIR)
The **ZIR** represents what your circuit does based purely on **stored energy**.

- **What it is:** Response with NO external input sources
- **Caused by:** Initial conditions (capacitor voltage V_c(0), inductor current I_L(0))
- **In time domain:** This is the **natural response** - the circuit "ringing" due to stored energy
- **Key insight:** ZIR exists even after you turn off all sources

### Zero-State Response (ZSR)
The **ZSR** represents what your circuit does based purely on **external inputs**.

- **What it is:** Response with NO initial stored energy (all initial conditions = 0)
- **Caused by:** External voltage/current sources
- **Key insight:** ZSR assumes the circuit starts from a "blank slate"

### Total Response = ZIR + ZSR
By **superposition**, the complete circuit response is:
```
Total Response = ZIR + ZSR
```

### Network Functions H(s)
The **network function** is the mathematical DNA of your circuit in the s-domain.

**Definition:**
```
H(s) = Output(s) / Input(s)     [with all initial conditions = 0]
```

**Critical Points:**
- H(s) ONLY describes the ZSR (zero-state response)
- Must set all initial conditions to zero when finding H(s)
- Relates output to input in frequency domain

**Types of Network Functions:**

1. **Transfer Function H(s) or T(s)**
   - Input and output at DIFFERENT ports
   - Example: V_out(s) / V_in(s)

2. **Driving-Point Impedance Z(s)**
   - Measured at SAME port: V(s) / I(s)

3. **Driving-Point Admittance Y(s)**
   - Measured at SAME port: I(s) / V(s)
   - Y(s) = 1/Z(s)

---

## Part 2: What Are Poles and Zeros?

### Network Function as Rational Function
Every network function can be written as:

```
H(s) = N(s) / D(s)
```

Where:
- N(s) = Numerator polynomial
- D(s) = Denominator polynomial

### POLES: The Circuit's Natural Frequencies

**Definition:** Poles are the roots of the denominator: **D(s) = 0**

**Why "poles"?** At these values of s, H(s) → ∞ (the function "blows up")

**What poles tell you:**

1. **In s-domain:** 
   - Locations where H(s) becomes infinite
   - Also called "natural frequencies" or "characteristic roots"

2. **In time domain:**
   - Determine the **natural response** modes
   - Each pole creates an exponential term in the output
   - Real pole at s = -α → term like: k·e^(-αt)
   - Complex poles at s = -α ± jω_d → damped sinusoid: k·e^(-αt)·cos(ω_d·t + φ)

3. **In differential equations:**
   - Poles come from the **OUTPUT side** (left side) of the ODE
   - The characteristic equation D(s) = 0 gives you the poles

4. **Physical meaning:**
   - Poles represent modes that are **always present** in the output
   - Even if your input doesn't contain these frequencies, they'll appear in the response
   - **Special case:** If input frequency = pole frequency, you get resonance (term becomes t·e^(s_0·t))

### ZEROS: The Circuit's Blocking Frequencies

**Definition:** Zeros are the roots of the numerator: **N(s) = 0**

**Why "zeros"?** At these values of s, H(s) = 0 (the function becomes zero)

**What zeros tell you:**

1. **In s-domain:**
   - Locations where H(s) = 0

2. **In time domain:**
   - Determine which frequencies are **blocked** from appearing in output
   - If input contains e^(z_i·t) where z_i is a zero, that term is **completely eliminated** from output

3. **In differential equations:**
   - Zeros come from the **INPUT side** (right side) of the ODE

4. **Physical meaning:**
   - Zeros act as "blockers" - they prevent certain input frequencies from reaching the output
   - Like a notch filter that kills specific frequencies

### Quick Reference Table

| Property | Poles | Zeros |
|----------|-------|-------|
| **Math** | Roots of D(s) = 0 | Roots of N(s) = 0 |
| **H(s) value** | H(s) → ∞ | H(s) = 0 |
| **ODE side** | Output (left) | Input (right) |
| **Time domain** | Always in output | Never in output |
| **Circuit property** | Natural modes | Blocked frequencies |

---

## Part 3: Master Decision Tree - Problem Solving Strategy

```mermaid
flowchart TD
    Start([Start: Given Problem])
    Q1{What are you given?}
    
    Start --> Q1
    
    Q1 -->|Circuit Diagram| Path1[Path A: Circuit Analysis]
    Q1 -->|Network Function| Path2[Path B: From H-s]
    Q1 -->|Differential Equation| Path3[Path C: From ODE]
    
    Path1 --> Q2{What do you need to find?}
    
    Q2 -->|H-s| A1[Follow Part 4: Circuit to H-s]
    Q2 -->|Poles and Zeros| A2[First get H-s then Part 5]
    Q2 -->|Time Response| A3[Get H-s then Part 7: ILT Method]
    Q2 -->|Differential Equation| A4[First get H-s then Part 6B]
    
    Path2 --> Q3{What do you need?}
    
    Q3 -->|Poles and Zeros| B1[Follow Part 5: Find Poles and Zeros]
    Q3 -->|Differential Equation| B2[Follow Part 6B: H-s to ODE]
    Q3 -->|Time Response| B3[Follow Part 7: ILT Method]
    
    Path3 --> Q4{What do you need?}
    
    Q4 -->|H-s| C1[Laplace transform both sides solve for Output over Input]
    Q4 -->|Poles and Zeros| C2[Get H-s first then Part 5]
    Q4 -->|Time Response| C3[Solve ODE via Laplace method]
    
    A1 --> Done1[Solution Complete]
    A2 --> Done1
    A3 --> Done1
    A4 --> Done1
    B1 --> Done1
    B2 --> Done1
    B3 --> Done1
    C1 --> Done1
    C2 --> Done1
    C3 --> Done1
```

---

## Part 4: Step-by-Step Process to Find H(s) from Circuit

```mermaid
flowchart TD
    Start([Given: Circuit Diagram])
    Step1[Step 1: Transform to s-Domain]
    Detail1[R remains R, C becomes 1 over sC, L becomes sL]
    Step2[Step 2: Zero Initial Conditions]
    Detail2[CRITICAL: Set all ICs to zero, Voltage sources become Short, Current sources become Open]
    Step3[Step 3: Define Input and Output]
    Detail3[Identify Input and Output variables]
    Step4[Step 4: Circuit Analysis]
    Q1{Which technique is easiest?}
    T1[Combine impedances]
    T2[Voltage or Current divider]
    T3[Nodal or Mesh analysis]
    Step5[Step 5: Form H-s]
    Detail5[H-s equals Output over Input]
    Step6[Step 6: Simplify to Rational Form]
    Detail6[H-s equals N-s over D-s]
    End([H-s Found Ready for Part 5])
    
    Start --> Step1
    Step1 --> Detail1
    Detail1 --> Step2
    Step2 --> Detail2
    Detail2 --> Step3
    Step3 --> Detail3
    Detail3 --> Step4
    Step4 --> Q1
    Q1 -->|Series or Parallel| T1
    Q1 -->|Two elements| T2
    Q1 -->|Complex circuit| T3
    T1 --> Step5
    T2 --> Step5
    T3 --> Step5
    Step5 --> Detail5
    Detail5 --> Step6
    Step6 --> Detail6
    Detail6 --> End
```

### Process Overview
```
Time-domain circuit → s-domain circuit → H(s) → Poles & Zeros
```

### Detailed Steps

**Step 1: Transform Circuit to s-Domain**

Convert each element to its s-domain impedance:
- **Resistor R** → Z = R
- **Capacitor C** → Z = 1/(sC)
- **Inductor L** → Z = sL

**Step 2: Zero All Initial Conditions**

This is CRITICAL for finding H(s):
- Voltage sources (including initial condition sources) → **short circuits**
- Current sources → **open circuits**
- This ensures H(s) represents only the ZSR

**Step 3: Define Input and Output**

Identify:
- Input variable: V_in(s) or I_in(s)
- Output variable: V_out(s) or I_out(s)

**Step 4: Analyze the s-Domain Circuit**

Use standard resistive circuit techniques:
- Voltage divider
- Current divider
- Nodal analysis (KCL)
- Mesh analysis (KVL)
- Source transformations
- Series/parallel combinations

**Step 5: Form H(s)**

Calculate:
```
H(s) = Output(s) / Input(s)
```

**Step 6: Simplify to Rational Form**

Express as:
```
H(s) = (a_m·s^m + a_(m-1)·s^(m-1) + ... + a_0) / (b_n·s^n + b_(n-1)·s^(n-1) + ... + b_0)
```

Factor if possible to show poles and zeros explicitly:
```
H(s) = K · (s - z_1)(s - z_2)...(s - z_m) / (s - p_1)(s - p_2)...(s - p_n)
```

---

## Part 5: Step-by-Step Process to Find Poles and Zeros

```mermaid
flowchart TD
    Start([Given: H-s equals N-s over D-s])
    Split{Find which?}
    Z1[Step 1: Identify N-s]
    P1[Step 1: Identify D-s]
    Both[Do both paths]
    Z2[Step 2: Set N-s equals 0]
    Z3[Step 3: Solve for s]
    ZQ{Polynomial order?}
    ZS1[s equals negative b over a]
    ZS2[Use quadratic formula]
    ZS3[Factor or use numerical methods]
    ZEnd[Zeros Found]
    P2[Step 2: Set D-s equals 0 - Characteristic Equation]
    P3[Step 3: Solve for s]
    PQ{Polynomial order?}
    PS1[s equals negative b over a]
    PS2[Use quadratic formula Check discriminant]
    PS3[Factor or use numerical methods]
    PEnd[Poles Found]
    PCheck{Discriminant b squared minus 4ac}
    Real[Two real poles]
    Repeated[Repeated real pole]
    Complex[Complex conjugate pair s equals negative alpha plus or minus j omega]
    Final([Solution Complete])
    
    Start --> Split
    Split -->|Zeros| Z1
    Split -->|Poles| P1
    Split -->|Both| Both
    Both --> Z1
    Both --> P1
    Z1 --> Z2
    Z2 --> Z3
    Z3 --> ZQ
    ZQ -->|1st order| ZS1
    ZQ -->|2nd order| ZS2
    ZQ -->|Higher order| ZS3
    ZS1 --> ZEnd
    ZS2 --> ZEnd
    ZS3 --> ZEnd
    P1 --> P2
    P2 --> P3
    P3 --> PQ
    PQ -->|1st order| PS1
    PQ -->|2nd order| PS2
    PQ -->|Higher order| PS3
    PS1 --> PEnd
    PS2 --> PCheck
    PS3 --> PEnd
    PCheck -->|Greater than 0| Real
    PCheck -->|Equals 0| Repeated
    PCheck -->|Less than 0| Complex
    Real --> PEnd
    Repeated --> PEnd
    Complex --> PEnd
    ZEnd --> Final
    PEnd --> Final
```

Once you have H(s) = N(s)/D(s):

### Finding Zeros

**Step 1:** Identify the numerator polynomial N(s)

**Step 2:** Set N(s) = 0

**Step 3:** Solve for s
- Factor if possible
- Use quadratic formula for 2nd order
- Use numerical methods for higher orders

**Example:**
```
If N(s) = s² + 3s + 2
Then: s² + 3s + 2 = 0
      (s + 1)(s + 2) = 0
Zeros: s = -1, s = -2
```

### Finding Poles

**Step 1:** Identify the denominator polynomial D(s)

**Step 2:** Set D(s) = 0 (this is the **characteristic equation**)

**Step 3:** Solve for s
- Same techniques as for zeros

**Example:**
```
If D(s) = s² + 4s + 13
Then: s² + 4s + 13 = 0

Using quadratic formula:
s = (-4 ± √(16 - 52)) / 2
s = (-4 ± √(-36)) / 2
s = (-4 ± j6) / 2
s = -2 ± j3

Poles: s = -2 + j3, s = -2 - j3 (complex conjugate pair)
```

### Types of Poles and Their Time-Domain Responses

```mermaid
flowchart TD
    Start([Pole Type])
    Q{Pole location?}
    R1[Time response: k times e to the negative alpha t - Decaying exponential]
    R2[Time response: k times e to the positive alpha t - Growing exponential - UNSTABLE]
    R3[Time response: k times u-t - Step function - Integrator]
    C1{Sign of alpha?}
    I1[Time response: k times cosine omega zero t plus phi - Sustained oscillation - Marginally stable]
    C2[k times e to negative alpha t times cosine omega d t plus phi - Damped oscillation - Stable]
    C3[k times e to positive alpha t times cosine omega d t plus phi - Growing oscillation - UNSTABLE]
    End1[Stable]
    End2[Unstable]
    End3[Marginally Stable]
    
    Start --> Q
    Q -->|Real negative s equals negative alpha where alpha greater than 0| R1
    Q -->|Real positive s equals positive alpha| R2
    Q -->|At origin s equals 0| R3
    Q -->|Complex conjugate s equals negative alpha plus or minus j omega d| C1
    Q -->|Imaginary s equals plus or minus j omega zero| I1
    C1 -->|alpha greater than 0| C2
    C1 -->|alpha less than 0| C3
    C1 -->|alpha equals 0| I1
    R1 --> End1
    R2 --> End2
    R3 --> End3
    C2 --> End1
    C3 --> End2
    I1 --> End3
```

**Key Points:**

1. **Real, negative pole (s = -α, α > 0)**
   - Time response: k·e^(-αt) → decaying exponential
   - Stable

2. **Real, positive pole (s = +α)**
   - Time response: k·e^(+αt) → growing exponential
   - **UNSTABLE**

3. **Complex conjugate pair (s = -α ± jω_d)**
   - Time response: k·e^(-αt)·cos(ω_d·t + φ)
   - Damped oscillation if α > 0
   - Growing oscillation if α < 0 (unstable)

4. **Imaginary poles (s = ±jω_0)**
   - Time response: k·cos(ω_0·t + φ)
   - Sustained oscillation (marginally stable)

5. **Pole at origin (s = 0)**
   - Time response: k·u(t) → step function
   - Indicates integrator in system

---

## Part 6: Creating Differential Equations from Circuits

```mermaid
flowchart TD
    Start([Need: Differential Equation])
    Q{What do you have?}
    MethodA[Method A: Direct Time-Domain Analysis]
    MethodB[Method B: From H-s - EASIER]
    A1[Step 1: Write KCL or KVL in time domain]
    A2[Step 2: Use element relations]
    A3[Step 3: Combine to get ODE relating input to output]
    A4[Step 4: Solve via Laplace transform if needed]
    B1[Step 1: Start with H-s equals N-s over D-s]
    B2[Step 2: Cross-multiply Output times D-s equals Input times N-s]
    B3[Step 3: Replace s with d over dt]
    B4[Step 4: Write the ODE]
    Key[KEY INSIGHT: Denominator D-s poles goes to Output side LEFT - Numerator N-s zeros goes to Input side RIGHT]
    End([ODE Found])
    
    Start --> Q
    Q -->|Circuit diagram| MethodA
    Q -->|Network function H-s| MethodB
    MethodA --> A1
    A1 --> A2
    A2 --> A3
    A3 --> A4
    MethodB --> B1
    B1 --> B2
    B2 --> B3
    B3 --> B4
    B4 --> Key
    A4 --> End
    Key --> End
```

### Method A: Direct Time-Domain Analysis

**Step 1:** Write KCL/KVL equations in time domain

**Step 2:** Use element relationships:
- Resistor: v = R·i
- Capacitor: i = C·(dv/dt) or v = (1/C)·∫i dt
- Inductor: v = L·(di/dt) or i = (1/L)·∫v dt

**Step 3:** Combine to get ODE relating input to output

**Step 4:** Solve via Laplace transform:
- Transform ODE to s-domain
- Solve algebraically
- Inverse transform back

### Method B: From Network Function (EASIER!)

If you already have H(s), you can directly write the ODE:

**Step 1:** Start with H(s) in polynomial form
```
H(s) = V_out(s)/V_in(s) = N(s)/D(s)
```

**Step 2:** Cross-multiply
```
V_out(s)·D(s) = V_in(s)·N(s)
```

**Step 3:** Interpret s as the derivative operator d/dt
- s → d/dt
- s² → d²/dt²
- s³ → d³/dt³, etc.

**Step 4:** Write the ODE

**Example:**
```
Given: H(s) = (2s + 3) / (s² + 5s + 6)

Cross-multiply:
V_out(s)·(s² + 5s + 6) = V_in(s)·(2s + 3)

Replace s with d/dt:
(d²/dt² + 5·d/dt + 6)·v_out(t) = (2·d/dt + 3)·v_in(t)

Final ODE:
d²v_out/dt² + 5·dv_out/dt + 6·v_out = 2·dv_in/dt + 3·v_in
```

**Key Insight:**
- **Denominator coefficients (poles)** → output side (left)
- **Numerator coefficients (zeros)** → input side (right)

---

## Part 7: Time-Domain Response via Inverse Laplace Transform

```mermaid
flowchart TD
    Start([Given: H-s and Input V in-s])
    Step1[Step 1: Find V out-s equals H-s times V in-s]
    Step2[Step 2: Factor Denominator Find ALL poles]
    Identify[Identify pole sources: Poles from H-s gives Natural response - Poles from V in-s gives Forced response]
    Step3[Step 3: Partial Fraction Expansion PFE]
    PFE[V out-s equals k zero over s minus p zero plus k one over s minus p one plus dot dot dot]
    Step4[Step 4: Find Residues]
    Q{Pole type?}
    Simple[Cover-Up Method: k i equals s minus p i times V out-s evaluated at s equals p i]
    Complex[Both residues will be complex conjugates Use cover-up on each]
    Repeated[Use special methods derivatives of cover-up]
    Step5[Step 5: Inverse Transform Each Term]
    Transform[k i over s minus p i transforms to k i times e to p i t times u-t]
    Special{Special cases?}
    SC[Combine conjugate pairs: 2 magnitude k times e to negative alpha t times cosine omega d t plus angle k times u-t]
    SR[Direct transform: k times e to pt times u-t]
    Step6[Step 6: Combine All Terms v out-t equals Sum of all transformed terms]
    Classify[Classify response: Terms from H-s poles equals Natural - Terms from V in-s poles equals Forced]
    End([Time Response Found])
    
    Start --> Step1
    Step1 --> Step2
    Step2 --> Identify
    Identify --> Step3
    Step3 --> PFE
    PFE --> Step4
    Step4 --> Q
    Q -->|Simple pole| Simple
    Q -->|Complex conjugate| Complex
    Q -->|Repeated pole| Repeated
    Simple --> Step5
    Complex --> Step5
    Repeated --> Step5
    Step5 --> Transform
    Transform --> Special
    Special -->|Complex poles s equals negative alpha plus or minus j omega d| SC
    Special -->|Real poles| SR
    SC --> Step6
    SR --> Step6
    Step6 --> Classify
    Classify --> End
```

### The Big Picture

When you have:
```
V_out(s) = H(s)·V_in(s)
```

The time response v_out(t) contains TWO types of terms:

1. **Natural Response** → from poles of H(s)
2. **Forced Response** → from poles of V_in(s)

### Step-by-Step ILT Process

**Step 1: Find V_out(s)**
```
V_out(s) = H(s)·V_in(s)
```

**Step 2: Factor the Denominator**

Factor completely to find ALL poles:
- Poles from H(s) → natural response
- Poles from V_in(s) → forced response

**Step 3: Partial Fraction Expansion (PFE)**

Decompose into simple terms:
```
V_out(s) = k_0/(s - p_0) + k_1/(s - p_1) + k_2/(s - p_2) + ...
```

**Step 4: Find Residues Using Cover-Up Method**

For simple pole at s = p_i:
```
k_i = [(s - p_i)·V_out(s)]|_(s=p_i)
```

Cover up the (s - p_i) term in V_out(s), then substitute s = p_i everywhere else.

**Step 5: Inverse Transform**

Each term transforms as:
```
k_i/(s - p_i) → k_i·e^(p_i·t)·u(t)
```

**Step 6: Combine Terms**
```
v_out(t) = k_0·e^(p_0·t) + k_1·e^(p_1·t) + k_2·e^(p_2·t) + ...
           [forced]        [natural response terms]
```

### Special Cases

**Complex Conjugate Poles (s = -α ± jω_d):**

If k and k* are conjugate residues:
```
k/(s - (-α + jω_d)) + k*/(s - (-α - jω_d))
```

Combines to give:
```
2|k|·e^(-αt)·cos(ω_d·t + ∠k)·u(t)
```

**Repeated Poles:**

For pole p_i with multiplicity n, use special techniques (not covered in detail here, but involves derivatives of the cover-up method).

### Understanding Natural vs Forced Response

```mermaid
flowchart LR
    Input[Input V in-s has poles]
    Forced[Forced Response Same shape as input Amplitude scaled by H-s]
    Network[Network H-s has poles]
    Natural[Natural Response Circuits own modes Independent of input]
    Output[Total Output v out-t]
    Special[Special Case: Input frequency equals H-s pole]
    Resonance[Resonance Output term: t times e to s zero t]
    
    Input --> Forced
    Network --> Natural
    Forced --> Output
    Natural --> Output
    Special --> Resonance
```

**Forced Response:**
- Comes from input poles
- Has same "shape" as input
- Amplitude scaled by H(s) evaluated at input frequency
- If v_in(t) = K·e^(s_0·t)·u(t), then forced term = K·H(s_0)·e^(s_0·t)

**Natural Response:**
- Comes from H(s) poles
- Independent of input type
- Determined by circuit elements (R, L, C)
- Same modes appear in ZIR (zero-input response)

**Key Insight:** If input frequency matches a pole of H(s), you get **resonance** - the output term becomes t·e^(s_0·t) (grows with time).

---

## Part 8: Common Mistakes to Avoid

```mermaid
flowchart TD
    Start([Common Pitfalls])
    M1[Mistake 1: Forgetting to zero ICs when finding H-s]
    Fix1[Fix: Always set V c zero equals 0 and I L zero equals 0 for H-s - H-s only describes ZSR]
    M2[Mistake 2: Confusing poles and zeros]
    Fix2[Fix: Poles equals D-s equals 0 denominator - Zeros equals N-s equals 0 numerator]
    M3[Mistake 3: Wrong impedance conversions]
    Fix3[Fix: C is 1 over sC NOT sC - L is sL NOT 1 over sL]
    M4[Mistake 4: Not factoring completely]
    Fix4[Fix: Find ALL poles and zeros - Complex poles come in conjugate pairs]
    M5[Mistake 5: Forgetting u-t in time domain]
    Fix5[Fix: 1 over s minus a transforms to e to at times u-t NOT just e to at]
    M6[Mistake 6: Mixing up natural vs forced]
    Fix6[Fix: Natural equals H-s poles - Forced equals Input poles]
    M7[Mistake 7: Missing resonance case]
    Fix7[Fix: When input frequency equals pole of H-s special case - Term becomes t times e to s zero t]
    End([Stay Alert])
    
    Start --> M1
    M1 --> Fix1
    Fix1 --> M2
    M2 --> Fix2
    Fix2 --> M3
    M3 --> Fix3
    Fix3 --> M4
    M4 --> Fix4
    Fix4 --> M5
    M5 --> Fix5
    Fix5 --> M6
    M6 --> Fix6
    Fix6 --> M7
    M7 --> Fix7
    Fix7 --> End
```

1. **Forgetting to zero initial conditions when finding H(s)**
   - H(s) ONLY represents ZSR
   - Must set V_c(0) = 0 and I_L(0) = 0

2. **Confusing poles and zeros**
   - Poles = denominator roots (D(s) = 0)
   - Zeros = numerator roots (N(s) = 0)

3. **Not factoring completely**
   - Must find ALL poles and zeros
   - Complex poles come in conjugate pairs

4. **Wrong impedance conversions**
   - Capacitor: 1/(sC) not sC
   - Inductor: sL not 1/(sL)

5. **Forgetting unit step u(t) in time domain**
   - ILT of 1/(s-a) is e^(at)·u(t), not just e^(at)

6. **Mixing up which response is which**
   - Natural response = from H(s) poles
   - Forced response = from input poles

7. **Not recognizing resonance**
   - When input frequency = pole of H(s), special case occurs

---

## Part 9: Quick Reference Formulas

### s-Domain Impedances
```
Z_R = R
Z_C = 1/(sC)
Z_L = sL
```

### Network Function
```
H(s) = N(s)/D(s) = Output(s)/Input(s)  [with ICs = 0]
```

### Finding Poles and Zeros
```
Zeros: N(s) = 0
Poles: D(s) = 0  [characteristic equation]
```

### Differential Equation from H(s)
```
If H(s) = N(s)/D(s)
Then: D(d/dt)·y(t) = N(d/dt)·x(t)
```

### Common Laplace Pairs
```
u(t) ↔ 1/s
e^(at)·u(t) ↔ 1/(s-a)
t·e^(at)·u(t) ↔ 1/(s-a)²
cos(ωt)·u(t) ↔ s/(s² + ω²)
sin(ωt)·u(t) ↔ ω/(s² + ω²)
e^(-αt)·cos(ωt)·u(t) ↔ (s+α)/((s+α)² + ω²)
```

### Cover-Up Method (Simple Poles)
```
k_i = [(s - p_i)·V_out(s)]|_(s=p_i)
```

---

## Part 10: Practice Problem Workflow

```mermaid
flowchart TD
    Start([Example: RC Low-Pass Filter - V in to R to C to V out])
    Goal[Goal: Find H-s poles zeros and diff eq]
    S1[Step 1: s-Domain Transform - Z R equals R - Z C equals 1 over sC]
    S2[Step 2: Voltage Divider - H-s equals Z C over Z R plus Z C]
    S3[Step 3: Substitute - H-s equals 1 over sC divided by R plus 1 over sC]
    S4[Step 4: Simplify - Multiply top and bottom by sC]
    Result1[H-s equals 1 over 1 plus sRC equals 1 over RC divided by s plus 1 over RC]
    FindPZ[Find Poles and Zeros]
    Num[Numerator: N-s equals 1 over RC constant]
    Z[No finite zeros cannot equal 0]
    Den[Denominator: D-s equals s plus 1 over RC]
    P[Set s plus 1 over RC equals 0 - Pole: s equals negative 1 over RC]
    PZDone[Pole at s equals negative 1 over RC - No finite zeros]
    DiffEq[Create Differential Equation]
    Cross[Cross-multiply: V out-s times s plus 1 over RC equals V in-s times 1 over RC]
    Replace[Replace s with d over dt]
    ODE[dv out over dt plus v out over RC equals v in over RC]
    TimeResp[Find Time Response to step input: v in equals u-t]
    VinS[V in-s equals 1 over s]
    VoutS[V out-s equals H-s times V in-s equals 1 over RC divided by s plus 1 over RC times 1 over s]
    PFE[Partial Fractions: V out-s equals A over s plus B over s plus 1 over RC]
    CoverUp[Cover-up method: A equals 1 - B equals negative 1]
    ILT[Inverse Laplace: v out-t equals 1 minus e to negative t over RC]
    Final[Final: v out-t equals 1 minus e to negative t over RC times u-t - Natural response: negative e to negative t over RC from H-s pole - Forced response: 1 from input pole at s equals 0]
    Complete([Complete Solution])
    
    Start --> Goal
    Goal --> S1
    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> Result1
    Result1 --> FindPZ
    FindPZ --> Num
    FindPZ --> Den
    Num --> Z
    Den --> P
    Z --> PZDone
    P --> PZDone
    PZDone --> DiffEq
    DiffEq --> Cross
    Cross --> Replace
    Replace --> ODE
    ODE --> TimeResp
    TimeResp --> VinS
    VinS --> VoutS
    VoutS --> PFE
    PFE --> CoverUp
    CoverUp --> ILT
    ILT --> Final
    Final --> Complete
```

**Example Circuit: RC Low-Pass Filter**

Given: Input v_in, output v_out across capacitor, R and C in series.

**Find H(s), poles, zeros, and differential equation:**

**Solution:**

1. **s-domain circuit:**
   - Z_R = R
   - Z_C = 1/(sC)

2. **Voltage divider:**
   ```
   H(s) = V_out(s)/V_in(s) = Z_C/(Z_R + Z_C)
   H(s) = [1/(sC)] / [R + 1/(sC)]
   H(s) = 1 / (1 + sRC)
   H(s) = 1/(RC) / (s + 1/(RC))
   ```

3. **Poles and zeros:**
   ```
   N(s) = 1/(RC) → No finite zeros
   D(s) = s + 1/(RC) = 0
   Pole: s = -1/(RC)
   ```

4. **Differential equation:**
   ```
   Cross-multiply: V_out(s)·(s + 1/(RC)) = V_in(s)·(1/(RC))
   
   Replace s → d/dt:
   (d/dt + 1/(RC))·v_out = (1/(RC))·v_in
   
   dv_out/dt + v_out/(RC) = v_in/(RC)
   ```

5. **Time response to step input (v_in = u(t)):**
   ```
   V_in(s) = 1/s
   V_out(s) = H(s)·V_in(s) = [1/(RC)]/[(s + 1/(RC))·s]
   
   PFE: V_out(s) = 1/s - 1/(s + 1/(RC))
   
   v_out(t) = [1 - e^(-t/(RC))]·u(t)
   ```

---

## Part 11: Quiz Preparation Checklist

```mermaid
flowchart TD
    Start([Quiz Day Preparation])
    C1{Can you do this?}
    T1[Transform R L C to s-domain]
    Study1[Review Part 4]
    C2{Can you do this?}
    T2[Find H-s from circuit using circuit analysis]
    Study2[Review Part 4]
    C3{Can you do this?}
    T3[Find poles: set D-s equals 0 - Find zeros: set N-s equals 0]
    Study3[Review Part 5]
    C4{Can you do this?}
    T4[Write diff eq from H-s by cross-multiplying]
    Study4[Review Part 6]
    C5{Can you do this?}
    T5[Do partial fraction expansion]
    Study5[Review Part 7]
    C6{Can you do this?}
    T6[Use cover-up method for residues]
    Study6[Review Part 7]
    C7{Can you do this?}
    T7[Inverse Laplace transform each term]
    Study7[Review Part 7]
    C8{Do you understand?}
    T8[Distinguish natural vs forced response]
    Study8[Review Part 2 and 7]
    C9{Do you remember?}
    T9[Zero ICs when finding H-s]
    Study9[Review Part 1 and 4]
    C10{Can you recognize?}
    T10[Different pole types and their time responses]
    Study10[Review Part 5]
    Ready[READY FOR QUIZ]
    
    Start --> C1
    C1 -->|Yes| T1
    C1 -->|No| Study1
    T1 --> C2
    C2 -->|Yes| T2
    C2 -->|No| Study2
    T2 --> C3
    C3 -->|Yes| T3
    C3 -->|No| Study3
    T3 --> C4
    C4 -->|Yes| T4
    C4 -->|No| Study4
    T4 --> C5
    C5 -->|Yes| T5
    C5 -->|No| Study5
    T5 --> C6
    C6 -->|Yes| T6
    C6 -->|No| Study6
    T6 --> C7
    C7 -->|Yes| T7
    C7 -->|No| Study7
    T7 --> C8
    C8 -->|Yes| T8
    C8 -->|No| Study8
    T8 --> C9
    C9 -->|Yes| T9
    C9 -->|No| Study9
    T9 --> C10
    C10 -->|Yes| T10
    C10 -->|No| Study10
    T10 --> Ready
    Study1 --> C1
    Study2 --> C2
    Study3 --> C3
    Study4 --> C4
    Study5 --> C5
    Study6 --> C6
    Study7 --> C7
    Study8 --> C8
    Study9 --> C9
    Study10 --> C10
```

### Essential Skills Checklist

**Before the quiz, make sure you can:**

✓ **Transform circuits to s-domain**
- R → R
- C → 1/(sC)
- L → sL

✓ **Find H(s) from circuits**
- Zero all initial conditions first!
- Use voltage/current dividers or nodal/mesh analysis
- Express as rational function N(s)/D(s)

✓ **Find poles and zeros**
- Poles: solve D(s) = 0
- Zeros: solve N(s) = 0
- Use quadratic formula for 2nd order

✓ **Write differential equations from H(s)**
- Cross-multiply: Output(s)·D(s) = Input(s)·N(s)
- Replace s with d/dt
- Poles → output side, Zeros → input side

✓ **Perform partial fraction expansion**
- Factor denominator completely
- Set up PFE with one term per pole
- Use cover-up method for residues

✓ **Inverse Laplace transform**
- k/(s-p) → k·e^(pt)·u(t)
- Handle complex conjugate pairs properly
- Combine to get natural + forced response

✓ **Conceptual understanding**
- H(s) only describes ZSR (zero initial conditions)
- Poles = always in output (natural response)
- Zeros = never in output (blocked frequencies)
- Natural response from H(s) poles
- Forced response from input poles

---

## Part 12: Key Conceptual Questions for Understanding

```mermaid
flowchart TD
    Q1[Q: Why do we zero initial conditions for H-s?]
    A1[A: H-s only describes ZSR zero-state response - ICs would add ZIR component]
    Q2[Q: What is the difference between poles and zeros?]
    A2[A: Poles from D-s equals 0 always in output - Zeros from N-s equals 0 blocked from output]
    Q3[Q: Why do complex poles come in conjugate pairs?]
    A3[A: Real circuits have real coefficients - Complex roots of real polynomials must be conjugate pairs]
    Q4[Q: What does a pole at origin s equals 0 mean?]
    A4[A: Integrator in system - Step response in time domain - DC gain is infinite]
    Q5[Q: What happens when input frequency equals pole of H-s?]
    A5[A: RESONANCE - Output grows as t times e to s zero t - System is driven at natural frequency]
    Q6[Q: How do you identify natural vs forced response?]
    A6[A: Natural from H-s poles - Forced from input poles - Check which pole each term came from]
    Q7[Q: What makes a system unstable?]
    A7[A: Poles in right half-plane positive real part - Leads to growing exponentials]
    Q8[Q: Why is the characteristic equation important?]
    A8[A: D-s equals 0 gives the poles - Poles determine natural response - Same for ZIR and ZSR natural modes]
    
    Q1 --> A1
    Q2 --> A2
    Q3 --> A3
    Q4 --> A4
    Q5 --> A5
    Q6 --> A6
    Q7 --> A7
    Q8 --> A8
```

### Think About These:

1. **Why zero initial conditions for H(s)?**
   - H(s) represents only the ZSR (zero-state response)
   - Initial conditions would add the ZIR component
   - We want the pure input-to-output relationship

2. **What's the physical meaning of a pole?**
   - A natural frequency of the circuit
   - Will appear in output even if not in input
   - Determined by circuit elements (R, L, C values)

3. **What's the physical meaning of a zero?**
   - A frequency that gets blocked/cancelled
   - If input contains this frequency, it won't reach output
   - Like a notch filter

4. **Why do complex poles always come in conjugate pairs?**
   - Real circuits have real-valued components
   - Polynomials with real coefficients have conjugate complex roots
   - Ensures time-domain response is real

5. **What happens at resonance?**
   - Input frequency matches a pole of H(s)
   - Normal exponential becomes t·e^(st)
   - Output grows without bound (in theory)

---

## Part 13: Final Tips for Quiz Success

### Time Management Strategy

```mermaid
flowchart LR
    Read[1. Read problem carefully 1 min]
    Identify[2. Identify what is given and what is asked 1 min]
    Plan[3. Choose method Circuit to H-s to poles or zeros 30 sec]
    Execute[4. Execute solution Show all steps 5-8 min]
    Check[5. Check answer Units? Reasonable? 1 min]
    
    Read --> Identify
    Identify --> Plan
    Plan --> Execute
    Execute --> Check
```

### During the Quiz:

1. **Read carefully** - What's given? What do they want?

2. **Write down knowns** - Circuit values, initial conditions, input type

3. **Choose your path** - Use the decision tree from Part 3

4. **Show all work** - Partial credit is your friend!

5. **Check units** - Does s = -5 rad/s make sense?

6. **Verify stability** - Are poles in left half-plane?

7. **Double-check signs** - Especially negative signs in exponentials

### Common Quiz Question Types:

- **Type 1:** Given circuit → Find H(s)
- **Type 2:** Given H(s) → Find poles/zeros
- **Type 3:** Given circuit + input → Find v_out(t)
- **Type 4:** Given H(s) → Write differential equation
- **Type 5:** Given poles/zeros → Sketch time response

### Quick Mental Checks:

✓ Did I zero initial conditions for H(s)?
✓ Are my impedances correct? (1/sC not sC!)
✓ Did I factor completely?
✓ Does my answer make physical sense?
✓ Did I include u(t) in time-domain?

---

## Part 14: Summary - The Big Picture

```mermaid
flowchart TD
    Circuit[Circuit with R L C]
    Transform[Transform to s-Domain]
    Hs[Network Function H-s equals N-s over D-s]
    Split{What do you need?}
    PZ[Find roots: Poles D-s equals 0 - Zeros N-s equals 0]
    DE[Cross-multiply and replace s with d over dt]
    TR[V out-s equals H-s times V in-s Then PFE and ILT]
    Understand[Understanding: Poles gives Natural response - Zeros gives Blocked frequencies]
    Master[MASTERY: You can now analyze any linear circuit]
    
    Circuit --> Transform
    Transform --> Hs
    Hs --> Split
    Split -->|Poles and Zeros| PZ
    Split -->|Diff Eq| DE
    Split -->|Time Response| TR
    PZ --> Understand
    DE --> Understand
    TR --> Understand
    Understand --> Master
```

### Remember the Core Concepts:

1. **H(s) = N(s)/D(s)** is the heart of everything
2. **Poles (D(s) = 0)** → Natural modes, always present
3. **Zeros (N(s) = 0)** → Blocked frequencies, never in output
4. **Natural response** comes from H(s) poles
5. **Forced response** comes from input poles
6. **Always zero ICs** when finding H(s)

### The Complete Problem-Solving Framework:

**Path 1: Circuit → H(s) → Poles/Zeros**
1. Transform to s-domain (R, 1/sC, sL)
2. Zero initial conditions
3. Use circuit analysis to find H(s)
4. Find poles: D(s) = 0
5. Find zeros: N(s) = 0

**Path 2: H(s) → Differential Equation**
1. Start with H(s) = N(s)/D(s)
2. Cross-multiply
3. Replace s → d/dt
4. Write ODE (poles on output side, zeros on input side)

**Path 3: Circuit + Input → Time Response**
1. Find H(s) from circuit
2. Calculate V_out(s) = H(s)·V_in(s)
3. Partial fraction expansion
4. Cover-up method for residues
5. Inverse Laplace transform
6. Identify natural vs forced response

### You've Got This! 🎯

This guide covers everything you need. The Mermaid diagrams show you the decision-making process at each step. When you're stuck:
- Look at the master decision tree (Part 3)
- Follow the step-by-step flowcharts
- Check the common mistakes section
- Verify with the quiz preparation checklist

**Practice a few problems using these flowcharts, and you'll be ready!**

**Good luck on your quiz!**