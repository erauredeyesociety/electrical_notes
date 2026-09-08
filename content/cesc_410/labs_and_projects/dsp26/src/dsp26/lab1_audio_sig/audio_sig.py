"""Audio analysis helpers for Lab 1: metadata, waveform, and spectrogram.

Transcribed from the Lab 1 handout. Three jobs:

  print_wave_file_properties   read the WAV header and report it
  plot_audio_sig_in_td         time-domain waveform over a chosen window
  plot_audio_sig_in_fd         frequency-domain view via the STFT

The short-time Fourier transform behind the two spectral views is

    X(m, k) = sum_{n=0}^{N-1} x[n + mH] w[n] exp(-j 2 pi k n / N)

with window length N = win_length, hop H = hop_length, and w a Hann window.
At the lab's 16 kHz sample rate the handout's 400/160 sample settings are a
25 ms window advanced every 10 ms -- the standard speech-processing framing,
long enough to resolve pitch harmonics and short enough to track a syllable.
"""

import wave

import librosa.display
import matplotlib.pyplot as plt
import numpy as np


## Print various parameters of an audio file
# Open the WAV file in read mode to access the properties
def print_wave_file_properties(wav_file_path):
    """Report the WAV header fields the lab asks students to identify."""
    wav_file_path = str(wav_file_path)
    with wave.open(wav_file_path, 'r') as wav_file:
        print(f"\nDetailed properties of {wav_file_path} ------------------")
        # Number of audio channels
        n_channels = wav_file.getnchannels()
        print("Number of channels:", n_channels)

        # Sample width in bytes
        sample_width = wav_file.getsampwidth()
        print("Sample width (bytes):", sample_width)

        # Frame rate (sample rate)
        frame_rate = wav_file.getframerate()
        print("Frame rate (sample rate):", frame_rate)

        # Number of audio frames
        n_frames = wav_file.getnframes()
        print("Number of frames:", n_frames)

        # Duration of the audio in seconds
        duration = n_frames / float(frame_rate)
        print("Duration (seconds):", duration)
        # Other properties can be accessed similarly


# Display the waveform from start_s to end_s seconds
def plot_audio_sig_in_td(audio, sample_rate, start_s=0.0, end_s=None):
    """Plot the waveform between start_s and end_s.

    end_s=None means "to the end of the file". The x-axis is drawn 0-based
    because waveshow re-zeros the segment it is given, then relabelled with
    the true start and end times so the figure reads correctly.
    """
    # Convert the requested times to sample indices before slicing.
    start_idx = int(start_s * sample_rate)
    if end_s == None:
        end_idx = len(audio)
        end_s = end_idx / sample_rate
    else:
        end_idx = int(end_s * sample_rate)

    segment = audio[start_idx:end_idx]
    time_length = len(segment) / sample_rate

    # DEVIATION FROM HANDOUT: bare plt.figure() rather than a numbered one.
    # The handout already does this here, and it must stay that way -- a
    # hard-coded number returns the SAME Figure on a second call, so the two
    # time-domain plots would overplot into one plot and save identical
    # images. That is known issue KI-01, found in Lab 0.
    fig = plt.figure(figsize=(16, 9))
    librosa.display.waveshow(segment, sr=sample_rate, color="blue")

    ax = plt.gca()
    ax.set_xlim(0, time_length)          # keep the selected window visible
    ax.set_xticks([0, time_length])      # left and right edge only
    ax.set_xticklabels([f"{start_s}", f"{end_s}"])  # label as start_s/end_s

    plt.title(f"Waveform from {start_s:.1f}s to {end_s:.1f}s")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

    # DEVIATION FROM HANDOUT: the handout returns nothing. The Figure is
    # returned so the caller can save it, which is the only way to produce
    # artifacts headless -- plt.show() is a no-op with no display (KI-02).
    return fig


def plot_audio_sig_in_fd(audio, sample_rate, fd_format='linear'):
    """Plot the STFT magnitude in dB, on a linear, log, or mel axis.

    fd_format selects the frequency axis only; the underlying transform is
    identical in all three. Amplitudes are converted to dB relative to the
    loudest bin, so the colour scale is 0 dB at the peak and negative below.
    """
    # Short-time Fourier transform: 512-point FFT over a 400-sample window,
    # advanced 160 samples at a time.
    spec = librosa.stft(audio, n_fft=512, hop_length=160, win_length=400)
    # Magnitude in decibels, referenced to the maximum, so quiet detail is
    # visible against the loudest partial.
    spec_db = librosa.amplitude_to_db(np.abs(spec), ref=np.max)

    fig = plt.figure(figsize=(16, 9))
    librosa.display.specshow(spec_db, y_axis=fd_format, x_axis='time',
                             sr=sample_rate, hop_length=160)
    plt.colorbar()
    plt.title('Spectrogram of an Audio Signal')
    plt.show()

    # DEVIATION FROM HANDOUT: see plot_audio_sig_in_td -- returned so it can
    # be saved headless.
    return fig
