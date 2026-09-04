# Claude entry point — CPSC 462 homework

**Trigger:** *"`hwNN/` now exists with the assignment in it, work it."*

**Read [`docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md) first.**
That is the doctrine — the two-document rule, the citation rule, the verification
rule, the per-assignment checklist. Shared by every course under the doctrine and
not repeated here.

This file carries **only what is specific to CPSC 462.**

> **Nothing has been assigned yet.** This folder is scaffolding: the macros file
> and `.gitignore` are in place and smoke-tested, so the first assignment can be
> worked immediately.

---

## The course

**Computer Networks** · Fall 2026 · currently working through **Wireshark**.

Syllabus: [`../class_materials/CS 462 Syllabus_Fall26.pdf`](<../class_materials/CS 462 Syllabus_Fall26.pdf>)
→ extracted at [`../md_notes/cs_462_syllabus_fall26.md`](../md_notes/cs_462_syllabus_fall26.md)

---

## What to cite

**Cite [`../md_notes/`](../md_notes/), not `../class_materials/`.** The notes are
extracted from the source `.docx`/`.pdf` by
[`../tools/extract_notes.py`](../tools/extract_notes.py) and keep headings and
figures; citing them means the citation is greppable.

| Notes | Source | Quality |
| --- | --- | --- |
| [`introduction_to_wireshark.md`](../md_notes/introduction_to_wireshark.md) | `.docx` | ✅ full, 7 figures |
| [`application_layer.md`](../md_notes/application_layer.md) | 106-slide PDF | ✅ 453 ch/slide |
| [`cs_462_syllabus_fall26.md`](../md_notes/cs_462_syllabus_fall26.md) | `.docx` | ✅ full |
| [`introduction_cpsc_462.md`](../md_notes/introduction_cpsc_462.md) | 85-slide PDF | ⚠ 396 ch/slide — picture-heavy |
| [`intro_and_syllabus.md`](../md_notes/intro_and_syllabus.md) | 6-slide PDF | ⚠ 99 ch/slide — almost all images |

The two ⚠ decks carry little text. **Open the original PDF for their diagrams**
rather than citing a page you have not seen.

Re-extract after new material lands:

```sh
content/cpsc_462/tools/extract_notes.py          # rebuild what is out of date
content/cpsc_462/tools/extract_notes.py --list   # show the plan, change nothing
```

---

## Macros

Shared preamble plus [`reference_docs/cpsc462_macros.tex`](reference_docs/cpsc462_macros.tex):

| Macro | For |
| --- | --- |
| `\dnodal` `\dproc` `\dqueue` `\dtrans` `\dprop` | the four delay components and their sum |
| `\Mbps` `\kbps` `\ms` `\RTT` | link rates and times |
| `\field{TTL}` | a protocol header field |

Kept deliberately small — **add a macro when a second problem needs the same
notation, not in anticipation.**

CPSC 462 assignments are not known to state learning outcomes, so use the
three-argument `\problemheader{n}{pts}{title}`. Switch to `\problemheaderlo` if
an assignment does state them.

---

## Watch for

**This course may ship packet captures or code**, unlike the pure-paper courses.
The directive says homework rarely needs a zip — check that assumption here
before relying on it. A `.pcapng` referenced by a solution is source material,
not a build product: keep it, and add a `.gitignore` negation if needed.

---

## Human-only

Everything in the directive's Human-only table. Submission form is
**unconfirmed** — no assignment has been seen yet.
