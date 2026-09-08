# TA supplemental reference — Lab 1

**What this is:** a plain-text transcript of the one-page PDF the TA calls the *"supplemental
reference document"* in [`ta_announcement_lab1_and_future_labs.md`](ta_announcement_lab1_and_future_labs.md).
Transcribed so the text is greppable; **the PDF is the original and carries the screenshot.**

| | |
| --- | --- |
| Source | Canvas → the CESC 410/510 course site → the **Lab 1** page, uploaded alongside the announcement |
| Original filename on Canvas | `CESC410L_Lab1.pdf` |
| Saved as | [`ta_supplement_lab1_reference.pdf`](ta_supplement_lab1_reference.pdf) — 1 page, unmodified |
| Retrieved | 2026-09-08 by the operator |
| Author | the lab TA, Ryle (the screenshot's paths are `C:\Users\rylet\CESC410L\projects\dsp26\…`) |

Extracted with `pdftotext -layout lab01/ta_supplement_lab1_reference.pdf -` — rerun that to check this
transcript against the original.

---

## Transcript

> For app_cli.py, make sure you leave everything in there alone – simply copy and paste the new
> content. I have also added the updated app_cli.py file to canvas.
>
> If you have build errors, go here and download the installer:
> https://visualstudio.microsoft.com/visual-cpp-build-tools/
>
> Then Run the installer and check Desktop development with C++ in the workload list.
>
> Then click install and wait
>
> Then open up a new powershell and run pip install -e .
>
> For the .wav file, download the .wav file I gave you then make sure it is under audio_files like
> this: projects\dsp26\audio_files\2086-149220-0033.wav
>
> When it works, it should look something like this:

…followed by a single screenshot, described below.

---

## The screenshot on that page

One 1299×517 image, a Windows PowerShell window with a Tk **Audio Player** window overlapping its
right-hand side. **It is the TA's screen, not ours** — it can be read as a target, and it must never
be submitted as one of our artifacts.

**Terminal half** (paths truncated by the overlapping window):

```
PS C:\Users\rylet\CESC410L\projects\dsp26> uv run python src\dsp26\la…
        Built dsp26 @ file:///C:/Users/rylet/CESC410L/projects/dsp26
        Built simpleaudio==1.0.4
Uninstalled 1 package in 12ms
Installed 25 packages in 1.06s
Generated WAV file at: C:\Users\rylet\CESC410L\projects\dsp26\audio_f…
PS C:\Users\rylet\CESC410L\projects\dsp26> dsp26 play-plot-audio
The basic frequency is 5.0 Hz.
Loading: C:\Users\rylet\CESC410L\projects\dsp26\audio_files\2086-1492…
Duration: 10.00 seconds

Detailed properties of C:\Users\rylet\CESC410L\projects\dsp26\audio_f…
Number of channels: 1
Sample width (bytes): 2
Frame rate (sample rate): 16000
Number of frames: 160000
Duration (seconds): 10.0
```

**Audio Player half** — a Tk window, title bar **`Audio Player`**:

| Element | Text |
| --- | --- |
| Line 1 | `Playing: 2086-149220-0033.wav` |
| Line 2 | `Duration: 10.00 seconds` |
| Buttons, row 1 | **Play** · **Pause** · **Resume** |
| Button, row 2 | **Exit** (centred under Pause) |

---

## What it settles, and the one difference that is not a defect

Our run of `dsp26 play-plot-audio` against the TA's `.wav` prints **the same header block** —
`1` channel, sample width `2`, `16000` Hz, `160000` frames, `10.0` s. Verified 2026-09-08; see
[`README.md`](README.md) § *Reproduce*.

**`The basic frequency is 4.0 Hz.` vs the TA's `5.0 Hz.` is correct and must not be "fixed".** That
line is Lab 0's module-level print, and the number is derived from the per-student `myID` seed. Ours
is `6127` ([`../reference_docs/submission_requirements.md`](../reference_docs/submission_requirements.md)
§ *Student ID*); the TA's is theirs. A run that printed `5.0` here would mean the seed had been
overwritten with someone else's.

Two lines in the TA's terminal have no counterpart in ours, and neither is a problem:

- `Generated WAV file at: …` — the TA ran a WAV-generator script of their own under
  `src\dsp26\lab1_audio_sig\`. **No such script is in the handout or in our package**, and none is
  required: the finished `.wav` was uploaded to Canvas and is what we use.
- `Built simpleaudio==1.0.4` / `Installed 25 packages` — a first `uv run` on Windows compiling
  `simpleaudio`. Ours is already built and in sync.
