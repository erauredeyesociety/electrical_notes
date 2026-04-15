# Chapter 19 — The First Law of Thermodynamics

The first law of thermodynamics extends conservation of energy to include transfer of mechanical and thermal energy between a system and its surroundings.

---

## 1. Thermodynamic systems

A **thermodynamic system** is any collection of objects with the potential to exchange energy (mechanical or thermal) with its surroundings. A **thermodynamic process** describes the changes in state variables ($p, V, T, n$).

Processes are assumed **quasi-static** — state variables are well defined at every point along the path.

## 2. Work done during volume changes

- Positive work: piston moves outward, volume expands.
- Negative work: piston moves inward, volume contracts.

Starting from $dW = F\,dx$ with $F = pA$ and $A\,dx = dV$:
$$dW = p\,dV$$
$$W = \int_{V_1}^{V_2} p\,dV\quad\text{(work done in a volume change)}$$

Geometrically, $W$ is the **area under the $p$-$V$ curve** between $V_1$ and $V_2$. The work depends on the **path**, not just the endpoints.

### 2.1 Work in an isothermal expansion

For an ideal gas at constant $T$, $p = nRT/V$, so
$$W = \int_{V_1}^{V_2}\frac{nRT}{V}\,dV = nRT\ln\!\frac{V_2}{V_1}\quad\text{(isothermal)}$$

**Example (Ex. 3):** Two moles of ideal gas compressed isothermally at 65.0 °C until the pressure triples. Sketch the $pV$ diagram and compute $W$.

## 3. The four standard thermodynamic paths

1. **Isothermal** — $\Delta T = 0$
2. **Isobaric** — $\Delta p = 0$
3. **Isochoric** — $\Delta V = 0$
4. **Adiabatic** — $Q = 0$

## 4. Internal energy and the first law

**Internal energy** $U$ is the sum of all the kinetic and interaction potential energies of the molecules in the system.

Conservation of energy: heat added to a system either raises its internal energy or is spent doing work on the surroundings:
$$Q = \Delta U + W\quad\text{(first law of thermodynamics)}$$

Equivalently,
$$\Delta U = Q - W$$

**Key property:** $\Delta U$ depends only on the initial and final states (it is a state function). $Q$ and $W$ individually depend on the path.

For an ideal gas, **$U$ depends only on $T$**:
$$\Delta U = n C_V\,\Delta T\quad\text{(for \emph{any} path on an ideal gas)}$$

### 4.1 Cyclic processes

In a cycle the system returns to its initial state, so $\Delta U = 0$ over the full cycle. Therefore over the cycle $Q_\text{net} = W_\text{net}$. Graphically, $W_\text{net}$ is the enclosed area of the loop on a $pV$-diagram — positive if the loop runs clockwise, negative if counter-clockwise.

## 5. Kinds of thermodynamic processes — first-law applied

| Process | Condition | First-law result |
|---|---|---|
| Adiabatic | $Q = 0$ | $\Delta U = -W$ |
| Isochoric | $\Delta V = 0$ | $W = 0$, $\Delta U = Q = n C_V\Delta T$ |
| Isobaric | $\Delta p = 0$ | $W = p\,\Delta V$, $Q = n C_P\Delta T$ |
| Isothermal | $\Delta T = 0$ (ideal gas) | $\Delta U = 0$, $Q = W = nRT\ln(V_2/V_1)$ |

## 6. Internal energy of an ideal gas (free expansion)

Free-expansion experiments on low-density gases show that $T$ is unchanged when the gas expands into a vacuum. Since $Q = 0$ and $W = 0$ for free expansion, $\Delta U = 0$, even though $p$ and $V$ change. Conclusion: **for an ideal gas, $U$ depends on $T$ alone**, not on $p$ or $V$.

## 7. Heat capacities of an ideal gas

From the isochoric path:
$$Q_V = n C_V\Delta T \Rightarrow \Delta U = n C_V\Delta T\quad\text{(always, ideal gas)}$$

From the isobaric path:
$$\Delta U = Q_p - W = n C_P\Delta T - p\Delta V = n C_P\Delta T - nR\Delta T$$

Equating the two expressions for $\Delta U$ gives the fundamental relation
$$\boxed{\,C_P = C_V + R\,}$$

### 7.1 Ratio of heat capacities

$$\gamma = \frac{C_P}{C_V}$$

- **Monatomic gas** (3 translational DOF): $C_V = \tfrac{3}{2}R$, $C_P = \tfrac{5}{2}R$, $\gamma = 5/3$.
- **Diatomic gas** (5 DOF near room temperature): $C_V = \tfrac{5}{2}R$, $C_P = \tfrac{7}{2}R$, $\gamma = 7/5$.

Remember: $\Delta U = n C_V\Delta T$ holds whether $V$ is constant or not.

## 8. Adiabatic processes for an ideal gas

For an adiabat, $Q = 0$, so $dU = -dW$:
$$n C_V\,dT = -p\,dV = -\frac{nRT}{V}\,dV$$
$$\frac{dT}{T} + \frac{R}{C_V}\,\frac{dV}{V} = 0$$
$$\frac{R}{C_V} = \frac{C_P - C_V}{C_V} = \gamma - 1$$

Integrating:
$$T V^{\gamma - 1} = \text{const}$$
$$p V^{\gamma} = \text{const}$$

Work done along an adiabat:
$$W = \int_{V_1}^{V_2} p\,dV = \frac{1}{\gamma - 1}(p_1 V_1 - p_2 V_2) = -\Delta U = -n C_V\Delta T = n C_V(T_1 - T_2)$$

---

## Summary of key equations

$$W = \int_{V_1}^{V_2} p\,dV$$
$$Q = \Delta U + W,\qquad \Delta U = Q - W$$
$$\Delta U = n C_V\Delta T\quad\text{(ideal gas, any path)}$$
$$C_P = C_V + R,\qquad \gamma = C_P/C_V$$
$$W_\text{isothermal} = nRT\ln(V_2/V_1)$$
$$W_\text{adiabatic} = \frac{p_1 V_1 - p_2 V_2}{\gamma - 1},\quad pV^\gamma = \text{const},\quad TV^{\gamma-1} = \text{const}$$
