# What each lab actually requires

> ⚠ **This is the biggest open question in the whole setup, and it is not resolved.** What a lab submission consists of is **not uniform** and has not been confirmed with the TA. Do not assume every lab wants code, or a report, or figures. **Confirm per lab, and record the answer here.**

---

## What we actually know

| Source | Says |
| --- | --- |
| **CESC 410L course info** | *"Please submit the report and code of the old lab before coming to the lab meeting of the new one."* — so **report + code** is the general rule |
| | *"Although you are required to submit lab reports, the report will not be assessed before the ATs can see your live demo of the lab."* — the **demo gates the report** |
| | One submission per team, **except ABET-artifact labs**, where every student submits independently |
| | **Late reports are not accepted. Missing report = 0. No resubmission.** |
| **Lab 0 handout** | *"This is Lab 0, and the submission is only for a testing if you can run the project. The focus of this submission is the screenshot of the four figures."* |

**Those two disagree for Lab 0**, and that disagreement is the point of this file. The course info says report+code; the Lab 0 handout says the focus is four screenshots. The handout is more specific and more recent, so it probably governs — but *probably* is not good enough when late means zero.

**Ask the TA at the first meeting.** Then fill in the table below.

---

## Per-lab requirements

Fill in as each is confirmed. `?` means unconfirmed — treat it as "produce everything and ask."

| Lab | Figures | Code | Report | Confirmed with TA? | Notes |
| --- | --- | --- | --- | --- | --- |
| 00 | ✅ **the four PNGs — this is the whole submission** | ❌ no | ❌ no | ✅ per handout | *"The focus of this submission is the screenshot of the four figures... these figures can be saved to files using an option of the command."* Saving is sanctioned, so the PNGs are the screenshots |
| 01 | ? | ? | ? | ❌ | |

---

## Questions to ask

1. ~~For Lab 0 — is the four-figure screenshot the whole submission?~~ **Resolved: yes, four figures only.** The handout is explicit and it governs over the course info's general report+code rule. *Still worth confirming the general rule for Lab 1 onward.*
2. Is the report format the same four-section template used in CEC 320 (Introduction / Narrative / Artifacts / Discussion & Results)? Is there a CESC 410L template posted?
3. When code is submitted, what form — a zip of the package, individual `.py` files, or pasted into the report?
4. Should the *whole* `dsp26` package be submitted each time, or only that lab's subpackage?
5. Is a PDF report required, or is another format accepted? (We author `.tex` and can produce either.)
6. Which labs collect **ABET artifacts** — those require independent individual work and separate submissions.

---

## Student ID

| | |
| --- | --- |
| ERAU student ID | **2636127** |
| Last 4 digits (`myID`) | **6127** |

The last four digits seed each lab's RNG, so the value lives in the lab source:

```sh
grep -rn "myID" dsp26/src/          # currently: recipes.py, myID = 6127
```

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
tools/strip_comments.py file.py                                 # preview one file
tools/strip_comments.py file.py --keep 'PATTERN'                # keep extra
```

---

## Before submitting, every time

- [ ] **This lab's row above is filled in and confirmed** — otherwise ask first
- [ ] ERAU ID set (`grep -rn myID dsp26/src/`) and figures regenerated
- [ ] Live demo done, or a video demo sent (**two allowed all semester**)
- [ ] Figures regenerated — `figs/` is gitignored, so they may not exist
- [ ] Report renders — `tools/render_reports.sh labNN`
- [ ] If code is being submitted: `dsp26 --help` still works on the *stripped* copy (KI-08)
- [ ] Zip contents checked: lab code only, no `.venv`, no `tools/`
- [ ] Team correct for this lab (teams rebuild every two labs from Lab 3)
- [ ] Submitted **before the next lab meeting** — late is a zero

---

**Related:** [`code_separation.md`](code_separation.md) · [`code_commenting.md`](code_commenting.md) · [`report_guide.md`](report_guide.md) · [`../prompt.md`](../prompt.md)
