# Prompt Evaluation Rubric

**v3.2 (2026-11-14).** Applies to every saved workflow prompt, any task type. Evidence, sources and change log: Prompt-Evaluation-Rubric-Evidence.md. Grading prompt: Prompt-Grader.md.

Score each criterion 1 to 3. A criterion with nothing to act on scores 3 if the prompt states that case and how to handle it.

<!-- markdownlint-disable MD013 -->
| Criterion | 1 — Legacy | 2 — Developing | 3 — Standard |
| --- | --- | --- | --- |
| 1. Context | Vague, or includes material the task doesn't use. | Right material, but not delimited, or long material follows the goal with no restatement. | Only material the task uses, each piece labeled and delimited. Long material first; goal and output after. |
| 2. Goal | Scripts the model's reasoning ("think step by step"). | Goal mixed with procedure the task doesn't need. | States the goal and success criteria. Steps only where their order is part of the result or a person takes part. |
| 3. Limits | Vague bans ("don't be wordy") or no limits. | Basic limits; edge cases open. | Positive, specific limits. A named label or action for each kind of uncertainty. Claims cite sources when sources exist. |
| 4. Output | Open, or described casually. | General form only ("use a table"). | Parts in order, each part's form and limits, any labels or IDs. Working before the final block. JSON only for programs. |
| 5. Signal | Filler, personas, threats, tips. | Some padding. | Every sentence serves context, goal, limits or output. Definitions needed to stand alone stay. |
| 6. Inputs and handoffs | Demands a specification from the person, or takes a raw chat or summary. | Treats every detail from a person as binding, or the next step can't check the output. | States how each input is treated. A person's free talk fills a stated rubric: named dimensions, each rated Clear, Fuzzy or Unknown against written definitions, with an exit rule; anything unresolved becomes an open item. Specifics are sorted as binding, example, background or guess; examples restated generally. The handoff translates what the person wants into a finite, testable artifact built to a named standard for its type (requirements: INCOSE rules, EARS syntax); it is a translation, never a summary; it lists open items and is confirmed by the person. A rubric encoding that standard checks it: a lint for mechanical rules, an anchored review for judgment. The next prompt takes only the artifact, in a new thread. |
<!-- markdownlint-enable MD013 -->

## Rules

- Name no particular system, product, site, vendor or person; specifics arrive as inputs.
- Remove unwanted details from the input instead of telling the model to ignore them.
- A ban naming one exact item ("never write TBD") is allowed.
- Show formats with empty templates, not filled examples.
- State artifacts directly, without process references ("from Stage 4").
- Review in a new thread, with the output, the artifact it came from, and the person's words only.
- Fix a thread's own artifact in that thread; hand on only the fixed artifact.
- Follow the Agile cycle: build from the artifact, the person reviews the result, new or changed requirements go into the artifact as a versioned patch with a change-log line, and the next cycle starts a new thread from the revised artifact.
- Before saving a changed prompt, rerun it on the same input.
