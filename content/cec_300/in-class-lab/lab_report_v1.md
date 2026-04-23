# CEC 300 — Fixed-Wing Aircraft Pitch Controller Lab Report

**Author:** [Your Name Here]
**Course:** CEC 300 — Avionics & Control Systems
**Date:** 2026-04-22

---

## 1. Introduction

The plant modeled in this lab is a small fixed-wing general-aviation aircraft
with an elevator input δₑ(t) and a pitch-angle output θ(t). Newton's rotational
law gives

$$
I_y \frac{d^2\theta}{dt^2}
= -C_\alpha\,\theta(t) - C_q\,\frac{d\theta}{dt}
+ C_\delta\,\delta_e(t) + C_{\dot\delta}\,\frac{d\delta_e}{dt}.
$$

Dividing both sides by the pitch inertia \(I_y\) produces the coefficient form
used throughout this lab:

$$
\frac{d^2\theta}{dt^2} + 0.739\,\frac{d\theta}{dt} + 0.921\,\theta(t)
= 1.15\,\frac{d\delta_e}{dt} + 0.17\,\delta_e(t).
$$

Two aerodynamic effects dominate the left-hand (plant) side:

- **Aerodynamic damping — `0.739 dθ/dt`.** The horizontal tail behaves like a
  velocity-dependent shock absorber: as the nose pitches, the tail moves through
  the airstream, and the extra lift/drag opposes the motion. This term bleeds
  rotational kinetic energy out of the airframe.
- **Aerodynamic stiffness — `0.921 θ(t)`.** Static stability. Because the
  horizontal stabilizer is behind the center of gravity, any pitch deviation
  generates a restoring moment that rotates the aircraft back toward its trimmed
  attitude — the "weathervane" effect.

Taking the Laplace transform and solving for θ(s)/δₑ(s) gives the plant
transfer function:

$$
G(s) = \frac{\theta(s)}{\delta_e(s)}
     = \frac{1.15\,s + 0.17}{s^{2} + 0.739\,s + 0.921}.
$$

The denominator reveals an undamped natural frequency
\(\omega_n = \sqrt{0.921} \approx 0.96\ \text{rad/s}\) and damping ratio
\(\zeta = 0.739/(2\omega_n) \approx 0.385\). The aircraft is **under-damped** —
it will oscillate (wobble) before settling on any new pitch attitude.

The numerator contains a left-half-plane zero at
\(s = -0.17/1.15 \approx -0.148\) (the "elevator-rate whip" term
\(1.15\,d\delta_e/dt\)), which produces a pronounced initial transient spike in
the step response even though the DC gain is only
\(G(0) = 0.17/0.921 \approx 0.185\).

The controller is placed in a unity-feedback loop:

```text
  r(t) = 1.0  ──► [ + ] ──► C(s) ──► G(s) ──┬──► θ(t)
                  [ - ] ◄─────────────────── ┘
```

All controllers were built with the instructor's corrected PID transfer-function
form:

$$
C(s) = \frac{K_d\,s^2 + K_p\,s + K_i}{s}
\quad\Longrightarrow\quad
\texttt{num = [Kd, Kp, Ki], den = [1, 0]}.
$$

---

## 2. System Plots

All plots were produced by [pitch_control.py](pitch_control.py) using the
`python-control` library. Simulation horizon = 120 s (required because the PI/PID
closed-loop settles on a ~60–70 s time-scale).

### Task 1 — Open-Loop Response

![Task 1 open-loop step response](task1_open_loop.png)

### Task 2 — P-Control (Kp = 2)

![Task 2 P-control step response](task2_p_control.png)

### Task 3 — PI-Control (Kp = 2, Ki = 0.5)

![Task 3 PI-control step response](task3_pi_control.png)

### Task 4 — PID vs PI (Kp = 2, Ki = 0.5, Kd = 1.5)

![Task 4 PID vs PI comparison](task4_pid_vs_pi.png)

### Task 4 (Extra) — Kd Sweep

![Task 4 Kd sweep](task4_kd_sweep.png)

---

## 3. Data Table

Metrics computed directly from each simulation (see
[lab_data.json](lab_data.json) for raw values). "Peak value" = maximum of the
time response; "settle time" is the 2 % criterion.

| Metric                    | Open-Loop | P-Control (Kp=2) | PI-Control (Kp=2, Ki=0.5) | PID-Control (Kp=2, Ki=0.5, **Kd = 1.5**) |
|:--------------------------|:---------:|:----------------:|:-------------------------:|:----------------------------------------:|
| Final Value (Steady State)| 0.1846    | 0.2696           | 0.9986                    | 0.9987                                   |
| Steady-State Error        | 0.8154    | 0.7304           | 0.0014                    | 0.0013                                   |
| Peak Value                | 0.8404    | 0.6675           | 0.9986                    | 0.9987                                   |
| Settle Time (2 %)         | never *   | never *          | 66.64 s                   | 66.45 s                                  |

\* The open-loop and P-control responses never converge to within 2 % of the
   target within the 120 s horizon (nor ever, for the open-loop case — the
   aircraft simply has a non-unity DC gain).

---

## 4. Analysis — Why Kp alone wasn't enough, and how Ki fixed it

**Why Kp alone cannot reach the target.** The plant `G(s)` is a *type-0* system
(no free integrator — `s` is not a factor of the denominator). In the unity
feedback loop, the closed-loop DC gain with pure P-control is

$$
T(0) = \frac{K_p\,G(0)}{1 + K_p\,G(0)}
     = \frac{K_p\cdot(0.17/0.921)}{1 + K_p\cdot(0.17/0.921)}
     \;<\;1 \quad \text{for any finite } K_p.
$$

At steady state, the elevator deflection is proportional to the error:
`δₑ_ss = Kp · e_ss`. A non-zero deflection is needed to maintain the new pitch
against the aerodynamic-stiffness restoring moment, so the error *can never
become zero* under P-control. With Kp = 2 the measured steady-state value is
0.2696 — a residual error of 0.7304. Raising Kp would shrink the error, but
never to zero, and would eventually induce oscillation as the damping ratio
drops.

**How Ki fixes it.** Adding an integral term `Ki/s` puts a pole at the origin in
the forward path, making the open-loop type-1:

$$
C_{PI}(s)\,G(s)
  = \frac{K_p\,s + K_i}{s}\cdot G(s).
$$

For a type-1 loop, the Final-Value theorem guarantees zero steady-state error
to a step input: any residual error is continuously accumulated by the
integrator, causing `δₑ` to keep growing until the error is driven to zero.
The simulation confirms this — with Ki = 0.5 the final value is 0.9986 and the
steady-state error is effectively zero (0.0014, within numerical tolerance of
the 2 % settle point).

---

## 5. Analysis — Kᵢ Impact

Adding the integral term to the P-controller produced three changes:

1. **Steady-state error collapsed from 0.7304 to 0.0014** — the dominant
   improvement (~99.8 % error reduction). This is the effect described in
   Section 4.
2. **A settle time now exists at all** (~66.6 s to 2 %). Under P-control there
   was no settle-time in a meaningful sense because the system converged to the
   wrong value. Under PI the system is slow, but it does eventually reach the
   target.
3. **The initial transient is muted and then crawls back up.** The response
   rises to ~0.73 inside the first second (same aerodynamic whip as open-loop,
   scaled by the controller), dips to ~0.58 as the natural damping pulls the
   nose back, and then the integrator slowly winds up the command until the
   error is eliminated.

**Does Ki improve damping?** No — strictly speaking, Ki does not alter the
closed-loop damping ratio the way a higher Kp or a derivative term would. The
closed-loop poles are shifted (because the loop is now type-1), but the
pole-zero geometry of the response is not dominated by new damping. What Ki
does is *correct the final value* at the cost of a slower approach — the
integrator needs time to wind up. That is why the settle time is so long
(66.6 s): the low-frequency content of the response is limited by how quickly
Ki = 0.5 can integrate the residual error.

**Impact on settle time.** Ki made a settle time meaningful but slow. A
larger Ki would shorten the settle time at the risk of introducing oscillation
(integral wind-up effectively destabilizes the loop if too aggressive).

---

## 6. Analysis — Kd Impact

The derivative gain `Kd` adds a zero into the forward-path compensator at
`s = -Kp/Kd ≈ -1.33` (for Kp = 2, Kd = 1.5). Its intended role is to "apply
the brakes" when the pitch rate is high — it reacts to the *rate* of error
change rather than the error itself, which adds phase lead and increases the
effective damping of the closed loop.

In this specific configuration, however, the measured effect of Kd is small:

| Kd   | Final  | SS Error | Peak   | Settle (2 %) |
|:----:|:------:|:--------:|:------:|:------------:|
| 0.50 | 0.9987 | 0.0013   | 0.9987 | 66.58 s      |
| 1.00 | 0.9987 | 0.0013   | 0.9987 | 66.51 s      |
| 1.50 | 0.9987 | 0.0013   | 0.9987 | 66.45 s      |
| 2.00 | 0.9987 | 0.0013   | 0.9987 | 66.39 s      |
| 3.00 | 0.9987 | 0.0013   | 0.9987 | 66.26 s      |
| 5.00 | 0.9988 | 0.0012   | 0.9988 | 66.00 s      |

**Observations from the Kd sweep plot:**

- The **initial aerodynamic-whip spike** grows visibly with Kd — the response
  at t ≈ 0.1 s is ~0.37 for Kd = 0.5 but ~0.85 for Kd = 5.0 — because a step
  input passed through `Kd·s` produces a large derivative kick.
- The **first local minimum** (the dip near t = 5 s) deepens slightly for
  large Kd, but the subsequent rise to 1.0 is essentially unchanged.
- The **settle-time improvement is < 1 % across a 10× Kd sweep** (66.58 s at
  Kd = 0.5 down to 66.00 s at Kd = 5.0).

**Why Kd does so little here.** The base PI controller with Kp = 2, Ki = 0.5
already produces a *non-oscillatory* closed-loop response — there is no
overshoot above 1.0 and no ringing for Kd to damp. The slow approach to 1.0
is integrator-limited (Ki = 0.5), not damping-limited. Derivative action helps
most when the closed-loop is ringing or overshooting; here it has no ringing
to kill, so its main visible effect is the transient kick at t = 0.

**Does Kd improve damping or settle time?** Marginally. In this configuration,
Kd's primary useful role is to stabilize the loop against future Kp increases
— if we wanted a faster response by raising Kp, Kd would start earning its
keep by suppressing the overshoot that would otherwise appear.

---

## 7. Analysis — Tuning Results

The specified gains (Kp = 2, Ki = 0.5, Kd = 1.5) produce an accurate but
**slow** response (ts ≈ 66 s, SSE ≈ 0.001). Through the Kd sweep, the best
settle time I achieved without violating the "reasonably fast" qualifier is:

- **Best Kd** within the specified parameter range: **Kd = 5.0** →
  ts = 66.00 s, peak = 0.9988, SSE = 0.0012.

The gain is marginal (≈ 0.5 s out of 66 s, or < 1 %) and comes at the cost of
a larger initial transient kick in δₑ that, in a real aircraft, would feel like
a jerky elevator input to passengers. The design intent of the assigned
(Kp, Ki, Kd) = (2, 0.5, 1.5) is therefore a sensible compromise:

- **Accuracy:** SSE < 0.2 % (integral-dominated).
- **Passenger comfort:** no visible overshoot above the commanded pitch, no
  oscillations, moderate initial elevator deflection.
- **Speed:** ~66 s to 2 %. This is slow for agile aircraft but reasonable for
  a small general-aviation airframe where aerodynamic stiffness is modest.

If a faster response were required, a more productive direction is to raise
Kp and Ki together (tightening the loop bandwidth) and then use Kd to pull the
resulting overshoot back down. Meaningful Kd tuning only becomes valuable in
that higher-gain regime.

---

## 8. Lessons Learned / Insights

1. **Type of the plant dictates what a controller can achieve.** The
   zero-steady-state-error property of PI control is *not* about Ki's magnitude
   — it's about adding an integrator to a type-0 plant. Once I understood this,
   the poor performance of pure P-control on this aircraft stopped being
   surprising and became predictable from the transfer function alone.

2. **Aerodynamic physics show up as specific terms in the transfer function.**
   The `0.921 θ` stiffness and `0.739 dθ/dt` damping are not abstract
   coefficients — they correspond directly to the weathervane restoring moment
   and tail-induced aerodynamic drag. Reading a plant transfer function as
   *physics* made the damping-ratio math feel concrete.

3. **The numerator zero matters as much as the denominator poles.** The
   `1.15 s` "whip" term in the numerator produces a large initial transient in
   every response, even under closed-loop control. This is why the PI/PID
   closed-loop shows an initial bump even though the final response is smooth.

4. **Derivative action needs oscillation to act on.** My Kd sweep demonstrated
   that Kd has almost no effect when the base PI loop is already non-oscillatory.
   Kd earns its keep only when the loop would otherwise ring — a real
   consideration when pairing it with higher Kp for faster response.

5. **Long simulation horizons are sometimes necessary.** My first run used a
   30 s horizon and produced final values of ~0.87 for the PI and PID cases,
   which *looked* like unresolved steady-state error. Extending to 120 s showed
   the responses were simply still climbing. A good reminder to always check
   whether a simulation has reached steady state before drawing conclusions
   from its "final" value.

6. **The professor's PID coefficient-order correction is a good illustration
   of s-domain intuition.** A PID controller is `Kp + Ki/s + Kd·s`, which as a
   single rational function is `(Kd s² + Kp s + Ki)/s`. The `python-control`
   `TransferFunction([num], [den])` argument takes coefficients from the
   highest power of `s` down — so the numerator list must be
   `[Kd, Kp, Ki]`. Getting the order wrong assigns gains to the wrong
   dynamics.
