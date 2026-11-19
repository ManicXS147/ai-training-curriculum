# Systems Engineering Playbook (v2)

Do these procedures in sequence to make a verified Systems Requirements Specification (`Golden_SyRS_v1.1.md`) and a Verification Cross-Reference Matrix (`Golden_VCRM_v1.1.md`):

- **Stage 0 (Discovery):** Define the operational problem and produce a
  stakeholder-confirmed Discovery Brief.
- **Stage 1 (Architecture):** Define system boundaries and record architecture
  decisions.
- **Stage 2 (Requirements):** Compile and review the baseline requirements.
- **Stage 3 (Risk):** Analyze failure modes and prepare decisions for
  specification updates.
- **Stage 4 (Baseline and Release):** Consolidate approved updates and verify
  release readiness.

Stages are work phases. Reviews check phase outputs, decision menus capture
user choices, and interview rounds are question-and-answer exchanges within
Stage 0.

---

## Thread Map

Work and review never share a thread. The model that wrote an output does not
grade it in the same context.

| Thread | Purpose | What to paste or attach |
|:---|:---|:---|
| Thread 1 (work) | Stage 0 interview and Discovery Brief | Nothing; start here |
| Review thread R0 (fresh) | Discovery Brief Review | Review Gate block, full Thread 1 transcript, Discovery Brief |
| Thread 2 (work) | Stages 1, 2, 3, and 4 | Sanitized Discovery Brief |
| Review thread R1 (fresh) | Architecture Review | Review Gate block, Sanitized Discovery Brief, Stage 1 output |
| Review thread R2 (fresh) | Mechanical Lint, then Requirements Review | Review Gate block, Sanitized Discovery Brief, Stage 1 selections, `SyRS v1.0`, `VCRM v1.0` |
| Review thread R4 (fresh) | Mechanical Lint, then Release Review | Review Gate block, Sanitized Discovery Brief, both Golden documents |

After each review, paste its patch block back into the work thread before you
run the next stage.

---

## Audit Limits and Rules

### 1. Review Gate (paste this block into every review thread)

```xml
<review_gate>
Rate every finding on two anchored scales. Use the anchor text, not intuition.

Impact (I):
- 1 Cosmetic: wording or formatting only; meaning is unchanged.
- 2 Local: one row is weaker than it should be; nothing else depends on it.
- 3 Propagating: the meaning of one row is wrong or unclear, and another row,
  a VCRM criterion, or a CFG key depends on it.
- 4 Structural: an interface, a state, a decision, or several rows are affected.
- 5 Baseline-breaking: scope is wrong, a stakeholder constraint or safety
  limit is missing or contradicted, or an item has no source.

Ambiguity (A):
- 0 Two independent testers would write the same test.
- 1 Two testers would write the same test with small differences in setup.
- 2 Two testers could write different tests, or no test can be written.

Gate:
- Patch when I >= 4 (any A).
- Patch when I = 3 and A = 2.
- Keep in every other case and record the finding in the scorecard only.

Always Keep: stylistic variation, mathematical limits ("at or below",
"at or above"), and uniform interface or ID lists that share one identical
verification test.

Mechanical defects (table shape, placeholders, shall count, listed purpose
phrases, ID closure, audit tags) are found by the Mechanical Lint and are
always patched. Do not score them and do not re-check them by reading.
</review_gate>
```

### 2. Risk Gate (used in Stage 3)

$$\text{RPN} = \text{Severity } (S) \times \text{Plausibility } (P) \times \text{Spec Gap } (G)$$

| Scale | Value | Anchor |
|:---|:---|:---|
| S | 1 | No user-visible effect |
| S | 2 | Inconvenience; the user recovers without help |
| S | 3 | Wrong or missing output that is caught before anyone uses it |
| S | 4 | Wrong output is used in a decision, or data loss that can be recovered |
| S | 5 | Safety or privacy harm, unauthorized write, or unrecoverable data loss |
| P | 1 | Needs several independent faults at once |
| P | 2 | Rare edge condition |
| P | 3 | Expected occasionally in normal operation |
| P | 4 | Expected regularly in normal operation |
| P | 5 | Expected in nearly every run unless mitigated |
| G | 0 | A `SYS-REQ-*` prevents or detects the failure and its `VCRM-*` criterion exercises it |
| G | 0.5 | A `SYS-REQ-*` covers the failure only in part, or no `VCRM-*` criterion exercises it |
| G | 1 | No `SYS-REQ-*` addresses the failure |

- **Tier 1 (Specification Update Required):** `RPN >= 12`, or `S = 5` with
  `G >= 0.5`. Create atomic `SYS-REQ-*`, `CFG_*`, and `VCRM-*` delta rows and
  add policy options to the Risk Decision Menu.
- **Tier 2 (No Update):** Record the risk in the risk table only.

### 3. Identifier and Traceability Rules

| ID family | Meaning | Created in |
|:---|:---|:---|
| `DB-<section>.<n>` | One stakeholder-stated item in the Discovery Brief | Stage 0 |
| `OPEN-<n>` | One unresolved item (`[OPEN RECONNAISSANCE / ARCHITECTURE TRADE ITEM]`) | Stage 0 onward |
| `ADM-<category><option>` | One selected architecture option, for example `ADM-1B` | Stage 2 |
| `RDM-<category><option>` | One selected risk policy option, for example `RDM-2A` | Stage 4 |
| `ASM-<n>` | One value or behavior the model chose without a stakeholder statement | Stage 2 onward |

- Every `SYS-REQ-*` cites at least one `DB-*`, `ADM-*`, `RDM-*`, or `ASM-*` ID
  in its `Source` column.
- Every `DB-*` item is covered by at least one `SYS-REQ-*`, or is listed as a
  non-goal.
- Every `OPEN-*` item ends in exactly one disposition: resolved by a menu
  selection, converted to an `ASM-*` assumption, or carried forward in the
  Open Items Register. No open item disappears.

### 4. Unknowns Rule

- Never write `TBD` and never invent a value silently.
- When a requirement needs a value that the stakeholder did not state, choose
  a working value, put it behind a `CFG_*` key, mark its provenance `Assumed`,
  and add an `ASM-*` row.
- When no working value can responsibly be chosen, keep the item in the Open
  Items Register and write no requirement that depends on it.

### 5. Output Rules

- Output only failed rows during reviews. Omit passing sections and rows.
- Write normative statements and rationales without audit notes (*"Updated per Requirements Review"*, *"R18 split"*, *"FM-01"*).

---

## Stage 0 — Discovery Interview (Thread 1)

**Condition:** Use this prompt when the operational problem is known, but the scope, limits, and boundaries are undefined.

```xml
<goal>
Conduct a 2-to-5-round discovery interview with the user to define the operational problem and produce a structured, user-confirmed Discovery Brief.
</goal>

<dimensions>
1. Trigger, workflow, stakeholders, and decision-makers.
2. Data sources and coupling scope.
3. Target deliverables and user workflow.
4. Error impact and boundaries between deterministic logic and heuristic/AI inference.
5. Operating environment, release phases, scale, safety, and compute limits.
6. Success criteria and non-goals (how the user will judge the result, and what is explicitly out of scope).
</dimensions>

<coupling_scope_definitions>
Classify every sample file, note, or named system as exactly one of:
- Illustrative: shows the kind of data only. Nothing in it constrains the design.
- External interface (EXT-*): a fixed outside system that the new system must exchange data with. Its format is a constraint at the boundary only.
- Binding: its actual structure and content are in scope. The new system must handle exactly this.
</coupling_scope_definitions>

<status_definitions>
- Clear: the user gave an explicit answer, and no second reasonable reading of it would change the system boundary or a decision.
- Fuzzy: the user answered, but the answer is vague, conflicts with an earlier answer, or allows two readings that lead to different designs.
- Unknown: not yet discussed, or the user said they do not know.
</status_definitions>

<constraints>
- Begin each interview round with a summary of known facts and a status list of the 6 dimensions rated as `Clear`, `Fuzzy`, or `Unknown` per the status definitions.
- Ask a maximum of 3 questions per round with concrete A/B/C options. Add a final option to every question: "D: None of these, or I don't know."
- Write options that are distinct outcomes. Do not make one option obviously preferred.
- Ask for sample files or notes by round 2 and classify their coupling scope. Confirm each classification with the user.
- Use plain language without systems-engineering terminology in questions.
- Record only what the user stated or confirmed. Record every inference of your own and every unknown technical detail as `[OPEN RECONNAISSANCE / ARCHITECTURE TRADE ITEM]`.
- Replace proper nouns, table names, and column identifiers from Illustrative samples with generic terms. Keep the names of External interface and Binding items.
- Describe functional needs without unapproved software libraries or schemas.
- After round 5, stop asking. Convert every dimension that is still `Fuzzy` or `Unknown` into one or more `OPEN-*` items that state exactly what is unresolved, then emit the Draft Discovery Brief.
</constraints>

<output_schema>
### Active Interview Round (While any dimension is Fuzzy or Unknown, up to round 5)
1. **Summary:** 2-to-3 sentences of captured context.
2. **Dimension Status:** Numbered list (1–6) marked `Clear`, `Fuzzy`, or `Unknown`.
3. **Questions:** 1 to 3 plain-language questions with A/B/C/D options.

### Draft Output (When all 6 dimensions are Clear, or after round 5)
Emit the **Draft Discovery Brief** with these exact Markdown sections. Write every item as its own bullet with an ID: `DB-<section>.<n>` in sections 1–6 and `OPEN-<n>` in section 7.
- `## 1. Trigger, Workflow, and Stakeholders`
- `## 2. Data Reality and Coupling Scope`
- `## 3. Target Deliverables and User Experience`
- `## 4. Error Impact and Determinism Boundaries`
- `## 5. Operating Environment, Scale, and Limits`
- `## 6. Success Criteria and Non-Goals`
- `## 7. Open Reconnaissance and Architecture Trade Items`

Then ask: "Reply `Confirmed`, or list the item IDs to correct."

### Final Output (After the user replies)
Apply the corrections and emit the **Discovery Brief** with the same sections and stable IDs.
</output_schema>
```

---

## Discovery Brief Review — Handoff Audit (Fresh Review Thread R0)

**Condition:** Use this prompt after the user confirms the Discovery Brief. Start a fresh thread and paste the full Thread 1 transcript and the Discovery Brief.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
[PASTE FULL THREAD 1 TRANSCRIPT]
[PASTE DISCOVERY BRIEF]
Audit the Discovery Brief against the transcript.
</context>

<goal>
Rate each finding with the Review Gate. Correct only findings the gate marks Patch and emit a clean Discovery Brief for Thread 2.
</goal>

<constraints>
- Verify Fidelity: Every `DB-*` item is something the user stated or confirmed in the transcript. Move unsupported items to section 7 as `OPEN-*` items.
- Verify Completeness: Every stakeholder, constraint, success criterion, non-goal, and open item in the transcript appears in the brief.
- Verify Coupling Hygiene: Replace Illustrative proper nouns or identifiers with generic terms. Label fixed external systems as `EXT-*`. Confirm each sample has exactly one coupling scope.
- Verify Solution Neutrality: Remove libraries, storage engines, and data formats that the user did not mandate.
- Verify Determinism Boundary: Deterministic rules are separated from heuristic inference.
- Keep all item IDs stable. Give new items the next unused ID.
- Omit audit commentary from the sanitized brief.
</constraints>

<output_schema>
1. **Review Scorecard Table:**
   | Principle | Observation | I (1-5) | A (0-2) | Gate (Patch / Keep) |
   |:---|:---|:---|:---|:---|
2. **Sanitized Discovery Brief:** Provide a single fenced `markdown` code block containing sections `## 1` through `## 7`.
</output_schema>
```

---

## Stage 1 — System Boundary and Architecture Decision Menu (Fresh Thread 2)

**Condition:** Start a new thread and attach the Sanitized Discovery Brief from the Discovery Brief Review.

```xml
<context>
[PASTE OR ATTACH SANITIZED DISCOVERY BRIEF FROM DISCOVERY BRIEF REVIEW]
</context>

<goal>
Establish the system architecture boundaries and create the Architecture Decision Menu from the Discovery Brief.
</goal>

<constraints>
- Scope Limit: Define system boundaries and trade-offs only. Reserve normative
  requirements (`SYS-REQ-*`), schemas, and code for Stage 2.
- Keep illustrative examples generic.
- Cite the `DB-*` or `OPEN-*` IDs that each interface, capability, and menu category comes from.
- Present all policy decisions in the Architecture Decision Menu.
- Give every `OPEN-*` item exactly one disposition: a menu category, or a row in the Open Item Disposition Table. Leave no `OPEN-*` item unlisted.
- Format table cells without raw pipe characters (`|`).
- Stop after the Selection Prompt and request the user's option selections (for example: `1B, 2A, 3A`).
</constraints>

<output_schema>
1. `## 1. External Interface Table (IF-01 to IF-0N)`
   | Interface ID | External Entity (EXT-*) | Direction | Payload Summary | Trust & Control Boundary | Source (DB-* / OPEN-*) |
   |:---|:---|:---|:---|:---|:---|
2. `## 2. Deterministic vs. Heuristic Split Table`
   | Core Capability | Execution Mode (Deterministic / Heuristic) | Verification, Refusal, or Human-Override Control | Source (DB-* / OPEN-*) |
   |:---|:---|:---|:---|
3. `## 3. Architecture Decision Menu (Max 5 Categories)`
   For each category (`### Category 1` to `### Category N`):
   - **Open Items Addressed:** `OPEN-*` and `DB-*` IDs from the Discovery Brief.
   - **Options Table:** `| Option (A/B/C) | Architecture Summary | Pros | Cons | Failure Impact |`
   - **Recommended Default:** Explicit selection and rationale.
4. `## 4. Open Item Disposition Table`
   One row for every `OPEN-*` item that is not addressed by a menu category.
   | Open Item (OPEN-*) | Proposed Disposition (Assume / Carry Forward) | Proposed Working Assumption or Reason to Defer |
   |:---|:---|:---|
5. `## 5. Selection Prompt`
   Request shorthand selections from the user, and ask the user to accept or change each proposed disposition.
</output_schema>
```

---

## Architecture Review — Trade Study Audit (Fresh Review Thread R1)

**Condition:** Use this prompt after Stage 1, before you send the architecture selections. Start a fresh thread and paste the Sanitized Discovery Brief and the Stage 1 output.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
[PASTE SANITIZED DISCOVERY BRIEF]
[PASTE STAGE 1 OUTPUT]
Audit the Stage 1 output against the Discovery Brief.
</context>

<goal>
Rate each finding on the Stage 1 architecture tables and Architecture Decision Menu with the Review Gate. Output replacement blocks only for findings the gate marks Patch.
</goal>

<constraints>
- Check that no Illustrative sample identifiers appear in the core system scope.
- Check coverage in both directions: every actor, `EXT-*` boundary, safety limit, success criterion, and non-goal in the Discovery Brief appears in Stage 1, and every Stage 1 row cites a `DB-*` or `OPEN-*` ID that supports it.
- Check that every `OPEN-*` item has exactly one disposition (menu category or disposition table row).
- Check that each heuristic capability has a deterministic verification,
  refusal, or override control.
- Check that the architecture options represent distinct engineering alternatives, that no option violates a `DB-*` constraint or non-goal, and that all policy decisions appear in the menu.
- Emit replacement rows or categories only for Patch findings. Omit passing sections and tables.
</constraints>

<output_schema>
1. **Review Scorecard Table:**
   | Check ID | Observation | I (1-5) | A (0-2) | Gate (Patch / Keep) |
   |:---|:---|:---|:---|:---|
2. **Surgical Replacements (Conditional):**
   - If any finding is Patch: Output only the corrected Markdown rows or trade categories.
   - If no finding is Patch: Output the exact sentence: `Architecture Review passed and is ready for shorthand selection.`
</output_schema>
```

---

## Stage 2 — Architecture Selection and Baseline `SyRS v1.0` Compilation (Thread 2)

**Condition:** Use this prompt after Architecture Review. Paste any Architecture Review patches, then enter your architecture choices in the `<context>` block.

```xml
<context>
Architecture Selections: [INSERT SHORTHAND, e.g., 1B, 2A, 3A, 4B, 5B + notes]
Open Item Dispositions: [INSERT, e.g., "accept all" or "OPEN-4 carry forward, OPEN-6 assume <value>"]
Architecture Review Patches: [PASTE PATCH BLOCK OR "none"]
Source Data: Stage 1 Architecture, the patches above, and the Sanitized Discovery Brief in this thread.
Standards: ISO/IEC/IEEE 29148 and INCOSE GtWR v4.
</context>

<goal>
Compile the complete Baseline Systems Requirements Specification (`SyRS v1.0`) and Verification Cross-Reference Matrix (`VCRM v1.0`).
</goal>

<constraints>
- **Law 1 (INCOSE R18 Single Action):** Write exactly one `"shall <verb>"` and one verifiable condition per requirement row. Place separate actions or fault transitions into atomic `-A`, `-B`, `-C` rows. Two actions joined under one `shall` ("shall log and reject") count as two actions.
- **Law 2 (INCOSE R20 Purpose Placement):** Put all purpose explanations (such as `"to ensure"`, `"to prevent"`, `"in order to"`, `"so that"`) in the `Rationale` column. Keep the `Normative Statement` column free of purpose clauses.
- **Law 3 (State and Pattern Grounding):** Assign each requirement to `"All Operational States"` or one exact `STATE-*` identifier from Section 1. Ensure the state model has entry triggers, permitted operations, and exit transitions for every state. Write each normative statement in exactly one EARS pattern and name it in the `EARS Pattern` column:
  - Ubiquitous: `The <system> shall <response>.` (state is `All Operational States`)
  - State-driven: `While <STATE-*>, the <system> shall <response>.`
  - Event-driven: `When <trigger>, the <system> shall <response>.`
  - Unwanted-behavior: `If <fault condition>, then the <system> shall <response>.`
  - Optional-feature: `Where <feature is included>, the <system> shall <response>.`
  - Complex: `While <STATE-*>, when <trigger>, the <system> shall <response>.`
- **Law 4 (Parameterization and Provenance):** Replace hardcoded tunable numbers, timeouts, weights, and patterns in normative statements with `CFG_*` keys defined in Section 3. Mark each key's provenance as `Stated` (the default comes from a `DB-*` or `ADM-*` item) or `Assumed` (you chose it; add an `ASM-*` row in Section 4).
- **Law 5 (Solution Neutrality):** Specify externally observable behavior in the `Normative Statement` column. Place internal software library names in the `Rationale` column unless required by an external interface (`IF-*`).
- **Law 6 (Table Hygiene and Traceability):** Write complete values for all cells and exclude raw pipe characters (`|`) inside cells. Follow the Unknowns Rule: never write `"TBD"`, never invent a value silently; use an `ASM-*` row or an `OPEN-*` row. Map every `SYS-REQ-*` 1-to-1 to a `VCRM-*` row. Cite at least one `DB-*`, `ADM-*`, or `ASM-*` ID in every `Source` cell. Cover every `DB-*` item in sections 1–5 and every success criterion in section 6 with at least one `SYS-REQ-*`. Write no requirement that implements a non-goal.
</constraints>

<output_schema>
## Section 1 — External Interfaces (IF-*) and Formal State Model (STATE-*)
### 1.1 External Interfaces
| Interface ID | External System (EXT-*) | Direction | Data Contract | Failure Handling |
|:---|:---|:---|:---|:---|

### 1.2 Formal State Model
| State ID (STATE-*) | Entry Trigger | Permitted Operations | Exit Transitions & Target States |
|:---|:---|:---|:---|

## Section 2 — Normative Requirements Table (SYS-REQ-*)
| Req ID | EARS Pattern | System State | Normative Statement | Rationale | Source |
|:---|:---|:---|:---|:---|:---|

## Section 3 — Attachment B: Configuration Registry (CFG_*)
| Config Key (CFG_*) | Data Type | Default Value | Valid Range | Governing Req ID | Provenance (Stated / Assumed) | Purpose |
|:---|:---|:---|:---|:---|:---|:---|

## Section 4 — Assumptions Register (ASM-*)
| ASM ID | Assumption | Affected IDs (SYS-REQ-* / CFG_*) | Consequence if Wrong | Sign-Off (Pending / Confirmed) |
|:---|:---|:---|:---|:---|

## Section 5 — Open Items Register (OPEN-*)
| Open Item (OPEN-*) | Description | Disposition (Resolved by ADM-* / Converted to ASM-* / Carried Forward) | What Is Needed to Close |
|:---|:---|:---|:---|

## Section 6 — Verification Cross-Reference Matrix (VCRM-*)
| VCRM ID | Req ID | Verification Method (T/I/A/D) | Verification Stage | Deterministic Pass/Fail Criterion |
|:---|:---|:---|:---|:---|
</output_schema>
```

---

## Mechanical Lint (Fresh Review Threads R2 and R4)

**Condition:** Run this before the Requirements Review and before the Release Review. Use a model with a code execution tool, or run an equivalent script yourself and paste its output. A model that only reads the tables is not a valid lint.

```xml
<context>
[ATTACH THE SyRS AND VCRM DOCUMENTS AND THE SANITIZED DISCOVERY BRIEF AS FILES]
</context>

<goal>
Write and run a script that parses the Markdown tables and reports every violation of checks L1–L12. Report only what the script prints.
</goal>

<checks>
- L1 Table shape: every table row has the same number of cells as its header row.
- L2 Placeholders: no cell is empty or contains `TBD`, `TBA`, `...`, `omitted`, or `unchanged`.
- L3 Shall count: every `Normative Statement` cell contains the word `shall` exactly once.
- L4 Purpose phrases: no `Normative Statement` cell contains `in order to`, `so that`, `to ensure`, `to prevent`, `to allow`, `to enable`, or `to avoid`.
- L5 State grounding: every `System State` cell is `All Operational States` or exactly one `STATE-*` ID defined in Section 1.2.
- L6 VCRM closure: every `SYS-REQ-*` has exactly one `VCRM-*` row, and every `VCRM-*` row names one existing `SYS-REQ-*`.
- L7 CFG closure: every `CFG_*` key used in a normative statement is defined in the registry; every registry key names an existing governing `SYS-REQ-*` and is used in at least one normative statement.
- L8 Interface and state closure: every `IF-*` and `STATE-*` ID used anywhere is defined in Section 1; every exit transition targets a defined state.
- L9 Source closure: every `Source` cell cites at least one ID; every cited `DB-*`, `ASM-*`, and `OPEN-*` ID exists; every `DB-*` item in brief sections 1–5 and every success criterion is cited by at least one `SYS-REQ-*`; every `Assumed` registry key has an `ASM-*` row.
- L10 Audit tags: no `Normative Statement` or `Rationale` cell contains `FM-<digits>`, `R18`, `R20`, `Updated`, `split`, or `per review`.
- L11 Literal numbers (warning only): list every `Normative Statement` cell that contains a digit outside an ID or `CFG_*` key.
- L12 Counts: print total counts of `IF-*`, `STATE-*`, `SYS-REQ-*`, `CFG_*`, `VCRM-*`, `ASM-*` (and how many are Pending), and `OPEN-*` (and how many are Carried Forward).
</checks>

<output_schema>
1. **Lint Report:** `| Check | Row / ID | Violation |` with one row per violation, or the sentence `Lint passed: zero violations in L1–L10.`
2. **L11 Warnings:** list of row IDs, or `none`.
3. **L12 Counts:** one line per ID family.
4. The script source in one fenced code block.
</output_schema>
```

Every L1–L10 violation is a required patch. Paste the Lint Report into the work thread with the instruction `Emit corrected rows for these lint violations only`, then re-run the lint until it passes.

---

## Requirements Review — Surgical Audit (Fresh Review Thread R2)

**Condition:** Use this prompt in the same review thread after the Mechanical Lint passes on `SyRS v1.0`.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
[PASTE SANITIZED DISCOVERY BRIEF, STAGE 1 SELECTIONS, `SyRS v1.0`, AND `VCRM v1.0` IF NOT ALREADY IN THIS THREAD]
The Mechanical Lint has passed. Do not re-check L1–L10. Audit what a script cannot judge.
</context>

<goal>
Audit `SyRS v1.0` and `VCRM v1.0` for content correctness against the Discovery Brief and for judgment-level compliance with the 6 Specification Laws. Rate each finding with the Review Gate and emit surgical replacement rows only for Patch findings.
</goal>

<constraints>
- **Content Check 1 (Fidelity):** For each `SYS-REQ-*`, read the items in its `Source` cell. Flag a requirement that contradicts, strengthens, or weakens its source.
- **Content Check 2 (Necessity):** Flag a requirement whose only source is an `ASM-*` ID and that adds a capability the brief did not ask for. Flag any requirement that implements a non-goal.
- **Content Check 3 (Sufficiency):** For each `DB-*` item and success criterion, judge whether the citing requirements, taken together, satisfy it. Flag items that are cited but not actually satisfied.
- **Content Check 4 (Verification Quality):** Flag any `VCRM-*` criterion that would pass a system that does not meet its requirement, or that two testers would run differently.
- **Law 1 Check (R18):** Flag rows with multiple actions under one `shall` or with distinct triggers. Keep mathematical limits and uniform ID lists that share an identical verification test.
- **Law 2 Check (R20):** Flag purpose clauses the lint list did not catch (`"to <verb>"` used as a purpose, `"for the purpose of"`, `"thereby"`).
- **Law 3 Check:** Flag statements whose wording does not match the named EARS pattern, and state-driven or complex statements whose `While` state differs from the `System State` cell.
- **Law 4 Check:** Review the L11 warnings. Flag tunable values that belong in `CFG_*`. Flag `Stated` provenance that the cited source does not support.
- **Law 5 Check:** Flag sample proper nouns, internal library names, or design decisions in the `Normative Statement` column.
- Output only the scorecard, the coverage exceptions, and corrected rows for Patch findings. Omit passing rows and audit tags from replacement cells.
</constraints>

<output_schema>
1. **Compliance Ledger:**
   | Row / ID | Check (Content 1-4 / Law 1-5) | Observation | I (1-5) | A (0-2) | Gate (Patch / Keep) |
   |:---|:---|:---|:---|:---|:---|
2. **Coverage Exceptions:**
   | Brief Item (DB-*) | Citing Req IDs | Gap |
   |:---|:---|:---|
   List only items that are unsatisfied or only partly satisfied. If none, write `All brief items are satisfied.`
3. **Surgical Patch Block (Conditional):**
   - If no finding is Patch: Output `SyRS v1.0 passed Requirements Review and is ready for Stage 3.`
   - If any finding is Patch: Output replacement tables containing only the corrected, split, or added `SYS-REQ-*`, `CFG_*`, `ASM-*`, and `VCRM-*` rows.
</output_schema>
```

---

## Stage 3 — FMEA Risk Review and Risk Decision Menu (Thread 2)

**Condition:** Use this prompt after Requirements Review approves `SyRS v1.0`. Paste the Requirements Review patch block into Thread 2 first.

```xml
<context>
Requirements Review Patches: [PASTE PATCH BLOCK OR "none"]
Evaluate `SyRS v1.0` with the patches above applied.
</context>

<goal>
Analyze failure modes across 5 reliability areas, calculate the Risk Priority Number (RPN), and generate atomic specification delta rows and a Risk Decision Menu for Tier 1 risks.
</goal>

<reliability_lenses>
1. Epistemic and Data Integrity (stale data, dropped payloads, unverified schema drift).
2. State-Space Continuity (mid-process timeouts, partial aborts, deadlocks).
3. Resource and Scale Limits (combinatorial growth, memory or replica exhaustion).
4. Interface and Human Input Errors (malformed payloads, conflicting manual edits).
5. Safety, Privacy, and Hard Invariants (unauthorized writes, sensitive data exposure).
</reliability_lenses>

<risk_gate>
RPN = Severity (S: 1–5) * Plausibility (P: 1–5) * Spec Gap (G: 0, 0.5, or 1).
S anchors: 1 no user-visible effect; 2 inconvenience, user recovers alone; 3 wrong or missing output caught before use; 4 wrong output used in a decision, or recoverable data loss; 5 safety or privacy harm, unauthorized write, or unrecoverable data loss.
P anchors: 1 needs several independent faults; 2 rare edge condition; 3 occasional in normal operation; 4 regular in normal operation; 5 nearly every run unless mitigated.
G anchors: 0 a SYS-REQ prevents or detects it and its VCRM criterion exercises it; 0.5 a SYS-REQ covers it in part, or no VCRM criterion exercises it; 1 no SYS-REQ addresses it.
Tier 1: RPN >= 12, or S = 5 with G >= 0.5. Tier 2: everything else.
</risk_gate>

<constraints>
- Identify failure modes under every lens. Score the 5 to 8 with the highest expected RPN in the ledger. List every other identified failure mode in the Unscored Failure Modes list with one line each.
- Name the `SYS-REQ-*` rows that justify any `G` value below 1.
- Give at least one scored failure mode to every `ASM-*` assumption whose "Consequence if Wrong" is severe.
- **Tier 1:** Write atomic `SYS-REQ-*`, `CFG_*`, `ASM-*`, and `VCRM-*` delta rows that obey all 6 Specification Laws from Stage 2 (one `"shall <verb>"`, zero purpose clauses in normative text, one named EARS pattern, exact `STATE-*` ID, `CFG_*` parameters with provenance, a `Source` cell, zero audit tags).
- **Tier 2:** Record the failure mode in the FMEA Ledger only. Create delta rows only for Tier 1 risks.
- Group policy and threshold choices for Tier 1 deltas into the Risk Decision Menu (maximum 5 categories). List every Tier 1 choice that does not fit in the menu under Defaults Applied Without Menu so the user can override it.
- Stop for user input after section 5.
</constraints>

<output_schema>
## 1. Ranked FMEA Ledger
| FM ID | Lens (1-5) | Failure Summary | Mitigating SYS-REQ IDs | S (1-5) | P (1-5) | G (0/0.5/1) | RPN | Tier (1: Delta / 2: Log Only) |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|

### Unscored Failure Modes
One line each: lens number and failure summary.

## 2. Verified Tier 1 Delta Rows (Tier 1 Only)
- **SYS-REQ Delta Table:** `| Req ID | EARS Pattern | System State | Normative Statement | Rationale | Source |`
- **CFG Delta Table:** `| Config Key (CFG_*) | Data Type | Default Value | Valid Range | Governing Req ID | Provenance (Stated / Assumed) | Purpose |`
- **ASM Delta Table:** `| ASM ID | Assumption | Affected IDs (SYS-REQ-* / CFG_*) | Consequence if Wrong | Sign-Off (Pending / Confirmed) |`
- **VCRM Delta Table:** `| VCRM ID | Req ID | Verification Method (T/I/A/D) | Verification Stage | Deterministic Pass/Fail Criterion |`

## 3. Risk Decision Menu (Max 5 Categories)
For each category (`### Category 1` to `### Category N`):
- **Governing FM ID & Req IDs:** Reference list.
- **Options Table:** `| Option (A/B/C) | Policy & Threshold Setting | Operational Trade-Off |`
- **Recommended Default:** Explicit selection.

## 4. Defaults Applied Without Menu
| Governing FM ID & Req IDs | Default Applied | How to Override |
|:---|:---|:---|

## 5. Assumptions for Sign-Off
Every `ASM-*` row from `SyRS v1.0` and the delta table with status `Pending`, in one table. Ask the user to confirm, correct, or leave each one pending.
</output_schema>
```

---

## Stage 4 — Risk Decision Selection and Golden Baseline Consolidation (Thread 2)

**Condition:** Use this prompt to reply to the Risk Decision Menu from Stage 3.

```xml
<context>
Risk Decisions: [INSERT SHORTHAND, e.g., 1B, 2A, 3A + modifications]
Default Overrides: [INSERT OR "none"]
Assumption Sign-Off: [INSERT, e.g., "ASM-01 confirmed; ASM-03 change default to <value>; others remain Pending"]
Source Materials: `SyRS v1.0`, Requirements Review patches, and Stage 3 Tier 1 deltas configured with the selections above.
</context>

<goal>
Consolidate all baseline items and verified updates into two complete standalone Markdown documents: `Golden_SyRS_v1.1.md` and `Golden_VCRM_v1.1.md`.
</goal>

<constraints>
- **Complete Output:** Write every section and table row in full. Never truncate rows or write `"unchanged"`, `"..."`, or `"omitted"`. If the output limit is near, stop at the end of a complete table row and write `CONTINUE FROM <next ID>`; resume from that ID when the user replies `continue`.
- **Clean-Room Text:** Exclude all audit markers, failure mode IDs (`FM-*`), and version notes (`"Updated"`, `"R18 split"`) from normative statements and rationales. Cite risk decisions in the `Source` column as `RDM-*` IDs only.
- **6-Law Compliance:** Ensure every row has one `"shall <verb>"` (R18), zero purpose clauses in normative statements (R20), one named EARS pattern, one valid `STATE-*` reference, complete `CFG_*` links with provenance, a `Source` cell, 1-to-1 `VCRM-*` traceability, and zero raw pipe characters (`|`) inside table cells.
- **Sign-Off Status:** Set each `ASM-*` row to `Confirmed` or `Pending` exactly as the user stated. Change `Provenance` to `Stated` only for keys whose assumptions the user confirmed.
- **Open Items:** Carry every unresolved `OPEN-*` item into Section 5. Drop none.
</constraints>

<output_schema>
### Document 1: `Golden_SyRS_v1.1.md` (Emit inside a single fenced `markdown` code block)
- `# Systems Requirements Specification (Golden_SyRS_v1.1)`
- `## Section 1 — External Interfaces (IF-*) and Formal State Model (STATE-*)`
- `## Section 2 — Normative Requirements Table (SYS-REQ-*)`
- `## Section 3 — Attachment B: Configuration Registry (CFG_*)`
- `## Section 4 — Assumptions Register (ASM-*)`
- `## Section 5 — Open Items Register (OPEN-*)`

### Document 2: `Golden_VCRM_v1.1.md` (Emit inside a second fenced `markdown` code block)
- `# Verification Cross-Reference Matrix (Golden_VCRM_v1.1)`
- `## Section 1 — Verification Traceability Table (VCRM-*)`
</output_schema>
```

---

## Release Review — Final Readiness Check (Fresh Review Thread R4)

**Condition:** Use this prompt after Stage 4 outputs both Golden documents and the Mechanical Lint passes on them. Paste the L12 counts from the lint.

```xml
<review_gate>
[PASTE REVIEW GATE BLOCK]
</review_gate>

<context>
Documents to review:
- `Golden_SyRS_v1.1.md`
- `Golden_VCRM_v1.1.md`
- Sanitized Discovery Brief
Lint Result: [PASTE LINT REPORT AND L12 COUNTS]
The Mechanical Lint has passed. Do not re-check L1–L10 and do not recount items.
</context>

<goal>
Verify release readiness on the checks a script cannot make. Rate each finding with the Review Gate and issue either the Golden Baseline Release Certificate or surgical replacement rows for Patch findings.
</goal>

<constraints>
- Check Consolidation: Confirm every Requirements Review patch, every Tier 1 delta, and every user selection is reflected, and that no superseded row survives beside its replacement.
- Check Syntax Judgment (R18 & R20): Confirm no row hides two actions under one `shall` and no normative statement carries a purpose clause the lint list missed.
- Check Content: Confirm no requirement contradicts its `Source` items, no requirement implements a non-goal, and every success criterion is satisfied by the cited requirements.
- Check Verification Quality: Confirm each `VCRM-*` criterion would fail a system that does not meet its requirement.
- Check Sign-Off Integrity: Confirm no `Assumed` value is presented as `Stated`, and that every carried-forward `OPEN-*` item states what is needed to close it.
- Omit passing rows from the output.
</constraints>

<output_schema>
1. **Release Audit Scorecard:**
   | Check Area | Observation | I (1-5) | A (0-2) | Gate (Pass / Fail) |
   |:---|:---|:---|:---|:---|
2. **Release Decision (Conditional):**
   - If no check fails: Emit the **Golden Baseline Release Certificate**. Copy the counts of `IF-*`, `STATE-*`, `SYS-REQ-*`, `CFG_*`, and `VCRM-*` items from the L12 lint output. State the number of `Pending` assumptions and carried-forward open items, list their IDs, and state: `Released with <n> pending assumptions and <m> open items.`
   - If any check fails: Emit only the corrected replacement rows required for final export.
</output_schema>
```
