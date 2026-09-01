"""Top-level CLI for the dsp26 package.

One Typer command per lab, so every lab in the course is reachable as
`dsp26 <command>` without activating the virtual environment. Adding a lab
means adding a subpackage under dsp26/ and one command block here.
"""

import typer
from dsp26.lab0_sinusoids.recipes import plot_sinusoids_td_fd_


app = typer.Typer()

__version__ = "0.1.0"


########################################################################
# Version reporting: `dsp26 --version`
def print_version(value: bool):
    """Print the version and exit, when --version is passed."""
    if value:
        typer.echo(f"Version of dsp26: {__version__}")
        raise typer.Exit()


# Register --version on the app itself rather than on a command, so it works
# as `dsp26 --version` with no subcommand. is_eager makes it run before any
# command argument is parsed.
@app.callback()
def callback(version: bool = typer.Option(
        None, "--version", callback=print_version, is_eager=True)):
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
