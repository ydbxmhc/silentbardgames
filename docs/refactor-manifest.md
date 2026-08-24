# Refactor Manifest - SilentBardGames / L1

Working document for the site refactor begun 2026-08-24. One place to hold every
change, its blast radius, its dependencies, and its status, so the work survives
across sessions and nobody has to remember any of it.

**This file is process, not rulebook content.** Nothing here is canon. Anything
Claude inferred, proposed, or reformulated carries `@@*` and stays noncanon until
the author formally clears it.

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

## Open decisions (nothing downstream moves until these land)

1. **Exact filename for the renamed Kessa page.** Title is settled as *Starting
   Out*. Proposal: `starting-out.html` / `starting-out.md`, matching the
   hyphenated-lowercase convention used everywhere else in `L1/`. `@@*`
2. **Redirect stub at the old `quickstart.html` path?** The new quick start takes
   over that URL, so any existing bookmark or outbound link lands on a different
   page than it did. Options: (a) accept it, site is young; (b) leave a one-line
   meta-refresh stub - but the freed name is immediately reoccupied, so a stub
   would have to live at the *new* name instead, which defeats the purpose.
   Realistically this is a yes/no on (a). `@@*`
3. **Where the Recovery Trope lives.** Is it a titled section inside the new
   quick start, a callout box within it, or its own short page? It is an
   in-fiction justification device rather than a procedure, which argues for a
   box or a section rather than a page of its own - but it is also a *named*
   trope players will want to link to and cite, which argues the other way. `@@*`
4. **What happens to `safety.html`.** Absorbed into Session Zero and deleted
   (its prev/next chain between `magick/beyond` and `glossary` then needs
   mending), or kept as a short appendix entry that points forward to Session
   Zero? `@@*`
5. **Nav placement of Session Zero.** End of Getting Started, or somewhere more
   prominent still? "More prominent" was the stated goal for the safety material;
   naming the slot pins it. `@@*`

---

## A. Rename the Kessa walkthrough to *Starting Out*

**Status:** `READY` (pending decision 1)

**What:** `L1/quickstart.html` + `.md` become `L1/starting-out.html` + `.md`.
Page `<title>`, `<h1>`, breadcrumb, and every inbound reference update to
*Starting Out*. Page content itself is untouched - not one word.

**Why:** The page is a worked example of the standard build, offered up front for
readers who learn from a finished specimen and then run with it. `chargen.html`
is the same ground laid out in ink for readers who want the methodology. Both are
deliberate. Only the label was wrong, and it was squatting on the name the real
quick start needs.

**Blast radius** - 12 files, all mechanical, no prose changes:

| File | Change |
| --- | --- |
| `L1/quickstart.html` | rename; title, h1, breadcrumb, next-link |
| `L1/quickstart.md` | rename; heading, breadcrumb, next-link |
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
`#negotiating-details`, `#character-drives`, `#putting-it-together`) survive the
rename unchanged; only the file part of each href moves.

**Depends on:** nothing. This can go first.

**Note:** `nav.html` and `toc.html` are both listed in `CLAUDE.md` as
do-not-modify-without-explicit-instruction. This item is the explicit
instruction; recording that here so the exception is on the record rather than
assumed.

---

## B. The real Quick Start

**Status:** `BLOCKED` - author prose required

**What:** A new `L1/quickstart.html` occupying the freed name. The procedure, as
the author described it: sit down and start playing. Declare name, Hook, Roles
and Maneuvers as they come up, until the starting Karma is spent. No build step
before play.

**Why:** There was no quick start. There was an example of the standard setup
wearing the name.

**Division of labor:** This is new design, not a PDF transcription. **The author
writes every word of the prose.** Claude scaffolds the HTML shell to site
convention - CSS and script load order, breadcrumb, section ids, prev/next
wiring, nav and TOC entries - with `@@` placeholders where the text goes.

**Proposed reading chain** `@@*`:

    This is a Game?  ->  The Core Loop  ->  Quick Start  ->  Starting Out  ->  Core Mechanics

Rationale: a reader cannot "just start playing" without the Core Loop, so the
quick start sits after it. *Starting Out* then follows as the worked example, and
`core-mechanics` picks up its prev-link from *Starting Out* instead of from
`quickstart`. This ordering costs exactly two link edits beyond item A.

**Depends on:** A (frees the name), and decision 3 (whether the Recovery Trope
lands inside this page).

---

## C. The Recovery Trope

**Status:** `BLOCKED` - author prose required; placement is decision 3

**What it is,** restated from the author's description so the earlier
misunderstanding in `CLAUDE.md` does not propagate: it is the *in-fiction
explanation* for why a competent, established character is only now buying the
first rank of a Role they supposedly always had. They were injured, they are
recovering, and they cannot yet manage the full use of their own skills. That
lets a player declare a Level 1 character who is a known badass and then make
good on the claim as play proceeds, instead of being a newcomer to the world by
mechanical default. `@@*`

**What it is not:** the quick start itself. The retroactive-allocation procedure
is the quick start (item B); the Recovery Trope is the story that makes it feel
earned rather than arbitrary.

**Correction owed to `CLAUDE.md`:** the existing backlog entry conflates the two,
describing the Recovery Trope as the quick-start section. That entry needs
rewriting once B and C settle, and the two open questions logged under it there
(deadline on the retroactive spend; whether you may flashback-justify something
already attempted) belong to **B**, not to C. The parked "reincarnates make
viable PCs" cross-reference belongs to **C**, since remembering a prior life's
skill is the same device with different fiction.

**Depends on:** B.

---

## D. Session Zero page, and promoting the safety material

**Status:** `BLOCKED` - author prose required; decisions 4 and 5

**What:** A new Session Zero page covering table setup before play - C.A.T.S.
(Concept, Aim, Tone, Subject matter), lines and veils, the open-door policy, and
content warnings. Largely a rewrite and expansion of the current `safety.html`,
which already carries all four in about twenty lines and is buried as the first
entry under Appendices, sitting between *The Beyond* and *Glossary*.

**Inbound links wanted:**

- a closing note at the foot of *Starting Out* (item A)
- from `chargen.html`
- wherever else safety currently gets a passing mention (audit during item F)

**Why the promotion:** safety tooling is a before-you-play concern reachable only
by scrolling past the entire rulebook. Moving it forward makes it findable at the
moment it is useful.

**Depends on:** A (for the closing note), decisions 4 and 5.

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

**Method:** a section-by-section diff, digest against site, with an author ruling
on each divergence as to which side is canon. Then back-port in the ruled
direction. Small batches, verified, as with everything else here.

**Blocker on method:** `WIP/core-rules-digest.md` is useless as a diff target.
`html2md.py` flattened the whole file into an unbroken wall of prose with **zero
surviving headings** - the `<section>` wrapper defeats it. Either diff HTML to
HTML, or write a proper extractor first. See item G.

**Depends on:** A, B, F. Deliberately last.

---

## F. Link and anchor audit

**Status:** `READY` - read-only, changes nothing, produces a report

**What:** Sweep every internal `href` in `L1/` and its subfolders; resolve every
`#anchor` against the ids that actually exist on the target page; check the `.md`
mirrors separately, since they drift on their own schedule and have drifted
before. Output is a findings report, not edits.

**Why now:** it tells us what is already broken *before* we add pages, so new
breakage is distinguishable from old.

**Depends on:** nothing. Best run before A, so the rename's damage is visible
against a known-clean baseline.

---

## G. Tooling repairs

**Status:** `READY` for G1; G2 and G3 already logged in `CLAUDE.md`

- **G1. `html2md.py` drops headings inside `<section>`.** New finding, 2026-08-24.
  `WIP/core-rules-digest.md` contains not a single `#`, despite its HTML carrying
  eighty-odd `<h1>`/`<h2>` elements. This is the same class of bug as the two
  already logged, and it is what blocks item E's diff.
- **G2. `html2md.py` flattens `<table>`.** Already logged. Affects
  `assist-rule.html`, where the reference table's cells fuse into one line.
- **G3. `anchor_sections.py` writes CRLF on Windows.** Already logged. Matters
  more than the other two because this tool writes `toc.html` and `nav.html`,
  both of which item A touches.

**Recommendation:** fix G3 before item A runs, or item A's `toc.html` edit may
come back with the wrong line endings and fight `.gitattributes`. `@@*`

---

## H. Side quests

Bucket for whatever surfaces. Nothing is here yet. Items get promoted out of this
list into a lettered item of their own once they are more than a note.

---

## Decisions Log

| Date | Decision |
| --- | --- |
| 2026-08-24 | The Kessa walkthrough is renamed *Starting Out*. Its redundancy with `chargen` is intentional: example-first readers and methodology-first readers are separate audiences. |
| 2026-08-24 | The Recovery Trope is the in-fiction justification for retroactive skill purchase, not the quick-start procedure itself. Supersedes the conflated description in `CLAUDE.md`. |
