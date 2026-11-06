# HANDOFF - Level One solo playtest, Caria Greenhaven - START S09 HERE

Spoiler-free; Lee may read this. It replaces "S08 Start Here." Saved 2026-10-09; updated 2026-10-11 (gap log addendum, README). The S08 chat (played 2026-10-07 to 10-09, one compaction) is closed.

## Where the files live
- **The project (Averond) holds everything a fresh chat needs to play,** no PC link required:
  - this handoff and the GM ONLY S09 brief
  - Cari's master sheet (through S08)
  - the S1-S8 gap log
  - the S08 ledger
  - the Saltwind Gazetteer and the CAST - Voices card (both through S08)
  - the Bare Oracle note, the Tenets, the GM Operating Guide and the setting docs
- **Lee's PC** (`Lili's Bottle\Averond\Caria Playtest`) holds all of the above plus:
  - the cumulative S1-S7 ledger (about 360 KB)
  - the S1-S6 transcripts
  - the older per-session snapshots and summaries
  - `roll.sh`

  Reach them through the desktop link if a detail from S1-S7 matters; otherwise ask Lee.
- **The ledgers are split.** The S08 ledger covers S08 only; it is NOT joined to the S1-S7 ledger. For older history, search the S07 cumulative ledger.
- **Write-back:** at session end, put the updated sheet, gap log and ledger in Lee's folder (through the link), or hand them to Lee to save. Refresh the project copies too.

## Attach or read, in this order
1. This file.
2. `GM ONLY - S09 Resume Brief (spoilers)`. Lee: attach it, don't read it.
3. `CHARACTER - Caria Greenhaven - Current Sheet (basics).md` - the ONE living sheet: current numbers only, updated in place (Asher already on the 2026-10-11 points model). (Project name: `CHARACTER - Caria Playtest - Caria Greenhaven - Current Sheet (basics).md`.)
4. `2026-10-09 PLAYTEST - S08 Gap Log - Caria (cumulative S1-S8).md` - the real deliverable.
5. `2026-10-11 PLAYTEST - Gap Log Addendum - Caria - Crafting, Downtime, Wands (pre-S09).md` - design talk between S08 and S09: crafting on fiction time, spells in items (wands), downtime, and the NEW GM habits for NPC knowledge (Present lines in the ledger, a who-knows-what table in the brief). Read it before voicing anyone. Fold it into the S09 gap log. (Project name: `PLAYTEST - Caria - Gap Log Addendum ...`.)
6. `2026-10-09 CAST - Voices of Saltwind and the Road North (through S08).md` - how each NPC talks, moves and what they want.
7. `2026-10-09 SETTING - Saltwind Gazetteer - People, Places, Map (through S08).md` - Saltwind, plus the road north (Tanner's Fords, the Court woods camp).
8. `2026-10-09 PREP - S09 Crossroads Return (continuity and likely encounters).md` - who and what Cari left in Crossroads in S2, the threads that come home there, eight encounter seeds, and Lee's open questions. Lee may read it. (Project name: `PREP - Caria Playtest - S09 Crossroads Return ...`.)

**GM ONLY, read before voicing NPCs:** `2026-10-11 GM ONLY - NPC Frames (spoilers).md` - simple stat frames for Kade, Hollis, Korrin and Jem, and the policy for adding more. (Project name: `GM ONLY - Caria Playtest - NPC Frames ...`.)

**If the GM needs more:** `2026-10-09 CHARACTER - Caria Greenhaven (master file, through S08).md` (every advancement and the Accords ledger; Asher there is pre-ruling Level 3). `2026-10-09 GM ONLY - S08 Ledger (spoilers).md` (about 125 KB; search it rather than loading it whole). For S1-S7: `2026-10-07 GM ONLY - S07 Ledger (spoilers, cumulative S1-S7).md` (PC only; about 360 KB).

## For the GM (Lilita), first thing
- **Read in this order:** the brief, the sheet's S08 END section, then the gazetteer's road section.
- **After any compaction:** re-read the ledger before narrating anything already established. Invent only into true blanks, and mark it @@*.
- **Before voicing anyone:** build the who-knows-what table into the S09 brief (see the addendum), then check it and the CAST card.
- **Check the CAST card before voicing anyone.** S08 slips: Korrin's pronoun (she), a Scots burr given to Kade (he has no dialect), oxen narrated as mules.
- **Rules:** they live in the SilentBardGames repo (public: github.com/ydbxmhc/silentbardgames). Read /L1/*.md only, indexed by /L1/toc.md. **Read the rule, the spell and the Role page before ruling or recording it.** S08 slips: a Summoning run before reading conjuror.md, and a "gap" logged that luck.md already covered.
- **Logging:** keep appending to a NEW S09 ledger and the gap log every beat. Ledger first, then gap log, in Lee's words.
- **Files:** playtest files are ASCII-only (`--`, `->`). Ask Lee whether he's out of a file before editing it.
- **Dice:** `roll.sh` is in Lee's folder. If there's no link, recreate it (below) and run it as `./roll.sh EL OPP "label" 2>>stderr.log`. NEVER `2>/dev/null`. Never pipe `2>&1` into anything but `tee`.

```bash
#!/usr/bin/env bash
set -u
el="${1:-}"; opp="${2:-0}"; label="${3:-}"
if ! [[ "$el" =~ ^[0-9]+$ && "$opp" =~ ^[0-9]+$ ]]; then
  echo "usage: ./roll.sh EL OPP \"label\"  (EL and OPP are whole numbers)" >&2; exit 1; fi
coin() { if [[ -n "${SRANDOM:-}" ]]; then echo $(( SRANDOM % 2 )); else echo $(( RANDOM % 2 )); fi; }
roll_pool() { local n="$1" faces="" sum=0 d i
  for (( i = 0; i < n; i++ )); do d=$(coin); faces+="$d "; sum=$(( sum + d )); done
  echo "${faces% }|$sum"; }
extreme_tag() { local n="$1" sum="$2"
  if (( n >= 3 )); then
    if (( sum == n )); then echo " (EXTREME SUCCESS)"; return; fi
    if (( sum == 0 )); then echo " (EXTREME FAILURE)"; return; fi; fi; echo ""; }
IFS='|' read -r afaces asum <<< "$(roll_pool "$el")"
echo "== ${label:-roll} =="
echo "EL $el -> ${afaces:-(no dice)} = $asum$(extreme_tag "$el" "$asum")"
if (( opp > 0 )); then IFS='|' read -r ofaces osum <<< "$(roll_pool "$opp")"
  echo "vs ${opp}d -> $ofaces = $osum$(extreme_tag "$opp" "$osum")"
else osum=0; echo "vs 0d (unopposed) = 0"; fi
echo "EFFECT $(( asum - osum ))   | if Tokened: $el - $osum = EFFECT $(( el - osum ))"
```

## Practical notes for the next Lilita (from S08, 2026-10-09)
- **The PC link.** When this chat is linked to Lee's computer, his playtest folder is `C:\Users\pavel\Lili's Bottle\Averond\Caria Playtest`. Ask once for access to `C:\Users\pavel\Lili's Bottle` if it isn't already granted.
  - To read a file: stage it (it lands under `/mnt/user-data/uploads/Lili's Bottle/...`, read-only; copy it before editing).
  - To write a file: copy it into `/mnt/user-data/outputs/`, then commit it to the PC path.
- **Saving to the project.** `project_write` with `local_path` only accepts files inside the working directory, so keep the working copies there (S08 used `game/out/`).
- **File names differ slightly.** PC names drop "Caria Playtest -" (e.g. `HANDOFF - S09 Start Here ...`); project names keep it. Same contents.
- **Start a NEW ledger for S09.** Append every beat. Check ASCII before saving: `LC_ALL=C grep -c -P '[^\x00-\x7F]' FILE` should print 0. That grep exits 1 on zero matches; that's fine. Never `2>/dev/null`.
- **Context weight.** S08 ran long enough to compact once and burden Lee's PC. Keep turns short. Read big files by grep or by section, not whole. At a natural break, offer to save and hand off rather than letting the thread bloat.
- **README.** The folder's `00 README - Caria Playtest Index.md` points at this handoff (updated 2026-10-11). Ask Lee whether he's out of it before updating it again.

## Table conventions
- Sandbox. Short beats, about one screen per turn. No branching menus. No popup questions; ask in prose, one at a time.
- Show the raw dice; never fudge. On rolls that matter, offer "if it stands / if Tokened."
- Use the bare oracle often (2d: 2 yes, 1 a sign, 0 no). See the Bare Oracle design note.
- `<...>` is OOC; unmarked speech is in character.
- Lee invites invention ("I like when you invent, so don't be shy"). Mark every invention @@*. When an invention collides with the record, an in-fiction retcon beats a table stop: the lame off-ox traded for mules at Saltwind is the model.
- Words are representational. Borrowed terms are fine; real-world religious idiom stays out of NPC mouths.
- **Standing kit** [Lee, S08]: a character keeps her signs of office and personal gear unless play separates her from them. Don't narrate her leaving things behind, and don't make her say "I grab my parazonium."
- **Materials:** very little steel in Averond. Default to bronze, brass and leather (Cari's parazonium is bronze; Korrin's lantern is brass).

## Rulings added in S08 (details in the gap log)
- **Spellcraft:**
  - Binding costs the rank everywhere in the Role, Artifice and counterspell included ("Everything costs").
  - On a recast, only a zero destabilizes.
  - Stone Shape: reshaped stone reverts when focus ends; moved stone stays.
  - Fatigue applies to the improvisation hold roll.
- **Engine:**
  - A Token sets any result up to the maximum (already in luck.md).
  - Boosts add dice, even after the fact.
  - Flat target numbers are an optional variant.
- **Sleep debt:** a standard recovery roll with situational modifiers. The Hindrance clause lets some of it linger in the narrative.
- **Spirits:**
  - Every spirit has Display and Manifestation built in at base Role rank; Possession needs the Maneuver.
  - Asher is essentially a Fire Adept.
  - A Conjuror may spend her Token on her spirit's roll.
  - The True Name double payout is "kind of intentional" (to be revisited against Beast Handler).
- **The Accords:**
  - Intention governs. A gift accepted implies a debt among those who know the Accords.
  - Trickery weakens a debt; fey inflate tiny ones.
  - "Met as paid" (two fingers on an open palm) zeroes a meeting.
- **Folk charms:** salt for the dead, silver for demons, iron for fey. A threshold works if you have the right and the belief. Vulnerability tracks how far a being leans into its nature.
- **Use it to grow it:** use in fiction only (no roll) defaults to the session's NEW purchase.
- **Apprentices:** an NPC apprentice is GM-owned by default. Beast Handler's Companion Training is the model to adapt. Still OPEN.

## Where we are: S09 opens
- **Time and place:** the night of Day 3 on the road north, going on dawn of Day 4.
  - Korrin's eleven wagons are camped in a ring at the near edge of the Court woods, past Tanner's Fords.
  - Cari is asleep by Kade's fire, under her orange Healer's robe and Kade's cloak, with Hollis along her back.
  - Jem is at Korrin's wagon.
- **Lights burning:** Korrin's brass lantern with the watch; Jem's tin lantern; the picket cairn on the east side (bright, with an ember-red core and a sulphur tang).
- **The road ahead:** the Court woods (the Weeping Court lies in them), the fork, then Crossroads, where Jem needs clothes and kit. Ganth is about three weeks from Saltwind.
- **Still to tell Kade:** the ring-stone in the dead tower at Saltwind was lifted in recent weeks.
- **Riding north:**
  - Dasha Korrin, who carries Harl's ambergris to Ganth and is Jem's self-appointed guardian.
  - Jem, Cari's apprentice: a spit-handshake "Deal," lessons on the wagon by Korrin's terms.
  - Brother Kade and Hollis.
  - Clerk Fennick.
  - Tam on wagon two, and the drovers.
- **Caria:**
  - Level 4. Tokens 4/4 at session start (luck.md). Karma 0 carried, +1 attendance at S09 start. Hook A Hint of Brimstone 4. No Harm.
  - New after S08: Loremaster 2 (+ Light, a spell she already knew), Fax Iacta 2, Spell Improvisation 2.
  - Bound: Fax Iacta, Phantasmal Veil, Stone Shape; 1 unbound rank; Fume left unbound by choice.
  - Carrying Mira's hag-stone.

## Paperwork still owed (not blocking play)
- Summary pages (HTML, as before) for S06 Part 2, S07 and S08.
- The Truths and Tolls of the Order (Tenets companion pieces).
- Open rules questions:
  - whether an item opposes at its rank or its points
  - Korrin's Level (played as 3)
  - "Everything rolls" as a book line
  - oracle weighting
  - Query the Candle: whose rating?
  - the apprentice model, and Asher's growth
