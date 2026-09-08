# What each lab actually requires

> ⚠ **Still the biggest open question in the setup — but it is now a smaller one.** **When** a
> submission is due, and **when** the demo must happen, were answered by the TA on 2026-09-08 and are
> recorded below as **ANSWERED**. **What** a submission consists of is still **not uniform and not
> confirmed**. Do not assume every lab wants code, or a report, or figures. **Confirm per lab, and
> record the answer here.**

---

## What we actually know

| Source | Says |
| --- | --- |
| **TA announcement, *"Lab 1 and Future Labs"*, Ryle, retrieved 2026-09-08** | *"Lab write-ups/deliverables are due on Canvas **1 week** after they are assigned."* — the **Canvas deadline**, stated |
| | *"You must demo your completed lab to me by the next lab section."* — the **demo deadline**, stated. Note this is *by the next section*, not *at the start of the meeting* as the course info implied |
| | *"If you complete your lab before class, you are welcome to show up, demo it to me, and leave early."* — **early checkout is sanctioned** |
| | *"If you need supplemental instruction or extra help, you are welcome to show up and attend the other lab section as well."* — **the other section is a second slot** |
| | *"I will copy over and post the Lab PDF directly inside the **Modules** tab under the respective lab pages."* — where handouts live |
| | *"For future labs, I will continue posting a reference document addressing common edge cases, setup quirks, or potential issues."* — **expect a supplemental doc per lab; read Announcements before starting one** |
| | **It does not say what a submission consists of.** "Write-ups/deliverables" is exactly as vague as the course info |
| **CESC 410L course info** | *"Please submit the report and code of the old lab before coming to the lab meeting of the new one."* — so **report + code** is the general rule |
| | *"Although you are required to submit lab reports, the report will not be assessed before the ATs can see your live demo of the lab."* — the **demo gates the report** |
| | One submission per team, **except ABET-artifact labs**, where every student submits independently |
| | **Late reports are not accepted. Missing report = 0. No resubmission.** |
| **Lab 0 handout** | *"This is Lab 0, and the submission is only for a testing if you can run the project. The focus of this submission is the screenshot of the four figures."* |

Full transcript of the announcement:
[`../lab01/ta_announcement_lab1_and_future_labs.md`](../lab01/ta_announcement_lab1_and_future_labs.md).

**The course info and the Lab 0 handout still disagree about *what*,** and that disagreement is the
point of this file. The course info says report+code; the Lab 0 handout says the focus is four
screenshots. The handout is more specific and more recent, so it probably governs — but *probably* is
not good enough when late means zero.

**The announcement also quietly corrected a timing assumption.** This repo had been telling people the
demo happens *"at the start of the meeting"* — an inference from the course info's ordering. The TA's
rule is **by the next lab section**, and early checkout is offered. Arriving early is still the
sensible play; it is what makes leaving early possible. Anywhere that phrasing survives, it is stale.

### The two deadlines are separate rules

| | Canvas deliverable | In-person demo |
| --- | --- | --- |
| Rule | **1 week after the lab is assigned** | **By the next lab section** |
| Lab 1, Sec 1 (assigned 9/8) | due **9/15** | by the **9/15** meeting |
| Lab 1, Sec 2 (assigned 9/4) | due **9/11** | by the **9/11** meeting |
| When they diverge | a lab spanning a no-lab week — **10/2–10/6, 10/16–10/20, 11/6–11/10** — pushes the *meeting* out a week while the 1-week upload clock keeps running | |

Lab dates: [`../README.md`](../README.md#schedule) § *Schedule*. **Do not collapse these into one
date.** For Lab 1 they coincide; for Lab 5 (Sec 2 assigned 10/9, next meeting 10/23) they will not.

### Settling it · Why human: **Judgment** (two defensible answers, and the wrong one is a zero)

**WHO.** **Ryle**, the lab TA — recorded 2026-09-08, so this instruction no longer has to say "the TA".

| Route | Address | When |
| --- | --- | --- |
| In person | LB 373, at the lab meeting — Sec 1 Tue / Sec 2 Fri, 5:15–8:15 pm | Best: the same trip as the demo, so it costs nothing |
| In person, other section | same room, the *other* section's day | The TA invites students to attend either section |
| Discord | **`ryletraub_30890`** | Between meetings — the TA's own first suggestion |
| Canvas **Inbox** | on the course site | If you want it on the course record |

⚠ **Email is invited but no address is published.** *"Feel free to email me or reach out via Discord"*
— with only the Discord handle given. **Do not construct an address**; ask for it at a meeting and add
it to [`../README.md`](../README.md#course-facts-that-drive-the-workflow) § *Course facts*.

> **Still missing: the Canvas course URL and the exact module titles.** The *tab* is known — the TA
> posts each lab's material under **Modules**, on that lab's page — but not the titles. The
> step-by-step for filling those last two in is
> [`../README.md`](../README.md#how-to-fill-in-the-last-two--three-minutes-once--why-human-credentialed)
> § *How to fill in the last two*.

**WHAT.** Ask in this order, and write the answers down verbatim:

1. Figures, code, report — which of the three does *this* lab want?
2. If code: the whole `dsp26` package, only this lab's subpackage, individual `.py` files, or pasted
   into the report?
3. Is a PDF required, or is another format accepted?
4. Does this lab collect an **ABET artifact**? (If yes, every student submits independently.)

**VERIFY.** This lab's row in [Per-lab requirements](#per-lab-requirements) is filled in, *Confirmed
with TA?* is ✅, and the Notes column quotes the TA's own wording. An unquoted row is a guess.

⚠ **Check the handout first — it may already answer it.** Lab 1's did: *"Submit a single PDF file containing all the artifacts."* When the handout is explicit, follow it; over-submitting is only a safe default when nothing says otherwise.

**IF YOU CANNOT ASK IN TIME.** **Produce everything and submit everything** — figures, code zip and
report. Over-submitting has no stated penalty. Under-submitting is a zero with no resubmission, so the
asymmetry is not close.

**BLOCKS.** Only which mode of `make_submission.sh` runs. Nothing about writing the code, generating
the figures or drafting the report waits on this — **do all of that first.**

---

## Per-lab requirements

Fill in as each is confirmed. `?` means unconfirmed — treat it as "produce everything and ask."

| Lab | Figures | Code | Report | Confirmed with TA? | Notes |
| --- | --- | --- | --- | --- | --- |
| 00 | ✅ **the four PNGs — this is the whole submission** | ❌ no | ❌ no | ✅ per handout | *"The focus of this submission is the screenshot of the four figures... these figures can be saved to files using an option of the command."* Saving is sanctioned, so the PNGs are the screenshots |
| 01 | **1 PDF** | ✅ **ANSWERED by the handout, 2026-09-08** | — | ✅ resolved | Handout § Submission: *"Submit a single PDF file containing all the artifacts collected from the tasks above."* One file. **Not** the code zip — the Programming task asks for a *Code Snippet*, i.e. code printed INSIDE the PDF, which it is. The zip is 93% `uv.lock` and 1.8% Lab 0 code; uploading it adds dependency-lockfile noise the handout never asked for. The "submit all three" default was the right call while this was unknown, and is now superseded |

---

## Questions to ask

Each row says who to ask, what changes when it is answered, and **what to do until it is** — so an
unanswered question never stalls work. Cross a row out when it is settled and record the wording.

Answered rows keep their wording and the source, so nobody re-asks them. **Ask Ryle** —
Discord `ryletraub_30890`, Canvas Inbox, or at a meeting; see *Settling it* above for the routes.

| # | Question | Ask | If unanswered, do this | What it blocks |
| --- | --- | --- | --- | --- |
| 1 | ~~For Lab 0 — is the four-figure screenshot the whole submission?~~ **Resolved: yes, four figures only.** The handout is explicit and governs over the course info's general report+code rule. Still worth confirming the general rule for Lab 1 onward. | TA, at a meeting | — | — |
| 2 | Is the report format the CEC 320 four-section template (Introduction / Narrative / Artifacts / Discussion & Results)? Is a CESC 410L template posted? | Ryle; also check Canvas **Modules** and the **Syllabus** page | Use [`report_template.tex`](report_template.tex) as-is and say in the report's Introduction that the CEC 320 structure was followed | Nothing. The report is written either way; only its section headings would change |
| 3 | When code is submitted, what form — a zip of the package, individual `.py` files, or pasted into the report? | Ryle | Submit the zip **and** paste the lab's own files into the report's Artifacts section | Nothing. `make_submission.sh` already builds the zip |
| 4 | The whole `dsp26` package each time, or only that lab's subpackage? | Ryle | Submit the whole package — it is what the handout's single-venv design produces, and the zip is under 100 kB | Nothing |
| 5 | Is a PDF required, or is another format accepted? | Ryle | Submit the PDF. `tools/render_reports.sh labNN` produces it and it is the least surprising format | Nothing |
| 6 | Which labs collect **ABET artifacts**? Those require independent individual work and separate submissions. | Ryle, **at the start of each lab** — it changes per lab | **Submit individually.** An extra individual submission is never wrong; a missing one is a zero | How many times you upload |
| 7 | ~~When is a lab's Canvas submission due?~~ **✅ ANSWERED 2026-09-08** — *"Lab write-ups/deliverables are due on Canvas **1 week** after they are assigned."* | — | — | — |
| 8 | ~~When must the live demo happen, and does it have to be at the start of the meeting?~~ **✅ ANSWERED 2026-09-08** — *"You must demo your completed lab to me by the next lab section."* **By the next section**, not necessarily at the start of one. | — | — | — |
| 9 | ~~Can you demo early and leave, or must you sit the whole session?~~ **✅ ANSWERED 2026-09-08** — *"If you complete your lab before class, you are welcome to show up, demo it to me, and leave early."* | — | — | — |
| 10 | ~~Who is the lab TA and how do you reach them outside the meeting?~~ **✅ ANSWERED 2026-09-08** — **Ryle**, Discord `ryletraub_30890`. **Email is invited but no address is given** — that part is still open, and is question 11. | — | — | — |
| 11 | What is Ryle's email address? The announcement says *"feel free to email me"* and gives only the Discord handle. | Ryle, at a meeting | Use **Discord** or Canvas **Inbox**. **Do not construct an address** from the handle or an ERAU pattern | Nothing. Two working routes already exist |

**Source for rows 7–10:** the announcement *"Lab 1 and Future Labs"*, transcribed at
[`../lab01/ta_announcement_lab1_and_future_labs.md`](../lab01/ta_announcement_lab1_and_future_labs.md).

**None of these block the work.** Every open row has a default that is safe to act on today. That is
the point of writing them this way — see
[`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md) Rule 5.

### Still open, and why the announcement did not settle it

The TA answered every **timing** question and left every **content** question untouched. *"Lab
write-ups/deliverables"* is one phrase covering figures, code and report without distinguishing them —
the same ambiguity the course info has. **Rows 2–6 and 11 stand.** Until row 3 or 4 is answered, Lab 1
and every lab after it defaults to *produce everything and submit everything*: over-submitting has no
stated penalty, and under-submitting is a zero with no resubmission.

---

## Student ID

| | |
| --- | --- |
| ERAU student ID | **2636127** |
| Last 4 digits (`myID`) | **6127** |

The last four digits seed each lab's RNG, so the value lives in the lab source:

Run from `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

```sh
grep -rn "myID" dsp26/src/
```

Prints exactly two lines today (verified 2026-09-08) — `lab0_sinusoids/recipes.py:27:myID = 6127` and
the `np.random.seed` line beneath it. **Name the file precisely when you quote this:** there is a
`recipes.py` in every lab subpackage, and only Lab 0's carries a `myID`.

Expect every lab to have its own `myID` line. Set it before generating anything you intend to submit.

**Note on `Freq_1` in Lab 0:** setting the real ID produced figures identical to the `1234` placeholder. That is expected — see [KI-06](known_issues.md#ki-06--setting-your-erau-id-may-not-change-the-figures-at-all). Only four base frequencies are reachable, so collisions are common.

### Publishing and git — not a concern here

**Decision (2026-09-01): the publishing and git-repository aspects of the parent `electrical_notes` repo do not apply to this project.** Recorded so it does not get re-raised.

For context, since it will look surprising later: the parent repo has a GitHub remote and a `hugo.yaml` with `baseURL: https://erauredeyesociety.github.io/electrical_notes/`, which would normally mean everything under `content/` is web-published. **That is not how this coursework folder is being treated.** Store IDs and course material here as convenient; do not add redaction steps, and do not warn about it again.

---

## Packaging a submission

**Requirements vary by lab and are expected to change.** `tools/make_submission.sh` therefore has modes rather than one fixed output. Add modes as new shapes appear; do not hand-assemble a zip.

| Lab wants | Command | Produces |
| --- | --- | --- |
| **Report + figures** (Lab 0) | `make_submission.sh labNN name --figures` | `labNN-figures-name.zip` — `report.pdf`, `report.tex`, `report.md`, `figs/*.png` |
| **Code** | `make_submission.sh labNN name` | `dsp26-labNN-name.zip` — stripped package with per-file headers |
| Code, comments intact | `... --keep-comments` | same, unstripped |

`--figures` delegates rendering to `tools/render_reports.sh` — **the only script that renders PDFs**. PDFs are kept and gitignored (`report*.pdf`), so there is no exception to reason about: rendering behaves the same everywhere.

**All `*.zip` is gitignored.** Every archive here is a build product of this script; nothing zipped belongs in the repo.

Both modes print their file list. **Read it before uploading.**

**Packaging refuses to build** if any file about to ship names our tooling — a script, a flag, or a repository path. It prints the offending file and line. Deliverables should not describe how our repo works ([KI-09](known_issues.md#ki-09--tooling-references-leaked-into-a-submitted-report)).

### When a lab needs a shape that does not exist yet

Add a mode. The pattern is a flag, an early-exit block, and a row in the table above. Do not build zips by hand — the printed manifest is the check that stops `.venv` or `tools/` leaking into a submission.

---

## Preparing code for submission

Only relevant when code is actually being submitted.

Working copies carry heavy explanatory comments — that is deliberate, and it is what makes the code useful to us months later ([`code_commenting.md`](code_commenting.md)). **That density is not what you hand in.** `tools/make_submission.sh` strips it.

```sh
tools/make_submission.sh lab00 nelson-gatlin
```

Pipeline: copy `dsp26/` to a staging dir → strip comments and docstrings → prepend a `# CESC 410L -- Lab N / name / date` header to each file → zip → print the file list.

**The working tree is never modified.** Stripping happens on a throwaway copy; your commented source stays exactly as it is.

### What survives a strip, and why

| Kept | Reason |
| --- | --- |
| Shebang, encoding lines | Functional, not commentary |
| `DEVIATION FROM HANDOUT` blocks — **whole block** | Honest disclosure that handout code was modified |
| The `last 4 digits` ERAU-ID marker | Marks the one line that must be personalised |

**Everything else — every explanatory comment and every docstring — is removed.**

> **On keeping the DEVIATION markers.** `--strip-all` removes them too, and it is there if you want it. But think about what it does: it ships modified handout code with no indication it was modified. The point of the marker is that a TA reading the code sees *"this differs from the handout, and here is why"* — which is the same story the report's Narrative section tells and gets graded on. Removing the comment while the report describes the fix is just inconsistent. **The default keeps them; that is the recommended setting.**

### Why not regex

The obvious implementation — `re.sub(r'#.*$', '', line)` — is unsafe, because `#` appears inside string literals:

```python
url = "https://example.com/#anchor"     # regex truncates the URL
css = "color: #fff"                     # and breaks this
```

`tools/strip_comments.py` uses Python's `tokenize` module, which distinguishes a comment from a `#` inside a string. It then:

- removes docstrings via `ast`, **except** one that is a function's sole statement (removing it would be a `SyntaxError`);
- **verifies** the result by re-parsing and comparing ASTs, and refuses to emit anything that fails;
- was checked against the real lab code by running the stripped copy and confirming it produces **byte-identical figures**.

Options:

```sh
tools/make_submission.sh lab00 nelson-gatlin --keep-comments   # submit as-is
tools/make_submission.sh lab00 nelson-gatlin --strip-all       # drop DEVIATION too

# strip_comments.py is NOT executable and is not on PATH -- run it through the
# project interpreter. `tools/strip_comments.py file.py` gives Permission denied.
uv run --project dsp26 python tools/strip_comments.py <file>.py                    # preview one file
uv run --project dsp26 python tools/strip_comments.py <file>.py --keep 'PATTERN'   # keep extra
uv run --project dsp26 python tools/strip_comments.py <file>.py -o <out>.py        # write somewhere
```

The two shell scripts (`make_submission.sh`, `render_reports.sh`) **are** executable and run directly;
the two Python tools are not, and every invocation of them in these docs goes through
`uv run --project dsp26 python`.

---

## Before submitting, every time

Run these from `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`. Each line is a
command and the output that means it passed — not a feeling.

| # | Check | Command | Passes when |
| --- | --- | --- | --- |
| 1 | This lab's row above is filled in and confirmed | — | *Confirmed with TA?* is ✅. Otherwise ask, and meanwhile submit everything |
| 2 | ERAU ID is set | `grep -rn "myID" dsp26/src/` | prints `myID = 6127`, never `1234`. **Byte-identical figures are expected** — [KI-06](known_issues.md#ki-06--setting-your-erau-id-may-not-change-the-figures-at-all) |
| 3 | Figures exist and are distinct | `uv run --project dsp26 python tools/check_artifacts.py labNN/figs` | `OK    artifacts present, non-trivial, and distinct`. `figs/` is gitignored, so they may simply not exist |
| 4 | Report renders | `tools/render_reports.sh labNN` | `labNN/report.tex   OK  -> labNN/report.pdf` then `All rendered. PDFs kept (gitignored).` |
| 5 | The stripped copy still works | `tools/make_submission.sh labNN nelson-gatlin` | it prints a file list and does not abort. A lost `DEVIATION FROM HANDOUT` disclosure aborts it — [KI-14](known_issues.md#ki-14--naming-deviation-from-handout-in-a-docstring-aborts-packaging) |
| 6 | `--help` survived stripping | the three lines below — **not** "unzip the staging copy": `make_submission.sh` stages into a `mktemp -d` and deletes it on exit, so there is nothing left to open. Use the zip it wrote | every command still shows its description — [KI-08](known_issues.md#ki-08--stripping-docstrings-removes-typers---help-text) |
| 7 | Zip contents are clean | read the list step 5 printed | lab code only. **No `.venv`, no `tools/`, no `__pycache__`** |
| 8 | Live demo done | — | **Ryle** has seen it in person **by the next lab section** — either section's meeting counts, and you may demo and leave early. Failing that, a video demo sent before the meeting (**two allowed all semester**) |
| 9 | Team correct for this lab | — | teams rebuild every two labs from Lab 3; on ABET-artifact labs everyone submits independently |
| 10 | Uploaded within **1 week of the lab being assigned** | Canvas shows a submission timestamp | it is earlier than *assigned date + 7 days* — **not** merely earlier than the next meeting, which is a different rule and can be a later date. Lab dates: [`../README.md`](../README.md#schedule). **Late is a zero. No resubmission.** |

**Step 6 in full** — run it after step 5, from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

```sh
T=$(mktemp -d)
unzip -q labNN/dsp26-labNN-nelson-gatlin.zip -d "$T"
MPLBACKEND=Agg uv run --project "$T/dsp26" dsp26 --help ; rm -rf "$T"
```

`uv` builds a throwaway venv from the zip's own `uv.lock` (a few seconds; packages are cached), then
prints the help screen **of the stripped code the TA will receive**. Expected — verified 2026-09-08 on
`lab01/dsp26-lab01-nelson-gatlin.zip` — a `Commands` panel listing `plot-sinusoids-td-fd` and
`play-plot-audio`, **each with its description text beside it.** A command listed with a blank
description is KI-08 recurring: a docstring the CLI needed got stripped.

Steps 2–7 are yours to run and are not human work. **Steps 1, 8, 9 and 10 are the only ones that need
a person** — write them as blocks in the lab README, not as bullets.

---

**Related:** [`code_separation.md`](code_separation.md) · [`code_commenting.md`](code_commenting.md) · [`report_guide.md`](report_guide.md) · [`../prompt.md`](../prompt.md)
