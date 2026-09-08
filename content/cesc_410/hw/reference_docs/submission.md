# What each homework requires

> **Most of this used to say "unconfirmed."** It is not: the rules were on disk the whole time, in
> [`../../senior_design/cesc410-course-info-fall2026.pdf`](../../senior_design/cesc410-course-info-fall2026.pdf)
> § 8.6 *Submission of Work* and § 11 *Class Policies*. Everything below marked **CONFIRMED** is
> quoted from that PDF. Everything marked **UNKNOWN** genuinely is not written down anywhere we
> hold, and each one comes with the exact sentence to ask, the person to ask, and what we did in
> the meantime.

Human tasks in this file follow
[`../../../../docs/directives/human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md):
every one states **WHERE, WHAT, VERIFY, IF ABSENT, BLOCKS**.

---

## CONFIRMED — quoted from the course-info PDF

The lecture course governs, not CESC 410L. The two documents have **different** submission rules and
the lab one does not apply here. CESC 510's § 8.7 is byte-identical to CESC 410's § 8.6, so the rule
holds whichever section the roster says.

| Question | Answer | Source |
| --- | --- | --- |
| What file format? | **PDF only.** *"For electronic submission, please submit PDF only except otherwise specified."* | 410 info § 8.6 |
| Paper size and margins? | **US Letter, 1-inch margins.** *"All work turned in for grading must be done neatly and professionally on Letter-sized paper, leaving 1-inch margins for making copy and binding."* | 410 info § 8.6 |
| Working, or answers only? | **The working.** *"Use correct approach and show all necessary intermediate steps."* Also *"Draw neat, clearly labeled sketches as necessary; all the variables used must be clearly defined."* | 410 info § 8.6 |
| Handwritten or typeset? | **Either — electronic is explicitly contemplated.** § 8.6 names "electronic submission"; § 11.3 says HW *"can be submitted online."* Nothing requires paper. | 410 info § 8.6, § 11.3 |
| Submitted on paper or online? | **Online.** *"No makeups for missing bi-weekly HW as they can be submitted online."* | 410 info § 11.3 |
| Late work? | **Not accepted, ever.** *"Submitting work on time... No late submission is accepted."* | 410 info § 8.6 |
| Does HW ever include code? | **Yes, sometimes.** *"There will be (roughly) bi-weekly homework assignments, which may include programming assignments."* Do not assume "no code" — check each handout. | 410 info § 8.1 |
| If it does include code, what style? | **1TBS, 4-space indentation**, typed neatly. The PDF prints a worked `int abs(int x)` example. | 410 info § 8.6 |
| Must AI use be disclosed? | **Yes.** *"If you use AI tools for your assignment, you should clearly indicate it."* See [H3](#h3--decide-and-place-the-ai-use-disclosure--why-human-judgment) — this is not optional and it is not currently in any `.tex`. | 410 info § 11.1 |
| What is HW worth? | **15 of 100 course points**, across ten assignments — roughly **1.5 points each**. | 410 info § 10 |
| Group work? | Discussion encouraged, *"each student should write their solutions independently."* | 410 info § 8.3, § 8.6 |

### What this settles about our two documents

The [two-document rule](hw_workflow.md#two-documents-different-jobs) is unchanged, but which one is
the **deliverable** is now decided:

| Document | Role | Submitted? |
| --- | --- | --- |
| `hwNN/pNN_<slug>.tex` → PDF | every intermediate step | ✅ **this is the submission** — § 8.6 demands the steps |
| `hwNN/hwNN_solutions.tex` → PDF | answers only | ❌ **internal.** A grader asked for steps; an answers-only sheet under-delivers |

`hw01_solutions.pdf` stays useful for checking your own work and for revising before a quiz. It is
not what goes to the instructor unless [Q1](#still-unknown--and-exactly-how-to-ask) comes back saying
otherwise.

---

## Deadlines — from § 9 Class Schedule

| HW | Released | **Due** | Same-day event |
| --- | --- | --- | --- |
| 1 | Mon 8/31/26 | **Wed 9/9/26** | Lctr 6; HW 2 released |
| 2 | Wed 9/9/26 | Fri 9/18/26 | Lctr 9; HW 3 released |
| 3 | Fri 9/18/26 | Fri 9/25/26 | Lctr 12; HW 4 released |
| 4 | Fri 9/25/26 | Mon 10/5/26 | Lctr 15; HW 5 released |
| 5 | Mon 10/5/26 | Mon 10/12/26 | Lctr 18; HW 6 released |
| 6 | Mon 10/12/26 | Fri 10/23/26 | Lctr 21; HW 7 released |
| 7 | Fri 10/23/26 | Fri 10/30/26 | Lctr 24; HW 8 released |
| 8 | Fri 10/30/26 | Mon 11/9/26 | Lctr 27; HW 9 released |
| 9 | Mon 11/9/26 | Mon 11/16/26 | Lctr 30; HW 10 released |
| 10 | Mon 11/16/26 | Mon 11/30/26 | Lctr 33 |

⚠ **Treat the schedule as the plan, not the deadline.** Two reasons, both checked:

1. **It has already slipped.** The schedule says HW 1 was released Mon 8/31. The handout's own PDF
   metadata says it was made **Thu 2026-09-03 20:41 EDT** — three days later.
   `pdfinfo /home/devel/electrical_notes/content/cesc_410/hw/hw01/dsphw26-hw1.pdf` shows it.
2. **Two rows of the schedule are internally wrong.** The 11/23 row says *"HW 6 due"*, but HW 6 is
   already due 10/23; and § 8.5 says the final covers *"everything covered in the entire semester,
   including HW 13"* while the schedule lists only HW 1–10. Neither affects HW 1 — both are worth
   one sentence when you next email ([Q5](#still-unknown--and-exactly-how-to-ask)).

**No time of day is stated anywhere.** Class is MWF 4:00–4:50 pm; the safe reading is *before class
on the due date*, not *end of day*. Confirm it — [Q2](#still-unknown--and-exactly-how-to-ask).

---

## Still UNKNOWN — and exactly how to ask

Four things are not written down in any document we hold. Verified negatives, not guesses:

- The **CESC 410 course-info PDF contains the word "Canvas" zero times.** Checked:
  `pdftotext -layout cesc410-course-info-fall2026.pdf - | grep -ci canvas` → `0`.
- The **HW 1 handout says nothing about submission at all.** Checked:
  `pdftotext -layout dsphw26-hw1.pdf - | grep -iE 'submit|due|name|upload|canvas|pdf'` → no output.
  It is six problems and nothing else.
- The **only Canvas pointer in any course document we hold** is CESC 410L § 6 — *"Lab handouts are
  posted on the **CESC 510** Canvas site."* CESC 510 is the co-listed graduate section: same
  instructor, same room (CoAS 203), same MWF 4:00 pm slot, and the HW 1 handout is titled
  **"CESC 410/510 HW 1"**. So the shared Canvas site is plausibly where HW goes too — **plausibly is
  not confirmed**, and it is the first place to look before asking.

| # | Ask this, close to verbatim | Ask whom | What we assumed meanwhile | What changes if the answer differs |
| --- | --- | --- | --- | --- |
| **Q1** | "For HW 1, should I upload one combined PDF with all six problems, or a separate PDF per problem?" | Dr. Liu — [contact below](#who-to-ask-and-when) | **One combined PDF.** Built and verified: 15 pages, letter, `hw01-nelson-gatlin.pdf` | Nothing is rebuilt. The six per-problem PDFs already exist side by side; you upload those instead of the merged one. Zero extra work either way — which is why we did not wait for the answer |
| **Q2** | "Is HW 1 due at the start of class on Wednesday 9/9, or at the end of that day?" | Dr. Liu | **Before class, 4:00 pm Wed 9/9.** The strictest reading, and late is a zero | If it is end-of-day you gained eight hours. If it were earlier you would already have missed it — which is why the strict reading is the assumption |
| **Q3** | "Where do I submit homework — is it the CESC 510 Canvas site that the lab handouts are on, or a separate CESC 410 site?" | Dr. Liu, or a classmate who has already submitted | **The CESC 510 Canvas site**, because 410L § 6 names it and the handout is titled "CESC 410/510" | Only the destination changes; the PDF is identical. A classmate answers this faster than the instructor and it costs them nothing |
| **Q4** | "Is there a required cover sheet or file-naming convention for homework submissions?" | Dr. Liu | **No cover sheet.** Each problem PDF carries course, HW number, problem number, LO and points in its `\problemheaderlo` header; the file is named `hw01-nelson-gatlin.pdf` | A cover sheet is one `.tex` page and ten minutes. A naming convention is a `mv`. Neither touches the solutions |
| **Q5** | "The schedule shows HW 6 due twice (10/23 and 11/23), and § 8.5 mentions HW 13 though the schedule stops at HW 10 — which is right?" | Dr. Liu, whenever convenient | **The 10/23 date for HW 6; ten assignments total.** Nothing depends on this yet | Only the [deadline table](#deadlines--from--9-class-schedule) above changes. Ask it as a rider on Q1–Q4, not as its own email |

**Do not invent an answer to any of these.** Every one is a "we assumed X, and X is cheap to undo"
— that is what makes shipping without the answer safe. If an assumption ever becomes expensive to
undo, it stops being an assumption and becomes a blocker.

---

## Who to ask, and when

From § 1 of the course-info PDF. This is the whole reason "ask the instructor" is a usable
instruction rather than a shrug:

| | |
| --- | --- |
| **Instructor** | Dr. Jianhua Liu, Associate Professor of Electrical and Computer Engineering |
| **Email** | `jianhua.liu@erau.edu` — alternate `liu620@erau.edu` |
| **Office** | LB 349 |
| **Office hours** | **MWF 1:30 pm – 3:50 pm**, or by appointment on Zoom |
| **Phone** | 226-7713 (work) |
| **Class** | MWF 4:00–4:50 pm, CoAS 203 — the ten minutes before class is the other reliable window |
| **Canvas** | Host **`https://erau.instructure.com`** (confirmed). **Course id: NOT RECORDED — fill this in.** Overwrite this cell with `https://erau.instructure.com/courses/<NNNNNN>` the first time you open the CESC 410 (or 510) site; the whole of [H1](#h1--confirm-where-homework-is-submitted-and-submit-it--why-human-credentialed) is vague until you do |
| **TAs** | **No route yet.** § 1 lists TAs' office hours as **"TBD"**, and no TA is named. For homework, the instructor is the only address. (The *lab* TAs are a separate matter — see [`../../labs_and_projects/reference_docs/submission_requirements.md`](../../labs_and_projects/reference_docs/submission_requirements.md).) |

**Timing note, and it matters.** Office hours are **M/W/F**. There are none on a Tuesday. If it is
a Tuesday and HW is due Wednesday, email is the only route that arrives in time — send it rather
than planning to catch him in person.

---

## Human tasks

### H1 · Confirm where homework is submitted, and submit it · Why human: Credentialed

**Already tried — do not repeat:**

- Every instructor PDF we hold, counted for the word:

  ```sh
  cd /home/devel/electrical_notes/content/cesc_410
  for f in senior_design/*.pdf hw/hw01/dsphw26-hw1.pdf; do
    printf '%-52s canvas=%s\n' "$f" "$(pdftotext -layout "$f" - | grep -ci canvas)"
  done
  ```

  ```text
  senior_design/cecs510-and-senior-design-projects.pdf canvas=0
  senior_design/cesc410-course-info-fall2026.pdf       canvas=0
  senior_design/cesc410L-course-info-fall2026.pdf      canvas=1
  senior_design/cesc510-course-info-fall2026.pdf       canvas=0
  hw/hw01/dsphw26-hw1.pdf                              canvas=0
  ```

  **One hit in five documents**, and it is the lab course's § 6 quoted above. Nothing anywhere
  names a Canvas site for the lecture course's homework.
- `pdftotext` on the HW 1 handout, grepped for `submit|due|name|upload|canvas|pdf` — no output.
- Both the CESC 410 and CESC 510 info PDFs read end to end. § 8.6 / § 8.7 are identical and describe
  *format*, never *destination*. § 11.3's "can be submitted online" is the only statement that the
  channel is electronic at all.

**WHERE.** Start at **`https://erau.instructure.com`** — that is ERAU's Canvas, and it is not a
guess: it is printed in the page footers and page dumps of seven other courses on this disk. Then:

1. **Dashboard** → look for a **CESC 510** card (that is where the lab handouts live) and a
   **CESC 410** card. Check a **CESC 410** site first if one exists; the handout is titled
   "CESC 410/510 HW 1", so either is possible, and the 410 site is the more specific home.
2. **If neither card is on the Dashboard, that does not mean they are not there.** Canvas hides
   unfavourited courses from the Dashboard. Go **Courses → All Courses** and read the full list,
   including any *Past Enrollments* section.
3. In the course that has it: left nav → **Assignments** → the entry named for **HW 1**.

⚠ **No CESC 410 or CESC 510 Canvas course id is recorded anywhere in this repo.** Verified
2026-09-08, not assumed:

```sh
nice -n 19 grep -rlo 'erau\.instructure\.com' /home/devel/electrical_notes/content/ \
  | cut -d/ -f6 | sort -u
#   cesc_420  cesc_470  cpsc_462  ps160  stat_412  sys_304  syse_301
```

Seven other courses print the host; **`cesc_410` was absent from that list** until this paragraph
put the bare hostname on the page, so it now appears too — the only `cesc_410` hit is this file, and
it carries no course number. So this instruction can give you the host and the click path but not a
direct link, and **the CESC 470 id `208698` is a different course: do not reuse it.**

**When you find it, write it down once and every future hand-off gets specific for free.** Read the
course id out of the address bar (`https://erau.instructure.com/courses/<NNNNNN>`) and add it to two
places: the [Who to ask, and when](#who-to-ask-and-when) table in this file, and § *Course facts* in
[`../../labs_and_projects/README.md`](../../labs_and_projects/README.md#course-facts-that-drive-the-workflow),
which has been carrying a **NOT RECORDED** row for the same reason
([KI-15](../../labs_and_projects/reference_docs/known_issues.md#ki-15--a-human-task-that-names-no-place-costs-a-round-trip)).

**WHAT.** Upload the combined PDF:

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_410/hw/hw01/hw01-nelson-gatlin.pdf` | the HW 1 assignment submission box on the Canvas site above |

If that file is not on disk, build it — [Producing the PDF](#producing-the-pdf) below, two commands
(build, then merge).

**VERIFY.** Canvas shows the submission with a timestamp **before 4:00 pm on the due date**, and the
file it lists is **15 pages**. Open the preview and confirm page 1 is Prob 1 (phasor form) and the
last page is the convolution problem. A 2-page file means you uploaded one problem, not all six.

**IF IT IS NOT THERE.** No HW assignment entry on either Canvas site:

1. Check **Announcements** and **Modules** on the CESC 510 site — an assignment posted late often
   appears as an announcement first.
2. Ask a classmate. This is a one-line question and they answer in minutes; the instructor may not.
3. Email Dr. Liu with [Q3](#still-unknown--and-exactly-how-to-ask) verbatim. Copy both addresses.
4. **Fallback: print it and hand it in at the 4:00 pm class.** § 8.6 reads as though paper is the
   base case (*"on Letter-sized paper, leaving 1-inch margins for making copy and binding"*) with
   *"For electronic submission..."* as the variant, and the build already satisfies both
   constraints. **Cost, state it honestly:** this is an inference from the wording, not a stated
   rule, and § 11.3 says HW *"can be submitted online"* — so say "I could not find the online
   submission point" when you hand it over, and upload it as well once you find it.

**BLOCKS.** This blocks *only the act of turning it in*. The six problem files, the solutions
document, all builds, all flattened copies and the combined PDF are done and verified.

---

### H2 · Decide whether the working or the answers go in · Why human: Judgment

**Largely settled — read this before spending a question on it.** § 8.6 says *"Use correct approach
and show all necessary intermediate steps."* That is the per-problem files, not the answers-only
document. Treat it as decided.

**WHERE / WHAT.** Nothing to do. Both documents already exist and both build.

**VERIFY.** After a `--keep` build, both documents are on disk:

```sh
ls /home/devel/electrical_notes/content/cesc_410/hw/hw01/*.pdf
```

**Nine files, not seven** — the seven we build (`p01_…` … `p06_…` plus `hw01_solutions.pdf`), the
merged `hw01-nelson-gatlin.pdf`, and the instructor's `dsphw26-hw1.pdf`, which is not a build
product. The two that matter to this decision are `p01_phasor_form.pdf` (the working) and
`hw01_solutions.pdf` (the answers).

**IF THE GRADER SAYS OTHERWISE.** If feedback ever indicates only final answers were wanted, the
answers-only PDF is already built — swap the upload, change nothing else, and record the answer in
the [CONFIRMED table](#confirmed--quoted-from-the-course-info-pdf).

**BLOCKS.** Nothing. Both artifacts exist precisely so this decision costs nothing either way.

---

### H3 · Decide and place the AI-use disclosure · Why human: Judgment

**This is a course requirement and it is currently unmet.** § 11.1:

> *"If you use AI tools for your assignment, you should clearly indicate it."*

And the accountability clause that gives it teeth:

> *"Regardless of whether your code is handwritten or generated with AI assistance, you must be able
> to explain your code when asked (in class, during labs, or on assessments). If you cannot explain
> how your code works, you will not receive credit for that portion of the assignment."*

**Why this is human and not automated.** *What* to disclose and *how much* is a personal
representation about your own work. An agent must not write that sentence on your behalf, and must
not decide it is unnecessary. § 11.1 permits AI use outright — the requirement is disclosure, not
abstinence.

**WHERE.** The problem files, at
`/home/devel/electrical_notes/content/cesc_410/hw/hw01/p01_phasor_form.tex` … `p06_convolution.tex`
(and whatever `hwNN/` is current). The natural home is one line under `\problemheaderlo`, or a
single line on the first page of the combined PDF.

**WHAT.** Decide the wording, then add it once — one line of LaTeX under `\problemheaderlo`, no
macro needed. **Then rebuild AND re-merge.** These are two separate steps and skipping the second is
the trap: `hw01-nelson-gatlin.pdf` is a `pdfunite` of the six problem PDFs, so rebuilding a `.tex`
does *not* update it, and the file you upload would be the old one without the disclosure in it.

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_410/hw/hw01 --keep
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01
pdfunite p01_phasor_form.pdf p02_phasor_arithmetic.pdf p03_signal_transformations.pdf \
         p04_periodicity.pdf p05_system_properties.pdf p06_convolution.pdf \
         hw01-nelson-gatlin.pdf
```

**VERIFY.** Grep the **merged** file — that is the one that gets uploaded. Grep for a phrase, not
for `ai`: "ai" matches *obtained*, *pair* and *maintain*.

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01
pdftotext -layout hw01-nelson-gatlin.pdf - | grep -in 'AI tool'
```

Run today, before the line is added, it prints nothing and exits 1 — that empty result is the proof
the disclosure is **not** there yet (re-confirmed 2026-09-08 on both `p01_phasor_form.pdf` and the
merged file). After the line is added and the merge re-run, it must print the line, with a line
number. If it prints for `p01_phasor_form.pdf` but not for `hw01-nelson-gatlin.pdf`, you rebuilt but
did not re-merge.

**IF YOU ARE UNSURE WHAT FORM IT SHOULD TAKE.** § 11.1 does not prescribe one. Ask Dr. Liu:
*"For homework, how would you like AI use indicated — a line on the first page, or a note per
problem?"* Until answered, a single sentence on the first page is the conservative choice: it
cannot be *too* disclosed.

**BLOCKS.** Nothing technical. It is a policy obligation on the submission, so it must be settled
before **H1**, not after.

---

### H4 · Ask Q1–Q5 · Why human: Credentialed (they are a person, not a file)

**WHERE.** Email `jianhua.liu@erau.edu` and `liu620@erau.edu` (both — the info PDF lists two, so use
two), or office hours **MWF 1:30–3:50 pm, LB 349**, or the ten minutes before class in CoAS 203.

**WHAT.** Send **Q1–Q4 as one message**, with Q5 as a postscript. Batching matters: five separate
emails to an instructor buys five separate delays. The verbatim wording is in the
[table above](#still-unknown--and-exactly-how-to-ask) — it is written to be copy-pasted.

**VERIFY.** A reply that answers Q1 and Q3 by name. When it arrives, move each answer from the
UNKNOWN table into the [CONFIRMED table](#confirmed--quoted-from-the-course-info-pdf) with the date
and "per Dr. Liu, email" as the source, and delete the row from UNKNOWN. **That is the point of this
file** — it is the place answers get written down so nobody asks twice.

**IF THERE IS NO REPLY BEFORE THE DEADLINE.** Submit on the assumptions in the table — all four are
chosen so that being wrong costs a re-upload, not a rewrite. Then ask in person at the next class.

**BLOCKS.** Nothing. Every assumption is already implemented.

---

## Producing the PDF

**Two steps, not one:** build, then merge. Step one runs from the **repo root** and takes
repo-relative paths. **`--keep` is not optional here** — without it `build_tex.sh` deletes every PDF
it just made and there is nothing left to merge or upload:

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_410/hw/hw01 --keep     # keeps the PDFs
```

The course-local copy still works and takes paths relative to `content/cesc_410/hw/`, so its `cd`
is a different one — `cd /home/devel/electrical_notes/content/cesc_410/hw && tools/build_tex.sh hw01
--keep`. Prefer the shared checker: it is the same script every course uses, so a fix lands
everywhere at once.

**Verified 2026-09-08:** all seven files build, and every output is
`612 x 792 pts (letter)` with text starting at x = 71.99999 pt — 1.000 inch. § 8.6 satisfied without
anyone touching a setting; the margin comes from `\usepackage[margin=1in]{geometry}` in
`docs/latex/coursework_preamble.tex`.

### One combined PDF

`pdfunite` (poppler, already installed at `/usr/bin/pdfunite`) merges the per-problem PDFs in order.
Run after a `--keep` build:

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01
pdfunite p01_phasor_form.pdf p02_phasor_arithmetic.pdf p03_signal_transformations.pdf \
         p04_periodicity.pdf p05_system_properties.pdf p06_convolution.pdf \
         hw01-nelson-gatlin.pdf
```

Verified: 15 pages (2+2+3+2+3+3), letter, margins unchanged. **List the files explicitly in problem
order** — a `p0*.pdf` glob happens to sort correctly today and will stop doing so at `p10`.

The output name matches the `hw[0-9][0-9]-*.pdf` rule in
[`../.gitignore`](../.gitignore), so the merged file is ignored like every other build product. The
instructor's handouts are matched by no rule and stay tracked — confirm with
`git check-ignore -v <file>`, never by eye ([HW-07](findings.md#hw-07--build-products-vs-source-material-in-one-folder)).

Building a `\include` wrapper `.tex` instead would also work, but nothing needs it: `pdfunite` needs
no new source file, cannot drift from the problem files, and produces the same page sequence.

### Pre-submission check

Everything § 8.6 asks for, in one loop. Run it on the folder you are about to submit from:

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01
for f in *.pdf; do
  size=$(pdfinfo "$f" | awk -F': +' '/^Page size/{print $2}')
  lm=$(pdftotext -bbox "$f" - 2>/dev/null | grep -o 'xMin="[0-9.]*"' \
       | tr -dc '0-9.\n' | sort -n | head -1)
  tool=$(pdftotext -layout "$f" - 2>/dev/null \
         | grep -ciE 'build_tex|flatten_tex|new_tex|course_text|/home/|content/cesc|reference_docs')
  printf '%-34s %-22s left=%-10s toolrefs=%s\n' "$f" "$size" "$lm" "$tool"
done
```

Expected — actual output, 2026-09-08:

```text
dsphw26-hw1.pdf                    612 x 792 pts (letter) left=70.866000  toolrefs=0
hw01_solutions.pdf                 612 x 792 pts (letter) left=72.000000  toolrefs=0
p01_phasor_form.pdf                612 x 792 pts (letter) left=71.999990  toolrefs=0
p02_phasor_arithmetic.pdf          612 x 792 pts (letter) left=71.999940  toolrefs=0
...
```

Read it as: **`(letter)`** on every row, **`left=72`** (± a rounding tick) on every row of *ours*,
and **`toolrefs=0`** on every row. The handout's own `left=70.866` is 25 mm — that is the
instructor's template, not ours, and it is the row to ignore.

`toolrefs` is the same no-tooling-references rule the labs enforce
([`../../labs_and_projects/reference_docs/code_separation.md`](../../labs_and_projects/reference_docs/code_separation.md)):
nothing submitted may name a script, a flag, or a repository path.

---

## If the deliverable goes through Overleaf

**Never paste a source file in.** Its `\input` climbs above the project root and
cannot resolve there. Flatten first:

```sh
cd /home/devel/electrical_notes
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
#   -> content/cesc_410/hw/hw01/overleaf/*.tex   (gitignored, regenerable)
```

Each output is self-contained: paste or upload one and it needs no other file.
Verified for HW1 — all seven flattened copies compile on their own under `tectonic`,
re-checked 2026-09-08.

Two things to know before handing a flattened copy to anyone:

- **If the `.tex` itself is ever the deliverable, hand in the flattened copy, not the source.** The
  source's first two lines are `\input{../../../../docs/latex/...}` and
  `\input{../../reference_docs/...}` — repository paths, in the file. The flattened copy has none;
  **no output from this grep is the pass**, and it exits 1:

  ```sh
  cd /home/devel/electrical_notes/content/cesc_410/hw/hw01
  grep -nE 'docs/latex|reference_docs|/home/' overleaf/*.tex
  ```

  Re-run 2026-09-08 on all seven flattened copies: nothing.
- The flattened copy opens with two comment lines — *"Self-contained: preamble inlined"* and
  *"Generated copy of `p01_phasor_form.tex` — edit the original, not this."* **They carry no
  repository path**; the flattener was fixed to emit only the basename
  ([HW-10](findings.md#hw-10--the-flattener-used-to-stamp-a-repo-path-into-its-output--fixed)).
  A LaTeX comment never reaches the PDF, so this only matters at all if the `.tex` is what gets
  handed in — in which case delete the two lines, since even a basename names our filename.
- **Edit the source, never the flattened copy.** `overleaf/` is overwritten on
  the next run.

**Check any submitted `.tex` or PDF carries no tooling references** — no script names, flags, or repository paths. Same rule as the labs ([`../../labs_and_projects/reference_docs/code_separation.md`](../../labs_and_projects/reference_docs/code_separation.md)). The [pre-submission check](#pre-submission-check) above does this for PDFs.

---

## Per-assignment record

Fill a row when the assignment appears; move answers here as they are confirmed.

| HW | Due | Format | Confirmed? | Notes |
| --- | --- | --- | --- | --- |
| 01 | **Wed 9/9/26** (§ 9 schedule; time of day unconfirmed — [Q2](#still-unknown--and-exactly-how-to-ask)) | Single combined PDF, letter, 1-in margins, full working | ⚠ format per § 8.6; **destination** unconfirmed — [Q3](#still-unknown--and-exactly-how-to-ask) | 6 problems, 130 pts. Handout labels two of them "Prob 1" ([HW-02](findings.md#hw-02--the-handout-numbers-two-different-problems-prob-1)). No code in this one |

---

**Related:** [`../prompt.md`](../prompt.md) · [`hw_workflow.md`](hw_workflow.md) · [`findings.md`](findings.md) · [`../hw01/README.md`](../hw01/README.md) · [`../../senior_design/cesc410-course-info-fall2026.pdf`](../../senior_design/cesc410-course-info-fall2026.pdf)
