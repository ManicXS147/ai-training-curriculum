# Prompt Evaluation Rubric: Evidence and Change Log (v2.1 full text)

**Version 2.1 (2026-11-14).** Version 1.0 was Andrew's original (2026-11-14). The change log and sources are at the end.

*This is the full v2.1 rubric with its reasoning, change log and sources. The working rubric is the short version in Prompt-Evaluation-Rubric.md (v3.0); the grading prompt is Prompt-Grader.md.*

*(Standing rule: every workflow prompt must follow this rubric. Workflow prompts are the ones that are saved in a playbook, improved over time, and used by copy and paste, or later in a harness such as SkyChat. The rubric is the tool for creating and updating them. It does not apply to the conversational practice prompts in AI Basics. It's a research-based prompt style.)*

**Any kind of prompt fits:** interview, analysis, generation, drafting, review, transformation. Each criterion grades a property every prompt has (its inputs, its goal, its limits, its output, its wording, its handoffs), never a property of one task type. Examples in the cells are illustrations, not requirements. When a criterion has nothing to act on (a prompt with no source material, or no person's input), it scores 3 if the prompt states that case and what to do in it.

**Tools these prompts run in:** Copilot Chat (GCC High; the underlying model is not disclosed) and Gemini Enterprise. Neither enforces an output format, and either may or may not be a reasoning model on a given day. Every rule below is written to hold when the model is unknown.

**How a workflow prompt meets a person:** people think out loud, not in specifications. So a workflow does not ask the person to talk like a robot. The person rambles; the saved prompt does the refining. Criterion 6 says how.

<!-- markdownlint-disable MD013 -->
| Criterion | 1 — Outdated (Legacy) | 2 — Developing | 3 — Research-Backed Standard |
| --- | --- | --- | --- |
| 1. Context Architecture | Relies on vague background, or includes material the task doesn't use. | Includes the right material, but it isn't separated from the instructions, or long material sits after the instructions with nothing restating the goal. | Supplies everything the task works on and nothing it doesn't, each piece labeled by name and role with delimiters (XML tags or Markdown headers). Long material goes first; the goal and output structure follow it. |
| 2. Goal vs. Process | Scripts how the model should think ("think step by step", "first consider... then..."). | Mixes the end goal with procedure the task doesn't need. | States the end goal and the success criteria the output will be judged by, and leaves the reasoning to the model. Ordered steps appear only where the order is itself part of the result or the person takes part in the steps. |
| 3. Constraints & Boundaries | Uses vague negative rules ("don't be wordy", "don't hallucinate") or leaves limits unstated. | Includes basic length or tone limits, but leaves edge cases ambiguous. | States limits as positive, specific targets. For each kind of uncertainty the task can meet (missing input, unsupported claim, guess, conflict), names the label or action to use. When the prompt has source material, each factual claim points to where it came from. |
| 4. Output Structure | Leaves the output open or describes it casually in prose. | Asks for a general form ("use bullets", "make a table") without specifics. | Fully specifies the output: its parts in order, the form and limits of each part, and any labels or IDs, so two runs can be compared and the output can be checked. The form fits the result (headings, table columns, a fixed paragraph order, a set of questions). Any working comes before the final block, not inside it. JSON only when a program will read the output. |
| 5. Signal-to-Noise Ratio | Bloated with filler, generic personas ("act as a world-class guru"), threats, tips or "magic" words. | Generally clear, with some padding or rules the task doesn't need. | Every sentence serves context, goal, a limit or the output structure. Short is not the target: definitions the prompt needs to stand alone stay in. |
| 6. Inputs and Handoffs | Requires the person to write a specification before the AI will help, or takes a raw conversation or a summary of one as input. | Accepts free-form input from a person, but treats every detail in it as binding; or produces output the next step can't check. | Takes each input in the form it arrives (a person's free talk or answers, files, an upstream artifact) and says how to treat it. Any specific from a person (a named system, number, example, guess) is sorted as binding, example, background or guess, and examples are restated in general terms. When the output feeds another step, it is a handoff artifact in a named, checkable structure suited to its type (for requirements: INCOSE rules and EARS syntax), with open items listed, confirmed by the person; the next prompt takes only that artifact, in a new thread. |
<!-- markdownlint-enable MD013 -->

## Workflow Rules (apply across prompts)

- **Hand off an artifact, not a conversation.** Each stage ends in an artifact (after an interview, the confirmed map of what is clear, fuzzy and unknown). A summary or compaction of the chat is not a handoff artifact, because a summary removes context without checking that the right context is there. The standard does two jobs: it is a checklist that forces every needed element to be covered (unstated items become open items instead of guesses), and a filter that keeps out details the standard has no place for. The artifact follows a named structure whose rules a lint or review can check line by line, chosen for the artifact's type: for requirements, INCOSE rules and EARS patterns such as "When [trigger], the [system] shall [response]"; other artifact types use their own established structure. The next stage starts a new thread with that artifact only, leaving the rambling behind. A refining prompt at the end of the same thread is the right move when the thread's own artifact is what needs fixing, as in the Ingres case; the corrected artifact is then what moves on.
- **Review in a fresh chat.** The chat that produced an output does not grade it. Start a new chat with the output and the artifact it was built from.
- **Reviewers see the person's words, not the AI's.** When a review needs the conversation, paste the person's answers verbatim, not the AI's turns.
- **Remove, don't forbid.** To keep a detail out of the result, take it out of the input where you can. Telling the model to ignore something weakens its pull without removing it. When the detail is woven into a thread you must keep, the refining prompt names it as an example and restates the requirement in general terms.
- **Every saved prompt is first principles.** It names no particular instance (a specific system, product, site, vendor or person) and holds for any case of its kind. Specifics come in through the inputs, sorted by criterion 6.
- **Test a change before saving it.** Rerun the changed prompt on the same input. Small wording changes can flip individual results even when the average looks the same.

## What Not to Include in Modern Prompts

- Fluffy Personas and Flattery: Cut "Act as a world-class expert" and "Take a deep breath and do your best." Expert personas, including ones matched to the field, did not improve accuracy, and threats or tips did not either. To get a domain lens, state the audience and the domain context instead of a role.
- Generic Reasoning Instructions: Don't add "think step by step" or "show your work." On current models it adds little or no accuracy, can make answers less consistent, and adds time, whether or not the model is a reasoning model. Asking for specific checks (for example "for each number, show the calculation") is a success criterion, not this.
- Unneeded Context: Leave out background the task doesn't use: other projects, history, a whole manual when the task needs one section. Material the task works on is not a dump: a full meeting transcript for meeting notes, or a full alarm log for an alarm analysis, belongs in the prompt. Irrelevant material lowers accuracy and can steer answers.
- Vague Negative Constraints: Skip open-ended bans like "don't be wordy," "avoid jargon," or "do not hallucinate." Use positive, specific targets ("limit output to 150 words", "write UNKNOWN when the input doesn't say"). A ban that names one exact thing ("never write TBD") is fine.
- Rigid Step-by-Step Micro-Management: Don't dictate how the model processes information when a clear end goal and checks are enough. The exception is when the person takes part in the steps (an interview, a decision menu): there the steps are the person's.
- Filled-In Examples: Leave out worked examples for straightforward tasks. When a format needs showing, use an empty template. If a filled example is unavoidable, make it clearly fictional and unlike the real case, because models copy example content into their answers.
- Conversational Padding: Remove polite openers, transitional filler, and meta-commentary like "Here is what I need you to do today." Every sentence should carry instruction or context.
- Unnecessary Process Provenance: Omit references such as "from Stage 4" when they add no task-relevant context. State the required artifacts and checks directly.

## Change Log

| Version | Date | Change | Why | Source |
| --- | --- | --- | --- | --- |
| 2.1 | 2026-11-14 | First-principles pass so any prompt type fits: added the "any kind of prompt fits" rule and N/A handling; criterion 3 no longer assumes source documents; criterion 4 renamed Output Structure and no longer assumes Markdown tables; criterion 6 renamed Inputs and Handoffs and covers every input type, not only interviews; standards for handoff artifacts chosen by artifact type; fab- and task-specific words removed from rules. | Andrew 2026-11-14: the rubric grades prompts and must not be fixated on one type of task. | Andrew 2026-11-14 |
| 2.0 | 2026-11-14 | Added criterion 6, Human Input (Ramble to Refined). | Matches Andrew's method: people think out loud, the prompt refines. Underspecified asks get guessed; details mentioned in passing steer decisions even against stated rules; models that ask clarifying questions do better. | Andrew 2026-11-14; Yang 2025; Zheng, Tian and Rizoiu 2026; Wu 2025 |
| 2.0 | 2026-11-14 | Added Workflow Rules, including "refine where the work lives." | Rebuilding the task in a clean context helped when the person's messages held the whole task, but hurt when later turns built on AI-made drafts or results; there, keeping the thread was best. Andrew's Ingres fix (refining prompt at the end of an artifact thread) is that second case. A checker that could see the AI's earlier reasoning did worse than no check. An "ignore this" reminder cut a detail's effect by about a third. Per-question results flip under small changes. | Ho 2026; Laban 2025; Andrew's Ingres case; Zheng, Tian and Rizoiu 2026; Illusion of Robustness 2026 |
| 2.0 | 2026-11-14 | Handoff artifact must follow a named, checkable standard (INCOSE requirement rules, EARS syntax for requirements), not a summary. | Andrew 2026-11-14. Supporting evidence: an LLM that faithfully summarized the conversation did not reproduce the gains of rebuilding a consolidated task specification, even with more compute. INCOSE and EARS are engineering standards, not AI studies; I found no study of EARS or INCOSE rules as AI handoff formats. The checklist role matches the finding that models silently guess requirements nobody stated; the filter role matches the finding that passing details steer decisions. | Andrew 2026-11-14; Ho 2026; Yang 2025; Zheng, Tian and Rizoiu 2026; INCOSE GtWR; Mavin et al. 2009 |
| 2.0 | 2026-11-14 | Criterion 1: "dump" redefined as material the task doesn't use; long material first, goal and template after it; label each piece by name and role. | Andrew's clarification that a full transcript for notes is relevant. Focused inputs beat full inputs padded with irrelevant content. Anthropic reports up to 30% better answers with documents first and the question last; OpenAI says instructions above context beat below, best at both ends, so the goal is stated before and after long material. | Andrew 2026-11-14; Chroma 2025; Anthropic; OpenAI |
| 2.0 | 2026-11-14 | Criterion 2 and "Generic Reasoning Instructions" reworded so they hold when the model is unknown. | Chain-of-thought prompting added little or no accuracy for reasoning models, gave mixed results for others, and added 20% to 600% more time. | Wharton Report 2 |
| 2.0 | 2026-11-14 | Criterion 3: named the labels for missing data, required source-tied claims, and allowed specific bans. | Models guess rather than abstain unless abstaining is allowed. Models handle negation poorly, so vague bans are weak; a ban naming one exact token is unambiguous. Quoting the source first helps the model focus on the relevant content. | OpenAI 2025; Truong 2023; Anthropic |
| 2.0 | 2026-11-14 | Criterion 4 renamed Output Template; "strict schema, exact JSON keys" replaced by a fixed Markdown template, analysis before the formatted block, JSON only for programs. | Strict format requirements reduced reasoning quality; letting the model reason before formatting gained up to 27%. JSON performed poorly for documents in OpenAI's tests. Copilot Chat and Gemini cannot enforce a schema, so the template is a request checked by a lint or review. | Tam 2024; In-Writing 2026; OpenAI |
| 2.0 | 2026-11-14 | Criterion 5 and "Personas": threats and tips added; "unless a specific domain lens is required" replaced with "state the audience and domain context"; density over brevity. | Expert personas, including domain-matched ones, did not improve accuracy. Threats and tips did not either. Too many requirements also hurts, because models follow a limited number of instructions. | Wharton Reports 3 and 4; Yang 2025 |
| 2.0 | 2026-11-14 | "Redundant Few-Shot Examples" became "Filled-In Examples." | Examples steer format strongly, but models copy example content, which defeats first-principles prompts. | Anthropic; Ali et al. 2024 |
| 2.0 | 2026-11-14 | Header: scope, tools and the ramble-to-refined principle stated up front. | Andrew 2026-11-14: prompts should fit how people think instead of forcing them to "talk like a robot." | Andrew 2026-11-14 |
| 1.0 | 2026-11-14 | Original rubric. | | Andrew |

## Not Backed by Research (house style or open)

- **Conversational Padding** and **Unnecessary Process Provenance** are house style. They are sensible and consistent with the context findings, but no study tests them directly.
- **Criterion 6's sorting step** (binding, example, background, guess) is a design built from the studies above and from Andrew's practice. It has not been tested as written in Copilot Chat or Gemini.
- **Same thread versus fresh chat for refining:** the study behind this rule used benchmarks, not artifact work in Copilot or Gemini. Andrew's Ingres result is the most direct evidence for the same-thread case.
- **XML tags versus Markdown headers:** vendors recommend both; I found no study showing one beats the other for chat use. Use whichever the playbook already uses, consistently.
- **No study shows rambling beats structured input** for brainstorming. The rubric's position rests on Andrew's reasoning about how people think plus the evidence that a structured refining pass works.
- Several sources are 2026 preprints not yet peer reviewed (Ho, Zheng, Illusion of Robustness, In-Writing).

## Sources

- Laban et al. (2025). [LLMs Get Lost in Multi-Turn Conversation](https://arxiv.org/abs/2505.06120).
- Ho et al. (2026). [Agentic Context Management for Multi-Turn Human-AI Conversations](https://arxiv.org/abs/2611.00518). Preprint.
- Zheng, Tian and Rizoiu (2026). [Reading Too Much into Context: Passive Exposure Can Steer LLM Decisions](https://arxiv.org/abs/2609.33065). Preprint.
- Yang et al. (2025). [What Prompts Don't Say: Underspecification in LLM Prompts](https://arxiv.org/abs/2505.13360).
- Wu et al. (2025). [CollabLLM: From Passive Responders to Active Collaborators](https://arxiv.org/abs/2502.00640).
- (2026). [The Illusion of Robustness: Prediction Flips under Task-Irrelevant Context](https://arxiv.org/abs/2607.12963). Preprint.
- Chroma (2025). [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://trychroma.com/research/context-rot).
- Anthropic. [Long context prompting tips and prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips).
- OpenAI. [GPT-4.1 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide) (delimiters and instruction placement).
- Meincke, Mollick et al. (2025). [Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/). Wharton.
- Meincke, Mollick et al. (2025). [Prompting Science Report 3: I'll pay you or I'll kill you, but will you care?](https://gail.wharton.upenn.edu/research-and-insights/techreport-threaten-or-tip/). Wharton.
- Wharton Generative AI Labs (2025). [Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/).
- Kalai et al. (2025). [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664). OpenAI.
- Truong et al. (2023). [Language Models Are Not Naysayers](https://arxiv.org/abs/2306.08189).
- Tam et al. (2024). [Let Me Speak Freely? Format Restrictions and LLM Performance](https://arxiv.org/abs/2408.02442).
- (2026). [Thinking Before Constraining: In-Writing decoding](https://arxiv.org/abs/2601.07525). Preprint.
- Ali et al. (2024). [Mitigating Copy Bias in In-Context Learning](https://arxiv.org/abs/2410.01288).
- INCOSE Requirements Working Group. Guide to Writing Requirements (GtWR). INCOSE.
- Mavin, Wilkinson, Harwood and Novak (2009). Easy Approach to Requirements Syntax (EARS). IEEE International Requirements Engineering Conference.
