# PS 160 Midterm 2 — Thermodynamics Study Guide

Formula-by-formula review of the thermodynamics material on Midterm 2.

---

## 1. Thermal expansion

$$\Delta L = \alpha L_0\,\Delta T$$
- $\Delta L$: change in length (m)
- $\alpha$: linear expansion coefficient (K⁻¹)
- $L_0$: original length (m)
- $\Delta T$: temperature change (K or °C, same magnitude)

Materials expand when heated.

$$\Delta V = \beta V_0\,\Delta T$$
- $\beta$: volumetric expansion coefficient (K⁻¹)
- For isotropic solids, $\beta = 3\alpha$

## 2. Heat capacity and latent heat

$$Q = m c\,\Delta T$$
- $c$: specific heat capacity (J/(kg·K))

$$Q = \pm m L$$
- $L$: latent heat (J/kg); $+$ for heat absorbed (melting, boiling), $-$ for heat released (freezing, condensing)
- Temperature is **constant** during the phase change.

## 3. Molar heat capacities

$$C_V = \frac{f}{2}R$$
- $f$ = active degrees of freedom: monatomic gas $f = 3$, diatomic $f = 5$, polyatomic $f = 6$ (or more).

$$C_P = C_V + R$$
For any ideal gas: $C_P$ is $R$ more than $C_V$ because expansion work is done at constant pressure.

$$\gamma = \frac{C_P}{C_V}$$
Adiabatic index — appears in adiabatic processes.

$$C_V \approx 3 R\quad\text{(solids, Dulong–Petit)}$$

## 4. Heat transfer

### Conduction
$$H = k A\frac{\Delta T}{L}$$
Flux through a slab of area $A$, thickness $L$, thermal conductivity $k$.

### Radiation (Stefan–Boltzmann)
$$H = e A\sigma T^4$$
- $\sigma = 5.67\times 10^{-8}$ W/(m²·K⁴)
- $e$: emissivity (1 for a blackbody)

Net radiation exchanged with surroundings at $T_s$:
$$H_\text{net} = e A\sigma(T^4 - T_s^4)$$

## 5. Ideal gas law

$$pV = N k T = n R T$$
- $N$ molecules, $n$ moles
- $k = 1.38\times 10^{-23}$ J/K, $R = 8.314$ J/(mol·K)
- $k N_A = R$

## 6. Kinetic theory and Maxwell–Boltzmann

Average translational KE per particle:
$$\tfrac{1}{2}m\langle v^2\rangle = \tfrac{3}{2} k T$$

Root-mean-square speed:
$$v_\text{rms} = \sqrt{\langle v^2\rangle} = \sqrt{\frac{3 k T}{m}} = \sqrt{\frac{3 R T}{M}}$$
($M$ = molar mass.)

Maxwell–Boltzmann speed distribution:
$$f(v)\propto v^2 e^{-m v^2/(2 k T)}$$

## 7. Laws of thermodynamics

- **Zeroth:** $T_A = T_B = T_C$ (transitivity of thermal equilibrium)
- **First:** $dU = \bar d Q - \bar d W$ (work done *by* the system)
- **Second:** $\Delta S_\text{isolated}\ge 0$

## 8. Work and entropy

$$W = \int p\,dV$$
Area under the $p$-$V$ curve.

$$\Delta S = \int\frac{\bar d Q_\text{rev}}{T}$$

$$S = k\ln w$$
$w$ = number of microstates consistent with the macrostate (Boltzmann entropy).

## 9. Engines, refrigerators, heat pumps

Engine efficiency:
$$e = \frac{W}{Q_H} = 1 - \frac{|Q_C|}{Q_H}$$

Carnot (reversible) engine:
$$e_\text{Carnot} = 1 - \frac{T_C}{T_H}$$

Refrigerator / cooling COP (benefit = heat removed from cold side):
$$K_\text{ref} = \frac{Q_C}{|W|}$$

Heat pump / heating COP (benefit = heat delivered to hot side):
$$K_\text{HP} = \frac{|Q_H|}{|W|}$$

## 10. Entropy change in a Carnot cycle

$$\Delta S_\text{Carnot} = \frac{Q_H}{T_H} + \frac{Q_C}{T_C} = 0$$

The Carnot cycle is reversible, so the net entropy change of the working substance over one cycle is zero.

## Process summary for an ideal gas

| Process | Constant | $W$ | $Q$ | $\Delta U$ |
|---|---|---|---|---|
| Isobaric | $p$ | $p\Delta V$ | $nC_P\Delta T$ | $nC_V\Delta T$ |
| Isochoric | $V$ | $0$ | $nC_V\Delta T$ | $nC_V\Delta T$ |
| Isothermal | $T$ | $nRT\ln(V_2/V_1)$ | $W$ | $0$ |
| Adiabatic | $Q = 0$ | $(p_1V_1 - p_2V_2)/(\gamma-1)$ | $0$ | $-W$ |

For all ideal-gas processes: $\Delta U = n C_V\Delta T$ (not just isochoric).

Key adiabatic invariants: $pV^\gamma = \text{const}$, $TV^{\gamma-1} = \text{const}$.

## Entropy changes for simple processes

$$\Delta S_\text{isothermal, ideal gas} = nR\ln(V_2/V_1)$$
$$\Delta S_\text{heating} = m c\ln(T_2/T_1)$$
$$\Delta S_\text{phase change} = \pm\frac{m L}{T}$$
