# CESC 470 — Homework 1

**Fall 2026** · source: [`HW1.pdf`](HW1.pdf) · **due 9/13/2026** · **100 points**

Ten problems. Each has its own `.tex` with full step-by-step work and citations;
[`hw01_solutions.tex`](hw01_solutions.tex) is the condensed answers-only version.

```sh
cd /home/devel/electrical_notes      # every path below is relative to the repo root
docs/latex/build_tex.sh   content/cesc_470/hw/hw01           # build-check all 11
docs/latex/build_tex.sh   content/cesc_470/hw/hw01 --keep    # ...and keep the PDFs
docs/latex/flatten_tex.sh content/cesc_470/hw/hw01           # -> overleaf/ (gitignored)
```

> ### ⚠ Uploading to Overleaf? Upload from [`overleaf/`](overleaf/), never a `.tex` above.
>
> A source `.tex` in this folder **cannot** build in Overleaf and fails with
> ``LaTeX Error: File `../../../../docs/latex/coursework_preamble.tex' not found.``
> The upload-ready twin of each one sits in
> `/home/devel/electrical_notes/content/cesc_470/hw/hw01/overleaf/`, same filename.
> Full steps, including what to do when that folder is empty or stale:
> [**§ Overleaf**](#overleaf) below.

Doctrine: [`docs/directives/coursework-solutions.md`](../../../../docs/directives/coursework-solutions.md) ·
course traps: [`../../reference_docs/findings.md`](../../reference_docs/findings.md)

---

## Problems

| # | File | Pts | Topic | Status |
| --- | --- | ---: | --- | --- |
| 1 | [`p01_five_components.tex`](p01_five_components.tex) | 5 | Five classic components | ✅ |
| 2 | [`p02_von_neumann_tradeoff.tex`](p02_von_neumann_tradeoff.tex) | 10 | Stored-program advantage/disadvantage | ✅ |
| 3 | [`p03_instruction_encodings.tex`](p03_instruction_encodings.tex) | 5 | $2^{32}$ unique instructions | ✅ |
| 4 | [`p04_architecture_vs_organization.tex`](p04_architecture_vs_organization.tex) | 10 | Architecture vs organization | ✅ |
| 5 | [`p05_same_isa_different_org.tex`](p05_same_isa_different_org.tex) | 5 | Same ISA, different organizations | ✅ |
| 6 | [`p06_isa_components.tex`](p06_isa_components.tex) | 3 | Three components of an ISA | ✅ |
| 7 | [`p07_arm_vs_x86.tex`](p07_arm_vs_x86.tex) | 25 | ARM vs x86 — **research question** | ✅ |
| 8 | [`p08_target_clock_rate.tex`](p08_target_clock_rate.tex) | 15 | Target clock rate for Computer B | ✅ |
| 9 | [`p09_cpi_and_execution_time.tex`](p09_cpi_and_execution_time.tex) | 12 | Average CPI (5) + execution time (7) | ✅ |
| 10 | [`p10_amdahl_speedup.tex`](p10_amdahl_speedup.tex) | 10 | Amdahl's law | ✅ |
| | | **100** | | |

**Point total matches the handout's stated 100** — nothing missed.
$5+10+5+10+5+3+25+15+12+10 = 100$.

---

## Answers at a glance

| # | Result |
| --- | --- |
| 1 | Control unit, datapath, memory, input, output (CU + datapath = CPU) |
| 2 | $+$ reprogrammability · $-$ von Neumann bottleneck (shared memory/bus) |
| 3 | $2^{32} = 4{,}294{,}967{,}296$ |
| 4 | Architecture = *what* (ISA + organization); organization = *how* |
| 5 | Desktop vs laptop x86-64 — same binary, different clock/cache/pipeline |
| 6 | Instruction set, register set/storage, addressing modes |
| 7 | ARM: $+$ power, $-$ compatibility · x86: $+$ compatibility, $-$ decode complexity |
| 8 | **1.8 GHz** |
| 9 | (a) CPI $= 1.8$ · (b) $1.8$ ms |
| 10 | **3.57×** achieved; **5×** ceiling |

---

## Verification

**Numbers — recomputed from the handout in Python, not re-read from the `.tex`**
(2026-09-05). Every quantitative answer agreed, each by at least two independent
routes:

| # | Independent routes | Agrees |
| --- | --- | --- |
| 3 | $2^{32}$ direct; and $4 \times 1024^{3}$; range of a `uint32` | ✅ 4,294,967,296 |
| 8 | absolute cycles ($1.08{\times}10^{10} \to 1.62{\times}10^{10}$, ÷ 9 s); pure ratios ($600\ \text{MHz} \times 1.5 \times 2$); back-substitution returns exactly 9 s | ✅ 1.8 GHz |
| 9 | fractional weights; integer counts (18/10); explicit $10^{6}$-instruction mix; and via clock rate (1 GHz) | ✅ CPI 1.8, 1.8 ms |
| 10 | normalised fractions; concrete 100 s → 28 s; ceiling as the numerical $n\to\infty$ limit | ✅ 3.5714×, 5× |

Bounds held too: CPI must lie in $[1,3]$ and below 2 given the mix (1.8 does);
speedup must satisfy $1 < S < 5$ (3.57 does). The naive **1.2 GHz** for Q8 is
recorded as the trap — it ignores the $1.5\times$ cycle penalty.

**Citations — spot-checked against the deck.** The six pages carrying the load
(PDF p13, 23, 29, 31, 55, 86) were opened and matched to their printed slide
numbers (6, 11, 15, 16, 32, 49). Offset is PDF page − 7 for this deck.

**Documents — built, flattened, compiled standalone, and looked at.**

| Check | Result |
| --- | --- |
| `build_tex.sh` on all 11 `.tex` | 11/11 OK |
| `flatten_tex.sh` → `overleaf/` | 11/11, no surviving `\input` |
| `tectonic` on each of the 11 flattened copies | **11/11 compile standalone** |
| Repo paths / script names in the flattened output | none |
| `% OVERLEAF` marker block on every source `.tex` | **11/11** — and stripped from **11/11** flattened copies |
| PDFs rebuilt after the marker was added (2026-09-08) | **pixel-identical** to the pre-marker build, 11/11 — rebuilt from `git show HEAD:`, same page count, same `pdftotext` output, same `pdftoppm` page renders. (PDF *bytes* always differ: `tectonic` stamps a fresh `CreationDate` on every run, so two builds of one unedited file differ in 60 bytes.) |
| Overfull / underfull boxes | **0 / 0** |
| Pages rendered to PNG and inspected | page 1 of all 10 problem files, every page of p04/p07/p10, all 3 solutions pages |

Six layout and markup defects were found by *looking* that the build had passed
silently — Markdown asterisks printing literally, an empty `[external: ]`
citation, a table 45.7 pt past the right margin, a stretched table cell, a
dangling `×`, and a swallowed space. All fixed; none touched an answer.
Detail: [`../../reference_docs/findings.md`](../../reference_docs/findings.md).

---

## ⚠ Q10 is ambiguous — both readings are given

*"If floating-point performance is improved by a factor of 10, what is the
**maximum possible** speedup?"*

- Answering the **stated 10× improvement**: $1/(0.2 + 0.8/10) = 3.57\times$
- Answering **"maximum possible" as the ceiling**: $1/0.2 = 5\times$

Since the problem supplies a specific factor, **3.57× is the answer**, with the
5× ceiling stated alongside. Giving only 5× ignores the data provided; giving
only 3.57× misses what "maximum possible" points at. See
[`p10_amdahl_speedup.tex`](p10_amdahl_speedup.tex).

## Q7 is the only problem needing outside sources

It says *"Research and compare…"*, so the course materials are genuinely silent —
and it is worth 25 of the 100 points. External claims are marked with
`\extref{}`, which renders in a different colour so they are never confused with
lecture content. Everything else cites
[`../../Module 01 Introduction to computer technology & ISA (1).pdf`](<../../Module 01 Introduction to computer technology & ISA (1).pdf>)
by PDF page and slide number.

## Two handout typos, restated rather than reproduced

- The header reads **"CEC 470"**; the syllabus says **CESC 470** throughout.
- Q8 reads *"Given that **Computer** requires 1.5× more cycles"* — it must mean
  **Computer B**, since A's cycle count is derived from its own given time and
  clock rate. [`p08_target_clock_rate.tex`](p08_target_clock_rate.tex) states
  "Computer B".

Neither changes what is being asked, so neither is flagged on the face of the
document.

---

## Submission — **human, due 9/13/2026**

**Why human:** `Credentialed` (Canvas login) **and** `Judgment` (the syllabus fixes the
format but not the file count). Full write-up:
[`../../reference_docs/human_tasks.md`](../../reference_docs/human_tasks.md) § H1.

**Already checked, do not repeat.** The syllabus' only submission sentence is
*"All homework must be typed and converted to pdf for submission"*
([`../../cesc_470.pdf`](../../cesc_470.pdf) p5) — a format, not a count. All three pages
of [`HW1.pdf`](HW1.pdf) were rendered and searched for `submit`, `Canvas`, `upload` and
`pdf`: the only such line is `Total: 100 points   Due Date: 9/13/2026`. No code, no zip.

**WHERE.** `https://erau.instructure.com/courses/208698` → **Assignments** →
**Homework 1**. Read the *Submission Details* block and any rubric — that page overrides
the syllabus. (The course id comes from the print footer of the syllabus PDF; it has
never been opened from this machine.)

**WHAT.** Build first, then upload:

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep
```

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_470/hw/hw01/hw01_solutions.pdf` | Canvas 208698 → Assignments → Homework 1 → **Submit Assignment** |
| `/home/devel/electrical_notes/content/cesc_470/hw/hw01/p01_five_components.pdf` … `p10_amdahl_speedup.pdf` | the same upload, **only if** the Canvas page asks for per-problem files |

**VERIFY.** `ls -l /home/devel/electrical_notes/content/cesc_470/hw/hw01/*.pdf` shows
**12** files — the handout `HW1.pdf` plus the eleven build products
(`hw01_solutions.pdf`, `p01_…`–`p10_…`) freshly timestamped; and the Canvas assignment
page shows **Submitted!** with a timestamp. No timestamp means it did not go through.

**IF CANVAS DOES NOT SAY WHICH FILES.** Check Modules, then Announcements; then email
`lis14@erau.edu` or ask at MWF 11:00 in Lehman 369 — there is no TA in this course.
**Fallback if no answer arrives by 9/13:** upload **both**, solutions document first, and
say so in the submission comment. **If the widget has no "Add Another File" button** it is
a single-file assignment — upload `hw01_solutions.pdf` alone, which is the complete
assignment, and say the per-problem PDFs are available on request. ⚠ Do not wait past the
deadline for a reply — syllabus p6: 20% off within 3 days, **not accepted at all** after 3.

**BLOCKS.** Only the upload. All eleven documents are built, flattened, verified
numerically and inspected visually (§ Verification above).

---

## Overleaf

**Upload from [`overleaf/`](overleaf/) — never one of the `.tex` files in this
folder.** A source `.tex` cannot compile in Overleaf: it `\input`s the shared
preamble by a relative path that climbs above the project root, and an Overleaf
project is self-contained. Uploading one fails every time, with:

```text
LaTeX Error: File `../../../../docs/latex/coursework_preamble.tex' not found.
```

That error has now been hit twice, so every source in this folder opens with a
six-line `% OVERLEAF WILL NOT BUILD THIS FILE` comment saying so on sight, and
`flatten_tex.sh` warns about any source that lacks it.

**WHERE.** On disk:
`/home/devel/electrical_notes/content/cesc_470/hw/hw01/overleaf/` — a subfolder
of this one, holding a flattened twin of every source under the **same
filename**. In the browser: your Overleaf project → **Upload** (or **New File
→ Upload**).

**WHAT.** One document or all eleven — they are independent, and none of them
needs any other file.

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_470/hw/hw01/overleaf/hw01_solutions.tex` | Overleaf project → **Upload**, then set it as the **Main document** |
| `/home/devel/electrical_notes/content/cesc_470/hw/hw01/overleaf/p01_five_components.tex` … `p10_amdahl_speedup.tex` | the same project — only if the per-problem write-ups are wanted too |

Upload nothing else. No preamble, no `cesc470_macros.tex`, no figures: the
flattener inlined all of it.

**VERIFY.** In Overleaf, **Recompile** — a PDF appears and the log contains no
`File ... not found`. `hw01_solutions.tex` renders **3 pages**; `p01`–`p10`
render 2–3 pages each. The same check without a browser, which is what actually
proves it (run 2026-09-08, 11/11 passed):

```sh
rm -rf /tmp/ol && mkdir -p /tmp/ol
cp /home/devel/electrical_notes/content/cesc_470/hw/hw01/overleaf/*.tex /tmp/ol/
cd /tmp/ol && for f in *.tex; do timeout 180 tectonic "$f" || echo "FAILED: $f"; done
```

Expected: eleven PDFs, no `FAILED` line. `/tmp/ol` sits outside the repo and has
no route to the shared preamble, so whatever compiles there compiles in Overleaf.

**IF `overleaf/` IS EMPTY, MISSING, OR STALE.** It is **gitignored and fully
regenerable** — a fresh clone will not have it, and that is not a fault. Rebuild
it from the repo root:

```sh
cd /home/devel/electrical_notes
docs/latex/flatten_tex.sh content/cesc_470/hw/hw01
```

Expected: eleven `->` rows, then `Self-contained copies in:
content/cesc_470/hw/hw01/overleaf`, with no `FAIL` and no `WARN`. A `FAIL` row
means an `\input` survived — do not upload that file; fix the source and re-run.

Staleness is the quieter risk (edit a source, forget to re-flatten, upload
yesterday's answers). Check before every upload:

```sh
cd /home/devel/electrical_notes/content/cesc_470/hw/hw01
for f in *.tex; do [ "overleaf/$f" -nt "$f" ] || echo "STALE: $f"; done
```

Silence means every twin is newer than its source. Any `STALE:` line — or a
missing twin, which also prints `STALE:` — means re-flatten before uploading.

**Edit the source, never the copy.** `overleaf/*.tex` is generated output,
overwritten wholesale on the next `flatten_tex.sh` run. An edit made there is
lost silently and never reaches the graded PDF.

**BLOCKS.** Overleaf only. The Canvas submission above uses the locally built
PDFs and never touches `overleaf/`; `build_tex.sh`, the answers, and every check
in § Verification work without that folder existing.
