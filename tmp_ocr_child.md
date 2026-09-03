# Scoping notes — lecture PDF extraction (prospective child project)

> **Status: discussion document. Nothing built.** Placed in the `electrical_notes` root deliberately — it is about work that should *leave* this repo.
>
> Written 2026-09-02 from measurements of the actual files, not from assumptions. Every number below is reproducible with the commands shown.

---

## The headline: this is mostly not an OCR problem

The request was "OCR the lecture PDFs." Having looked inside them, **only a fraction of one of three source types needs anything resembling OCR**, and even that part may be better solved by *not* recognising text at all.

That reframing is the main value of this document. Building an OCR pipeline first would solve the wrong problem.

### What is actually in the files

Measured on `content/cesc_410/lectures/`:

| | **Type A — born-digital LaTeX** | **Type B — slide deck** | **Type C — ink-annotated** |
| --- | --- | --- | --- |
| Example | `dsp-lctr1-…-26-08-26.pdf` | `f26_lctr02_DT signals….pdf` | `f26_lctr02_…-plw.pdf` |
| Producer | `pdfTeX` via pandoc + Eisvogel | `GPL Ghostscript 9.06` | **`PDF Annotator 10.0.0.1011`** |
| Pages | 12 | 10 | 10 |
| Text layer | **18,589 chars — rich** | **1,385 chars — thin** | +0 chars over base |
| Embedded images | 11 | 24 | 36 (**+12**) |
| Ink objects | 0 | 0 | **7 `/Ink`** |
| Equations | **real Unicode text** (`∑ ∫ 𝑒 𝑥 𝜋 𝜔` all extract) | images, ~130 ppi | — |
| Needs OCR? | **No** | Partly — for text inside figures | **No — it is vector ink** |

Reproduce:

```sh
pdfinfo FILE.pdf | grep -E 'Producer|Pages'
pdftotext FILE.pdf - | wc -c
pdfimages -list FILE.pdf | tail -n +3 | wc -l
```

### The three findings that change the design

**1. Type A equations extract as real text.** `pdftotext` on the LaTeX-built lecture yields `∑` ×10, `∫` ×9, `𝜋` ×47 and so on — genuine Unicode math characters, not images. Converting Unicode math → LaTeX is a *transformation* problem, not a recognition problem. Much easier, and lossless.

**2. Type C ink adds zero extractable text but is vector, not raster.** `diff` of base vs annotated text output is empty; the file carries **7 `/Ink` objects**, which are stroke coordinate paths. Handwriting here is *geometry*, not pixels.

**3. There are two different kinds of `-plw` file, and they are unrelated.** This is the biggest trap:

- `dsp-lctr1-…-plw.pdf` is the **LaTeX source recompiled** with typed additions. The diff shows words re-flowed into paragraphs (`"we need to"` → `"we need to do"`) and a note *"Will continue from here on 8/28/26."* Pixel diff: 0–446 px/page. **No handwriting at all.**
- `f26_lctr02_…-plw.pdf` is **PDF Annotator ink** over a slide deck. Pixel diff: 500–1,720 px/page.

**Detecting which kind you have must be step one of any pipeline.** They share a naming convention and nothing else. Producer string is the reliable discriminator.

---

## The insight worth arguing about

For Type C, **the goal may not be text at all.**

The stated need is *"hold [graphs and equations] as images to insert into markdown files for reports."* If the output is an image either way, then recognising handwriting into text is effort spent to then throw the text away.

A cheaper pipeline that may be strictly better:

1. Diff annotated against base, per page, to find *where* the instructor wrote.
2. Crop those regions at high DPI.
3. Emit an image plus a placeholder caption.
4. **Optionally** attempt recognition, as an enrichment, never as a dependency.

This yields something useful on day one and degrades gracefully. Handwriting recognition on maths is genuinely hard — and the instructor's annotations are exactly the hard case: mixed symbols, arrows, underlines, marginal scrawl.

**Counter-argument worth taking seriously:** text is searchable and images are not. If the point is to search *"which lecture covered convolution?"*, images fail. Likely resolution: the base PDF's text layer already answers search; ink only needs to be *located and shown*, not read.

This is the first thing to decide, because it determines whether the project is a weekend or a month.

---

## Output format: Markdown or LaTeX

Genuinely open. The honest answer is **both, from one intermediate** — but only if the intermediate is designed first.

| | Markdown | LaTeX |
| --- | --- | --- |
| Equations | needs a math extension; renders inconsistently | native, exact |
| Images | trivial | trivial |
| Diffable / greppable | **yes** | mostly |
| Feeds a lab report | needs conversion | **direct** |
| Feeds Hugo / notes site | **direct** | needs conversion |

Both consumers exist here: `cesc_410` reports are LaTeX ([`content/cesc_410/labs_and_projects/reference_docs/report_guide.md`](content/cesc_410/labs_and_projects/reference_docs/report_guide.md)), the notes site is Markdown.

**Suggested position:** extract to a **structured intermediate** (JSON/YAML per page: text blocks, equations, image refs, ink regions, coordinates) and render Markdown and LaTeX from it. Writing two extractors, or extracting to one format then converting, both end badly. The intermediate is the actual design work.

`pandoc` would do the format conversion (**not currently installed** — `sudo apt install pandoc`).

---

## Proposed scope

### In

- Classify a PDF: born-digital / slide-deck / ink-annotated.
- Extract the text layer where one exists, preserving structure.
- Extract embedded figures as image files with page/position metadata.
- Locate ink annotations by diffing against the base PDF; crop to images.
- Emit a structured intermediate; render Markdown and LaTeX from it.
- Pair base and `-plw` files automatically and report unpaired ones.

### Out (at least initially)

- **Handwriting recognition.** Enrichment, not a dependency. See above.
- **Full-page OCR.** No file examined needs it; every one has a text layer.
- Re-typesetting slide decks into clean documents.
- Anything requiring the instructor's original source.

### Uncertain — decide before building

- Unicode-math → LaTeX conversion. Tractable and high-value for Type A, but a rabbit hole.
- Whether Type B's low-resolution figures (127–151 ppi) are good enough to embed in a report, or need re-rendering from vector where the original is vector.

---

## Open questions

1. **How much Type C actually exists?** `cesc_410/lectures` has **1** ink-annotated file. `cec_320/lectures` has **25 lecture PDFs and zero `-plw`**. If this stays at one or two files a semester, cropping by hand beats building anything.
2. Does the instructor post annotated versions consistently, or was this one-off? Worth simply asking.
3. Is the real need *reading* lectures, or *quoting* them in reports? Different pipelines.
4. Does `cec_320`'s existing `LECTURE_INDEX.md` / `lctr27_summary.md` represent prior work worth generalising, or a dead end?
5. Do other courses (`ps160`, `stat_412`, `syse_301`) have scanned material that *does* need real OCR? **Nothing in `cesc_410` does.** If the genuine OCR need lives elsewhere, that changes the project.

---

## Separate concern: `electrical_notes` repository size

Related only in that it motivated moving this work out. Worth its own decision.

```
.git          625 MB
size-pack     450 MB
objects      1,948
```

Largest objects in history:

| Size | Path |
| ---: | --- |
| 55.9 MB | `content/ps160/m14/M14_textbook_chapter.pdf` |
| 49.4 MB | `content/ps160/m12/M12_textbook_chapter.pdf` |
| 47.8 MB | `content/ps160/m16/M16_textbook_chapter.pdf` |
| 40.0 MB | `content/ps160/m15/M15_Textbook_chapter.pdf` |
| 31.0 MB | `content/cec_320/labs_and_projects/lab03/lab03-Gatlin-Nelson.zip` |

**Observations.** Roughly 200 MB is four PS160 textbook chapters. A 31 MB submission zip is committed — exactly the class of build artifact now gitignored in `cesc_410`. The size is *content*, not history churn, so aggressive history rewriting is not obviously the fix.

**Options, cheapest first:**

| Option | Effect | Cost |
| --- | --- | --- |
| Leave it | 625 MB clone | none |
| Stop adding artifacts (already done for `cesc_410`) | halts growth | none |
| `git lfs migrate` for PDFs over ~10 MB | large drop; history preserved | rewrites history; everyone re-clones |
| `git filter-repo` to drop textbook chapters | ~200 MB drop | **destructive**; rewrites history; textbooks gone from history |
| Split courses into separate repos | small repos | loses single-clone convenience |

> ⚠ Every option below "stop adding artifacts" **rewrites history and requires a force-push.** Do not do it casually, and not while coursework is being actively submitted from this repo. Decide separately from the OCR project.

---

## If it becomes a child project

Per `~/llm-project-bootstrap` convention, existing children (`ptm`, `mentalmodel`) live at `<bootstrap>/<name>/docs/` with:

```
<name>/docs/
├── README.md
├── scope.md              # this document, promoted and tightened
├── roadmap.md
├── todo.md
├── lessons_inbox.md
└── findings/             # one file per investigated question
```

**Nothing here is a child project yet.** This is a scoping note. The first real decision — *recognise handwriting, or just locate and crop it?* — should be settled before any structure exists, because it changes what the project even is.

**Aggressive minimalism check:** if the answer to open question 1 is "one or two annotated PDFs a semester," the correct outcome is **no project at all** — a 20-line script in `electrical_notes` would do. That is a legitimate result and worth ruling in or out first.

---

## Commands used to gather the above

```sh
cd content/cesc_410/lectures
pdfinfo FILE.pdf | grep -E 'Producer|Pages|Page size'
pdftotext FILE.pdf - | wc -c
pdfimages -list FILE.pdf
pdffonts FILE.pdf
diff <(pdftotext base.pdf -) <(pdftotext annotated.pdf -)

# per-page visual delta, the test that separated Type A from Type C
pdftoppm -png -r 40 -f N -l N base.pdf /tmp/b
pdftoppm -png -r 40 -f N -l N annotated.pdf /tmp/p
compare -metric AE /tmp/b-*.png /tmp/p-*.png null:

# ink objects
python3 -c "d=open('annotated.pdf','rb').read(); print(d.count(b'/Ink'))"

# repo size
du -sh .git && git count-objects -vH
```
