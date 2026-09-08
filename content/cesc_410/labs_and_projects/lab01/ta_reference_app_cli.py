import typer
from dsp26.lab0_sinusoids.recipes import plot_sinusoids_td_fd_
from dsp26.lab1_audio_sig.recipes import play_plot_audio_


app = typer.Typer()

__version__ = "0.1.0"


########################################################################
# Print out the version: dsp26 --version
def print_version(value: bool):
    if value:
        typer.echo(f"Version of dsp26: {__version__}")
        raise typer.Exit()


# Add the version option.
@app.callback()
def callback(
    version: bool = typer.Option(
        None, "--version", callback=print_version, is_eager=True
    )
):
    pass


########################################################################
# Lab0-sinusoids
@app.command()
def plot_sinusoids_td_fd(
    folder_name: str = typer.Option(
        "",
        "--folder-name",
        help="Optional output folder name for saving generated plots. "
        "If set, plots will be written under <folder-name>/figs.",
    ),
):
    """Plot time-domain waveform and frequency-domain spectrum of sinusoids.
    Use --folder-name to save figures to <folder-name>/figs."""
    plot_sinusoids_td_fd_(folder_name=folder_name)


########################################################################
# Lab1-audio-sig
@app.command()
def play_plot_audio(
    path_name: str = typer.Option(
        "",
        "--path-name",
        help="Optional output path name for loading an audio file. "
        "If set, the specified audio file will be loaded.",
    ),
):
    """Play and plot audio signal.
    Use --path-name to load audio file from."""
    play_plot_audio_(path_name=path_name)