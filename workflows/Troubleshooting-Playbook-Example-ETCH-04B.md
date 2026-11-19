# Worked Example: ETCH-04 B through the 8D loop

SYNTHETIC TRAINING DATA. Made up for the AI for Troubleshooting course. Not from any real tool, vendor, lot, product or person.

Use this with Troubleshooting Playbook v0.6, in Gemini Enterprise. Two things in this example are mocked: the **inputs** (the case files in the kit, and your answers when the AI interviews you) and the **technicians' findings**. Everything else is whatever your AI tool actually produces when you run the playbook: the 8D record, the hypotheses, the check plans, the reviews, the D7 actions and the lesson. Nothing below is a model output.

You play the engineer who picked up the problem at 7:00 a.m. on Monday, Nov 9: you've read the case brief and the shift notes, and nothing else yet.

- The AI's questions won't come in the same order or words every time. Match each one to the topic, not to the exact question.
- If it asks something no response covers, answer "D: I don't know." That's realistic, and it should become an OPEN item.
- Some responses deliberately include background details and a guess. Part of the exercise is to see whether the AI sorts every specific correctly.
- Each stage ends with **what a good output contains**: a checklist to judge your own run against, not an answer to copy.
- **Restart points.** Each stage also names a restart point: a real output saved from the instructor's own run of the playbook, so a trainee whose run went sideways can paste it and keep up. These are TO BE CAPTURED FROM A REAL RUN; until then the slots are empty.

| Stage | 8D | Playbook prompt | Mocked input you paste | Restart point (real run) |
|:---|:---|:---|:---|:---|
| 1. Frame | D0 to D3 | Frame the Event | Interview responses | Record v1.0 |
| 2. Update with data and documents | D4 | Hypothesis Update | Kit case files | Record after the first update |
| 3. Cycle 1 | D4 | Check Plan, Technician Results, Hypothesis Update | Engineer's selections; findings bank, before the fix | Cycle 1 plan; record after cycle 1 |
| 4. Cycle 2 | D4 to D6 | Same | Engineer's selections; findings bank | Cycle 2 plan; record after cycle 2 |
| 5. Prevent recurrence | D7 | Prevent Recurrence, D7 Review | None | D7_Actions.md |
| 6. Close and lesson | D8 | Close and Lesson, Lesson Review | None | Lesson_Learned.md |

---

## Stage 1. Frame the Event (D0 to D3)

Paste the Frame the Event prompt in a new chat. Then paste this as your first message:

```text
ETCH-04 chamber B keeps going down on "He backside flow high." It came back from a chuck PM Friday morning and it's been down four or five times since. Every reset gets it running for a few hours, then it trips again. Night shift is sure it's the new He MFC that went in at the PM. It ran P-110, P-220, P-330 and P-440 all weekend. Crew B did the PM. I just picked it up and my manager wants a problem statement, the likely cause backed by data before anyone orders parts, and containment.
```

**If it asks WHAT the symptom or alarm is:**
```text
Alarm is "He backside flow high." There was also one "ESC clamp fault, backside pressure not reached" on Sunday at 00:55. On Friday night the operator noted the He flow on the tool screen looked higher than the A side, but no alarm then.
```

**If it asks WHERE (which chambers have it and which don't):**
```text
Only ETCH-04 B. ETCH-04 A was fine all weekend. ETCH-05 A got the same new-rev He MFC on Thursday and the notes say no issues. I don't know about ETCH-05 B.
```

**If it asks WHEN (first occurrence and pattern):**
```text
04B came back from the chuck PM Friday Nov 6 at 07:10. Downs: Sat 02:10, Sat 14:20, Sun 00:55 (the clamp fault), Sun 09:00 (held for engineering until Mon 00:40), Mon 05:30. I don't know whether 04B ever had this alarm before the PM.
```

**If it asks WHAT CHANGED:**
```text
Chuck PM on 04B from Thu Nov 5 20:00 to Fri Nov 6 07:10: the chuck was lifted, the chuck seal O-ring replaced, and the He MFC swapped to the new rev while it was open. A software patch was loaded on ETCH-04 during the same window (04A was paused about 50 minutes for it). Facilities reported a He header pressure dip Sat 22:35 to 23:20, and every chamber got a supply warning.
```

**If it asks HOW MUCH (frequency, size, downtime):**
```text
Four He backside flow alarms plus one clamp fault since the PM, so five downs. Roughly 22 hours of downtime by Monday 7 a.m. Each reset gives a few hours. I don't know the actual flow values yet.
```

**If it asks about CONTAINMENT (the tool, and product run since the change):**
```text
04B has been down since Mon 05:30 and I've told the shift no more resets without me. The lots that ran on 04B since the PM haven't been looked at. Hold them until we've checked their etch results; that's my call for now.
```

**If it asks about the TEAM or CONSTRAINTS (who, safety, access, parts):**
```text
I'm the engineer on it during the day. Day-shift and night-shift techs are available and do the hands-on work. Nights and weekends go to the on-call engineer. Chuck work needs the site lockout procedure. I don't know what spare parts are on hand.
```

**If it asks what EVIDENCE or data is available:**
```text
I have the shift notes, alarm history, maintenance log, FDC summary and limits, change log, the chuck chapter of the manual and past lessons learned. The PM sign-off says He leak 0.41 sccm at 22 C, PASS. Sunday's tech did an MFC zero check: 0.02 sccm at zero, OK. Nobody has done a leak check since the PM.
```

**If it asks you to confirm the MFC is a guess:**
```text
Yes, that's the night shift's guess. Nobody has tested it. Record it as a guess to check.
```

**If it asks about the recipes, the crew, or anything you only mentioned in passing:**
```text
That's background. I mentioned it, but I have nothing that ties it to the problem.
```

**When it shows the draft record:** read it before you reply. If the D2 problem statement names the MFC, the seal, a leak, or any cause, reply with that item's ID and "this is a cause, take it out." Otherwise reply `Confirmed`.

Then run the Record Review in a new chat with the Review Gate, the record and your pasted responses only (leave out the AI's turns).

**What a good record v1.0 contains:**
- A D2 problem statement in observable terms only: five stops (four He backside flow high, one clamp fault), Sat Nov 7 02:10 to Mon Nov 9 05:30, about 22 hours, since the chuck PM; ETCH-04 A not affected. No cause in it.
- D1 roles: the engineer, the day and night technicians, the on-call engineer.
- D3: the chamber held with no resets without the engineer; the lots run on 04B since the PM held until their etch results are checked.
- Hypotheses wide enough to cover every physical path for "He flow high": something like seal leak, wafer or chuck surface leak, flow measurement, supply pressure, pressure control, and the alarm limit. All Open.
- The night shift's MFC idea recorded as a guess against a flow-measurement hypothesis, not as evidence.
- Recipes and Crew B kept out as background; "it alarmed before the PM" not stated as fact.

**Restart point:** record v1.0 from a real run. TO BE CAPTURED.

---

## Stage 2. Hypothesis Update with data and documents (D4)

New chat. Paste the Hypothesis Update prompt with your record v1.0, and attach `alarm_history.csv`, `fdc_summary.csv`, `fdc_limits.csv`, `maintenance_log.csv`, `change_log.csv`, `manual_excerpt.txt` and `past_lessons.txt`. Gemini writes and runs the code the counts need.

**What a good update contains:**
- The supply-pressure hypothesis ruled out: the Saturday dip warned all four chambers, but only 04B alarms, before and after it.
- The alarm-limit hypothesis ruled out as the cause: the interlock is 4.0 on every chamber. The missing 2.0 warning on the B chambers recorded as an open item, not dropped.
- The MFC hypothesis weakened but still Open: ETCH-05 A has the same new-rev MFC and runs clean (0 alarms in 49 runs), and 04B shows a climb, not a step.
- The seal hypothesis raised, citing the run-by-run climb, the reset pattern, the cold sign-off check (0.41 sccm at 22 C, WO-58470), manual 7.6 NOTE and 7.9, and Lesson 2024-031. Raised, not Confirmed.
- Two one-off He alarms on 04B before the PM (Oct 20, a chipped wafer; Nov 1, a particle), each a single wafer that did not repeat: not the same pattern.
- Counts with code behind them. A common miss is 41 alarms where the file holds 46; an unverified count must read COUNT NOT VERIFIED and change nothing.

**Restart point:** record after the first update. TO BE CAPTURED.

---

## Stage 3. Cycle 1: checks that don't open the chamber (D4)

### The engineer's selections (mocked input)

New chat. Paste Check Plan Prompt A with your latest record. The AI shows a decision menu and stops. Read it first: an option that swaps a part or opens the chamber before anything is Confirmed should not be there. Then paste these selections. They name hypotheses by mechanism, not by ID, because your AI numbers them its own way:

```text
This cycle, split the seal, wafer or chuck surface, flow measurement and pressure control hypotheses using only checks that don't open the chamber. Downtime: start now on day shift. Parts: none this cycle. Escalation: stop and call me when the checks are done, or sooner on any reading the plan doesn't cover.
```

Then paste Prompt B in the same chat and attach `manual_excerpt.txt`. If it asks:
- **Reference standard:** "We have a reference flow standard the techs use for MFC flow verifies."
- **Test wafer:** "Use a known-good test wafer from the tool's test-wafer slot."
- **Who the technician calls:** "Me on day shift, the on-call engineer otherwise."

**What a good cycle 1 plan contains:** a hot leak check per manual 7.6 (60 C, 30-minute soak, test wafer, flow recorded at 5 minutes) with backside pressure recorded against setpoint; a flow verify against the reference; a branch rule and a stop-and-report point for every step; nothing that lifts the chuck or swaps a part. **What a good review catches:** a leak check with no temperature, or "verify leak OK" with nothing to record (the exact escape in this case); a part swap before a check (I = 5); a costlier step chosen over a cheaper one that splits the same hypotheses.

Then build the technician's notes from the **findings bank** below, using the "before the fix" column, and run Technician Results and the Hypothesis Update.

**What a good cycle 1 update contains:** flow measurement ruled out by the flow verify; pressure control ruled out because pressure held setpoint; the wafer ruled out but the chuck surface still Open; the seal still Open and ranked first, **not Confirmed**. A high hot leak is what a bad seal would show, but a damaged chuck surface would show the same number. This is the teaching moment of cycle 1: the AI often wants to call the seal confirmed here.

**Restart points:** cycle 1 plan, and record after cycle 1. TO BE CAPTURED.

---

## Stage 4. Cycle 2: inspect, fix, qual (D4, D5, D6)

### The engineer's selections (mocked input)

```text
Lift the chuck and inspect the seal and the chuck surface. Photograph the seal as found before touching it. Reinstall with a new seal O-ring per manual 7.4c and 7.4d, then the hot leak check and the qual. Parts: one chuck seal O-ring kit. Escalation: stop and call if the seal and surface both look fine, if anything is damaged besides the O-ring, or if the hot leak is above 1.0 after reinstall.
```

If it asks:
- **Parts:** "Chuck seal O-ring kits are in stores."
- **Safety or lockout:** "Chuck removal needs the site lockout procedure, and the chuck must be below 30 C (manual 7.4a). Use only the safety steps in the manual sections attached."
- **The qual:** "After chuck work the qual is: hot He leak check per manual 7.6 at 1.0 sccm or less at 60 C, then a 25-wafer season, then monitor wafers in spec. The tool returns to production only on a passed qual."

Why the new O-ring is allowed before the seal is Confirmed: manual 7.4c requires one at every chuck removal, so it is part of the procedure, not a repair chosen on a guess. A good plan cites 7.4c; a good review flags it if not.

Build the notes from the findings bank: inspection and reinstall entries, then the "after the fix" column for the hot leak check and the qual.

**What a good cycle 2 update contains:** the seal Confirmed, citing both the rolled seal and the leak falling from about 1.5 to about 0.4 sccm once it was seated (a result that would differ if the seal were not the cause); the surface ruled out; the root cause and an escape point with two parts (a cold sign-off leak check, and no warning limit on the B chambers); D5 and D6 filled; the held lots still open for the engineer to decide.

**Restart points:** cycle 2 plan, and record after cycle 2. TO BE CAPTURED.

---

## Findings bank: what the technicians found (mocked)

The AI writes a different plan every run, so the findings are keyed to the **kind of check**, not to step numbers. To build the technician's notes for a cycle, go down the released plan step by step, find the matching check below, and copy its note in the plan's order. Stop where the plan says stop and report. Paste the notes as they are: they are meant to be loose, so the Technician Results prompt has real work to do.

The state of the tool matters. Use the "before the fix" note until a new seal has been seated, and the "after the fix" note from then on.

| Kind of check | Before the fix | After the fix |
|:---|:---|:---|
| Hot leak check at process temperature (60 C, soak, test wafer) | "soaked 30 min at 60, test wafer from slot 25. backside held 10 torr fine the whole time. flow at 5 min was 1.48. thats way over." | "hot leak at 60 after 30 min soak 0.36." |
| Read the as-found state from the tool screen (no reset) | "04B still stopped, no wafer on the chuck, chuck at 24 C, no new alarms since 05:30." | "chuck at 24 C, no alarms." |
| Repeat the hot reading after unclamp and reclamp cycles | "unclamped and reclamped 3 times, 5 min each. 1.52, 1.57, 1.61. still going up." | "3 reclamps, 0.36, 0.37, 0.36." |
| Leak check at room temperature | "leak check cold, 23 C, 0.43. passes." (This is the trap: a cold check passes on a bad seal.) | "cold check 0.31." |
| Leak check with no temperature stated | "did a leak check, read 0.45, chuck was still cooling down, didnt look at the temp." (Untraceable on purpose: a good results review flags it.) | Same note, reading 0.33 |
| MFC flow verify against the reference | "flow verify on the He MFC with the ref standard, within 1%. MFC looks fine to me." | Same |
| MFC zero check | "MFC zero 0.02 sccm at zero flow. ok." | Same |
| He supply pressure | "He supply at the tool 29.8 psi, steady, no dips while i watched." | Same |
| Backside pressure control (sealed test wafer, hold setpoint) | "set 10 torr with the test wafer, held 10.0, valve not hunting." | Same |
| Alarm limit check | "interlock is 4.0 on 04B, same as 04A. 04B has no 2.0 warning set, 04A does." | Same |
| Inspect the wafer | "wafer from the last down looks fine, no chips, no particles on the back that i can see." | Same |
| Lift the chuck, inspect the seal and surface | "locked out, cooled to 28, lifted the chuck. seal was rolled out of the groove at about 4 o'clock for maybe 3 cm, took photos. chuck surface looks clean, no scratches." | Not applicable |
| Fit a new O-ring and reinstall per 7.4c to 7.4e | Not applicable | "new oring in, ran a finger all the way round, lowered straight, torqued 2 passes star pattern." |
| Swap the MFC (if the engineer approved it) | "swapped to the old rev MFC. hot leak at 60 still 1.47. alarmed again after 9 runs." (A wasted swap: the frivolous-plan lesson.) | Not needed |
| Qual: 25-wafer season, then monitor wafers | "season started, He leak alarm on run 9, stopped." | "ran the 25 wafer season, no alarms. monitor wafers in spec per the qual sheet. qual passed, called the engineer to release it." |
| Anything not listed here | "didnt do that one, not sure what the step wanted. stopped and called." | Same |

Two rules keep this honest whatever plan the AI writes:
- **A step that isn't in the bank was not performed.** The note says so, and the next update has to work with the gap instead of guessing.
- **A step the engineer shouldn't have released still gets a realistic result.** A cold leak check passes; an MFC swap fixes nothing. The class sees what a weak plan costs.

---

## Stage 5. Prevent recurrence (D7)

New chat. Paste the Prevent Recurrence prompt with your record after cycle 2.

**What a good D7_Actions.md contains:**
- An action for each half of the escape point: a hot leak check at temperature as a sign-off item in the chuck PM procedure, and a He leak warning limit on the B chambers.
- The finding that Lesson 2024-031 already listed both actions, with no known status. A good D7 says so plainly and asks for an owner, so this time the action closes.
- A way to verify each action (for example, the next chuck PM sign-off shows a reading at 60 C).
- Where else, all TO CHECK: ETCH-05 B; other chambers whose chuck was lifted at a PM; ETCH-02 A from the 2024 lesson.

**What a good D7 Review catches:** an action that answers neither the root cause nor the escape point (for example, "go back to the old-rev MFCs"); an action with no way to verify it; sister chambers missing from Where Else.

**Restart point:** D7_Actions.md. TO BE CAPTURED.

---

## Stage 6. Close and lesson (D8)

New chat. Paste the Close and Lesson prompt with the record including D7.

**What a good Lesson_Learned.md contains:**
- A title in the words someone would search for: the alarm text, "after chuck PM", and the tool type.
- The signature: one chamber only; leak above 1.0 sccm from the first run after chuck work; climbs run by run; each reset drops it and it climbs faster.
- The earliest sign: 1.14 sccm on the first run after the PM, already above the 1.0 acceptance.
- Every statement traced to a record section in the self-check table.

**What a good Lesson Review catches:** a title without the alarm text or the tool type; a signature that would also fit a ruled-out hypothesis, such as the MFC; any statement the closed record doesn't support.

A good closure summary also credits the night-shift operator who noticed on Friday that the flow looked higher than the A side: the earliest human catch.

**Restart point:** Lesson_Learned.md. TO BE CAPTURED.

---

## Notes for the instructor

- **Capture the restart points.** Run the whole playbook once in the tool the class will use, with these inputs and the findings bank, and save each output named in the stage table. Those become the restart points. Only a real run can supply them.
- **Mocked values to sanity-check before the course:** every reading in the findings bank, the seal finding (rolled at 4 o'clock for about 3 cm), the qual definition, parts in stores, the on-call rule, and the lot hold.
- **Running a cycle in class:** the instructor can call out the findings as the "technician", or trainees build the notes from the bank themselves. The second is slower but shows the matching of findings to the plan.
