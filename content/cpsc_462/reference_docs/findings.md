# CPSC 462 — reference notes

What was learned building and smoke-testing this course's scaffolding, kept so
it is not re-derived. Doctrine is
[`docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md);
this file records only what is specific to CPSC 462.

Last verified: **2026-09-05**, before any assignment existed.

---

## 1. The macros file sits at course level, not under `hw/`

```text
content/cpsc_462/
├── reference_docs/cpsc462_macros.tex   ← ONE file, all three kinds input it
├── hw/    prompt.md   hwNN/
├── qz/    qzNN/
├── exam/  examNN/
├── class_materials/   md_notes/   tools/
└── .gitignore                          ← ONE file, course-wide
```

### Why it moved

The doctrine writes the path as
`content/<course>/<kind>/reference_docs/<course>_macros.tex`, and this course
started that way. **That path only works for a course that has exactly one
kind.** CPSC 462 has three: the syllabus grades Assignments 30%, Quizzes 10%,
Examinations 30%, and the schedule names five quizzes and two exams (Exam 1 on
9/30/26, Exam 2 on 11/6/26). So `hw/`, `qz/` and `exam/` are siblings.

`new_tex.sh` finds the macros by walking **up** from the assignment folder,
running `find <probe> -maxdepth 2 -path '*/reference_docs/*_macros.tex'` at each
level. From `content/cpsc_462/qz/qz01` the walk reaches `content/cpsc_462`,
where `hw/reference_docs/cpsc462_macros.tex` sits **three** levels down — past
`-maxdepth 2`. It is never found, and the script exits with *"no
reference_docs/\*_macros.tex found at or above …"*. A quiz literally could not
be scaffolded.

The two alternatives were worse:

- **Copy the file into `qz/reference_docs/` and `exam/reference_docs/`.** The
  upward walk takes the *nearest* match, so a quiz and the homework it follows
  would compile against different notation with nothing raising an error —
  silent divergence in the one file whose job is consistency.
- **Point `qz/` at `../../hw/reference_docs/…` by hand.** Re-introduces exactly
  the hand-counted relative path `new_tex.sh` exists to eliminate, and makes
  quizzes structurally subordinate to homework for no reason.

At course level the file is two levels below `content/cpsc_462`, inside
`-maxdepth 2`, so all three kinds resolve it as `../../reference_docs/…` with no
change to the shared toolchain. Verified by scaffolding `hw99/`, `qz99/` and
`exam99/` — all three printed
`macros: ../../reference_docs/cpsc462_macros.tex`.

`hw/reference_docs/` is gone. A kind-specific reference doc (a submission
checklist, say) can still live in `hw/reference_docs/` later — just never a
second `*_macros.tex`, which is what breaks the walk.

---

## 2. One course-level `.gitignore`, whitelisting our build products

The old `hw/.gitignore` ignored `*.pdf` and negated the instructor's handouts by
guessed name (`!HW*.pdf`, `!Lab*.pdf`). That fails in the dangerous direction:
**anything not guessed is silently untracked.** This course's handouts are named
"Lab 0", "Introduction to Wireshark", "Hands on" — none match `HW*`.

The rule is now inverted. `build_tex.sh` writes `<basename>.pdf` beside each
`.tex`, and every `.tex` in an assignment folder is either `pNN_<slug>.tex` or
`<kind>NN_solutions.tex`, so our build products are exactly:

```gitignore
p[0-9][0-9]_*.pdf
*_solutions.pdf
```

Everything else — instructor PDFs, `.pcapng` captures, anything under
`class_materials/` — stays tracked by default. A stray build product in
`git status` is cheap; source material going missing is not.

Verified with `git check-ignore -v` over 19 representative paths across all three
kinds: build products and `overleaf/` ignored; handouts, captures, `.tex`,
`README.md` and `class_materials/*.pdf` tracked.

---

## 3. Macro review — what the course actually writes

Checked against `md_notes/`. The two load-bearing slides were **rendered and
looked at**, not read off the PDF text layer.

| Macro | Verdict | Evidence |
| --- | --- | --- |
| `\dnodal` `\dproc` `\dqueue` `\dtrans` `\dprop` | **kept** | `Introduction CPSC 462.pdf` p50–51 prints `dnodal = dproc + dqueue + dtrans + dprop`, `dtrans = L/R`, `dprop = d/s`, set as italic *d* with upright subscripts — exactly what `d_{\mathrm{...}}` gives |
| `\RTT` | **kept** | `Application Layer.pdf` p29: *"Non-persistent HTTP response time = 2RTT + file transmission time"*. Upright, used as a coefficient |
| `\field` | **kept** | packet-analysis course: field names (`Dest Port`, `TTL`) and display filters (`http.request.method == "GET"`) run through `introduction_to_wireshark.md` and must not read as prose or as a variable |
| `\Mbps` | **kept** | p33 prints `R = 100 Mb/s`. siunitx is loaded by the shared preamble but renders `\unit{\mega\bit\per\second}` as `Mbit s⁻¹`, which this course does not write |
| `\kbps` | **removed** | `kb/s` and `kbps` appear **nowhere** in the notes. Nearest hit is `L = 10 Kbits` (p32) — a quantity of bits, not a rate |
| `\ms` | **removed** | a generic unit shorthand, not networks notation. siunitx is already loaded and `\SI{0.1}{\milli\second}` renders `0.1 ms` correctly — confirmed in the smoke-test PDF |

The rule that fell out, worth reusing: **hand-roll a unit macro only where
siunitx's output disagrees with the course's own notation.** `Mb/s` yes, `ms` no.

### Considered and deliberately not added

Adding these now would be the anticipation the macros file forbids. Add one when
a **second** problem needs it:

- traffic intensity `La/R` — one slide
- bottleneck throughput `min(Rs, Rc)` — one slide
- a dedicated Wireshark display-filter macro — `\field` covers it today

### Trap: `d` is overloaded

On p51 the same letter is the delay symbol (`dprop`) *and* the physical link
length (`dprop = d/s`, "*d*: length of physical link"). A solution writing both
in one line must not let them collide. It is the course's own overload, so keep
it and be explicit rather than inventing a different symbol.

---

## 4. Citations: PDF page == printed slide number, for both decks

The doctrine warns that a deck's printed slide number usually differs from the
PDF page. **For these two decks it does not.** Every page was checked:

| Deck | Pages | Footer form | Agreement |
| --- | --- | --- | --- |
| `Introduction CPSC 462.pdf` | 85 | `Introduction: 1-N` | every page carrying a footer; p39 carries none |
| `Application Layer.pdf` | 106 | `Application Layer: 2-N` | every page carrying a footer; p72–73 carry none |

So `\srcref{Introduction, PDF p50, slide 1-50}` is unambiguous, and the two
numbers agreeing is a signal the citation is right rather than redundant noise.
**Re-check this for each new deck** — it is a property of these files, not a rule.

---

## 5. `tools/extract_notes.py` — verified, with one cosmetic caveat

All five documents re-extracted with `--force` into a scratch directory and
diffed against the tracked `md_notes/`:

- 4 of 5 byte-identical; media file list identical.
- `introduction_to_wireshark.md` differed **only** in the width of pandoc's
  table rule lines (`-----`). Identical once those are normalised.

Cause: pandoc's `--extract-media` writes **absolute** image paths and sizes a
simple table's rule to the longest cell, so the rule width depends on the length
of the output directory's absolute path. `extract_notes.py` strips the prefix
afterwards, by which point the dashes are already sized. Harmless — it is a rule,
not content — but the tracked file is only byte-reproducible when regenerated
**into `content/cpsc_462/md_notes`**. Don't chase a diff that is only dashes.

`md_notes/media/cs_462_syllabus_fall26/` is an empty directory pandoc creates for
a `.docx` with no embedded images. Harmless; `media/` is gitignored.

---

## 6. Link checking is programmatic

[`../tools/check_links.py`](../tools/check_links.py) resolves every relative
Markdown link under `content/cpsc_462/` and exits non-zero on a broken one.

```sh
content/cpsc_462/tools/check_links.py            # everything
content/cpsc_462/tools/check_links.py a.md b.md  # only these
```

It also flags a link whose target contains a space or parenthesis but is **not**
angle-bracketed. That form —
`[x](../class_materials/CS 462 Syllabus_Fall26.pdf)` — is not a valid link at all
in CommonMark and renders as literal text. Several class-materials filenames
contain spaces, so this is a live hazard here. The correct form wraps the target:
`[x](<../class_materials/CS 462 Syllabus_Fall26.pdf>)`.

Self-tested against a fixture carrying a broken target, an unbracketed space, a
correctly bracketed name containing parentheses, an anchor, a URL and a quoted
title. All six classified correctly.

---

## 7. Course facts worth having on hand

From [`../md_notes/cs_462_syllabus_fall26.md`](../md_notes/cs_462_syllabus_fall26.md):

- **Weights:** Assignments 30%, Examinations 30%, Final Report 20%, Class
  Participation 10%, Quizzes 10%.
- **Assignments are called "Hands on"** (plus "Lab 0"). That is what lands in
  `hw/` — do not expect a file named `HW1.pdf`.
- **Quizzes are named by topic, not numbered:** Quiz Application (9/9), Quiz
  Transport (9/16), Quiz Network 1 (9/28), Quiz Network 2 (10/14), Quiz Link
  Layer (10/26), Quiz Wireless (11/4). `qzNN` numbering therefore needs the topic
  recorded in the assignment `README.md`.
- **Exam 1** 9/30/26, **Exam 2** 11/6/26 — each covers material since the
  previous exam.
- Late work: one letter grade per 24 h, floored at 50.
- The decks are Kurose & Ross, re-branded; chapter number shows in the slide
  footer (`1-N` introduction, `2-N` application layer).

---

## 8. The packet capture is automatable — only *reading* it is not

**Found:** 2026-09-08, working out what a Wireshark hands-on would actually hand to a
human.

A Wireshark lab reads as one indivisible GUI procedure, and the handout writes it that
way: *"Start up the Wireshark software … select the Capture pull down menu …"*. Handing
that over whole would have moved the entire lab onto the operator. It splits:

| Half | Verdict | Why |
| --- | --- | --- |
| **Recording** the packets | **AUTOMATABLE** | `dumpcap` on this machine carries `cap_net_admin,cap_net_raw=eip` and the account is in group `wireshark` — headless, no `sudo`, no window |
| **Reading** the packets | `Capture`, human | the graded artefact is the expanded HTTP tree in the detail pane, and `tshark` is **not installed**, so nothing here can decode a frame |

Verified by capturing on `lo` with a BPF filter — four pings plus one HTTP request in,
eight ICMP frames out, the HTTP filtered away:

```text
Capturing on 'Loopback: lo'
Packets: 2 Packets: 6 Packets: 8 Packets captured: 8
Packets received/dropped on interface 'Loopback: lo': 8/0 (100.0%)
```

Two traps make a *correct* capture look empty, and both cost an hour if unwritten: the
browser silently upgrades the lab URL to HTTPS so no plain `GET` appears (the handout's
own fix uses `curl --http1.1`, and its command has a typo — `INTRO-wireshark-ile1.html`,
missing the `f`), and a live VPN puts the traffic on `tun0` while the capture watches
`wlo1`.

**Generalises:** the same shape as CESC 410's `MPLBACKEND=Agg` — a task is not human
because it *ends* in a window; it is human only for the part that *is* the window. The
operational detail is in [`human_tasks.md`](human_tasks.md) § H3.

---

**Related:** [`human_tasks.md`](human_tasks.md) — the human-facing hand-offs, with the
office-hour conflict, the capture interfaces and the searches already done ·
[`../hw/prompt.md`](../hw/prompt.md) ·
[`cpsc462_macros.tex`](cpsc462_macros.tex) ·
[`../../../docs/latex/INDEX.md`](../../../docs/latex/INDEX.md)
