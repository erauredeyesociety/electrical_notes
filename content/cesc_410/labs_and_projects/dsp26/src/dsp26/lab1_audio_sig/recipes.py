"""Lab 1 orchestration: play an audio file, then plot it five ways.

Bridges the CLI command in app_cli.py to the helpers in audio_sig.py and
audio_player.py, matching the structure Lab 0 established.

The five figures, in the order the handout produces them:

  1. waveform, whole file
  2. waveform, zoomed to [start_s, end_s]      <- the programming task
  3. spectrogram, linear frequency axis
  4. spectrogram, log frequency axis
  5. spectrogram, mel frequency axis
"""

import os
from pathlib import Path

import librosa

from dsp26.lab1_audio_sig.audio_player import play_audio
from dsp26.lab1_audio_sig.audio_sig import (
    print_wave_file_properties,
    plot_audio_sig_in_td,
    plot_audio_sig_in_fd,
)


# The handout's Figure 2 window. Used when the caller asks for neither bound,
# so a no-argument run still reproduces the handout's five figures exactly.
# See the note in play_plot_audio_ for why this is not simply the default.
HANDOUT_ZOOM_S = (0.4, 1.4)


def play_plot_audio_(
    path_name: str = "",
    start_s: float = 0.0,
    end_s: float = None,
    folder_name: str = "",
):
    """Play an audio file and produce the lab's five figures.

    start_s / end_s select the window for Figure 2. Their defaults are the
    defaults of plot_audio_sig_in_td, as the handout's programming task
    requires -- not the handout's own 0.4/1.4, which are the values it passes
    at the call site rather than declares in the signature.

    Because 0.0/None means "the whole file", a no-argument run would otherwise
    make Figure 2 a duplicate of Figure 1. When neither bound is supplied we
    therefore fall back to HANDOUT_ZOOM_S, so the default output still matches
    the handout while any explicit window is honoured.
    """
    if path_name:
        audio_file_path = path_name
    else:
        # Get the directory containing this Python file:
        # dsp26/src/dsp26/lab1_audio_sig/recipes.py
        current_dir = Path(__file__).resolve().parent
        # Go up:
        # lab1_audio_sig -> dsp26 -> src -> project root (dsp26)
        project_root = current_dir.parents[2]
        # Construct the audio file path
        audio_file_path = project_root / "audio_files" / "2086-149220-0033.wav"

    # DEVIATION FROM HANDOUT: the handout calls play_audio unconditionally.
    # It opens a Tk window and BLOCKS in mainloop() until a human closes it,
    # so an unattended run hangs forever instead of producing figures.
    #
    # The skip is keyed on MPLBACKEND=Agg, not on DISPLAY. Checking DISPLAY was
    # tried first and is wrong: this machine has one (DISPLAY=:1), so a batch
    # run still opened a window and waited for a click that was never coming.
    # Agg is the project's existing "batch, no windows" signal -- see
    # reference_docs/known_issues.md KI-02, which already documents
    # `MPLBACKEND=Agg uv run dsp26 ...` as the headless path.
    #
    # Interactively -- `dsp26 play-plot-audio` under a desktop, which is how
    # the lab is demonstrated and screenshotted -- MPLBACKEND is unset, the
    # player opens, and the behaviour is exactly what the handout describes.
    batch = os.environ.get("MPLBACKEND", "").lower() == "agg"
    if batch:
        print("MPLBACKEND=Agg -- batch run, skipping the audio player window. "
              "Run without it under a desktop session to hear the file.")
    else:
        play_audio(audio_file_path)

    print_wave_file_properties(audio_file_path)

    # sr=None keeps the file's own sample rate instead of resampling to
    # librosa's 22050 Hz default, so the printed rate and the spectrogram
    # axes describe the actual recording.
    audio, sample_rate = librosa.load(audio_file_path, sr=None)

    # Figure 2's window: honour whatever the caller asked for, and only fall
    # back to the handout's zoom when neither bound was given.
    if start_s == 0.0 and end_s is None:
        zoom_start, zoom_end = HANDOUT_ZOOM_S
    else:
        zoom_start, zoom_end = start_s, end_s

    fig1 = plot_audio_sig_in_td(audio, sample_rate)
    fig2 = plot_audio_sig_in_td(audio, sample_rate, zoom_start, zoom_end)

    fig3 = plot_audio_sig_in_fd(audio, sample_rate)
    fig4 = plot_audio_sig_in_fd(audio, sample_rate, 'log')
    fig5 = plot_audio_sig_in_fd(audio, sample_rate, 'mel')

    # DEVIATION FROM HANDOUT: saving to file is not in the handout, which
    # relies on plt.show() and a screenshot. Headless that produces nothing
    # (KI-02), so --folder-name writes the same five figures to disk. Both
    # SVG and PNG: the report needs PNG, SVG is the handout's own choice
    # elsewhere in the course.
    if folder_name:
        figs_dir = Path(folder_name) / "figs"
        figs_dir.mkdir(parents=True, exist_ok=True)
        names = [
            (fig1, "lab1_audio_fig1_waveform_full"),
            (fig2, "lab1_audio_fig2_waveform_zoom"),
            (fig3, "lab1_audio_fig3_spec_linear"),
            (fig4, "lab1_audio_fig4_spec_log"),
            (fig5, "lab1_audio_fig5_spec_mel"),
        ]
        for fig, stem in names:
            for ext in ("svg", "png"):
                fig.savefig(figs_dir / f"{stem}.{ext}")
        print(f"Figures Saved in {folder_name}")
