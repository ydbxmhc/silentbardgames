# HANDOFF - Level One solo playtest, Caria Greenhaven - START S08 HERE

Spoiler-free. Lee may read this. It replaces "S06 Resume Here." Saved 2026-10-07. The S06 Part 2 / S07 chat ("Cari 2," about 640 turns, one compaction) is closed.

## Where the files live
- **The project (Averond)** holds this handoff, the GM ONLY S08 brief, the Saltwind Gazetteer, the Rikitak Tenets, the GM Operating Guide, and the setting docs. A fresh chat attached to the project can read all of them.
- **Lee's PC**, in the folder `Lili's Bottle\Averond\Caria Playtest`, holds everything else. A chat linked to that computer can reach it there. Otherwise Lee attaches what is listed below.

## Attach or read, in this order
1. This file.
2. `GM ONLY - S08 Resume Brief (spoilers)` (project, and the playtest folder). Lee: attach it, don't read it.
3. `2026-10-07 CHARACTER - Caria Greenhaven (master file, through S07).md` - the sheet, every advancement, and the S07 END state.
4. `2026-10-07 PLAYTEST - S07 Gap Log - Caria (cumulative S1-S7).md` - the real deliverable.
5. `2026-10-07 CAST - Voices of Saltwind and the Road North (through S07).md` - how each NPC talks, carries themselves and what they want. In the project too.
6. `2026-10-07 SETTING - Saltwind Gazetteer - People, Places, Map (through S07).md` - who lives where, and the map. It's in the project too.
7. `2026-10-01 GM ONLY - Cast Card (S06 save, spoilers).md` - NPC looks and manners. GM only. For anyone met in S06 Part 2 and S07, the gazetteer and the brief supersede it.

**If the GM needs more:** `2026-10-07 GM ONLY - S07 Ledger (spoilers, cumulative S1-S7).md`. It's about 360 KB, so search it, don't load it. The S07 section is at the end.

**Not attachable:** the S1-S6 transcripts (far too big; search them in the folder). There is no verbatim transcript of S06 Part 2 or S07. The ledger holds every roll, oracle, invention, correction and ruling from those sessions.

## For the GM (Lilita), first thing
- Read the brief, then the sheet's S07 END section, then the gazetteer. **After any compaction, re-read the ledger before narrating anything already established. Never fill a memory gap with invention.** (S07 lesson: the GM made Hesta Rook the cook of Garth's pot.)
- Recreate `game/roll.sh` from the S06 handoff (the L1 Simple Pool roller). Run it as `./roll.sh EL 0 "label" 2>>stderr.log`. NEVER `2>/dev/null`. Never pipe `2>&1` into anything but `tee`.
- Keep appending to the ledger and the gap log every beat. Playtest files are ASCII-only (`--`, `->`). Ask Lee whether he's out of a file before editing it.
- Rules live in the SilentBardGames repo (public: github.com/ydbxmhc/silentbardgames), /L1/*.md only, indexed by /L1/toc.md. **Read the rule (and the spell) before ruling or recording it.** Spells are in /L1/magick/spells.md; casting is in spellcraft.md.

## Table conventions (unchanged)
- Sandbox. Short beats, about one screen per turn. No branching menus. No popup questions; ask in prose.
- Show the raw dice; never fudge. On rolls that matter, offer "if it stands / if Tokened." Use the bare oracle (2d: 2 yes, 1 a sign, 0 no) often. See the Bare Oracle design note.
- `<...>` is OOC; unmarked speech is in character.
- Lee invites invention: "I like when you invent, so don't be shy; we can true up the lore when it goes off-script." Mark every invention @@*.
- Words are representational. Borrowed terms (chapel, sexton, Cari's Latin) are fine; the point is the feeling. Avoid real-world religious idiom in NPC speech ("like a Christian").

## Rulings added in S06 Part 2 and S07 (details in the gap log)
- **Use it to grow it** (playtest advancement rule): each session, one optional NEW purchase (a new Role, a Maneuver that doesn't qualify, or Level; Level always takes this slot). Any number of paid improvements to Roles and Maneuvers USED that session. A new Maneuver counts as used if it would have applied to a roll she made (bare Role or unarguable Synergy). "Used" means a roll that mattered.
- **Medicine:** diagnosis feeds treatment as a Boost. Treatment and medicine can be Gear. A batch is a pool of Boost, given out in doses (cap a dose at the administering rank). Privation works like fatigue and blocks recovery; greens or a tonic unlock the recovery roll. Apothecary isn't Alchemy.
- **Persistent Wager:** the effect becomes a standing Boost "until the GM says so." Chained Boosts are intentional, and NPCs can build them too.
- **Known spells from other Roles:** a Maneuver can be a known spell (Cari: Loremaster 1, Scry). It's cast with Spellweaving and is bindable. The knowing Role's rank never adds to casting. The spell's Maneuver rank adds only when countering THAT spell.
- **Binding math (spellcraft.md):** recast EL = Level + UNBOUND Spellweaver ranks + ranks bound in that spell + that spell's Maneuvers.
- A Hook can never exceed Level. Attendance Karma is credited at session start (at a mid-story break, at the break).
- Nothing to See, Sister has two modes, FAST and SHAPED.

## Where we are: S08 opens
- **Time and place:** the night of Saltwind Day 2, then dawn of Day 3. Cari is at the wagon camp by the brook. The eleven wagons roll north at first light. She rides in wagon one (Korrin's terms: "light at night, eyes on the dark").
- **Riding north with her:** Dasha Korrin, carrying Harl's ambergris to Ganth. Jem, provisionally Cari's apprentice in "the light." Brother Kade and Hollis. Clerk Fennick. Tam on wagon two, and the drovers.
- **First, at the camp before sleep (Lee's plan):** half an hour of "meditating loudly," performing binding rituals for **Stone Shape** and **Fume** (Poison Cloud; brimstone from Garrow at Crossroads). These get rolled at S08's opening. **@@ Lee still has to confirm** that he means binding all four (Fax, Veil, Stone Shape, Fume), which gives Fax 6, Veil 5, Stone Shape 5, Fume 5, rituals 4, counter 4. The first ritual rolls at EL6, the second at EL5. Each keeps 1 point.
- **Still to tell Kade:** the ring-stone in the dead tower was lifted in recent weeks. Mira already knows.
- **Left in Saltwind:** Cobb's skeps (blessing and guardian, not done); proper goodbyes to Mirna, Jory and Karinna (the Hook took them). The grain comes back by a returning wagon. Tonight Min and Jory are on the north rocks for laver.
- **Caria:** Level 4. Tokens 4/4. Karma 1 carried. Hook A Hint of Brimstone 4. No Harm; nothing running. New after S07: Loremaster 1 (Scry), Conjuror 3 (Asher 3, Asher Level 3), Healer 3 (Apothecary 3).

## Paperwork still owed (not blocking play)
- S06 Part 2 and S07 summary pages (HTML, as before).
- A Cast Card refresh (the gazetteer covers Saltwind folk for now).
- README index update.
- The Truths and Tolls of the Order (Tenets companion pieces).
- Open rules questions: whether an item opposes at its rank or its points; Korrin's Level (played as 3); "Everything rolls" as a book line; oracle weighting; whether Karma flows "too well" (Lee: not urgent).
