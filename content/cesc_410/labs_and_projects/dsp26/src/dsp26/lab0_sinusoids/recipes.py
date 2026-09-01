"""Lab 0 parameters and figure orchestration.

Bridges the CLI command in app_cli.py to the plotting helpers in
sinusoids.py. Holds every signal parameter for the lab, so the plotting
code stays generic and this file is the only place numbers are chosen.

Produces four figures:
  1. one sinusoid            A=1,   f=Freq_1
  2. one sinusoid            A=0.5, f=2*Freq_1
  3. sum of 1 and 2, added as signals
  4. sum of three sinusoids, built from parameter vectors
"""

import numpy as np

from dsp26.lab0_sinusoids.sinusoids import (
    plot_one_sinusoid_td_fd,
    plot_multi_sinusoids_td_fd_sum,
    plot_multi_sinusoids_td_fd_parameters,
)


# >>> SET THIS <<<  last 4 digits of your ERAU ID.
# Seeds the RNG that picks Freq_1, so it changes every figure this lab
# produces. The handout ships 1234 as a placeholder; leaving it would mean
# submitting the instructor's example plots rather than your own.
myID = 6127
np.random.seed(seed=myID)

pi = np.pi

# Base frequency, drawn from the seeded RNG so each student gets a different
# signal. floor((10 + U{0..9}) / 3) lands in 3..6 Hz -- low enough to sit well
# inside the sparse Nyquist limit (Fs_s/2 = 32 Hz) even at the 3rd harmonic.
Freq_1 = np.floor((10 + np.random.randint(0, 10)) / 3)
print("The basic frequency is", Freq_1, "Hz.")

# Two samplings of the same one-second window.
#   dense  -- stands in for the continuous signal; drawn as a line
#   sparse -- the signal as actually sampled; drawn as dots, and the only
#             one the DFT is taken of
# The 16x ratio makes the sparse samples visibly discrete against the dense
# curve while still leaving Ns a power of two, so the FFT stays efficient.
Nd = 1024           # dense sample count
Ns = Nd / 16        # sparse sample count -> 64
Ns2 = int(Ns // 2)  # half, for searching only the non-redundant spectrum half
Fs_d = Nd           # dense sample rate (Hz); Nd samples over 1 s
Fs_s = Ns           # sparse sample rate (Hz) -> 64 Hz, Nyquist 32 Hz
t_d = np.arange(Nd) / Fs_d           # dense sample times
t_s = np.arange(Ns) / Fs_s           # sparse sample times

# Two-sided frequency axis for the shifted spectrum: -Fs_s/2 .. +Fs_s/2-1,
# matching what fftshift produces.
Freq_s = np.arange(-Fs_s/2, Fs_s/2)

# Figure 4's three components: a fundamental plus its 2nd and 3rd harmonics,
# with decreasing amplitude. Harmonically related so the sum is periodic.
Am = np.array([1, 0.5, 0.2])                 # amplitudes
Fm = np.array([Freq_1, 2*Freq_1, 3*Freq_1])  # frequencies (Hz)
Pm = np.array([np.pi/4, np.pi/3, np.pi/9])   # phases (rad)


def plot_sinusoids_td_fd_(folder_name: str = ""):
    """Build all four lab figures, optionally saving them.

    With no folder_name the figures are only displayed, which needs a GUI
    backend. Headless, pass a folder and read the files instead.
    """
    # Figures 1 and 2: single sinusoids. Sequences are returned so figure 3
    # can sum them without regenerating.
    A1, F1, P1 = 1, Freq_1, np.pi/4
    fig1, x1_d, x1_s = plot_one_sinusoid_td_fd(A1, F1, P1, t_d, t_s, Ns, Fs_s, Freq_s)

    A2, F2, P2 = 0.5, 2*Freq_1, np.pi/3
    fig2, x2_d, x2_s = plot_one_sinusoid_td_fd(A2, F2, P2, t_d, t_s, Ns, Fs_s, Freq_s)

    # Figure 3: superposition by adding the sampled signals directly.
    # Both spectral lines survive, because the DFT is linear.
    x_s = x1_s + x2_s
    x_d = x1_d + x2_d
    fig3 = plot_multi_sinusoids_td_fd_sum(x_d, x_s, t_d, t_s, Ns2, Freq_s)

    # Figure 4: same idea, three components, built from parameter vectors
    # rather than from pre-summed sequences.
    fig4 = plot_multi_sinusoids_td_fd_parameters(Am, Fm, Pm, t_d, t_s, Ns2, Freq_s)

    if folder_name:
        from pathlib import Path

        figs_dir = Path(folder_name) / "figs"
        figs_dir.mkdir(parents=True, exist_ok=True)

        # DEVIATION FROM HANDOUT: handout saves .svg only. PNG is added
        # because the deliverable is a screenshot of each figure, and SVG is
        # awkward to paste into a report. Drop the ".png" entry to match the
        # handout exactly.
        for ext in ("svg", "png"):
            fig1.savefig(figs_dir / f"lab0_sinusoids_fig1.{ext}")
            fig2.savefig(figs_dir / f"lab0_sinusoids_fig2.{ext}")
            fig3.savefig(figs_dir / f"lab0_sinusoids_fig3.{ext}")
            fig4.savefig(figs_dir / f"lab0_sinusoids_fig4.{ext}")
        print(f"Figures Saved in {folder_name}")
