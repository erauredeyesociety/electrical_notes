# Chapter 12: Fluid Mechanics Simplified

*Author: Oussama Mhibik — 07/03/2024*

## 1. Introduction

**Fluids** are substances that can flow and take the shape of their containers. They include liquids, gases, and plasmas. Unlike solids (fixed shape and volume), fluids adapt to the shape of their environment.

Key properties of fluids:

1. **Viscosity** — resistance to flow (honey has high viscosity; water has low viscosity).
2. **Density** — mass per unit volume. Influences buoyancy and pressure. Oil is less dense than water, so it floats.
3. **Pressure** — force exerted per unit area. Increases with depth in liquids.
4. **Flow rate** — volume of fluid passing a point per unit time.

**Fluid mechanics** studies the behavior of fluids and the forces acting on them. It includes:

- **Fluid statics** — fluids at rest (hydrostatic pressure, Archimedes' principle).
- **Fluid dynamics** — fluids in motion. Key principles:
  - **Continuity equation**: mass flow rate is constant through a pipe: $A_1 v_1 = A_2 v_2$.
  - **Bernoulli's equation**: an increase in fluid speed is accompanied by a decrease in pressure or potential energy — conservation of energy for flowing fluids.
  - **Navier–Stokes equations**: nonlinear PDEs describing fluid motion, including viscosity, pressure, and external forces.

Applications: aerodynamics, hydraulics, meteorology, biology (blood flow).

## 2. Density

Density measures how much mass is packed into a given volume.

$$\rho = \frac{m}{V}$$

SI units: $\mathrm{kg/m^3}$.

## 3. Pressure

Pressure is the force per unit area exerted by fluid molecules (e.g., air molecules in a balloon bouncing against the walls). More molecules or faster molecules produce more pressure.

## 4. Hydrostatic Pressure

**Hydrostatic pressure** is the pressure exerted by a fluid at rest due to gravity. The deeper you go, the more fluid presses down from above.

$$P = \rho g h$$

where:
- $P$ = hydrostatic pressure,
- $\rho$ = fluid density,
- $g$ = acceleration due to gravity,
- $h$ = depth of the fluid above the point.

This is why dams are wider at the bottom (greater pressure) and why ears hurt when diving deep.

## 5. Buoyant Force

**Buoyant force** is the upward push a fluid exerts on an immersed object. It equals the weight of the fluid displaced by the object (Archimedes' principle).

- If buoyant force > weight of object → object floats.
- If buoyant force < weight of object → object sinks.

A metal ship floats because it's shaped to displace enough water to generate sufficient buoyant force.

## 6. The Continuity Equation

For an incompressible fluid in a closed pipe, the mass flow rate is constant:

$$A_1 v_1 = A_2 v_2$$

Narrower sections of a pipe cause faster flow. This is why rivers flow faster in narrow sections.

## 7. Pascal's Law

**Pascal's Law**: a pressure change applied to an enclosed fluid is transmitted equally in all directions throughout the fluid.

This is the foundation of hydraulic systems — car brakes, hydraulic lifts. A small force on a small piston creates a large force on a larger piston.

## 8. Bernoulli's Law

**Bernoulli's Law** is conservation of energy for a flowing fluid:

$$P + \tfrac{1}{2}\rho v^2 + \rho g h = \text{constant}$$

where:
- $P$ = fluid pressure,
- $\rho$ = fluid density,
- $v$ = fluid velocity,
- $g$ = gravitational acceleration,
- $h$ = height above a reference.

Applications:
- **Airplane wings**: air moves faster over the top → lower pressure on top → lift.
- **Shower curtain**: fast-moving air inside shower lowers pressure, pulling the curtain in.
- Bird flight, carburetors, and many fluid-flow phenomena.
