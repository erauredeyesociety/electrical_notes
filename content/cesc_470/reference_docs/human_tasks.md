# Human tasks — CESC 470

**The rules are shared; this file is only the coordinates.** Read
[`docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md)
first — it defines the six reasons a task may be human, the
WHERE / WHAT / VERIFY / IF-ABSENT / BLOCKS form, the Source (FROM) → Destination (TO)
rule, and the hand-off checklist. **None of that is repeated here**, deliberately: a
second copy would drift from the first.

What follows is only what the directive cannot know — *which* Canvas course, *which*
instructor, *which* folder on this machine, and *what has already been searched for so
nobody searches twice.*

Everything below was verified on **2026-09-08** unless a line says otherwise.

---

## Course coordinates — the answer to every "WHERE"

The directive's Rule 3 says a WHERE fails on category nouns. "Canvas" is a category
noun. This table is what replaces it.

| Thing | Value | Evidence |
| --- | --- | --- |
| LMS | Canvas at `erau.instructure.com` | print footer on all 12 pages of [`../cesc_470.pdf`](../cesc_470.pdf) |
| **Canvas course id** | **208698** → course home `https://erau.instructure.com/courses/208698` | that footer reads `https://erau.instructure.com/courses/208698/external_tools/136240` |
| Canvas course title | `DB-CESC 470 01DB Computer Architecture` | same footer line, syllabus p1 |
| Instructor | **Siyao Li** · `lis14@erau.edu` | syllabus p1 |
| Office hours | **not printed.** The syllabus says only *"Instructors are available during scheduled office hours … Appointments outside office hours can be arranged by request."* Ask in class or by email. | syllabus p5 |
| Class meeting | MWF 11:00–11:50 AM, **Lehman Building 369** | syllabus p1 |
| TA | **none — the syllabus names no TA anywhere.** "Ask the TA" is not an option in this course; the instructor is the only route. | syllabus, all 12 pages |
| Walk-in tutoring | College of Engineering tutoring lab, **COE LB 332** — covers 300/400-level `CESC` | syllabus p12 |
| Canvas support | Help link, bottom of Canvas' left global nav · hotline 1-833-334-2831, 24/7 | syllabus p7 |
| Late penalty | **20% within 3 days; not accepted after 3 days** unless arranged beforehand | syllabus p6 |
| Submission format | *"All homework must be typed and converted to pdf for submission."* — format only; it does **not** say how many files | syllabus p5 |

⚠ **The course id was read off a print footer, not opened.** This machine holds no
Canvas session, so `208698` has never been confirmed by loading the page. It appears on
**every one of the 12 page footers** of the syllabus print-out, so it is very unlikely to
be wrong — but if `https://erau.instructure.com/courses/208698` 404s, or opens some other
course, **this is the whole recovery. Do not go hunting; do this:**

1. `https://erau.instructure.com` → **Dashboard** → the **CESC 470 / Computer
   Architecture** card. If no such card is there, **Courses → All Courses** — unfavourited
   courses are hidden from the Dashboard.
2. Open it and read the address bar: `https://erau.instructure.com/courses/<NNNNNN>`.
3. Confirm it is the right course before trusting the number: the title contains
   **CESC 470** and the instructor is **Siyao Li**. A number that opens a different course
   is the wrong number.
4. Correct **every** occurrence. The id is written in **three files**, and fixing only
   this table leaves the other two stale. This command lists all of them — do not count
   them by eye:

   ```sh
   grep -rn 208698 /home/devel/electrical_notes/content/cesc_470/ --include='*.md' \
     | grep -v pdf_transcripts
   ```

   The three files are this one,
   `/home/devel/electrical_notes/content/cesc_470/hw/prompt.md`, and
   `/home/devel/electrical_notes/content/cesc_470/hw/hw01/README.md`.
   **Leave `content/cesc_470/pdf_transcripts/cesc_470.md` alone** — that is the `grep -v`
   above; it is a verbatim transcript of the PDF and must keep whatever the PDF printed,
   even if the PDF was wrong.
5. If the course is genuinely not in **All Courses**, the enrolment is the problem and not
   the URL — email `lis14@erau.edu`. There is no TA to ask.

## Where downloaded files land on this machine

Not a guess — the browser's copies are still there, byte-identical to the tracked ones:

```sh
md5sum "/home/devel/electrical_notes/content/cesc_470/Module 01 Introduction to computer technology & ISA (1).pdf" \
       "/home/devel/Downloads/Module 01 Introduction to computer technology & ISA (1).pdf"
```

```text
341b4c26c830c8db56aa8c7969bba3b0  /home/devel/electrical_notes/content/cesc_470/Module 01 Introduction to computer technology & ISA (1).pdf
341b4c26c830c8db56aa8c7969bba3b0  /home/devel/Downloads/Module 01 Introduction to computer technology & ISA (1).pdf
```

So **`/home/devel/Downloads/` is the FROM side of every download task below**, and the
copy is a plain `cp` with no conversion. `/home/devel/Downloads/HW1.pdf` is there too.

## Destinations, by kind of file

| Kind of file | Destination (TO) — absolute | Exists today? |
| --- | --- | --- |
| Lecture deck (`Module NN ….pdf`) | `/home/devel/electrical_notes/content/cesc_470/` | ✅ yes |
| Syllabus or schedule | `/home/devel/electrical_notes/content/cesc_470/` | ✅ yes |
| Homework handout | `/home/devel/electrical_notes/content/cesc_470/hw/hwNN/` | only `hw01/` |
| Quiz handout | `/home/devel/electrical_notes/content/cesc_470/qz/qzNN/` | ❌ `qz/` exists, no `qzNN/` yet |
| Exam handout | `/home/devel/electrical_notes/content/cesc_470/exam/examNN/` | ❌ **`exam/` does not exist at all** |

**Where the folder does not exist, the `mkdir -p` is part of the task, not a suggestion.**
Git stores no empty directories, so these have to be created at the moment a file lands
in them — copy the line you need:

```sh
mkdir -p /home/devel/electrical_notes/content/cesc_470/hw/hw02      # next homework
mkdir -p /home/devel/electrical_notes/content/cesc_470/qz/qz01      # first quiz
mkdir -p /home/devel/electrical_notes/content/cesc_470/exam/exam01  # first exam
```

Every one of these destinations is **tracked by git whatever the file is called** — the
course `.gitignore` whitelists our own build products instead of blanket-ignoring `*.pdf`.
Proved below under *Closed tasks*, so no human needs to check it again.

## Already searched — do not repeat

| Question | Command run | Answer |
| --- | --- | --- |
| Is there a Module 02+ deck anywhere on this machine? | `find /home/devel -iname 'Module 0*.pdf'` | No. Only Module 01, in the repo and in `Downloads/`. |
| Does `HW1.pdf` say how to submit? | rendered all 3 pages and grepped for `submit`, `Canvas`, `upload`, `pdf` | **No.** The only such line is `Total: 100 points   Due Date: 9/13/2026`. The handout is problems and nothing else. |
| Does the syllabus name a TA, or an office-hour time? | read all 12 pages of the transcript | No to both. |

---

## The register

### H1 · Confirm what to upload for HW1, then upload it — **due 9/13/2026**

**Why human:** `Credentialed` (Canvas login) **and** `Judgment` (the syllabus is silent
on how many files).

**Already tried — do not repeat.** The syllabus' only submission sentence is p5's
*"All homework must be typed and converted to pdf for submission"*: a **format**, not a
**count**. `HW1.pdf` adds nothing (see the search table above). So the repo genuinely
cannot tell whether the grader wants the one condensed solutions PDF, the ten
per-problem PDFs, or both, and picking silently is exactly what
[`coursework-solutions.md`](../../../docs/directives/coursework-solutions.md) forbids.

**WHERE.** `https://erau.instructure.com/courses/208698` → left nav **Assignments** →
the **Homework 1** item. Read the *Submission Attempts / Submission Details* block and
any rubric on that page — Canvas states the accepted file count and type there, and
that page overrides the syllabus.

**WHAT.** Build the PDFs first, then upload. The build is already automatable and done:

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_470/hw/hw01 --keep
```

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_470/hw/hw01/hw01_solutions.pdf` | Canvas → course 208698 → Assignments → Homework 1 → **Submit Assignment** |
| `/home/devel/electrical_notes/content/cesc_470/hw/hw01/p01_five_components.pdf` … `p10_amdahl_speedup.pdf` | the same upload, **only if** the Canvas page asks for per-problem files |

**VERIFY.** Two checks, both cheap:

```sh
ls -l /home/devel/electrical_notes/content/cesc_470/hw/hw01/*.pdf
```

expects **12** files — the handout `HW1.pdf`, plus the eleven build products
(`hw01_solutions.pdf` and `p01_…` through `p10_…`) freshly timestamped. Then, in Canvas,
the assignment page shows **Submitted!** with a timestamp before 9/13/2026 in the right
sidebar. A submission with no timestamp did not go through.

**IF THE CANVAS PAGE DOES NOT SAY.**
1. Check **Modules** and then **Announcements** for the same assignment — instructors
   often state the format once, in one place.
2. Email `lis14@erau.edu`, or ask at the start of MWF 11:00 class in Lehman 369.
   One sentence: *"For HW1, do you want the single solutions PDF or one PDF per
   problem?"*
3. **Fallback if no answer arrives before 9/13:** upload **both** —
   `hw01_solutions.pdf` first, the ten per-problem PDFs after it. A superset cannot lose
   points for omission. Note the choice in the submission comment so it is visible rather
   than silent.
   **If the upload widget offers no "Add Another File" button**, the assignment is
   configured for a single file and the question answers itself: upload
   `hw01_solutions.pdf` alone — it is the complete assignment, all ten problems, and say
   in the submission comment that per-problem PDFs are available on request. Do not
   concatenate the eleven into one file to get around the limit; the solutions document
   is already the condensed whole.

⚠ **Do not let this run past the deadline while waiting for an answer.** Syllabus p6:
20% off within 3 days, and **after 3 days it is not accepted at all**.

**BLOCKS.** Only the upload. All eleven documents are written, built, flattened,
verified numerically and visually — see
[`../hw/hw01/README.md`](../hw/hw01/README.md) § Verification. Nothing in the repo waits
on this.

---

### H2 · Bring the homework/quiz schedule into the repo

**Why human:** `Credentialed`.

**Already tried.** Syllabus p6 says, in full: *"A tentative schedule for homework
assignments and quizzes will be provided later. Please review it and inform me of any
time conflicts."* It is not in the syllabus PDF, and nothing matching it is on this
machine. **So it may genuinely not exist yet** — this is a "check whether it has
appeared", not a "find the thing that is definitely there".

**WHERE.** `https://erau.instructure.com/courses/208698` → **Syllabus** tab (Canvas
renders the course's dated assignment list at the bottom of that tab even when no file
is posted), then **Announcements**, then **Files**.

**WHAT.** If it is a file:

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Downloads/<whatever it is called>.pdf` | `/home/devel/electrical_notes/content/cesc_470/` |

If it is only the Canvas-rendered list, paste the dates into a comment at the top of
[`../hw/prompt.md`](../hw/prompt.md) § Assignments instead — a screenshot is not
greppable.

**VERIFY.**

```sh
ls -l /home/devel/electrical_notes/content/cesc_470/*.pdf
```

Today that prints exactly two files (`cesc_470.pdf` and the Module 01 deck); a third
means it landed.

**IF ABSENT.** Ask in class — this is a one-line question and the syllabus explicitly
invites it (*"inform me of any time conflicts"*). There is no TA to ask.

**BLOCKS.** Nothing today. It blocks *knowing whether an HW2 or a quiz exists* — the
repo currently has no way to learn that a deadline has been set.

---

### H3 · Fetch Module 02 and later decks as they are posted

**Why human:** `Credentialed`.

**Already tried.** `find /home/devel -iname 'Module 0*.pdf'` returns only Module 01
(twice: the tracked copy and the `Downloads/` original). Nothing later has been posted
to this machine.

**WHERE.** `https://erau.instructure.com/courses/208698` → **Modules** (the decks are
named `Module NN <topic>`), or **Files** if Modules is not enabled.

**WHAT.**

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Downloads/Module 02 <topic>.pdf` | `/home/devel/electrical_notes/content/cesc_470/Module 02 <topic>.pdf` |

**Keep the instructor's filename exactly, spaces and all.** The `.gitignore` tracks it
whatever it is called, and renaming would break the citations that name it.

**VERIFY.** Run the triage before citing a single page of it:

```sh
cd /home/devel/electrical_notes/ocr_handler
uv run ocr-handler inspect "../content/cesc_470/Module 02 <topic>.pdf"
```

Module 01 prints this today, which is the shape to expect (abbreviated — the real run also
prints a `pages needing OCR:` list and, under the `!` line, a `pages:` list naming the
suspect pages, then a paragraph explaining each signal; that is normal, not an error):

```text
Module 01 Introduction to computer technology & ISA (1).pdf: 88 pages, 22,062 chars (251/page)
verdict: ocr-partial
  ok 26   sparse 48   empty 14
  pages needing OCR: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, … (+32 more)
  ! structure-suspect-partial: 6/88 pages  (letter-spaced 1  shredded-lines 1  …)
    pages: 1, 52, 53, 54, 55, 56
```

A verdict of `text-layer-sufficient` means the deck can be read directly; `ocr-partial`
means the same "locator, not reader" caution as Module 01 applies.

**IF ABSENT.** The decks appear as the term progresses; absence usually means "not
taught yet", not "lost". Cross-check the date against the schedule from H2 before
asking anyone.

**BLOCKS.** Only work on that module. **Deriving the new deck's PDF-page → printed-slide
offset is not a human task** — it is automatable and will be done here once the file
exists. Module 01's offset (PDF page − 7) does *not* carry over; see
[`findings.md`](findings.md) § HW-01.

---

### H4 · Fetch the next handout — HW2, or the first quiz

**Why human:** `Credentialed`.

**WHERE.** `https://erau.instructure.com/courses/208698` → **Assignments** for homework,
**Quizzes** or **Modules** for a quiz. HW1's file was called `HW1.pdf`, so `HW2.pdf` is
the likely name — but do not rely on it, and do not rename whatever arrives.

**WHAT.** Create the folder first; **neither of these exists yet**, and git stores no
empty directories, so the `mkdir -p` is part of the task. Run the line that matches what
actually arrived:

```sh
# a homework
mkdir -p /home/devel/electrical_notes/content/cesc_470/hw/hw02
# a quiz  —  content/cesc_470/qz/ exists but is empty; there is no qz01/ yet
mkdir -p /home/devel/electrical_notes/content/cesc_470/qz/qz01
```

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Downloads/HW2.pdf` | `/home/devel/electrical_notes/content/cesc_470/hw/hw02/HW2.pdf` |
| `/home/devel/Downloads/<whatever the quiz handout is called>.pdf` | `/home/devel/electrical_notes/content/cesc_470/qz/qz01/<same filename>.pdf` |

**Keep the instructor's filename, spaces and all.** The quiz will not be called
`Quiz01.pdf` just because the folder is `qz01` — see *Closed tasks* below, where an
instructor filename with a space was checked against `.gitignore` and kept.

**VERIFY.** The file is present *and* git will keep it. Substitute the path you actually
used:

```sh
cd /home/devel/electrical_notes
ls -l content/cesc_470/hw/hw02/          # or content/cesc_470/qz/qz01/
git check-ignore -v content/cesc_470/hw/hw02/HW2.pdf ; echo "exit=$?  (1 = kept, good)"
```

`git check-ignore` exiting **1** with no output means the file is tracked — that is the
good case, and it is what this prints today for both a `hwNN/` and a `qzNN/` path.
Any output means a `.gitignore` rule matched it and it would be lost — stop and report
that, naming the rule the command printed.

**IF ABSENT.** See H2: no schedule has been published, so "no HW2 yet" is the expected
state, not a failure.

**BLOCKS.** All work on that assignment — there is nothing to solve until the handout
exists. Everything for HW1 is done.

---

### H5 · Decide whether to raise the Q10 wording with the instructor — *optional*

**Why human:** `Judgment`.

HW1 Q10's *"maximum possible speedup"* has two defensible readings (3.57× achieved,
5× ceiling). This is **already handled**: both are on the face of the submitted
document, so a grader never has to guess which was meant.
[`findings.md`](findings.md) § HW-02 has the full argument.

Nothing is required. Raising it with `lis14@erau.edu` before 9/13 could confirm the
intended reading; **the cost of not raising it is zero**, because answering both cannot
be marked wrong for omission. Listed here so the choice is visible, not because it is
outstanding.

**BLOCKS.** Nothing.

---

## Closed tasks — kept so they are not re-opened

### ✅ "Confirm the quiz PDF naming" — closed 2026-09-08, no human needed

This sat on the human list on the theory that an unpredictably-named quiz handout might
be swallowed by `.gitignore`. **It cannot be**, and that is now checked rather than
assumed:

```sh
cd /home/devel/electrical_notes
git check-ignore -v "content/cesc_470/qz/qz01/Quiz Application.pdf"
git check-ignore -v "content/cesc_470/qz/qz01/whatever.pdf"
git check-ignore -v "content/cesc_470/hw/hw01/p01_five_components.pdf"
```

```text
                     (no output, exit 1)  -> "Quiz Application.pdf"  KEPT
                     (no output, exit 1)  -> "whatever.pdf"          KEPT
content/cesc_470/.gitignore:33:p[0-9][0-9]_*.pdf   -> our build product  IGNORED
```

Both an instructor filename with a space and an arbitrary one are kept; only our own
generated PDFs are ignored. The rule is a whitelist of our output, so **no handout name
can be lost** and there is nothing to confirm. Reasoning: [`findings.md`](findings.md)
§ HW-09.

---

**Related:** [`findings.md`](findings.md) ·
[`../hw/prompt.md`](../hw/prompt.md) ·
[`../hw/hw01/README.md`](../hw/hw01/README.md) ·
[`../qz/README.md`](../qz/README.md) ·
[`../../../docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md) ·
sibling register: [`../../cpsc_462/reference_docs/human_tasks.md`](../../cpsc_462/reference_docs/human_tasks.md)
