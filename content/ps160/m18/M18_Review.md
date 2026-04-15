# M18 Review — Worked Solutions

## Question 1: Ideal Gas Pressure

**Problem**: 1.1 mol ideal gas in 39 L at 20 C. Find $p$ in atm. ($1\,\text{L} = 10^{-3}\,\text{m}^3$; $1\,\text{atm} = 1.01325 \times 10^5$ Pa.)

$$p = \frac{nRT}{V}$$

Convert: $V = 39 \times 10^{-3}$ m$^3$; $T = 293.15$ K.

$$p = 6.8743 \times 10^4~\text{Pa} = 0.6781~\text{atm}$$

## Question 2: Ideal Gas Process (Combined Gas Law)

**Problem**: $P_2 = 1.9 P_1$, $V_2 = 0.8 V_1$, $T_1 = 301$ K. Find $T_2$.

$$\frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}$$
$$T_2 = T_1 \cdot \frac{P_2 V_2}{P_1 V_1} = 301 \times 1.9 \times 0.8 = 457.52~\text{K}$$

## Question 3: Ideal Gas — Find Final Volume

**Problem**: $p_1 = p_0$, $V_1 = 0.9$ m$^3$, $p_2 = 0.8 p_0$, $T_2 = 1.55 T_1$. Find $V_2$.

$$V_2 = V_1 \frac{P_1 T_2}{P_2 T_1} = \frac{0.9 \times 1.55}{0.8} = 1.743~\text{m}^3$$

## Question 4: Tire Problem (with leak and temperature rise)

**Problem**: Tire gauge pressure $P_{g,1} = 258{,}811$ Pa, $V = 3$ L, $T_1 = 6$ C. $\Delta T = +24$ C°, 13% of gas leaks. Atmospheric $P_0 = 1.00 \times 10^5$ Pa. Find new gauge pressure in psi. ($1$ psi $= 6895$ Pa; volume unchanged.)

Generalized gas law with changing $n$:
$$\frac{P_1 V_1}{n_1 T_1} = \frac{P_2 V_2}{n_2 T_2}$$

With $V_1 = V_2$ and $n_2 = 0.87 n_1$:
$$P_2 = P_1 \cdot 0.87 \cdot \frac{T_2}{T_1}$$

Use **absolute** pressure ($P_1 = P_{g,1} + P_0$), then subtract $P_0$ for final gauge, convert to psi:
$$P_{g,2} \approx 34.665~\text{psi}$$

## Question 5: Molecules in a Tiny Mass

**Problem**: Number of molecules in 57.5 attograms of C$_6$H$_8$OH. ($1$ ag $= 10^{-18}$ g.)

Molar mass: $M = 6(12.01) + 8(1.008) + 16.00 + 1.008 \approx 97.13$ g/mol.

Number of moles: $n = \dfrac{57.5 \times 10^{-18}~\text{g}}{97.13~\text{g/mol}}$.

Number of molecules:
$$N = n \cdot N_A \approx 356{,}489~\text{molecules}$$

## Question 6: Moles of C$_2$H$_3$

$M = 2(12.01) + 3(1.008) = 27.044$ g/mol.
$$n = \frac{61}{27.044} \approx 2.255~\text{mol}$$

## Question 7: Total Translational KE

**Problem**: 5.1 mol ideal gas at 25 C.

$$K_{\text{trans}} = \tfrac{3}{2} n R T = \tfrac{3}{2}(5.1)(8.314)(298.15) \approx 18{,}960~\text{J}$$

## Question 8: Find Temperature from Total KE

**Problem**: $K_{\text{trans,total}} = 235{,}863$ J, $n = 17$ mol. Find $T$.

$$T = \frac{2 K}{3 n R}$$
(The PDF has an algebra typo but the idea is straightforward.)

## Question 9: RMS Speed of Helium

**Problem**: $T = 21.3$ C, $M = 4.00$ g/mol.
$$v_{\text{rms}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3 \times 8.314 \times 294.45}{4.00 \times 10^{-3}}} \approx 1354.7~\text{m/s}$$

## Question 10: Average velocity component

**Problem**: Average $v_x$ of O$_2$ at 12.7 C.

By isotropy of random molecular motion:
$$\langle v_x \rangle = 0~\text{m/s}$$
(But $v_{\text{rms}}$ is not zero!)

## Question 11: Most Probable Speed of O$_2$

**Problem**: O$_2$ at 42.2 C. $M_{O_2} = 32.0$ g/mol.

$$v_{\text{mp}} = \sqrt{\frac{2kT}{m}} = \sqrt{\frac{2RT}{M}}$$
$$T = 315.35~\text{K}, \quad v_{\text{mp}} \approx 404.71~\text{m/s}$$

## Question 12: Heat to Warm a Monatomic Solid (Dulong–Petit)

**Problem**: Atomic mass 49 amu, mass 28 g. $C_V \approx 3R$ per mole.

$$n = \frac{28}{49} = 0.571~\text{mol}$$
$$Q = n \cdot 3R \cdot \Delta T \approx 270.80~\text{J}$$

## Question 13: Molar Heat Capacity

**Problem**: 2.1 mol, $Q = 379$ J, $\Delta T = 9.1$ K.

$$C_V = \frac{Q}{n \Delta T} = \frac{379}{2.1 \times 9.1} \approx 19.83~\text{J/(mol·K)}$$
