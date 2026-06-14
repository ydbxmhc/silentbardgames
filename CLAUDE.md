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

