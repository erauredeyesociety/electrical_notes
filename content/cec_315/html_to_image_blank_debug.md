# html-to-image BLANK/WHITE Output — Debug Research

Target file: `/home/devel/electrical_notes/content/cec_315/exam3/exam3_cheatsheet_v10.html`

Stack: `html-to-image@1.11.13` + KaTeX 0.16.11 from jsDelivr + CSS Grid + tables,
served over `http://localhost:8000/...`.

Symptoms: copy-to-clipboard produces a blank white PNG (no content, no KaTeX math,
no tables). Page renders fine in the browser.

---

## TL;DR — single most likely cause

**`cacheBust: true` is appending `?t=<timestamp>` query strings to the jsDelivr
KaTeX CSS/font URLs. jsDelivr's CORS response depends on the exact URL, and the
query-stringed variants get a different (or missing) `Access-Control-Allow-Origin`
header than the bare URL. html-to-image's CSS inliner then either (a) throws when
reading `cssRules` on the newly-fetched stylesheet and swallows the error, or (b)
refetches the webfonts but can't base64-embed them. Either way the cloned
foreignObject has no styles and no fonts, so it paints as a blank white box.**

Compounding that: KaTeX webfonts are famously not embedded correctly on the
**first** `toBlob()` call — a well-known workaround is calling it twice, letting
the first call prime the font cache.

### One-line fix to try first

Change `cacheBust: true` → `cacheBust: false` in `renderOpts()`
(line 117 of `exam3_cheatsheet_v10.html`). If content appears, the issue was the
CDN+query-string CORS mismatch. Do NOT also leave `cacheBust: true` and add
`skipFonts: true` — that will disable font embedding entirely.

---

## 1. Stylesheet-cloning failure (most likely)

html-to-image walks every `document.styleSheets` entry and calls `.cssRules` to
serialize each rule into an inline `<style>` inside the cloned foreignObject
SVG. If any stylesheet throws a `SecurityError: Failed to read the 'cssRules'
property` the library **catches and ignores it silently** (issues
[#301](https://github.com/bubkoo/html-to-image/issues/301),
[#362](https://github.com/bubkoo/html-to-image/issues/362),
[#395](https://github.com/bubkoo/html-to-image/issues/395)).

The result: cloned DOM has NO CSS. The `.page` has no width/height/grid; tables
have no borders; text is at default font-size. Painted onto a 5×3-in canvas with
`overflow: hidden` and `backgroundColor: '#ffffff'`, the un-laid-out content
either renders at 0px or is clipped to the 5in×3in white background → blank.

### How to verify

Open DevTools → Console → run:

```js
[...document.styleSheets].forEach((s, i) => {
  try { void s.cssRules.length; console.log(i, 'OK:', s.href); }
  catch (e) { console.warn(i, 'BLOCKED:', s.href, e.message); }
});
```

If any row says BLOCKED, that's the culprit.

### Fix recipes

- Set `cacheBust: false` (primary fix).
- Ensure `<link rel="stylesheet" ... crossorigin="anonymous">` on the KaTeX
  stylesheet (ALREADY present in v10 — good).
- As a belt-and-suspenders: download `katex.min.css` locally (same-origin) and
  change the `<link href>` to a relative path. Eliminates CORS from the equation.
- Use html-to-image's `fontEmbedCSS` option: pre-fetch the KaTeX CSS yourself,
  pass it as a string, library skips the cross-origin read.

---

## 2. `cacheBust: true` + jsDelivr (highly likely contributor)

`cacheBust: true` appends a timestamp query string to EVERY resource URL during
cloning, including `katex.min.css` and each `KaTeX_Main-Regular.woff2`, etc.
jsDelivr CORS (see jsdelivr issue [#18038](https://github.com/jsdelivr/jsdelivr/issues/18038)) can
reject or strip CORS headers for cache-busted URLs because the cache key
changes. Effect: the font fetch for the SVG embed fails, or the stylesheet
fetch returns an opaque response. Combined with §1 → blank.

See html-to-image issue [#259](https://github.com/bubkoo/html-to-image/issues/259)
(cacheBust interaction with query-string URLs) and
[#399](https://github.com/bubkoo/html-to-image/issues/399) (requesting
`no-cache` fetch option).

**Fix:** `cacheBust: false` (CDN URLs already have far-future cache headers;
you don't gain anything by busting them).

---

## 3. KaTeX webfonts not embedded on first call (very likely compounding factor)

Widely reported pattern: html-to-image uses `<foreignObject>` which needs
`@font-face` entries converted to `data:` URIs. KaTeX's font rules get inlined
but the font **bytes** aren't always fetched in time for the first render, even
after `document.fonts.ready`. The result: math glyphs collapse to fallback or
the whole SVG paints empty.

**Standard workaround** (widely circulated in the dev community): call
`toBlob()` twice, discard the first result. The first call warms the font cache,
the second call produces the real image.

```js
async function copyPageWithFontWarmup(page, opts) {
  await htmlToImage.toBlob(page, opts);   // throwaway — primes font cache
  return htmlToImage.toBlob(page, opts);  // real capture
}
```

Alternative: preload fonts via `fontEmbedCSS: await htmlToImage.getFontEmbedCSS(page)`
once at page load, then pass that cached string on every capture.

---

## 4. Overflow: hidden on the captured element (a real possibility)

`.page` has `overflow: hidden; width: 5in; height: 3in` with a CSS Grid.
html-to-image measures `getBoundingClientRect()` of the root passed in. If the
element's computed width/height ever reads 0 (e.g. it's display:none at the
moment of capture, or the user has it scaled with `transform: scale(2.0)` via
the zoom toggle), the SVG `<foreignObject>` is written with 0×0 dimensions and
the output is blank.

Check: is the "Toggle 2x preview zoom" active when the user clicks Copy? The
transform doesn't change bounding rect in all browsers consistently but the
grid children may be laid-out-relative to a transformed ancestor. Click Copy
with zoom OFF first.

---

## 5. Race with KaTeX render (unlikely — code already handles it)

Current code awaits `document.fonts.ready` before capturing (good). The v10
code also does TWO `requestAnimationFrame` calls after `renderMathInElement`
before calling `buildCopyControls` (good). Race is unlikely but:

- `document.fonts.ready` resolves when fonts the BROWSER already knows about
  are ready. If html-to-image's cloner inserts new `@font-face` rules into the
  SVG, those haven't been "seen" yet.
- Bug fix: add one more RAF INSIDE the click handler right before `toBlob`:

```js
await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
```

---

## 6. Service Worker interference (unlikely here)

If `python3 -m http.server` is serving the site there is no service worker.
Rule out only if user has registered one via a different tool. Check
DevTools → Application → Service Workers. If any SW is listed for
`localhost:8000`, click Unregister and retry.

---

## 7. CSS Grid / foreignObject layout bug (unlikely but possible)

html-to-image occasionally reports sizing issues with flex/grid children. The
`.col > .block` children are floated into an auto-grid; their bounding box is
computed correctly only if the `.page` itself has real dimensions at capture
time. See §4.

---

# Diagnostic checklist — in DevTools, in order

1. **Console errors**: open DevTools BEFORE clicking Copy. Any red errors?
   Especially `SecurityError: ... cssRules` or `Failed to fetch` or `NetworkError
   when attempting to fetch resource`.
2. **Run the stylesheet probe** from §1 above. Any BLOCKED lines?
3. **Network tab** during Copy click: filter by `katex`. Do you see `woff2`
   requests? Do they 200? Do they have `Access-Control-Allow-Origin: *`?
4. **Grab the raw SVG**: temporarily replace `toBlob` with `toSvg` —
   `htmlToImage.toSvg(page, renderOpts()).then(u => open(u))`. Opens the SVG as
   data URL in a new tab. Does the SVG show math and tables, or is it empty?
   This is the decisive test.
5. **Try `toPng` → new tab**: `toPng(page, opts).then(u => { const w=open(); w.document.write('<img src='+u+'>'); })`.
6. **Check `document.hasFocus()`** right before the clipboard write. Clipboard
   API silently rejects without focus.
7. **Toggle zoom OFF** before clicking Copy (transform: scale(2) on ancestor
   can wreck bounding-rect math).
8. **Service workers**: Application → Service Workers. Unregister anything on
   localhost.
9. **`document.fonts.status`** in console. Should be `"loaded"`.
10. **Try `cacheBust: false`** — see §2.

---

# Top 3 most likely causes (this exact stack)

| # | Cause | One-line fix |
|---|-------|--------------|
| 1 | `cacheBust: true` breaking jsDelivr CORS on KaTeX CSS/fonts → CSS inlining fails silently → blank | `cacheBust: false` in `renderOpts()` |
| 2 | KaTeX webfonts not embedded on first `toBlob` call (foreignObject+@font-face bug) → math invisible, layout collapses | Call `toBlob` twice; discard first result |
| 3 | Cross-origin stylesheet `cssRules` read blocked despite `crossorigin="anonymous"` (CDN subresource) → entire clone has no styles | Self-host `katex.min.css` locally OR pre-fetch and pass as `fontEmbedCSS` |

---

# Canary test

Yes. Drop this inline button into the page temporarily and click it:

```html
<button class="no-print" onclick="(async()=>{
  const d = document.createElement('div');
  d.textContent = 'Hello';
  d.style.cssText = 'width:200px;height:100px;background:#def;color:#000;font:20px sans-serif;padding:20px';
  document.body.appendChild(d);
  const blob = await htmlToImage.toBlob(d, { pixelRatio: 2, backgroundColor:'#fff' });
  d.remove();
  const url = URL.createObjectURL(blob);
  window.open(url, '_blank');
})()">CANARY</button>
```

Outcomes:
- Opens a blue-ish "Hello" image → html-to-image itself works; problem is
  KaTeX-CSS/CDN-specific → fix per §1/§2/§3.
- Opens a blank image too → broader issue (CSP? browser?) → check DevTools
  console for errors, check service workers, check browser version.

A sharper canary: capture one `.page` with `cacheBust: false` and nothing else
changed. If that fixes it, confirmed §2.

---

# Recommended minimal patch to v10

In `renderOpts()` (around line 113 of `exam3_cheatsheet_v10.html`):

```js
function renderOpts() {
  return {
    pixelRatio: 3,
    backgroundColor: '#ffffff',
    cacheBust: false,                    // was true — jsDelivr CORS
    filter: function (node) {
      return !(node.classList && node.classList.contains('no-print'));
    }
  };
}
```

And wrap the capture in a font-warmup double-call:

```js
// inside copyPageToClipboard, replace the single toBlob with:
var blobPromise = htmlToImage.toBlob(page, renderOpts())
  .then(function () { return htmlToImage.toBlob(page, renderOpts()); });
```

If the problem persists, self-host KaTeX CSS (one file, ~30 KB) next to the
HTML and change the `<link href>` to a relative path. That eliminates every
CORS variable in one stroke.

---

# References

- html-to-image repo: https://github.com/bubkoo/html-to-image
- Issue #301 — CSS CORS: https://github.com/bubkoo/html-to-image/issues/301
- Issue #362 — cssRules access denied: https://github.com/bubkoo/html-to-image/issues/362
- Issue #395 — cssRules when packaged as SDK: https://github.com/bubkoo/html-to-image/issues/395
- Issue #259 — cacheBust cache-key bug: https://github.com/bubkoo/html-to-image/issues/259
- Issue #399 — fetch `no-cache` option request: https://github.com/bubkoo/html-to-image/issues/399
- Issue #449 — empty image from valid HTML: https://github.com/bubkoo/html-to-image/issues/449
- Issue #461 — blank images in Safari: https://github.com/bubkoo/html-to-image/issues/461
- jsDelivr CORS issue: https://github.com/jsdelivr/jsdelivr/issues/18038
- HTML/CSS-to-Image debug guide: https://docs.htmlcsstoimage.com/guides/debugging-white-or-blank-images
- KaTeX common issues: https://katex.org/docs/issues.html
