# Findings — CESC 470 homework

Things learned by doing the work, in the form that would have saved the time.
Ordered by how badly each one bites. **HW-01 through HW-04 are the dangerous
ones: they produce confidently wrong output, not errors.**

Sibling course under the same doctrine, worth reading:
[`../../cesc_410/hw/reference_docs/findings.md`](../../cesc_410/hw/reference_docs/findings.md).

---

## HW-01 — Module 01's text layer is thin, and "62 of 88" is easy to misquote ⚠

**Found:** auditing the course, 2026-09-05.

[`Module 01 Introduction to computer technology & ISA (1).pdf`](<../Module 01 Introduction to computer technology & ISA (1).pdf>)
is 88 pages. The triage tool grades it:

```text
verdict: ocr-partial
  ok 26   sparse 48   empty 14
  ! letter-spacing artefacts detected (one glyph per text run)
```

**62 of 88 pages are flagged `sparse` or `empty`** (48 + 14). That is where the
number comes from, and it is *not* the same claim as "62 pages are image-only":

| Measure | Count |
| --- | ---: |
| Flagged `sparse` **or** `empty` by the triage tool | **62** |
| Genuinely no text layer (< 20 chars) | **7** — pages 2–6, 49, 68 |
| Carrying a raster image | 37 |
| Carrying usable prose (> 120 chars) | 53 |

Calling all 62 "image-only" overstates it, and invites the *opposite* error —
assuming a cited page cannot be read when it can. PDF p13, the five-components
diagram, is flagged `sparse` yet its text layer still holds *Control Unit*,
*Datapath*, *Arithmetic logic unit*, *Registers*, *Memory*, *Input*, *Output*.

**The real hazard is the letter-spacing artefact.** The deck emits one glyph per
text run, so extracted words arrive split and word-boundary greps miss them.
With the doctrine's standing rule — never transcribe an equation from a text
layer — treat extraction as a *locator*, never as a reader.

**Verified, and reusable.** The deck prints its own slide numbers bottom-right,
and every HW1 citation matches:

| PDF page | Printed slide | Content |
| ---: | ---: | --- |
| 13 | 6 | The five classic components |
| 23 | 11 | ISA includes (six items) |
| 29 | 15 | Review: computer architecture |
| 31 | 16 | Review: computer organization |
| 55 | 32 | Performance equation I |
| 86 | 49 | Amdahl's law |

The offset is **PDF page − 7 = slide number** across this deck. Do not assume it
holds for Module 02 — re-derive it, because the number of unnumbered title
slides varies.

**Check before citing:**

```sh
cd ocr_handler && uv run ocr-handler inspect \
  "../content/cesc_470/Module 01 Introduction to computer technology & ISA (1).pdf"
```

---

## HW-02 — Q10's "maximum possible" is genuinely ambiguous ⚠ two defensible answers

**Found:** HW1 Problem 10.

> *"A program spends 80% of its time performing floating-point operations. If
> floating-point performance is improved by a factor of 10, what is the maximum
> possible speedup?"*

Two readings, both grammatical, giving different numbers:

| Reading | Result |
| --- | --- |
| "What speedup results from the stated 10× improvement?" | $1/(0.2 + 0.8/10) = \mathbf{3.57\times}$ |
| "What is the ceiling on speedup from improving this part at all?" | $1/0.2 = \mathbf{5\times}$ |

The problem *supplies* a factor of 10, so **3.57× is the answer**, with the 5×
ceiling stated beside it. Answering only 5× throws away the data given;
answering only 3.57× ignores what "maximum possible" is pointing at.

**Both are on the face of the document** —
[`../hw/hw01/p10_amdahl_speedup.tex`](../hw/hw01/p10_amdahl_speedup.tex) and the
solutions sheet — so a grader never has to guess which reading was taken. That
is the general move for an ambiguous prompt: state the reading, then answer it.

---

## HW-03 — Markdown emphasis compiles silently and prints literal asterisks ⚠ **no error**

**Found:** rendering the HW1 files, 2026-09-05.

Six places had drifted into Markdown emphasis inside `.tex` prose:

```latex
instructions being *indistinguishable from data*     % p02, ×3
Both implement the **same ISA** (x86-64)             % p05, ×2
Structure it as the question asks: for **each** ISA  % p07, ×1
```

LaTeX has no such syntax. `*` is an ordinary character, so this **builds without
a single warning** and prints the asterisks:

```text
  instructions being *indis-      <- and the asterisk is hyphenated across the
  tinguishable from data*,           line break, which is worse
```

`build_tex.sh` reported `OK` for all eleven files while three of them printed
asterisks. Nothing in the toolchain looks for this.

**Grep for it before believing a build:**

```sh
grep -nE '\*\*?[A-Za-z]' content/cesc_470/hw/hw01/*.tex
```

Fixed: `*x*` → `\emph{x}`, `**x**` → `\textbf{x}`.

---

## HW-04 — Three more markup bugs that compile without a warning

**Found:** rendering the HW1 files, 2026-09-05.

**1. `\times` before punctuation is set as a *binary* operator.** TeX converts a
trailing `Bin` atom to `Ord`, so `$3.57\times$` is fine — but put anything after
it and the conversion does not happen:

```latex
= \mathbf{3.571\ldots \approx 3.57\times.}   % 3.57 × .   <- reads as unfinished
= \mathbf{3.571\ldots \approx 3.57{\times}}. % 3.57×.     <- right
```

Braces make it an ordinary symbol. Same class of bug as CESC 410's
`\angle -75^\circ` rendering as a subtraction: **the spacing is the meaning.**
Only 2 of the 30 `\times` uses in HW1 were affected — the rest end a math group.

**2. `\extref{}` with an empty argument renders `[external: ]`.** Prose that
*mentions* the macro must not *call* it:

```latex
marked with \extref{} throughout   % prints a broken-looking empty citation
marked as external throughout      % right
```

**3. `\checkmark` swallows the space after it.** It is a control word, so a
following space terminates the name instead of printing:

```latex
$\ldots = 1.00$ \checkmark --- they must sum   % "1.00 ✓— they"
$\ldots = 1.00$ \checkmark{} --- they must sum % "1.00 ✓ — they"
```

Only matters when text follows on the same line, which is why 8 of the 9 uses
needed nothing.

---

## HW-05 — A table that compiles is not a table that fits

**Found:** rendering [`../hw/hw01/p04_architecture_vs_organization.tex`](../hw/hw01/p04_architecture_vs_organization.tex), 2026-09-05.

An `{lll}` table sizes each column to its widest cell with **no upper bound**.
One long cell — *"Instruction set, registers, addressing modes"* — pushed the
table **45.7 pt past the right margin**, straight through the header rule. The
build reported `OK`.

The evidence exists, but only in the log, which `build_tex.sh` deletes:

```text
Overfull \hbox (45.74539pt too wide) in paragraph at lines 148--159
```

**Two rules follow:**

- **Any table with a sentence-length cell needs `p{}` columns, not `l`.** Fixed
  with `@{}l>{\raggedright\arraybackslash}p{5.1cm}>{\raggedright\arraybackslash}p{5.1cm}@{}`.
  (`>{...}` needs the `array` package; `longtable` in the shared preamble
  already pulls it in — verified, not assumed.)
- **Justify nothing in a narrow `p{}` column.** The solutions sheet's Q7 table
  stretched *"Decode complexity"* across a 3.9 cm cell (underfull, badness 2781)
  and hyphenated *"performance-per-watt"*. `\raggedright` fixed both.

**Harvest the warnings instead of trusting the exit code:**

```sh
cd content/cesc_470/hw/hw01/overleaf
for f in *.tex; do tectonic -o /tmp/o "$f" 2>&1 | grep -E 'Overfull|Underfull'; done
```

HW1 now reports **zero** overfull and zero underfull boxes across all eleven
documents.

---

## HW-06 — The handout has two errors of its own; neither is worth "correcting" silently

**Found:** [`../hw/hw01/HW1.pdf`](../hw/hw01/HW1.pdf), 2026-09-05.

| Handout says | Should be | Handled by |
| --- | --- | --- |
| Header: *"CEC 470 Computer Architecture"* | **CESC 470** — the syllabus uses it 14 times | `\coursename` stays `CESC 470` |
| Q8: *"Given that **Computer** requires 1.5× more cycles"* | *Computer **B*** — A's cycle count is derived, so the sentence is otherwise meaningless | Restated as "Computer B" |

Both are typos, not traps: reading them literally makes Q8 unsolvable rather
than differently-solvable. Restating is right; **doing it silently is not**.
Where a handout error changes *what is being asked*, put it on the face of the
document, the way CESC 410 does for its duplicated "Prob 1".

**Check the point total against the stated total, every time.**
$5+10+5+10+5+3+25+15+12+10 = 100$ matches the handout's "Total: 100 points" —
the one cheap check that catches a dropped problem.

---

## HW-07 — Q7 is the only problem the course materials cannot answer

**Found:** HW1 Problem 7.

Nine of the ten problems are answerable from Module 01 alone. Q7 —
*"Research and compare one advantage and one disadvantage of each…"* —
explicitly asks for outside work, and carries **25 of the 100 points**.

That makes it the only legitimate `\extref{}` on the assignment; everything else
cites the deck by PDF page and printed slide number. The split matters because
`\extref{}` renders in a different colour, so a reader sees at a glance which
claims came from the course and which did not.

**Do not import an outside convention where the course teaches one.** It is
tempting to conclude "RISC is faster", but the course's own position (PDF p31,
slide 16) is that measured performance is dominated by *organization*, not ISA.
The durable ISA-level differences are decode complexity and energy per
instruction, and [`../hw/hw01/p07_arm_vs_x86.tex`](../hw/hw01/p07_arm_vs_x86.tex) is
framed that way deliberately — see its `trap` box.

---

## HW-08 — Macros under `hw/` make a quiz impossible to scaffold — moved to course level

**Found:** working out how a `qz01/` would be set up, 2026-09-05. **Fixed the
same day.**

`new_tex.sh` resolves the macros file by walking up from the target folder
running `find <probe> -maxdepth 2 -path '*/reference_docs/*_macros.tex'`. From
`content/cesc_470/qz/qz01` the walk reaches the course root — where
`hw/reference_docs/…` sits **three** levels down, past `-maxdepth 2`. It never
sees the file and exits 1 without writing anything:

```text
error: no reference_docs/*_macros.tex found at or above content/cesc_470/qz/qz99.
       Expected content/cesc_470/reference_docs/cesc_470_macros.tex
```

This is a **hard blocker, not untidiness**: while the macros lived under `hw/`,
a quiz could not be scaffolded at all.

**The two tempting fixes are both wrong.**

- *A second macros file under `qz/reference_docs/`* makes the scaffolder work
  and earns this, correctly: `WARNING: 2 macros files for course 'cesc_470'`.
  The walk takes the **nearest** hit, so `hw/` and `qz/` would compile against
  different notation with **no error anywhere** — a silent-wrong-answer bug.
- *A symlink* avoids the divergence and does work (`realpath` resolves through
  to the real path, so the generated `\input` points at the real file), but it
  still trips that warning on every future scaffold, which trains people to
  ignore it. Tried, then reverted.

**The fix is the layout the doctrine now mandates: one macros file per COURSE.**
Notation is a property of the subject, not of the assignment kind — `\CPI` means
the same thing on a homework, a quiz, and an exam.

```text
content/cesc_470/
├── reference_docs/cesc470_macros.tex   ← ONE, shared by all kinds
├── hw/hw01/pNN_*.tex                   → ../../reference_docs/cesc470_macros.tex
└── qz/qz01/pNN_*.tex                   → ../../reference_docs/cesc470_macros.tex
```

**What the migration actually took** (2026-09-05):

1. `content/cesc_470/hw/reference_docs/` → `content/cesc_470/reference_docs/`
   (macros **and** this file).
2. All eleven HW1 sources repointed, `../reference_docs/` → `../../reference_docs/`.
   The preamble line is unchanged — it is four levels up either way.
3. `hw/.gitignore` and `qz/.gitignore` collapsed into one course-level
   [`../.gitignore`](../.gitignore).

**Verified after:** all 11 HW1 files build; all 11 flatten and compile
standalone; `new_tex.sh` scaffolds `qz99/` with **no warning**, and the result
builds, flattens and compiles with `CESC 470` in the running head — which is what
proves the macros were really loaded rather than silently absent.

CESC 470 was the last course still on the old layout; CESC 410 and CPSC 462 had
already moved.

> **Stale references left behind, in the read-only `docs/` tree** — not fixable
> from here, recorded so they are not trusted:
> `docs/latex/coursework_preamble.tex` line 15 still shows
> `\input{../reference_docs/cesc470_macros.tex}` as its example, and
> `docs/directives/documentation-discipline.md` line 25 still names
> `content/cesc_470/hw/reference_docs/`. Both should read the course-level path.

---

## HW-09 — A gitignore of negations loses source material; whitelist your own output instead

**Found:** consolidating the per-kind gitignores, 2026-09-05.

The old rule was a blanket `*.pdf` plus negations for the handouts whose names
had been guessed in advance (`!HW*.pdf`, `!hw*/HW*.pdf`). It fails the wrong way:
**any source PDF whose name was not guessed is silently untracked.** Of this
course's three source PDFs, only `HW1.pdf` matched — `cesc_470.pdf` and
`Module 01 Introduction to computer technology & ISA (1).pdf` were saved only by
living outside the `hw/` folder the rule applied to. A quiz handout called
anything but `Quiz*` or `QZ*` would have vanished.

**Invert it.** `build_tex.sh` writes `<basename>.pdf` beside each `.tex`, and
every `.tex` in an assignment folder is either `pNN_<slug>.tex` or
`<kind>NN_solutions.tex`. So two patterns describe our build products exactly:

```gitignore
p[0-9][0-9]_*.pdf
*_solutions.pdf
```

Nothing else is ignored, so **no source PDF can go missing regardless of its
name**. A stray build product appearing in `git status` is a far cheaper failure
than source material disappearing.

Verified by rule number, not by eye:

```text
IGNORED  p01_five_components.pdf     .gitignore:33:p[0-9][0-9]_*.pdf
IGNORED  hw01_solutions.pdf          .gitignore:34:*_solutions.pdf
KEPT     HW1.pdf
KEPT     cesc_470.pdf
KEPT     Module 01 Introduction to computer technology & ISA (1).pdf
KEPT     whatever-the-instructor-calls-it.pdf
```

`git check-ignore -v` names the exact rule that matched. Use it whenever a
gitignore changes; "it looks right" is not a check.

---

## HW-10 — "Flattened OK" and "compiles in Overleaf" are separate claims

**Found:** auditing the Overleaf outputs, 2026-09-05.

`flatten_tex.sh` guarantees exactly one thing: no `\input` survived. It never
builds what it wrote. So the check that matters was not being run:

```sh
docs/latex/flatten_tex.sh content/cesc_470/hw/hw01
cd content/cesc_470/hw/hw01/overleaf
for f in *.tex; do tectonic "$f" || echo "FAIL $f"; done
```

Result on 2026-09-05: **all 11 outputs compiled**, no surviving `\input`, and no
repo path or script name anywhere in the body. The only comments the flattener
adds now are bare filenames (`% ─── inlined: coursework_preamble.tex ───`),
which are content, not tooling — and a LaTeX comment never reaches the PDF in
any case.

Nothing needed fixing — but nothing had been *verified* either, and the two are
not the same state.

**Generalises past LaTeX:** a generator that validates its own output against a
weaker property than the one you care about passes forever while shipping broken
artifacts.

---

## HW-11 — The macros file is a fragment: it is *supposed* to fail a standalone build

**Found:** auditing every `.tex` in the course, 2026-09-05.

`build_tex.sh` builds **every** `.tex` in a folder it is pointed at. Pointed at
`reference_docs/`, that includes a file which is not a document:

```text
content/cesc_470/reference_docs/cesc470_macros.tex   FAIL
    error: cesc470_macros.tex:7: LaTeX Error: Command \coursename undefined.
```

**That failure is correct.** The file `\renewcommand`s `\coursename`, which the
shared preamble must have `\providecommand`ed first, and it has no
`\begin{document}`. A fragment that compiled alone would not be a fragment.

**Rule: do not "fix" a fragment by making it build.** Point `build_tex.sh` at
assignment folders (`hw/hw01`, `qz/qz01`), never at `reference_docs/`. "Every
`.tex` builds" means every *document* builds — the eleven under `hw/hw01/` — and
that is the claim to check.

---

**Related:** [`cesc470_macros.tex`](cesc470_macros.tex) ·
[`../hw/prompt.md`](../hw/prompt.md) ·
[`../hw/hw01/README.md`](../hw/hw01/README.md) ·
[`../qz/README.md`](../qz/README.md) ·
[`../../../docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md)
