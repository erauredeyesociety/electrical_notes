# 2026-09-08 — CESC 410 Lab 1 delivered, and the human-task standard that came out of it

**Seat:** PM2 Project-Lead · **Mode:** maintenance + coursework · **Outcome:** Lab 1 complete and demoed; a repo-wide standard for handing work to the human; three silent-failure classes closed

---

## What was done

### 1. CESC 410L Lab 1 — complete, demoed, submission-ready

Code, figures, report and the submission artifact. `dsp26` gained `lab1_audio_sig/` (the handout's
three files, transcribed) and `play-plot-audio` with the graded `--start-s` / `--end-s` options.
**Submission is one file: `lab01/lab01-artifacts-nelson-gatlin.pdf`**, 6 pages, 12/12 required
artifacts verified present. TA signed off on the demo.

Four deviations from the handout, each marked in source and explained in the report's Narrative: the
plotting helpers return their `Figure` (the only way to save headless); `play_audio` is skipped in
batch mode; a `--folder-name` writes figures to disk; figures save as PNG **and** SVG.

### 2. Three silent failures, found and closed

These are the session's real content. Each was invisible — no error, no warning, correct-looking
output — and each is now caught mechanically.

| Failure | How it presented | Now caught by |
| --- | --- | --- |
| A GUI window opened during an unattended run and blocked it **forever** | no output, no exit; reads like a hang in the DSP | `MPLBACKEND=Agg` gates the player ([KI-13](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md)) |
| A **stale** Overleaf copy compiles and looks right | you submit work that no longer matches your source | `flatten_tex.sh --check`, run automatically by `build_tex.sh` ([KI-18](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md)) |
| A "code" archive that is **93% dependency lockfile** | the file list looks entirely reasonable | `make_submission.sh` now prints a composition report |

The stale-copy check found a real leak on its first run: a committed flattened copy still carried
`% Generated from content/cesc_410/…` — a repo path inside a submitted document, the KI-09 class.

### 3. `docs/directives/human-task-instructions.md` — the standard

Ported from CEC 320's lab docs, which do this well, plus two rules those docs imply but never state.
Every human task now carries a **reason** from a closed vocabulary (GUI-only / Hardware / Credentialed
/ Capture / Judgment / Policy), absolute paths, and the five things: **WHERE / WHAT / VERIFY /
IF-ABSENT / BLOCKS**.

The two added rules are the ones that had actually failed:

- **Do the human's homework first, and show it.** The operator was told to fetch a WAV from Canvas
  without anyone first checking whether it could be obtained otherwise. It could — in about a minute.
- **Every blocking input gets a fallback**, with an honest urgent-vs-cosmetic call. Nothing was
  blocked; the lab ran fully on a stand-in. Knowing that would have changed how hard they looked.

Applied across all three current courses and into `lab_template.md`, so every future lab inherits it.

### 4. Every source `.tex` now says it cannot go to Overleaf

19 files across CESC 410 and 470 begin with `\input` and contained the word "overleaf" **zero** times.
The doctrine documented the rule; the file in the operator's hand did not. Each now opens with six
lines naming the error, the file to upload instead, and the regenerate command. `new_tex.sh` writes it
into every new file; `flatten_tex.sh` warns when a source lacks it.

---

## Decisions made

| Decision | Rationale |
| --- | --- |
| **The TA's supplied WAV is authoritative** | It is not the LibriSpeech audio its filename implies — different file, 10.00 s vs 7.43 s. A grader comparing figures expects theirs |
| **Submit one PDF, not the code zip** | The handout says so in one sentence. The zip is 93% `uv.lock`, 1.8% the *previous* lab's code |
| **Over-submitting is a default, not a policy** | Right when a handout is silent; wrong when it is explicit. Recorded repo-wide |
| **`--check` proceeds on an unmeasurable host, loudly** | Refusing would make the tool useless on the box the work runs on |
| **`figs_player/` is tracked; `figs_*/` are not** | A screenshot of a running GUI cannot be regenerated. Its siblings can |

---

## Discoveries

- **A filename that parses as a dataset id is not provenance.** `2086-149220-0033.wav` really is a
  LibriSpeech utterance id, the corpus really is public, and the file the TA shipped is neither.
  Sound reasoning, wrong conclusion — [KI-19](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md).
- **`DISPLAY` answers "could a window open?", never "should one?"** The first guard tested display
  availability; this machine has one, so a batch run opened a window and waited for a click.
- **Naming `DEVIATION FROM HANDOUT` in a docstring aborts packaging** — the marker is stripped with
  the docstring, so the guard correctly saw a lost disclosure ([KI-14](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md)).
- **The TA's audio is a 440.00 + 554.40 Hz dyad**, and the 0.4–1.4 s figure shows a clean beat at
  their 114.4 Hz difference — a better teaching signal than anything chosen here.
- **The spectrogram aliases its own display.** Frames at 100/s, Nyquist 50 Hz, so the 114.4 Hz
  envelope folds to 14.4 Hz — visible as ribbing, in a figure about sampling.

### Corrections to earlier work in this repo

| Claim | Reality |
| --- | --- |
| "a log axis makes a harmonic series evenly spaced" | Backwards. Harmonics space evenly on a **linear** axis and bunch on a log one |
| tones at 441.4 / 554.7 / 113.3 Hz | 440.00 / 554.40 / 114.40, measured |
| `figs_music/` reproduced byte-for-byte from `test_tone.wav` | False; regenerated from both and compared md5s |
| the report's PDFs are "byte-identical" after a comment-only edit | Impossible — tectonic stamps a fresh CreationDate. Pixel-identical is the provable claim |

---

## Blockers

- **pwnstar is down** (`No route to host`), so ResearchHub is unavailable. ZeroTier is online on this
  side; the host is not answering. Ollama and docs-rag are unaffected.
- **`nvidia-smi` is still broken on the skytracker GPU host** — reported to that team 2026-09-06.

---

## Next

1. **Upload `lab01-artifacts-nelson-gatlin.pdf` to Canvas** — due one week from assignment. The only
   outstanding item on this lab.
2. **CESC 470 and CPSC 462 have no labs yet.** Both now carry `shared_tools.md` and the submission
   rule, so their first assignment inherits the standard rather than rediscovering it.
3. `ocr_handler` M2 remains the leverage — retire the three per-course extractor scripts.

---

**See:** [../directives/human-task-instructions.md](../directives/human-task-instructions.md) ·
[../directives/coursework-solutions.md](../directives/coursework-solutions.md) ·
[../lessons_learned/lessons.md](../lessons_learned/lessons.md) ·
[../latex/INDEX.md](../latex/INDEX.md)
