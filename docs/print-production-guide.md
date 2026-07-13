# Print Production Guide (handoff-ready)

**Date:** 2026-07-13
**Companions:** `print-booklet-plan.md` (the *what*: booklets + page map), `print-production-notes.md` (the *why* + session history). This file is the *how* - prescriptive, and **self-contained**: guide + a page's source text is enough to produce correct booklet HTML in any session (Cowork, a plain chat on a phone, or Kiro).

---

## 0. Preflight - confirm your environment first

Before doing anything, establish what you can actually reach, because the answer changes the workflow:

- **Repo present?** Look for `L1/*.md` (the source text mirrors), `docs/print-booklet-plan.md`, and `WIP/core-rules-digest.html` (the current working file). If they're here, you have the source of truth.
- **Local-only agent (e.g. Kiro)?** Confirm the `L1/*.md` mirrors exist and are current on this machine. They are the *only* approved text source. If they're missing, stop and ask - do not reconstruct text from memory.
- **Plain chat, no file tools (e.g. phone session)?** Expect the human to paste the page's source text. Build the HTML from what's pasted, using the CSS in section 4.
- **Can you open the result in Chrome?** You must be able to. Chrome is the only faithful preview (see section 6).

---

## 1. The one rule - verbatim text

Text comes from the website's `.md` mirrors (or pasted source), **reflowed for print, never rewritten.** Do not paraphrase, tighten, "improve," or invent. The author edits and trims; the build only *formats*.

The single allowed normalization is house style: **em-dash `—` becomes ` - ` (hyphen with spaces).** This matches the author's `dedash-on-save` hook and is wanted. Nothing else about the wording changes.

---

## 2. Target format

- **Trim:** digest, 5.5 x 8.5 in.
- **Binding:** saddle-stitch - page counts in **multiples of 4**, ~**64pp** practical ceiling per booklet. Full-page art can act as shims to hit the multiple.
- **Palette** (from `L1/style.css`): parchment `#fdf2d5`, ink `#1a1008`, woodburn (headings/accent) `#8b3a0f`, ink-mid `#4a3520`, rule/hairline `#c8a96e`, callout tint `#f6ecc9`. Body face: Georgia serif.

---

## 3. Pipeline (spec - implement as a local tool, e.g. `tools/build-booklet.py`)

1. Take the ordered list of source pages (`.md` files) for the booklet.
2. **Clean each page:** drop everything above the first `# ` H1 (removes the breadcrumb and the category label), drop standalone `---` rules, drop `- [← Previous ...]` / `- [Next → ...]` nav lines. Strip markdown images except art you deliberately place.
3. **Normalize:** em-dash `—` -> ` - `.
4. **Convert** markdown -> HTML (python-markdown `extra`, or equivalent).
5. **Wrap** in the HTML shell: the base CSS (section 4) in a `<style>`, content in `<body>`, and the Paged.js polyfill `<script src="https://unpkg.com/pagedjs/dist/paged.polyfill.js"></script>` at the end of body.
6. Output one self-contained `.html`. Review in Chrome; Chrome + Paged.js paginate it into digest pages, and Ctrl-P -> Save as PDF gives a proof.

Hand-laid pages (ones with tuned art/spacing) are authored directly as an HTML `<section class="opener">` block and concatenated ahead of the continuous flow. Plain pages just flow.

---

## 4. Base CSS (paste-ready)

```css
@page{size:5.5in 8.5in;margin:0.5in 0.45in 0.45in;background:#fdf2d5;}
@page:right{@bottom-right{content:counter(page);font:9.5pt Georgia,serif;color:#4a3520;}}
@page:left{@bottom-left{content:counter(page);font:9.5pt Georgia,serif;color:#4a3520;}}
html{background:#fdf2d5;color:#1a1008;}
body{background:#fdf2d5;font:10.5pt/1.45 Georgia,"Times New Roman",serif;}
.pagedjs_sheet,.pagedjs_page,.pagedjs_pagebox{background:#fdf2d5 !important;}   /* full-bleed parchment in Chrome */
h1{font-size:17pt;line-height:1.12;margin:0.7em 0 0.3em;color:#8b3a0f;break-after:avoid;}
h2{font-size:12.5pt;margin:1em 0 0.25em;color:#8b3a0f;break-after:avoid;}
p{margin:0 0 0.5em;text-align:justify;}
a{color:inherit;text-decoration:none;} strong{font-weight:bold;} em{font-style:italic;}
blockquote{border:1px solid #c8a96e;background:#f6ecc9;padding:0.45em 0.7em;margin:0.7em 0;}
blockquote>:first-child{margin-top:0;} blockquote>:last-child{margin-bottom:0;}
/* callout must tuck up beside a float, not clear under it (Chrome bug fix): */
.opener blockquote{display:flow-root;break-inside:avoid;clear:none;margin:.45em 0 0;}
/* a hand-laid page: tightened, forced onto its own sheet */
.opener{break-after:page;line-height:1.36;}
.opener h1{font-size:16pt;margin:.05em 0 .3em;}
.opener h2{font-size:11.5pt;margin:.55em 0 .12em;}
.opener p{margin:0 0 .4em;}
```

---

## 5. Layout cookbook (the moves, with code)

- **Float art, wrap text around it:** `float:right;width:30%;margin:.1em 0 .35em .75em;` (or `float:left`).
- **Nudge a float up/down:** negative or positive top margin (`margin-top:-0.40in`).
- **Bleed off the trim edge:** negative side margin (`margin-right:-0.9in`). NOTE: true print bleed needs a few mm of image past trim + bleed setup at export; on screen it just runs off the sheet.
- **Line break without paragraph spacing:** `<br>` inside the paragraph.
- **Blend a gray/paper-backed sketch into the parchment:** `mix-blend-mode:multiply;`
- **Feather a hard image edge to nothing:** `mask-image:radial-gradient(ellipse at center,#000 48%,rgba(0,0,0,.5) 70%,transparent 95%);` (add `-webkit-mask-image` twin).
- **"Tossed sketch" tilt:** `transform:rotate(-3deg);`
- **Callout beside a tall float (not dropping under it):** `display:flow-root;break-inside:avoid;` on the blockquote. This was the fix for a real Chrome-only drop.
- **Fit one page:** tighten `line-height` / paragraph margins on the section, then place art in the reclaimed space. Work one page at a time and check the fit in Chrome.

---

## 6. Gotchas (learned the hard way - do not relearn them)

- **Chrome is the truth; a PDF proof engine is not.** If you use WeasyPrint (or similar) for page-count checks, know it renders floats and bordered callouts *differently* than Chrome/Paged.js and **cannot fetch remote (R2) images**. A layout that looks perfect in the proof can drop or overlap in Chrome. Always confirm the real look in Chrome.
- **Art specs:** print wants **300 dpi**; line art should be **transparent PNG** so it sits on the parchment; edge art needs **bleed**. Screen/web art is too low-res for print.
- **Version control:** committing from a sandbox / remote environment has been unreliable here - **commit from the local machine.**

---

## 7. State & what's left

- **Working file:** `WIP/core-rules-digest.html` - the Core booklet (Getting Started + Core Mechanics, Gear pulled to the GM book). Pages 1 and 2 are laid out with art; the rest flows.
- **Remaining:** pages 3+ one at a time, then the other booklets per `print-booklet-plan.md` (Roles as ~4 category booklets, Magick incl. supernatural roles, Running the Game incl. Gear + appendices), folding in the web deltas (Tricks, Hooks on Credit, Gear Traits, Assist Rule; the two rules clarifications).
- **Final step:** proper PDF conversion once content is done - Paged.js print / CLI, with bleed and crop marks for the printer.
