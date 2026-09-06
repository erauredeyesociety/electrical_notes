# Known issues

**Check here before debugging.** Traps that have already cost time, and things in the handouts that are wrong.

Add an entry when something takes more than ~15 minutes to work out, or when handout code does not do what it says.

---

## KI-01 · Repeated `plt.figure(N)` silently overplots — figures come out identical

**Seen in:** Lab 0, `sinusoids.py` · **Status:** fixed, deviation marked in source

**Symptom.** Four figures saved, but two were the same image. `lab0_sinusoids_fig1.svg` and `fig2.svg` both came out at exactly 95410 bytes.

**Cause.** `plot_one_sinusoid_td_fd()` opens its figure with `plt.figure(1)` and the recipe calls it twice. **pyplot returns the *existing* Figure for a repeated number** — so `fig1 is fig2` is `True`, the second call draws on top of the first (4 lines on the axes instead of 2), and both `savefig` calls write the same overplotted figure.

**Why it looks fine in class.** Interactively, `plt.show()` *blocks*, and closing the window destroys figure 1 — so the next `plt.figure(1)` gets a fresh one. The bug only appears when saving to file, because headless `plt.show()` is a no-op and nothing is ever closed. **The broken path is the one the handout recommends for submission.**

**Fix.** Bare `plt.figure()` auto-numbers (1, then 2), matching the handout's intent and leaving the explicit `figure(3)` / `figure(4)` calls alone.

```python
fig_plot = plt.figure()     # was: plt.figure(1)
```

**How to catch it.** Two output files with the *same byte size* are a bug, not a coincidence:

```sh
ls -l figs/ | awk '{print $5, $9}'
md5sum figs/*
```

Note that identical size with *different* md5 still means overplotted — matplotlib writes randomized element ids into SVG, so the bytes differ even when the picture is the same.

**Generalize:** any handout helper that hard-codes a figure number and gets called more than once has this bug.

---

## KI-02 · `plt.show()` does nothing headless

**Seen in:** Lab 0 · **Status:** expected, not a bug

`UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown`. Expected on a machine with no display. Save instead:

```sh
MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN
```

The handouts sanction saving to file, so this is a supported path, not a workaround. **Screenshots for submission still need a real GUI** — that part is human work.

---

## KI-03 · `myID` is a per-student seed and must be set every lab

**Seen in:** Lab 0, `recipes.py` · **Status:** resolved for Lab 0 (`myID = 6127`)

```python
myID = 6127                 # last 4 digits of the ERAU ID
np.random.seed(seed=myID)
Freq_1 = np.floor((10 + np.random.randint(0, 10)) / 3)
```

Handouts ship the placeholder `1234`. Expect this pattern in every lab, and set it before generating anything you intend to submit:

```sh
grep -rn "myID" dsp26/src/
```

**But do not expect the output to change visibly** — see [KI-06](#ki-06--setting-your-erau-id-may-not-change-the-figures-at-all). In Lab 0 the real ID and the placeholder both yield 4.0 Hz. Set it because the handout asks for it, not because you can see the difference.

---

## KI-04 · `uv` is not in the system package manager

**Status:** resolved

Not in apt. Install standalone (no root, lands in `~/.local/bin`):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
```

Installed here: **uv 0.12.8**. Add the `PATH` line to your shell profile or every new terminal will report `uv: command not found`.

---

## KI-05 · ImageMagick renders matplotlib SVG almost blank

**Seen in:** verifying Lab 0 figures · **Status:** avoid the tool

`convert file.svg out.png` on a matplotlib SVG produced axes and text but **no data** — plots looked empty. ImageMagick's built-in SVG renderer does not handle matplotlib's paths and clip paths.

**This can make correct output look broken.** To check a figure, save PNG directly from matplotlib rather than converting:

```python
fig.savefig("out.png", dpi=60)
```

Or use a real SVG renderer (`rsvg-convert`, Inkscape, a browser).

---

## KI-06 · Setting your ERAU ID may not change the figures at all

**Seen in:** Lab 0, `recipes.py` · **Status:** expected, not a bug

Changing `myID` from the placeholder `1234` to a real ID `6127` produced **byte-identical figures**. It looks like the change did not take effect. It did.

```python
Freq_1 = np.floor((10 + np.random.randint(0, 10)) / 3)
```

The draw genuinely changed — seed 1234 gives 3, seed 6127 gives 4 — but `floor((10+v)/3)` collapses ten possible draws onto **four** frequencies:

| `Freq_1` | Draws that produce it | Share of seeds |
| --- | --- | ---: |
| 3 Hz | 0, 1 | 20% |
| **4 Hz** | 2, 3, 4 | **30%** |
| **5 Hz** | 5, 6, 7 | **30%** |
| 6 Hz | 8, 9 | 20% |

Both 1234 and 6127 land in the 4 Hz bucket.

**Consequences worth knowing:**

- **Do not debug this.** Verify the seed changed the *draw*, not the frequency:
  ```sh
  uv run python -c "import numpy as np; np.random.seed(6127); print(np.random.randint(0,10))"
  ```
- Roughly **30% of the class will produce the same figures as each other**, and 30% will match the handout's placeholder output. Identical figures between two students are not evidence of anything.
- It also means "leaving the placeholder = submitting the instructor's plots" is only *sometimes* true. Set your real ID anyway — it is what the handout asks, and the seed is what is being checked.

---

## KI-07 · `splitlines()` vs `tokenize` desync silently corrupted stripped output

**Seen in:** `tools/strip_comments.py` · **Status:** fixed · **Found by:** adversarial testing, not by use

**Symptom.** Comments survived a strip; a `DEVIATION FROM HANDOUT` disclosure was deleted or truncated to a bare `#`; a string constant was silently truncated. **All exiting 0.**

**Cause.** Cut positions were keyed by *tokenize* line numbers, which break only on `\n`. The emit loop iterated `source.splitlines()` — which **also** breaks on U+000B, **U+000C (form feed)**, U+001C–1E, U+0085, **U+2028** and U+2029. One of those anywhere in the file shifts every subsequent line number, so cuts land on the wrong lines.

**Why it mattered here.** Form feeds are used as section separators in real source (several stdlib modules have them), and **U+2028 rides along in copy-paste from PDFs — which is exactly how handout code reaches us.**

**Why the safety net missed it.** `_verify` compared ASTs, and **comments carry no AST**. In the docstring case it was worse: `norm()` deleted `body[0]` from *both* trees, hiding a genuinely different string constant.

**Fix.** Split on `"\n"` everywhere, matching tokenize:

```python
src_lines = source.split("\n")            # was: source.splitlines()
for i, line in enumerate(source.split("\n"), start=1):
```

Plus a second check in `_verify`: every kept-pattern comment present in the input must still be present in the output. Comments have no AST, so this has to be explicit.

**Generalize:** `str.splitlines()` and every tokenizer disagree about what a line break is. **Never mix them.** If you index one by the other's line numbers, you have this bug.

---

## KI-08 · Stripping docstrings removes Typer's `--help` text

**Seen in:** `app_cli.py` · **Status:** fixed

**Symptom.** After stripping, `dsp26 --help` listed the command with **no description**.

**Cause.** Typer and Click build help text *from the function docstring*. To a stripper it looks like commentary; to the CLI it is user-visible output. The Lab 0 handout tells students to run `dsp26 --help`, so that text is part of what the lab demonstrates.

**Fix.** `strip_comments.py` keeps docstrings on functions whose decorators include `command` or `callback`:

```python
FUNCTIONAL_DOCSTRING_DECORATORS = ("command", "callback")
```

`--keep-docstrings` is the blunt escape hatch if some other decorator turns out to be functional too.

**Generalize:** a docstring is not always commentary — `argparse`, `pytest` ids, `doctest` and anything reading `__doc__` at runtime all make it functional. **Check `--help` still works after any strip.**

---

## KI-09 · Tooling references leaked into a submitted report

**Seen in:** `lab00/report.tex` · **Status:** fixed, and now blocked automatically

**Symptom.** The packaged `report.tex` carried a header naming our automation:

```latex
% Render:  tools/render_reports.sh lab00 --keep
% Package: tools/make_submission.sh lab00 nelson-gatlin --figures
```

One of those flags no longer even existed. The submitted document was advertising a build harness that is not part of the coursework — the same boundary [`code_separation.md`](code_separation.md) draws for code, crossed in a document instead.

**Cause.** Build instructions were written into the file they build, because that felt convenient.

**Fix, three layers:**

1. `report_template.tex` carries no tooling references, and says so in its own header, so new reports start clean.
2. `make_submission.sh --figures` strips **comment-only lines** from `.tex` before packaging.
3. A **hard guard** scans every packaged `.tex`/`.md`/`.txt`/`.py` for tooling references and **refuses to build the zip** if any survive, naming file and line.

Layer 3 is the one that actually enforces it; 1 and 2 just keep it tidy.

**Why only comment-only lines are stripped.** In LaTeX a trailing `%` suppresses the following space, so removing it changes the rendering. Deleting a whole comment-only line is safe — TeX consumes such lines entirely, and deleting one does not introduce the blank line that would start a new paragraph. Verified: PDF still 4 pages with identical text after stripping.

**Generalize:** build instructions belong with the build tooling, never in the artifact. If a file is going to be handed to someone else, nothing in it should describe how your repo works.

---

## KI-10 · `report_template.tex` did not build — it pointed at a figure that is never there

**Seen in:** `reference_docs/report_template.tex` · **Status:** fixed

**Symptom.** Build-checking the template failed outright:

```
Unable to load picture or PDF file 'figs/lab0_sinusoids_fig1.png'
```

**Cause.** The template's example figure named a real path from `lab00` — but
the template does not live in `lab00`, and `figs/` is gitignored everywhere, so
the file is absent on any fresh checkout regardless of folder. A template that
cannot be build-checked is a template nobody notices has rotted.

**Fix.** The example figure is wrapped in `\IfFileExists` with a visible
placeholder box as the fallback, so the skeleton compiles with no figures at
all and uses your figure once it exists. Both report files also gained
`\graphicspath{{./}{../}}` so a copy of the document one folder down still
resolves `figs/`.

**How to catch it.** Build the template itself, not only the reports written
from it. It is a document; treat it like one.

---

## KI-11 · A flattened report must never be packaged

**Seen in:** auditing the Overleaf outputs, 2026-09-05 · **Status:** expected — documented, not fixable here

**Symptom.** A report flattened for Overleaf opens with:

```latex
% Generated from content/cesc_410/labs_and_projects/lab00/report.tex -- edit that, not this.
```

That line matches both `reference_docs` and `labs_and_projects` in the
submission guard's pattern, so packaging a flattened copy is refused —
[KI-09](#ki-09--tooling-references-leaked-into-a-submitted-report) firing
exactly as designed, on a file the flattener wrote itself.

**Cause.** The flattener stamps its source path into every output. It lives
under the shared `docs/` tree, which this course does not own.

**Fix.** None needed. A report has no `\input` and needs no flattening. The
`overleaf/` copies exist only for pasting into Overleaf and are gitignored;
**the submission path is always `labNN/report.tex`.**

**How to catch it.** The guard already catches it, before the zip exists. That
is the point of having it.

---

## Template

```markdown
## KI-NN · One-line symptom

**Seen in:** where · **Status:** open / fixed / expected

**Symptom.** What you observe.
**Cause.** Why.
**Fix.** Code or command.
**How to catch it.** The check that would have caught it sooner.
```

---

**Related:** [`../prompt.md`](../prompt.md) · [`../README.md`](../README.md)
