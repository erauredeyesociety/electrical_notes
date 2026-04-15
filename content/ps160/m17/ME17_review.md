# ME17 Review — Worked Solutions

## Temperature Scale Conversion (custom scale)

**Problem**: Invent a "W temperature scale" where water boils at 187 W and freezes at $-79$ W. Convert $-39$ C to W.

Linear form: $W = aC + b$.

Using the two known points:
$$187 = 100a + b$$
$$-79 = 0 \cdot a + b \Rightarrow b = -79$$
$$a = \frac{187 + 79}{100} = 2.66$$

So:
$$W = 2.66 C - 79$$
$$W(-39) = 2.66(-39) - 79 = -182.74~\text{W}$$

## Phase Change: Steam Bubbled Into Water (Problem 1)

**Problem**: $m_s = 2.4$ kg steam at 100 C is bubbled through $m_w = 15.0$ kg water at $T_w = 12.0$ C. Find $T_f$. $L_v = 2.26 \times 10^6$ J/kg; $c_w = 4190$ J/(kg·K).

**Step 1 — Heat released if all steam condenses**:
$$Q_{\text{steam}} = m_s L_v = 2.4 \times 2.26 \times 10^6 = 5.424 \times 10^6~\text{J}$$

**Step 2 — Heat water can absorb up to 100 C**:
$$Q_{\text{water}} = m_w c_w (100 - T_w) = 15.0 \times 4190 \times 88 = 5.53 \times 10^6~\text{J}$$

Since $Q_{\text{water}} > Q_{\text{steam}}$, the steam **fully condenses**.

**Step 3 — Energy balance**:
$$m_s L_v - m_s c_w (T_f - T_s) = m_w c_w (T_f - T_w)$$
$$T_f = \frac{m_s L_v + m_s c_w T_s + m_w c_w T_w}{c_w(m_w + m_s)}$$
$$T_f \approx 98.53^\circ \text{C}$$

## Phase Change: Steam Bubbled (Problem 2)

**Problem**: $m_s = 1.9$ kg steam at 100 C into $m_w = 14.0$ kg water at 28.0 C.

$$Q_{\text{steam}} = 1.9 \times 2.26 \times 10^6 = 4.294 \times 10^6~\text{J}$$
$$Q_{\text{water}} = 14.0 \times 4190 \times 72 = 4.22 \times 10^6~\text{J}$$

Since $Q_{\text{water}} < Q_{\text{steam}}$, the steam **partially condenses**. The water reaches 100 C, which is the max accessible temperature:
$$T_f = 100^\circ \text{C}$$

## Phase Change: Ice in Water (Problem 3)

**Problem**: $m_{\text{ice}} = 2.8$ kg at 0 C placed in $m_w = 13.4$ kg water at 24.0 C. $L_f = 3.35 \times 10^5$; $c_w = 4190$.

**Step 1 — Heat to melt all ice**:
$$Q_{\text{melt}} = m_{\text{ice}} L_f = 2.8 \times 3.35 \times 10^5 = 9.38 \times 10^5~\text{J}$$

**Step 2 — Heat the water can release cooling to 0 C**:
$$Q_{\text{water}} = m_w c_w (T_w - 0) = 13.4 \times 4190 \times 24.0 = 1.342 \times 10^6~\text{J}$$

Since $Q_{\text{water}} > Q_{\text{melt}}$, ice **fully melts**.

**Step 3 — Energy balance**:
$$-m_w c_w (T_f - T_w) = m_{\text{ice}} L_f + m_{\text{ice}} c_w (T_f - 0)$$
$$T_f \approx 6.03^\circ \text{C}$$

## Phase Change: Ice in Water (Problem 4)

**Problem**: $m_{\text{ice}} = 6.5$ kg at 0 C in $m_w = 8.5$ kg water at 26.9 C.

$$Q_{\text{water}} = 8.5 \times 4190 \times 26.9 = 9.58 \times 10^5~\text{J}$$
$$Q_{\text{melt}} = 6.5 \times 3.35 \times 10^5 = 21.77 \times 10^5~\text{J}$$

Since $Q_{\text{water}} < Q_{\text{melt}}$, ice **partially melts**:
$$T_f = 0^\circ \text{C}$$
