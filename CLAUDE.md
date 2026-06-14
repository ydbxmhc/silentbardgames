# CLAUDE.md — Steering file for SilentBardGames / OneSRD repo

This file contains standing instructions for any Claude session working in this repository.
Read it before doing anything else. These rules are non-negotiable.

---

## Shell / Bash hygiene

- **NEVER redirect stderr to /dev/null.** Send it to `stderr.log` (appending: `2>>stderr.log`).
  Silent error disposal hides real problems. Read the log before re-running a failed command.
- Prefer `2>>stderr.log` for background noise; use `2>&1` only when stderr content
  is directly relevant to the output you are capturing.
- Before assuming "file not found," check whether an error was actually logged.
- `stderr.log` is not tracked by git and may not exist; create it with `touch` if needed,
  but note the sandbox may not be able to create files in the repo root — use
  `/sessions/.../mnt/outputs/stderr.log` as a fallback.

---

## Content integrity — THE PRIME DIRECTIVE

This is an SRD (System Reference Document) for a published TTRPG rulebook.
**Do not rewrite, rephrase, "improve," or editorialize any rulebook content. Ever.**

Your job here is FORMATTING and STRUCTURE only:
- Correct HTML structure (headings, paragraphs, lists, tables, anchors)
- Navigation and linking
- CSS class application
- Page organization to match the source PDF

If you find yourself changing a word the author wrote, **stop and ask.**
The PDF is the source of truth. The HTML must match it — not improve on it.

---

## Workflow

- Always consult before making changes to multiple files in one go.
- Prefer small, targeted edits over wholesale rewrites of a page.
- When comparing HTML to PDF, note discrepancies and **ask** before correcting them.
- The `action/` folder contains narrative vignette pages ("In Action" stories).
  The `roles/` folder contains the rules text. Both are intentional. Do not merge them.

---

## Repository structure — OneSRD multi-game platform

This is not a single-game site. It hosts multiple games under one domain.

```
/                          ← Root: OneSRD dispatch page (index.html only)
/resources/
  onesrd.css               ← Shared structural CSS (all games load this first)
  nav.js                   ← Shared nav/header injection script
/L1/                       ← Level One RPG (game subfolder)
  index.html               ← L1 home page
  config.js                ← L1 config: BASE_PATH='/L1/', CDN, L1Prefs
  style.css                ← L1 theme CSS (overrides onesrd.css vars)
  header.html              ← L1 header inner content (injected by nav.js)
  nav.html                 ← L1 drawer nav (injected by nav.js)
  settings.html            ← User preference page
  *.html                   ← All L1 rules pages
  roles/                   ← Role rules pages
  action/                  ← Narrative "In Action" vignette pages
  magick/                  ← Magic system pages
/[future-game]/            ← Future games follow the same pattern as /L1/
```

### CSS load order (every L1 page)
```html
<link rel="stylesheet" href="/resources/onesrd.css">   <!-- structure -->
<link rel="stylesheet" href="/L1/style.css">            <!-- L1 theme  -->
```
`onesrd.css` defines neutral default CSS variables. `style.css` overrides them
with L1's parchment-and-woodburn theme. Never add inline styles.

### Script load order (every L1 page, at end of body)
```html
<script src="/L1/config.js"></script>      <!-- SiteConfig, L1Prefs, applyAll() -->
<script src="/resources/nav.js"></script>  <!-- fetches header.html + nav.html   -->
```
`nav.js` reads `SiteConfig.BASE_PATH` to know where to fetch from.
Do not modify `nav.js` or `config.js` without explicit instruction.

### nav.html link format
Links in `/L1/nav.html` use **game-relative paths** (no leading slash):
  `start.html`, `roles/warrior.html`, `magick/spells.html`
`nav.js` rewrites these to absolute paths by prepending `BASE_PATH`.
Do **not** add leading slashes to nav links — they will not be rewritten.

### header.html
Contains only the inner elements of `<header id="site-header">` — no wrapping tag.
The home link uses an absolute path: `/L1/index.html`.

---

## Key files — do not modify without explicit instruction

- `/resources/onesrd.css` — shared structural styles
- `/resources/nav.js` — shared nav loader
- `/L1/config.js` — game config and user preferences
- `/L1/nav.html` — single source of truth for L1 drawer nav
- `/L1/header.html` — L1 header inner content
- `/L1/settings.html` — must remain readable with all styles/images off

---

## Source reference

PDFs (`L1,*.pdf`) are source reference only; excluded from version control via `.gitignore`.
The PDF is the source of truth for all rulebook content.

# Task Brief: Verbatim Web Replication of the *Level One RPG* Rulebook

## What This Project Is

I am publishing the *Level One RPG* rulebook (by The Silent Bard) as a set of
web pages. The website already exists as static HTML/CSS/JS. Your job is to make
the web pages reproduce the book **functionally exactly** — as close to the PDF
as the medium allows.

I will hand you the source PDFs. Everything you produce must come **from those
PDFs**.

---

## THE ONE RULE THAT MATTERS MOST

**Every word of page content must be an exact, character-for-character
transcription of the PDF.**

- Do **not** paraphrase.
- Do **not** summarize.
- Do **not** "clean up," "tighten," or "improve" the prose.
- Do **not** invent examples, names, rules, headings, or sentences.
- Do **not** generate *any* original wording to fill gaps.
- Do **not** reorder or merge the author's sentences.

If the book says it, the page says it — identically. If the book doesn't say it,
it does **not** appear on the page. There is no acceptable amount of invented or
rephrased text. The correct quantity is zero.

### Why I am this strict

My readers are tabletop RPG enthusiasts. They can spot AI-generated or
paraphrased text instantly, and they will reject the entire product over it. A
single fabricated example or reworded rule discredits the whole book. This is
not a stylistic preference — it is the core requirement of the job. Accuracy
beats everything, including speed.

---

## How Picky I Am (read this twice)

- I will read your output **side by side with the PDF**, sentence by sentence.
- I will reject a page for a single invented example, a single dropped clause,
  a single "improved" phrasing, or a changed heading.
- I do not want you to "capture the meaning." I want the **words**.
- If you are tempted to make the text read better — don't. The author already
  chose the words. Your taste is irrelevant here.
- "Close enough" is a failure. Punctuation, italics, bold, capitalization,
  numbers, and list order all matter.
- If a passage is unclear in the PDF image, **stop and tell me** — do not guess
  and do not fill it in with plausible-sounding text.

---

## The Only Process That Works

The PDFs are **image-based** (exported via "Microsoft Print to PDF"). Text
extraction returns nothing. You must read the pages **as images**, visually.

1. Install the renderer (not persistent between sessions):
   `apt-get install -y poppler-utils`
2. Render the specific pages you need to PNGs:
   `pdftoppm -r 150 -png -f <first> -l <last> <pdf_path> /tmp/out/page`
3. **Open each PNG and read it yourself, in this session.** Transcribe what you
   literally see, word for word.
4. Write the HTML directly from what you read.
5. Work in **small batches** (a page or two at a time) so I can verify before
   you continue.

### Hard prohibitions on method

- **Do NOT delegate content transcription to sub-agents.** Every prior failure
  came from an agent paraphrasing or inventing text instead of copying it. The
  session that reads the image must be the one that writes the words.
- **Do NOT** transcribe from memory, from a previous summary, or from the
  existing pages on the site (some existing pages contain fabricated content —
  trust only the PDF).
- **Do NOT** rely on `pdftotext` / text extraction — it produces nothing
  useful for these files.

---

## Layout & Formatting Fidelity

The words are non-negotiable; the layout should match the book **as closely as
the web medium reasonably allows**:

- Preserve the book's **headings and subheadings** exactly (same text, same
  order, same hierarchy).
- Preserve **bold and italic emphasis** where the book uses it.
- Preserve **callout boxes, sidebars, and "in-play" example blocks** as distinct
  visual elements, matching where they appear relative to the body text.
- Preserve **list structure** (bulleted vs. numbered, and item order).
- Preserve **art placement** relative to the text. I can move/swap the actual
  image assets myself — just put the placeholder/image in the right spot and
  tell me what art belongs there.
- Match the existing site's HTML structure and CSS conventions for these
  elements (inspect the existing pages to reuse the right classes); do not
  invent new styling unless asked.

If something in the book cannot be reproduced faithfully on the web, **ask me**
how I want to handle it rather than improvising.

---

## Workflow Expectations

1. Tell me which book pages map to which web page **before** you write.
2. Render and read those exact PDF pages.
3. Produce the page, then **stop and show me** so I can check it against the PDF.
4. Wait for my confirmation before moving on.
5. When I approve, commit that page and continue to the next batch.

**Work cycle** = one round trip in the chat: the user sends a message, Claude
responds. Commit at the end of every work cycle in which files changed.
Push only when the user explicitly says to push.

Do not run ahead and rewrite many pages at once. Small, verifiable increments.

---

## What "Done" Looks Like

A page is done when I can place the PDF and the rendered web page next to each
other and the **text is identical** and the **structure/art placement clearly
mirrors the book**. Nothing less counts.

If you are ever unsure whether you're allowed to write something that isn't
directly on the page in front of you, the answer is no. Read the image, copy the
words, ask if anything is unclear.

