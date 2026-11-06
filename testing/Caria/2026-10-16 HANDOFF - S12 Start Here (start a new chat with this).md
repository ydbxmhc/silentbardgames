# HANDOFF - Level One solo playtest, Caria Greenhaven - START S12 HERE

Spoiler-free; Lee may read this. It replaces "S11 Start Here." Saved 2026-10-16. The S11 chat (played 2026-10-13 to 2026-10-16, with two compactions and one overnight device drop) is closed. Everything in the S09-S11 handoffs about file locations, roll.sh, ASCII, logging, table conventions and rulings still applies. This file only adds what changed.

## Attach or read, in this order
1. This file.
2. `GM ONLY - S12 Resume Brief (spoilers)` -- a DELTA brief with the S11 Who Knows What changes. Lee: attach, don't read.
3. The S09 Resume Brief (still the main GM brief), then the S10 and S11 briefs (deltas). Lee: attach, don't read.
4. `GM ONLY - S09 Who Knows What (spoilers)`, plus the WKW sections of the S11 and S12 briefs.
5. `CHARACTER - Caria Playtest - Caria Greenhaven - Current Sheet (basics).md` -- updated to S11 END and the S11 save.
6. `PLAYTEST - Caria - S11 Gap Log (S11 entries)` -- read with the earlier logs. It holds this session's many rulings.
7. `GM ONLY - S11 Ledger (spoilers)` -- about 1,300 lines. Read the last 150 first; search the rest.
8. The L1 repo (public): read the rule before ruling. S11 proved it again and again.

## Method (proven in S11)
- Ledger first, every beat, by heredoc to the device. It survived two context compactions and an overnight drop of the computer link with nothing lost. If the device drops mid-roll, hold the beat in a scratch note and fold it in when the link returns.
- Roll everything on the device: `bash ./roll.sh EL XE "label" 2>>"$HOME/stderr.log"`. Opposition is a separate call. Never discard stderr.

## Rulings added in S11 (details in the gap log)
- Tokens: one per SCENE (cap = Level). A scene is one camera shot. Anyone may spend a Token on ANY roll. Tokens can exceed the cap from Extremes and GM kudos. NPC Extremes pay the GM a Token, not Karma.
- Dice committed to an action are gone for defense: an all-in character gets NO defense roll.
- Everything rolls: Difficulty is dice, never a fixed target.
- Intimidation and illusions deal Complications. Harm stays undifferentiated until the recovery roll.
- Required spell Traits count toward Difficulty (Scry is DL4; Guidable +1). Improvisation hold: the spell rolls its DL; Spell Improvisation counts.
- Dismissing an effect is not Releasing a spell. Release means unbinding.
- Free-action pre-existing Boosts add their value to EL as dice. An Extreme's side effect scales with the roll.
- Maneuver limit: the COUNT of Maneuvers is capped by the Role's rank. A new Maneuver at rank 1 costs 1K.
- Chronic illness is a permanent Hindrance; a won dawn heals up to 1 Injury a day.

## Where we are: S12 opens
- **Day 8, late morning, the Monastery of Rikitak.** Cari stands in the infirmary beside Merrit, who is asleep, stitched and recovering. The hearing in the chapter house broke off before any verdict on her.
- **What she did (S11):** found Wenna Tarro in the west wing and got her out of the gate in disguise with the Prior's written release. Saw the undercroft table with the Prior at dawn. Scried Ivro's mother's grave and had Asher clear the ivy off it. Ivro is in remission. At the hearing she stopped the Prior breaking Calder's sealed packet. She broke Tobin (who had beaten Merrit and hidden him), exposed Brask with her own lifted glamour, and drove a confession out of him. She burned the man behind it all, Brother Sever, off the wall of the chapter house. She put the steward down without killing him, broke Calder's ward, and made the Hierarch yield. She has not killed anyone.
- **Caria:** Level 4. Tokens 3/4 (S12 adds 1 per scene). Karma 0 spendable, with 1 pinned toward Level 5. **New:** Healer 4 with Trauma Care 1 (Healer EL8, Apothecary 11, Trauma Care 9; care cap 4). Spell Improvisation 3 (improvising: Fax 11, Veil 9, Stone Shape 9). No Harm. Her leather girdle is lost; her left bracer is gouged.
- **Asher** keeps watch over Calder from the Fax light in Calder's hearth.

## Paperwork still owed (not blocking play)
- Summary pages (HTML) for S06 Part 2 through S11.
- Master character file through S11.
- CAST and Gazetteer additions from S11: Prior A. Feyne, Odo, Ruddock, Holm (Sacrist), the Cellarer, Lanfric (lector), Benet (barber), Teague, Wystan, Sever, Sabeth, Nell, Fulke, the steward.
- Open questions are in the S11 gap log: splitting Harm at recovery, excess effect through a broken barrier, and Tokens against an Extreme.
