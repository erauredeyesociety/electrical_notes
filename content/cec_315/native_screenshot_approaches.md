# Native / minimal-dependency ways to capture `<div class="page">` as PNG

Context: `exam3_cheatsheet_v10.html` renders a CSS Grid page with tables and
KaTeX math (inline SVG + custom fonts). `html-to-image` produces a blank white
PNG because its foreignObject trick can't embed the remote KaTeX font faces
or the KaTeX SVGs reliably. The user serves the file via
`python3 -m http.server`, Chromium is installed, and `check_pages.sh` already
uses `google-chrome --headless --print-to-pdf`.

---

## 1. `getDisplayMedia()` + canvas

Prompts the user to pick a window/tab/screen, returns a `MediaStream`, you
grab a frame onto a canvas and export PNG.

- Pros: 100% WYSIWYG — whatever the browser actually paints is captured, so
  KaTeX fonts, SVGs, everything looks right.
- Cons: Picker prompt every click; you can't automatically crop to just
  `.page` (you capture whole tab/window, then must crop via
  `getBoundingClientRect()`); Firefox/Safari support differs; requires HTTPS
  or localhost (localhost OK here).

```js
const s = await navigator.mediaDevices.getDisplayMedia({preferCurrentTab:true});
const track = s.getVideoTracks()[0];
const bmp = await new ImageCapture(track).grabFrame();
track.stop();
const r = el.getBoundingClientRect();
const c = new OffscreenCanvas(r.width*devicePixelRatio, r.height*devicePixelRatio);
c.getContext('2d').drawImage(bmp, r.left*devicePixelRatio, r.top*devicePixelRatio,
  r.width*devicePixelRatio, r.height*devicePixelRatio, 0,0,c.width,c.height);
const blob = await c.convertToBlob({type:'image/png'});
```

Picker cannot be suppressed. Chrome 107+ has `preferCurrentTab:true` which
defaults the picker to the current tab (one extra click).

## 2. `window.print()` + PDF → image

A button sets a print style that hides everything except the target `.page`,
calls `window.print()`, user saves as PDF, then runs `pdftoppm -png`.

- Pros: Pure CSS, no JS library, perfect fidelity (print stylesheet can even
  force single-page layout).
- Cons: Two manual steps (save PDF, run converter). Not "one click".

```css
@media print { body * { visibility:hidden; } .page.selected, .page.selected * { visibility:visible; } .page.selected { position:absolute; left:0; top:0; } }
```

## 3. CSS Paint API / Houdini

Not applicable. Paint worklets draw into CSS backgrounds; they can't read or
serialize sibling DOM. Skip.

## 4. Hand-rolled SVG `<foreignObject>`

This is what html-to-image does internally: inline the element into a
`<foreignObject>`, inline all CSS, rasterize via `<img>` → canvas. The blank
output is usually caused by (a) CORS-tainted KaTeX webfonts not getting
inlined as data: URIs, and (b) Chrome silently refusing to paint
foreignObject when any stylesheet/font fails CORS.

- Pros: Pure client-side, no picker, no server.
- Cons: You inherit the exact same bug. Getting KaTeX fonts into the SVG
  requires fetching `KaTeX_*.woff2`, base64-encoding, and injecting
  `@font-face src:url(data:font/woff2;base64,...)` into the foreignObject's
  `<style>`. Doable but ~60 lines, and you're still fighting browser quirks.

## 5. MediaRecorder + canvas captureStream

Skipped per instructions — requires already rendering DOM to canvas.

## 6. Programmatic "Copy image" trick

No. "Copy image" only appears on `<img>`/`<canvas>`/`<video>` elements. You'd
have to first produce an `<img>` (which requires solving the same rendering
problem). `contenteditable` doesn't enable it. Dead end.

## 7. Browser extension

Skipped per user.

## 8. Manual canvas drawing (walk DOM, fillText each node)

- Pros: No library.
- Cons: Nightmare. You'd reimplement CSS layout: grid tracks, table column
  widths, line wrapping, baselines. KaTeX is the killer — it's hundreds of
  nested spans positioned via em-scale CSS transforms plus inline SVGs for
  surds/braces. You are writing a browser. Do not attempt.

## 9. DOM → data-URL SVG

Same as #4. `<svg><foreignObject>...</foreignObject></svg>` encoded as
`data:image/svg+xml;utf8,...` drawn into an `<img>`. Same font/CORS trap.

## 10. Headless Chromium server-side (RECOMMENDED)

`check_pages.sh` already does `google-chrome --headless --print-to-pdf`, so
the pipeline is proven on this machine. Wrap it in a tiny Python HTTP server
alongside (or replacing) `python3 -m http.server`. The HTML gets a button
that calls `/render?page=1` and downloads the returned PNG.

- Pros: Uses Chromium's real renderer — pixel-identical to what the student
  sees. No picker. One click. KaTeX fonts work because Chromium loads them
  normally. Leverages existing `check_pages.sh` tooling.
- Cons: Needs a Python script instead of `python3 -m http.server`. ~40 lines.

### Python server sketch (`serve_render.py`)

```python
#!/usr/bin/env python3
"""Serves static files + /render?page=N endpoint that returns a PNG of
   the Nth <div class="page"> in exam3_cheatsheet_v10.html."""
import http.server, socketserver, subprocess, tempfile, urllib.parse, pathlib, os

PORT = 8000
HTML = "exam3_cheatsheet_v10.html"
ROOT = pathlib.Path(__file__).parent.resolve()

class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path != "/render":
            return super().do_GET()
        q = urllib.parse.parse_qs(u.query)
        page = int(q.get("page", ["1"])[0])
        with tempfile.TemporaryDirectory() as td:
            pdf = os.path.join(td, "out.pdf")
            subprocess.run([
                "google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
                "--no-pdf-header-footer", "--virtual-time-budget=10000",
                f"--print-to-pdf={pdf}", f"http://localhost:{PORT}/{HTML}",
            ], check=True, cwd=td)
            # pdftoppm emits "page-1.png", "page-2.png", ...
            subprocess.run(["pdftoppm", "-png", "-r", "200", pdf,
                            os.path.join(td, "page")], check=True)
            png = os.path.join(td, f"page-{page}.png")
            data = open(png, "rb").read()
        self.send_response(200)
        self.send_header("Content-Type", "image/png")
        self.send_header("Content-Disposition",
                         f'attachment; filename="cheatsheet-page-{page}.png"')
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

os.chdir(ROOT)
with socketserver.ThreadingTCPServer(("", PORT), H) as s:
    print(f"Serving on http://localhost:{PORT}  (try /render?page=1)")
    s.serve_forever()
```

Button in the HTML (replace the current html-to-image handler):

```html
<button onclick="window.location='/render?page=1'">Download page 1 PNG</button>
<button onclick="window.location='/render?page=2'">Download page 2 PNG</button>
```

Run with `python3 serve_render.py` from the `exam3/` directory instead of
`python3 -m http.server`.

---

## Ranked recommendation (for a non-technical student, one-click goal)

1. **Approach 10 (Python + headless Chromium)** — definitively works, one
   click, zero picker, identical to `check_pages.sh` output the user already
   trusts. Swap `python3 -m http.server` for `python3 serve_render.py`.
2. **Approach 1 (`getDisplayMedia`)** — pure client-side fallback, works
   offline, but requires a picker click each time. Good second choice if the
   user can't/won't run a custom Python script.
3. **Approach 2 (`window.print()` + pdftoppm)** — reliable but two-step.
4. **Approach 4 (hand-rolled foreignObject with inlined KaTeX fonts)** — only
   if pure-client-side and no picker are both required. Fragile.
5. Everything else — don't bother.
