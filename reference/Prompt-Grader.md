# Prompt Grader

**v1.0 (2026-11-14).** Grades any saved prompt against the Prompt Evaluation Rubric v3.2 and returns a revised version. Start a new chat, paste the block below, fill in the two brackets, and run it. I graded it against the rubric by hand: 3 on all six criteria. Running it on itself in Copilot Chat is the real test.

```xml
<rubric>
Score each criterion 1 to 3. A criterion with nothing to act on scores 3 if the prompt states that case and how to handle it.

| Criterion | 1 — Legacy | 2 — Developing | 3 — Standard |
| --- | --- | --- | --- |
| 1. Context | Vague, or includes material the task doesn't use. | Right material, but not delimited, or long material follows the goal with no restatement. | Only material the task uses, each piece labeled and delimited. Long material first; goal and output after. |
| 2. Goal | Scripts the model's reasoning ("think step by step"). | Goal mixed with procedure the task doesn't need. | States the goal and success criteria. Steps only where their order is part of the result or a person takes part. |
| 3. Limits | Vague bans ("don't be wordy") or no limits. | Basic limits; edge cases open. | Positive, specific limits. A named label or action for each kind of uncertainty. Claims cite sources when sources exist. |
| 4. Output | Open, or described casually. | General form only ("use a table"). | Parts in order, each part's form and limits, any labels or IDs. Working before the final block. JSON only for programs. |
| 5. Signal | Filler, personas, threats, tips. | Some padding. | Every sentence serves context, goal, limits or output. Definitions needed to stand alone stay. |
| 6. Inputs and handoffs | Demands a specification from the person, or takes a raw chat or summary. | Treats every detail from a person as binding, or the next step can't check the output. | States how each input is treated. A person's free talk fills a stated rubric: named dimensions, each rated Clear, Fuzzy or Unknown against written definitions, with an exit rule; anything unresolved becomes an open item. Specifics are sorted as binding, example, background or guess; examples restated generally. The handoff translates what the person wants into a finite, testable artifact built to a named standard for its type (requirements: INCOSE rules, EARS syntax); it is a translation, never a summary; it lists open items and is confirmed by the person. A rubric encoding that standard checks it: a lint for mechanical rules, an anchored review for judgment. The next prompt takes only the artifact, in a new thread. |

Rules:

- Name no particular system, product, site, vendor or person; specifics arrive as inputs.
- Remove unwanted details from the input instead of telling the model to ignore them.
- A ban naming one exact item ("never write TBD") is allowed.
- Show formats with empty templates, not filled examples.
- State artifacts directly, without process references ("from Stage 4").
- Review in a new thread, with the output, the artifact it came from, and the person's words only.
- Fix a thread's own artifact in that thread; hand on only the fixed artifact.
- Follow the Agile cycle: build from the artifact, the person reviews the result, new or changed requirements go into the artifact as a versioned patch with a change-log line, and the next cycle starts a new thread from the revised artifact.
- Before saving a changed prompt, rerun it on the same input.
</rubric>

<prompt_under_review>
[PASTE THE PROMPT TO GRADE]
</prompt_under_review>

<purpose>
[One line: what the prompt is for and who runs it. Write NOT STATED if unknown.]
</purpose>

<goal>
Grade the prompt under review against every rubric criterion and rule, and write a revised prompt that does the same job and scores 3 on all six criteria. Success: every score below 3 has evidence and a fix, and the revised prompt changes only what the fixes require.
</goal>

<limits>
- Use the rubric cell wording as the anchor for each score.
- Evidence is the exact quoted line, or MISSING plus what is missing.
- When the purpose is NOT STATED and a score depends on it, write ASSUMED and the purpose you assumed.
- Keep the prompt's task, inputs and intended output. Record each change in the change list, outside the revised prompt.
- Revised prompt length: the original length plus only what the fixes add.
</limits>

<output>
1. Scorecard: table with columns Criterion | Score (1-3) | Evidence | Fix; rows 1 to 6, then one row per rule broken.
2. Change list: numbered, one line per change, each naming its criterion or rule.
3. Revised prompt: one fenced code block, ready to paste.
4. Open items: decisions the person must make before saving the revised prompt, or NONE.
5. Retest: one line naming the input to rerun the revised prompt on before saving.
</output>
```
