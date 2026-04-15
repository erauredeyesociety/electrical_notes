# Chapter 20 — The Second Law of Thermodynamics

The first law of thermodynamics, $\Delta U = Q - W$, is a statement of conservation of energy. It does not, however, forbid heat from flowing spontaneously from a cold body to a warmer one. We need an additional principle — the **second law of thermodynamics** — to explain why heat should flow from hot to cold. In this chapter we introduce a new state variable, **entropy** $S$, whose change $\Delta S$ tells us unambiguously the direction of heat flow in a thermodynamic process.

## 1. Directions of Thermodynamic Processes

All thermodynamic processes that occur spontaneously in nature are **irreversible** — they proceed in one direction and never spontaneously in the other (e.g., heat flow from a hot body to a cold body).

We can imagine an idealized class of **reversible processes** in which the system is always arbitrarily close to thermodynamic equilibrium with its surroundings. Heat flow between two bodies whose temperatures differ only infinitesimally can be reversed by an infinitesimal change in either temperature. Reversible processes are also called **equilibrium processes**; they are an idealization that cannot be precisely attained, but a process can be made nearly reversible by keeping temperature and pressure gradients very small.

## 2. Heat Engines

A **heat engine** is any device that partly transforms heat into work or mechanical energy. The simplest analysis applies to a cyclic process, in which the working substance returns to its original state at the end of each cycle. A heat engine:

1. Absorbs heat $Q_H$ from a high-temperature reservoir.
2. Performs mechanical work $W$.
3. Rejects heat $|Q_C|$ to a low-temperature reservoir.

Because the substance returns to its initial state, $\Delta U = 0$ over one cycle, so the first law gives:
$$Q_{\text{net}} = W$$
$$W = Q_H + Q_C = |Q_H| - |Q_C|$$

(with the sign convention that heat absorbed is positive and heat rejected is negative).

The **thermal efficiency** of an engine is:
$$e = \frac{W}{Q_H} \tag{1}$$

### Example 1

A diesel engine performs 2200 J of mechanical work and discards 4300 J of heat each cycle.

(a) Heat supplied each cycle:
$$Q_H = W + |Q_C| = 2200 + 4300 = 6500 \text{ J}$$

(b) Efficiency:
$$e = W/Q_H = 2200/6500 \approx 0.338 = 33.8\%$$

### Example 34 (preview)

A heat engine takes 0.350 mol of a diatomic ideal gas around a cycle with $1 \to 2$ at constant volume, $2 \to 3$ adiabatic, and $3 \to 1$ at a constant pressure of 1.00 atm, with $\gamma = 1.40$. Find pressures, volumes, $Q$, $W$, and $\Delta U$ for each process; net work and net heat flow in one cycle; thermal efficiency; compare to a Carnot engine running between the same $T_{\min}$ and $T_{\max}$.

## 3. Internal-Combustion Engines

### 3.1 The Otto Cycle

The idealized gasoline-engine cycle has four strokes on a $pV$ diagram with compression ratio $r = V_{\max}/V_{\min}$:

- $a \to b$: adiabatic compression.
- $b \to c$: constant-volume heat input $Q_H$ (ignition).
- $c \to d$: adiabatic expansion (power stroke).
- $d \to a$: constant-volume heat rejection $|Q_C|$.

From Eq. (1):
$$e = \frac{W}{Q_H} = \frac{Q_H + Q_C}{Q_H} = 1 + \frac{Q_C}{Q_H} = 1 - \frac{T_d - T_a}{T_c - T_b}$$

On the adiabats:
$$V_c T_c^{\gamma-1} = (rV_c) T_d^{\gamma-1} \;\Rightarrow\; T_d = \frac{T_c}{r^{\gamma-1}}$$
$$V_b T_b^{\gamma-1} = (rV_b) T_a^{\gamma-1} \;\Rightarrow\; T_a = \frac{T_b}{r^{\gamma-1}}$$

Substituting:
$$\boxed{\; e = 1 - \frac{1}{r^{\gamma-1}} \;} \qquad \text{(Otto cycle)}$$

Typical $r \approx 8$ gives $e \approx 0.56$ (theoretical).

### Example 8

Otto cycle with $\gamma = 1.40$, $r = 9.50$:
$$e = 1 - \frac{1}{9.5^{0.4}} \approx 1 - 0.407 \approx 0.594$$

If $Q_H = 10{,}000$ J, heat discarded:
$$|Q_C| = (1 - e) Q_H \approx 0.406 \times 10{,}000 \approx 4060 \text{ J}$$

### 3.2 The Diesel Cycle

Similar in operation to the gasoline engine but there is no fuel in the cylinder during the compression stroke — so pre-ignition cannot occur and the compression ratio can be much higher. Typical $r$ in a Diesel engine is 15–20 and theoretical efficiencies range from 0.65 to 0.70.

## 4. Refrigerators

A refrigerator is a heat engine operating in reverse: it takes heat $|Q_C|$ from a cold place and ejects heat $|Q_H|$ to a warm place, requiring a work input. Conservation of energy:
$$W + |Q_C| = |Q_H| \quad\Longrightarrow\quad W = |Q_H| - |Q_C|$$

The **coefficient of performance** (COP) is:
$$K = \frac{|Q_C|}{W} = \frac{|Q_C|}{|Q_H| - |Q_C|}$$

a dimensionless figure of merit — also called the **energy efficiency rating**. Larger $K$ means a more efficient refrigerator.

### Example 12

$K = 2.10$, $|Q_C| = 3.10 \times 10^4$ J per cycle.

(a) Mechanical work per cycle:
$$W = |Q_C|/K = 3.10\times10^4 / 2.10 \approx 1.48 \times 10^4 \text{ J}$$

(b) Heat discarded to high-temperature reservoir:
$$|Q_H| = |Q_C| + W \approx 3.10\times10^4 + 1.48\times10^4 \approx 4.58\times10^4 \text{ J}$$

## 5. The Second Law of Thermodynamics

Experimental evidence shows that it is impossible to build a 100% efficient heat engine. This is stated in the **second law of thermodynamics**:

> **(Engine form.)** It is impossible for any system to undergo a process in which it absorbs heat from a reservoir at a single temperature and converts the heat completely into mechanical work, with the system ending in the same state in which it began.
>
> **(Refrigerator form.)** It is impossible for any process to have as its sole result the transfer of heat from a cooler to a hotter body.

These two statements are logically equivalent: a violation of one could be combined with an ordinary engine/refrigerator to produce a violation of the other.

## 6. The Carnot Cycle

Sadi Carnot (1796–1832) devised a hypothetical, idealized, reversible heat engine achieving the maximum efficiency consistent with the second law between two reservoirs at $T_H$ and $T_C$. It consists of four reversible steps:

1. Isothermal expansion at $T_H$, absorbing $Q_H$ ($a \to b$).
2. Adiabatic expansion until temperature drops to $T_C$ ($b \to c$).
3. Isothermal compression at $T_C$, rejecting $|Q_C|$ ($c \to d$).
4. Adiabatic compression back to the initial state at $T_H$ ($d \to a$).

For the isothermal steps of an ideal gas:
$$Q_H = W_{ab} = nR T_H \ln\!\left(\frac{V_b}{V_a}\right)$$
$$Q_C = W_{cd} = nR T_C \ln\!\left(\frac{V_d}{V_c}\right) = -nR T_C \ln\!\left(\frac{V_c}{V_d}\right)$$

The efficiency:
$$e = \frac{W}{Q_H} = \frac{Q_H + Q_C}{Q_H} = 1 - \frac{T_C \ln(V_c/V_d)}{T_H \ln(V_b/V_a)} \tag{2}$$

For an adiabatic ideal-gas process, $TV^{\gamma-1} = \text{const}$, so:
$$b \to c: \quad T_C V_c^{\gamma-1} = T_H V_b^{\gamma-1}$$
$$d \to a: \quad T_C V_d^{\gamma-1} = T_H V_a^{\gamma-1}$$

Taking the ratio gives $V_c/V_d = V_b/V_a$. Substituting into Eq. (2):
$$\boxed{\; e_{\text{Carnot}} = 1 - \frac{T_C}{T_H} \;} \tag{3}$$

(temperatures in kelvins).

### Example 15

Carnot engine with $T_H = 620$ K takes in 550 J and rejects 335 J per cycle.

(a) Work done per cycle:
$$W = Q_H - |Q_C| = 550 - 335 = 215 \text{ J}$$

(b) Cold reservoir temperature. Using $|Q_C|/Q_H = T_C/T_H$:
$$T_C = T_H \frac{|Q_C|}{Q_H} = 620 \times \frac{335}{550} \approx 377.6 \text{ K}$$

(c) Thermal efficiency:
$$e = W/Q_H = 215/550 \approx 0.391 = 39.1\%$$

Check: $1 - T_C/T_H = 1 - 377.6/620 \approx 0.391$. 

## 7. Entropy

The second law as stated above is a statement of impossibility rather than an equation. To put it in quantitative form, introduce a new state variable — the **entropy** $S$.

### Isothermal Process

For an isothermal expansion of an ideal gas, $dU = 0$, so $dQ = dW = p\,dV = (nRT/V)\,dV$, and therefore:
$$nR \frac{dV}{V} = \frac{dQ}{T}$$

If we define the infinitesimal entropy change as:
$$\boxed{\; dS = \frac{dQ}{T} \;} \qquad [\text{J/K}] \tag{4}$$

then for an isothermal doubling of the volume, the entropy increases by $nR\ln 2$.

### Non-Isothermal Paths

For a finite reversible process on any thermodynamic path, integrate the infinitesimal entropy changes:
$$\Delta S = \int_{T_1}^{T_2} \frac{dQ}{T}$$

Since $S$ is a state function, $\Delta S$ depends only on the endpoints (but you must use a reversible path to evaluate the integral).

### Example 23

Heat is added to 0.350 kg of ice at $0.0$ C until all melted. $L_f = 3.34 \times 10^5$ J/kg.

(a) Change in entropy of the water (melting is isothermal at $T = 273.15$ K):
$$Q = m L_f = 0.350 \times 3.34\times10^5 \approx 1.17\times10^5 \text{ J}$$
$$\Delta S_{\text{water}} = \frac{Q}{T} = \frac{1.17\times10^5}{273.15} \approx 428 \text{ J/K}$$

(b) Source of heat is a massive body at $25.0$ C ($T = 298.15$ K). The body loses the same $Q$:
$$\Delta S_{\text{source}} = -\frac{Q}{298.15} \approx -392 \text{ J/K}$$

(c) Total entropy change:
$$\Delta S_{\text{total}} = 428 - 392 \approx 36 \text{ J/K} > 0$$

Positive, as required by the second law for an irreversible process.

## 8. Microscopic Interpretation of Entropy

Imagine $N$ coins. The macrostate "all heads up" corresponds to exactly 1 microstate; "1 head, 9 tails" with 10 coins corresponds to $\binom{10}{1} = 10$ microstates. In general, the number of microstates is the binomial coefficient $\binom{n}{m}$: the number of ways to arrange $n$ coins so that $m$ are heads.

For $n$ = 4, 10, 100, 1000 coins, the distribution of microstates as a function of macrostate $m$ is peaked at $m = n/2$ and becomes sharper as $n$ grows. The probability of a fluctuation away from the mean becomes vanishingly small for macroscopic $n$.

Probability of "all heads up":

| $n$ | probability |
| --- | --- |
| 4 | $0.0625$ |
| 10 | $9.77 \times 10^{-4}$ |
| 100 | $7.89 \times 10^{-31}$ |
| 1000 | $9.33 \times 10^{-302}$ |

The probability of all 1000 molecules in a room being in the left half is $\sim 9.33 \times 10^{-302}$. Scaled to Avogadro's number, we would wait many universe lifetimes for such a fluctuation.

### Microscopic Definition of Entropy

Let $\Omega$ (textbook uses $w$) be the number of microstates corresponding to a given macrostate. Then:
$$\boxed{\; S = k_B \ln \Omega \;}$$

where $k_B = 1.38 \times 10^{-23}$ J/K is **Boltzmann's constant**. $k_B$ has the same units as entropy — not a coincidence; $k_B$ is inextricably linked to the definition of entropy.

The entropy is non-negative: the smallest accessible state space has $\Omega = 1$, giving $S = 0$.

### Change of Entropy Between Macrostates

If a process takes the system from macrostate 1 ($\Omega_1$ microstates) to macrostate 2 ($\Omega_2$ microstates):
$$\Delta S = S_2 - S_1 = k_B \ln \Omega_2 - k_B \ln \Omega_1 = k_B \ln\!\left(\frac{\Omega_2}{\Omega_1}\right)$$

## Key Equations Summary — Chapter 20

- Cyclic engine: $W = |Q_H| - |Q_C|$
- Thermal efficiency: $e = W/Q_H = 1 - |Q_C|/|Q_H|$
- Otto cycle: $e = 1 - 1/r^{\gamma-1}$
- Refrigerator COP: $K = |Q_C|/W$
- Carnot efficiency: $e_{\text{Carnot}} = 1 - T_C/T_H$
- Carnot COP: $K_{\text{Carnot}} = T_C/(T_H - T_C)$
- Entropy (reversible): $dS = dQ/T$, $\Delta S = \int_1^2 dQ/T$
- Isothermal ideal gas: $\Delta S = nR \ln(V_2/V_1)$
- Second law (entropy form): $\Delta S_{\text{universe}} \ge 0$
- Boltzmann's relation: $S = k_B \ln \Omega$, $\Delta S = k_B \ln(\Omega_2/\Omega_1)$
