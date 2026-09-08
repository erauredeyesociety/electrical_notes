# Shared tooling this course can use

Everything here already exists and is shared across courses — **do not write a
course-local copy.** Paths are from the repository root
(`/home/devel/electrical_notes`).

## LaTeX toolchain — [`docs/latex/`](../../../docs/latex/INDEX.md)

| Tool | Language | Use it when |
| --- | --- | --- |
| [`new_tex.sh`](../../../docs/latex/new_tex.sh) | bash | Starting a new problem file. It **computes** the `../` depth of the `\input` lines instead of you counting them, and writes the Overleaf marker for you. |
| [`build_tex.sh`](../../../docs/latex/build_tex.sh) | bash | Checking a file or a whole assignment compiles. Deletes the PDF unless `--keep`. Also checks the Overleaf copies are current. |
| [`flatten_tex.sh`](../../../docs/latex/flatten_tex.sh) | bash | Producing the file you actually upload to Overleaf, and `--check`ing that the ones you have are still current. |
| [`coursework_preamble.tex`](../../../docs/latex/coursework_preamble.tex) | LaTeX | The shared preamble. Every problem file `\input`s it. Course-specific *notation* goes in this course's own `cesc_470_macros.tex`, never here. |

```sh
cd /home/devel/electrical_notes
docs/latex/new_tex.sh   content/cesc_470/hw/hw02 p01_some_problem
docs/latex/build_tex.sh content/cesc_470/hw/hw02
docs/latex/flatten_tex.sh content/cesc_470/hw/hw02      # -> overleaf/, upload from there
docs/latex/flatten_tex.sh --check                 # are all copies current?
```

> ⚠ **Upload the copy in `overleaf/`, never the source.** The source `\input`s
> a path above the project root, which Overleaf cannot resolve — it fails with
> `File '../../../../docs/latex/coursework_preamble.tex' not found`. Every source
> file says so in its first six lines. `overleaf/` is gitignored and regenerable.

## Repo-wide doctrine

| Document | Governs |
| --- | --- |
| [`docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md) | The two-document rule, citations, one macros file per course, what to gitignore |
| [`docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md) | How a task handed to the human must be written |

## Python tooling — per course, not shared

CESC 410's labs carry their own Python under
`content/cesc_410/labs_and_projects/tools/` (artifact and input checks, a
submission packager, a comment stripper). Those are **specific to that course's
`dsp26` package** and are not shared. If this course grows a need for
something similar, copy the *pattern*, not the files, and keep it under this
course's own `tools/`.

**The LaTeX toolchain above is bash, not Python.** Worth stating because the two
get conflated: `docs/latex/*.sh` is shared and repo-wide; `*/tools/*.py` is
course-local.

## Before you submit anything

**Read the handout's own deliverables section — not its task descriptions.** They are different
passes, and reading only the tasks is how a lab gets submitted with files nobody asked for.

```sh
grep -inE 'submit|deliverab|artifact' <the handout>.md
```

- **If the handout is explicit, follow it exactly.** No additions, however harmless. CESC 410L Lab 1
  says *"Submit a single PDF file containing all the artifacts"* — one file, and a code archive
  alongside it would have been 93% dependency lockfile and 1.8% the *previous* lab's code.
- **If the handout is silent, over-submitting is the right default** — and only then.
- **Look inside any bundle before sending it.** `unzip -l` takes two seconds. A "code" archive is not
  necessarily code.

Full rule and the incident behind it:
[`docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md)
§ *Read the handout's own deliverables section*.
