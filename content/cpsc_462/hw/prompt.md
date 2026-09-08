# Claude entry point — CPSC 462

**Trigger:** *"`hwNN/` (or `qzNN/`, `examNN/`) now exists with the assignment in
it, work it."*

**Read [`docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md) first.**
That is the doctrine — the two-document rule, the citation rule, the verification
rule, the per-assignment checklist. Shared by every course under the doctrine and
not repeated here.

**Before writing anything that starts "the human needs to…", read
[`docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md)**
— classify the task and give it a reason, absolute paths, and all five of
WHERE / WHAT / VERIFY / IF-ABSENT / BLOCKS. This course's live hand-offs, with the
instructor's office hours, the capture interfaces on this machine and the searches
already done, are in
[`../reference_docs/human_tasks.md`](../reference_docs/human_tasks.md).

**Tooling you already have — do not rebuild it.** The shared LaTeX toolchain (`new_tex.sh` to scaffold a problem file with the `\input` depth computed, `build_tex.sh` to build-check, `flatten_tex.sh` to produce the Overleaf copy **and `--check` that it is still current**) is listed with worked commands in [`../reference_docs/shared_tools.md`](../reference_docs/shared_tools.md). It is bash under `docs/latex/`, shared by every course.

This file carries **only what is specific to CPSC 462.**

> **Nothing has been assigned yet.** This is scaffolding. It was proved end to
> end on 2026-09-05 with throwaway `hw99/`, `qz99/` and `exam99/` folders —
> scaffolded, built, flattened, and every flattened file compiled standalone
> with `tectonic` — then deleted. The first assignment can be worked immediately.

---

## The course

**Computer Networks** · Fall 2026 · currently working through **Wireshark**.

Syllabus: [`../class_materials/CS 462 Syllabus_Fall26.pdf`](<../class_materials/CS 462 Syllabus_Fall26.pdf>)
→ extracted at [`../md_notes/cs_462_syllabus_fall26.md`](../md_notes/cs_462_syllabus_fall26.md)

Three graded written kinds, all under the same doctrine:

| Kind | Folder | Weight | Notes |
| --- | --- | --- | --- |
| Assignments | `hw/hwNN/` | 30% | the instructor calls them **"Hands on"** and **"Lab N"** — don't expect a file named `HW1.pdf` |
| Quizzes | [`../qz/qzNN/`](../qz/README.md) | 10% | named by **topic**, not numbered — record which topic in the folder's `README.md` |
| Examinations | [`../exam/examNN/`](../exam/README.md) | 30% | Exam 1 9/30/26, Exam 2 11/6/26; each covers material since the previous exam |

There is also a Final Report (20%) and Class Participation (10%).

---

## Layout — the macros live at course level

```text
content/cpsc_462/
├── reference_docs/       ← cpsc462_macros.tex + findings.md — ONE copy, shared
├── hw/    prompt.md   hwNN/
├── qz/    qzNN/
├── exam/  examNN/
├── class_materials/      source PDF / DOCX / PPTX
├── md_notes/             Markdown extraction of the above — cite THIS
├── tools/                extract_notes.py, check_links.py
└── .gitignore            ONE file, course-wide
```

**Do not put a second `*_macros.tex` anywhere under this course.** `new_tex.sh`
walks up from the assignment folder and takes the *nearest* match, so a second
file would let `hw/` and `qz/` silently compile against different notation. The
reasoning, and why the file is not under `hw/`, is in
[`../reference_docs/findings.md`](../reference_docs/findings.md) §1.

---

## What to cite

**Cite [`../md_notes/`](../md_notes/), not `../class_materials/`.** The notes are
extracted from the source `.docx`/`.pdf` by
[`../tools/extract_notes.py`](../tools/extract_notes.py) and keep headings and
figures; citing them means the citation is greppable.

| Notes | Source | Quality |
| --- | --- | --- |
| [`introduction_to_wireshark.md`](../md_notes/introduction_to_wireshark.md) | `.docx` | ✅ full, 8 figures |
| [`application_layer.md`](../md_notes/application_layer.md) | 106-slide PDF | ✅ 453 ch/slide |
| [`cs_462_syllabus_fall26.md`](../md_notes/cs_462_syllabus_fall26.md) | `.docx` | ✅ full |
| [`introduction_cpsc_462.md`](../md_notes/introduction_cpsc_462.md) | 85-slide PDF | ⚠ 396 ch/slide — picture-heavy |
| [`intro_and_syllabus.md`](../md_notes/intro_and_syllabus.md) | 6-slide PDF | ⚠ 99 ch/slide — almost all images |

The two ⚠ decks carry little text. **Open the original PDF for their diagrams**
rather than citing a page you have not seen — the delay slides are in the
picture-heavy one.

**For these two decks the PDF page and the printed slide number agree** (footer
reads `Introduction: 1-N` / `Application Layer: 2-N`), unlike the doctrine's
usual warning. Verified over every page; re-check it for each new deck.

Re-extract after new material lands:

```sh
content/cpsc_462/tools/extract_notes.py          # rebuild what is out of date
content/cpsc_462/tools/extract_notes.py --list   # show the plan, change nothing
```

---

## Macros

Shared preamble plus
[`../reference_docs/cpsc462_macros.tex`](../reference_docs/cpsc462_macros.tex):

| Macro | For | Evidence |
| --- | --- | --- |
| `\dnodal` `\dproc` `\dqueue` `\dtrans` `\dprop` | the four delay components and their sum | `Introduction CPSC 462.pdf` p50–51 |
| `\RTT` | round-trip time, used as a coefficient (`2\RTT`) | `Application Layer.pdf` p29 |
| `\Mbps` | link rate the way the slides write it, `Mb/s` | `Introduction CPSC 462.pdf` p33 |
| `\field{TTL}` | a header field or a Wireshark display filter | `introduction_to_wireshark.md` |

Kept deliberately small — **add a macro when a second problem needs the same
notation, not in anticipation.** `\kbps` and `\ms` were removed on 2026-09-05 for
want of a user; see [`../reference_docs/findings.md`](../reference_docs/findings.md) §3
for what was considered and rejected.

**Units:** siunitx is already loaded by the shared preamble, so write
`\SI{0.1}{\milli\second}`. Only hand-roll a unit macro where siunitx's output
disagrees with the course's own notation — which is why `\Mbps` exists and `\ms`
does not.

**Watch the overloaded `d`:** on p51 it is both the delay symbol (`\dprop`) and
the physical link length (`\dprop = d/s`). The course does this; be explicit
rather than inventing a different symbol.

CPSC 462 assignments are not known to state learning outcomes, so use the
three-argument `\problemheader{n}{pts}{title}`. Switch to `\problemheaderlo` if
an assignment does state them.

---

## Watch for

**This course ships packet captures and hands-on labs**, unlike the pure-paper
courses. A `.pcapng` referenced by a solution is source material, not a build
product: keep it beside the solution. [`../.gitignore`](../.gitignore) already
tracks it — the ignore rules name *our* build products (`pNN_*.pdf`,
`*_solutions.pdf`, `overleaf/`, LaTeX intermediates) rather than blanket-ignoring
`*.pdf`, so an instructor handout with an unguessable name is kept by default.

Verify any ignore change with `git check-ignore -v <path>`, never by eye.

### The capture is not a human task — only reading it is

A Wireshark lab *looks* like one indivisible GUI job. It is two, and only the second
needs a person. **Do not hand the whole thing over.**

`dumpcap` — the capture engine Wireshark itself drives — is installed here with
`cap_net_admin,cap_net_raw=eip`, and this account is in group `wireshark`, so a capture
runs **headless and without `sudo`**:

```sh
cd /home/devel/electrical_notes
mkdir -p content/cpsc_462/hw/hw01          # dumpcap will NOT create it; -w fails without this
ip route get 128.119.245.12                # gaia — whatever it prints after `dev` is the -i
dumpcap -i wlo1 -f "host gaia.cs.umass.edu" -a duration:30 \
        -w content/cpsc_462/hw/hw01/intro_http.pcapng
capinfos content/cpsc_462/hw/hw01/intro_http.pcapng     # packets, duration, encapsulation
```

The `-f` is a **capture** filter (BPF), not a display filter, and it is not optional:
an unfiltered capture on `wlo1` records everyone else's traffic too.

What genuinely needs a human is the *view* — the expanded HTTP tree, the Dest Port
field, the screenshots. That half, and the two traps that make a good capture look
empty (the browser's silent HTTPS upgrade; a live VPN putting the traffic on `tun0`),
are in [`../reference_docs/human_tasks.md`](../reference_docs/human_tasks.md) § H3.

⚠ **`tshark` is not installed on this machine** (`dumpcap`, `capinfos`, `editcap` are).
So packets can be recorded and summarised here, but not decoded — which is why the
analysis half is currently human at all. `sudo apt install tshark` retires it.

---

## Overleaf

**Never paste a source file into Overleaf** — its relative `\input` climbs above
the project root and cannot resolve there. Flatten first:

```sh
docs/latex/flatten_tex.sh content/cpsc_462/hw/hw01
#   -> content/cpsc_462/hw/hw01/overleaf/*.tex   (self-contained, gitignored)
```

Scaffold new files rather than hand-writing the `\input` lines. `new_tex.sh`
computes both the `../` depth and the macros path, for any of the three kinds:

```sh
mkdir -p content/cpsc_462/hw/hw01
docs/latex/new_tex.sh content/cpsc_462/hw/hw01 3 some-slug --pts "10 pts"
docs/latex/new_tex.sh content/cpsc_462/hw/hw01 --solutions
docs/latex/build_tex.sh content/cpsc_462/hw/hw01
```

Detail: [`docs/latex/INDEX.md`](../../../docs/latex/INDEX.md)

---

## Before handing anything back

```sh
docs/latex/build_tex.sh content/cpsc_462/<kind>/<kind>NN     # every file builds
docs/latex/flatten_tex.sh content/cpsc_462/<kind>/<kind>NN   # Overleaf copies
content/cpsc_462/tools/check_links.py                        # every link resolves
```

A build that succeeds is not a document that is correct — render at least one
page to PNG and look at it. `check_links.py` also flags a Markdown link whose
target contains a space or parenthesis but is not wrapped in angle brackets;
several class-materials filenames contain spaces, so write
`[x](<../class_materials/CS 462 Syllabus_Fall26.pdf>)`.

---

## Human-only

**The full register, written to the standard, is
[`../reference_docs/human_tasks.md`](../reference_docs/human_tasks.md)** — every task
there names a reason, a place, a check, a fallback and what it blocks. This is the
index, not a second copy.

| # | Task | Why human | Where it happens |
| --- | --- | --- | --- |
| H1 | Fetch the "Hands on" / "Lab N" handout when one is assigned | `Credentialed` — and **never search for `HW`**; this instructor's handouts are named by topic | Canvas → Assignments / Modules / Files |
| H2 | **Find the Canvas course id** and record it | `Credentialed` — the syllabus is a `.docx` and leaks no URL, so nothing on disk knows it | `erau.instructure.com` → Dashboard → the CS 462 card |
| H3b | Read the capture in the Wireshark window and answer from it | `Capture` — the recording half (H3a) is automatable and must be done first | the GUI, on a `.pcapng` `dumpcap` already produced |
| H4 | Screenshots for the report | `Capture` | the same window |
| H5 | `sudo apt install tshark` | `Policy` — needs root; retires the whole `Capture` class above | any terminal |
| H6 | Confirm the submission form for the first assignment | `Credentialed` + `Judgment` — the syllabus never says what to submit, not even a file type | Canvas → the Hands-on item |
| H7 | Record which topic each `qzNN` is | `Judgment` — quizzes are named, not numbered | `qzNN/README.md` |

Plus everything in the directive's own Human-only table, and **all git mutations**.

**Not human, though it looks it:** running the packet capture (H3a — headless `dumpcap`,
no `sudo`), and checking that a `.pcapng` or an oddly-named handout survives
`.gitignore` (verified 2026-09-08). Do not hand either over.

**No TA exists in this course** — the syllabus prints a TA block with four empty fields.
The instructor is the only route: `sultanr1@erau.edu`, LB 355. ⚠ Use the **1–2pm** office
hour, not the 11am one: CESC 470 meets MWF 11:00–11:50 and conflicts with it.
