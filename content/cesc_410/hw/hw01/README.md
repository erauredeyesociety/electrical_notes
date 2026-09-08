# HW1 — Basic signals/systems and convolution

**Fall 2026** · source: `dsphw26-hw1.pdf` · **130 pts total**

Six problems. Each has its own `.tex` with full step-by-step work;
[`hw01_solutions.tex`](hw01_solutions.tex) is the condensed answers-only version.

> ### ⚠ Going to Overleaf? Upload `overleaf/<same-name>.tex`, not the file beside this README.
> The seven `.tex` files here **cannot** compile on Overleaf — they `\input` the shared preamble
> from above the project root. Upload the flattened twin in
> `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/` instead.
> Full instructions: [**Overleaf**](#overleaf) below.

```sh
cd /home/devel/electrical_notes                            # the shared tooling takes repo-relative paths
docs/latex/build_tex.sh  content/cesc_410/hw/hw01           # build-check everything (PDFs deleted after)
docs/latex/build_tex.sh  content/cesc_410/hw/hw01 --keep    # ...and keep the PDFs
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01          # self-contained Overleaf copies
```

All seven files build, and all seven flatten to `hw01/overleaf/` and compile
standalone from there — verified by running `tectonic` on each flattened copy,
not just by flattening successfully. `overleaf/` is gitignored and regenerable, so a fresh clone
has none until `flatten_tex.sh` is run — see [**Overleaf**](#overleaf).

The course-local copy still works — `cd /home/devel/electrical_notes/content/cesc_410/hw &&
tools/build_tex.sh hw01`, paths relative to that folder — but the shared checker above is the one
to use.

---

## Problems

| # | File | LO | Pts | Topic | Status |
| --- | --- | --- | ---: | --- | --- |
| 1 | [`p01_phasor_form.tex`](p01_phasor_form.tex) | LO01 | 20 | Phasor form of 4 voltage sources | ✅ |
| 2 | [`p02_phasor_arithmetic.tex`](p02_phasor_arithmetic.tex) | LO01 | 10 | Sum/difference via phasors | ✅ |
| 3 | [`p03_signal_transformations.tex`](p03_signal_transformations.tex) | LO02 | 20 | Plot $x[n]$, $x[n-2]$, $x[-n]$, $x[2-n]$ | ✅ |
| 4 | [`p04_periodicity.tex`](p04_periodicity.tex) | LO03 | 20 | Periodicity + fundamental period ×4 | ✅ |
| 5 | [`p05_system_properties.tex`](p05_system_properties.tex) | LO04 | 40 | Linear/TI/causal/BIBO for 5 systems | ✅ |
| 6 | [`p06_convolution.tex`](p06_convolution.tex) | LO05 | 20 | $a^n u[n] \ast a^n u[n]$ by flip-slide-sum | ✅ |
| | | | **130** | | |

Point total matches the handout's stated 130 — nothing missed.

---

## ⚠ Two transcription traps in this handout

**1. The handout numbers the last problem "Prob 1" a second time.** There is no
Prob 6 in the PDF; the convolution problem is labelled Prob 1 (LO05). Files use a
continuous index (`p06_`) so they sort correctly, and both `p06` and the
solutions document note the discrepancy on their face.

**2. `pdftotext` flattens fractions and misreads two problems.** Verified against
the rendered page at 400 dpi, not the text layer:

| `pdftotext` says | Actually is | Why it matters |
| --- | --- | --- |
| `cos( 6π n)` | $\cos\!\big(\tfrac{\pi}{6}n\big)$ | $\cos(6\pi n) = 1$ for all integer $n$ — a constant, not a signal |
| `e^{j(πn/ 8)}` with a stray `√` | $e^{j(\pi n/\sqrt{8})}$ | The $\sqrt{\ }$ is the whole point of part 4: it makes the signal **aperiodic** |

**Do not trust `tools/course_text.py --grep` for equations in this handout.** It
reads the same broken text layer. Render the region and look at it.

---

## Answers at a glance

| # | Result |
| --- | --- |
| 1 | $10\angle-75°$, $15\angle15°$, $12\angle75°$, $8\angle165°$ |
| 2 | $5\sqrt{13}\angle-18.69°$ ; $3\sqrt{21}\angle-34.11°$ |
| 3 | Samples $\{1,\ 0.866,\ 0.5,\ 0\}$ relocated to supports $[0,3]$, $[2,5]$, $[-3,0]$, $[-1,2]$ |
| 4 | Periodic $N_0=16$ ; periodic $N_0=18$ ; **not** periodic ; **not** periodic |
| 5 | Only $T_a$ is BIBO-unstable; only $T_c$, $T_d$ are non-causal |
| 6 | $y[n] = (n+1)a^n u[n]$ |

## Verification

Every numeric answer was checked computationally, not just re-derived:

- **P1** — each phasor reconstructed and compared to the original over a full
  $\omega t$ sweep: max error $\approx 10^{-14}$.
- **P2** — magnitudes confirmed exact ($\sqrt{325} = 5\sqrt{13}$,
  $\sqrt{189} = 3\sqrt{21}$) by two independent routes: component arithmetic, and
  geometry (the phasors are $90°$ apart in part 1; law of cosines in part 2).
- **P4** — brute-force search for $N \le 10{,}000$ satisfying
  $\omega_0 N = 2\pi k$: found 16 and 18, found none for part 4.
- **P6** — `np.convolve` vs $(n+1)a^n$ for $a = 0.5,\ 2.0,\ -0.7$ over $n < 40$:
  max error $0$, $0$, and $1.1\times10^{-16}$.

---

<a id="overleaf"></a>

## ⚠ Overleaf — upload the flattened copy, never the source

*Why human: `Credentialed` (Overleaf login) + `GUI-only`. Everything up to the upload is done.*

**This has now failed twice**, both times by opening the obvious file and uploading it:

```text
LaTeX Error: File `../../../../docs/latex/coursework_preamble.tex' not found.
./main.tex, 1
```

Nothing is broken when that happens. Every source in this folder `\input`s the shared preamble by a
relative path that climbs four levels above the assignment folder — correct here, impossible on
Overleaf, where a project is self-contained and cannot see above its own root. The flattened copies
have that preamble inlined and contain no `\input` at all.

**WHERE.** `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/` — the same seven
filenames as the sources, one directory deeper. Every source also says so in a comment on its first
line, so the file itself warns you before you upload it.

**WHAT.** One file per Overleaf project; each flattened copy is standalone and needs no other file.

| Source (FROM) — do **not** upload | Upload this instead (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/hw01_solutions.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/hw01_solutions.tex` |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/p01_phasor_form.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/p01_phasor_form.tex` |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/p02_phasor_arithmetic.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/p02_phasor_arithmetic.tex` |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/p03_signal_transformations.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/p03_signal_transformations.tex` |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/p04_periodicity.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/p04_periodicity.tex` |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/p05_system_properties.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/p05_system_properties.tex` |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/p06_convolution.tex` | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf/p06_convolution.tex` |

In Overleaf: **New Project → Blank Project**, then **Upload** the file — or paste its contents over
the whole of `main.tex`. If you upload it under its own name, right-click it in the file tree and
choose **Set as Main Document**, or Overleaf keeps compiling the empty `main.tex` it created.

**VERIFY.** Prove it locally *before* uploading — the same compile Overleaf will run:

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf
tectonic hw01_solutions.tex                              # or any of the seven
grep -cE '^[[:space:]]*\\(input|include)\{' hw01_solutions.tex
```

Expected: tectonic ends with ``note: Writing `hw01_solutions.pdf` (53.9 KiB)`` and no `not found`
anywhere; the `grep -cE` prints `0` (the same source counts `2`). Match the pattern exactly — a
plain `grep -c '\input'` prints `1` even on a good copy, because the generated header line
*mentions* `\input` in prose. In Overleaf itself: the PDF renders and the log contains no
`File ... not found`. If that error appears in the log, the source went up instead of the flattened copy.

**IF `overleaf/` IS EMPTY, MISSING, OR OLDER THAN THE SOURCES.** Expected, not a fault —
`overleaf/` is gitignored (`content/cesc_410/hw/.gitignore`), so it exists only where it was last
generated and never in a fresh clone. Regenerate it; it is idempotent and takes about a second:

```sh
cd /home/devel/electrical_notes
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
```

Expected: seven `-> content/cesc_410/hw/hw01/overleaf/... (N KB)` lines, then
`Self-contained copies in: ...`. Two failure modes worth knowing:

- `FAIL <file> -- unresolved \input remains` — the copy is **not** safe to upload. A path in the
  source did not resolve; fix it there and rerun. The script refuses to ship a broken copy.
- `WARN <file> -- source has \input but no OVERLEAF marker comment` — the source lost its
  first-line warning. Put it back; that comment is the only thing standing between the next reader
  and this error.

Staleness cannot be seen by eye. **If any source changed since the last run, rerun the command** —
re-flattening a current folder costs a second and changes nothing. And `overleaf/` is generated
output: edit the source, never the copy, or the next run silently discards your edit.

**BLOCKS.** The Overleaf route only. The graded PDF below is built locally with `tectonic` and
never touches Overleaf.

---

## Submission

**Due Wed 9/9/26** (course info § 9 schedule; time of day unconfirmed — assume
*before the 4:00 pm class*). **Late is a zero and there is no makeup.**

Overleaf is **not** part of this; the file below is built locally. If you are editing on Overleaf
anyway, upload only the flattened copies — [**Overleaf**](#overleaf), just above.

| | |
| --- | --- |
| **What goes in** | The six per-problem PDFs, merged — **not** `hw01_solutions.pdf`. § 8.6 requires *"all necessary intermediate steps"* |
| **Format** | PDF only, US Letter, 1-inch margins — all three satisfied by the build, measured not assumed |
| **Code / zip** | None in this assignment. Verified against the handout |
| **File** | `/home/devel/electrical_notes/content/cesc_410/hw/hw01/hw01-nelson-gatlin.pdf` — 15 pages |
| **Still unconfirmed** | *Where* it is uploaded, and whether one combined PDF or six separate ones |

Build it in two steps. **They run from different directories, so both `cd`s are here** — pasting
the merge at the repo root gives `I/O Error: Couldn't open file 'p01_phasor_form.pdf'`. And
`--keep` is required: without it the build deletes the PDFs it just made.

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_410/hw/hw01 --keep
```

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01
pdfunite p01_phasor_form.pdf p02_phasor_arithmetic.pdf p03_signal_transformations.pdf \
         p04_periodicity.pdf p05_system_properties.pdf p06_convolution.pdf \
         hw01-nelson-gatlin.pdf
pdfinfo hw01-nelson-gatlin.pdf | grep -E '^(Pages|Page size)'   # expect 15, letter
```

The file list is written out rather than globbed on purpose: `p0*.pdf` happens to sort correctly
today and stops doing so at `p10`.

**Before uploading, do the two human steps** — the AI-use disclosure that
§ 11.1 requires, and finding the submission point. Both are written out with
WHERE / WHAT / VERIFY / IF ABSENT / BLOCKS in
[`../reference_docs/submission.md`](../reference_docs/submission.md#human-tasks);
the index is [Human-only](../prompt.md#human-only).
