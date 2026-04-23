"""
CEC 300 --- In-Class Lab: Fixed-Wing Aircraft Pitch Controller

Plant model (from Section 2 of the lab guide):
    G(s) = theta(s) / delta_e(s) = (1.15 s + 0.17) / (s^2 + 0.739 s + 0.921)

Tasks
-----
    1. Open-loop step response of G(s)
    2. P-controller with Kp = 2
    3. PI-controller with Kp = 2, Ki = 0.5
    4. PID-controller with Kp = 2, Ki = 0.5, Kd = 1.5 (and Kd-tuning sweep)

PID transfer-function form (uses the instructor's corrected coefficient order):
    C(s) = Kp + Ki/s + Kd*s = (Kd s^2 + Kp s + Ki) / s
    => num = [Kd, Kp, Ki], den = [1, 0]

Outputs saved to this folder:
    task1_open_loop.png
    task2_p_control.png
    task3_pi_control.png
    task4_pid_vs_pi.png
    task4_kd_sweep.png
    lab_data.json       (metrics table as JSON for reference)
"""
from __future__ import annotations

import json
from pathlib import Path

import control as ct
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Plant G(s) --- fixed-wing pitch-to-elevator transfer function
# ---------------------------------------------------------------------------
G = ct.TransferFunction([1.15, 0.17], [1, 0.739, 0.921])

# Shared time vector so all step plots are on the same horizon.
# PI/PID on a type-0 plant introduces an integrator: closed-loop approach to 1.0
# can take >60s with Ki=0.5, so we use a long horizon to capture steady state.
T_FINAL = 120.0
T = np.linspace(0.0, T_FINAL, 12001)


def pid_tf(Kp: float, Ki: float = 0.0, Kd: float = 0.0) -> ct.TransferFunction:
    """PID controller in the instructor's corrected form: num=[Kd,Kp,Ki], den=[1,0]."""
    return ct.TransferFunction([Kd, Kp, Ki], [1, 0])


def step_metrics(sys: ct.TransferFunction, target: float = 1.0,
                 t: np.ndarray = T) -> dict:
    """Return final value, steady-state error, peak value, and settle time (2%)."""
    t_out, y = ct.step_response(sys, T=t)
    final_val = float(y[-1])
    ss_err = float(target - final_val)
    peak = float(np.max(y))

    # Settle time: last time the response is outside 2% of target
    tol = 0.02 * target
    outside = np.where(np.abs(y - target) > tol)[0]
    settle = float(t_out[outside[-1]]) if outside.size else 0.0

    return {
        "final_value": final_val,
        "ss_error": ss_err,
        "peak_value": peak,
        "settle_time_2pct": settle,
        "t": t_out,
        "y": y,
    }


def save_fig(fig, name: str) -> None:
    out = HERE / name
    fig.savefig(out, dpi=130, bbox_inches="tight")
    print(f"  saved {out.name}")


# ---------------------------------------------------------------------------
# Task 1 --- Open-loop response
# ---------------------------------------------------------------------------
print("Task 1: Open-loop step response")
m1 = step_metrics(G)
fig1, ax = plt.subplots(figsize=(7, 4))
ax.plot(m1["t"], m1["y"], "b", lw=1.6, label="Open-loop G(s)")
ax.axhline(1.0, color="k", ls="--", lw=0.8, label="Target = 1.0")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Pitch $\\theta$ (rad or normalized unit)")
ax.set_title("Task 1: Open-Loop Pitch Response (No Autopilot)")
ax.grid(alpha=0.3)
ax.legend()
save_fig(fig1, "task1_open_loop.png")
plt.close(fig1)


# ---------------------------------------------------------------------------
# Task 2 --- Proportional control (Kp = 2)
# ---------------------------------------------------------------------------
print("Task 2: P-control (Kp=2)")
Kp = 2.0
Cp = Kp  # scalar gain works as a transfer function for feedback()
Tp = ct.feedback(Cp * G, 1)
m2 = step_metrics(Tp)

fig2, ax = plt.subplots(figsize=(7, 4))
ax.plot(m2["t"], m2["y"], "g", lw=1.6, label=f"P-control Kp={Kp}")
ax.axhline(1.0, color="k", ls="--", lw=0.8, label="Target = 1.0")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Pitch $\\theta$")
ax.set_title("Task 2: Closed-Loop P-Control Response")
ax.grid(alpha=0.3)
ax.legend()
save_fig(fig2, "task2_p_control.png")
plt.close(fig2)


# ---------------------------------------------------------------------------
# Task 3 --- PI control (Kp = 2, Ki = 0.5)
# ---------------------------------------------------------------------------
print("Task 3: PI-control (Kp=2, Ki=0.5)")
Ki = 0.5
Cpi = pid_tf(Kp, Ki=Ki, Kd=0.0)
Tpi = ct.feedback(Cpi * G, 1)
m3 = step_metrics(Tpi)

fig3, ax = plt.subplots(figsize=(7, 4))
ax.plot(m3["t"], m3["y"], "m", lw=1.6, label=f"PI Kp={Kp}, Ki={Ki}")
ax.axhline(1.0, color="k", ls="--", lw=0.8, label="Target = 1.0")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Pitch $\\theta$")
ax.set_title("Task 3: Closed-Loop PI-Control Response")
ax.grid(alpha=0.3)
ax.legend()
save_fig(fig3, "task3_pi_control.png")
plt.close(fig3)


# ---------------------------------------------------------------------------
# Task 4 --- PID control (Kp = 2, Ki = 0.5, Kd = 1.5)
# ---------------------------------------------------------------------------
print("Task 4: PID-control (Kp=2, Ki=0.5, Kd=1.5) + Kd sweep")
Kd = 1.5
Cpid = pid_tf(Kp, Ki=Ki, Kd=Kd)
Tpid = ct.feedback(Cpid * G, 1)
m4 = step_metrics(Tpid)

# Plot PID vs PI on the same axes
fig4, ax = plt.subplots(figsize=(7, 4))
ax.plot(m3["t"], m3["y"], "b", lw=1.4, label="PI Control")
ax.plot(m4["t"], m4["y"], "r", lw=1.6, label="PID Control")
ax.axhline(1.0, color="k", ls="--", lw=0.8, label="Target = 1.0")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Pitch $\\theta$")
ax.set_title("Task 4: PID vs PI Control")
ax.grid(alpha=0.3)
ax.legend()
save_fig(fig4, "task4_pid_vs_pi.png")
plt.close(fig4)

# Kd sweep --- tune until jitter is reduced but speed is still reasonable
print("Task 4 (extra): Kd sweep")
kd_values = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
fig5, ax = plt.subplots(figsize=(8, 4.5))
sweep_results = []
for kd_val in kd_values:
    T_sw = ct.feedback(pid_tf(Kp, Ki=Ki, Kd=kd_val) * G, 1)
    m = step_metrics(T_sw)
    ax.plot(m["t"], m["y"], lw=1.3,
            label=f"Kd={kd_val}  peak={m['peak_value']:.3f}  ts={m['settle_time_2pct']:.2f}s")
    sweep_results.append({"Kd": kd_val, **{k: v for k, v in m.items() if k not in ("t", "y")}})
ax.axhline(1.0, color="k", ls="--", lw=0.8, label="Target")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Pitch $\\theta$")
ax.set_title(f"Task 4 Tuning: Kd Sweep (Kp={Kp}, Ki={Ki})")
ax.grid(alpha=0.3)
ax.legend(loc="lower right", fontsize=8)
save_fig(fig5, "task4_kd_sweep.png")
plt.close(fig5)


# ---------------------------------------------------------------------------
# Summary table --- all four tasks
# ---------------------------------------------------------------------------
summary = {
    "Open-Loop":           {k: v for k, v in m1.items() if k not in ("t", "y")},
    f"P  (Kp={Kp})":        {k: v for k, v in m2.items() if k not in ("t", "y")},
    f"PI (Kp={Kp},Ki={Ki})": {k: v for k, v in m3.items() if k not in ("t", "y")},
    f"PID (Kp={Kp},Ki={Ki},Kd={Kd})": {k: v for k, v in m4.items() if k not in ("t", "y")},
}

print("\n" + "=" * 80)
print(f"{'Controller':<28s} {'Final':>10s} {'SS Err':>10s} {'Peak':>10s} {'ts(2%)':>10s}")
print("-" * 80)
for name, m in summary.items():
    print(f"{name:<28s} {m['final_value']:>10.4f} {m['ss_error']:>10.4f} "
          f"{m['peak_value']:>10.4f} {m['settle_time_2pct']:>10.3f}")
print("=" * 80)

print("\nKd sweep results:")
print(f"{'Kd':>6s} {'Final':>10s} {'SS Err':>10s} {'Peak':>10s} {'ts(2%)':>10s}")
for r in sweep_results:
    print(f"{r['Kd']:>6.2f} {r['final_value']:>10.4f} {r['ss_error']:>10.4f} "
          f"{r['peak_value']:>10.4f} {r['settle_time_2pct']:>10.3f}")

# Save metrics as JSON for the report
(HERE / "lab_data.json").write_text(json.dumps(
    {"summary": summary, "kd_sweep": sweep_results}, indent=2))
print(f"\nSaved metrics to {HERE / 'lab_data.json'}")
