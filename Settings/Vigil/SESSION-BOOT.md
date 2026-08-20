# Vigil -- Session Boot Guide

*Written 2026-08-08 for a fresh session picking up the **Vigil** superhero setting.*

Repo root: `c:\Users\P2759474\silentbardgames`

## Boot sequence -- do these in order

1. **Activate the two manual steering files** (section 1). Do not skip; do not wait to be
   asked.
2. **Read `/CLAUDE.md` in full** (section 1).
3. **Read the L1 rules** listed in sections 3a and 3b. Batch them.
4. **Read `Settings/Vigil/supers-in-level-one.md`** -- the current working draft, and the
   thing you will actually be editing. Everything in it is unratified.
5. **Skim `Settings/Accord/firefly-reference.md`** -- optional but useful. A worked example
   of converting known fiction into L1 characters, and the source of the 10-Karma
   calibration.
6. **Ask the author the questions in section 7** before proposing anything.

Then stop and check in. Do not begin generating proposals or setting material until he has
steered.

---

## 1. Steering -- do this FIRST, before any other work

Two steering files require **manual activation** and will not appear on their own.
Activate both immediately with `disclose_context`:

- **`c:\Users\P2759474\.kiro\steering\collaboration.md`** -- pacing and collaboration.
  **This is the most important file in the repo for how to behave.** The previous session
  failed to read it until prompted and made exactly the mistake it warns about.
- **`c:\Users\P2759474\.kiro\steering\windows-git-bash.md`** -- the shell is **Git Bash**,
  not PowerShell or cmd. Also bash coding standards and the no-non-ASCII rule.

These arrive automatically as Included Rules, but know they exist: `stderr-handling.md`,
`shell-command-padding.md`, `pre-push-secret-scan.md`, `infra-runners.md`.

Then **read `/CLAUDE.md` in full.** Not just a section. It is the repo's own steering file
and contains the Prime Directive, the `@@*` convention, workflow limits, and repo structure.

---

## 2. The rules that matter most

**Don't run off without me.** The author has significant ADHD and the shared screen is
append-only -- he cannot scroll back while output is still arriving. Work in small visible
steps. Stop often. If a turn's output exceeds roughly a screen, stop and let him read
before continuing. The harm is blind unsupervised chaining, not lack of permission.

**Everything you invent gets `@@*`.** Rules, mechanics, names, definitions, builds,
setting details, analytical conclusions. All of it. See `/CLAUDE.md` for the convention.

**Conversation is not validation.** His words: *"in conversation is never official until
stamped and approved."* A discussion that went well still leaves content tagged `@@*`.
Only an explicit formal decision clears it, and clearing is his action, not yours.

**ASCII only.** No em-dashes, no arrows, no typographic quotes. Use `--` and `->`. A
`dedash-on-save` hook runs `tools/dedash.py` automatically, but it likely only catches
em-dashes, not arrows or other non-ASCII. Check your own output with
`grep -cP '[^\x00-\x7F]'`.

Also: **ask whether he is out of a file and saved before editing it.** Check the open-editor
context every turn. The previous session edited an open file repeatedly without asking.

### What the previous session actually got wrong -- learn from these, don't repeat them

**It did not activate `collaboration.md` until told to look for it.** This is the root
cause of everything below. Do section 1 first, without being asked.

**It was asked for a folder and produced a 200-line rules document**, written in
declarative voice as though the mechanics were settled. The author's response: *"you are
writing into putative canon declarations you made."* Scope your output to what was actually
requested; propose in conversation before writing proposals into files.

**It asserted things it had not checked.** Twice. It claimed the `Next ->` footer chain
skipped pages without ever reading a footer, and it claimed the Karma cost curve was
undocumented when `spending-karma.md` contains it in full. Both were corrected by the
author. **Investigate before asserting** -- he is an experienced IT professional and a few
words from him will short-circuit a long hunt.

**It reversed the author's own terminology** (bubbler and wheezer) and had to be corrected,
because it inferred the meanings instead of asking.

**It chained multiple file edits and commits inside single turns.** `/CLAUDE.md` requires
consulting before changing multiple files in one go, and `collaboration.md` warns that
blind chaining is the specific harm.

None of these were disasters, and the author was gracious about all of them -- but every
one cost a correction cycle that a slower, more visible approach would have avoided.

---

## 3. What to read in the L1 rules

### How the rules files are laid out -- read this before opening anything

Every rules page exists **twice** in `/L1/`, as a matched pair sharing the same base name:

```
/L1/chargen.md      <-- READ THIS
/L1/chargen.html    <-- ignore
```

**Read only the `.md` files.** The `.html` versions are the published website build and
carry markup, navigation wiring, and CSS classes you do not need. The Markdown is the same
content, cleaner and cheaper to read. This holds throughout, including the subfolders:
`/L1/roles/`, `/L1/action/`, and `/L1/magick/` all follow the same paired pattern.

Every filename in the tables below is a `.md` file in `/L1/` unless a subfolder is shown.

**Use `/L1/toc.md` as your lookup.** It is a complete hierarchical manifest of the entire
book with links, so it serves as both a map and an index -- if you need to find where a
concept lives, search the toc rather than guessing at filenames or crawling the site. It is
also a better guide to structure than following the `Next ->` footer chain at the bottom of
each page, because the toc shows the hierarchy while the footer chain only shows sequence.

Read files in batches rather than one at a time. Reading order does not matter much for
comprehension since it all lands in the same context, but grouping related pages together
helps.

### 3a. Essential spine -- read all of this

| File | Why |
|---|---|
| `core-loop.md` | The resolution engine in four steps. EL, roll, count odds, compare. |
| `quickstart.md` | A full character built in dialogue. Best single orientation. |
| `karma.md` | How Karma is earned. **Contains the rank-scaled Hook trigger rule.** |
| `spending-karma.md` | **The cost curve.** Level costs its NEW value; everything else costs its CURRENT rating. Caps, and the one-advance-per-session limit. |

Then the character-building chain, `chargen.md` through `role-synergy.md` -- nineteen
pages that follow their own `Next ->` links cleanly:

`chargen` `hooks` `hooks-how-they-work` `crafting-good-hooks`
`self-hooking-and-table-courtesy` `common-pitfalls` `hooks-and-growth` `imposed-hooks`
`hooks-on-credit` `tricks` `nonhuman` `nonhuman-as-a-hook` `roles` `the-nature-of-roles`
`mechanical-function` `maneuvers` `the-sweet-spot` `examples-in-practice` `role-synergy`

### 3b. Critical for supers specifically

Superpowers are the reason this setting is hard, and these are the pages that bear on it.
The previous session deliberately skipped most of them, which limited what it could
propose.

| File | Bears on |
|---|---|
| `nonhuman.md` | **Conceits.** The demon who is *Immune To Fire* is a superpower already handled by the rules. This is the central mechanism. |
| `nonhuman-as-a-hook.md` | How inherent advantages get paid for, and what is free. |
| `glossary.md` | **Where Conceit is actually defined:** *"An unrated Truth (capital T) about the game or something in it."* Also a fast reference for every term in the system. |
| `hooks-on-credit.md` | Starting a Hook above rank 1 for extra Karma. Relevant to any proposal that trades powers for Hooks. |
| `imposed-hooks.md` | Mind control, curses, compulsions. Also the adoption mechanic. |
| `traits.md` | **Read this early.** States that *"Conceits are unrated Traits - narrative truths,"* which makes a Conceit formally a **subtype of Trait**. So the whole powers-as-Conceits question is really a question about the Traits system. Also covers behavioral, combat, area-effect, defensive, and vulnerability Traits, and creating new ones. |
| `actions-and-timing.md` | Free actions, Direct actions, Boosts, Boosts with duration. |
| `multiple-actions.md` and `wagered-actions.md` | **The speedster question.** A speedster wants more actions, not a bigger EL. |
| `resolving-combat.md` | The two-axis offense/defense model. |
| `harm.md`, `types-of-harm.md`, `feeling-down.md` | Invulnerability and durability Conceits need this. |
| `gear.md`, `what-gear-does.md`, `gear-traits.md`, `assist-rule.md` | Gear-based heroes: Iron Man, utility belts. |
| `luck.md`, `extreme-results.md`, `dice.md` | Luck Tokens, Extreme results, and the dice options. |

### 3c. Worth reading, though not required

- **`/Settings/Accord/firefly-reference.md`** -- Wash, Kaylee, Zoe, and Jayne converted to
  L1. The best available demonstration of the translation method, and the origin of the
  10-Karma calibration. Includes a Jayne-versus-Zoe comparison showing why breadth plus a
  good Maneuver beats raw depth at equal EL.
- **`/Settings/Accord/setting-notes.md`** -- shows the house format for setting notes, if
  and when Vigil needs one. Content is unrelated sci-fi; skim the structure, ignore the
  substance.

### 3d. Do not read unless asked

- `/L1/magick/` -- the magic system. Only relevant if Vigil has magic-based heroes.
- `/L1/roles/` and `/L1/action/` -- individual Role writeups and narrative vignettes.
  Useful later when building characters, not needed for orientation.
- `/Settings/Averond/` -- the fantasy setting. Large and unrelated.
- `/Settings/Accord/playtest-pregens.md` -- sci-fi characters, unrelated.
- `/TS/` -- unrelated.

---

## 4. Vocabulary discipline -- get this right

**Roles are narrow thematic verbs, not professions or backgrounds.**

> Loremaster **knows**. Sneak **sneaks**. Warrior **hits**. Sniper **shoots**.

"Knows the undercity" is **Loremaster**, not Sneak. A Sneak Maneuver may encode undercity
knowledge only insofar as it serves sneaking -- hiding places, sight lines, patrol
schedules. Cross-Role application is the interesting exception, never the baseline. The
previous session got corrected on precisely this.

**Maneuvers always display a rank**, even when using only the free rank from a Role.
Write `Pilot 2`, never bare `Pilot`.

**Every Role rank grants one free Maneuver rank**, usable to raise an existing Maneuver or
open a new one. Additional Maneuver ranks can be bought with Karma. A Role may not have
more Maneuvers than its rank.

**Sci-fi and modern lanes already settled in conversation** (still `@@*`): piloting is an
Athlete Maneuver, navigation is a Tinker Maneuver. No new Roles were needed. Expect the
same to hold for supers -- resist inventing Roles.

---

## 5. Current state of Vigil

**One file: `supers-in-level-one.md`.** It is a **discussion draft** and every item in it
is tagged `@@*`. It carries per-item status markers: `PROPOSAL`, `OBSERVATION`,
`OPEN QUESTION`. There is an empty **Decisions Log** at the bottom for ratified rulings.

**Nothing in it is a position to defend.** The author's own words about the proposals: he
will likely do things *"very similar, but not exactly the same."* Treat the file as an
agenda of things to discuss, and expect to discard or rewrite freely.

The single load-bearing proposal, flagged as such in the file, is that **Conceits grant no
dice** -- they provide narrative permission only, never a bonus. If that is wrong, most of
the rest needs rework. Argue about that one first.

**What is actually settled:** only the name. The author chose **Vigil**. **Sanction** is
reserved as a character name, **Warrant** is reserved for a future Western setting.

Setting material -- the world, factions, cities, tone -- **does not exist yet** and should
go in a new `setting-notes.md` in this folder, not into the mechanics draft.

---

## 6. Known gotchas and outstanding corrections

**`@@*` A correction that needs the author's decision.** `/CLAUDE.md` contains a logged
item describing "multiple Karma-paying Hook triggers per session" as an untested variance
invented for Pellan Atavism. **That is wrong.** `karma.md` already contains it as an
optional group rule scaled to Hook rank: a Hook at rank N may be triggered for Karma N
times per session before yielding Luck Tokens. The `CLAUDE.md` entry should be rewritten
as a question about whether that optional rule is on by default. Raise this early; do not
silently edit `CLAUDE.md`.

**Two rules from `spending-karma.md` that are easy to miss** and that invalidated some
earlier reasoning about pregens: a character must be **Rested and fully healed of Injury**
to raise Level, and a character **cannot hold more Karma than the cost of their next
Level**.

**A broken cross-reference in the rulebook, found 2026-08-08 and reported to the author --
not yet fixed.** Every mention of Conceit in `glossary.md`, `traits.md`, `gear-traits.md`,
`assist-rule.md`, `gear.md`, and `nonhuman.md` links to `hooks-in-play.md`, which never uses
the word. `oddball-rule.md` links it to `chargen.md` instead, a seventh and different
target. Either `hooks-in-play.md` is missing an intended Conceit section, or all those links
point at the wrong page. **Do not fix this without being asked** -- it is rulebook content
and falls under the Prime Directive. The working definition is in `glossary.md` and the
mechanical framing is in `traits.md`.

**Karma calibration.** Ten Karma produced characters that felt right for competent,
experienced figures -- see `Accord/firefly-reference.md`. Five is the recommended starting
figure in the rules, but starting Karma is explicitly a group choice and can be anything
from zero upward. Confirm the figure for Vigil rather than assuming.

**Git.** Working branch has been `claude/finish-website-rulebook-iQ7qN`. Commit only when
asked. Scan for secrets before pushing. Note that `grep` for secret markers throws false
positives on "Luck Token" and "work in secret"; filter known-benign matches and report the
remainder.

---

## 7. What to ask the author early

These are unanswered and shape everything:

- **What is Vigil actually about?** Tone, era, scale, whether powers are public or hidden,
  whether there is a registration or licensing regime. The name suggests self-appointed
  watchmen, which hints at unsanctioned heroes -- but that is inference, not canon.
- **Starting Karma and power level** for the intended playtest.
- **Table size.** Prior sessions assumed two players, occasionally three or four.
- **Whether to keep working up the difficulty ladder** in the draft (Rung 3 next would be
  Spider-Man or Wolverine), or to settle the speedster and gear questions first, or to
  abandon the ladder and build original Vigil characters instead.
