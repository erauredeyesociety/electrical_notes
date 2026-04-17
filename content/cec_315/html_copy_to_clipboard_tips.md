# HTML → Clipboard (PNG) Research Notes

Research target: add a per-page "Copy to Clipboard" button to
`exam3_cheatsheet_v10.html` that serializes one `<div class="page">`
(KaTeX math + custom fonts) to a PNG and writes it to the system clipboard.

---

## 1. Library comparison — html2canvas vs html-to-image vs dom-to-image-more vs modern-screenshot

Two fundamentally different rendering strategies:

| Library | Strategy | Size | Speed | KaTeX/SVG |
|---|---|---|---|---|
| **html2canvas** | Re-implements CSS layout on a `<canvas>` (paints from scratch) | ~200 KB | Slow | **Buggy with KaTeX** (breaks `\frac` horizontal rules, `\sqrt` glyphs, vector symbols) |
| **html-to-image** | Clones DOM into SVG `<foreignObject>`, lets browser paint it, rasterizes via canvas | ~17 KB | Fast | **Good** — SVG/KaTeX paint natively |
| **dom-to-image-more** | Same foreignObject trick; fork of the (unmaintained) original dom-to-image | ~20 KB | Fast | Good |
| **modern-screenshot** | Rewrite/fork of html-to-image with newer CSS support and streaming | ~25 KB | Fastest reported (~3× faster than html2canvas) | Good |

**Notable issues:**
- html2canvas GH #789: KaTeX fraction horizontal bar disappears. Issue #879: custom fonts inconsistently load. Vector symbols from KaTeX don't render.
- html-to-image GH #213/#207: Google Fonts / CDN fonts can fail to embed if CORS isn't set; requires `crossorigin="anonymous"` on the stylesheet or explicit `fontEmbedCSS` option.
- Safari has historically had issues with `<foreignObject>` security, though modern Safari (16+) works. Modern-screenshot improves on this.

**Code snippet (html-to-image via CDN):**
```html
<script src="https://cdn.jsdelivr.net/npm/html-to-image@1.11.13/dist/html-to-image.js"></script>
<script>
  const page = document.querySelector('.page');
  htmlToImage.toBlob(page, { pixelRatio: 2 }).then(blob => { /* ... */ });
</script>
```

**Pitfall:** html2canvas looks like the "default" (most GitHub stars, most StackOverflow answers) but is the *worst* choice for KaTeX-heavy content.

---

## 2. Clipboard API for images

`navigator.clipboard.write([new ClipboardItem({'image/png': blob})])`

**Support (as of 2026):**
- Chrome/Edge 76+, Safari 13.1+, Firefox 127+ (shipped mid-2024).
- `image/png` is the only MIME type *mandated* across all browsers.
- `ClipboardItem.supports('image/png')` returns `true` everywhere now.

**Requirements:**
1. **Secure context required** — HTTPS or `localhost`. File:// is NOT secure context (see §3).
2. **Transient user activation required** — must be called from a click/keydown handler. Calling it from a `setTimeout` after the user clicked will fail.
3. **Document must have focus** (`document.hasFocus()`).
4. **No permission prompt for writing** in Chrome/Edge. Firefox/Safari also skip the prompt for writes (reads are prompted).

**Safari quirk:** Safari kills user activation across `await` boundaries. You must either:
- Do all the async work, then call `clipboard.write` synchronously, OR
- Pass a **Promise<Blob>** directly inside ClipboardItem (Safari resolves it without losing activation):

```js
const item = new ClipboardItem({
  'image/png': (async () => await htmlToImage.toBlob(node, opts))()
});
await navigator.clipboard.write([item]);
```

Chromium added Promise-to-Blob support in 2022, so this pattern works cross-browser today.

**Pitfall:** Firefox doesn't expose the `clipboard-write` permission query (returns `not-supported`); don't branch on `navigator.permissions.query`.

---

## 3. `file://` protocol gotchas

**Clipboard API over file://:**
- Chrome: `navigator.clipboard` is `undefined` on `file://`. Clipboard writes fail with `TypeError: Cannot read properties of undefined`.
- Firefox: Same — not a secure context.
- Safari: Same.

Workarounds:
1. **Serve locally** (recommended): `python3 -m http.server 8000 -d /path/to/exam3/` then open `http://localhost:8000/exam3_cheatsheet_v10.html`. Localhost IS a secure context.
2. **Chrome flag** (fragile, per-origin): `chrome://flags/#unsafely-treat-insecure-origin-as-secure` — requires a restart and an explicit origin. Doesn't cleanly accept `file://`.
3. **`document.execCommand('copy')` fallback** — deprecated but still works on file:// for the legacy `ClipboardEvent` path; however you cannot put a PNG Blob on the clipboard through it, only text/HTML. Not viable for this use case.

**CORS + CDN fonts over file://:**
- KaTeX CSS is loaded from `cdn.jsdelivr.net`. Fonts are fetched relative to that CSS. Normal page load works fine.
- When html-to-image embeds the page into SVG, it needs to **re-fetch the font files and inline them as base64**. Those fetches inherit file:// origin and will be blocked by CORS (CDN sends `Access-Control-Allow-Origin: *` but the request itself may be flagged opaque from file://).
- Serving via `python3 -m http.server` fixes both the clipboard *and* the font-embed problem at once.

**Recommendation:** Tell the student to run `python3 -m http.server 8000` in the exam3 directory and open via `http://localhost:8000/`. One command, fixes everything.

---

## 4. KaTeX rendering inside the captured image

KaTeX output is a mix of:
- Inline spans with the `KaTeX_Main`, `KaTeX_Math`, `KaTeX_Size{1..4}` font families.
- Inline SVG (for `\sqrt`, `\vec`, horizontal fraction rules, delimiter stretching).
- Heavily-CSS-positioned spans (negative margins, `vertical-align`, custom line-heights).

**html2canvas:** Breaks fraction bars (drawn via a CSS-border hack that html2canvas's reimplementation miscalculates), breaks `\sqrt` symbols (the SVG glyph overlay), occasionally shifts baselines when font metrics are wrong.

**html-to-image / modern-screenshot:** The browser itself paints the foreignObject, so everything that rendered correctly on screen renders correctly in the image — *provided fonts are embedded*.

**Font embedding — the #1 gotcha:**
The foreignObject SVG is isolated; it does NOT automatically inherit `@font-face` rules from the outer page's stylesheets. html-to-image handles this by fetching the webfont CSS, pulling font files, base64-encoding them, and inlining. This requires:
1. CORS-accessible font server (jsDelivr is fine; file:// is not — see §3).
2. Fonts actually loaded *before* capture. Wait for `document.fonts.ready`:
   ```js
   await document.fonts.ready;   // after renderMathInElement() completes
   const blob = await htmlToImage.toBlob(page, { pixelRatio: 2 });
   ```
3. If font embedding still fails, precompute once with `htmlToImage.getFontEmbedCSS(document.body)` and pass it via the `fontEmbedCSS` option on every subsequent capture — avoids repeated CDN fetches.

**Pitfall:** Missing fonts produce an image where KaTeX symbols fall back to a generic font — fraction bars, integral signs, large parens all collapse. Visible instantly.

---

## 5. Image quality / dimensions

Target: one 5×3-inch "index card" page.

CSS pixels at 96 dpi: 5 × 96 = 480px wide, 3 × 96 = 288px tall → 480×288 CSS px.

| pixelRatio | Output px | Approx blob | Looks |
|---|---|---|---|
| 1 | 480×288 | ~30 KB | Fuzzy KaTeX, unreadable small text |
| 2 | 960×576 | ~120 KB | Crisp, matches Retina screen |
| **3** | **1440×864** | **~250 KB** | **Print-quality, pastes large in docs** |
| 4 | 1920×1152 | ~420 KB | Overkill; large paste |

**Recommendation: `pixelRatio: 3`.** KaTeX symbols need the extra resolution because they're assembled from many small spans with sub-pixel positioning. PNG compresses flat-colored math well, so the size penalty is modest.

Code:
```js
htmlToImage.toBlob(page, {
  pixelRatio: 3,
  backgroundColor: '#ffffff',   // defeat transparent-bg paste into Word/Slack
  cacheBust: true
});
```

**Pitfall:** Clipboard managers (Windows Win+V, macOS Universal Clipboard) may cap image sizes around 4 MB. `pixelRatio: 3` for a 5×3" card is well under.

---

## 6. Cross-browser divergence

| Browser | html-to-image | clipboard.write(image/png) | Notes |
|---|---|---|---|
| Chrome 120+ | ✓ | ✓ | Best overall. Promise<Blob> supported. |
| Edge 120+ | ✓ | ✓ | Chromium; same as Chrome. |
| Firefox 127+ | ✓ | ✓ | Shipped image writes in mid-2024. Earlier versions throw. |
| Safari 16.4+ | ✓ (mostly) | ✓ | **Must use Promise<Blob> pattern** (§2). Older Safari had `<foreignObject>` security restrictions; fixed 16+. |
| Safari iOS | ✓ | ✓ (with user gesture) | Works but user may need to tap a confirm overlay on some versions. |

**Known quirks:**
- Firefox <127 silently writes nothing with image MIME types — no error, clipboard gets text fallback. Feature-detect with `ClipboardItem.supports?.('image/png')`.
- Safari requires the top frame to have focus; if the page is in an iframe, clipboard writes fail silently.

---

## 7. Fallback strategies

Detect clipboard capability, then degrade:

```js
async function copyPageToClipboard(pageEl) {
  const makeBlob = () => htmlToImage.toBlob(pageEl, { pixelRatio: 3, backgroundColor: '#fff' });

  // Primary: async clipboard with Promise<Blob> (Safari-safe)
  if (navigator.clipboard && window.ClipboardItem) {
    try {
      const item = new ClipboardItem({ 'image/png': makeBlob() });
      await navigator.clipboard.write([item]);
      flash(pageEl, 'Copied!');
      return;
    } catch (err) {
      console.warn('Clipboard write failed, falling back:', err);
    }
  }

  // Fallback 1: download as PNG
  const blob = await makeBlob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `page-${pageEl.dataset.pageIndex || 1}.png`;
  a.click();
  URL.revokeObjectURL(url);
  flash(pageEl, 'Downloaded (clipboard unavailable)');
}
```

**Additional fallback options (in order of desirability):**
1. **Download** (shown above) — universally works.
2. **Open in new tab** (`window.open(url)`) — user can right-click → Copy Image. Good for file:// where downloads also struggle.
3. **Inline preview** — append an `<img src="<dataURL>">` next to the page; user right-clicks to copy. Most reliable on file://.

---

## 8. Minimal standalone example

Save as `clip_demo.html` and serve via `python3 -m http.server` (not file://):

```html
<!doctype html>
<html><head>
<meta charset="utf-8">
<title>Copy page → clipboard demo</title>
<link rel="stylesheet" crossorigin="anonymous"
      href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/html-to-image@1.11.13/dist/html-to-image.js"></script>
<style>
  body { font-family: sans-serif; padding: 20px; background: #eee; }
  .page { width: 5in; height: 3in; padding: 0.2in; background: white;
          border: 1px solid #888; box-sizing: border-box; }
  button { margin-top: 10px; padding: 8px 14px; cursor: pointer; }
  .flash { color: green; margin-left: 10px; font-weight: bold; }
</style>
</head><body>

<div class="page" id="p1">
  <h3>Laplace basics</h3>
  <p>Impulse: $\mathcal{L}\{\delta(t)\} = 1$.</p>
  <p>Integrator: $\mathcal{L}\{\int_0^t f(\tau)\,d\tau\} = \frac{F(s)}{s}$.</p>
  <p>Damped sine: $\mathcal{L}\{e^{-at}\sin(\omega t)\} = \dfrac{\omega}{(s+a)^2 + \omega^2}$.</p>
  <p>Square root example: $x = \sqrt{b^2 - 4ac}$.</p>
</div>
<button id="copyBtn">Copy page to clipboard</button>
<span class="flash" id="flash"></span>

<script>
window.addEventListener('load', async () => {
  renderMathInElement(document.body, {
    delimiters: [
      { left: '$$', right: '$$', display: true },
      { left: '$',  right: '$',  display: false }
    ],
    throwOnError: false
  });
  await document.fonts.ready;

  document.getElementById('copyBtn').addEventListener('click', async () => {
    const page = document.getElementById('p1');
    const flash = document.getElementById('flash');
    const makeBlob = () => htmlToImage.toBlob(page, {
      pixelRatio: 3, backgroundColor: '#ffffff', cacheBust: true
    });
    try {
      const item = new ClipboardItem({ 'image/png': makeBlob() });
      await navigator.clipboard.write([item]);
      flash.textContent = 'Copied! Paste into Word/Slack/etc.';
    } catch (err) {
      // Fallback: download
      const blob = await makeBlob();
      const url = URL.createObjectURL(blob);
      const a = Object.assign(document.createElement('a'),
                              { href: url, download: 'page.png' });
      a.click();
      URL.revokeObjectURL(url);
      flash.textContent = 'Clipboard blocked; downloaded instead.';
      console.warn(err);
    }
  });
});
</script>
</body></html>
```

**To test:**
```
cd /tmp && python3 -m http.server 8000
# open http://localhost:8000/clip_demo.html
```

Paste result (Ctrl-V) into Word, Google Docs, Slack, or an image viewer.

---

## Recommended stack for v10

**Library:** `html-to-image@1.11.x` via jsDelivr.
**API:** `htmlToImage.toBlob(page, { pixelRatio: 3, backgroundColor: '#fff', cacheBust: true })`
wrapped in a `ClipboardItem({ 'image/png': <promise> })` for Safari compatibility.

**Setup steps:**
1. Add the script tag below KaTeX in `<head>`:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/html-to-image@1.11.13/dist/html-to-image.js"></script>
   ```
   Also add `crossorigin="anonymous"` to the KaTeX CSS `<link>` so fonts embed cleanly.
2. After `renderMathInElement(...)` completes, add `await document.fonts.ready` before enabling the copy buttons (otherwise first click may ship un-embedded fonts).
3. Inject a small button into each `<div class="page">` at creation time (or in `autoPaginate`'s page-building code). Exclude buttons from the capture with `filter: node => !node.classList?.contains('copy-btn')`.
4. **Tell the student:** open the file via `python3 -m http.server 8000` from the `exam3/` directory, not via double-clicking the HTML. File:// breaks both the clipboard API and font CORS.
5. Include the download fallback from §7 so Chromium users on file:// still get a usable PNG.

**Why this stack:**
- html-to-image renders KaTeX SVG correctly (fractions, sqrt glyphs, vector symbols); html2canvas does not.
- Tiny bundle (~17 KB), no build step, drop-in CDN script.
- Safari-safe Promise<Blob> pattern matches Chrome's behavior with the same code.
- `pixelRatio: 3` gives a sharp 1440×864 PNG for a 5×3" card — reads cleanly in any paste target.
