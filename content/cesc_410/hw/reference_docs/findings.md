# Findings — CESC 410 homework

Things learned by doing the work, in the form that would have saved the time.
Ordered by how badly each one bites. **HW-01 through HW-04 are the dangerous
ones: they produce confidently wrong answers, not errors.** **HW-12 and HW-13
are the dangerous ones of a different kind** — neither is a wrong answer. HW-12
produced a confidently wrong *"we do not know"*, costing a round-trip to the
human; HW-13 was a rule that was **correct, enforced, and unreadable at the
moment it was needed**, costing two failed uploads.

Sibling: [`../../labs_and_projects/reference_docs/known_issues.md`](../../labs_and_projects/reference_docs/known_issues.md) (KI-01…KI-09).

---

## HW-01 — `pdftotext` silently corrupts fractions ⚠ **wrong answers, no error**

**Found:** HW1, Problems 3 and 4, 2026-09-04.

`pdftotext -layout` flattens a stacked fraction by emitting numerator and
denominator in visual order, with no delimiter. The result is valid-looking
text that means something else entirely.

| Text layer says | Actually is | Consequence if believed |
| --- | --- | --- |
| `cos( 6π n)` | $\cos\!\big(\frac{\pi}{6}n\big)$ | $\cos(6\pi n) = 1\ \forall n \in \mathbb{Z}$ — the signal becomes a constant, and all four plots are wrong |
| `e^{j(πn/ 8)}` + stray `√` on its own line | $e^{j(\pi n/\sqrt{8})}$ | The $\sqrt{\ }$ is the entire point of the part: with it the signal is **aperiodic**, without it $N_0 = 16$ |

Both misreadings are *plausible*. Neither raises an error. The second is worse:
the stray `√` lands on the wrong line, so it looks like it belongs to part 3.

**Fix — render the region and look at it:**

```python
import fitz
d = fitz.open("/home/devel/electrical_notes/content/cesc_410/hw/hw01/dsphw26-hw1.pdf")
d[0].get_pixmap(clip=fitz.Rect(180, 270, 420, 320), dpi=400).save("/tmp/x.png")
```

Then read the PNG. 400 dpi is enough to resolve a $\sqrt{\ }$ from a `/`.

**Rule: never transcribe an equation from a text layer.** `--grep` is for
*finding* which document discusses a topic, never for reading the maths in it.
This applies to `tools/course_text.py` too — it reads the same broken layer.

---

## HW-02 — The handout numbers two different problems "Prob 1"

**Found:** HW1, 2026-09-04.

`dsphw26-hw1.pdf` has Prob 1 (LO01, phasors) and then, after Prob 5, a second
**Prob 1** (LO05, convolution). There is no Prob 6.

**Fix:** files use a continuous internal index (`p06_convolution.tex`) so they
sort correctly, and **the discrepancy is stated on the face of the document** —
both in `p06` and in the solutions document — so a grader is never left
wondering whether a problem was skipped or duplicated.

**Check the point total against the handout's stated total.** HW1 says 130;
$20+10+20+20+40+20 = 130$ confirms nothing was missed. Do this every assignment;
it is the only cheap check that catches a dropped problem.

---

## HW-03 — `\angle` makes a following minus sign *binary*

**Found:** while rendering the HW1 solutions, 2026-09-04.

`\angle` is a `\mathord`, so TeX parses the `-` in `\angle -75^\circ` as a
**binary** operator and typesets it with space on both sides:

```
  10 ∠ − 75°      wrong — reads as a subtraction
  10 ∠ −75°       right
```

**Fixed in `../../reference_docs/cesc410_macros.tex`** (course level — `/home/devel/electrical_notes/content/cesc_410/reference_docs/cesc410_macros.tex`). `\phasor` wraps its second
argument in `\mathord{}`, which starts a fresh math list so the sign is unary.
Use `\phasor{10}{-75^\circ}` and it comes out right; do not hand-write `\angle`
in problem files.

---

## HW-04 — Verify numerics computationally, and prefer two independent routes

**Found:** HW1 throughout.

A derivation that is internally consistent can still be wrong. Every numeric
answer in HW1 was checked by an independent computation, and two checks caught
things a re-read would not have:

- **Evaluating at a single point proves almost nothing.** $x(0) = A\cos\phi$
  agrees for both $+\phi$ and $-\phi$, since cosine is even. A full-sweep
  comparison over $\omega t$ is the real check (max error $\approx 10^{-14}$).
- **Exact forms beat decimals.** P2's magnitudes are $\sqrt{325} = 5\sqrt{13}$
  and $\sqrt{189} = 3\sqrt{21}$ exactly — confirmed independently by geometry
  (the phasors are $90°$ apart; then the law of cosines). Two routes agreeing on
  a closed form is much stronger evidence than one decimal matching.

**Rule:** for any claim of the form "not periodic" or "no solution exists",
**run the search**. P4 parts 3 and 4 were confirmed by brute-forcing
$N \le 10{,}000$ and finding nothing, which is what makes "aperiodic" a result
rather than an assertion.

---

## HW-05 — `plt`-free plotting: stem plots come from the `.tex`

**Found:** HW1 Problem 3.

The stem plots are drawn by pgfplots from coordinates written directly in the
`.tex` (`\stemplot`), not rendered to image files. Consequences:

- No image files to gitignore, no figure pipeline, nothing to regenerate.
- The plot and the numbers cannot drift apart — they are the same source.
- Zero-valued samples must be listed explicitly to draw the baseline circles
  that the class plotting format uses.

`\stemplot` takes an optional first argument passed straight to the pgfplots
`axis`, so a compact side-by-side version is
`\stemplot[width=\textwidth,height=3.4cm]{...}`.

---

## HW-06 — `axis lines=middle` puts the y-label through the data

**Found:** while rendering HW1 Problem 3, 2026-09-04.

With `axis lines=middle`, pgfplots centres the y-label at mid-height **on the
y-axis**, which is exactly where a full-height stem at $n = 0$ is drawn. The
label and the tallest sample overlap.

**Fixed in `../../reference_docs/cesc410_macros.tex`** (course level — `/home/devel/electrical_notes/content/cesc_410/reference_docs/cesc410_macros.tex`) by anchoring the label to the
axis box corner:

```latex
ylabel style={at={(current axis.north west)}, anchor=south west}
```

**General lesson: a document that compiles is not a document that is correct.**
`docs/latex/build_tex.sh` returning OK says nothing about layout. Render to PNG
and look at it at least once per new visual element.

---

## HW-07 — Build products vs. source material in one folder

**Found:** setting up `hw/.gitignore`, 2026-09-04.
**Approach changed:** 2026-09-08 — the negation was removed. See below.

`hwNN/` holds both generated PDFs (regenerable) and the instructor's assignment
PDF (not regenerable, and the source of truth). A blanket `*.pdf` loses the one
that matters.

**The first fix was `*.pdf` plus `!dsphw*.pdf`. That was wrong and is gone.** A
negation only protects the filenames you predicted: the next handout named
`dsp-bc-...` or `hw2-final.pdf` would have been silently ignored and never
committed, and nobody would notice until it was needed and absent.

**The fix that shipped: ignore OUR output by name, and ignore nothing else.**
Our filenames are ours to predict; the instructor's are not.

```text
$ cd /home/devel/electrical_notes/content/cesc_410/hw
$ git check-ignore -v hw01/p01_phasor_form.pdf hw01/hw01_solutions.pdf \
                      hw01/hw01-nelson-gatlin.pdf hw01/dsphw26-hw1.pdf
content/cesc_410/hw/.gitignore:6:p[0-9][0-9]_*.pdf      hw01/p01_phasor_form.pdf
content/cesc_410/hw/.gitignore:7:*_solutions.pdf        hw01/hw01_solutions.pdf
content/cesc_410/hw/.gitignore:30:hw[0-9][0-9]-*.pdf    hw01/hw01-nelson-gatlin.pdf
```

**Four paths in, three lines out — and the missing one is the point.**
`dsphw26-hw1.pdf` matches no rule, so it prints nothing and stays tracked. The
absence of a line is the pass here, not a failure; `git check-ignore` only exits
non-zero when *nothing at all* matched. Re-run 2026-09-08: exactly those three
lines, in that order.

`git check-ignore -v` names the exact rule that matched. Use it on every
gitignore change; "it looks right" is not a check.

---

## HW-08 — `build_tex.sh <folder>` also tries to build the preamble fragments

**Found:** auditing every `.tex` in the course, 2026-09-05.
**Counts corrected:** 2026-09-08, after the HW-11 move. See the warning below.

`build_tex.sh` builds **every** `.tex` at the top level of a folder it is
pointed at. Two of the course's `.tex` files are not documents, and they now sit
in **two different folders** — so each folder reports exactly **one** FAIL, not
two. Re-run 2026-09-08:

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_410/hw/reference_docs   # 1 file(s) failed.
docs/latex/build_tex.sh content/cesc_410/reference_docs      # 1 file(s) failed.
```

`build_tex.sh` prints `FAIL` on the file's line and the tectonic error indented
underneath it, so read the two together:

| Folder | File | Result | Error printed underneath |
| --- | --- | --- | --- |
| `hw/reference_docs` | `cesc410_preamble.tex` | FAIL | `(job aborted, no legal \end found)` |
| `hw/reference_docs` | `problem_template.tex` | OK | — |
| `reference_docs` (course level) | `cesc410_macros.tex` | FAIL | `LaTeX Error: Command \coursename undefined.` |

Both failures are **correct**. `cesc410_macros.tex` `\renewcommand`s
`\coursename`, which the shared preamble must have `\providecommand`ed first,
and it has no `\begin{document}`; `cesc410_preamble.tex` is a comment-only
tombstone. A fragment that compiled alone would not be a fragment.

⚠ **This finding said "two failures in `reference_docs/`" for three days after
that stopped being true.** `cesc410_macros.tex` moved to the course level on
2026-09-05 ([HW-11](#hw-11--new_texsh-could-not-reach-a-sibling-kinds-macros-file--fixed))
and the expected-output block here was not swept. A reader who saw one FAIL
instead of two had no way to tell whether the repo was broken or the doc was.
Same lesson as HW-11, one finding later: **an expected-output block is a claim
with a date on it, and it has to be re-run when the thing it describes moves.**

**Rule: do not "fix" a fragment by making it build.** Build the template by
name, and read a folder-level FAIL against the list above before believing it.

---

## HW-09 — A flattened file that flattens is not a flattened file that compiles

**Found:** auditing the Overleaf outputs, 2026-09-05.

`flatten_tex.sh` guarantees exactly one thing: no `\input` survived. It never
builds what it wrote, so "flattened OK" and "compiles in Overleaf" are separate
claims and only one of them was being checked.

**Check both:**

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
cd content/cesc_410/hw/hw01/overleaf && for f in *.tex; do tectonic "$f"; done
```

Result on 2026-09-05: all 7 HW1 outputs compiled, plus
`reference_docs/problem_template.tex`. Nothing needed fixing — but nothing had
been *verified* either.

**Generalises past LaTeX:** a generator that validates its own output against a
weaker property than the one you care about will pass forever while shipping
broken artifacts.

---

## HW-10 — The flattener used to stamp a repo path into its output ✅ FIXED

**Found:** grepping the flattened copies for tooling references, 2026-09-05.
**Fixed:** same day, in `docs/latex/flatten_tex.sh`.

Flattened files used to open with a second line naming the full source path
(`content/cesc_410/labs_and_projects/lab00/report.tex`) — a repository path in a
document that might be submitted, emitted by the tool that enforces the
no-tooling-references rule everywhere else. The header now carries only the
**basename**, which locates the source without naming a path.

**⚠ The original write-up of this finding overstated the consequence**, and the
correction is the useful part:

> "Lab reports: blocking. The lab packaging guard scans `.tex` for tooling
> references and refuses to build the zip."

**That was wrong on two independent counts.** Both were tested, not reasoned
about:

1. **The strip runs BEFORE the guard.** `make_submission.sh` pipes the staged
   `report.tex` through `strip_comments.py` (which removes comment-only lines),
   and only *then* runs `find_tooling_refs` on the result. The header was a
   comment-only line, so it never reached the guard. Verified by running the
   project's own `strip_tex` + `find_tooling_refs` in that order: **CLEAN**.
2. **The packager never sees the flattened copy anyway.** It copies
   `$LAB/report.tex` — the source — into the staging folder. `overleaf/` is not
   in the packaged set.

So packaging was never blocked. The path in the header was still worth removing,
which is why it was, but the finding as first written would have sent a future
session chasing a failure that could not occur.

**The transferable lesson: check the ORDER of a pipeline's stages before
concluding one of them rejects your input.** "A guard matches this pattern" is
not the same as "the guard sees this text."

---

## HW-11 — `new_tex.sh` could not reach a sibling kind's macros file ✅ FIXED

**Found:** working out how a `qz01/` would be scaffolded, 2026-09-05.
**Fixed:** by moving the macros file up one level (commit `3fc3d5b`).
**Re-verified:** 2026-09-08 — see below. **Do not act on the old workaround.**

The scaffolder walks up from the target folder running
`find <ancestor> -maxdepth 2 -path '*/reference_docs/*_macros.tex'`. While the
macros file sat at `content/cesc_410/hw/reference_docs/`, that walk from
`content/cesc_410/qz/qz01` saw `qz/reference_docs/` and
`content/cesc_410/reference_docs/` — but **not** `hw/reference_docs/`, three
levels below the common ancestor. It exited 1 before writing a file:

```text
error: no reference_docs/*_macros.tex found at or above content/cesc_410/qz/qz01.
```

**The tempting fix was the wrong one, and still is.** Creating
`qz/reference_docs/cesc410_macros.tex` makes the scaffolder work and triggers
this, correctly:

```text
WARNING: 2 macros files for course 'cesc_410':
         Two files means hw/ and qz/ can silently diverge.
```

Two macros files for one course is a silent-wrong-answer bug: `hw/` and `qz/`
compile against different notation and nothing errors.

**The right fix — one macros file per course, at the COURSE level** — is done:

```sh
find content -name '*_macros.tex'
#   content/cesc_410/reference_docs/cesc410_macros.tex
#   content/cesc_470/reference_docs/cesc470_macros.tex
#   content/cpsc_462/reference_docs/cpsc462_macros.tex
```

That is exactly where the walk reaches from any kind. Verified end to end on a
throwaway `content/cesc_410/qz/qz99/` (created, exercised, deleted) on
2026-09-08: `new_tex.sh` scaffolded a problem file and a solutions document,
resolving `macros: ../../reference_docs/cesc410_macros.tex`; both built; both
flattened; both flattened copies compiled standalone.

**⚠ The stale instruction outlived the bug by three days.** `hw_workflow.md`,
`prompt.md` and this file all still told a reader to copy the template by hand
*"because `new_tex.sh` cannot scaffold a quiz today."* Nothing was wrong when
written; the fix landed elsewhere and no one swept the docs that described the
old behaviour.

**The transferable lesson: a workaround must name the condition it depends on.**
"Copy the template" was written as a fact. Had it been written as *"while the
macros file is under `hw/`, copy the template"*, the move that invalidated it
would have been visible in the same sentence. Detail:
[`hw_workflow.md`](hw_workflow.md#quizzes-and-exams).

---

## HW-12 — "Unconfirmed" was a research failure, not a fact ⚠ **cost a round-trip**

**Found:** applying the human-task standard to this folder, 2026-09-08.

`submission.md` opened with *"Unconfirmed and expected to vary... homework
submission format has not been established"* and listed four open questions.
**Three of the four were answered on disk**, in a PDF sitting two folders away:

```sh
/home/devel/electrical_notes/content/cesc_410/senior_design/cesc410-course-info-fall2026.pdf
```

§ 8.6 *Submission of Work* states the format (PDF only), the paper size
(Letter), the margins (1 inch), and — deciding which of our two documents is the
deliverable — *"Use correct approach and show all necessary intermediate steps."*
§ 11.1 adds a requirement nobody had noticed at all: *"If you use AI tools for
your assignment, you should clearly indicate it."*

**Why it was missed:** the file lives under `senior_design/`, not under `hw/`, and
no doc pointed at it. Nothing was hidden; nothing was looked for either.

**The transferable rule: before writing "unconfirmed", grep the course folder.**
`find` for the course-info PDF by name, and read § *Submission of Work* and the
class-policy section, every time. Two minutes:

```sh
nice -n 19 find /home/devel/electrical_notes/content/cesc_410 -iname '*course-info*'
#   -> senior_design/cesc410-course-info-fall2026.pdf    <- THIS one governs homework
#      senior_design/cesc410L-course-info-fall2026.pdf      the LAB course; different rules
#      senior_design/cesc510-course-info-fall2026.pdf       co-listed grad section; § 8.7 == § 8.6

pdftotext -layout \
  /home/devel/electrical_notes/content/cesc_410/senior_design/cesc410-course-info-fall2026.pdf - \
  | sed -n '/Submission of Work/,/^[0-9]* Class/p'      # 25 lines, § 8.6 entire
```

**Three files come back, not one, and picking the wrong one gives you the wrong
rules.** The lecture course governs; `410L` is the lab course and its submission
section does not apply here.

**And the sharper version, which is the whole point of
[`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md):**
*"unconfirmed" is a conclusion, and a conclusion has to show its work.* A question
handed to a human must say what was already searched, who can answer it, what was
assumed meanwhile, and what changes if the assumption is wrong. Four sentences.
Without them the human re-runs the search you did not do — which is exactly what
happened on the Lab 1 Canvas hunt.

**What is genuinely still unknown**, verified by negative greps rather than
assumed: the submission *destination*. The CESC 410 info never says "Canvas"
(`grep -ci canvas` → 0), and the HW 1 handout says nothing about submission at
all. Those are real questions and they are written up as such in
[`submission.md`](submission.md#still-unknown--and-exactly-how-to-ask).

---

## HW-13 — The Overleaf rule was documented everywhere except where it was needed ⚠ **cost two failed uploads**

**Found:** 2026-09-08, the second time a source `.tex` was uploaded to Overleaf
and failed. **Fixed:** same day.

Nothing was broken. `flatten_tex.sh` worked, the flattened copies compiled, and
the rule was written down in three places —
[`coursework-solutions.md`](../../../../docs/directives/coursework-solutions.md)
§ Overleaf, [`docs/latex/INDEX.md`](../../../../docs/latex/INDEX.md), and
[`hw_workflow.md`](hw_workflow.md) § Overleaf. **The defect was that none of
those is on screen at the moment the mistake is made.** The operator opens
`hw01_solutions.tex`, drags it into a browser, and the file itself says nothing.

The audit that made it obvious, run when the second failure was reported:

```sh
cd /home/devel/electrical_notes
# sources that begin with \input -- i.e. cannot compile on Overleaf
grep -lE '^\s*\\input\{' content/cesc_4*/hw/hw01/*.tex \
    content/cesc_410/hw/reference_docs/problem_template.tex | wc -l   # 19
# ...of which, how many say so?
grep -lie overleaf content/cesc_4*/hw/hw01/*.tex \
    content/cesc_410/hw/reference_docs/problem_template.tex | wc -l   # 0
```

**19 files that cannot be uploaded. 0 of them saying so.**

**Fix — a six-line `OVERLEAF` comment block at the top of every source**, above
the `\input` lines, naming the flattened copy by absolute path. Supporting
changes so it does not decay:

| Where | Change |
| --- | --- |
| `new_tex.sh` | emits the marker into every scaffolded file, paths filled in — the actual prevention, since the scaffolder is the normal route and the template is the fallback |
| `flatten_tex.sh` | strips the marker from the flattened copy (where it would be *false*), and warns for any source with `\input` and no marker |
| `problem_template.tex` | carries the marker, and tells a hand-copier to re-point it |

**The transferable lesson, and it is not about LaTeX: a correct fix in the wrong
location is not a fix.** Documentation is read *before* a task and *after* a
failure, never *during*. Anything that must be known at the instant of an action
has to live on the artifact the hand is touching. Ask of every rule: *what will
this person have open when they get it wrong?* — and put it there.

---

## HW-14 — The flattener drops tooling comments line-by-line, cutting sentences in half

**Found:** 2026-09-08, checking that the new `OVERLEAF` marker strips cleanly.
**Not fixed** — reported, with the fix proposed and deliberately not applied.

`flatten_tex.sh` drops a comment-only line when it matches `TOOLING_RE`. At
depth > 0 it drops *every* comment, precisely because line-by-line stripping
"left sentences cut in half" — the script says so in its own comment. **At depth
0 that reasoning was never applied**, and the same thing happens to the user's
own file. From `problem_template.tex` before this was noticed:

| In the source | In the flattened copy |
| --- | --- |
| `…Decide it once per assignment -- see the` / `reference_docs/submission.md human tasks -- and add one line under the` / `problem header.` | `…Decide it once per assignment -- see the` / `problem header.` |

The middle line matched `reference_docs/`, so it went; the two around it did
not, so they stayed, welded into a sentence that says nothing.

**It also re-opens [HW-10](#hw-10--the-flattener-used-to-stamp-a-repo-path-into-its-output--fixed).**
HW-10 removed the repo path the flattener *stamped* on its output. A repo path
the flattener *passes through* is the same problem by a different route:

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/reference_docs
grep -n /home/devel content/cesc_410/hw/reference_docs/overleaf/problem_template.tex
#   % for qz/ and exam/ too. From the REPO ROOT, /home/devel/electrical_notes:
```

An absolute repo path, in a document that may be submitted, emitted by the tool
that enforces the no-tooling-references rule elsewhere — the exact sentence
HW-10 was written to retire. It survives because `TOOLING_RE` matches tool and
path *fragments*, and that line happens to contain none of them.

**Proposed fix: strip contiguous comment BLOCKS, not lines.** Treat a run of
consecutive comment lines, bounded by a blank line or a bare `%`, as one unit;
if any line in it matches `TOOLING_RE`, drop the whole unit. On the template
this removes both mangled paragraphs and the leaked path, and keeps the
`THIS FILE IS THE GRADED ARTIFACT` paragraph, which is separated by a bare `%`
and names no tooling.

**Why it was not implemented here:** it changes the output of every flattened
file, and the brief that surfaced it allowed a tooling change only where it
*could not* break existing use. This can. It wants its own change, with a
before/after diff of all 19 flattened copies as the evidence.

**Meanwhile the marker is safe from it**, by construction rather than by luck:
every line of the marker names Overleaf, a script, or a repo path, so all six
are dropped individually and nothing is left welded together. Anyone rewording
the marker must preserve that, and can check it in one command:

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
grep -i overleaf content/cesc_410/hw/hw01/overleaf/*.tex   # expect no output
```

---

## HW-15 — "Self-contained" was stamped on a file that cannot compile ✅ FIXED

**Found:** 2026-09-08, verifying the OVERLEAF marker work by building every
flattened copy **alone in an empty directory**, the way Overleaf builds it.

21 of 22 copies compiled. The one that did not was
`hw/reference_docs/overleaf/cesc410_preamble.tex`:

```text
error: !Emergency stop
*** (job aborted, no legal \end found)
```

Nothing was wrong with the flattening. `flatten_tex.sh <dir>` flattens **every**
`.tex` in the folder, and `cesc410_preamble.tex` is the superseded tombstone of
[HW-08](#hw-08--build_texsh-folder-also-tries-to-build-the-preamble-fragments)
— comment-only, no `\begin{document}`. Flattening a fragment yields a fragment,
and the header the script writes on every output then reads:

```text
% Self-contained: preamble inlined, no external \input.
```

on a file that compiles to nothing. **That header sat in the one folder a human
is told to upload from**, beside the real copy, under the same instruction. The
marker block exists to end which-file-do-I-upload; a second, broken file in the
destination folder re-opens the question one directory later.

**Fixed:** the flattener writes to a temp file, checks it for a **non-comment**
`\begin{document}`, and refuses to emit one that has none — deleting any copy an
earlier run left behind:

```text
  cesc410_preamble.tex     -> removed stale copy (fragment)
  (1 fragment(s) skipped: no \begin{document}, so nothing to upload.)
```

Non-comment matters: the tombstone *quotes* the line it tells you to write
(`%   \begin{document}`), and the first version of the check was fooled by it.

**Evidence it broke nothing**, the bar [HW-14](#hw-14--the-flattener-drops-tooling-comments-line-by-line-cutting-sentences-in-half)
set for changing this script: md5 manifest of every flattened copy before and
after — 22 files to 21, the removed line being the tombstone copy, **every other
file byte-identical**. Standalone rebuild after the change: 20 of 21 compile.

### The remaining one is not a fragment — `\includegraphics` is not inlined

`labs_and_projects/lab00/overleaf/report.tex` fails alone with

```text
error: Unable to load picture or PDF file 'figs/lab0_sinusoids_fig1.png'
```

and compiles to 4 pages the moment `figs/` is beside it. Flattening inlines
**text**; an `\includegraphics` still points outside the file. "Self-contained"
was over-claimed for any document with figures — the tombstone's mistake one
level up. The flattener now prints a `NOTE` listing every image an output needs
(comments stripped first, so `% \includegraphics` in prose does not raise one),
and its closing line no longer says "it needs no other file" when there are any.

**Standalone means no other `.tex`. It does not mean no other file.**

**The lesson, twice in one sweep:** a generator that prints a claim about its
own output has to check the claim it prints. "No `\input` survived" was checked;
"is a document" and "needs no other file" were asserted in the output header and
never checked at all.

---

**Related:** [`README.md`](README.md) · [`hw_workflow.md`](hw_workflow.md) · [`../prompt.md`](../prompt.md) · [`submission.md`](submission.md) · [`../hw01/README.md`](../hw01/README.md)
