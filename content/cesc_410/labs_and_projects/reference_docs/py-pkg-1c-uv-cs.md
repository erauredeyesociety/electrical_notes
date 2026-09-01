<!-- bgn hidden -->

This is the cheatsheet for using uv. The quick guide version is at [py-pkg-1c-uv-qg](py-pkg-1c-uv-qg.md).

-   #2026-08-30:


<!-- end hidden -->

<!-- bgn cli -->

# Command-line instructions

```sh
pandoc -N -V fontsize=11pt "py-pkg-1c-uv-cs.md" -o "build/py-pkg-1c-uv-cs.pdf" --data-dir=../../a5ar/pandoc -L select-blocks.lua -M blocks2select="nil" --template=eagle.tex -V linestretch=1.1 -V verbatim-in-note -V codefontsize=9.5 -M geometry="top=2.7cm, bottom=2.8cm, left=2.5cm, right=2.4cm, headsep=0.3cm, footskip=0.9cm" --listings --filter pandoc-crossref -M listings -M titleblock --toc --shift-heading-level-by=-1 -M title="A Cheatsheet for Python Packaging with uv" -M author="Jianhua Liu" -M date="Fall 2026"
```

<!-- end cli -->

<!-- bgn tags -->

Tags: #python, #uv,

<!-- end tags -->

<!-- bgn hidden -->

```toc
style: number
min_depth: 1
max_depth: 6
```

## Cheatsheet of uv

-   To create a new CLI project:
-   To install a local app:
    -   Note that we often have to force the installation. This will update the dependences.

## From .py to PDF

For the DSP class, it is a good idea to use a IPython notebook so that the code and documentation will be in the same file. Yet, we'd like to run the code in the CLI command style. This way, using IPython notebook is a bit awkward in terms of calling functions hosted in certain notebooks. What we will do will be using .py files to host the code. In the .py file, we will have `# %% [Markdown]` sections so that we can create a PDF file for each .py file with VS Code.

Yet, there is one important link is missing: VS Code itself does not directly export a .py file with `# %% [markdown]` cells to a well-typeset PDF as smoothly as it does for notebooks. The workflow should be:

.py → Jupytext → .ipynb → PDF

This lets us keep the .py file as our primary source for CLI development while producing a polished PDF with rendered LaTeX equations.

Recommended workflow

### Step 1: Write our .py file using cell markers

For example, wer_tool.py:

```python
# %% [markdown]
# # WER Evaluation Tool
#
# This program calculates Word Error Rate (WER).
#
# The WER is defined as:
#
# $$
# \mathrm{WER} = \frac{S + D + I}{N}
# $$
#
# where:
#
# - $S$ = substitutions
# - $D$ = deletions
# - $I$ = insertions
# - $N$ = number of reference words.

# %%
def calculate_wer(S, D, I, N):
    """Calculate Word Error Rate."""
    return (S + D + I) / N


# %% [markdown]
# ## Example

# %%
wer = calculate_wer(2, 1, 3, 100)
print(f"WER = {wer:.2%}")
```

### Step 2: Install the VS Code extensions

Install:

-   Python — Microsoft
-   Jupyter — Microsoft

These allow VS Code to recognize the cell markders.

### Step 3: Install Jupytext

Jupytext converts between Python scripts and Jupyter notebooks.

Install it: `pip install jupytext`

Then convert your Python file: `jupytext --to notebook wer_tool.py`

This creates: `wer_tool.py` and `wer_tool.ipynb`

The Markdown sections become notebook Markdown cells, and the Python sections become code cells.

### Step 4: Open the .ipynb file in VS Code

Open: `wer_tool.ipynb` in VS Code. You should see:

-   formatted headings;
-   rendered Markdown;
-   properly typeset LaTeX equations;
-   executable Python cells;
-   program output.


### Step 5: Export to PDF

This is optional, which is based on VS Code notebook export

Open the `.ipynb` file and use the notebook export functionality from VS Code's notebook toolbar or Command Palette.

Look for an option similar to:

Export
    ↓
PDF

Depending on your VS Code/Jupyter configuration, you may need additional software such as a LaTeX distribution. On Windows, common choices include `texlive` or `MiKTeX`.

Then the workflow becomes:

```
wer_tool.py
     ↓
Jupytext
     ↓
wer_tool.ipynb
     ↓
VS Code preview
     ↓
Export
     ↓
wer_tool.pdf
```


<!-- end hidden -->

<!-- bgn ch-title -->

# A Cheatsheet for Python Packaging with uv

<!-- end ch-title -->

## Introduction

uv is a fast Python package and project management tool developed by Astral. It can manage dependencies, virtual environments, Python versions, and project packaging through a unified workflow (to build and publish our projects as well as install and run Python projects from various as command line tool). Designed as a modern alternative to combining tools such as pip, venv, and virtualenv, uv emphasizes speed, reproducibility, and simplicity.

If you are curious where comes the name of uv, you can consider this rumor: it's name comes from ultraviolet, which has a shorter wavelength or higher frequency than the visible light, implying that uv is faster than all the other existing python packaging tools.

There are a few types of files that are important with uv. They are introduced below.


### The `pyproject.toml` file

uv uses the `pyproject.toml` file to manage the dependencies. It defines build system requirements and configuration for tools. It also defines metadata and others. It aims to provide a unified place for project metadata and dependency management. Below is an example.

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your_project"
version = "0.1.0"
description = "A sample Python project"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
dependencies = [
    "requests>=2.24.0",
    "numpy>=1.19.2",
]

[project.optional-dependencies]
dev = [
    "pytest",
]
```

### Lockfile and synchronization

Lockfiles can be used for synchronizing the installation of dependencies across different computers for a specific project.

Different types of lockfiles are used to specify the exact versions of each package as will be discussed later.


## Installation of uv

Installation steps are detailed at [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/).

After the installation, we can run `uv --version` to verify it runs.

### Installation of uv on Windows

Use `irm` to download the script and execute it with `iex`. This can be done by executing the following in a Windows terminal:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, you can download `uv-x86_64-pc-windows-msvc.zip` from [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases) to do a manual installation.

#### Checking where uv is installed on Windows

To see where uv is installed, we can install a special Python version and see its location. Assume we have run `uv python install 3.12` before. Then, we can see installation using `uv python list`. It shows that version 3.12.12 is installed at `C:\Users\jhl\AppData\Roaming\uv\python\cpython-3.12.12-windows-x86_64-none\python.exe`.

### Installation of uv on Unix-like systems

On Unix-like systems, including Linux, macOS, and WSL, to install uv, open up a terminal and run

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

It is installed in your home directory; here is an example: `/home/jhl/.local/bin`.

### Verifying and updating the uv installation

To verify the installation, we can check the version of uv by running `uv self version` or `uv --version`.

New versions of uv are released very frequently. To update uv, run `uv self update` in a terminal.


## Basic uv operations for various tasks

uv is a feature-rich tool which can be used to replace a large number other tools. Yet, we only discuss a subset of features here, focusing on using basic uv operations for different tasks not related to project development. Operations related to project development are discussed in later sections.

If you want to see a list of detailed features of uv, see [https://docs.astral.sh/uv/getting-started/features/](https://docs.astral.sh/uv/getting-started/features/), which are listed in the following categories:

-   Python version management.
-   Using standalone Python scripts.
-   Managing Python-based projects. This is the focus of this doc, where we develop projects for our own or others to use.
-   Running and installing tools. This is about how to use projects developed by us or others on our system for various purposes.
-   The pip interface. pip is a very popular Python dependence handling tool. uv can be used as a drop-in replacement of pip.
-   Utility. This is for the management of uv itself.

All the commands below will run in a terminal, either on the Unix-like systems or on Windows.

### Checking the uv commands and help

As an all-in-one tool, uv has a large collection of commands. It is neither possible nor necessary to remember all commands and their options. What we can do is to seek help when needed.

-   To check the list of uv commands, run `uv`.
-   To get a brief help of all uv commands, run `uv --help`.
-   To get a more detailed help (in theory) of all uv commands, run `uv help`. Note that this is on the same level as `run --help`.
-   To get detailed help on each command, run `uv help <command>`. To navigate, use PgUp or PgDn. To exit, press "q".


### Working with a Python interpreter

#### Viewing installed Python versions

To see all the versions that can be used by uv, including locally installed and remotely available, run

```sh
uv python list
```

#### Installing a new Python interpreter

There are *two* approaches to install a new Python interpreter. The *explicit* approach is running

```sh
uv python install 3.13
```

-   If we ignore the version, the newest version will be installed.
-   We can install multiple versions in one-shot.

The *implicit* approach is to create a project with a specified version, as will be shown below.

For the newer versions of Python, where two version, regular and freethreaded versions available, if we want to use the later, we can use `uv python install 3.14+freethreaded`.

#### Reinstalling Python

For uv-managed Python, we can upgrade to a new release, say from 3.12.9 to 3.12.12. Here we use

-   `uv python install 3.12 --reinstall`.

#### Uninstalling a Python interpreter

We can remove a Python 3.12 installation using `uv python uninstall 3.12`.

#### Pinning a Python version

To use a specific Python version, say 3.11, run
```sh
uv python pin 3.11
```

Note that on Windows, we may have access issues.

#### Checking the Python version of a project

There are two ways to see the version of Python used with **a specific project**:

-   Checking the `.python-version` file.
-   Printing out info in a script `print(sys.version)`.

#### Changing Python version in a project

This can be done by editing the python version in the `.python-version` file directly.

Note that after this change, when we run `uv run ...`, the old v-env of the project will be removed and a new one will be created.

(Note that we may have to change the Python version in the `requires-python` field of `pyproject.toml`. Need to verify this later.)

#### Selecting a Python interpreter in VS Code

When we use VS Code, we need to select the Python interpreter from uv. This can be done with a setup in VS Code.

-   Open the VS Code Command Palette (Ctrl/Cmd + Shift + P).
-   Type "Python: Select Interpreter".
-   Choose the interpreter from the uv virtual environment, which should be something like `.venv/bin/python` or similar.

### Running a Python script

Note that a uv-installed Python interpreter may not be usable directly in CLI. That is Ok as we will usually run Python scripts by using `uv run`, as discussed here.

#### Running a Python script without dependencies

uv can be used to run a standalone Python script, say `hello_world.py`, directly with `uv run hello_world.py`. Yet, we don't see any advantages as compared to just running `python hello_world.py`.


### Managing dependencies for a project

We will discuss, in later sections, workflows for two different types of projects: those created locally from scratch and those cloned from somewhere else. Here we discuss the common operations we perform to address dependencies on an average project.

#### Checking the packages installed

To list the packages installed, we can use

```sh
uv pip list # for a plain list or
uv tree     # a tree-shape list
```

#### Removing a dependency

This can be done using

```
uv remove <package>
```

#### Updating dependency to a newer version

This can be done by running `uv lock --upgrade`.

Note that:

-   We may have to edit the `pyproject.toml` file manually to remove some *less-than constraints*, which limits us to use very new versions, before running the command.
-   The above instruction will upgrade the `uv.lock` file only. It does not update `pyproject.toml` file.

To upgrade the installed dependencies, we need to run `uv sync`.

#### Installing dependencies in two approaches

There are two approaches to add dependencies:

-   `uv add <a_package>`. This will install the dependency and update the `pyproject.toml` file; this is the preferred approach.
-   `uv pip install <a_package>`. This will install the dependency only without updating the `pyproject.toml` file.

#### Installing a local development package

If we have a local project, developing a package to be published later, we need to be able to test the component of the package during the development. Here, we need to run `uv pip install -e .` so that the package can be used as if it is an dependency.

Note that this is not the same as the installation of a local app, which is discussed at [Installing a local app](py-pkg-1c-uv-qg.md#Installing%20a%20local%20app).

### Working with lockfile for synchronization


We have the following types of lockfiles:

-   `uv.lock` is a _universal_ or _cross-platform_ lockfile that captures the packages that would be installed across all possible Python markers such as operating system, architecture, and Python version. Note that this is used by uv only.
-   `pylock.toml` is a new Python standard.
-   `requirements.txt` is the widely used one currently.

#### Creating and updating `uv.lock`

`uv.lock` will be created or updated from `pyproject.toml` by the following command:

```sh
uv lock
```

#### Creating and updating `pylock.toml` or `requirements.txt`

This can be done by the `uv export` command from `pyproject.toml`. Note that the project is re-locked before exporting unless the `--locked` or `--frozen` flag is used.

```sh
uv export -o pylock.toml
uv export -o requirements.txt
```
Note that if we have `requirements.in`, we can create `pylock.toml` or `requirements.txt` by running

```sh
uv pip compile -o pylock.toml -r requirements.in
```

## Working with tools/apps

A tool is a stand-alone Python app that we can run in CLI. We can have two types of tools:

-   An external one that is not developed by us, which can come from various sources, such as PyPI.
-   A local one that we have the source files stored locally. This can be developed by us or cloned from GitHub.

Here, we use `ruff` as an example.

### Managing an external tool with uv

#### Installing an external tool with pipx

For comparison, let's see what is the approach we use before the uv era.

pipx was created to install a tool in an isolated v-env. For example, we can install `ruff` using `pipx instll ruff`. After that, we can run `ruff` directly anywhere.


#### Running an external tool with uv without installation

uv runs very fast, and it is ok to run an external tool without installing it. For example, we can run `ruff` via `uvx ruff`, which is a short cut of `uv tool run ruff`.

If you want to see more details about running a tool without installing it, read [https://docs.astral.sh/uv/guides/tools/#using-tools](https://docs.astral.sh/uv/guides/tools/#using-tools).

#### Installing an external tool with uv

For most of the tools, we want to install them locally before running them. To install, run `uv tool install ruff`. Note that this command just replaces `pipx` with `uv tool`.

#### Running an external tool installed with uv

After installation using `uv tool install <command>`, we can run the tool by typing `command` anywhere in CLI.

#### Upgrading external tools installed with uv

To upgrade an external tool installed with uv, run `uv tool upgrade ruff`.

To upgrade all tools, run `uv tool upgrade --all`.


### Managing local apps

Suppose we have a local CLI app, saved in `<app_proj>`, which is developed locally or cloned from GitHub.

#### Installing a local app

Like with an external tool, we can install it using uv and run it anywhere in our system without having to activate the v-env.

To install, go to the root folder of the project and run `uv tool install . -e`.

Sometimes, especially after installing new dependencies, we need to run it again **to force some changes**. This can be done by running `uv tool install . -e --force`.

#### Running a local app

Once the local app is installed, it runs in the same way as all other CLI apps.

#### Uninstalling a tool with uv

We can uninstall an installed tool with uv as well. For both external tools and local apps, we use the same instruction:

```sh
uv tool uninstall <a_tool>
```

## Workflow for scratch-created projects

Here, we discuss the uv workflow when working on a project we create from scratch locally, regardless it is hosted on GitHub or not.

### Creating a project

Different Python projects can be used for different purposes in addition to their different functionality. For example, we can create a project that is targeted for:

-   A **collection of scripts**, including various CLI and GUI apps, which can be hold in various subfolders of the root project folder.
-   A **CLI app** that can run anywhere on our computer. Note that this type of project can also include **GUI apps** that can run anywhere on our computer.
-   A Python package that is used as a library.
-   A **workspace** to host related Python packages, including extensions (in other languages, such as Rust). Note that workspace is a concept used commonly in Rust but not in Python. As uv is developed in Rust, uv developers borrowed this concept to uv to handle workspace as well.

<!-- Note that all the above should be buildable, which means that users can install them from PyPI if they are published there. -->

#### Creating a project for multiple scripts

Many times, we will have multiple scripts related to a certain topic, such as all projects of a class. For organization reasons, we prefer to have all these scripts in a single project folder with dependencies handled together and multiple scripts in different subfolders.

The creation of such a project, called `<script_proj>`, can be done by running `uv init <script_proj>`. After the running, we will see that there are five files created in `<script_proj>` (say, `proj_scripts`): `.gitignore`, `.python-version`, `README.md`, `main.py`, and `pyproject.toml`. There is also a `.git` folder created.

Except the most trivial projects, we will have many scripts in such projects. To reduce the clutter, we will use subfolders under the root folder to host related scripts.


#### Creating a project for a CLI app

We can create a **packaged project** by running: `uv init --package <app_proj>`. Note that we can use `--python 3.12` to specify the version of Python to use.

When compared with the script project, an additional `src` folder is created to host the source files.

Note that uv cannot create a `tests` folder like Poetry does. To host the test scripts, we need to manually create the `tests` folder in the same level as the `src` folder.

#### Creating a library project

There is another option for the creation of a project, which is `--lib`, used to for hosting a library project: `uv init --lib <a_lib>`.

#### Creating a workspace

Currently, we don't have a use case yet. If we do, we will expend the guide according to [https://docs.astral.sh/uv/concepts/projects/workspaces/](https://docs.astral.sh/uv/concepts/projects/workspaces/).

### Adding dependencies to a scratch-created project

Assume we have a project created from scratch by using uv and are in the phase of developing code. In this process, we may need to add additional dependencies.

To **add** such a dependency, we use `uv add <package>`. This will install the package in the `.venv` folder and update the `pyproject.toml` file.

We may have to use the *dependency source* to tell where to find a certain dependency, as summarized below. For more details, see https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources.

#### Adding conventional PyPI packages

For conventional PyPI packages, we normally don't need to do anything special.

We can specify the version of the package though. For example

```sh
uv add 'requests==2.31.0'
```

#### Adding dependencies from GitHub or other online recourses

If the package is host on GitHub, we can use

```sh
uv add git+https://github.com/psf/requests
```

#### Adding a local file

When we add a local dependency, such as files from a project we developed locally, we can install it by specifying the path of the project. Say, assume we have a package named `numreps` under `projects`. If we develop a new project named `numreps-repl` under `projects`, we need to use the following with the  `numreps-repl` project to add `numreps` as dependency:

```sh
uv add ../numreps
```

After that, `numreps` will be used in the same way as the other dependencies.

### Adding dependencies to special groups

uv supports adding dependencies to special groups. For example, if we want to add pytest in to the dev group, we will run `uv add --dev pytest`. In the `pyproject.toml` file, we will see the following:

```toml
[dependency-groups]
dev = [
    "pytest>=8.3.4",
]
```

For special groups, we can use `--dev`, `--group`, or `--optional` flags.


### Addressing issues with running a script in the project

When we run `uv run a_script.py` under the root directory of the project, uv will automatically activate the v-env stored in `.venv`. If there is any issue with the importing of some modules, there are two approaches to handle the problem.

#### Manually activating the virtual environment for a project with uv

-   On Unix-like systems, this can be done by running `source .venv/bin/activate`.
-   On Windows, this can be done by running `.venv\Scripts\activate`.

For both OSes, to deactivate the v-env, run `deactivate`.


Note that this can be awkward if the folder we are running from is not the project folder. For this, we can use the following approach.

#### Activating the virtual environment for a project with code

This can be done in the `__init__.py` file, as shown below.

```python
from pathlib import Path
import subprocess

from .app_cli import app

def activate_env():
    script_dir = Path(__file__).parent
    activate_path = script_dir / "../../.venv/bin/activate"
    subprocess.run(f"source {activate_path}",
                   shell=True, executable="/bin/bash")

def main():
    activate_env()
    app()

if __name__ == "__main__":
    main()
```


### Additional tricks and solutions

#### Renaming the executable

By default, the name of executable app is defined in `pyproject.toml`, as shown below:

```toml
[project.scripts]
mp_app = "mp_app:main"
```

We need to pay attention to the following:

-   The first `mp_app` can be changed to another name if we want to **rename** the executable.
-   The second `mp_app` cannot be changed as it defines the project (package).
-   The `main` function is the entry point of the program. It must be defined in `__init__.py`.

#### Running pytest

To run pytest:

-   Create a `tests` folder beside the `src` folder and put our test functions in files of that folder.
-   Go to the root folder of the project.
-   Activate the v-env of the project as described above.
-   Run `pytest` to run all test functions or run `pytest tests/a_test_file.py` to run a specific file.


## Workflow for cloned projects

A cloned project is a project we copied from other sources:

-   It can come from `git clone`.
-   It can also come from downloading via archive tools.

### Working with cloned uv-managed projects

For these projects, they come with `pyproject.toml` and `uv.lock`. Here, we just need to run `uv run folder/script.py`, and the v-env will be created automatically and the dependencies will be installed. After that, the command will run.

Or, we can run `uv sync` to pre-install the dependencies used by the app.

### Managing cloned projects created by other tools to work under uv

Some projects come with a `pyproject.toml` file; for example, Poetry managed projects have such a file. Unfortunately, this is not in the format that uv can use. We need to migrate a project managed by other tools to uv if we want to keep working on the project under uv.

There is a tool called `migrate-to-uv` ([https://github.com/mkniewallner/migrate-to-uv](https://github.com/mkniewallner/migrate-to-uv)), which can be used to migrate a project from the management of following tools to uv:

-   Poetry
-   Pipenv
-   pip-tools
-   pip

To use this tool:

-   Change the directory to the project folder.
-   Run `uvx migrate-to-uv` to create `pyproject.toml` and `uv.lock` files.
-   Run `uv sync` to install the v-env.

### Managing cloned projects with `requirements.txt` to work under uv

If we cannot use the above `migrate-to-uv` to migrate the project, we can do a manual conversion so that the project can be under management of uv.

#### Creating a simple `pyproject.toml` file

First, we need to create a simple `pyproject.toml` file, as shown below.

```toml
[project]
name = "your-project"
version = "0.1.0"
dependencies = [

]
```

With this file, we don't need to create the `.venv` folder by running `uv venv`. This folder will be created automatically when we run the `uv add <package>` command.

#### Adding dependencies manually

For many small projects, we can use a tool, such as `pydeps`, to extract the dependencies and add them manually using `uv add <package>` for each dependency.

If the list of dependencies is not too long and the project does come with a `requriement.txt`, we can move on to the next step.

#### Adding dependencies from `requirements.txt`

This is done by running:

```sh
uv add -r requirements.txt
```

Note that the list of dependencies in the `pyproject.toml` is usually much longer than that created from the simple `uv add <a_package>` command.


### Working on cloned projects with `requirements.txt` as it

If we want to work on the project without converting to uv managed, we can just install the dependencies with `uv pip install -r requirements.txt`.

Note that `uv add -r requirements.txt` does not work since we don't have the needed `pyproject.toml` file.

Yet, **before the above** above installation, we need to create a v-env and activate it. Otherwise, the installation will be in the default Python env. So, the standard way for the installation has three steps:

```sh
uv venv
. .venv/bin/activate
uv pip install -r requirements.txt
```

## Packaging an exemplary project with external dependency

This is an exemplary CLI app project for illustrating packaging with uv. Please follow the steps below to create the project. Here, we assume uv is installed.

This project is illustrated on Windows with notes on the Unix-like systems.

### Creating the project

Go to the parent folder in a terminal where you want to place this project. Say, `C:\projects` (or `~/projects` on Unix-like systems).

Create the project by running:

```sh
uv init --package --python 3.12 numreps
```

### Editing source files

Now, change to the project folder `numreps` in a terminal and start VS Code by running `code .`. You should see the following files created:

-   `.gitignore`: the Git ignore files, used for ignoring source files when we use Git. This will not discuss the details of this file here for simplicity. A customized file is shown below.
-   `.python-version`: the file showing the version of Python.
-   `pyproject.toml`: the project/package management file.
-   `README.md`: the standard readme file.

`.gitignore`:
```gitignore
# Ignore everything
*

# Unignore top-level essentials
!/.gitignore
!/.python-version
!/pyproject.toml
!/pytest.ini
!/README.md
!/uv.lock

# Unignore src/numreps
!/src/
!/src/numreps/
!/src/numreps/*.py

# Unignore tests
!/tests/
!/tests/*.py
```

#### Editing the `README.md` file

Copy the following contents between the text separators, which provides a detailed description to the exemplary project, to this readme file:

---

numreps stands for number representations, and this app is used to convert a number to different representations:

For the CLI application, we have the following cases:

-   `numreps d2b -- n_bit num`: convert a number `num`, say 19, to `n_bit`-bit, say 8-bit, binary expression in the form of `0b0001_0011`. Here `num` is signed. If `num` is positive, we can ignore `--` in the command.
-   `numreps d2h -- n_bit num`: convert a number `num`, say 19, to `n_bit`-bit, say 8-bit, hexadecimal expression in the form of `0x13`. Here `num` is signed. If `num` is positive, we can ignore `--` in the command.
-   `numreps b2d type n_bit num`: convert a `n_bit`-bit binary number `num` to decimal. If `type` = "u", then, the binary is seen as unsigned; if `type` = "i", then the binary is seen as signed. Other values of `type` are not supported.
-   `numreps h2d type n_bit num`: convert a `n_bit`-bit hexadecimal number `num` to decimal. If `type` = "u", then, the corresponding binary is seen as unsigned; if `type` = "i", then the corresponding binary is seen as signed. Other values of `type` are not supported.

To see detailed format of how to run the app and updated functionalities of this app, run `numreps --help`.

---

<!-- bgn hidden -->

We will develop a GUI version based on QML, as shown below

```
| O Unsigned; O Signed  |   | Clear Fields  |
| n_bit                 |   | Dec to Bin    |
| Bin Seq               |   | Bin to Dec    |
| Dec Num               |   | Dec to Hex    |
| Hex Seq               |   | HEx to Dec    |
```

-   The top left is an area for radio buttons.
-   The others on the left are all text fields for display and input.
-   The right column are buttons for operations.
    -   The first one will be used to clear all text fields.
    -   The others are for conversions.

<!-- end hidden -->


#### Editing or creating source files in the `src/numreps` folder

We will use the following source files in this folder.

##### The `__init__.py` file

This is the entry point of the app.

`__init__.py`:
```python
from numreps.app_cli import app

def main():
    app()
```

<!-- bgn hidden -->

Note that the `activate_env()` function is used to activate the venv created for this project. We should have not used this trick; yet without it, we cannot run this app anywhere on our computer due to the missing of external dependencies.

<!-- end hidden -->

##### The `app_cli.py` file

This is the collection of commands for this app.

`app_cli.py`:
```python
import typer
from numreps.recipes import d2b_, d2h_, b2d_, h2d_


app = typer.Typer()

__version__ = "0.1.0"


########################################################################
# Print out the version: numreps --version
def print_version(value: bool):
    if value:
        typer.echo(f"Version of numreps: {__version__}")
        raise typer.Exit()


# Add the version option.
@app.callback()
def callback(version: bool = typer.Option(
        None, "--version", callback=print_version, is_eager=True)):
    pass


########################################################################
# Decimal to n-bit binary
@app.command()
def d2b(n_bit: int, num: int):
    """Print num, a decimal, in n-bit binary format: numreps d2b -- n_bit num.
    Example: numreps d2b -- 32 -66. If num is positive, -- can be removed."""
    binary = d2b_(n_bit, num)
    typer.echo(f'{num} to {n_bit}-bit binary: {binary}')


# Decimal to n-bit hexadecimal
@app.command()
def d2h(n_bit: int, num: int):
    """Print num, a decimal, in n-bit binary format: numreps d2h -- n_bit num.
    Example: numreps d2h -- 32 -66. If num is positive, -- can be removed."""
    hexa_d = d2h_(n_bit, num)
    typer.echo(f'{num} to {n_bit}-bit binary: {hexa_d}')


# n-bit binary to decimal
@app.command()
def b2d(b_type: str, n_bit: int, num: str):
    """Print num, an n-bit binary, in decimal: numreps b2d type n_bit num.
    Example: numreps b2d u 6 0b11_1111."""
    dec = b2d_(b_type, n_bit, num)
    typer.echo(f'{n_bit}-bit binary {num} to decimal: {dec}')


# n-bit Hexadecimal to decimal
@app.command()
def h2d(b_type: str, n_bit: int, num: str):
    """Print num, an n-bit hex, in decimal: numreps h2d type n_bit num.
    Example: numreps h2d u 6 0b3F."""
    dec = h2d_(b_type, n_bit, num)
    typer.echo(f'{n_bit}-bit binary {num} to decimal: {dec}')
```


##### The `recipes.py` file

This is the file for implementing all commands of the project. When the project grows, we may use a `recipes` folder to host the implementation of commands in multiple files.

`recipes.py`:
```python
from numreps.representations import (
    to_dec_twos_complement,
    add_separator,
    pad_num_seq,
    pad_hex_seq,
    strip_formatters,
)


#####################################################################
# Decimal to binary or hexadecimal
def d2b_(n_bit: int, num: int):
    num = to_dec_twos_complement(n_bit, num)
    bin_seq = bin(num)[2:]          # Binary sequence without '0b'
    bin_seq = pad_num_seq(n_bit, bin_seq)
    seged_bin = '0b' + add_separator(bin_seq, 4)
    return seged_bin


def d2h_(n_bit: int, num: int):
    num = to_dec_twos_complement(n_bit, num)
    hex_seq = hex(num)[2:].upper()  # Hexadecimal seq without '0x'
    # n_digit = (n_bit - 1)//4 + 1
    hex_seq = pad_hex_seq(n_bit, hex_seq)
    seged_hex = '0x' + add_separator(hex_seq, 4)
    return seged_hex


#####################################################################
# Binary or hexadecimal to decimal
def b2d_(b_type: str, n_bit: int, num: str):
    bin_seq = strip_formatters(num, '0b', '_')
    bin_seq = bin_seq[-n_bit:]       # Only keep the last n_bit bits
    dec_num = int(bin_seq, 2)
    if (bin_seq[0] == '1') and (b_type == 'i'):
        dec_num -= 2**n_bit
    return dec_num


def h2d_(b_type: str, n_bit: int, num: str):
    hex_seq = strip_formatters(num, '0x', '_')
    dec_num = int(hex_seq, 16)
    bin_seq = d2b_(n_bit, dec_num)
    dec_num = b2d_(b_type, n_bit, bin_seq)
    return dec_num
```

##### The `representations.py` file

This the file hosting the true functionalities that can be used by the CLI App or the GUI App. When the project grows, we may use multiple files or even multiple folders to host the sorce files.

`representations.py.py`:
```python
# Decimal-based two's complete
def to_dec_twos_complement(n_bit: int, num: int):
    mask = 2**n_bit - 1
    num = num & mask
    return num


# Add underscore separator in a sequence (seq) every seg_size chars
def add_separator(seq: str, seg_size: int):
    reversed_seq = "".join(reversed(seq))
    len_seq = len(reversed_seq)
    num_of_underscores = (len_seq - 1) // seg_size

    index = 0
    new_seq = ""
    while (index < num_of_underscores):
        new_seq += reversed_seq[seg_size * index: seg_size * (index+1)] + '_'
        index += 1
    new_seq += reversed_seq[seg_size * index:]

    return "".join(reversed(new_seq))


# Pad binary sequence
def pad_num_seq(n_bit: int, num_seq: str):
    if len(num_seq) < n_bit:
        num_seq = '0' * (n_bit - len(num_seq)) + num_seq
    return num_seq


# Pad hexadecimal sequence
def pad_hex_seq(n_bit: int, hex_seq: str):
    n_digit = (n_bit - 1)//4 + 1
    return pad_num_seq(n_digit, hex_seq)


# Binary or hexadecimal to decimal
def strip_formatters(num_seq: str, prefix: str, separator: str):
    num_seq = num_seq.replace(prefix, "")
    num_seq = num_seq.replace(separator, "")
    return num_seq
```


#### Creating source files in the `tests` folder

We use pytest to test our functions. Here, we put the test functions into two files:

-   `test_recipes.py`: Used to test the API functions hosted in `recipes.py` that can be used by the CLI or GUI apps.
-   `test_representations.py`: Used to test the functions hosted in `representations.py`.

##### The `test_recipes.py` file

`test_recipes.py`:
```python
import pytest

from numreps.recipes import d2b_, d2h_, b2d_, h2d_


def test_d2b_():
    assert d2b_(8, 1) == "0b0000_0001"
    assert d2b_(8, -1) == "0b1111_1111"
    assert d2b_(9, 17) == "0b0_0001_0001"
    assert d2b_(9, -17) == "0b1_1110_1111"


def test_d2h_():
    assert d2h_(8, 1) == "0x01"
    assert d2h_(8, -1) == "0xFF"
    assert d2h_(9, 17) == "0x011"
    assert d2h_(9, -17) == "0x1EF"
    assert d2h_(18, 17) == "0x0_0011"
    assert d2h_(18, -17) == "0x3_FFEF"


def test_b2d_():
    assert b2d_('u', 8, '0b1010_1010') == 170
    assert b2d_('i', 8, '0b1010_1010') == 170 - 256
    assert b2d_('i', 8, '0b0_1010_1010') == 170 - 256


def test_h2d_():
    assert h2d_('u', 8, '0xAA') == 170
    assert h2d_('i', 8, '0xAA') == 170 - 256
    assert h2d_('i', 8, '0x0AA') == 170 - 256
```

##### The `test_representations.py` file

`test_representations.py`:
```python
import pytest

from numreps.representations import (
    to_dec_twos_complement,
    add_separator,
    pad_num_seq,
    pad_hex_seq,
    strip_formatters,
)


def test_to_dec_twos_complement():
    assert to_dec_twos_complement(8, 1) == 1
    assert to_dec_twos_complement(8, -1) == 255
    assert to_dec_twos_complement(4, 17) == 1
    assert to_dec_twos_complement(4, -17) == (256-17) & 15


def test_add_separator():
    assert add_separator("abcdefghij", 4) == "ab_cdef_ghij"
    assert add_separator("123", 4) == "123"  # No separator needed
    assert add_separator("12345678", 3) == "12_345_678"  # Segments of 3
    assert add_separator("1", 3) == "1"  # Single character, no separator
    assert add_separator("ABCDEFGH", 2) == "AB_CD_EF_GH"  # Segments of 2
    assert add_separator("A", 2) == "A"  # Empty string case


def test_pad_num_seq():
    # We mainly test the padding of binary sequence here
    assert pad_num_seq(2, "10") == "10"
    assert pad_num_seq(8, "1000") == "00001000"


def test_pad_hex_seq():
    assert pad_hex_seq(4, "a") == "a"
    assert pad_hex_seq(6, "a") == "0a"
    assert pad_hex_seq(8, "a") == "0a"


def test_strip_formatters():
    assert strip_formatters("0b1_1010", "0b", "_") == "11010"
    assert strip_formatters("0xABC_def9", "0x", "_") == "ABCdef9"
    assert strip_formatters("0b1_1010", "0b", "_") == "11010"
```


### Adding dependencies

We add two different kind of dependencies for this project.

The first is like Typer, used when both running the App or test various functions. Here, we run `uv add typer`.

The second is like Pytest, used only during developing of the project. Here, we use  `uv add --dev pytest` to install it only for the develop group.


### Running the tests

To run the tests of the project, we need to activate the venv of this project and run `pytest` under the root folder of the project.


### Running the project

To run the project as an App, we need to install it first by running `uv tool install . -e`.

After this, we can run the project in anywhere on our computer in a terminal by running `numreps --help` and use the commands list there.


## Packaging an exemplary project with local dependency

This is an exemplary project for illustrating packaging with uv when there are local dependencies. Please follow the steps below to create the project.

### Creating the project

Go to the parent folder where you want to place this project. Say, `c:\projects` on Windows or `~/projects` on Unix-like systems.

Create the project by running:
```sh
uv init --package --python 3.12 numreps-repl
```

This project contains an app that can run the REPL loop based on the numreps package we develop locally. It uses prompt toolkit for text-based user interface.

### Editing source files

We edit the following source files for this project:

The `README.md` file:
```
This project is based on the numreps package we develop locally. It provides a text-based user interface so that users can use this App repeatedly without exiting.

To run the code, type `numreps-repl` in a terminal. Follow the hints in the top of the screen.

See the code for details of the functionalities.
```

The `__init__.py` file:
```python
from numreps_repl.app_tui import app

def main():
    app()
```

<!-- bgn hidden -->

The `__init__.py` file:
```python
from pathlib import Path
import subprocess

from .app_tui import app

def activate_env():
    script_dir = Path(__file__).parent
    activate_path = script_dir / "../../.venv/bin/activate"
    subprocess.run(f"source {activate_path}",
                   shell=True, executable="/bin/bash")


def main():
    activate_env()
    app()


if __name__ == "__main__":
    main()
```

<!-- end hidden -->


The `app_tui.py` file:
```python
#!/usr/bin/env python
"""A number representation converter."""

from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import SearchToolbar, TextArea

from numreps.recipes import d2b_, d2h_, b2d_, h2d_


cvt_states = {"D2B": 0, "D2H": 1, "B2D": 2, "H2D": 3}
cvt_state = cvt_states["D2B"]  # Initial state

app_hints = "Commands of the App:\n" + \
    "-   To exit, press Control-Q.\n" + \
    "-   To perform Binary to Decimal conversion, press Control-B.\n" + \
    "-   To perform Decimal to Binary conversion, press Control-C.\n" + \
    "-   To perform Decimal to Hexadecimal conversion, press Control-D.\n" + \
    "-   To perform Hexadecimal to Decimal conversion, press Control-H.\n"
app_hint_field = TextArea(style="class:app-field", text=app_hints, height=6)

cvt_hints = [
    "Decimal to Binary.      Input: n_bit num (ex: 8 -2)",
    "Decimal to Hexadecimal. Input: n_bit num (ex: 8 2)",
    "Binary to Decimal.      Input: type (u/i) n_bit num (ex: i 6 0b11_1010)",
    "Hexadecimal to Decimal. Input: type (u/i) n_bit num (ex: i 8 0xEF)"
]
cvt_cmd_field = TextArea(style="class:cvt-field",
    text=cvt_hints[cvt_state], height=1)

output_field = TextArea(style="class:output-field", text="")

input_field = TextArea(
    height=1,
    prompt=">>> ",
    style="class:input-field",
    multiline=False,
    wrap_lines=False,
    search_field=SearchToolbar(),  # For reverse search
)


# NOTE: It's better to assign an `accept_handler`, rather then adding a
#       custom ENTER key binding. This will automatically reset the input
#       field and add the strings to the history.
def accept_input(buff):
    # Evaluate "calculator" expression.
    try:
        inputs = input_field.text.split()
        if cvt_state == cvt_states["D2B"]:
            n_bit, num = int(inputs[0]), int(inputs[1])
            output = f"\n\n{n_bit}-bit D2B conversion of {num} ==>\n" + \
                f"Out: {d2b_(n_bit, num)}"
        if cvt_state == cvt_states["D2H"]:
            n_bit, num = int(inputs[0]), int(inputs[1])
            output = f"\n\n{n_bit}-bit D2H conversion of {num} ==>\n" + \
                f"Out: {d2h_(n_bit, num)}"
        if cvt_state == cvt_states["B2D"]:
            b_type, n_bit, num = inputs[0], int(inputs[1]), inputs[2]
            output = f"\n\n{n_bit}-bit B2D conversion of {num} ==>\n" + \
                f"Out: {b2d_(b_type, n_bit, num)}"
        if cvt_state == cvt_states["H2D"]:
            b_type, n_bit, num = inputs[0], int(inputs[1]), inputs[2]
            output = f"\n\n{n_bit}-bit H2D conversion of {num} ==>\n" + \
                f"Out: {h2d_(b_type, n_bit, num)}"
    except BaseException as e:
        output = f"\n\n{e}"

    output_text = output_field.text + output
    output_field.buffer.document = Document(    # add text to output buffer.
        text=output_text, cursor_position=len(output_text)
    )

input_field.accept_handler = accept_input

container = HSplit(
    [
        app_hint_field,
        Window(height=1, char="-", style="class:line"),
        cvt_cmd_field,
        Window(height=1, char="-", style="class:line"),
        output_field,
        Window(height=1, char="-", style="class:line"),
        input_field,
    ]
)

style = Style(
    [
        ("app-field", "bg:#404000 #ffffff"),
        ("cvt-field", "bg:#004400 #ffffff"),
        ("output-field", "bg:#000044 #ffffff"),
        ("input-field", "bg:#000000 #ffffff"),
        ("line", "#004400"),
    ]
)

kb = KeyBindings()

@kb.add("c-b")
def _(event):
    global cvt_state
    cvt_state = cvt_states["B2D"]
    cvt_cmd_field.buffer.document = Document( text=cvt_hints[cvt_state])

@kb.add("c-c")
def _(event):
    global cvt_state
    cvt_state = cvt_states["D2B"]
    cvt_cmd_field.buffer.document = Document( text=cvt_hints[cvt_state])

@kb.add("c-d")
def _(event):
    global cvt_state
    cvt_state = cvt_states["D2H"]
    cvt_cmd_field.buffer.document = Document( text=cvt_hints[cvt_state])

@kb.add("c-h")
def _(event):
    global cvt_state
    cvt_state = cvt_states["H2D"]
    cvt_cmd_field.buffer.document = Document( text=cvt_hints[cvt_state])

@kb.add("c-q")
def _(event):
    "Pressing Ctrl-Q or Ctrl-C will exit the user interface."
    event.app.exit()

application = Application(
    layout=Layout(container, focused_element=input_field),
    key_bindings=kb,
    style=style,
    mouse_support=True,
    full_screen=True,
)

def app():
    application.run()
```

### Adding dependencies

We also add two different kind of dependencies for this project.

The first is the numreps project we develop locally. To add this dependency, we run `uv add ../numreps`. Note that we have provided the path of this dependency.

The second is the conventional external dependency; here, we run `uv add prompt-toolkit` to add a new package so that we can develop the REPL functionalities in CLI applications.


### Installing the project

We also run `uv tool install . -e` to install the project so that it can run anywhere like a command.


### Running the project

You can run the app in any terminal by executing `numreps-repl`. Follow the on-screen hints at the top of the screen for instructions.
