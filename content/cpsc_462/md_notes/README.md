# CPSC 462 — class materials as Markdown

Text pulled out of [`../class_materials/`](../class_materials/) so it can be
read, searched, and grepped. **Generated — edit the source documents, not these.**

```sh
tools/extract_notes.py                    # rebuild anything out of date
tools/extract_notes.py --force            # rebuild everything
tools/extract_notes.py --only wireshark   # just one
tools/extract_notes.py --list             # show the plan, change nothing
```

---

## What's here

| Notes | Source used | Text quality |
| --- | --- | --- |
| [`introduction_to_wireshark.md`](introduction_to_wireshark.md) | `.docx` | ✅ **Full** — 19 KB, 8 figures extracted |
| [`application_layer.md`](application_layer.md) | `.pdf` (106 slides) | ✅ Good — 50 KB, 453 ch/slide |
| [`cs_462_syllabus_fall26.md`](cs_462_syllabus_fall26.md) | `.docx` | ✅ Full — 10 KB |
| [`introduction_cpsc_462.md`](introduction_cpsc_462.md) | `.pdf` (85 slides) | ⚠ 396 ch/slide — picture-heavy |
| [`intro_and_syllabus.md`](intro_and_syllabus.md) | `.pdf` (6 slides) | ⚠ 99 ch/slide — almost all images |

The two ⚠ decks are title/diagram slides with little real text. What is below
their warning banner is everything the text layer carries — **open the original
PDF for the diagrams.** They are flagged, not silently truncated.

## Wireshark

[`introduction_to_wireshark.md`](introduction_to_wireshark.md) is the lab
walkthrough and the most complete document here — it came from the `.docx`, so
it kept its formatting and its 8 figures. It covers packet-sniffer structure,
the capture library, the packet analyzer, and the HTTP capture exercise.

---

## How a source is chosen

Per document stem, best available wins:

| | | |
| --- | --- | --- |
| `.docx` | **preferred** | pandoc keeps headings, lists, and bold, and extracts embedded images as real files |
| `.pdf` | fallback | PyMuPDF, page by page, with `## Page N` markers |
| `.pptx` | **not used** | see below |

**Why `.pptx` is skipped.** Measured on this material, a deck's pptx text layer
is the same text its PDF already carries — *Application Layer*: 47,898 chars
from the pptx vs 47,990 from the PDF; *Intro and Syllabus*: 676 vs 600. pandoc
cannot read pptx at all (it only writes it), so using it would mean hand-parsing
slide XML for no gain. Where both exist, the PDF is the better source.

## Images

Extracted to `media/<slug>/` and **gitignored** — ~1.9 MB, and regenerable with
`--force`. The `.md` files are tracked.

---

**Related:** [`../class_materials/`](../class_materials/) · [`../tools/extract_notes.py`](../tools/extract_notes.py)
