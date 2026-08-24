# Refactor Manifest - SilentBardGames / L1

Working document for the site refactor begun 2026-08-24. One place to hold every
change, its blast radius, its dependencies, and its status, so the work survives
across sessions and nobody has to remember any of it.

**This file is process, not rulebook content.** Nothing here is canon. Anything
Claude inferred, proposed, or reformulated carries `@@*` and stays noncanon until
the author formally clears it.

Companion document: `docs/link-audit-2026-08-24.md`, the pre-refactor baseline.

---

## How to read this

| Status | Meaning |
| --- | --- |
| `BLOCKED` | Waiting on an author decision named in the item |
| `READY` | Fully specified, waiting only on a go |
| `DOING` | In progress this session |
| `DONE` | Complete and committed; date recorded in the Decisions Log |
| `PARKED` | Real work, deliberately not now |

Items are lettered so they can be referred to in chat without retyping them.

---

## Open decisions

1. **Does the new quick start keep the name `quickstart.html`?** It now lives in
   the Characters section as an alternate build method, not in Getting Started,
   so the name is descriptive of what it does for the *player* rather than where
   it sits. Keeping it means old bookmarks to `quickstart.html` land on a
   different page in a different section. The site is young; accepting that is a
   legitimate answer, and it costs nothing to decide later. `@@*`
2. **The named-callout standard** - see item I. Blocks C, and probably wants
   settling before any new page is written, since new pages will use it.

Resolved decisions have moved to the Decisions Log at the foot of this file.

---

## A. Rename the Kessa walkthrough to *Starting Out*

**Status:** `READY`

**What:** `L1/quickstart.html` + `.md` become `L1/starting-out.html` + `.md`.
Page `<title>`, `<h1>`, breadcrumb, and every inbound reference update to
*Starting Out*. Page content itself is untouched - not one word.

**Why:** The page is a worked example of the standard build, offered up front for
readers who learn from a finished specimen and then run with it. `chargen.html`
is the same ground laid out in ink for readers who want the methodology. Both are
deliberate and neither is redundant. Only the label was wrong, and it was
squatting on the name the real quick start wanted.

**Position is unchanged.** *Starting Out* stays exactly where the Kessa page
already sits, third in Getting Started:

    This is a Game?  ->  The Core Loop  ->  Starting Out  ->  Core Mechanics

**Blast radius** - 12 files, all mechanical, no prose changes:

| File | Change |
| --- | --- |
| `L1/quickstart.html` | rename; title, h1, breadcrumb |
| `L1/quickstart.md` | rename; heading, breadcrumb |
| `L1/nav.html` | `Quick Start` item retargeted and relabelled |
| `L1/nav.md` | mirror |
| `L1/toc.html` | entry plus five anchor children |
| `L1/toc.md` | mirror |
| `L1/index.html` | landing link |
| `L1/index.md` | mirror |
| `L1/core-loop.html` | next-link |
| `L1/core-loop.md` | next-link |
| `L1/core-mechanics.html` | prev-link |
| `L1/core-mechanics.md` | prev-link |

Also `Settings/Vigil/SESSION-BOOT.md` line 127 names `quickstart.md` in its
orientation table. Repo-internal, not a site link, but it goes stale if missed.

The five anchors in `toc.html` (`#character-concept`, `#roles-and-maneuvers`,
`#negotiating-details`, `#character-drives`, `#putting-it-together`) survive
unchanged; only the file part of each href moves.

**Depends on:** nothing. This goes first.

**Note:** `nav.html` and `toc.html` are both listed in `CLAUDE.md` as
do-not-modify-without-explicit-instruction. This item is the explicit
instruction; recorded here so the exception is on the record rather than assumed.

---

## B. The real Quick Start - an alternate build method

**Status:** `BLOCKED` - author prose required

**What it is:** a new page in the **Characters** section, beside `chargen`, not
in Getting Started. It is an alternate character-creation method, aimed at an
**experienced GM** running players of any experience level.

The procedure, as the author described it: sit down and start playing. Declare
name, Hook, Roles and Maneuvers as the fiction calls for them, until the starting
Karma is spent. No build step before play.

**Who it is for**, in the author's framing:

- new players, who get to ease in instead of facing a build sheet cold
- experienced players who would rather defer deciding what they want to play
- one-shots, where a build session is most of the budget
- the old hand who lets the new folk take whatever they like, then fills the
  gaps in the party with his own PC as play reveals what is missing

**Default timing:** the spend completes over session 1. A group that dislikes the
end-of-session limitation may simply discard it. Author-stated in conversation
2026-08-24, not yet written into the rules, therefore not ratified. `@@*`

**Cross-link required:** the page must point at *Starting Out* early, since the
two now sit in different sections and a reader arriving at the quick start may
never have seen the worked example.

**Division of labor:** This is new design, not a PDF transcription. **The author
writes every word of the prose.** Claude scaffolds the HTML shell to site
convention - CSS and script load order, breadcrumb, section ids, prev/next
wiring, nav and TOC entries - with `@@` placeholders where the text goes.

**Open questions inherited from the `CLAUDE.md` backlog**, which belong to this
item rather than to C:

- What is the deadline or cap on the retroactive spend? All of it by end of
  session one, or a set number of declarations?
- May a player flashback-justify something already *attempted* - "I always had
  lockpicks," declared after trying the door - or only declare forward?

**Depends on:** A (frees the name, if decision 1 keeps it), I (callout standard).

---

## C. The Recovery Trope

**Status:** `BLOCKED` - author prose required; needs item I

**What it is,** restated from the author's description so the conflation in
`CLAUDE.md` does not propagate: the *in-fiction explanation* for why a competent,
established character is only now buying the first rank of a Role they supposedly
always had. They were injured, they are recovering, and they cannot yet manage
the full use of their own skills. That lets a player declare a Level 1 character
who is a known badass and then make good on the claim as play proceeds, instead
of being a newcomer to the world by mechanical default. `@@*`

**What it is not:** the quick start itself. The retroactive-allocation procedure
is the quick start (item B). The Recovery Trope is *one example* of a story that
makes it feel earned rather than arbitrary - the author was explicit that it is
an example and not a requirement. Other justifications are equally valid and the
text should not imply otherwise.

**Form:** a callout box within the quick-start page, carrying its own heading and
its own TOC entry. That combination is exactly what item I has to make possible.

**Correction owed to `CLAUDE.md`:** the existing backlog entry describes the
Recovery Trope as the quick-start section itself. That entry wants rewriting once
B and C settle. Its two open questions have been reassigned to B above. The
parked "reincarnates make viable PCs" cross-reference belongs here, since
remembering a prior life's skill is the same device wearing different fiction.

**Depends on:** B, I.

---

## D. Session Zero

**Status:** `BLOCKED` - author prose required

**What:** A new Session Zero page covering table setup before play - C.A.T.S.
(Concept, Aim, Tone, Subject matter), lines and veils, the open-door policy, and
content warnings.

**Placement:** in the Characters section, near `chargen` and the new quick start.
The three belong together: all are things to settle before diving into a
campaign, or even a one-shot - compressed hard if three hours is all you have.

**Relationship to `safety.html`:** unresolved on purpose. Safety will most likely
stay a page of its own, but that cannot be known until Session Zero is actually
written and we see what it absorbs. Not to be pre-decided. If safety does end up
folded in, its prev/next chain between *The Beyond* and *Glossary* needs mending
at that time.

**Inbound links wanted:**

- a closing note at the foot of *Starting Out* (item A)
- from `chargen.html`
- wherever else safety currently gets a passing mention

**Depends on:** A (for the closing note).

---

## E. Reconcile the digest against the site

**Status:** `PARKED` until the site is stable - this is the large one

**What:** `WIP/core-rules-digest.html` is a single self-contained file laid out
for half-letter print: `@page{size:5.5in 8.5in}`, parchment ground, Georgia,
paged.js class hooks, art served from R2. Roughly eighty headings, running the
full core spine from *This is a Game?* through to *Spending Karma*.

**The finding that makes this urgent:** the digest text has **already diverged
from the site text.** It is a different revision, not a copy. First line of the
Kessa dialogue, as proof:

- site: *"her name is Kessa - she's a smart-mouthed thief who grew up in the merchant quarter"*
- digest: *"her name is Kessa - she's a smart-mouthed thief! She grew up in the merchant quarter"*

Nobody has been tracking which side is newer. Until that is established, editing
either copy risks overwriting good work with older work.

**Provenance, from the link audit:** all 324 internal links in the digest point at
`.md` targets. It was assembled from Markdown - the mirrors or a source document
- and never had its hrefs converted. So the digest is downstream of a Markdown
snapshot, and the divergences are most likely author edits made in the digest
after that snapshot. Worth confirming before ruling on canon. `@@*`

**Method:** a section-by-section diff, digest against site, with an author ruling
on each divergence. Then back-port in the ruled direction. Small batches,
verified, as with everything else.

**Blocker on method:** `WIP/core-rules-digest.md` is useless as a diff target.
`html2md.py` flattened the whole file into an unbroken wall of prose with **zero
surviving headings** - the `<section>` wrapper defeats it. Either diff HTML to
HTML, or write a proper extractor first. See item G.

**Depends on:** A, B, F. Deliberately last.

---

## F. Link and anchor audit

**Status:** `DONE` 2026-08-24 - see `docs/link-audit-2026-08-24.md`

**Result in one line:** the live `L1/` site is clean. Zero broken nav targets,
zero broken anchors in any `.html`. All 28 defects found are in the `.md`
mirrors, invisible to site readers, and all of them are generator bugs rather
than content bugs. `TS/` is in materially worse repair and is out of scope.

Re-run after each batch of edits. The script currently lives outside the repo; it
belongs in `tools/` if it earns a permanent home.

---

## G. Tooling repairs

**Status:** `READY`

Four generator defects, three of which now block or complicate other items.

- **G1. `html2md.py` drops headings inside `<section>`.** New, 2026-08-24.
  `WIP/core-rules-digest.md` contains not a single `#` despite eighty-odd
  headings in its HTML. Blocks item E's diff.
- **G2. `html2md.py` flattens `<table>`.** Already logged in `CLAUDE.md`. Affects
  `assist-rule.html`, whose reference table fuses into one line.
- **G3. `anchor_sections.py` writes CRLF on Windows.** Already logged. Matters
  most of the four, because this tool writes `toc.html` and `nav.html`, both of
  which item A touches. **Fix before A runs**, or A's output fights
  `.gitattributes eol=lf`. `@@*`
- **G4. `html2md.py` mangles links and images.** New, from the audit. Three
  faces, one pass to fix: fragments are not re-slugged for Markdown headings;
  anchors on `<dt>` and `<sup>` are dropped entirely, killing all 51 glossary
  anchors in the mirror; and image sources are reduced to bare filenames instead
  of keeping the absolute R2 URL. Detail and proposed fixes in the audit
  document.

**Note on sequencing:** hand-editing the mirrors to fix G4's symptoms would be
undone by the next regeneration. Fix the generator, then regenerate wholesale.

---

## H. Side quests

Bucket for whatever surfaces. Items get promoted out of here into a lettered item
once they are more than a note.

- `TS/` link rot: 54 broken nav targets, 43 broken anchors, 55 missing images,
  the latter being the entire card deck. Out of scope, recorded so it is not
  forgotten.
- `git gc` wanted on the author's side; the sandbox leaves stray unlinkable temp
  objects in `.git/objects` when it commits through the mount.

---

## I. A standard for named callouts

**Status:** `BLOCKED` - author decision; blocks B and C

**The problem, as surfaced by the Recovery Trope:** some callouts are decorative
asides, and some are *named things* readers will want to cite, link to, and find
in the table of contents. The Recovery Trope is the second kind. So are several
existing blocks that the book would otherwise have called sidebars - for example
*The Power of Good Representation* in `chargen.html`.

Right now there is no convention distinguishing them, which means each one gets
handled ad hoc and none of them are addressable.

**What a standard has to settle:**

- a CSS class, or a class pair, marking the named kind distinctly from a plain
  aside
- what heading level a named callout carries, and whether it interrupts the
  page's outline or sits outside it
- that it takes an `id`, so it can be linked to directly
- whether and how it appears in `toc.html` - as a nested child of its section, or
  visually distinguished as a callout rather than a heading
- what `anchor_sections.py` and the TOC generator must do with it automatically,
  so the convention survives regeneration
- how it prints in the half-letter digest, which already styles `blockquote` for
  this role but has no named variant

**Why it comes first:** every new page in items B, C and D will want at least one
of these. Settling it now means they are built to convention instead of being
retrofitted. `@@*`

**A survey of existing callouts is wanted before deciding** - how many there are,
how they are currently marked up, and which are named. Cheap, read-only, and I
can run it on request.

---

## Decisions Log

| Date | Decision |
| --- | --- |
| 2026-08-24 | The Kessa walkthrough is renamed *Starting Out*, filename `starting-out.html`. Its overlap with `chargen` is intentional: example-first readers and methodology-first readers are separate audiences. |
| 2026-08-24 | The Recovery Trope is an in-fiction justification for retroactive skill purchase, and only one possible example of such. It is not the quick-start procedure. Supersedes the conflated description in `CLAUDE.md`. |
| 2026-08-24 | The new quick start is an alternate build method living in the Characters section beside `chargen`, not a front-door page in Getting Started. Getting Started keeps its existing three-page shape. |
| 2026-08-24 | The Recovery Trope takes the form of a callout box with its own heading and its own TOC entry, pending the standard in item I. |
| 2026-08-24 | Session Zero lands in the Characters section near `chargen` and the quick start. |
| 2026-08-24 | `safety.html` most likely remains its own page, but the question stays open until Session Zero is written. Deliberately not pre-decided. |
