"""Sinusoid generation and time/frequency-domain plotting.

Lab 0. Lower-level plotting helpers called by recipes.py. Each builds one
figure with the waveform on top and its magnitude spectrum below.

Every plot overlays two samplings of the same signal:
  - dense  (Nd = 1024 samples) drawn as a line, standing in for the
    underlying continuous-time signal;
  - sparse (Ns = 64 samples)  drawn as dots, the signal as actually
    sampled. The DFT is always taken of the sparse sequence.

Comparing the two is the point of the lab: it shows what sampling keeps
and what it discards.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def plot_one_sinusoid_td_fd(Am, Fr, Ph, t_d, t_s, Ns, Fs_s, Freq_s):
    """Plot a single sinusoid in time and frequency.

    Signal:   x(t) = Am * cos(2*pi*Fr*t + Ph)
    Spectrum: X[k] = sum_{n=0}^{N-1} x[n] * exp(-j*2*pi*k*n/N)

    A real sinusoid has two spectral lines, at +Fr and -Fr, each of
    magnitude Am*Ns/2 when Fr falls exactly on a DFT bin.

    Returns the figure plus both sampled sequences, so the caller can sum
    them without regenerating the signal.
    """
    # Same signal at both sample rates. Sparse is what gets transformed;
    # dense is only drawn, to show the waveform the samples came from.
    x_s = Am * np.cos(2*np.pi*Fr*t_s + Ph)
    x_d = Am * np.cos(2*np.pi*Fr*t_d + Ph)

    # DFT of the sampled signal. fftshift moves zero frequency to the centre
    # so the two lines appear symmetrically about 0 Hz rather than split
    # across the array ends.
    X_s = np.fft.fft(x_s)
    X_F = np.abs(np.fft.fftshift(X_s))

    # Bin index of the positive-frequency line, used to annotate its value.
    # Exact only because the lab's frequencies land on bin centres.
    Freqint1 = int(np.round(Fr*Ns/Fs_s))

    # DEVIATION FROM HANDOUT: handout has `plt.figure(1)` here.
    # This function is called twice (fig1 and fig2). pyplot returns the SAME
    # Figure object for a repeated number, so the second call drew on top of
    # the first: `fig1 is fig2` was True and both SVGs were one overplotted
    # figure with 4 lines instead of 2.
    # It only breaks when saving. Interactively, plt.show() blocks and closing
    # the window destroys figure 1, so the next call gets a fresh one --
    # which is why the handout code looks fine in a GUI run.
    # Bare plt.figure() auto-numbers (1, then 2), matching the handout's intent
    # and leaving the explicit figure(3)/figure(4) calls below untouched.
    fig_plot = plt.figure()

    # Top: sparse samples as dots over the dense waveform as a line.
    plt.subplot(211)
    plt.plot(t_s, x_s, 'o', t_d, x_d)
    plt.axis([0, t_d[-1], -1.5, +1.5])
    plt.xlabel('Time')
    plt.ylabel('Waveform')

    # Bottom: magnitude spectrum, annotated with the complex DFT value at the
    # positive-frequency line. Real and imaginary parts encode the phase Ph.
    fig_text = f"{X_s[Freqint1].real:.3e} + j{X_s[Freqint1].imag:.3e}"
    plt.subplot(212)
    plt.stem(Freq_s, X_F)
    plt.text(Fr-2, np.abs(X_s[Freqint1])+3, fig_text)
    plt.axis([Freq_s[0], Freq_s[-1], 0, 45])
    plt.xlabel('Freq')
    plt.ylabel('Spectrum')

    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    plt.show()   # no-op when MPLBACKEND=Agg; opens a window under a GUI
    return fig_plot, x_d, x_s


def plot_multi_sinusoids_td_fd_sum(x_d, x_s, t_d, t_s, Ns2, Freq_s):
    """Plot a superposition given the already-summed sequences.

    Takes signals the caller has already added together. Because the DFT is
    linear, the spectrum of the sum is the sum of the spectra -- so each
    component keeps its own line and they do not interfere.
    """
    X_s = np.fft.fft(x_s)
    X_F = np.abs(np.fft.fftshift(X_s))

    # Locate the lines automatically -- with several components their
    # positions are no longer known in advance. Search only the first half
    # (0:Ns2): the spectrum of a real signal is conjugate-symmetric, so the
    # negative half is redundant.
    peakinds, _ = signal.find_peaks(np.abs(X_s[0:Ns2]), height=1)

    fig_plot = plt.figure(3)
    plt.subplot(211)
    plt.plot(t_s, x_s, 'o', t_d, x_d)
    plt.axis([0, t_d[-1], -1.5, +1.5])
    plt.xlabel('Time')
    plt.ylabel('Waveform')

    # Annotate every detected line with its complex value.
    plt.subplot(212)
    plt.stem(Freq_s, X_F)
    for peak in peakinds:
        fig_text = f"{X_s[peak].real:.3e} + j{X_s[peak].imag:.3e}"
        plt.text(peak-2, np.abs(X_s[peak])+3, fig_text)
    plt.axis([Freq_s[0], Freq_s[-1], 0, 45])
    plt.xlabel('Freq')
    plt.ylabel('Spectrum')

    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    plt.show()
    return fig_plot


def plot_multi_sinusoids_td_fd_parameters(Am, Fm, Pm, t_d, t_s, Ns2, Freq_s):
    """Plot a superposition built from parameter vectors.

    Same result as plot_multi_sinusoids_td_fd_sum, reached differently:
    here the components are generated from vectors of amplitude, frequency
    and phase rather than being passed in pre-summed.

        x(t) = sum_i Am[i] * cos(2*pi*Fm[i]*t + Pm[i])

    The two sample rates deliberately use two different implementations of
    that same sum -- an explicit loop and a vectorised outer product -- so
    the lab can show they agree.
    """
    # Sparse: accumulate one component at a time.
    x_s = np.zeros_like(t_s)
    for i in range(len(Am)):
        x_s += Am[i] * np.cos(2*np.pi*Fm[i]*t_s + Pm[i])

    # Dense: same sum with no Python loop. The outer product t_d (column) by
    # Fm (row) gives every (time, frequency) pair at once; broadcasting adds
    # the phases and scales by the amplitudes; axis=1 sums the components.
    x_d = np.sum(
        Am.reshape(1, -1)
        * np.cos(2*np.pi*np.dot(t_d.reshape(-1, 1), Fm.reshape(1, -1))
                 + Pm.reshape(1, -1)),
        axis=1
    )

    X_s = np.fft.fft(x_s)
    X_F = np.abs(np.fft.fftshift(X_s))
    peakinds, _ = signal.find_peaks(np.abs(X_s[0:Ns2]), height=1)

    fig_plot = plt.figure(4)
    plt.subplot(211)
    plt.plot(t_s, x_s, 'o', t_d, x_d)
    plt.axis([0, t_d[-1], -1.5, +1.5])
    plt.xlabel('Time')
    plt.ylabel('Waveform')

    plt.subplot(212)
    plt.stem(Freq_s, X_F)
    for peak in peakinds:
        fig_text = f"{X_s[peak].real:.3e} + j{X_s[peak].imag:.3e}"
        plt.text(peak-2, np.abs(X_s[peak])+3, fig_text)
    plt.axis([Freq_s[0], Freq_s[-1], 0, 45])
    plt.xlabel('Freq')
    plt.ylabel('Spectrum')

    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    plt.show()
    return fig_plot
