# Claude entry point — CESC 410L labs

**Trigger:** *"`labNN/` now exists with the lab material in it, get it all done."*

Read this file, then the docs it points at, then work. Stop only for the things listed under [Human-only](#human-only).

---

## Read first (in order)

1. This file.
2. [`README.md`](README.md) — layout, conventions, environment.
3. [`reference_docs/known_issues.md`](reference_docs/known_issues.md) — **check before debugging anything.** Recurring traps live here.
4. [`reference_docs/code_separation.md`](reference_docs/code_separation.md) — **which code is submitted and which is not.** Read before writing anything.
5. [`reference_docs/code_commenting.md`](reference_docs/code_commenting.md) — how to comment what you write.
6. [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md) — **what this lab actually has to hand in. Largely unconfirmed; surface it.**
7. The lab's own handout in `labNN/` (`.md` preferred over `.pdf` — the `.md` is the source and has the code in copyable form).
8. [`reference_docs/py-pkg-1c-uv-cs.md`](reference_docs/py-pkg-1c-uv-cs.md) — the instructor's `uv` cheatsheet. Only if the lab does something new with packaging.

---

## Procedure

### 1. Inventory the lab folder

List what is in `labNN/`. Then read the handout and build the expected-inputs list — every file the handout names or links to. Run:

```sh
uv run --project dsp26 python tools/check_inputs.py
```

**Report anything missing before starting work.** Handouts commonly reference a `.zip` of starter code, a dataset, or a sibling document that was not downloaded. Missing inputs are the single most common reason a lab stalls, and they need a human to fetch them from Canvas.

Record the result as the **Inputs** table in the lab README (see the template).

### 2. Extract the work

From the handout, separate:

- **Code to write** — usually into `dsp26/src/dsp26/labN_<topic>/`, plus a command in `app_cli.py`. This is **lab code**: it gets submitted, so it must stand alone and read like a student's solution.
- **Runs to perform** — the CLI invocations that produce output.
- **Artifacts to produce** — figures, numbers, tables. These are the deliverable.
- **Questions to answer** — handouts often bury prose questions between code blocks. They are graded. Collect them explicitly.

### 3. Do it

Write the code, run it, save artifacts into `labNN/figs/` (or `labNN/out/` for non-figures). Verify:

```sh
uv run --project dsp26 python tools/check_artifacts.py labNN/figs
```

**Keep lab code and automation separate** — [`reference_docs/code_separation.md`](reference_docs/code_separation.md). `dsp26/` is submitted and must work with `tools/` deleted; `tools/` is ours and never ships. Anything that exists only because we drive the lab from a terminal is automation.

**Comment as you write** — [`reference_docs/code_commenting.md`](reference_docs/code_commenting.md). One comment per logical step, naming the operation ("take the DFT and shift zero frequency to the centre"), never restating syntax. Put the governing equation in the docstring; it becomes the report's equation block.

**Transcribe handout code faithfully first, then fix.** If handout code is wrong, keep the structure and mark the change with a `DEVIATION FROM HANDOUT:` comment saying what the handout had, what broke, and why. The TA sees this code — an unexplained rewrite looks like the student didn't follow the lab. A marked, justified fix looks like engineering. Log every deviation in the lab README and, if it could recur, in `known_issues.md`.

### 4. Write `labNN/README.md`

Copy [`reference_docs/lab_template.md`](reference_docs/lab_template.md) and fill it. It is a **reproduction log**, not a summary: someone should be able to reproduce the lab from it without opening the handout. Every command verbatim, in order, with what it printed.

### 5. Report, if the lab needs one

Copy [`reference_docs/report_template.tex`](reference_docs/report_template.tex) to `labNN/report.tex` and fill the four sections. Verify it builds:

```sh
tools/render_reports.sh labNN
```

The `.tex` is the artifact — the human pastes it into Overleaf. The PDF is deleted after the build check.

### 6. Report back

Tell the human:

- What is done and verified.
- What is blocked, and on what.
- **Everything from [Human-only](#human-only) that this lab needs.**

---

## Human-only

Do not attempt these. Surface them clearly instead.

| Task | Why |
| --- | --- |
| **ERAU ID digits** | Labs seed an RNG with the last 4 digits of the student's ID, which changes every number and figure. The handout placeholder is `1234`. **Ask; never guess.** Grep for `myID` to find it. |
| **Live demo** | Graded at the start of each lab meeting. The report is not assessed until a TA sees the demo. |
| **Canvas submission** | Report + code, before the *next* lab meeting. Late is a zero, no resubmission. |
| **Confirming what a lab must submit** | Course info and handouts disagree. Only the TA can settle it — [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md). |
| **Downloading handouts / starter files** | Canvas login. |
| **Interactive GUI runs** | This environment is headless; `plt.show()` is a no-op. Anything needing a real window, or a screenshot of one, is human work. Prefer saving to a file — the handouts sanction it. |
| **Team coordination** | Teams of two, rebuilt every two labs from Lab 3. One submission per team, except on ABET-artifact labs where every student submits independently. |
| **Judging whether a deviation is acceptable** | Flag it; let the human decide whether to keep, revert, or mention it to the TA. |
| **Writing the lab report** | Draft it if asked, but it is the student's account of their own work. Structure: [`reference_docs/report_guide.md`](reference_docs/report_guide.md). |

---

## Rules

- **Never commit `.venv/`.** It is ~250 MB. It is gitignored; keep it that way. If a lab makes a venv under a different name, add it to `.gitignore` and say why in the lab README.
- **Commit `uv.lock`.** It is what makes the environment reproducible.
- **One package, many labs.** `dsp26` is shared for the whole semester — each lab adds a subpackage and a CLI command, not a new project. This is the handout's design, not ours.
- **Documentation lives in `labNN/`; lab code in `dsp26/`; automation in `tools/`.** Deliberate — see [`README.md`](README.md#why-code-and-docs-are-split) and [`reference_docs/code_separation.md`](reference_docs/code_separation.md).
- **Figures: save PNG and SVG.** The report needs PNG; handouts save SVG only, so this is a marked deviation.
- **`figs/` is gitignored** — regenerable, and images bloat git. Never `git add` it without `-f` and a reason.
- **Comment every file so it stands alone** ([`reference_docs/code_commenting.md`](reference_docs/code_commenting.md)). Comments are stripped at submission time by `tools/make_submission.sh`, so write them for us, not for the TA — but **never strip a `DEVIATION FROM HANDOUT` block**, which is disclosure.
- **Never put tooling references in a deliverable.** No script names, flags or repo paths in a report `.tex`/`.md`. Packaging blocks on it.
- **Never hand-edit code for submission.** `make_submission.sh` strips into a staging copy; the working tree keeps its comments.
- **Verify, don't assume.** Run it. Check the output is what the handout describes. Two identically-sized output files are a bug, not a coincidence.
- **Publishing and git are not a concern for this project.** The parent repo has a remote and a Hugo `baseURL`, but that does not apply here — see [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md#publishing-and-git--not-a-concern-here). Do not raise it, do not add redaction steps.
- **Prefer the `.md` handout over the `.pdf`.** Same content, copyable code, and it shows the instructor's build commands.

---

**Related:** [`README.md`](README.md) · [`reference_docs/known_issues.md`](reference_docs/known_issues.md) · [`reference_docs/code_separation.md`](reference_docs/code_separation.md) · [`reference_docs/code_commenting.md`](reference_docs/code_commenting.md) · [`reference_docs/report_guide.md`](reference_docs/report_guide.md) · [`reference_docs/lab_template.md`](reference_docs/lab_template.md)
