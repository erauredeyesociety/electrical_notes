# Lab report guide

> ⚠ **The structure below is carried over from CEC 320 (same instructor, Dr. Jianhua Liu) and has *not* been confirmed against a CESC 410L template.** No report template has been posted for this course yet. Confirm with the TA at the first lab meeting and correct this file. Everything else here holds regardless.

A lab report is **not** the same document as `labNN/README.md`:

| | `labNN/README.md` | The report |
| --- | --- | --- |
| Audience | us, and future-you | the TA |
| Purpose | reproduce the lab exactly | show the work and what was learned |
| Content | every command, verbatim, in order | prose, selected artifacts, answers |
| Submitted | no | **yes** |

Write the README as you work. Write the report from the README at the end.

---

## Four sections

### 1. Introduction

The lab, in your own words. What it asks for and why. Include preparation or background reading. Short.

### 2. Narrative

**How the procedure differed for you.** Modifications, problems, bugs, and how they were resolved. Research done to fix something belongs here.

This is where deviations from the handout go — it is a *graded* section, and a real debugging story is exactly what it is asking for. The [`known_issues.md`](known_issues.md) entries written during the lab are the raw material.

### 3. Artifacts — code snippets and screenshots

Only code you **added, modified, or commented on**. Not the whole file.

- Name the source file above each snippet.
- Caption each one: `Code Snippet 1 — sinusoids.py`.
- Number figures and refer to them by number.
- **Avoid dark backgrounds in screenshots.** Reports may be printed; CEC 320's template asked for this explicitly and it presumably still applies.

Formatting from the CEC 320 template — confirm it carries over:

| Part | Font |
| --- | --- |
| Narrative | Times Roman 12, single spaced |
| Code | Courier New 12, single spaced |

### 4. Discussions and results

Takeaways — what was learned, how it applies later. Then, explicitly:

- **Answer every question in the handout.** Handouts bury questions between code blocks; they are graded. Collect them while reading, not at the end.
- Summarize results.

---

## Format: Markdown or LaTeX

Two options. **LaTeX is preferred when the lab involves real math** — which is most of them in a DSP course.

| | Markdown | LaTeX |
| --- | --- | --- |
| Source | `labNN/report.md` | `labNN/report.tex` |
| Math | fenced `$…$`, renders inconsistently | native, unambiguous |
| Overleaf | no | **paste and go** — the report has no `\input` to resolve |
| Figures | relative links | `\includegraphics` |
| Check it builds | — | `tools/render_reports.sh labNN` |

> **Keep reports free of tooling references.** A report is a submitted document; nothing in it should name a script, a flag or a repository path. Build and packaging instructions live in this guide, not in the `.tex`. Packaging strips LaTeX comment-only lines and then **refuses to build the zip** if any tooling reference survives — see [KI-09](known_issues.md#ki-09--tooling-references-leaked-into-a-submitted-report).

Start from [`report_template.tex`](report_template.tex) — a complete standalone document with the four sections, a worked equation, a code listing and a figure already wired up.

### The report keeps its own preamble — deliberately

The homework side of this course shares one preamble across every problem file.
**Lab reports do not, and must not.** The reasons, in order of weight:

1. **A handed-in `.tex` has to compile wherever the reader puts it.** A shared
   preamble is reached by a relative path that resolves only at one exact depth
   inside this repository. Packaging copies `report.tex` into a staging folder;
   at that point the path is dead and the TA's copy does not build.
2. **The packaging guard would reject it.** The guard scans every `.tex` about
   to ship for repository paths, and an `\input` of a course macros file is a
   *non-comment* line — comment stripping cannot save it, so the zip is refused.
   Confirmed by running the guard against exactly that line.
3. **Different document shape.** A report is prose and figures under a title
   block. It wants no running head, no answer box, no problem header — which is
   most of what a solutions preamble exists to provide — and it does need
   `listings`, which that preamble does not load.

The overlap is four `\usepackage` lines, a margin and a `captionsetup`. That is
the whole cost, and both `report_template.tex` and `lab00/report.tex` carry a
header comment saying so, so the duplication is not mistaken for an oversight.

### The figure in the template is guarded

`figs/` is gitignored, so a fresh copy of the template has no figures and used
to fail to build on a missing image. The template now wraps its example figure
in `\IfFileExists` and falls back to a visible placeholder box, so the skeleton
compiles before you have generated anything. Drop the guard and keep the plain
`\includegraphics` line once your own figure is in place.

Both report files also set `\graphicspath{{./}{../}}`, so a copy of the document
sitting one folder down still finds `figs/`.

```sh
cp reference_docs/report_template.tex lab01/report.tex
# ...write it...
tools/render_reports.sh lab01
```

**`tools/render_reports.sh` is the only script that renders.** `make_submission.sh --figures` calls it rather than invoking tectonic itself, so rendering behaviour lives in one place.

> Use it rather than the shared homework build-checker. That one **deletes the
> PDF** unless asked not to, which is the opposite of what a report wants.

### If you flatten a report for Overleaf

A report needs no flattening — it has no `\input`. Flattening one anyway
produces a byte-identical render (verified on `lab00`: 4 pages, same extracted
text, same four images) and lands in `labNN/overleaf/`, which is gitignored.

⚠ **Never package a flattened copy.** The flattener writes the source path into
the file's header, and the submission guard refuses to build a zip containing a
repository path. The submission path is always `labNN/report.tex`.

**PDFs are kept, not deleted.** They are gitignored (`report*.pdf`), so the built report is on hand without a rebuild and still never enters the repo. The `.tex` remains the source you paste into Overleaf; the PDF is what a reader opens.

Rendering uses **tectonic**, already installed — self-contained, no TeX Live, fetches packages on demand. First run needs network.

*If you would rather write Markdown and convert, that needs pandoc (`sudo apt install pandoc`), which is **not** installed. Authoring `.tex` directly avoids a conversion step and a dependency, which is why the template is LaTeX.*

**Equations come from the code.** The commenting standard ([`code_commenting.md`](code_commenting.md#math)) puts the governing equation in each function's docstring in LaTeX-ish notation — so the report's `equation` blocks are close to copy-paste from source you already wrote.

---

## Header block

```
CESC 410L – Section <NN>
Lab #: <Lab Title>
Lab Start Date: MM/DD/YYYY
Report Date: MM/DD/YYYY
Team: <names, or "individual" on ABET-artifact labs>
```

---

## Practical notes

- **The demo is graded before the report is read.** Live demo at the start of each meeting; the report is not assessed until a TA has seen it. Get the thing running first.
- **One report per team** — except ABET-artifact labs, where every student submits independently and the artifact must be their own work.
- **Late is a zero.** No resubmission. Submit the previous lab's report and code before the next meeting.
- **Figures:** the CLI saves both SVG and PNG (a marked deviation — the handout saves SVG only). **Use the PNGs in the report;** SVG does not paste reliably into word processors, and `\includegraphics` handles PNG without extra packages.
- **`figs/` is gitignored.** Regenerate before rendering, or `render_reports.sh` fails on the missing image — intended behaviour, not a bug:
  ```sh
  cd dsp26 && MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN
  ```

---

**Related:** [`report_template.tex`](report_template.tex) · [`code_commenting.md`](code_commenting.md) · [`lab_template.md`](lab_template.md) · [`code_separation.md`](code_separation.md) · [`../prompt.md`](../prompt.md)
