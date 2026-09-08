# CESC 410 homework — reference docs

Doctrine, template and hard-won traps for `content/cesc_410/hw/`. Start here;
the per-assignment README (e.g. [`../hw01/README.md`](../hw01/README.md)) covers
one assignment, this folder covers all of them.

---

## ⚠ Submitting? Do NOT upload the `.tex` you are looking at

**This is the mistake this repo has now made twice.** You open the obvious file,
in the obvious folder, with the obvious name — `hw01_solutions.tex` — drag it
into Overleaf, and get:

```text
LaTeX Error: File `../../../../docs/latex/coursework_preamble.tex' not found.
./main.tex, 1
```

Nothing is broken. **Every source `.tex` here is deliberately not self-contained**
— it `\input`s one shared preamble by a relative path that climbs above the repo
root, which is right for this repo and impossible inside an Overleaf project.
There is a second, self-contained copy of **every source that is a document**,
and that is the one to upload. (A fragment — a `_macros.tex`, or the
`cesc410_preamble.tex` tombstone — gets no copy: it has no `\begin{document}`,
so there is nothing to upload. `flatten_tex.sh` skips those and says so.)

### H1 · Upload the flattened copy · Why human: Credentialed (Overleaf login)

**WHERE.** Beside the source, in a folder called `overleaf/`, under the **same
filename**. For HW 1:

| Source (FROM) — do NOT upload | Flattened copy (TO Overleaf) — upload this |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/hw01_solutions.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/hw01_solutions.tex` |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/p01_phasor_form.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/p01_phasor_form.tex` |
| …and so on for `p02`…`p06` | same name, one folder deeper, in `overleaf/` |

The rule generalises: **insert `overleaf/` before the filename.** Nothing else
changes — not the name, not the content you care about.

**WHAT.** In Overleaf, *New Project → Upload Project*, or drag the single `.tex`
into an existing project. It needs **no other `.tex`**: the preamble is already
inlined in it. Do not also upload `coursework_preamble.tex`, and do not upload
the `overleaf/` folder's parent. **Images are the one exception** — flattening
inlines text, not PNGs, so a document with `\includegraphics` needs its `figs/`
uploaded beside it. `flatten_tex.sh` prints a `NOTE` naming every image an
output needs; homework files here have none, lab reports do.

**VERIFY — before you upload, not after.** Compile the copy locally; if it
builds here with no arguments and no neighbours, Overleaf will build it too:

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf
timeout 300 tectonic hw01_solutions.tex
```

Expected: `Writing 'hw01_solutions.pdf'` and a PDF beside it. **Expected NOT to
appear anywhere in the output: the words `not found`.** A `File ... not found`
here means the copy is not actually flattened — regenerate it (below) rather
than uploading it. Belt and braces, since a flattened file that *flattens* is
not the same claim as a flattened file that *compiles*
([findings.md HW-09](findings.md)):

```sh
grep -c '\\input{' hw01_solutions.tex     # expect 0
```

**IF THE `overleaf/` FOLDER IS EMPTY, MISSING, OR STALE.** All three happen, and
the fix is the same one command. `overleaf/` is **gitignored and regenerable**,
so a fresh clone has none of it and neither does a machine that has not run the
flattener yet — an empty folder is normal, not damage.

```sh
cd /home/devel/electrical_notes
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
```

Stale is the dangerous one, because a stale copy uploads cleanly and grades
wrong. Check it — a copy older than its source is stale:

```sh
cd /home/devel/electrical_notes
d=content/cesc_410/hw/hw01
for f in "$d"/*.tex; do
  # A fragment gets no flattened copy, so its absence is not a fault.
  grep -qE '^[^%]*\\begin\{document\}' "$f" || continue
  t="$d/overleaf/$(basename "$f")"
  if   [ ! -e "$t" ];     then echo "MISSING  $t"
  elif [ "$f" -nt "$t" ]; then echo "STALE    $t"
  else echo "ok       $(basename "$f")"; fi
done
```

Anything but `ok` on every line → re-run `flatten_tex.sh` on the folder. It is
idempotent and takes about a second; when in doubt, just run it.

**Never hand-edit a file under `overleaf/`.** It is generated output and the
next `flatten_tex.sh` overwrites it without asking. Fix the source, re-flatten.

**BLOCKS.** Only the Overleaf route. Building, checking, and producing the PDF
locally are unaffected — `docs/latex/build_tex.sh` uses the sources directly and
never touches `overleaf/`. If the deliverable is a **PDF** rather than an
Overleaf project, you do not need any of this; see
[`submission.md` § Producing the PDF](submission.md). **Where the finished work
is submitted is still an open question** — it is written up as a human task in
[`submission.md` § H1](submission.md).

### Why the source cannot simply be made to work

Because the alternative is worse. One shared preamble means no drift across
three courses; uploading a copy of the preamble into each Overleaf project means
re-syncing every project by hand whenever the shared file changes. So the source
keeps its `\input` and the flattener produces the standalone copy on the way
out. Full reasoning:
[`../../../../docs/directives/coursework-solutions.md` § Overleaf](../../../../docs/directives/coursework-solutions.md).

### You should not have needed this README

Every source `.tex` now opens with a six-line `OVERLEAF` comment block saying the
same thing, above the `\input` lines, so it is the first thing on screen when the
file is opened. That marker — not this page — is the actual fix; a warning that
lives only in a document nobody has open at the moment of the mistake is not
available knowledge. `new_tex.sh` writes the marker into every new file, and
`flatten_tex.sh` warns about any source missing one.

---

## What is in this folder

| File | What it is | Read it when |
| --- | --- | --- |
| [`hw_workflow.md`](hw_workflow.md) | How a homework gets built, start to finish | Beginning any assignment |
| [`submission.md`](submission.md) | What the course requires, deadlines, and the open human tasks | Before submitting anything |
| [`findings.md`](findings.md) | Traps already hit, with the fix. HW-01…HW-04 produce **wrong answers, not errors** | Before trusting a number or a PDF text layer |
| [`problem_template.tex`](problem_template.tex) | The five-section per-problem template | Only if not using `new_tex.sh` — see below |
| [`cesc410_preamble.tex`](cesc410_preamble.tex) | **SUPERSEDED tombstone.** Do not `\input` it | Never; it explains where its contents went |
| `overleaf/` | Generated, gitignored, regenerable flattened copies — **documents only**, one per source that has a `\begin{document}` | Uploading to Overleaf |

Course-level macros live **outside** this folder, at
`/home/devel/electrical_notes/content/cesc_410/reference_docs/cesc410_macros.tex`
— one per course, shared by `hw/`, `qz/` and `exam/`.

> ⚠ `docs/latex/build_tex.sh content/cesc_410/hw/reference_docs` reports **one**
> FAIL, and that is correct: `cesc410_preamble.tex` is a comment-only tombstone
> with no `\begin{document}`. Do not "fix" a fragment by making it build —
> [findings.md HW-08](findings.md).

---

## Starting a new problem file

**Scaffold it; do not copy the template by hand.** `new_tex.sh` computes both
`\input` paths from the target's depth instead of trusting a `../` count, works
for `qz/` and `exam/` as well as `hw/`, and writes the `OVERLEAF` marker with
that file's own paths already filled in.

```sh
cd /home/devel/electrical_notes
mkdir -p content/cesc_410/hw/hw02                       # new_tex.sh will not create it
docs/latex/new_tex.sh content/cesc_410/hw/hw02 1 phasors --pts "20 pts" --lo LO01
docs/latex/build_tex.sh content/cesc_410/hw/hw02/p01_phasors.tex
```

Copying [`problem_template.tex`](problem_template.tex) also works — its two
`\input` lines are already correct for `content/cesc_410/hw/hwNN/` depth — but
then you must re-point the `OVERLEAF` block at the top so it names the new file
instead of the template. The scaffolder does that for you.

---

**Related:** [`../hw01/README.md`](../hw01/README.md) ·
[`../prompt.md`](../prompt.md) ·
[`../../../../docs/latex/INDEX.md`](../../../../docs/latex/INDEX.md) ·
[`../../../../docs/directives/coursework-solutions.md`](../../../../docs/directives/coursework-solutions.md) ·
[`../../../../docs/directives/human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md)
