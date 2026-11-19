# Troubleshooting Playbook (v0.5): the 8D loop

Works a troubleshooting event through all eight 8D disciplines as a loop, with AI doing part of the work in every discipline. The worked case in the course is a tool down; the same prompts work for process troubleshooting (see the note below). One living artifact, `8D_Record.md`, holds the problem, the containment and the hypothesis register. Each cycle, the engineer sends the technicians a short check plan, and their findings come back into the same record to update the hypotheses. The loop repeats until the root cause is confirmed and the tool passes its qual. Every prompt meets the Prompt Evaluation Rubric v3.2 (ai-training/reference/Prompt-Evaluation-Rubric.md).

## The Loop

```text
Frame (D0 to D3, first hypotheses)
   -> Hypothesis Update with data and documents (D4)
   -> Check Plan, signed by the engineer (D4 checks; D5 fix once a cause is confirmed; D6 qual)
   -> Technician Results
   -> Hypothesis Update with the results (D4, D5, D6)
   -> next Check Plan ... until the qual passes
   -> Prevent Recurrence (D7)
   -> Close and Lesson (D8)
```

| 8D discipline | Where it lives in this playbook |
|:---|:---|
| D0 Prepare and respond | Frame: the event, the emergency action taken |
| D1 Team | Frame: roles (engineer, technicians, on-call) |
| D2 Problem description | Frame: problem statement, Is / Is Not, what changed |
| D3 Containment | Frame, updated every cycle: tool held, product run since the change dispositioned |
| D4 Root cause and escape point | Hypothesis Register, updated every cycle until one hypothesis is confirmed; escape point recorded when found |
| D5 Permanent corrective action | Check Plan, only after a hypothesis is confirmed and the engineer approves the fix |
| D6 Implement and verify | Check Plan: the qual. The event closes on a passed qual |
| D7 Prevent recurrence | Prevent Recurrence: actions that answer the root cause and the escape point, and where else the mechanism could occur |
| D8 Close and recognize | Close and Lesson: the closure summary, the team's contributions, and a lesson learned written so the next person searching for the symptom finds it |

The 8D record maps section for section onto the kit's 8D_template.docx. On a tool down, the tool returns to production at D6 (a passed qual); D7 and D8 finish the 8D afterwards.

## Using this for process troubleshooting

The loop and every prompt stay the same; the unit of evidence changes. Where a tool down counts alarms per chamber run, a process excursion counts affected lots, wafers or sites, and the Is / Is Not compares lots, tools, chambers and dates. Hypotheses come from the process and the tools that ran it, checks are often metrology or a split lot instead of a hardware inspection, D3 containment is a lot hold, and the qual becomes the release criteria for the process. Designing the experiment itself belongs to the Process Development playbooks.

## Why the loop needs a record

Gemini Enterprise and Copilot Chat remember nothing between chats, so the record is the memory. Each cycle starts a new chat with only two things pasted in: the latest `8D_Record.md` and the newest evidence (data, document sections, or a confirmed `Results_Report.md`). Nothing else from earlier chats goes in, so stray details from old conversations can't leak into the hypotheses.

---

## Thread Map

| Thread | Who | Prompt | Paste or attach |
|:---|:---|:---|:---|
| Frame (once) | Engineer or lead tech | Frame the Event | Nothing. Pass-downs and notes when the interview asks |
| Record review (after every Frame or Update) | Engineer | Record Review | Review Gate, the new `8D_Record.md`, the evidence or interview answers it came from, the previous record version if any |
| Update (every cycle) | Engineer | Hypothesis Update | Latest `8D_Record.md`; new evidence attached |
| Plan (every cycle) | Engineer | Check Plan: decision menu, then plan | Latest `8D_Record.md`; procedure sections for the likely steps |
| Plan review (every cycle) | Engineer | Mechanical Lint, then Check Plan Review | Review Gate, `Check_Plan.md`, `8D_Record.md`, the engineer's selections |
| Results (every cycle) | Technician | Technician Results | Released `Check_Plan.md`, then the technician's notes |
| Results review (every cycle) | Technician, then engineer | Mechanical Lint, then Results Review | Review Gate, `Results_Report.md`, `Check_Plan.md`, the technician's notes |
| Prevent (once, after the qual) | Engineer | Prevent Recurrence | `8D_Record.md` with the qual passed |
| Prevent review | Engineer | D7 Review | Review Gate, `D7_Actions.md`, `8D_Record.md` |
| Close (once) | Engineer | Close and Lesson | `8D_Record.md` with D7 filled |

After a review, paste its patch block into the chat that built the artifact, fix it there, and hand on only the fixed artifact.

---

## Artifact Standards

| Artifact | Standard | Checked by |
|:---|:---|:---|
| `8D_Record.md` | D0 to D3 complete and sourced; problem statement in observable terms only (Kepner-Tregoe Is / Is Not); every hypothesis is a physical mechanism with a status, evidence for and against, a source for each, and the next discriminating check; a hypothesis changes status only on cited evidence; a cycle log; versioned with a change-log line per update | Record Review |
| `Check_Plan.md` | Check Plan Standard: every step has action, reference, conditions, record with units, hypotheses it splits and a branch rule; every branch ends at a step, a stop-and-report point or the qual; a repair appears only for a confirmed hypothesis with engineer approval; every safety step cites its procedure | Mechanical Lint L1 to L8, Check Plan Review |
| `D7_Actions.md` | Every action traces to the root cause or the escape point; each names what changes, how its effect is verified, and an owner; every other place the mechanism could occur is listed as TO CHECK | D7 Review |
| `Lesson_Learned.md` | Symptom written in the words someone would search for; observable signature; confirmed cause and proof; the fix; the check that would have caught it sooner; nothing in it beyond what the closed record shows | Close and Lesson self-check, engineer sign-off |
| `Results_Report.md` | One result per step reached, tied by ID; readings with units and conditions; observation separate from interpretation; confirmed by the technician | Mechanical Lint L9 to L10, Results Review |

---

## Shared Blocks

### Review Gate (paste into every review thread)

```xml
<review_gate>
Rate every finding on two anchored scales, matching each finding to the anchor text.

Impact (I):
- 1 Cosmetic: wording or formatting only; meaning is unchanged.
- 2 Local: one item is weaker than it should be; nothing else depends on it.
- 3 Propagating: one item is wrong or unclear, and a hypothesis, step, branch or decision depends on it.
- 4 Structural: a hypothesis status, a branch, a stop point, or several steps are affected.
- 5 Unsafe or unfounded: a safety step, lockout, interlock or spec limit is missing or contradicted; a repair comes before a confirmed hypothesis; a hypothesis changed status without cited evidence; or an item has no source.

Ambiguity (A):
- 0 Two technicians would do the same thing and record the same result.
- 1 Two technicians would do the same thing with small differences in setup.
- 2 Two technicians could do different things, record different results, or could not tell what to record.

Gate:
- Patch when I >= 4, any A.
- Patch when I = 3 and A = 2.
- Keep in every other case; record the finding in the scorecard only.

Always Keep: stylistic variation; wording that leaves what a technician does or records unchanged; limits written as "at or below" or "at or above".

Mechanical defects (table shape, placeholders, ID closure, branch closure, missing units) belong to the Mechanical Lint. Score only findings outside that list.
</review_gate>
```

### Hypothesis Ranking Scales

```text
Rank = E x C, each matched to its anchor.
E 1 Guess only. E 2 One document or one data pattern is consistent. E 3 The data pattern matches and a document describes this mechanism. E 4 As 3, and a past event or a technician result with the same signature supports it. E 5 As 4, and the evidence rules out every competing hypothesis.
C 1 Disassembly, parts, or more than 4 hours down. C 2 Disassembly under 4 hours, no parts. C 3 No disassembly; needs a test wafer, a procedure or a reference standard. C 4 Readable from the tool screen or a log with nothing stopped.
```

### Identifiers

| ID | Meaning |
|:---|:---|
| `HYP-<n>` | One hypothesis: a physical mechanism that could produce the symptom |
| `CON-<n>` | One containment action |
| `PDM-<category><option>` | One selected plan decision |
| `STEP-<n>` | One check plan step; branches as `STEP-2a`, `STEP-2b` |
| `RES-<n>` | One result, tied to exactly one `STEP-*` |
| `ASM-<n>` | One working value chosen without a stated source |
| `OPEN-<n>` | One unresolved item; it ends resolved, converted to an `ASM-*`, or carried to the next cycle |

---

## Frame the Event (once)

**Condition:** a tool is down or misbehaving and the cause is not known. New thread.

```xml
<context>
Input: the person's free description of the event, then their answers to your questions, plus any pass-downs, logs or work orders they attach. Treat every specific as one of:
- Binding: an observation or stated constraint with a source (a log row, a reading, a work order, a safety rule). The record must hold to it.
- Example: a specific given to illustrate a kind of thing. Restate it generally.
- Background: true, but it constrains nothing (who was on shift, which recipes ran). It stays out of the record.
- Guess: someone's idea of the cause. It becomes a hypothesis to test, kept out of the problem statement and the Binding items.

Interview dimensions:
1. What: the symptom, alarm text, and what the tool does that it shouldn't.
2. Where: which tool, chamber, module, lot or step shows it, and which similar ones do not.
3. When: first occurrence, pattern over time, and what changed just before (maintenance, parts, software, facilities, recipe).
4. How much: frequency, size of the deviation, downtime so far.
5. Containment: what has been done to the tool and to product run since the change.
6. Team and constraints: who works on it and when; safety, access, parts.

Status definitions:
- Clear: an explicit answer, and no second reasonable reading would change the problem statement or the hypotheses.
- Fuzzy: answered, but vague, conflicting, or open to two readings that lead to different hypotheses.
- Unknown: not yet discussed, or the person said they don't know.
</context>

<goal>
An 8D_Record.md v1.0 the person confirms: D0 to D3 complete, and a first hypothesis register listing every physical mechanism able to produce the symptom, so the search starts wide. Success: all six dimensions Clear, or every unresolved point recorded as an OPEN item, within four interview rounds.
</goal>

<limits>
- Interview turns contain only the round summary, dimension status and questions; causes appear only as HYP-* items in the draft record.
- Up to 3 questions per round, in plain language, each with options A, B and C as distinct, equally weighted outcomes, plus "D: None of these, or I don't know."
- Request logs, pass-downs or work orders by round 2; sort each one with the person.
- Record items hold only what the person stated or confirmed; your own inferences become OPEN items.
- Round 4 is the last round: anything still Fuzzy or Unknown becomes an OPEN item.
- Hypotheses come from how this kind of subsystem works (flow, pressure, temperature, sealing, sensing, control, supply, limits or settings), so the list holds for any tool of the type. Every hypothesis starts as Open with E 1 unless the interview gave binding evidence.
</limits>

<output>
Interview round (while any dimension is Fuzzy or Unknown, up to round 4):
1. Summary: 2 to 3 sentences.
2. Dimension status: list 1 to 6, each Clear, Fuzzy or Unknown.
3. Questions: 1 to 3, with options A to D.

Draft record (when all six are Clear, or after round 4):
1. Working: | Specific | Binding / Example / Background / Guess | Source |
2. 8D_Record.md v1.0 in one fenced markdown block:
   # 8D_Record.md v[version]
   ## D0 Event
   [symptom, tool, emergency action taken]
   ## D1 Team
   | Role | Who | Responsible for |
   ## D2 Problem Description
   [one sentence: object, defect, where, when, how much; observable terms only]
   | Dimension | Is | Is Not | Source |
   | What changed | Date | Source |
   ## D3 Containment
   | CON-n | Action | Status | Source |
   ## D4 Hypothesis Register
   | HYP-n | Mechanism | Status (Open / Ruled out / Confirmed) | Evidence for | Evidence against | Sources | Next discriminating check | E | C | Rank |
   Root cause: [NOT YET CONFIRMED, or the confirmed mechanism with its proof]
   Escape point: [NOT YET KNOWN, or why the problem wasn't caught]
   ## D5 Corrective Action
   [NONE YET, or the approved fix]
   ## D6 Implement and Verify
   [NONE YET, or the qual result]
   ## Guesses Recorded
   | Guess | Who | HYP-n |
   ## Cycle Log
   | Cycle | Evidence added | Hypotheses changed |
   ## Open Items
   | OPEN-n | What is unresolved |
   ## Change Log
   | Version | Change |
3. The line: "Reply Confirmed, or list the item IDs to correct."

After the reply: the corrected 8D_Record.md with stable IDs, in one fenced block.
</output>
```

---

## Hypothesis Update (every cycle)

**Condition:** a confirmed 8D record exists and there is new evidence: logged data, document sections, or a confirmed Results Report. New thread. Attach only the evidence for this cycle.

```xml
<context>
Latest 8D_Record.md:
[PASTE 8D_Record.md]

New evidence, binding (attached or pasted; one or more of):
- Data files: counts and comparisons come from them.
- Document sections: claims quote them.
- Results_Report.md, confirmed by the technician: results are tied to step IDs of the check plan named in it.

Ranking scales:
[PASTE HYPOTHESIS RANKING SCALES]
</context>

<goal>
The next version of 8D_Record.md, in which every hypothesis the new evidence touches has an updated status, evidence and rank; new hypotheses the evidence raises are added; the next discriminating check for each open hypothesis is the simplest one that rules out the most; and D3 to D6 reflect the new evidence. Success: the person can see from the change log exactly what this evidence changed and why.
</goal>

<limits>
- A status changes only on cited evidence: a count from executed code, a quoted document line with document and section, or a RES-* ID. Where code cannot run, the count reads COUNT NOT VERIFIED and the status stays as it was.
- A hypothesis is Ruled out only when evidence contradicts it; one that is merely less likely stays Open with a lower rank.
- A hypothesis is Confirmed only by a result that would differ if it were false (the fault returns or disappears with the mechanism), cited by RES-* ID.
- Every Open hypothesis keeps a next discriminating check; when the evidence points to a simpler or cheaper check than the one listed, the simpler one replaces it.
- When a hypothesis is confirmed, the record fills the root cause, the escape point if the evidence shows it, and leaves D5 as PROPOSED for the engineer.
- When the evidence dates when the mechanism started, D3 lists the product run since then for disposition, citing the evidence.
- When a result reads outside every open hypothesis, a new HYP-* is added from how the subsystem works.
- IDs stay stable; new items take the next unused ID. Table cells contain no raw pipe characters.
</limits>

<output>
1. Working: for each piece of evidence, the hypotheses it touches, the code run or the quote found, and the status change it supports.
2. 8D_Record.md with the version raised by 0.1, in one fenced markdown block, every section present, one new Cycle Log row, and one change-log line per change.
3. Next step, exactly one of: (a) plan the next checks; (b) a hypothesis is confirmed: plan the approved fix and the qual; (c) qual passed: the tool or process is released; go to Prevent Recurrence; (d) every hypothesis is ruled out: reopen the Frame with this record.
4. The line: "Reply Confirmed, or list the item IDs to correct."
</output>
```

---

## Record Review (after every Frame or Update)

**Condition:** after the person confirms a new record version. New thread.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
8D_Record.md under review (new version):
[PASTE NEW 8D_Record.md]

Source it came from (paste the one that applies):
- Frame: the person's interview answers, verbatim.
- Update: the previous 8D_Record.md version and the new evidence (attached data files, document sections, or Results_Report.md).
</context>

<goal>
A sanitized 8D_Record.md in which every item and every status change traces to its source, with each Patch finding corrected and each Keep finding left as written.
</goal>

<limits>
- Observable statement: the D2 problem statement contains only symptoms, locations, times and counts.
- Fidelity: every item matches the interview answers or the evidence; an unsupported item moves to Open Items.
- Sorting: every Guess and Background specific sits outside D2 and the Binding evidence.
- Counts: every count re-run with executed code; a mismatch is reported with both values.
- Quotes: every quoted line located verbatim; a quote not found verbatim is I = 5.
- Status changes: every changed status cites evidence that supports it; Ruled out rests on contradiction, Confirmed on a result that would differ if the hypothesis were false.
- Coverage: the Open hypotheses still cover every physical way the symptom can happen; add any the physics allows.
- IDs stay stable.
</limits>

<output>
1. Scorecard: | Check | Observation | I (1-5) | A (0-2) | Patch / Keep |, failed checks only.
2. 8D_Record.md with its version raised by 0.1 and a change-log line, in one fenced markdown block; or the line "No patches; record stands as v[version]."
</output>
```

---

## Check Plan (every cycle)

**Condition:** a reviewed 8D record exists and the next step is (a) or (b). New thread. The engineer takes part between the two prompts.

### Prompt A: Decision Menu

```xml
<context>
Latest 8D_Record.md:
[PASTE 8D_Record.md]
</context>

<goal>
A decision menu that puts every choice shaping this cycle's check plan in front of the engineer and ends with a request for selections. The plan follows the selections.
</goal>

<limits>
- Up to 4 categories, drawn from: which open hypotheses this cycle splits and in what order; downtime window; parts strategy; escalation (which results stop the technician and get reported).
- Each category offers options A, B and C as distinct outcomes, with pros, cons and the failure impact if wrong.
- Options include a repair only for a Confirmed hypothesis, and mark it as needing engineer approval.
- Each category cites the HYP-* and OPEN-* IDs it comes from.
- The response ends at the selection request.
</limits>

<output>
1. Menu: for each category, a heading, the IDs it addresses, | Option | Summary | Pros | Cons | Failure impact |, and a recommended default with its reason.
2. Selection request: one line asking for one option per category.
</output>
```

### Prompt B: Check Plan (same thread, after the engineer's selections)

```xml
<context>
Engineer's selections, binding:
[PASTE SELECTIONS]

Procedure and manual sections for the likely steps, binding sources:
[ATTACH OR PASTE]
</context>

<goal>
A Check_Plan.md the technicians can execute alone on nights or weekends: it splits the selected open hypotheses, performs a repair only for a confirmed hypothesis the engineer approved, ends every branch at a step, a stop-and-report point or the qual, and returns the tool to production only on a passed qual.
</goal>

<limits>
- Every step states action, reference, conditions (temperature, state, pressure, soak time), what to record (value, units, as-found and as-left), the HYP-* IDs it splits, and its branch rule as "If [result], go to STEP-n; if [result], go to STEP-m."
- Safety steps, lockouts and interlocks come from the cited procedures; where a procedure is silent, the step reads NOT IN SOURCE and becomes a stop-and-report point.
- A working value nobody stated becomes an ASM-* row marked ASSUMED. A spec, safety value or torque nobody stated reads NOT IN SOURCE and becomes an OPEN-* item.
- Stop-and-report points name their triggering results; at each one the technician stops, reports, and the results go back into the Hypothesis Update.
- Steps are numbered for this cycle only; the plan names its cycle number and the record version it came from.
- Table cells contain no raw pipe characters.
</limits>

<output>
1. Working: how the step order splits the selected hypotheses.
2. Check_Plan.md in one fenced markdown block:
   # Check_Plan.md, cycle [n], from 8D_Record.md v[version]
   ## 1. Hypotheses Being Split
   | HYP-n | Mechanism | Status | Rank |
   ## 2. Steps
   | STEP-n | Action | Reference | Conditions | Record (value, units) | Splits HYP-n | Branch |
   ## 3. Stop and Report Points
   | Trigger | Who to call | What to report |
   ## 4. Qual and Release Criteria
   [NOT THIS CYCLE, or the qual with its pass criteria]
   ## 5. Assumptions
   | ASM-n | Value | Used in STEP-n | Why assumed |
   ## 6. Open Items
   | OPEN-n | What is unresolved | Disposition |
</output>
```

---

## Mechanical Lint (plan review and results review threads)

**Condition:** before the Check Plan Review, and before the Results Review. Use a model with code execution, or run an equivalent script and paste its output. A lint read by eye is not valid.

```xml
<context>
Artifacts to lint, attached as files: Check_Plan.md, and Results_Report.md when linting results.
</context>

<goal>
A lint report produced by executed code that parses the Markdown tables, listing every violation of checks L1 to L11 exactly as the script prints it.
</goal>

<limits>
- L1 Table shape: every row has as many cells as its header.
- L2 Placeholders: no cell is empty or holds TBD, TBA, "...", "omitted", "as needed" or "unchanged".
- L3 Branch closure: every STEP-* has a Branch cell; every target is an existing STEP-*, "stop and report", or "qual".
- L4 Reachability: every STEP-* is reachable from STEP-1.
- L5 Units: every Record cell naming a reading names its units.
- L6 Conditions: every STEP-* with a reading has a filled Conditions cell.
- L7 Hypothesis coverage: every HYP-* in section 1 appears in at least one Splits cell.
- L8 Reference closure: every cited ASM-*, OPEN-* and PDM-* exists in its register or the selections.
- L9 Results closure (results only): every RES-* names exactly one existing STEP-*; every STEP-* on the path taken has a RES-*.
- L10 Results units (results only): every Reading cell has units and conditions.
- L11 Counts: totals of STEP-*, stop-and-report points, HYP-*, ASM-*, OPEN-*, and for results, RES-* and flags.
</limits>

<output>
1. Lint report: | Check | Row or ID | Violation |, one row per violation, or the line "Lint passed: zero violations in L1 to L10."
2. L11 counts: one line per ID family.
3. Script: one fenced code block.
</output>
```

Every L1 to L10 violation is a required patch: paste the lint report into the chat that built the artifact with the line `Emit corrected rows for these lint violations only`, then rerun the lint until it passes.

---

## Check Plan Review (every cycle)

**Condition:** in the plan review thread after the lint passes.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
Check_Plan.md under review:
[PASTE Check_Plan.md]

8D_Record.md it came from:
[PASTE 8D_Record.md]

Engineer's selections, verbatim:
[PASTE SELECTIONS]

Lint result: passed; counts [PASTE L11 COUNTS]. Mechanical checks L1 to L10 are settled.
</context>

<goal>
Either a Plan Release Certificate, when the plan passes every check below, or replacement rows for each Patch finding.
</goal>

<limits>
- Executability: a technician holding only the plan could perform every step as written; any A = 2 step is a finding.
- Discrimination: every step changes which hypotheses are open; a step that splits nothing is I = 3.
- Simplicity: no cheaper check in the record would split the same hypotheses; a costlier check chosen over a cheaper equivalent is I = 3.
- Confirmation: a repair for a hypothesis that is not Confirmed, or without engineer approval, is I = 5.
- Conditions: every measurement states conditions that match its cited procedure.
- Safety: every lockout, interlock and safety step the procedures require is present and cites its procedure.
- Selections: every selection is reflected, and only selected options appear.
- Sign-off integrity: every ASSUMED value is labeled as assumed; every carried-forward OPEN-* states what closes it.
</limits>

<output>
1. Scorecard: | Check | Observation | I (1-5) | A (0-2) | Pass / Fail |, failed checks only.
2. Either:
   - Plan Release Certificate: the L11 counts; the ASM-* and OPEN-* IDs carried; the line "Ready for engineer sign-off, cycle [n], with [n] assumptions and [m] open items."; then "Released by: ____ Date and time: ____"
   - or replacement rows only, for the plan chat to apply.
</output>
```

**Engineer sign-off:** the engineer reads the plan and the certificate, signs, and releases `Check_Plan.md` to the technicians.

---

## Technician Results (every cycle)

**Condition:** the technician has worked the released check plan to the qual or to a stop-and-report point. New thread.

```xml
<context>
Released Check_Plan.md, binding:
[PASTE Check_Plan.md]

Technician's notes, as written (any order, any wording):
[PASTE NOTES]

Definitions:
- Observation: what the technician saw, measured or did.
- Interpretation: what the technician thinks it means.
</context>

<goal>
A Results_Report.md the technician confirms, in which every step reached has one result tied to its STEP-* ID, every reading carries units and conditions, and observation sits apart from interpretation, ready to go back into the Hypothesis Update.
</goal>

<limits>
- Each RES-* records: done or not done, as-found, as-left, reading with units and conditions, and the branch taken.
- Every reading and observation comes from the notes; anything missing reads UNKNOWN and becomes a question.
- Flags cover: steps with no reading, readings without units or conditions, branches that differ from the plan's rule, and work outside the plan.
- Up to 3 questions, each with options A to C and "D: I don't know."
- Table cells contain no raw pipe characters.
</limits>

<output>
1. Results_Report.md in one fenced markdown block:
   # Results_Report.md, cycle [n], against Check_Plan.md cycle [n]
   ## 1. Results
   | RES-n | STEP-n | Done | As-found | As-left | Reading (units, conditions) | Branch taken | Observation | Interpretation |
   ## 2. Flags
   | RES-n or STEP-n | Flag |
2. Questions for the technician, or NONE.
3. The line: "Reply Confirmed, or answer the questions."
</output>
```

---

## Results Review (every cycle)

**Condition:** in the results review thread after the lint passes. The technician runs it before handing over.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
Results_Report.md under review:
[PASTE Results_Report.md]

Released Check_Plan.md it came from:
[PASTE Check_Plan.md]

Technician's notes, verbatim:
[PASTE NOTES]

Lint result: passed. Mechanical checks L1 to L10 are settled.
</context>

<goal>
A results scorecard covering the checks below, with replacement rows for each Patch finding, so the report can go into the Hypothesis Update.
</goal>

<limits>
- Fidelity: every result matches the technician's notes.
- Branch fidelity: each branch taken matches the plan's rule for the recorded result.
- Conditions: each reading was taken under the plan's stated conditions.
- Separation: every Observation cell holds only what was seen, measured or done.
- Off-plan work: work outside the plan is flagged; a part swapped outside the plan is I = 5.
</limits>

<output>
1. Scorecard: | Check | Observation | I (1-5) | A (0-2) | Pass / Fail |, failed checks only.
2. Replacement rows for the results chat to apply, or the line "Report stands; ready for the Hypothesis Update."
</output>
```

---

## Prevent Recurrence (D7)

**Condition:** the qual has passed and the record names a confirmed root cause. New thread.

```xml
<context>
8D_Record.md with the qual passed:
[PASTE 8D_Record.md]
</context>

<goal>
A D7_Actions.md the engineer can hand to the owners of procedures, limits and other tools: every action answers the confirmed root cause or the escape point, every action says how its effect would be verified, and every other tool or step where the same mechanism could occur is named as a place to check.
</goal>

<limits>
- Each action names what changes (a procedure step, a limit, a checklist, a training point, a sister tool), the root cause or escape point it answers, and how its effect would be verified.
- Each action answers why the problem happened or why it went uncaught; an action that answers neither stays out.
- Places where the record has no evidence read TO CHECK, not as findings.
- Owners and dates are left blank for the engineer.
- Table cells contain no raw pipe characters.
</limits>

<output>
1. Working: the root cause and escape point in one line each, and the gap each action closes.
2. D7_Actions.md in one fenced markdown block:
   # D7_Actions.md, from 8D_Record.md v[version]
   ## 1. Actions
   | D7-n | Action | What changes | Answers (root cause or escape point) | Verified by | Owner | Due |
   ## 2. Where Else
   | Tool or step | Why it could share the mechanism | TO CHECK |
</output>
```

### D7 Review

**Condition:** after D7_Actions.md is built. New thread.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
D7_Actions.md under review:
[PASTE D7_Actions.md]

8D_Record.md it came from:
[PASTE 8D_Record.md]
</context>

<goal>
A sanitized D7_Actions.md in which every action traces to the record, with each Patch finding corrected and each Keep finding left as written.
</goal>

<limits>
- Traceability: every action answers the confirmed root cause or the escape point as the record states them; an action with no trace is I = 4.
- Coverage: the escape point has at least one action; a missing one is I = 4.
- Verification: every action states an observable check of its effect.
- Where else: every tool or step that shares the subsystem with the failed one is listed, marked TO CHECK.
</limits>

<output>
1. Scorecard: | Check | Observation | I (1-5) | A (0-2) | Patch / Keep |, failed checks only.
2. The corrected D7_Actions.md in one fenced markdown block, or the line "No patches; D7 actions stand."
</output>
```

After the engineer assigns owners, paste the D7 actions into the record's D7 section with a change-log line.

---

## Close and Lesson (D8)

**Condition:** the record has D6 passed and D7 filled. New thread.

```xml
<context>
Closed 8D_Record.md:
[PASTE 8D_Record.md]
</context>

<goal>
Two things the engineer can sign: a closure summary for the 8D (D8), and a Lesson_Learned.md that the next person who sees the same symptom on any tool of this type finds with a search and can act on in under five minutes.
</goal>

<limits>
- The lesson's title and first line use the words a person would type when the symptom appears: the alarm text, the reading, and the tool type.
- Every statement in the lesson comes from the closed record; anything the record lacks reads NOT IN SOURCE.
- The lesson states the earliest observable sign that would have pointed to the cause, from the record's data.
- Contributions name the role and what it did, from D1 and the cycle log.
- Downtime and cycle counts come from the record.
</limits>

<output>
1. D8 closure summary: | Item | Content | for problem, root cause, fix, qual result, D7 actions, total downtime, cycles run, contributions.
2. Lesson_Learned.md in one fenced markdown block:
   # [symptom in search words], [tool type]
   ## Symptom
   ## Signature (what distinguishes it)
   ## Cause and proof
   ## Fix
   ## Earliest sign it was this
   ## Source: 8D_Record.md v[version]
3. Self-check: | Lesson statement | Record section it comes from |, one row per statement.
4. The line: "Reply Confirmed, or list the items to correct."
</output>
```

**Engineer sign-off:** the engineer signs the closure, files the lesson where the team searches for past events, and the record's change log takes its final line.

---

## Improving This Playbook

After each event, write one line on what you had to correct. Change the prompt that caused it, rerun the changed prompt on the same input before saving it, and add a change-log line below.

## Change Log

| Date | Version | Change | Why |
|:---|:---|:---|:---|
| 2026-11-14 | v0.5 | Rebuilt as an iterative 8D loop around one living, versioned 8D_Record.md: Frame (D0 to D3), Hypothesis Update every cycle with data, documents or technician results (D4), Check Plan per cycle with fix only for a confirmed hypothesis (D5) and the qual (D6), Technician Results feeding back into the same record; optional D7 handoff | Andrew: the workflow is iterative and follows 8D; technician findings go back into the same workflow to update the hypotheses |
| 2026-11-14 | v0.5 | Every 8D discipline gets an AI step: D7 Prevent Recurrence with its review in the main flow; new D8 Close and Lesson prompt; D3 containment updated from evidence; process-troubleshooting note | Andrew: go through all of the steps of 8D with AI to show its versatility; reference process troubleshooting |
