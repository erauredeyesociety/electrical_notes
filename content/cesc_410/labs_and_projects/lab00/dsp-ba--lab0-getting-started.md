<!-- bgn hidden -->

-   #2026-08-31: Created based on last year's note and new project

<!-- end hidden -->

<!-- bgn cli -->

# Commands for doc creation:

## Notes for Fall 2026:

```sh
pandoc -N -V fontsize=11pt "dsp-ba--lab0-getting-started.md" -o "dsp/dsp-ba--lab0-getting-started-26.pdf" --data-dir=../../a5ar/pandoc -L select-blocks.lua -M blocks2select="nil" --template=eagle.tex -V linestretch=1.1 -V verbatim-in-note -V codefontsize=9.5 -M geometry="top=2.7cm, bottom=2.8cm, left=2.5cm, right=2.4cm, headsep=0.3cm, footskip=0.9cm" --listings --filter pandoc-crossref -M listings -M titleblock --toc --shift-heading-level-by=-1 -M title="Getting Started with Python Programming for DSP Labs" -M author="Jianhua Liu" -M date="Fall 2026"
```

<!-- end cli -->

<!-- bgn hidden -->

```toc
style: number
min_depth: 1
max_depth: 6
```

<!-- end hidden -->

<!-- bgn ch-title -->

# Getting Started with Python Programming for DSP Labs and Projects

<!-- end ch-title -->

## Introduction

There will be many DSP Lab and class projects. Class projects include the following:

-   Demo code of lectures.
-   Code for HW problems. 
-   Class projects for graduate students.

As we discussed before, we will use Python for all the class related projects. These projects are mostly one or many Python script files.  

One issue with Python projects is the dependency---the many existing libraries that used by source files of the projects. A common way to address the dependency issue is to create a virtual environment for each project. 

There are many different ways to create virtual environments. Here, we use a modern tool, called uv, developed using Rust. See [py-pkg-1c-uv-cs](py-pkg-1c-uv-cs.md) for details about how to install and use uv.

uv will put all the dependency libraries inside a `.venv` folder, which can contain library files up to a few Giga Bytes in size when there are many dependencies. 

To strike a balance between the separation of projects and the size of storage used in a computer, we plan to have all the lab and class projects hosted in a single virtual environment. With this, the functionalities of all different projects of the DSP class are tied up by a single CLI app which can run in a terminal.

[py-pkg-1c-uv-cs](py-pkg-1c-uv-cs.md) shows how to manage Python packages using uv; please read it carefully. We will use the same approach to create and manage a Python package for all lab and class projects for the DSP class.


## Planning of the project

### Project folders

-   Use a single folder to host all source files. Yet, the folder structure is a bit different than a general-purpose project. For a general-purpose project, the source code files are organized according to their functionality. For convenience of DSP project submission, we organize the project files differently---we put the Python script files of each specific project into a single folder, which may contain subfolders.
-   The root folder of the project is named `dsp26`.
-   The parent folder of the `dsp26` folder is `projects`.

### CLI commands for different subprojects

We will use the `app_cli.py` file to host the top level code for Typer. Each project folder under `src/dsp26` will corresponds to a command after `dsp26`. We can use Typer options to add options for each command. This way, we do not need to activate the venv to run the app in a terminal.

### GitHub repo

This part should be skipped by students; it is only for the instructor to keep personal notes.

The local repo is in `dsp26`, and the GitHub repo is under `eraus` directly. 


## Creating the `dsp26` project

### Creating the project locally

We normally use Python that is two versions behind the newest release to make sure the dependencies work well. For projects created in 2026, where the newest release version is 3.14, we use Python 3.12.

On windows, this is done by running the following under the `projects` directory in a terminal: `uv init --package --python 3.12 dsp26`.

### Adding dependencies

We add two different kind of dependencies for this project.

The first is like Typer, used when both running the App or test various functions. Here, we run `uv add typer matplotlib numpy scipy`.

The second is like Pytest, used only during developing of the project. Here, we use  `uv add --dev pytest` to install it only for the develop group.


### Adding initial code directly under `src/dsp26`

#### The `__init__.py` file

This is the entry point of the app.

`__init__.py`:
```python
from dsp26.app_cli import app

def main():
    app()
```


#### The `app_cli.py` file

This is the collection of commands for this app although we only have one for this lab.

`app_cli.py`:
```python
import typer
from dsp26.lab0_sinusoids.recipes import plot_sinusoids_td_fd_


app = typer.Typer()

__version__ = "0.1.0"


########################################################################
# Print out the version: numreps --version
def print_version(value: bool):
    if value:
        typer.echo(f"Version of dsp26: {__version__}")
        raise typer.Exit()


# Add the version option.
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
        help="Optional output folder name for saving generated plots. " \
        "If set, plots will be written under <folder-name>/figs.",
    ),
):
    """Plot time-domain waveform and frequency-domain spectrum of sinusoids.
    Use --folder-name to save figures to <folder-name>/figs."""
    plot_sinusoids_td_fd_(folder_name=folder_name)
```

### Adding lab code under `src/dsp26/lab0_sinusoids`

We have two files here.


#### The `recipes.py` file

This is the file used to bridge the commands in the `app_cli.py` file.

`recipes.py`:
```python
import numpy as np

from dsp26.lab0_sinusoids.sinusoids import (
    plot_one_sinusoid_td_fd,
    plot_multi_sinusoids_td_fd_sum,
    plot_multi_sinusoids_td_fd_parameters,
)


myID = 1234                 # last 4 digits of my ERAU ID
np.random.seed(seed=myID)   # set the seed of the random number generator

pi = np.pi
# (random) frequency of signal in Hz
Freq_1 = np.floor((10 + np.random.randint(0,10)) / 3)
print("The basic frequency is", Freq_1, "Hz.")

Nd = 1024       # total number of samples for dense sampling; d = dense
Ns = Nd / 16    # total number of samples for sparse sampling; s = sparse
Ns2 = int(Ns // 2)  # Ns/2, to be used as the index for array
Fs_d = Nd       # sample rate for dense sampling
Fs_s = Ns       # sample rate for sparse sampling
t_d = np.arange(Nd) / Fs_d              # sample times for dense sampling
t_s = np.arange(Ns) / Fs_s              # sample times for sparse sampling
Freq_s = np.arange(-Fs_s/2, Fs_s/2)     # frequencies for spectrum display

Am = np.array([1, 0.5, 0.2])                 # amplitudes of three signals
Fm = np.array([Freq_1, 2*Freq_1, 3*Freq_1])  # frequencies of three signals
Pm = np.array([np.pi/4, np.pi/3, np.pi/9])   # phases of three signals


def plot_sinusoids_td_fd_(folder_name: str = ""):
    A1, F1, P1 = 1, Freq_1, np.pi/4
    fig1, x1_d, x1_s = plot_one_sinusoid_td_fd(A1, F1, P1, t_d, t_s, Ns, Fs_s, Freq_s)

    A2, F2, P2 = 0.5, 2*Freq_1, np.pi/3
    fig2, x2_d, x2_s = plot_one_sinusoid_td_fd(A2, F2, P2, t_d, t_s, Ns, Fs_s, Freq_s)

    x_s = x1_s + x2_s
    x_d = x1_d + x2_d
    fig3 = plot_multi_sinusoids_td_fd_sum(x_d, x_s, t_d, t_s, Ns2, Freq_s)

    fig4 = plot_multi_sinusoids_td_fd_parameters(Am, Fm, Pm, t_d, t_s, Ns2, Freq_s)

    if folder_name:
        from pathlib import Path

        figs_dir = Path(folder_name) / "figs"
        figs_dir.mkdir(parents=True, exist_ok=True)

        fig1.savefig(figs_dir / "lab0_sinusoids_fig1.svg")
        fig2.savefig(figs_dir / "lab0_sinusoids_fig2.svg")
        fig3.savefig(figs_dir / "lab0_sinusoids_fig3.svg")
        fig4.savefig(figs_dir / "lab0_sinusoids_fig4.svg")
        print(f"Figures Saved in {folder_name}")
```


#### The `sinusoids.py` file

This is the collection of all the lower level functions used for plotting and time-domain waveform and frequency-domain spectrum.

`sinusoids.py`:
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Plot the waveform and spectrum of a single frequency sinusoidal
# signal with Am, Fr, and Ph.
def plot_one_sinusoid_td_fd(Am, Fr, Ph, t_d, t_s, Ns, Fs_s, Freq_s):
    x_s = Am * np.cos(2*np.pi*Fr*t_s + Ph)
    x_d = Am * np.cos(2*np.pi*Fr*t_d + Ph)
    X_s = np.fft.fft(x_s)
    X_F = np.abs(np.fft.fftshift(X_s))
    Freqint1 = int(np.round(Fr*Ns/Fs_s))

    fig_plot = plt.figure(1)
    plt.subplot(211)
    plt.plot(t_s, x_s, 'o', t_d, x_d)
    plt.axis([0, t_d[-1], -1.5, +1.5])
    plt.xlabel('Time')
    plt.ylabel('Waveform')

    fig_text = f"{X_s[Freqint1].real:.3e} + j{X_s[Freqint1].imag:.3e}"
    plt.subplot(212)
    plt.stem(Freq_s, X_F)
    plt.text(Fr-2, np.abs(X_s[Freqint1])+3, fig_text)
    plt.axis([Freq_s[0], Freq_s[-1], 0, 45])
    plt.xlabel('Freq')
    plt.ylabel('Spectrum')

    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    plt.show()
    return fig_plot, x_d, x_s


# Plot the waveform and spectrum of the superposition of multiple
# sinusoidal signals given the summed signals
def plot_multi_sinusoids_td_fd_sum(x_d, x_s, t_d, t_s, Ns2, Freq_s):
    X_s = np.fft.fft(x_s)
    X_F = np.abs(np.fft.fftshift(X_s))
    peakinds, _ = signal.find_peaks(np.abs(X_s[0:Ns2]), height=1)

    fig_plot = plt.figure(3)
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


# Plot the waveform and spectrum of the superposition of multiple
# sinusoidal signals given the parameter vectors
def plot_multi_sinusoids_td_fd_parameters(Am, Fm, Pm, t_d, t_s, Ns2, Freq_s):
    # Generate the sparse sequence using the conventional method
    x_s = np.zeros_like(t_s)
    for i in range(len(Am)):
        x_s += Am[i] * np.cos(2*np.pi*Fm[i]*t_s + Pm[i])

    # Generate the dense sequence using the SUM methon
    x_d = np.sum(
        Am.reshape(1,-1)
        * np.cos(2*np.pi*np.dot(t_d.reshape(-1,1),Fm.reshape(1,-1))
                 + Pm.reshape(1,-1)),
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
```

## Running the project

Before running the project, you have to install it; check the instruction in [py-pkg-1c-uv-cs](py-pkg-1c-uv-cs.md). 

To see what commands are provided by the project, you can run `dsp26 --help`. With that, you can run the command to plot four different figures.

## Submission of work

This is Lab 0, and the submission is only for a testing if you can run the project. 

The focus of this submission is the screenshot of the four figures. Note that these figures can be saved to files using an option of the command of the project. 
