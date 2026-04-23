"""CEC 300 In-Class Lab: Fixed-Wing Aircraft Pitch Controller

Pure standard-library implementation. Runs on Windows, macOS, and Linux with
any Python 3.7+. No `pip install` required to get the numerical results.

If matplotlib happens to be installed, the five figures are regenerated into
the `cec300labimgs/` folder. Otherwise the script still runs and prints the
numbers used in the lab report.

Plant model (from Section 2 of the lab guide):
    G(s) = theta(s) / delta_e(s)
         = (1.15 s + 0.17) / (s^2 + 0.739 s + 0.921)

Controller form (instructor's corrected coefficient order):
    C(s) = Kp + Ki/s + Kd*s = (Kd s^2 + Kp s + Ki) / s
    => num = [Kd, Kp, Ki], den = [1, 0]

Tasks:
    1. Open-loop step response of G(s)
    2. Proportional control, Kp = 2
    3. PI control, Kp = 2, Ki = 0.5
    4. PID control, Kp = 2, Ki = 0.5, Kd = 1.5 (with Kd tuning sweep)
"""

import json
from pathlib import Path

# matplotlib is optional. If it is not installed the script still runs.
try:
    import matplotlib
    matplotlib.use("Agg")  # no display required; safe on all platforms
    import matplotlib.pyplot as plt
    HAVE_PLT = True
except ImportError:
    HAVE_PLT = False

HERE = Path(__file__).resolve().parent
IMG_DIR = HERE / "cec300labimgs"
IMG_DIR.mkdir(exist_ok=True)

# =========================================================================
# Polynomial / transfer function helpers.
# Coefficient lists are ordered from highest power of s down to the constant.
# Example: 2*s^2 + 3*s + 4  ->  [2, 3, 4].
# =========================================================================

def poly_mul(a, b):
    """Multiply two polynomials and return the product coefficient list."""
    out = [0.0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def poly_add(a, b):
    """Add two polynomials, padding the shorter with leading zeros."""
    n = max(len(a), len(b))
    a = [0.0] * (n - len(a)) + list(a)
    b = [0.0] * (n - len(b)) + list(b)
    return [x + y for x, y in zip(a, b)]


def closed_loop_unity(num_c, den_c, num_g, den_g):
    """Unity-feedback closed-loop transfer function T = C*G / (1 + C*G)."""
    num_cg = poly_mul(num_c, num_g)
    den_cg = poly_mul(den_c, den_g)
    num_T = num_cg
    den_T = poly_add(num_cg, den_cg)
    return num_T, den_T


def tf_to_state_space(num, den):
    """Convert a proper transfer function to controllable canonical form.

    Returns (A, B, C, D) where A is a list of lists, B and C are lists,
    and D is a scalar. Assumes the transfer function is proper, i.e.
    len(num) <= len(den). After forming closed-loop feedback this is
    always the case for the controllers used in this lab.
    """
    if len(num) > len(den):
        raise ValueError("Transfer function must be proper (deg(num) <= deg(den)).")

    scale = den[0]
    num = [x / scale for x in num]
    den = [x / scale for x in den]

    n = len(den) - 1  # system order
    # Left-pad numerator to length n+1 so b0, b1, ..., bn line up with den.
    num_padded = [0.0] * (len(den) - len(num)) + num

    D = num_padded[0]  # direct feed-through; zero for strictly proper plants

    # A is the companion matrix of den (without the monic leading coefficient).
    A = [[0.0] * n for _ in range(n)]
    for i in range(n - 1):
        A[i][i + 1] = 1.0
    for j in range(n):
        A[n - 1][j] = -den[n - j]

    B = [0.0] * n
    if n > 0:
        B[n - 1] = 1.0

    # C_i = b_{n-i} - b_0 * a_{n-i}
    C = [num_padded[n - j] - num_padded[0] * den[n - j] for j in range(n)]

    return A, B, C, D


def rk4_simulate(A, B, C, D, u_of_t, t_final, n_steps):
    """Classical 4th-order Runge-Kutta integration of dx/dt = Ax + Bu, y = Cx + Du."""
    n = len(B)
    dt = t_final / n_steps
    x = [0.0] * n
    ts = [0.0] * (n_steps + 1)
    ys = [0.0] * (n_steps + 1)

    def dxdt(state, u):
        out = [0.0] * n
        for i in range(n):
            s = 0.0
            for j in range(n):
                s += A[i][j] * state[j]
            out[i] = s + B[i] * u
        return out

    for k in range(n_steps + 1):
        t = k * dt
        ts[k] = t
        u = u_of_t(t)
        y = D * u
        for j in range(n):
            y += C[j] * x[j]
        ys[k] = y

        if k < n_steps:
            u_mid = u_of_t(t + dt / 2.0)
            u_next = u_of_t(t + dt)
            k1 = dxdt(x, u)
            x2 = [xi + (dt / 2.0) * ki for xi, ki in zip(x, k1)]
            k2 = dxdt(x2, u_mid)
            x3 = [xi + (dt / 2.0) * ki for xi, ki in zip(x, k2)]
            k3 = dxdt(x3, u_mid)
            x4 = [xi + dt * ki for xi, ki in zip(x, k3)]
            k4 = dxdt(x4, u_next)
            x = [xi + (dt / 6.0) * (k1i + 2 * k2i + 2 * k3i + k4i)
                 for xi, k1i, k2i, k3i, k4i in zip(x, k1, k2, k3, k4)]

    return ts, ys


def step_metrics(ts, ys, target=1.0):
    """Final value, steady-state error, peak value, 2% settle time."""
    final_val = ys[-1]
    ss_err = target - final_val
    peak = max(ys)
    tol = 0.02 * target
    settle = 0.0
    for i, y in enumerate(ys):
        if abs(y - target) > tol:
            settle = ts[i]
    return {
        "final_value": final_val,
        "ss_error": ss_err,
        "peak_value": peak,
        "settle_time_2pct": settle,
    }


# =========================================================================
# Plant and controllers
# =========================================================================

NUM_G = [1.15, 0.17]
DEN_G = [1.0, 0.739, 0.921]


def pid_controller(Kp, Ki=0.0, Kd=0.0):
    """PID in the instructor's corrected form: num=[Kd,Kp,Ki], den=[1,0]."""
    return [Kd, Kp, Ki], [1.0, 0.0]


T_FINAL = 120.0
N_STEPS = 12000  # dt = 0.01 s; ample accuracy for omega_n ~ 1 rad/s

def step_input(t):
    return 1.0 if t >= 0.0 else 0.0


def simulate(num_T, den_T, label):
    """Simulate a closed-loop TF to a unit step and print metrics."""
    A, B, C, D = tf_to_state_space(num_T, den_T)
    ts, ys = rk4_simulate(A, B, C, D, step_input, T_FINAL, N_STEPS)
    m = step_metrics(ts, ys)
    print(f"  {label:34s} final={m['final_value']:7.4f} "
          f"sse={m['ss_error']:7.4f} peak={m['peak_value']:7.4f} "
          f"ts={m['settle_time_2pct']:7.3f}s")
    return ts, ys, m


def save_single_plot(ts, ys, title, fname, color="b"):
    if not HAVE_PLT:
        return
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(ts, ys, color, lw=1.6, label=title)
    ax.axhline(1.0, color="k", linestyle="--", lw=0.8, label="Target = 1.0")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Pitch theta")
    ax.set_title(title)
    ax.grid(alpha=0.3)
    ax.legend()
    out = IMG_DIR / fname
    fig.savefig(out, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"    saved {out.name}")


# =========================================================================
# Run all tasks
# =========================================================================

print("CEC 300 Pitch Controller Lab --- pure-stdlib simulation")
if not HAVE_PLT:
    print("(matplotlib not installed; plots will be skipped, numbers will still print)")
print("=" * 90)

# Task 1: open-loop, the plant by itself
ts1, ys1, m1 = simulate(NUM_G, DEN_G, "Task 1  Open-loop G(s)")
save_single_plot(ts1, ys1,
                 "Task 1: Open-Loop Pitch Response (No Autopilot)",
                 "task1_open_loop.png", color="b")

# Task 2: P-control with Kp = 2
Kp = 2.0
num_T, den_T = closed_loop_unity([Kp], [1.0], NUM_G, DEN_G)
ts2, ys2, m2 = simulate(num_T, den_T, f"Task 2  P  Kp={Kp}")
save_single_plot(ts2, ys2,
                 "Task 2: Closed-Loop P-Control Response",
                 "task2_p_control.png", color="g")

# Task 3: PI-control with Kp = 2, Ki = 0.5
Ki = 0.5
num_c, den_c = pid_controller(Kp, Ki=Ki)
num_T, den_T = closed_loop_unity(num_c, den_c, NUM_G, DEN_G)
ts3, ys3, m3 = simulate(num_T, den_T, f"Task 3  PI Kp={Kp} Ki={Ki}")
save_single_plot(ts3, ys3,
                 "Task 3: Closed-Loop PI-Control Response",
                 "task3_pi_control.png", color="m")

# Task 4: PID-control with Kp = 2, Ki = 0.5, Kd = 1.5
Kd = 1.5
num_c, den_c = pid_controller(Kp, Ki=Ki, Kd=Kd)
num_T, den_T = closed_loop_unity(num_c, den_c, NUM_G, DEN_G)
ts4, ys4, m4 = simulate(num_T, den_T, f"Task 4  PID Kp={Kp} Ki={Ki} Kd={Kd}")

if HAVE_PLT:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(ts3, ys3, "b", lw=1.4, label="PI Control")
    ax.plot(ts4, ys4, "r", lw=1.6, label="PID Control")
    ax.axhline(1.0, color="k", linestyle="--", lw=0.8, label="Target = 1.0")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Pitch theta")
    ax.set_title("Task 4: PID vs PI Control")
    ax.grid(alpha=0.3)
    ax.legend()
    out = IMG_DIR / "task4_pid_vs_pi.png"
    fig.savefig(out, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"    saved {out.name}")

# Kd sweep
print("\nKd sweep (Kp = %.1f, Ki = %.1f):" % (Kp, Ki))
kd_values = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
sweep = []
sweep_curves = []
for kdv in kd_values:
    nc, dc = pid_controller(Kp, Ki=Ki, Kd=kdv)
    nt, dt_ = closed_loop_unity(nc, dc, NUM_G, DEN_G)
    ts_s, ys_s, m_s = simulate(nt, dt_, f"  Kd={kdv}")
    sweep.append({"Kd": kdv, **m_s})
    sweep_curves.append((kdv, ts_s, ys_s, m_s))

if HAVE_PLT:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for kdv, t_s, y_s, m_s in sweep_curves:
        ax.plot(t_s, y_s, lw=1.3,
                label=f"Kd={kdv}  peak={m_s['peak_value']:.3f}  "
                      f"ts={m_s['settle_time_2pct']:.2f}s")
    ax.axhline(1.0, color="k", linestyle="--", lw=0.8, label="Target")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Pitch theta")
    ax.set_title(f"Task 4 Tuning: Kd Sweep (Kp={Kp}, Ki={Ki})")
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right", fontsize=8)
    out = IMG_DIR / "task4_kd_sweep.png"
    fig.savefig(out, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"    saved {out.name}")

# Save metrics as JSON so the report-table values can be audited
summary = {
    "Open-Loop": m1,
    "P (Kp=%g)" % Kp: m2,
    "PI (Kp=%g, Ki=%g)" % (Kp, Ki): m3,
    "PID (Kp=%g, Ki=%g, Kd=%g)" % (Kp, Ki, Kd): m4,
}
(HERE / "lab_data.json").write_text(
    json.dumps({"summary": summary, "kd_sweep": sweep}, indent=2))
print(f"\nSaved metrics to {HERE / 'lab_data.json'}")
print("Done.")
