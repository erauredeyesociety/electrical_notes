# Human tasks — CPSC 462

**The rules are shared; this file is only the coordinates.** Read
[`docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md)
first — it defines the six reasons a task may be human, the
WHERE / WHAT / VERIFY / IF-ABSENT / BLOCKS form, the Source (FROM) → Destination (TO)
rule, and the hand-off checklist. **None of that is repeated here**, deliberately: a
second copy would drift from the first.

What follows is only what the directive cannot know — *which* instructor, *which*
network interface, *which* binary is installed on this machine, and *what has already
been searched for so nobody searches twice.*

Everything below was verified on **2026-09-08** unless a line says otherwise.

> **No assignment has been issued yet.** Every task here is either a standing
> "when it lands, do this", or a fact established in advance so the first Hands-on does
> not stall. The one genuinely urgent item is H2 — the Canvas course id is unknown, and
> that is the WHERE for everything else.

---

## Course coordinates — the answer to every "WHERE"

| Thing | Value | Evidence |
| --- | --- | --- |
| Instructor | **Rumia Sultana** · `sultanr1@erau.edu` · (316) 305-3358 | [`../md_notes/cs_462_syllabus_fall26.md`](../md_notes/cs_462_syllabus_fall26.md) header table |
| Office | **LB 355** | same table |
| Office hours | **MWF 11am–12pm and 1–2pm**, or by appointment | same table |
| ⚠ Usable office hours | **the 1–2pm slot only.** CESC 470 meets MWF 11:00–11:50 in Lehman 369, so the 11am slot is a hard conflict. Do not walk to LB 355 at 11. | [`../../cesc_470/pdf_transcripts/cesc_470.md`](../../cesc_470/pdf_transcripts/cesc_470.md) p1 |
| TA | **none.** The syllabus prints a TA block with four empty fields — no name, no email, no office, no hours. | same table |
| LMS | Canvas. The syllabus names it twice (*"posted in Canvas"*) but **gives no URL and no course id** — see H2. | syllabus, Course Policies + Disclaimer |
| Late penalty | one letter grade per 24 h past the due date, **floored at 50**; unsubmitted counts 0 | syllabus, Course Policies |
| Weights | Assignments 30% · Examinations 30% · Final Report 20% · Participation 10% · Quizzes 10% | syllabus, Grading |
| Handout names | **"Hands on"**, **"Lab 0"** — never `HW1.pdf` | syllabus, Tentative Schedule |
| Exam dates | Exam 1 **9/30/26** · Exam 2 **11/6/26** | syllabus, Tentative Schedule |

The full dated schedule — six topic-named quizzes and every "Hands on due (if any)" —
is in the syllabus notes and is *not* copied here; read it there so there is one copy.

## What is installed on this machine — checked, not assumed

| Tool | State | Consequence |
| --- | --- | --- |
| `wireshark` 3.6.2 | `/usr/bin/wireshark` | the GUI exists; only needed for the parts that are genuinely visual |
| `dumpcap` 3.6.2 | `/usr/bin/dumpcap`, caps `cap_net_admin,cap_net_raw=eip`, and `devel` is in group `wireshark` | **captures run headless with no sudo** — see H3 |
| `capinfos` `editcap` `mergecap` `text2pcap` `rawshark` | installed (`wireshark-common`) | a capture can be summarised and trimmed without opening a window |
| **`tshark`** | **NOT installed** | packets cannot be *decoded* on the command line — see H5 |

```sh
command -v wireshark dumpcap tshark capinfos
getcap /usr/bin/dumpcap
id -nG | tr ' ' '\n' | grep wireshark
```

```text
/usr/bin/wireshark
/usr/bin/dumpcap
/usr/bin/capinfos
/usr/bin/dumpcap cap_net_admin,cap_net_raw=eip
wireshark
```

`tshark` is absent from that list — that is the finding, not an omission.

## Which interface to capture on

`dumpcap -D` lists **41** interfaces on this machine, most of them Docker bridges and
`veth` pairs. Only four matter:

| Interface | What it is | Use it when |
| --- | --- | --- |
| `wlo1` | Wi-Fi | the normal choice — this is what the lab means by "Wi-Fi" |
| `eno2` | wired Ethernet | if the machine is docked / on a cable |
| `tun0` | **a VPN tunnel** | ⚠ see below |
| `lo` | loopback | only for testing the capture pipeline itself |

⚠ **`tun0` is UP on this machine right now** (checked 2026-09-08). If a VPN is carrying
the traffic when the capture runs, the lab's HTTP request leaves through `tun0` and what
`wlo1` sees is encrypted tunnel packets — so the capture succeeds, records frames, and
contains **no HTTP GET at all**. That failure looks exactly like "the filter is wrong".

**Do not try to work out whether "the VPN is up" — ask the kernel which interface the
lab's own traffic will use.** `ip link show tun0` is no help here — run it right now and
it prints `state UNKNOWN` on an interface that is up, so it cannot tell you whether the
lab's traffic will actually take it. This is the check that can, and it is the only one
needed:

```sh
ip route get 128.119.245.12      # 128.119.245.12 = gaia.cs.umass.edu
```

```text
128.119.245.12 via 10.33.255.254 dev wlo1 src 10.33.141.15 uid 1000
    cache
```

**Whatever `dev` names is the interface to pass to `dumpcap -i`.** Today that is `wlo1`,
so `-i wlo1` in H3a is correct as written and nothing needs bringing down. If it ever
prints `dev tun0`, change the `-i` to `tun0` rather than hunting for a way to disconnect
the VPN — capturing on the interface the traffic actually uses is the fix, and it needs no
privileges and no reconnection.

## Already searched — do not repeat

| Question | Command run | Answer |
| --- | --- | --- |
| Is any "Hands on" or "Lab 0" handout on this machine? | `find /home/devel -iname '*hands*on*' -o -iname 'Lab 0*'` | **No.** Every hit was unrelated third-party source (`handshake.py`, `Handsontable.svg`). |
| Is there an existing capture to work from? | `find /home/devel -iname '*.pcapng' -o -iname '*.pcap'` | **No course capture.** Only test fixtures inside `ardupilot/` and `go/pkg/mod/`. |
| Does the syllabus give a Canvas URL or course id? | grepped the extracted `.docx` notes and all five class-materials PDFs for `instructure`, `courses/`, `http` | **No.** The only URLs in the whole set are `wireshark.org` and `gaia.cs.umass.edu`. |

---

## The register

### H1 · Fetch the "Hands on" / "Lab N" handout when one is assigned

**Why human:** `Credentialed`.

**WHERE.** Canvas (see H2 for the URL) → **Assignments**, then **Modules**, then
**Files**. ⚠ **Do not search for `HW`.** This instructor's handouts are called *"Hands
on"*, *"Lab 0"*, and topic names — the syllabus schedule proves it, and a file named
`HW1.pdf` will never appear.

**WHAT.** The folder does not exist yet; the `mkdir -p` is part of this step:

```sh
mkdir -p /home/devel/electrical_notes/content/cpsc_462/hw/hw01
```

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Downloads/<the instructor's filename>.pdf` | `/home/devel/electrical_notes/content/cpsc_462/hw/hw01/<same filename>.pdf` |
| a `.pcapng` shipped with the assignment, if any | the same folder — **captures are source material, not build products** |

`/home/devel/Downloads/` is where this machine's browser puts course files; the tracked
copies of `Introduction to Wireshark.docx` and `Application Layer.pptx` are still
sitting there. **Keep the instructor's filename, spaces and all** — the `.gitignore`
keeps it regardless (proved under *Closed tasks*), and renaming breaks citations.

**VERIFY.** Present, and git will keep it:

```sh
cd /home/devel/electrical_notes
ls -l content/cpsc_462/hw/hw01/
git check-ignore -v "content/cpsc_462/hw/hw01/Hands on 1.pdf" ; echo "exit=$?  (1 = kept, good)"
```

Exit **1** with no output means tracked. Any output names a rule that would have lost
the file — stop and report it.

**IF ABSENT.** The schedule marks most Hands-on deadlines *"(if any)"*, so "not posted"
is a normal state. Ask in class, or at LB 355 during the **1–2pm** slot. There is no TA.

**BLOCKS.** All work on that assignment. Nothing else — the scaffolding is proved and
the notes are extracted.

---

### H2 · Find the Canvas course id and record it here — *do this once, before anything else*

**Why human:** `Credentialed`. This machine holds no Canvas session and cannot look.

**Already tried.** Every class-materials file was searched for a URL; the syllabus is a
`.docx` and carries none (see the search table). The sibling course's syllabus was a
Canvas *print-out*, so its footer leaked the id — this one was not printed from Canvas,
so nothing leaked.

**WHERE.** `https://erau.instructure.com` → **Dashboard** → the **CS 462 / CPSC 462**
card. Open it and read the address bar: it will be
`https://erau.instructure.com/courses/<NNNNNN>`.

**WHAT.** Write the number down in **all four places below.** Filling in only the
coordinates table leaves three others still saying "Canvas", which is the category noun
this task exists to remove:

| # | File (absolute) | What to change |
| --- | --- | --- |
| 1 | `/home/devel/electrical_notes/content/cpsc_462/reference_docs/human_tasks.md` | the *Course coordinates* **LMS** row — replace *"gives no URL and no course id"* with `https://erau.instructure.com/courses/<NNNNNN>` |
| 2 | the same file | this H2 entry — set the `CPSC 462` row of the comparison table below, and change H2's title from *"Find …"* to *"Found: `<NNNNNN>`"* so nobody re-opens it |
| 3 | the same file | H1's and H6's **WHERE**, which both read *"Canvas (see H2 for the URL)"* — replace with the real URL |
| 4 | `/home/devel/electrical_notes/content/cpsc_462/hw/prompt.md` | the *Human-only* table, rows H1, H2 and H6 — same substitution |

Find every one of them with:

```sh
grep -rn 'Canvas' /home/devel/electrical_notes/content/cpsc_462/reference_docs/human_tasks.md \
                  /home/devel/electrical_notes/content/cpsc_462/hw/prompt.md
```

For comparison, the sibling course's row reads:

| Course | Canvas id | How it was obtained |
| --- | --- | --- |
| CESC 470 | 208698 | leaked in the syllabus PDF's print footer |
| CPSC 462 | **unknown** | must be read off the address bar — nothing on disk carries it |

**VERIFY.** The URL loads a course whose title contains **CS 462** or **CPSC 462** and
whose Files area contains `CS 462 Syllabus_Fall26.docx`. A number that opens a different
course is the wrong number.

**IF ABSENT.** If no CS 462 card is on the Dashboard, check **Courses → All Courses**
(unfavourited courses are hidden from the Dashboard). If it is genuinely not there, the
enrolment is the problem, not the URL — email `sultanr1@erau.edu`.

**BLOCKS.** Every other Credentialed task in this file states "Canvas" and cannot say
more until this is filled in. Nothing in the repo is blocked.

---

### H3 · The Wireshark capture — **most of this is not a human task**

**Why human:** `Capture` — *for the screenshot half only.*

This is the split the directive's Rule 1 asks for. The lab handout describes one
undifferentiated GUI procedure; it is really two jobs, and only the second needs a
person.

#### H3a — recording the packets: **AUTOMATABLE, no GUI, no sudo**

`dumpcap` is the capture engine Wireshark itself drives, and on this machine it already
carries `cap_net_admin,cap_net_raw=eip` with `devel` in group `wireshark`. So the
capture runs headless — but it needs its folder first.

⚠ **The destination folder does not exist yet, and `dumpcap` will not create it.** Run
without the `mkdir` and the capture starts, then dies on the write — a failure that reads
like a capture problem but is not:

```text
Capturing on 'Loopback: lo'
dumpcap: The file to which the capture would be saved
("…/content/cpsc_462/hw/hw01/intro_http.pcapng") could not be opened:
No such file or directory.
```

(Reproduced on 2026-09-08, exit 1.) So the `mkdir -p` is the first line of this task, not
a suggestion — the same one H1 runs, and running it twice is harmless:

```sh
mkdir -p /home/devel/electrical_notes/content/cpsc_462/hw/hw01
dumpcap -i wlo1 -f "host gaia.cs.umass.edu" -a duration:30 \
        -w /home/devel/electrical_notes/content/cpsc_462/hw/hw01/intro_http.pcapng
```

Check `-i wlo1` against `ip route get 128.119.245.12` first — see *Which interface to
capture on* above; today it prints `dev wlo1`, so `wlo1` is right.

And in a second terminal, while it runs:

```sh
curl --http1.1 http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html
```

The **capture filter** (`-f`, BPF, not a display filter) is not optional politeness: an
unfiltered capture on `wlo1` records every packet the machine sees, including other
people's traffic on a shared network. `host gaia.cs.umass.edu` keeps only the lab's own
exchange.

**Verified end to end on 2026-09-08**, on `lo` rather than `wlo1` so nothing left the
machine — same command, same flags:

```text
Capturing on 'Loopback: lo'
File: …/probe2.pcapng
Packets: 2 Packets: 6 Packets: 8 Packets captured: 8
Packets received/dropped on interface 'Loopback: lo': 8/0 (100.0%)
```

with `-f "icmp"` against four pings plus one HTTP request: the eight ICMP frames were
kept and the HTTP request was filtered out, which is the filter working.

⚠ **Two traps that make this look broken when it is not.**
1. **The browser silently upgrades to HTTPS**, so there is no plain `GET` to find. The
   handout says this at its step 9 and the fix is the `curl --http1.1` above.
   The handout's own command has a **typo** — it reads `INTRO-wireshark-ile1.html`,
   missing the `f`. Use `INTRO-wireshark-file1.html`. Reproduce the handout's version
   and it 404s.
2. **A live VPN** puts the traffic on `tun0`, not `wlo1` — see *Which interface* above.

#### H3b — reading it: **HUMAN, reason `Capture`**

What the assignment actually grades is the *view*: the packet-detail pane with the HTTP
tree expanded and Frame/Ethernet/IP/TCP collapsed, the display filter box showing
`http`, the Dest Port field visible. That is a window, and there is no headless route
to it while `tshark` is missing (H5).

**WHERE.** Open the capture the automatable half already produced — this is *not* a new
capture, do not start one from the GUI:

```sh
wireshark /home/devel/electrical_notes/content/cpsc_462/hw/hw01/intro_http.pcapng &
```

**WHAT.** Follow the handout,
[`../md_notes/introduction_to_wireshark.md`](../md_notes/introduction_to_wireshark.md),
from its step 8 onward — steps 1–7 are the capture, already done:

| Step | Do this in the window |
| --- | --- |
| filter | type `http` in the display-filter bar and press Enter |
| select | click the `GET /wireshark-labs/INTRO-wireshark-file1.html` row |
| expand | open **Hypertext Transfer Protocol** in the detail pane; collapse Frame, Ethernet II, IPv4, TCP |
| read off | Dest Port from the TCP layer; the server IP; the GET→200 OK time delta |
| screenshot | the whole Wireshark window, once per figure the report needs |

**VERIFY.** Before opening anything, confirm the file is a real capture with packets in
it:

```sh
capinfos /home/devel/electrical_notes/content/cpsc_462/hw/hw01/intro_http.pcapng
```

Expected shape (this is real output from the verification capture):

```text
File type:           Wireshark/... - pcapng
File encapsulation:  Ethernet
Number of packets:   8
Capture duration:    0.910161533 seconds
```

`Number of packets: 0` means the filter or the interface was wrong — fix that before
opening the GUI, not after.

**IF THERE IS NO GET IN THE LIST.** In order: (1) the HTTPS upgrade — rerun H3a with
`curl --http1.1`, not the browser; (2) the wrong interface, VPN or otherwise — run
`ip route get 128.119.245.12` and re-capture with `-i <whatever it prints after dev>`
(**not** `ip link show tun0`, which reports `state UNKNOWN` either way and tells you
nothing); (3) if that still yields nothing, `dumpcap -D` lists all 41 interfaces — only
`wlo1`, `eno2`, `tun0` and `lo` are worth trying, the rest are Docker bridges and `veth`
pairs. **Fallback:** the handout
links a reference capture at `gaia.cs.umass.edu/wireshark-labs/`; using it instead of
your own trace is a **deviation** and must be said in the report, because several of the
questions ask for *your* machine's address.

**BLOCKS.** Only the figures and the packet-level answers. Nothing else — and H3a should
already have run before the human is asked for anything.

---

### H4 · Screenshots for the report

**Why human:** `Capture`.

**WHERE / WHAT.** From the Wireshark window opened in H3b. Save into a folder created
alongside the assignment:

```sh
mkdir -p /home/devel/electrical_notes/content/cpsc_462/hw/hw01/figs
```

**Which screenshot tool — checked on this machine, 2026-09-08.** `gnome-screenshot`,
`flameshot`, `scrot`, `maim`, `spectacle` and `shutter` are all **absent**; do not go
looking for them. Two routes exist, and Route A is better because it writes straight to
the final filename and skips the rename:

*Route A — command line, ImageMagick `import` (`/usr/bin/import`, ImageMagick 6.9.11).*
Run the line; the cursor becomes a crosshair; **click once anywhere inside the Wireshark
window** and that whole window is written to the filename you gave. No rename step, and
no `xdotool` — that one is **not** installed here:

```sh
import /home/devel/electrical_notes/content/cpsc_462/hw/hw01/figs/q04_tcp_dest_port.png
```

*Route B — GNOME's built-in.* The session is `ubuntu:GNOME` on X11 (GNOME Shell 42.9), so
**PrtScn** opens the screenshot UI and **Alt+PrtScn** grabs the focused window directly.
GNOME writes to `/home/devel/Pictures/Screenshots/` — which already exists and already
holds files named `Screenshot from 2026-07-25 23-51-20.png` — so this route always needs
a move:

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Pictures/Screenshots/Screenshot from ….png` | `/home/devel/electrical_notes/content/cpsc_462/hw/hw01/figs/qNN_<what it shows>.png` |

**Name each file for what it shows, not for when it was taken** — `q04_tcp_dest_port.png`
beats `Screenshot from 2026-09-08 12-23-37.png`, which tells a future reader nothing and
sorts by accident. Route A gets this right for free; Route B needs the `mv`.

**VERIFY.**

```sh
ls -l /home/devel/electrical_notes/content/cpsc_462/hw/hw01/figs/
```

one file per figure the report `\includegraphics`es, and no file the report never uses.

**IF THE WINDOW WILL NOT FIT.** Screenshot the panes separately rather than shrinking
the window — a 12 pt field name that is unreadable in the PDF is a lost point.

**BLOCKS.** Only the figures. The prose, the numbers read from `capinfos`, and the LaTeX
build do not wait on them.

---

### H5 · Install `tshark` — *one command, and it removes a whole class of human task*

**Why human:** `Policy` — it needs `sudo`, and package installation is not something an
agent does here.

**What it buys.** `tshark` is the command-line Wireshark: with it, "which protocols
appear", "what is the Dest Port", "how long between GET and 200 OK" all become
greppable, scriptable, checkable answers instead of things a person reads off a window.
Without it, `dumpcap` can *record* packets but nothing on this machine can *decode*
them, so every analysis question routes through the GUI.

**WHERE / WHAT.** Any terminal. On this Ubuntu box `wireshark-common` 3.6.2 is already
installed, and `tshark` is a separate Debian package of the same version:

```sh
sudo apt install tshark
```

⚠ **Not run from here** — this is the one command in this file that was *not* executed
and verified, because it needs root. It is written out so the human does not have to
work out the package name; `apt` will name any dependency it wants before proceeding.

**VERIFY.**

```sh
tshark -v | head -1
```

should print `TShark (Wireshark) 3.6.2 …`, matching the `dumpcap -v` already on the
machine. A version mismatch means a second Wireshark got installed from elsewhere.

**IF IT FAILS.** `apt` may ask whether non-superusers should be allowed to capture —
answer **Yes**; the machine is already configured that way (`devel` is in group
`wireshark` and `dumpcap` has the capabilities), and answering No would revoke it and
break H3a.

**BLOCKS.** Nothing today. It is an enabler: every future packet-analysis question stays
a `Capture` human task until this is done.

---

### H6 · Confirm the submission form for the first assignment

**Why human:** `Credentialed` + `Judgment`.

**Already tried.** The syllabus states weights, late penalties and dates but **never
says what to submit or in what format** — no page count, no file type, no naming
convention, no mention of a zip. Unlike CESC 470 it does not even fix "PDF". With no
assignment handout on disk, there is nothing further to read.

**WHERE.** Canvas (H2) → **Assignments** → the Hands-on item → the *Submission Details*
block and any rubric.

**WHAT.** Record the answer in the assignment's own README — the absolute path is
`/home/devel/electrical_notes/content/cpsc_462/hw/hw01/README.md` — not here, because it
may differ per assignment. That file does not exist yet either; H1's `mkdir -p` creates
the folder, and this is a plain new file:

```sh
mkdir -p /home/devel/electrical_notes/content/cpsc_462/hw/hw01
nano /home/devel/electrical_notes/content/cpsc_462/hw/hw01/README.md
```

(`nano`, `vi` and `gedit` are installed here; `vim` is not, and `$EDITOR` is unset — so
`$EDITOR <file>` does **not** work on this machine.)

Note especially whether the `.pcapng` itself is submitted alongside the report; this
course ships captures and several networking courses ask for them.

**VERIFY.** The Canvas page names a file type and a count. If it says only "upload your
work", that is not an answer — ask.

**IF ABSENT.** Email `sultanr1@erau.edu`, or LB 355 during the **1–2pm** slot. There is
no TA to ask.

**BLOCKS.** Only the upload.

---

### H7 · Record which topic each `qzNN` is — **standing; nothing to do today**

**Why human:** `Judgment` — trivial, but nobody else can decide it.

⚠ **There is nothing to do right now, and that is expected.**
`/home/devel/electrical_notes/content/cpsc_462/qz/` today holds only its own `README.md`
— no `qz01/`, no `qzNN/` of any kind, because no quiz has been given. This entry fires
the first time a quiz folder is created, not before. Do not go looking for folders that
are not there.

The quizzes are **named by topic and not numbered**: Quiz Application (9/9), Quiz
Transport (9/16), Quiz Network 1 (9/28), Quiz Network 2 (10/14), Quiz Link Layer
(10/26), Quiz Wireless (11/4). The folders will be `qz01`, `qz02`, … so the mapping has
to be written down or it is lost.

**WHERE.** `/home/devel/electrical_notes/content/cpsc_462/qz/qzNN/README.md`, one per
quiz folder, at the top of the file.

**WHAT.** One line, e.g. `Quiz Transport — 9/16/26`.
[`../qz/README.md`](../qz/README.md) already says to do this; this entry exists so it is
on the human list rather than only in a recipe.

**VERIFY.** Written so it behaves whether or not any folder exists yet — a bare
`head -3 …/qz/*/README.md` fails with `cannot open … No such file or directory` today,
which looks like a fault and is not:

```sh
find /home/devel/electrical_notes/content/cpsc_462/qz -mindepth 2 -name README.md \
  -exec head -3 {} +
```

Today it prints **nothing**, and empty output is the correct answer. Once quizzes exist,
every folder listed must show a topic and a date.

**IF ABSENT.** If a `qzNN/` exists but you cannot tell which quiz it is, the dated list
above is the key — match by date. If that fails, ask in class or at LB 355 during the
**1–2pm** slot; there is no TA.

**BLOCKS.** Nothing. It costs five seconds now and an archaeology session later.

---

## Closed tasks — kept so they are not re-opened

### ✅ "Will a `.pcapng` or an oddly-named handout be lost by `.gitignore`?" — closed 2026-09-08

Checked rather than assumed:

```sh
cd /home/devel/electrical_notes
git check-ignore -v "content/cpsc_462/hw/hw01/Hands on 1.pdf"
git check-ignore -v "content/cpsc_462/hw/hw01/capture.pcapng"
```

Both produce **no output and exit 1** — kept. The ignore rules are a whitelist of *our*
build products (`p[0-9][0-9]_*.pdf`, `*_solutions.pdf`, `overleaf/`), so a handout named
"Hands on", "Lab 0" or anything else survives, and so does a capture. Reasoning:
[`findings.md`](findings.md) §2.

### ✅ "Does capturing packets need root?" — closed 2026-09-08, it does not

`getcap /usr/bin/dumpcap` returns `cap_net_admin,cap_net_raw=eip` and `devel` is in
group `wireshark`. A headless capture was run and produced 8 packets. No `sudo`, no
GUI, no human. This is what moved H3a off the human list.

---

**Related:** [`findings.md`](findings.md) ·
[`../hw/prompt.md`](../hw/prompt.md) ·
[`../md_notes/introduction_to_wireshark.md`](../md_notes/introduction_to_wireshark.md) ·
[`../md_notes/cs_462_syllabus_fall26.md`](../md_notes/cs_462_syllabus_fall26.md) ·
[`../qz/README.md`](../qz/README.md) · [`../exam/README.md`](../exam/README.md) ·
[`../../../docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md) ·
sibling register: [`../../cesc_470/reference_docs/human_tasks.md`](../../cesc_470/reference_docs/human_tasks.md)
