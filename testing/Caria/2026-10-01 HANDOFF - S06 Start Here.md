# HANDOFF - Level One solo playtest, Caria Greenhaven - start of S06

Spoiler-free. Lee may read this. Attach it to the new chat together with the files below.

## Attach these to the new chat
1. This file.
2. `2026-10-01 CHARACTER - Caria Greenhaven (after S05).md` - the current sheet.
3. `2026-10-01 CHARACTER - Caria Greenhaven (master file, all sessions).md` - background and every advancement.
4. `2026-10-01 PLAYTEST - S05 Gap Log - Caria.md` - the gap log for S1-S5, cumulative (the real deliverable).
5. `2026-10-01 GM ONLY - S05 Ledger (spoilers).md` - the GM's private ledger. Lee: attach it, but don't read it.
6. `2026-10-01 GM ONLY - Cast Card (spoilers).md` - NPC looks, manners, and who knows what. GM only.
7. `2026-10-01 SESSION - S05 Summary - Tears Are Water.html` (and earlier summaries, if wanted).

## For the GM (Lilita), first thing in the new chat
- Read the cast card, the end of the ledger, and the sheet BEFORE narrating. Re-read the cast card after any compaction.
- Recreate the roller as `game/roll.sh`:
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
  Run as `./roll.sh EL 0 "label" 2>>stderr.log`. NEVER `2>/dev/null`.
- The rules are in the SilentBardGames repo: /L1/*.md only, indexed by /L1/toc.md. Read the rule before claiming it's missing.

## Table conventions
- Sandbox, short beats, about one screen per turn. No branching menus at the end of a turn. No popup questions.
- Show the raw dice. Never fudge. Offer "if it stands / if Tokened" outcomes. Oracle: bare 2d (2 yes, 1 sign, 0 no).
- `<...>` is OOC. Unmarked speech is in character. Hyphens with spaces, not em-dashes.
- Write every NPC's dialogue from what that NPC actually knows. Flag stumbles on either side for retcon.
- Ask Lee before improvising a rule that ought to exist. Log it in the gap log with tags: @@ MISSING / @@ UNCOMMITTED / @@ UNCLEAR / @@ OPEN / OK. Anything the GM invents is @@*.
- End of each session: an HTML summary, the sheet, the gap log, the GM ledger, and the Karma tally and spend.

## Where we are
- S06 opens at Mira Thousand-Voices' cottage west of Saltwind, nearly noon, as the bell tolls for the burial of Brother Aubric. Caria has agreed to speak.
- Caria: Level 4. Tokens 4/4. Karma 0 (+1 earmarked to Conjuror). No Harm, but short on sleep.
- Rulings in force: the two-step for improvised Traits; Hook alterations free; unbound ranks count everywhere in their Role; Trick See the Root; spell endings revert form, not place.
