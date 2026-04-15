# M17 Review — Worked Solutions

## Problem 1: Kelvin to Fahrenheit

**Given** $T = 201$ K, convert to F.

$$T_C = T_K - 273.15, \qquad T_F = \tfrac{9}{5}T_C + 32$$
$$T_F = \tfrac{9}{5}(T_K - 273.15) + 32 = -97.87^\circ \text{F}$$

## Problem 2: Linear Expansion — find $\Delta T$

A metal has $\alpha = 2.6 \times 10^{-5}$ (C°)$^{-1}$. Pipe length 1.7 m. Find $\Delta T$ for $\Delta L = 7.4$ mm.

$$\Delta L = \alpha L_0 \Delta T \Rightarrow \Delta T = \frac{\Delta L}{\alpha L_0} = \frac{7.4 \times 10^{-3}}{(2.6 \times 10^{-5})(1.7)} \approx 167.4^\circ \text{C}$$

## Problem 3: Linear Expansion — find $\Delta L$

$\alpha = 1.1 \times 10^{-5}$ (C°)$^{-1}$, $L_0 = 5.2$ m, $\Delta T = 46$ C°.

$$\Delta L = \alpha L_0 \Delta T \approx 2.63~\text{mm}$$

## Problem 4: Volume Expansion — unknown fluid $\beta$

Glass bottle volume $V_0 = 0.012$ m$^3$ filled with fluid of unknown $\beta$. Warmed by $\Delta T = 7.1$ C°, 16 mL spill out. Glass $\alpha = 1.9 \times 10^{-5}$ K$^{-1}$. Find $\beta$ in (kC°)$^{-1}$.

Let $\Delta V_{\text{spill}} = V_L' - V_B' = (\beta - 3\alpha) V_0 \Delta T$:
$$\beta = \frac{\Delta V_{\text{spill}}}{V_0 \Delta T} + 3\alpha$$

With $\Delta V = 16 \times 10^{-6}$ m$^3$:
$$\beta \approx 0.245~(\text{kC}^\circ)^{-1}$$

Note: $1000$ C° $= 1$ kC°.

## Problem 5: Falling Water — temperature rise

Bottle with 1.3 L water falls from $h = 150.2$ m. All mechanical energy to heat.

$$mgh = mc\Delta T \Rightarrow \Delta T = \frac{gh}{c} = \frac{9.8 \times 150.2}{4190} \approx 0.351^\circ \text{C}$$

## Problem 6: Specific Heat — find $\Delta T$

$Q = 3141$ J into $m = 4.3$ kg, $c = 645$ J/(kg·C°).

$$\Delta T = \frac{Q}{mc} \approx 1.13^\circ \text{C}$$

## Problem 7: Specific Heat — find $c$

$Q = 24{,}512$ J raises 2.8 kg by 11 C°.

$$c = \frac{Q}{m \Delta T} \approx 796~\text{J/(kg·C}^\circ\text{)}$$

## Problem 8: Mixing — equilibrium temperature

5.6 kg chloroform at 13.5 C + 9.5 kg propylene glycol at 36.8 C. $c_{\text{prop}} = 2500$, $c_{\text{ch}} = 1050$ J/(kg·K).

$$Q_{\text{ch}} + Q_g = 0$$
$$m_{\text{ch}} c_{\text{ch}}(T_f - T_{\text{ch}}) + m_g c_g(T_f - T_g) = 0$$
$$T_f = \frac{m_g c_g T_g + m_{\text{ch}} c_{\text{ch}} T_{\text{ch}}}{m_{\text{ch}} c_{\text{ch}} + m_g c_g} \approx 32.2^\circ \text{C}$$

## Problem 9: Energy to Freeze Water

0.29 kg water at 17 C. Cool to 0 C then freeze:
$$Q = m c_w (T_f - T_i) - m L_f$$
$$Q = (0.29)(4190)(0 - 17) - (0.29)(335{,}000) \approx -117.8~\text{kJ}$$
(negative = energy removed)

## Problem 10: Ice (−20 C) to Water (16 C)

2.69 kg ice at $-20$ C → water at 16 C. Three steps:
1. Warm ice: $m c_{\text{ice}} (0 - (-20))$
2. Melt: $m L_f$
3. Warm water: $m c_w (16 - 0)$

$$Q \approx 1192~\text{kJ}$$

## Problem 11: Ice Placed in Warm Water

7.2 kg ice at 0 C into 11.5 kg water at 28.4 C. $L_f = 3.35 \times 10^5$, $c = 4190$. Find $T_f$.

Check: energy available from water cooling to 0 C:
$$Q_{\text{avail}} = (11.5)(4190)(28.4) = 1{,}368{,}454~\text{J}$$

Energy needed to melt all ice:
$$Q_{\text{melt}} = (7.2)(3.35 \times 10^5) = 2.412 \times 10^6~\text{J}$$

Since $Q_{\text{avail}} < Q_{\text{melt}}$, ice is only **partially melted** and:
$$T_f = 0^\circ \text{C}$$

## Problem 12: Heat Conduction Through Window

Window $1.6 \times 2$ m, thickness 13.9 mm, $k_{\text{glass}} = 0.8$ W/(m·K). Outside −17 C, inside 18 C.

$$H = \frac{kA(T_H - T_C)}{L} = \frac{0.8 \times (1.6 \times 2) \times (18 - (-17))}{13.9 \times 10^{-3}} \approx 6.45~\text{kW}$$

## Problem 13: Radiation from a Ball

Radius 3.1 m, emissivity 0.63. Ball at 92 C, room at 28 C.

$$H = A e \sigma (T_H^4 - T_C^4), \quad A = 4\pi r^2$$
$$T_H = 365.15~\text{K}, \quad T_C = 301.15~\text{K}$$
$$H \approx 41.2~\text{kW}$$
