# Process Development Playbook: Plan an Experiment (draft v0.4)

Draft for a trial run, 2026-11-14. Same structure as the Systems Engineering Playbook v2. Every prompt is written to the Prompt Evaluation Rubric v3.2 (reference/Prompt-Evaluation-Rubric.md). Gemini Enterprise only.

Do these procedures in sequence to turn what you know about a process question into a confirmed Experiment Brief and a Golden Run Sheet (`Golden_RunSheet_v1.1.md`) with its analysis plan fixed before any data exists:

- **Stage 0 (Brief):** Talk the problem through, answer the interview, and confirm an Experiment Brief written to the Experiment Brief Standard.
- **Stage 1 (Design Menu):** Lay out the designs that could answer the brief inside its limits, choose, and confirm a Design Decision Record.
- **Stage 2 (Run Sheet):** Build the run sheet and analysis plan from the brief and the decision record, lint it, review it.
- **Stage 3 (Your Review):** Walk the run sheet as if you were running it. A missing or wrong requirement goes back into the brief as a versioned change, and the cycle restarts from the revised brief.
- **Stage 4 (Risk and Release):** Find how the experiment itself can fail, choose the mitigations, consolidate the Golden Run Sheet, lint it, release it.

Stages are work phases for the person running the playbook. The prompts name only artifacts (the brief, the decision record, the run sheet), never stages.

Every prompt is first-principles: it names no tool, film, product or site. The specifics of your project arrive as your answers and your files, never in the saved prompts.

**Where the standard comes from.** The Experiment Brief Standard below adapts the pre-experiment planning checklist used in industrial DOE practice (Coleman and Montgomery, *Technometrics*, 1993) and the INCOSE rules for well-formed requirements (one fact per statement, verifiable, no TBD). The run sheet is checked by an executed-code lint for the mechanical rules and an anchored review for judgment.

---

## Thread Map

Work and review never share a thread. Each artifact is fixed in the thread that built it, and only the fixed artifact moves on.

| Thread | Purpose | What to paste or attach |
|:---|:---|:---|
| Thread 1 (work) | Talk it through, interview, Experiment Brief v1.0 | The Discovery Interview prompt, then talk. Attach files when the interview asks. |
| Review thread R0 (new) | Brief Lint, then Brief Review | Brief standard block, review gate block, your own Thread 1 messages (numbered, word for word), the Experiment Brief |
| Thread 2 (work) | Design Decision Menu, then Design Decision Record | Experiment Brief, limits file if you have one |
| Review thread R1 (new) | Design Menu Review | Review gate block, Experiment Brief, Design Decision Menu |
| Thread 3 (work) | Run Sheet v1.0, risk, Golden Run Sheet | Experiment Brief, Design Decision Record, limits file |
| Review thread R2 (new) | Run Sheet Lint, then Design Review | Review gate block, Experiment Brief, Design Decision Record, Run Sheet v1.0 |
| Thread C (new, only when needed) | Brief Change | Experiment Brief, your change notes word for word |
| Review thread R4 (new) | Run Sheet Lint, then Release Review | Review gate block, Experiment Brief, Design Decision Record, your risk selections, Golden Run Sheet |

After each review, paste its patch block into the thread that built the artifact, apply it there, then move on.

**Your own messages, word for word.** R0 checks the brief against what you said, not against what the AI said. Copy each of your Thread 1 messages in order and number them `M1`, `M2`, and so on. Leave out the AI's turns.

---

## Pasteable Blocks

### 1. Experiment Brief Standard (Thread 1 and R0)

```xml
<brief_standard>
Every brief item meets all of:
S1 Singular: one fact per item.
S2 Quantified: every number has a unit; every spec or limit has a direction (at or below, at or above, between).
S3 Sourced: every item cites the person's message (M<n>), a file and line, an ASM-* ID or an OPEN-* ID.
S4 Sorted: every specific the person mentioned is Binding, Example, Background or Guess. Binding items appear as stated. Example items appear only in section 4, restated in general terms. Background items appear only in section 4. Guess items become ASM-* or OPEN-* items.
S5 Verifiable: a reader can tell from a measurement or a record whether the experiment met the item.
S6 Solution-neutral: no design family, factor level or run count.
S7 Complete: the brief holds the decision the result drives; every response with spec, measurement method and repeatability; every factor with limit, source of the limit and whether it is hard to change between runs; the believed mechanism; the budget in units and time; the equipment in scope; every group that differs physically (tool, chamber, lot, shift); safety rules; success criteria; non-goals. A missing field is an OPEN-* item.
S8 Resolved or open: never write TBD; every unresolved point is an OPEN-* item naming what is needed to close it.
S9 Versioned: the brief carries a version number and a change log.
</brief_standard>
```

### 2. Review Gate (every review thread)

```xml
<review_gate>
Rate every finding on two anchored scales, using the anchor text.

Impact (I):
- 1 Cosmetic: wording or formatting only; the experiment is unchanged.
- 2 Local: one run, level or plan item is weaker than it should be; nothing else depends on it.
- 3 Propagating: one item is wrong or unclear, and the run sheet, the analysis plan, or another item depends on it.
- 4 Structural: the design family, the blocking, the replication, or several runs are affected.
- 5 Experiment-breaking: the experiment cannot answer its question, breaks a hard limit or safety rule, exceeds the budget, or an item has no source.

Ambiguity (A):
- 0 Two engineers would run the same units in the same order and analyze them the same way.
- 1 Two engineers would run the same experiment with small differences in setup.
- 2 Two engineers could run different experiments, or the item cannot be executed as written.

Gate:
- Patch when I >= 4 (any A), or when I = 3 and A = 2.
- Keep in every other case; record it in the scorecard only.
- Keep stylistic variation and mathematical limits ("at or below", "at or above").
- Lint violations are always patched and carry no score.
</review_gate>
```

### 3. Missing Data Rules (inside every work prompt)

```xml
<missing_data>
- Fill every cell with a stated value, an ASM-* ID or an OPEN-* ID.
- For a value the brief does not state, choose a working value, mark it Assumed, and add an ASM-* row with its consequence if wrong.
- For a hard limit or safety rule the brief does not state, add an OPEN-* item and write no run that depends on it.
- Never write TBD.
</missing_data>
```

### 4. Risk Gate (the risk prompt)

```xml
<risk_gate>
RPN = Severity (S) x Plausibility (P) x Plan Gap (G).
S: 1 no effect on the result; 2 delay, recovered without extra units; 3 a run lost or repeated, caught before analysis; 4 a wrong or confounded result used in a decision, or the budget exceeded; 5 safety harm, equipment damage, or product put at risk.
P: 1 needs several independent faults; 2 rare edge condition; 3 expected occasionally; 4 expected regularly; 5 expected in nearly every run unless mitigated.
G: 0 a run sheet item or analysis rule prevents or detects it, and a lint check or review exercises it; 0.5 covered in part, or nothing checks it; 1 nothing in the plan addresses it.
Tier 1: RPN >= 12, or S = 5 with G >= 0.5. Tier 2: everything else.
</risk_gate>
```

### 5. Identifiers (for the person running the playbook)

| ID | Meaning |
|:---|:---|
| `M<n>` | Your nth message in Thread 1 |
| `EB-<section>.<n>` | One item in the Experiment Brief |
| `OPEN-<n>` | One unresolved item |
| `ASM-<n>` | One value chosen without a statement from you |
| `DM-<category><option>` | One selected design option, for example `DM-1B` |
| `RDM-<category><option>` | One selected risk policy option |
| `FM-<n>` | One way the experiment can fail |
| `RUN-<nn>` | One run (one unit processed at one setting) |

Every `OPEN-*` item ends in exactly one disposition: closed by a selection, converted to an `ASM-*`, or carried forward.

---

## Discovery Interview (Thread 1)

**Condition:** You need an experiment, and the question, the limits and the budget are not yet written down. Paste this prompt, then talk: say what you're trying to do, what you've heard, what worries you, the way you'd tell a colleague.

```xml
<brief_standard>
[PASTE EXPERIMENT BRIEF STANDARD BLOCK]
</brief_standard>

<dimensions>
1. Objective and decision: the decision the result will drive, and what "done" looks like.
2. Responses: every measured output, its spec, its measurement method, its measurement repeatability, and the later steps that depend on it.
3. Factors: every changeable input, its physical or equipment limit and the source of that limit, and which inputs are hard to change between runs.
4. Mechanism: the physical or chemical effect believed to link factors to responses, expected interactions, and earlier results.
5. Constraints: budget in units and time, equipment in scope, groups that differ physically, safety rules.
6. Success criteria and non-goals.
</dimensions>

<definitions>
Status of a dimension:
- Clear: an explicit statement with only one reasonable reading.
- Fuzzy: vague, conflicting, or open to two readings that lead to different experiments.
- Unknown: not discussed, or the person does not know.
Sort of a specific (a named tool, file, number, past experiment or story):
- Binding: in scope; the experiment must respect exactly this.
- Example: an instance offered to illustrate a general need.
- Background: true and relevant context that constrains nothing.
- Guess: the person's estimate, not a known value.
</definitions>

<input_treatment>
The person's messages are free talk. Rate each dimension against the definitions, and sort each specific; a specific stays unsorted until the person confirms its sort. Attached files are Binding only where the person says so.
</input_treatment>

<goal>
Produce Experiment Brief v1.0, confirmed by the person, that meets every rule in the brief standard. Success: every dimension is Clear, or every remaining gap is an OPEN-* item; the person replies Confirmed.
</goal>

<limits>
- Ask at most 3 plain-language questions per round, each with options A, B, C and "D: None of these, or I don't know." Options are distinct answers of comparable appeal.
- By round 2, ask for the limits file, the spec list and earlier reports, and confirm the sort of each.
- Ask about the problem only; design choices belong to the design menu.
- Record only what the person stated or confirmed, citing the message. Record each of your own inferences as an OPEN-* item.
- Exit after the round in which every dimension is Clear, or after round 5; then convert every Fuzzy or Unknown dimension into OPEN-* items and emit the draft.
</limits>

<output>
Each round:
1. Dimension status: numbered list 1 to 6, each Clear, Fuzzy or Unknown, with the message IDs behind it.
2. Specifics to sort: | Specific | Message | Proposed sort | (new specifics only, or NONE)
3. Questions: 1 to 3, with A/B/C/D options.

Draft, then final after the person's reply: one fenced markdown block titled `# Experiment Brief v1.0`, one bullet per item, each ending with its source in brackets, IDs `EB-<section>.<n>` in sections 1 to 6 and `OPEN-<n>` in section 7:
## 1. Objective and Decision
## 2. Responses, Specs and Measurement
## 3. Factors and Limits
## 4. Mechanism, Prior Learning, Examples and Background
## 5. Budget, Scope, Groups and Safety
## 6. Success Criteria and Non-Goals
## 7. Open Items
## 8. Change Log
| Version | Date | Change | Items affected |
After the draft: "Reply Confirmed, or list the item IDs to correct."
</output>
```

---

## Brief Lint and Brief Review (New Review Thread R0)

**Condition:** You have Experiment Brief v1.0. Start a new thread. Paste the lint prompt first; when it passes, paste the review prompt in the same review thread.

### Brief Lint

```xml
<brief>
[PASTE EXPERIMENT BRIEF]
</brief>

<input_treatment>
The brief is text to test exactly as written; judge no content.
</input_treatment>

<goal>
Report every violation of checks B1 to B6, computed by code you write and execute on the brief text. Success: the report lists every violation, or states that none exist.
</goal>

<checks>
- B1 IDs: every item has an ID of the form EB-<section>.<n> or OPEN-<n>; no ID repeats.
- B2 Sources: every item ends with a bracketed source of the form M<n>, a file name, ASM-<n> or OPEN-<n>.
- B3 Units: every number in sections 2, 3 and 5 is followed by a unit.
- B4 Placeholders: the text "TBD" appears nowhere.
- B5 Sections: headings 1 to 8 are present and in order.
- B6 Counts: items per section; OPEN-* items.
</checks>

<output>
1. Code: one fenced code block.
2. B6 counts: one line per section.
3. Lint report: | Check | Item ID | Violation |, or exactly: `Lint passed: zero violations in B1 to B5.`
</output>
```

Paste every violation into Thread 1 with `Correct these lint violations in the brief and reissue it.` Rerun the lint on the reissued brief until it passes.

### Brief Review

```xml
<brief_standard>
[PASTE EXPERIMENT BRIEF STANDARD BLOCK]
</brief_standard>

<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<person_messages>
[PASTE YOUR OWN THREAD 1 MESSAGES, NUMBERED M1, M2, ..., WORD FOR WORD]
</person_messages>

<brief>
[PASTE THE LINTED EXPERIMENT BRIEF]
</brief>

<input_treatment>
The person's messages are the only evidence of what the person wants. The brief is the artifact under review. The lint has settled IDs, source format, units, placeholders and section order.
</input_treatment>

<goal>
Produce a scorecard of every judgment finding on the brief, rated by the review gate, and corrected items for Patch findings only. Success: every brief item is checked against the person's messages and against rules S1, S4, S5, S6 and S7.
</goal>

<criteria>
- Fidelity: every item says what the cited message says, with no added scope; an item whose message does not support it is a finding.
- Sorting: every specific in the messages is sorted, and Example, Background and Guess items are handled as rule S4 states.
- Verifiability: every item can be judged met or not met from a measurement or record.
- Neutrality: no item fixes a design family, level or run count.
- Completeness: every field rule S7 requires is an item or an OPEN-* item.
</criteria>

<limits>
- Quote the message text that supports or contradicts each finding, or write NO SUPPORT.
- When the messages do not settle a finding, rate it A = 2 and propose an OPEN-* item instead of a correction.
- Keep IDs stable; new items take the next unused ID.
</limits>

<output>
1. Review scorecard: | Item ID | Criterion | Message quote or NO SUPPORT | Observation | I (1-5) | A (0-2) | Gate (Patch / Keep) |
2. Patch block: corrected and new items, each with ID and source, or exactly: `Experiment Brief passed review.`
</output>
```

Paste the patch block into Thread 1 with `Apply these patches, record a change log line, and reissue the brief for my confirmation.` Confirm it. That confirmed brief is the only thing that leaves Thread 1.

---

## Design Decision Menu (New Thread 2)

**Condition:** You have a confirmed, reviewed Experiment Brief. Start a new thread.

```xml
<brief>
[PASTE EXPERIMENT BRIEF]
</brief>

<limits_file>
[ATTACH THE LIMITS FILE, OR WRITE NONE]
</limits_file>

<input_treatment>
The brief is the complete statement of requirements: every EB-* item is binding as written, section 4 is context only, and every OPEN-* item needs a disposition. The limits file is binding where the brief cites it.
</input_treatment>

<goal>
Produce a Design Decision Menu of distinct experiment designs that can answer the brief's question inside its limits and budget, ending in a request for the person's selections. Success: every option is feasible, its costs and blind spots are stated, and the recommended default can estimate every effect in the question trace.
</goal>

<limits>
- Match design families to what the question needs: comparing settings, screening for main effects, estimating named interactions, or mapping curvature.
- Keep every option inside the binding limits and the budget, citing the EB-* IDs behind each.
- Give every OPEN-* item exactly one disposition: a menu category, or a row in the disposition table.
- Stop after the selection prompt; the run sheet is built from the decision record in a later thread.
</limits>

<missing_data>
[PASTE MISSING DATA RULES BLOCK]
</missing_data>

<output>
## 1. Question Trace
| Question (EB-*) | Effect to estimate | Smallest effect worth detecting | Measurement repeatability (EB-* or ASM-*) |
## 2. Design Decision Menu
At most 4 categories, covering design family, replication and noise estimate, blocking by groups that differ physically, and spares and run order. For each:
- Open items addressed: IDs
- | Option (A/B/C) | Summary | Units used | Can estimate | Aliased with | Failure impact |
- Recommended default: option and one-sentence rationale
## 3. Open Item Disposition Table
| OPEN-* | Assume / Carry Forward | Working assumption or reason to defer |
## 4. Selection Prompt
One line asking for one option per category in the form `<category><option>`, and acceptance or changes to each disposition.
</output>
```

---

## Design Menu Review (New Review Thread R1)

**Condition:** You have the Design Decision Menu and have not yet chosen. Start a new thread.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<brief>
[PASTE EXPERIMENT BRIEF]
</brief>

<menu>
[PASTE DESIGN DECISION MENU]
</menu>

<input_treatment>
The brief is the requirement; the menu is the artifact under review.
</input_treatment>

<goal>
Produce a scorecard of every finding on the question trace and the menu, rated by the review gate, with replacement rows for Patch findings only. Success: every criterion below is checked against every menu row.
</goal>

<criteria>
- Coverage both ways: every question, response, limit, group and budget figure in the brief appears in the menu, and every menu row cites an EB-* or OPEN-* ID.
- Feasibility: every option stays inside every binding limit, the budget and the non-goals, with correct unit counts and aliasing.
- Distinctness: options are different designs, not one design with different labels.
- Every OPEN-* item has exactly one disposition.
- The recommended default can estimate every effect in the question trace.
- Section 4 material of the brief shapes no option.
</criteria>

<limits>
- When a unit count or alias cannot be confirmed from the menu as written, rate the finding A = 2 and name what is missing.
</limits>

<output>
1. Review scorecard: | Row or category | Criterion | Observation | I (1-5) | A (0-2) | Gate (Patch / Keep) |
2. Patch block: corrected rows or categories for Patch findings, or exactly: `Design Menu passed review and is ready for selection.`
</output>
```

---

## Design Decision Record (Thread 2)

**Condition:** You have the Design Menu Review result. Paste its patch block and your selections in Thread 2.

```xml
<menu_patches>
[PASTE PATCH BLOCK, OR WRITE NONE]
</menu_patches>

<selections>
[ONE OPTION PER CATEGORY, AND YOUR CHANGES TO DISPOSITIONS]
</selections>

<input_treatment>
The selections are binding as written. The menu earlier in this thread, with the patches applied, defines what each selection means.
</input_treatment>

<goal>
Produce the Design Decision Record: a standalone record of what was chosen and why, which a new thread can build the run sheet from without this conversation. Success: every category has one selection, every OPEN-* item has a disposition the person accepted, and every ASM-* has its consequence if wrong.
</goal>

<missing_data>
[PASTE MISSING DATA RULES BLOCK]
</missing_data>

<output>
One fenced markdown block titled `# Design Decision Record v1.0`:
## 1. Question Trace
Same columns as the menu.
## 2. Selections
| DM ID | Category | Option chosen, stated in full | Units used | Can estimate | Aliased with |
## 3. Open Item Dispositions
| OPEN-* | Disposition | Working assumption or reason to defer |
## 4. Assumptions
| ASM ID | Assumption | Affected IDs | Consequence if wrong | Sign-off (Pending) |
End with: "Reply Confirmed, or list the IDs to correct."
</output>
```

---

## Run Sheet and Analysis Plan (New Thread 3)

**Condition:** You have the confirmed Experiment Brief and Design Decision Record. Start a new thread.

```xml
<brief>
[PASTE EXPERIMENT BRIEF]
</brief>

<decision_record>
[PASTE DESIGN DECISION RECORD]
</decision_record>

<limits_file>
[ATTACH THE LIMITS FILE, OR WRITE NONE]
</limits_file>

<input_treatment>
The brief and the decision record are binding as written. Section 4 of the brief is context for the riskiest-runs table only.
</input_treatment>

<goal>
Produce Run Sheet v1.0 with an analysis plan fixed before any data exists. Success: two engineers would run it the same way, every interaction named in the brief's question is estimable, and every response has a stated pass rule.
</goal>

<limits>
- Levels in engineering units, inside the binding limits.
- Run order randomized with a stated seed, blocked by every group the brief says differs physically.
- Smallest detectable effect stated for each response from its measurement repeatability.
- Run exclusion rule stated now, before results exist.
- Riskiest runs justified from the mechanism in the brief.
- Every row written in full; if the output limit is near, end on a complete row and write `CONTINUE`.
</limits>

<missing_data>
[PASTE MISSING DATA RULES BLOCK]
</missing_data>

<output>
One fenced markdown block titled `# Run Sheet v1.0`:
## 1. Run Sheet
| RUN ID | Run order | Block | One column per factor (engineering units) | Source (DM-* or EB-*) |
## 2. Estimable Effects
| Effect | Estimable (Yes / No) | Aliased with |
## 3. Detectable Effect by Response
| Response (EB-*) | Repeatability | Smallest detectable effect | Provenance (Stated / Assumed) |
## 4. Analysis Plan
| Response (EB-*) | Model terms | Pass rule against spec | Groups analyzed separately | Run exclusion rule |
## 5. Riskiest Runs
| RUN ID | Why (mechanism, EB-*) | Mitigation |
## 6. Assumptions Register
| ASM ID | Assumption | Affected IDs | Consequence if wrong | Sign-off (Pending / Confirmed) |
## 7. Open Items Register
| OPEN-* | Description | Disposition | What is needed to close |
</output>
```

---

## Run Sheet Lint (New Review Threads R2 and R4)

**Condition:** Run before the Design Review on Run Sheet v1.0, and before the Release Review on the Golden Run Sheet. The checks need executed code; a model reading the tables misses violations.

```xml
<files>
[ATTACH THE RUN SHEET, THE EXPERIMENT BRIEF, THE DESIGN DECISION RECORD AND THE LIMITS FILE]
</files>

<input_treatment>
The brief, decision record and limits file are the reference; the run sheet is the file under test. Judge no content beyond the checks.
</input_treatment>

<goal>
Report every violation of checks L1 to L7, and the counts in L8, computed by code you write and execute on the attached files. Success: the report lists every violation, or states that none exist.
</goal>

<checks>
- L1 Limits: every level of every run is inside the binding limit for that factor.
- L2 Budget: runs plus spares are at or below the budget.
- L3 Design shape: each factor has the number of levels the selected design calls for, and every design point appears the planned number of times.
- L4 Randomization: within each block, the rank correlation between run order and each factor is 0.5 or less in magnitude.
- L5 Aliasing: from the model matrix, every interaction named in the brief's question is estimable and unaliased with another two-factor interaction.
- L6 Coverage: every response in the brief appears in the analysis plan.
- L7 Placeholders: every cell holds a value, an ASM-* ID or an OPEN-* ID.
- L8 Counts: runs, blocks, center or replicate points, spares, ASM-* rows (and how many Pending), OPEN-* items.
</checks>

<limits>
- When a file needed for a check is missing, report that check as NOT RUN with the missing file.
</limits>

<output>
1. Code: one fenced code block.
2. L8 counts: one line per item.
3. Lint report: | Check | Row or ID | Violation |, or exactly: `Lint passed: zero violations in L1 to L7.`
</output>
```

Paste every violation into Thread 3 with `Correct these lint violations and reissue the run sheet.` Rerun the lint until it passes.

---

## Design Review (Review Thread R2, after the lint passes)

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<brief>
[PASTE EXPERIMENT BRIEF]
</brief>

<decision_record>
[PASTE DESIGN DECISION RECORD]
</decision_record>

<run_sheet>
[PASTE THE LINTED RUN SHEET v1.0]
</run_sheet>

<input_treatment>
The brief and the decision record are the requirements; the run sheet is the artifact under review. The lint has settled L1 to L7.
</input_treatment>

<goal>
Produce a ledger of judgment findings on Run Sheet v1.0 and its analysis plan, rated by the review gate, with replacement rows for Patch findings only. Success: every criterion below is checked.
</goal>

<criteria>
- Question fit: the design answers every question in the brief at the smallest effect worth detecting.
- Physical sense: the riskiest runs match where the mechanism predicts instability, and every response the mechanism predicts will move is measured.
- Groups: every group that differs physically is blocked or deliberately held constant, and the plan says which.
- Downstream: every later step that depends on a response is listed, with that response measured.
- Analysis plan: the exclusion rule is fixed before results, and every response is judged within the groups the brief says differ.
</criteria>

<limits>
- When the mechanism in the brief is too thin to judge physical sense, rate the finding A = 2 and propose an OPEN-* item.
</limits>

<output>
1. Compliance ledger: | Row or ID | Criterion | Observation | I (1-5) | A (0-2) | Gate (Patch / Keep) |
2. Patch block: corrected rows for Patch findings, or exactly: `Run Sheet v1.0 passed Design Review.`
</output>
```

Paste the patch block into Thread 3 with `Apply these patches and reissue the run sheet.`

---

## Your Review and Brief Change (Agile cycle)

**Condition:** Run Sheet v1.0 has passed the Design Review. Now you review what was built.

Walk the run sheet as if you were loading the units: the order, the settings, the measurements, the pass rules. You are looking for a requirement that is missing or wrong in the brief, not for a better run sheet.

- **A requirement changed** (a spec you forgot, a limit that is wrong, a group that differs, a response nobody measures): it goes into the brief. Run the prompt below in a new thread, confirm the revised brief, rerun the Brief Lint and Brief Review on the changed items, then start a new Thread 2 from the revised brief.
- **The brief is right but the run sheet misses it**: paste your note into Thread 3 and have it reissue the run sheet. Then rerun the lint.
- **Nothing to change**: go on to the risk prompt in Thread 3.

### Brief Change (New Thread C)

```xml
<brief_standard>
[PASTE EXPERIMENT BRIEF STANDARD BLOCK]
</brief_standard>

<brief>
[PASTE EXPERIMENT BRIEF]
</brief>

<change_notes>
[YOUR CHANGE NOTES, WORD FOR WORD, NUMBERED M1, M2, ...]
</change_notes>

<input_treatment>
The change notes are free talk: sort each specific as Binding, Example, Background or Guess, and confirm the sort with the person before it changes an item. The brief stands as written except where a note changes it.
</input_treatment>

<goal>
Produce the next version of the Experiment Brief with every change the person confirmed, a change log line per change, and a list of the items each change affects. Success: the revised brief meets every rule in the brief standard, and every changed item cites its note.
</goal>

<limits>
- Change only the items the notes reach; keep every other item and ID as written.
- New items take the next unused ID; a removed item stays listed in the change log.
- When a note conflicts with an item it does not name, ask before changing either.
</limits>

<output>
1. Sorting: | Specific | Note | Proposed sort |, or NONE.
2. Questions: 1 to 3 with A/B/C/D options, or NONE.
3. Revised brief: one fenced markdown block titled `# Experiment Brief v<next version>`, all sections, with the new change log line in section 8.
4. Items affected: | ID | Change | Run sheet sections that depend on it |
End with: "Reply Confirmed, or list the item IDs to correct."
</output>
```

---

## Experiment Risk Ledger and Risk Decision Menu (Thread 3)

**Condition:** Run Sheet v1.0, with the Design Review patches applied, is the last run sheet in Thread 3, and your review changed no requirement.

```xml
<risk_gate>
[PASTE RISK GATE BLOCK]
</risk_gate>

<lenses>
1. Measurement integrity: a metrology failure, a measurement that cannot resolve the effect, an unread data-quality note.
2. Execution continuity: an aborted run, a setting the equipment cannot hold, units processed out of order.
3. Hidden variation: drift over time, an unblocked group that differs physically, an uncontrolled input.
4. Analysis traps: pooling groups that differ, an interaction aliased away, a run excluded after seeing the result.
5. Safety, equipment and product: a setting outside a safe operating window, risk to equipment or product units.
</lenses>

<input_treatment>
The last run sheet in this thread is the artifact to analyze; the brief and decision record at the top of this thread are binding.
</input_treatment>

<goal>
Produce a ranked risk ledger of how this experiment can fail, delta rows that close every Tier 1 risk, and a Risk Decision Menu for the choices those deltas need, ending in a request for the person's selections and assumption sign-off. Success: every Tier 1 risk has a delta row or a menu category, and every G below 1 names the items that cover it.
</goal>

<limits>
- Cover all 5 lenses. Score the 5 to 8 failure modes with the highest expected RPN; list the rest in one line each.
- Justify every G below 1 with the run sheet or analysis plan items that cover it.
- Score at least one failure mode for every ASM-* whose consequence if wrong is S 4 or 5.
- Tier 1 delta rows use the run sheet's column layout; Tier 2 risks appear in the ledger only.
- At most 5 menu categories; Tier 1 choices outside the menu go under Defaults Applied Without Menu.
</limits>

<missing_data>
[PASTE MISSING DATA RULES BLOCK]
</missing_data>

<output>
## 1. Ranked Risk Ledger
| FM ID | Lens (1-5) | Failure summary | Mitigating items | S | P | G | RPN | Tier |
### Unscored Failure Modes
One line each: lens and failure summary.
## 2. Tier 1 Delta Rows
Run sheet, analysis plan, ASM and OPEN rows, each in the column layout of Run Sheet v1.0.
## 3. Risk Decision Menu
For each category: Governing FM IDs; | Option (A/B/C) | Policy or threshold | Trade-off |; Recommended default.
## 4. Defaults Applied Without Menu
| Governing FM ID | Default applied | How to override |
## 5. Assumptions for Sign-Off
| ASM ID | Assumption | Consequence if wrong | Status (Pending) |
End with one line asking the person to confirm, correct, or leave each assumption pending, and to choose one option per category.
</output>
```

---

## Golden Run Sheet (Thread 3)

**Condition:** Reply to the Risk Decision Menu.

```xml
<risk_selections>
[ONE OPTION PER CATEGORY, WITH ANY CHANGES]
</risk_selections>

<default_overrides>
[OVERRIDES, OR WRITE NONE]
</default_overrides>

<assumption_signoff>
[FOR EACH ASM ID: CONFIRMED, CHANGED TO A VALUE, OR PENDING]
</assumption_signoff>

<input_treatment>
The selections, overrides and sign-off are binding as written. The last run sheet and the Tier 1 delta rows in this thread are the material to consolidate.
</input_treatment>

<goal>
Produce Golden_RunSheet_v1.1.md: one complete, standalone document with every approved change applied, ready for the Release Review. Success: every Tier 1 delta row and every selection appears in the rows it changes, and nothing else changed.
</goal>

<limits>
- Write every section and row in full. If the output limit is near, end on a complete row and write `CONTINUE`.
- Cite risk selections in the Source column as RDM-* IDs; FM-* IDs and version notes stay out of the run sheet and rationale.
- Set each ASM-* to Confirmed or Pending exactly as the sign-off states.
- Carry every unresolved OPEN-* item into the open items register.
- When a selection conflicts with a delta row, apply the selection and add an OPEN-* item naming the conflict.
</limits>

<output>
One fenced markdown block titled `# Golden Run Sheet (Golden_RunSheet_v1.1)` with the seven sections and table columns of Run Sheet v1.0.
</output>
```

---

## Release Review (New Review Thread R4, after the lint passes on the Golden Run Sheet)

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<brief>
[PASTE EXPERIMENT BRIEF]
</brief>

<decision_record>
[PASTE DESIGN DECISION RECORD]
</decision_record>

<risk_selections>
[PASTE YOUR RISK SELECTIONS, OVERRIDES AND SIGN-OFF, WORD FOR WORD]
</risk_selections>

<golden_run_sheet>
[PASTE THE LINTED GOLDEN RUN SHEET]
</golden_run_sheet>

<input_treatment>
The brief, decision record and risk selections are the requirements; the Golden Run Sheet is the artifact under review. The lint has settled L1 to L7.
</input_treatment>

<goal>
Decide whether the experiment is ready to run, and list what must close before the first run. Success: every RDM-* selection is traced to the rows it changed, every question and response in the brief is still covered, and every open item that could change a result has an owner.
</goal>

<limits>
- Report failed checks only in the ledger.
- When an owner is not stated, write OWNER NEEDED.
</limits>

<output>
1. Release ledger: | Row or ID | Check | Observation | I (1-5) | A (0-2) | Gate (Patch / Keep) |
2. Before the first run: | ASM-* or OPEN-* | Could change a result because | Owner |
3. Release statement: corrected rows for Patch findings, or exactly: `Golden Run Sheet passed Release Review and is ready to run.`
</output>
```

Patches go back to Thread 3, then the lint and Release Review run again on the reissued Golden Run Sheet.

---

## Improving this playbook

When a prompt gave you something you had to fix by hand, fix the prompt, not just the output.

1. Grade the prompt with reference/Prompt-Grader.md in a new chat, and write the purpose line.
2. Rerun the revised prompt on the same input that went wrong. Keep it only if that output is now right and nothing else got worse.
3. Raise the playbook version and add a change log line: what changed, why, and the input you tested on.

## Change Log

| Version | Date | Change | Why |
|:---|:---|:---|:---|
| 0.4 | 2026-11-14 | Written to Prompt Evaluation Rubric v3.2: Experiment Brief Standard and Brief Lint added; four-way sort of specifics; R0 reviews against the person's own messages, not the transcript; each artifact fixed in the thread that built it; Design Decision Record handed to a new run sheet thread; person's review and Brief Change added as the Agile cycle; "Improving this playbook" added; filled examples removed from prompts. | Rubric v3.2 |

---

## How to try it on the course kit (about 75 to 90 minutes)

1. Thread 1: paste the Discovery Interview prompt, then talk about the kit's project the way you'd tell a colleague. Attach project_brief.txt, tool_limits.csv and past_reports.txt when it asks. Mention chamber A in passing once, and the old 8-wafer DOE, to see whether the sort catches them as Examples.
2. R0: copy your own messages, number them, run the Brief Lint, then the Brief Review. Patch and confirm in Thread 1.
3. Thread 2: Design Decision Menu. R1: review it. Back in Thread 2: patches and selections, then the Design Decision Record.
4. Thread 3: Run Sheet. R2: lint, then Design Review. Patch in Thread 3.
5. Your review: walk the run sheet. Try one Brief Change on purpose (for example, add a response you forgot) to see the cycle restart.
6. Thread 3: risk, select, Golden Run Sheet. R4: lint, then Release Review.
7. Note where it helped, where it was slow, and where you overrode it. Those notes shape the in-class walkthrough and the Analyze and Qualify playbooks.
