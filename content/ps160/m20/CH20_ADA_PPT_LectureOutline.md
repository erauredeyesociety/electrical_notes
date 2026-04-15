# Chapter 20 — The Second Law of Thermodynamics (Lecture Outline)

Covers reversible/irreversible processes, heat engines and their efficiency, the Otto and Diesel internal-combustion cycles, refrigerators and coefficient of performance, the Carnot cycle, entropy, and the microscopic (statistical) interpretation of entropy.

## Learning Outcomes

- The difference between reversible and irreversible processes.
- The physics of internal-combustion engines.
- How refrigerators and heat engines are related, and how to analyze the performance of a refrigerator.
- How the second law of thermodynamics sets limits on the efficiency of engines and the performance of refrigerators.
- What is meant by entropy, and how to use this concept to analyze thermodynamic processes.

## Introduction

Why does heat flow spontaneously from hot lava into cooler water, and never the reverse? Mechanical energy can be converted completely into heat, but the reverse is forbidden. The first law (energy conservation) alone cannot explain this — we need the **second law of thermodynamics** and the concept of **entropy**.

## Directions of Thermodynamic Processes

A **reversible process** is one whose direction can be reversed by an infinitesimal change in conditions. The system is always in (or very close to) thermal equilibrium — hence such processes are also called **equilibrium processes**.

- A block of ice placed in a hot metal box melts **irreversibly** (large temperature difference).
- A block of ice at 0 C placed in a 0 C metal box can be melted (or re-frozen) **reversibly** by infinitesimal temperature changes.

All real, spontaneous processes are irreversible.

## Heat Engines

A **heat engine** is any device that partly transforms heat into work or mechanical energy. Simple heat engines operate on a cyclic process:

1. Absorb heat $Q_H$ from a hot reservoir at $T_H$.
2. Do mechanical work $W$.
3. Reject heat $|Q_C|$ to a cold reservoir at $T_C$.

Since the working substance returns to its initial state each cycle, $\Delta U = 0$ and the first law gives:
$$W = Q_H + Q_C = |Q_H| - |Q_C|$$

### Thermal Efficiency

The fraction of $Q_H$ converted to work:
$$e = \frac{W}{Q_H} = 1 - \frac{|Q_C|}{|Q_H|}$$

"What you get divided by what you pay for." Always less than 1.

## Internal-Combustion Engines

### The Otto Cycle (Gasoline Engine)

Four strokes on a $pV$ diagram:
- $a \to b$: adiabatic compression of gasoline–air mixture.
- $b \to c$: heat $Q_H$ added at constant volume (ignition).
- $c \to d$: adiabatic expansion (power stroke).
- $d \to a$: constant-volume cooling, heat $|Q_C|$ rejected.

Thermal efficiency in terms of compression ratio $r = V_{\max}/V_{\min}$:
$$e = 1 - \frac{1}{r^{\gamma-1}}$$

Typical $r \approx 8$, giving a theoretical efficiency near $0.56$.

### The Diesel Cycle

- $a \to b$: adiabatic compression of air alone (no fuel present, so no pre-ignition).
- $b \to c$: constant-pressure heating (fuel injection and combustion).
- $c \to d$: adiabatic expansion (power stroke).
- $d \to a$: constant-volume cooling.

Because there is no fuel in the cylinder during compression, the compression ratio can be much higher ($r \sim 15\text{–}20$), giving theoretical efficiencies $\sim 0.65\text{–}0.70$.

## Refrigerators

A refrigerator is essentially a heat engine run in reverse: it takes heat $|Q_C|$ from a cold place and delivers heat $|Q_H|$ to a warmer place. By conservation of energy, a work input is required:
$$W + |Q_C| = |Q_H| \quad\Longrightarrow\quad W = |Q_H| - |Q_C|$$

### Coefficient of Performance

$$K = \frac{|Q_C|}{|W|} = \frac{|Q_C|}{|Q_H| - |Q_C|}$$

Dimensionless; the larger $K$, the better the refrigerator (more heat removed per unit work input). Also called the **energy efficiency rating**.

An **air conditioner** operates on the same principle, dumping heat from indoors to outside.

## The Second Law of Thermodynamics

Two equivalent statements:

**"Engine" statement:** It is impossible for any system to undergo a process in which it absorbs heat from a reservoir at a single temperature and converts that heat completely into mechanical work, with the system ending in the same state in which it began.

**"Refrigerator" statement:** It is impossible for any process to have as its sole result the transfer of heat from a cooler to a hotter object.

These two statements are logically equivalent:
- A workless refrigerator, combined with an ordinary engine, would produce a 100%-efficient engine.
- A 100%-efficient engine, combined with an ordinary refrigerator, would produce a workless refrigerator.

## The Carnot Cycle

A **Carnot cycle** is an idealized reversible cycle consisting of two isothermal and two adiabatic segments:

1. Isothermal expansion at $T_H$, absorbing $Q_H$.
2. Adiabatic expansion until temperature drops to $T_C$.
3. Isothermal compression at $T_C$, rejecting $|Q_C|$.
4. Adiabatic compression back to initial state at $T_H$.

### Carnot Efficiency

$$e_{\text{Carnot}} = 1 - \frac{T_C}{T_H} \qquad (T\text{ in kelvins})$$

This is the **maximum possible efficiency** of any heat engine operating between reservoirs at $T_H$ and $T_C$ (Carnot's theorem).

### Maximizing Efficiency

To maximize a real engine's efficiency:
- Make $T_H$ as high as possible (jet engines use ceramics that withstand $> 1000$ C).
- Make $T_C$ as low as possible.

### Carnot Refrigerator

Because each step of the Carnot cycle is reversible, running it backward gives the Carnot refrigerator, the ideal refrigerator. Its coefficient of performance is:
$$K_{\text{Carnot}} = \frac{T_C}{T_H - T_C}$$

### Carnot and the Second Law

No engine operating between two given temperatures can exceed the Carnot efficiency. All reversible engines operating between the same two reservoirs have the same (Carnot) efficiency.

## Entropy and Disorder

**Entropy** $S$ is a quantitative measure of disorder (randomness). Natural processes proceed in the direction of increasing randomness. Adding heat to a substance increases molecular kinetic energies and makes molecular motion more random.

### Entropy in Reversible Processes

For an infinitesimal reversible process at absolute temperature $T$:
$$dS = \frac{dQ}{T}$$

For a finite reversible process:
$$\Delta S = \int_{1}^{2} \frac{dQ}{T}$$

Units: J/K.

### Entropy in Cyclic Processes

For any **reversible** cyclic process (including the Carnot cycle), the total entropy change is zero:
$$\oint \frac{dQ_{\text{rev}}}{T} = 0$$

### Entropy Form of the Second Law

> **No process is possible in which the total entropy decreases, when all systems taking part in the process are included.**

$$\Delta S_{\text{universe}} \ge 0$$

Equality holds only for reversible processes. Example: the mixing of ink and water is irreversible, and the entropy of the combined system increases.

## Microscopic Interpretation of Entropy

Toss $N$ identical coins. The most probable outcome (half heads, half tails) corresponds to the macrostate with the greatest number of microstates. Let $w$ (or $\Omega$) be the number of microscopic states corresponding to a given macroscopic state.

### Boltzmann's Entropy Formula

$$S = k_B \ln w$$

where $k_B = 1.38 \times 10^{-23}$ J/K is Boltzmann's constant. The entropy change between two macrostates is:
$$\Delta S = k_B \ln\!\left(\frac{w_2}{w_1}\right)$$

### Example: Free Expansion

In a free expansion of $N$ molecules in which the volume doubles, each molecule has twice as many position states, so $w_2/w_1 = 2^N$. The entropy change is:
$$\Delta S = k_B \ln(2^N) = N k_B \ln 2 = nR \ln 2$$

consistent with the macroscopic result $\Delta S = nR\ln(V_2/V_1)$ for isothermal expansion.

## Key Equations Summary — Chapter 20

- First law for a cyclic engine: $W = Q_H + Q_C = |Q_H| - |Q_C|$
- Thermal efficiency: $e = W/Q_H = 1 - |Q_C|/|Q_H|$
- Otto cycle efficiency: $e = 1 - 1/r^{\gamma-1}$
- Refrigerator COP: $K = |Q_C|/|W| = |Q_C|/(|Q_H| - |Q_C|)$
- Carnot efficiency: $e_{\text{Carnot}} = 1 - T_C/T_H$
- Carnot COP: $K_{\text{Carnot}} = T_C/(T_H - T_C)$
- Entropy (reversible): $dS = dQ/T$, $\Delta S = \int dQ/T$
- Second law (entropy): $\Delta S_{\text{universe}} \ge 0$
- Boltzmann: $S = k_B \ln w$
