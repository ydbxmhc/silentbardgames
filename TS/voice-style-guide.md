# Tesserae Sortis — Voice & Prose Style Guide

*A working reference for editing oracle card text (lexicon entries, per-card
page prose, In Play examples). Companion to `oracle-edit-notes.md` — same
status convention.*

**Status: PROPOSED · drafted 2026-07-05 · awaiting author's editing pass**

This governs *how we write*, not *what the cards say*. It does not authorize
changing meanings, names, or the Yes/No-and/but logic of any card — that's
still the author's call, flagged per the existing edit-notes process. This
guide is scoped to prose style only.

---

## The diagnosis

Compare what's already sitting on `TS/cards/2h.html`, one card, three prose
layers stacked on top of each other:

1. **Keyword line** (italic, right under the H2): *"Intelligence delivered
   cleanly, and more than was asked for. Someone was watching and what they
   saw benefits you."*
2. **Body paragraph** (the thing we're fixing): *"Patience on the high ground
   has paid. The report that comes back is better than what was asked for:
   not just where, but when, and who, and how often. Somewhere in the extra
   detail is the lead you did not know to request. Read it twice; the second
   reading is where the gift is."*
3. **In Play example**: *"Sera's lookout comes back with the patrol's route,
   its timing, and the name of the officer who sets it."*

Layer 1 already told the reader everything the card means. Layer 2's job is
to add texture the reader doesn't have yet — and instead it mostly re-tells
layer 1 in longer sentences ("Patience on the high ground has paid" is a
poetic restatement of "someone was watching," not new information). That's
the abstraction problem in one sentence: **the paragraph is doing summary's
job with novel's word count.**

The author's rewrite fixes it by compressing, not by cutting content:

> The report is better than hoped: not just where, but when, who, and how
> often, with details you didn't know to request. Read it twice; there's
> more between the lines.

Same facts. Fewer words asked to carry each one.

---

## Principles

**1. Each layer earns its keep or gets cut.**
Before polishing a body paragraph, ask what it says that the keyword line
above it hasn't already said. If the answer is "nothing, just prettier,"
that's the edit — not a proofread, a structural fix.

**2. Compress lists; don't narrate them.**
"Not just where, but when, and who, and how often" → "not just where, but
when, who, and how often." Every "and" you can drop from a list without
losing rhythm, drop.

**3. Reach for the worn phrase over the invented one.**
"There's more between the lines" costs the reader nothing — it's a phrase
they already own. "The second reading is where the gift is" makes them
decode a metaphor mid-sentence. A familiar idiom that lands instantly beats
a novel one that's merely accurate. Save the invented image for when it's
actually doing work no stock phrase can.

**4. Contractions are the correct register here.**
"Didn't," "there's," "isn't" — not formality tics to iron out. The author's
version uses them; the original avoided them and reads stiffer for it. This
is a reference a player reads mid-session, not liturgy.

**5. Cut throat-clearing.**
"Patience on the high ground has paid" sets a mood the keyword line already
set. If a sentence's only job is atmosphere the reader's already standing
in, it's a candidate for the cut, not the polish.

**6. Length is a side effect, not the goal.**
The brief said it plainly: *doesn't have to be shorter.* The test isn't word
count, it's whether every remaining word is pulling weight. A paragraph that
earns its length by delivering something new in every clause is fine. One
that pads is not, regardless of how it counts out.

**7. Concrete noun over abstract summary noun, when there's a choice.**
"The lead you did not know to request" is already fine and concrete. Watch
for places where the instinct runs the other way — toward "insight,"
"opportunity," "benefit" as placeholders for a specific thing. Name the
thing.

**8. Semicolon-plus-punchline is a device, not a default.**
Both versions of 2H end on "Read it twice; [payoff]." That construction — a
short setup, a semicolon, a short landing clause — lands hard *because* it's
rare. Ration it. Used on every card it stops being a punch and starts being
a tic. Keep it in the kit for the card whose ending actually wants that
beat; let other cards close a different way — a flat statement, a question,
a fragment, nothing at all. Sentence structure should vary card to card on
principle, not just for this one device.

**9. In Play examples address the player, not a stand-in.**
**Convention change, 2026-07-05.** Earlier drafts (and the existing
lexicon prose in `oracle-master.md`) use named third-person characters for
every example — Sera's lookout, Thrn's escape, Calder's whole session.
Going forward, a card's own In Play example speaks to **"you"** directly:
"your lookout," "you can use them." The reader mid-session *is* the player
character; second person is more visceral than watching a stand-in do it.
**Mira in the Market is the deliberate exception** — she's a fixed,
always-the-same character, not the reader, so her vignettes stay third
person throughout, on every card.
This applies as each card gets its rewrite pass, not as a mechanical
find-and-replace across the existing master text — some of those named
examples carry detail (a name reused elsewhere, a running NPC) worth
checking before converting rather than assuming.

**10. Keyword-line fragments are separated by semicolons, not commas.**
Both the header's three keyword phrases and the Crossed line's three
keyword phrases are fragments, not a sentence — no conjunction before the
last item, no closing period, and semicolons between them rather than
commas. Commas read as though the phrases are sub-items of one continuous
list; semicolons treat each phrase as its own small unit, which is the
correct reading since each one is doing a different kind of interpretive
work (sound / sight / relationship, in 2H's case). Applies to every card,
both lines, header and Crossed alike:
> **2H (Sniper)** - a startling signal with a range-finding echo; a longer
> view of the big picture; the gift of a revealed admirer
>
> *__Crossed__ - Knowing too much; a source exposed; an overly ardent
> admirer*

---

## Already-on-model — don't "fix" these

Pulled straight from `oracle-master.md`'s pip lexicon. These are the target,
not the exception:

> **AH – Champion's Glory.** *The fighter's triumph spills over into
> celebration. The crowd is cheering and something beyond victory arrives
> with it.*

> **AC – Berserker's Rampage.** *Something let loose and made everything
> worse. The violence escalated past any useful point and kept going.*

> **8S – Hollow Leg.** *The medicine went in and nothing changed. The
> patient is still upright, still moving, still here. Failed healing that
> somehow left something intact.*

> **9S – Sage's Rescheduling.** *The Sage couldn't see you today. The
> knowledge is delayed, not denied. The appointment exists. Progress without
> result.*

Two to four short sentences, one concrete image each, no restated summary,
landing on a short clause. That's the voice. The per-card page prose (which
expands these into Upright/Inverted/In Play) is where the drift crept in —
because "expand" got read as "add more sentences" instead of "add more
information."

---

## Editing checklist (run this on a paragraph before calling it done)

- Does this sentence say anything the keyword line above it didn't already
  say? If not, cut it or replace it.
- Read it aloud. Any clause asking for a breath the sentence doesn't need?
- Any spelled-out list ("not just X, but Y, and Z, and also W") that
  compresses without losing rhythm?
- Any invented metaphor where a worn idiom would land faster?
- Any formal construction blocking a contraction for no reason?
- Would cutting this sentence change what the reader understands? If not,
  it's cut, not trimmed.

---

## Resolved (2026-07-05 discussion)

- **Numeric guardrail:** no hard ceiling. Length earns its place by what it
  delivers, not by a word count — the checklist governs, a number doesn't.
- **Design-note prose** (the italicized meta-commentary throughout the
  master, e.g. "Design note on color...") is **out of scope** for this
  guide. It's the author talking *to the reader* *about* the text — an
  aside, not part of the text itself — and is deliberately more expository
  and informal. Don't run it through the card-prose checklist.
- **In Play examples:** provisionally in scope but already close to
  on-model (Sera's lookout, Thrn's escape read tight as-is). No changes
  expected here beyond a spot check once the page-structure question below
  is settled.

## Open — page structure (tracked in `oracle-edit-notes.md`, N8)

The remaining "does scope include the lexicon one-liners" question turned
out to be the wrong question. Each section of a card page has its own job
and its own register (header / primary reading / secondary reading / In
Play / design note), and the per-section rules only make sense once the
section list itself is settled — including stripping the redundant
notation footer and renaming "Inverted" to something the mechanic actually
supports. That structural discussion is logged as **N8** in
`TS/oracle-edit-notes.md`, following the existing proposal/discuss/apply
process for anything touching the master or the page templates.

Nothing in this guide or in N8 touches actual card wording yet. First test
case, whenever ready: run 2H through the finished checklist *and* the
finished page structure together, confirm both tools work, then move on to
the other 53.
