# HANDOFF - Level One solo playtest, Caria Greenhaven - RESUME S06 MID-SCENE

Spoiler-free. Lee may read this. It replaces "S06 Start Here." Saved 2026-10-01, about 20:30 Lee's clock, after the old chat (788 turns, several compactions) was archived to transcripts.

## Attach these to the new chat (in this order)
1. This file.
2. `2026-10-01 GM ONLY - S06 Resume Brief (spoilers).md` - the GM's working brief. Lee: attach it, don't read it.
3. `2026-10-01 CHARACTER - Caria Greenhaven (master file, through S06 save).md` - the sheet, every advancement, and the S06-in-progress state at the bottom.
4. `2026-10-01 GM ONLY - Cast Card (S06 save, spoilers).md` - NPC looks, manners, who knows what. GM only.
5. `2026-10-01 PLAYTEST - S06 Gap Log - Caria (cumulative).md` - the real deliverable, S1 to now.
6. `2026-10-01 SESSION - S06 Part 1 Summary - Every Prayer Has Weight.html` - what has happened this session.

Optional, if the GM asks for more:
- `2026-10-01 GM ONLY - S06 Ledger (spoilers, cumulative S1-S6).md` - the full private ledger (large; the GM should read the last section and search the rest, not read it whole).
- Earlier session summaries (S01-S05 HTML).

**Do NOT attach the two transcripts.** They are far too big for a chat. Keep them in the folder. If the new chat is linked to this computer with the Averond folder connected, the GM can search them there when a detail matters.
- `2026-10-01 TRANSCRIPT - Caria S1-S6 Play (story and table talk).md` - every word Lee and the GM wrote, timestamped.
- `2026-10-01 TRANSCRIPT - Caria S1-S6 Complete (verbatim, with tool calls).md` - the same plus every dice roll command and file write.

## For the GM (Lilita), first thing in the new chat
- Read, in order: the GM Resume Brief, the cast card, the sheet's S06 section, and the S06 Part 1 summary. Re-read the cast card after any compaction.
- Recreate the working folder and the roller as `game/roll.sh`:
```bash
#!/usr/bin/env bash
# L1 Simple Pool roller. Usage: roll.sh EL [extra_effort_dice] [label]
EL=${1:?EL required}; XE=${2:-0}; LABEL=${3:-roll}
N=$((EL+XE)); T=0; D=""
for ((i=0;i<N;i++)); do r=$((RANDOM%2)); D+="$r "; T=$((T+r)); done
echo "[$LABEL] EL$EL +${XE}XE -> ${N}d[0-1]: $D= $T"
if (( T > EL )); then echo "  OVER EL -> total failure (effect 0)"
elif (( T == 0 && N >= 3 )); then echo "  ALL ZEROES -> EXTREME FAILURE"
elif (( T == 0 )); then echo "  zero -> failure"
elif (( T == EL && T == N && N >= 3 )); then echo "  ALL MAX & = EL -> EXTREME SUCCESS"
else echo "  result $T"; fi
```
  Run as `./roll.sh EL 0 "label" 2>>stderr.log`. NEVER `2>/dev/null`. Never pipe `2>&1` into anything but `tee`.
- Copy the attached ledger/gap log/cast/sheet into the working folder as `ledger.md`, `gap-log.md`, `cast.md`, `caria.md`, and keep appending to them every beat.
- Rules live in the SilentBardGames repo: /L1/*.md only (ignore the .html), indexed by /L1/toc.md. Read the rule before saying it's missing. The repo is ASCII-only and its rulebook text is never edited.

## Table conventions
- Sandbox. Short beats, about one screen per turn. No branching menus at the end of a turn. No popup questions; ask in prose.
- Show the raw dice. Never fudge. On a roll that matters, offer "if it stands / Hook dice / if Tokened" outcomes and let Lee choose. Oracle: bare 2d (2 yes, 1 a sign, 0 no).
- Effect = roll minus Difficulty or opposition. Extremes need 3+ dice. A Luck Token makes a roll your EL.
- `<...>` is OOC. Unmarked speech is in character. Text after `---` is often Lee stepping out to ask the GM something.
- Write every NPC's dialogue from what that NPC actually knows. Flag stumbles on either side for retcon.
- Ask Lee before improvising a rule that ought to exist. Log it in the gap log: @@ MISSING / @@ UNCOMMITTED / @@ UNCLEAR / @@ OPEN / OK. Anything the GM invents is @@*.
- Hyphens with spaces, not em-dashes. Lee invites GM interruptions mid-speech.
- End of session: an HTML summary (collapsible sections), the sheet, the gap log, the GM ledger, and the Karma tally and spend.

## Rulings in force (cumulative highlights)
- Role Synergy: a Role counts if failing at it would visibly change the outcome.
- Hooks: the owner gets flat successes, a per-scene budget equal to rank. Hook alterations are always free. Hook budget may be spent on narrative presence (letting the mark show) without taking a trigger. Karma for up to Hook-rank triggers a session.
- Boost size: an optional guideline only (a Boost adds no more dice than the EL it boosts). Canon precedent: gear Boosts are capped at the user's Role rank.
- Double sessions: two improvements, one attendance Karma.
- Unbound Spellweaver ranks behave normally; an unbound known spell's full ritual is Level + unbound ranks (EL6).
- Spell endings: the world tends to put things back. Form reverts, place doesn't; what can't revert crumbles.
- Trick, See the Root: where a problem has a living or spiritual trace, Second Sight Boosts the diagnosis.
- Accords: over-giving creates counter-debt. A favor requested is a debt. A spirit's Hook can name its price. Renegotiating terms by restating their intent is a clarification, not a new favor.
- Every Role rank carries a Maneuver rank. Maneuvers may be stacked and renamed (Open Hands = Mediation + Diplomacy).

## Where we are
- **Scene:** Saltwind, the evening of Brother Aubric's burial. Mirna's back kitchen behind the lodge hall, dusk. Yard door open to the sea; a lamp on the scrubbed table; a folded cloth over a scorched brass button.
- **Present:** Caria; Mira Thousand-Voices (in the yard doorway, looking down the beach, silent); Brother Kade (on the stool by the hall door); Clerk Fennick (at the table, hands flat on the boards); Hollis under the table across Caria's feet. Asher is tending Mirna's lamps in the hall.
- **Last beat:** Caria has laid it out: the sliver that festers into gangrene, the great dark lode under the Mountain, Calder's leash. Kade: binding a thing that size takes its True Name. Fennick: "somehow" is usually paid for, and he enters those lines in a fair hand. Caria's thumb circles the rim of her cup. **Lee's move.**
- **Caria:** Level 4. Tokens 3/4. Karma 2 (+1 earmarked to Conjuror). Hook A Hint of Brimstone 4, with 2 of 4 left this scene and 1 trigger taken this session. No Harm; exhausted; a sulphur taste she can't rinse out.
- **Good Fun candidates so far:** the eulogy and dirge; Tessa's message; Jory counting her breaths.
