# CLAUDE.md -- Steering file for SilentBardGames / OneSRD repo

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
  but note the sandbox may not be able to create files in the repo root -- use
  `/sessions/.../mnt/outputs/stderr.log` as a fallback.

---

## Content integrity -- THE PRIME DIRECTIVE

This is an SRD (System Reference Document) for a published TTRPG rulebook.
**Do not rewrite, rephrase, "improve," or editorialize any rulebook content. Ever.**

Your job here is FORMATTING and STRUCTURE only:
- Correct HTML structure (headings, paragraphs, lists, tables, anchors)
- Navigation and linking
- CSS class application
- Page organization to match the source PDF

If you find yourself changing a word the author wrote, **stop and ask.**
The PDF is the source of truth. The HTML must match it -- not improve on it.

---

## Workflow

- Always consult before making changes to multiple files in one go.
- Prefer small, targeted edits over wholesale rewrites of a page.
- When comparing HTML to PDF, note discrepancies and **ask** before correcting them.
- The `action/` folder contains narrative vignette pages ("In Action" stories).
  The `roles/` folder contains the rules text. Both are intentional. Do not merge them.

---

## Repository structure -- OneSRD multi-game platform

This is not a single-game site. It hosts multiple games under one domain.

```
/                          <-- Root: OneSRD dispatch page (index.html only)
/resources/
  onesrd.css               <-- Shared structural CSS (all games load this first)
  nav.js                   <-- Shared nav/header injection script
/L1/                       <-- Level One RPG (game subfolder)
  index.html               <-- L1 home page
  config.js                <-- L1 config: BASE_PATH='/L1/', CDN, L1Prefs
  style.css                <-- L1 theme CSS (overrides onesrd.css vars)
  header.html              <-- L1 header inner content (injected by nav.js)
  nav.html                 <-- L1 drawer nav (injected by nav.js)
  settings.html            <-- User preference page
  *.html                   <-- All L1 rules pages
  roles/                   <-- Role rules pages
  action/                  <-- Narrative "In Action" vignette pages
  magick/                  <-- Magic system pages
/[future-game]/            <-- Future games follow the same pattern as /L1/
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
Do **not** add leading slashes to nav links -- they will not be rewritten.

### header.html
Contains only the inner elements of `<header id="site-header">` -- no wrapping tag.
The home link uses an absolute path: `/L1/index.html`.

---

## Key files -- do not modify without explicit instruction

- `/resources/onesrd.css` -- shared structural styles
- `/resources/nav.js` -- shared nav loader
- `/L1/config.js` -- game config and user preferences
- `/L1/nav.html` -- single source of truth for L1 drawer nav
- `/L1/header.html` -- L1 header inner content
- `/L1/settings.html` -- must remain readable with all styles/images off

---

## Source reference

PDFs (`L1,*.pdf`) are source reference only; excluded from version control via `.gitignore`.
The PDF is the source of truth for all rulebook content.

# Task Brief: Verbatim Web Replication of the *Level One RPG* Rulebook

## What This Project Is

I am publishing the *Level One RPG* rulebook (by The Silent Bard) as a set of
web pages. The website already exists as static HTML/CSS/JS. Your job is to make
the web pages reproduce the book **functionally exactly** -- as close to the PDF
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

If the book says it, the page says it -- identically. If the book doesn't say it,
it does **not** appear on the page. There is no acceptable amount of invented or
rephrased text. The correct quantity is zero.

### Why I am this strict

My readers are tabletop RPG enthusiasts. They can spot AI-generated or
paraphrased text instantly, and they will reject the entire product over it. A
single fabricated example or reworded rule discredits the whole book. This is
not a stylistic preference -- it is the core requirement of the job. Accuracy
beats everything, including speed.

---

## How Picky I Am (read this twice)

- I will read your output **side by side with the PDF**, sentence by sentence.
- I will reject a page for a single invented example, a single dropped clause,
  a single "improved" phrasing, or a changed heading.
- I do not want you to "capture the meaning." I want the **words**.
- If you are tempted to make the text read better -- don't. The author already
  chose the words. Your taste is irrelevant here.
- "Close enough" is a failure. Punctuation, italics, bold, capitalization,
  numbers, and list order all matter.
- If a passage is unclear in the PDF image, **stop and tell me** -- do not guess
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
  existing pages on the site (some existing pages contain fabricated content --
  trust only the PDF).
- **Do NOT** rely on `pdftotext` / text extraction -- it produces nothing
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
  image assets myself -- just put the placeholder/image in the right spot and
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

---

## Open items / deferred work

These are known gaps to revisit -- do NOT silently fix them; ask the author first.

### Content pages awaiting author revision
- **`roles/beast-handler.html`** (and maneuvers + in-action pages): PDF draft is
  too dense/wrong; the author intends to rewrite the Beast Handler section before
  these pages can be properly transcribed. Current stub pages are placeholders.
- **`roles/naturalist.html`**: Several sections were "glossed over" in the current
  PDF draft. The author needs to add content before those sections can be filled in.

### Content errata (fix on the page's next rewrite)
- **`magick/beyond.html`** (pending rewrite). These errors exist in both the live
  page and the source document:
  - **Mundis** is the correct spelling throughout (live page currently has "Mundus").
  - "thus little **know**" --> *little known* (Dreamlands paragraph).
  - "processing messages" --> *projecting* messages (Communication Magic section).
  - Emotional Currents paragraph is missing its first half: the massacre/rage
    example was dropped, leaving only the euphoria half. Full version: *"A projector
    exploring the spiritual echo of a massacre might become consumed with rage or
    despair, while investigating a site of great joy could leave them euphorically
    unable to focus on their mission."*
  - Unclosed italics: `*rarely.` at end of Psychic Predators --> should be `*rarely.*`

### Rules design / clarifications (not yet in the book)
- **NEW PAGE -- "The Recovery Trope" (building-a-character / quick-start section).**
  Let players start at the table with their starting Karma **unspent** and allocate it
  *retroactively* across session one -- "I always had this Role, and that Maneuver..."
  -- so they're up and playing fast and the character assembles itself out of what the
  fiction actually calls for. Author writes the page prose (new design, not a PDF
  transcription); Claude may scaffold the HTML shell + nav/toc/prev-next wiring to site
  convention with `@@` placeholders. Decisions to pin when writing: (a) the deadline/cap
  on the retroactive spend -- all of it by end of session one, or a set number of
  declarations? (b) may you flashback-justify something already *done* ("I always had
  lockpicks" after trying the door), or only declare *forward*? Cross-reference the
  parked "reincarnates make viable PCs" idea (sample-characters booklet) -- a reincarnate
  "remembering" a prior life's skill is this same trope; they may share the page or the
  example. Surfaced 2026-07-25.
- **NEW PAGE + CANON -- "It's Not About the Build" (design-philosophy; building-a-character
  / intro, and folded into the canon rules).** L1 is deliberately **not** about *builds*.
  There must be no construction that hands a player an unfair edge the way MMORPGs do --
  no "goblin rogue with the assassin build that stun-locks the tank." The three real axes
  instead: **EL for skill *depth*; *breadth* for versatility to cover your weak seams; and
  *role*-playing your Hooks** -- so the GM has an obvious lever to complicate your day in a
  way that *moves the story forward*, and one that *pays* you for good characterization, so
  that later you get to be **awesome** when it's your turn in the spotlight. Thesis: the game
  is not about assembling the "build" that "wins," it's about playing it and enjoying it --
  and as a system, **the vicarious characterization IS the power-play.** Author writes the
  prose (new design / manifesto, not a PDF transcription); Claude may scaffold the site page
  (HTML shell + nav/toc/prev-next wiring) with `@@` placeholders. Wanted on the **site** *and*
  folded into the **canon rules**. Pairs naturally with the Recovery-Trope page above -- both
  are building-a-character philosophy, and both argue play-first over optimize-first. Surfaced
  2026-07-29.
- **CLARIFY -- when/how a Hook can reach zero and be removed.** The working rule is that
  Hooks "can't *generally* go to zero," yet the book already describes paths that clearly end
  at nothing: an unfed or refused **Imposed Hook** degrades a rank per session and fades out
  entirely (`imposed-hooks.html`: *"Must Keep It Secret* dwindles to *Habit of Silence*, to
  *Socially Distant*, to nothing at all"), and `hooks-and-growth.html` covers reducing a Hook
  by declining its events. Need an explicit statement of the exception: under what conditions
  a Hook may actually be driven to zero and struck from the sheet, versus being floored at
  rank 1. Also pin the timing asymmetry the author noted: *advancement* (ranking a Hook up)
  happens only at end of session and counts against the one-improvement-per-session limit,
  but *downgrading* a Hook can happen at any time. Reconcile the "generally" floor with the
  Imposed/adopted-Hook fade-out so the two sections don't appear to contradict. Surfaced
  2026-08-06.
- **TEST -- multiple Karma-paying Hook triggers per session (Hook-severity variance).** Base rule:
  a Hook pays **Karma** on its first trigger in a session and **Luck Tokens** on any trigger after
  that. Proposed variance, surfaced from the *Dominion and Accord* setting: an exceptionally severe
  Hook may pay **Karma up to three times per session**. Test case is **Pellan Atavism** (see the
  setting notes below) -- a Hook on Credit that starts at **rank 3 minimum**, grants up to 3 dice
  whenever Pellan physiology is an advantage (once per scene), and can be triggered for Karma up to
  3x/session. **Not yet written into the rules; author is unsure whether to keep it.** Things to
  watch in playtest: (a) a player willing to take the trigger becomes the fastest-advancing
  character at the table -- is that a feature (it rewards leaning into a brutal Hook) or a
  balance problem? (b) does the multiplier belong to *rank*, to a named severity tier, or stay a
  per-Hook GM ruling? (c) does it also multiply the Luck Token fallback once the Karma triggers are
  spent? (d) interaction with the Hooks-on-Credit debt rules, since a rank-3 credited Hook already
  can't be declined with a Luck Token while Karma is owed. Note the Level interaction is a real
  constraint, not a side effect: a rank-3 Hook requires **Level 3**, which costs 5K, so a 5-Karma
  starting Pellan (5 + 2 credit = 7K) has only 2K left for Roles and Maneuvers -- very strong
  physically, nearly untrained. That may be exactly right, but it means the variance effectively
  sets a build floor. Surfaced 2026-08-07.
- **Resist vs. oppose on *imposed effects*.** The resist/oppose choice (Resistance
  page: "any defense that can't hurt your attacker back is resistance rather than
  opposition") applies to *any* imposed effect, not just blows -- but players won't
  realize they may *oppose* a dazzle, a Boost, etc. rather than merely resist it.
  Add one clarifying line on the Resistance page (or a margin note) so every effect
  inherits it; do NOT build a subsystem. Surfaced during the Tricks / "The Opener"
  discussion (`_scratch/`).
- **Opposing a *guaranteed / Released* effect (resolved -- needs a wording fix).** Call
  a Released spell "guaranteed, no *reroll*," NOT "no roll." The banked value *is* the
  caster's stored roll on that spell, so it's contestable like any result: resist to
  cancel it, or oppose it (the banked value stands as the number to beat, the difference
  resolves, no reroll). This removes the apparent contradiction between "guaranteed" and
  "opposed contest." Action: reword the Release definition in the Spellweaver text to
  "no reroll," and confirm the resist/oppose choice carries over to it.
- **Hooks cut both ways -- an opponent may use your Hook against you.** The site only
  states the character-side half (`hooks.html`: "add your Hook's current rank to any
  roll where it's relevant; the GM may also apply it for free when it obviously fits").
  The reciprocal is missing: when a Hook (a drive, fear, addiction, or nature) is
  relevant *against* the character, the GM may add its rank to the opposing roll, or to
  the situation's DL. It's implied by the two-edged framing (Hooks complicate you; the
  GM triggers them hard and often) but never stated as a mechanic. Action: add a
  clarifying line to `hooks.html`/`.md` (and fold into the source) making the
  against-you application explicit. Surfaced 2026-07-14.

### Canon integration / source refactor (Tricks now canon)
- **Tricks is live and canon** (`L1/tricks.html` + `.md`, wired into `nav.html`
  after the Hooks chain; prev/next set between `hooks-on-credit` and `nonhuman`).
  The web now carries a rule the **source PDF does not**. Refactor the original
  document so the book and the site agree:
  - Add the **Tricks** section to the source rulebook (after the Hooks material).
  - Add one line to **`chargen`** (`.md`/`.html`) naming Tricks alongside Hooks as a
    standard, no-cost part of building a character. (Left to the author -- rulebook prose.)
  - Fold in the two clarifications above (resist/oppose on imposed effects; Release
    "no *reroll*") wherever the source text defines them.
  - Still-open author note (from `_scratch/tricks-page-draft.md`): the examples are
    western/sci-fi/demo flavor; consider a fantasy example or two so the page matches
    the book's default setting.

### Side-panel / rails follow-ups
- **Suppress rails on meta-pages**: `toc.html` and `settings.html` currently show
  the side panels (TOC beside the TOC, etc.). Suppress with a `body[data-no-rails]`
  check in `rails.js` if desired -- harmless for now.

### Infrastructure / ops
- **Domain email**: set up addresses on `silentbardgames.com`. Plan: move DNS
  from Namecheap to Cloudflare (registrar stays Namecheap; just change the
  nameservers), then use Cloudflare Email Routing (free) to forward
  `you@silentbardgames.com` to an existing inbox. Add Gmail "send as" or a
  mailbox provider (Zoho/Workspace) later if sending *from* the domain is
  needed. Keep GitHub Pages DNS records DNS-only at first so its TLS cert keeps
  working. Bonus: once DNS is on Cloudflare, binding R2 to
  `assets.silentbardgames.com` becomes trivial.

### Search (Lunr.js)
- **Client-side full-text search, no backend.** Prebuild a JSON index from page
  content (reuse the `html2md` / `extractFragment` DOM-walking; the `.md`
  mirrors are a ready corpus), ship it as a static file, query it in the browser
  with Lunr. Search box in the header; results show page title + snippet.
  Self-host the Lunr script on the CDN. Fuller writeup in
  `docs/dynamic-side-panels.md` section 13.
- **Curated alias / synonym map** (author-maintained, e.g. `search-aliases.json`).
  Maps common alternate or "wrong" terms to the right target so a query the
  rulebook text wouldn't otherwise match still lands -- the system renames
  familiar concepts, so players will search the D&D-ish word. Examples:
  "hit points" --> Harm & Recovery, "armor class" --> Armor, "mana / spell
  points" --> Focus. Use it to expand the Lunr query and/or show a "See also"
  suggestion above the results. Adding a new redirect = one line in the JSON.
