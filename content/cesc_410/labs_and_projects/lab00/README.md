# Lab 0 — Getting started with Python for DSP

**Handout:** [`dsp-ba--lab0-getting-started.md`](dsp-ba--lab0-getting-started.md) ([pdf](dsp-ba--lab0-getting-started-26.pdf)) · **Started:** 2026-09-01 · **Status:** ✅ demo done, package built — ready to upload

**Goal:** stand up the `dsp26` uv package that every later lab will extend, and prove it runs by producing four figures — time-domain waveform and frequency-domain spectrum for single and summed sinusoids.

This lab is a setup check. The graded content is the four figures.

---

## Inputs

| File | Purpose | Status |
| --- | --- | --- |
| `dsp-ba--lab0-getting-started.md` / `.pdf` | handout, with all source code inline | ✅ present |
| [`../reference_docs/py-pkg-1c-uv-cs.md`](../reference_docs/py-pkg-1c-uv-cs.md) / `.pdf` | uv cheatsheet the handout links to | ✅ present, moved to `reference_docs/` |
| `py-pkg-1c-uv-qg.md` | uv **quick guide** — the cheatsheet's companion | ❌ **not on disk — check Canvas** |

Two notes, both found by `tools/check_inputs.py`:

- The handout links to `py-pkg-1c-uv-cs.md` as a sibling; it now lives in `reference_docs/` since it is course-wide, so that link inside the handout no longer resolves. Content unchanged, handout not edited.
- **`py-pkg-1c-uv-qg.md` was never downloaded.** The cheatsheet references it twice — once as the quick-guide version, and once pointing at its *"Installing a local app"* section. Lab 0 did not need it (the cheatsheet was sufficient), but it is a real gap worth closing before a later lab depends on it.

---

## Code

Lab code lives in the shared package — see [`../README.md`](../README.md#why-code-and-docs-are-split).

| File | What it does |
| --- | --- |
| `dsp26/src/dsp26/__init__.py` | entry point; `main()` calls the Typer app |
| `dsp26/src/dsp26/app_cli.py` | `--version` plus the `plot-sinusoids-td-fd` command |
| `dsp26/src/dsp26/lab0_sinusoids/recipes.py` | parameters, RNG seed, orchestrates the four figures, saves them |
| `dsp26/src/dsp26/lab0_sinusoids/sinusoids.py` | the three plotting functions |

All transcribed from the handout, with two marked deviations (below).

---

## Reproduce

```sh
# uv is not in apt; standalone installer, no root, lands in ~/.local/bin
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv --version        # -> uv 0.12.8
```

```sh
cd labs_and_projects
uv init --package --python 3.12 dsp26     # already done; skip if dsp26/ exists
cd dsp26
uv add typer matplotlib numpy scipy
uv add --dev pytest
```

Then write the four source files from the handout, and:

```sh
uv sync
uv run dsp26 --help
```

```
The basic frequency is 4.0 Hz.
Usage: dsp26 [OPTIONS] COMMAND [ARGS]...
...
╭─ Commands ─────────────────────────────────────────────╮
│ plot-sinusoids-td-fd  Plot time-domain waveform and    │
│                       frequency-domain spectrum ...    │
╰────────────────────────────────────────────────────────╯
```

Generate the figures. Headless here, so `MPLBACKEND=Agg` and save to file — the handout sanctions saving via `--folder-name`:

```sh
MPLBACKEND=Agg uv run dsp26 plot-sinusoids-td-fd --folder-name ../lab00
```

```
The basic frequency is 4.0 Hz.
Figures Saved in ../lab00
```

*(Three `FigureCanvasAgg is non-interactive` warnings are expected headless — [KI-02](../reference_docs/known_issues.md#ki-02--pltshow-does-nothing-headless). On a laptop with a display, drop `MPLBACKEND=Agg` and four windows open.)*

Verify:

```sh
cd .. && uv run --project dsp26 python tools/check_artifacts.py lab00/figs
```

```
OK    artifacts present, non-trivial, and distinct
```

Package the submission (report + figures, no code):

```sh
tools/make_submission.sh lab00 nelson-gatlin --figures
```

```
Rendering lab00/report.tex ...
  OK
Wrote lab00/lab00-figures-nelson-gatlin.zip
Size: 404K
```

Contains `report.pdf` (4 pages, one figure each), `report.tex`, `report.md`, and the four PNGs under `figs/`.

---

## Artifacts

`myID = 6127`, giving `Freq_1 = 4.0 Hz`.

> **These four PNGs are the entire submission.** The handout: *"The focus of this submission is the screenshot of the four figures. Note that these figures can be saved to files using an option of the command of the project."* Saving is explicitly sanctioned, so the saved PNGs serve as the screenshots — no code zip, no report.
>
> ```
> lab00/figs/lab0_sinusoids_fig1.png
> lab00/figs/lab0_sinusoids_fig2.png
> lab00/figs/lab0_sinusoids_fig3.png
> lab00/figs/lab0_sinusoids_fig4.png
> ```
>
> ⚠ `figs/` is gitignored. Regenerate before submitting if they are not on disk.

| # | File | Shows |
| --- | --- | --- |
| 1 | `figs/lab0_sinusoids_fig1.png` | single sinusoid, A=1, 4 Hz, φ=π/4 — 4 cycles in 1 s, spectral peaks at ±4 Hz |
| 2 | `figs/lab0_sinusoids_fig2.png` | single sinusoid, A=0.5, 8 Hz, φ=π/3 — 8 cycles, peaks at ±8 Hz, half the height |
| 3 | `figs/lab0_sinusoids_fig3.png` | sum of figures 1 and 2, summed **as signals** |
| 4 | `figs/lab0_sinusoids_fig4.png` | sum of three sinusoids built **from parameter vectors** (`Am`, `Fm`, `Pm`), one loop and one vectorized |

Collected into `report.tex` / `report.md` — a figures-only document with a title block and one captioned figure per page, no prose sections. `report.pdf` is generated by the packaging step and is what a reader opens.

Each figure: sparse samples as dots over the dense waveform (top), magnitude spectrum with the complex value annotated at each peak (bottom). Both `.png` and `.svg` are saved; **use the PNGs in the report.**

---

## Deviations from the handout

| # | Change | Why |
| --- | --- | --- |
| 1 | `plt.figure(1)` → `plt.figure()` in `plot_one_sinusoid_td_fd` | **Bug fix.** The function is called twice; pyplot returns the *same* Figure for a repeated number, so `fig1 is fig2` was `True`, the second call drew on top of the first, and both saved figures were one overplotted image (95410 bytes each, 4 lines instead of 2). Full write-up: [KI-01](../reference_docs/known_issues.md#ki-01--repeated-pltfiguren-silently-overplots--figures-come-out-identical) |
| 2 | Save `.png` alongside `.svg` in `recipes.py` | The deliverable is a screenshot of each figure and SVG does not paste reliably into a report. Handout saves SVG only. |

Both are marked in the source with `DEVIATION FROM HANDOUT:` comments.

**Deviation 1 is worth mentioning in the report's Narrative** — it is a real debugging story, and it only manifests on the save path the handout recommends. Interactively it is invisible, because `plt.show()` blocks and closing the window destroys the figure.

---

## Handout questions

None. Lab 0 is a setup check — *"the submission is only for a testing if you can run the project."* The deliverable is the four figures.

---

## Needs a human

| Task | Status |
| --- | --- |
| **Set ERAU ID** — `myID = 6127` | ✅ done |
| Regenerate figures | ✅ done |
| Live demo at the lab meeting | ✅ done |
| Build submission package | ✅ `lab00-figures-nelson-gatlin.zip` |
| **Upload to Canvas** before the Lab 1 meeting (Sec 1: 9/8, Sec 2: 9/4) | ⬜ **remaining** |

**Note on the ID.** Setting `myID` from `1234` to `6127` produced **byte-identical figures**. That is expected, not a failure — the seed changed the underlying draw (3 → 4) but `floor((10+v)/3)` maps both onto 4.0 Hz, one of only four possible values. See [KI-06](../reference_docs/known_issues.md#ki-06--setting-your-erau-id-may-not-change-the-figures-at-all).

---

## Notes

- **The package is the semester, not the lab.** `dsp26` is shared by every lab; Lab 1 adds `lab1_<topic>/` and one more command to `app_cli.py`. Do not start a new project.
- `.venv` is **254 MB** — gitignored. `uv.lock` is committed; that is what makes it reproducible.
- `uv run` resolves the environment itself. You never activate the venv, which is the point of the handout's single-venv design.
- Editable install: edit `src/` and re-run, no reinstall needed.
- Verifying SVGs with ImageMagick made correct figures look blank — its SVG renderer can't handle matplotlib paths. Save PNG from matplotlib instead ([KI-05](../reference_docs/known_issues.md#ki-05--imagemagick-renders-matplotlib-svg-almost-blank)).
