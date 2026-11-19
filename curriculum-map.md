# Curriculum Map — AI Training
*(Upload to project knowledge. Update when a course's scope changes.)*

## Structure

```
                     ┌──> AI for Troubleshooting  (engineers + equipment techs, 90 min)
                     │          ▲ 8D content is optional/useful for process engineers too
AI Basics ───────────┼──> AI for Process Development (process engineers, 90 min)
(everyone, 90 min)   │
                     └──> AI for Leaders (managers + execs, 50 min)
```

AI Basics is the prerequisite for everything else. The three advanced courses are parallel branches, not a sequence. Process engineers don't need Troubleshooting, though its 8D material may help with process issues.


## How the advanced courses teach (Andrew, 2026-11-14)

Everything after AI Basics is taught as a **workflow with saved prompts**, not as loose tips.

- Each course walks one or more real workflows end to end. Every step has a prompt that attendees keep and reuse.
- Each course also teaches people to **improve the workflow and its prompts over time**: notice where the output fell short, change the prompt, keep the better version.
- Attendees leave with the course **playbook** and know how to improve it and build their own.
- **Playbook standard:** a playbook is not a simple text prompt. Every playbook is held to the standard of Andrew's Systems Engineering Playbook v2 (`reference/Systems-Engineering-Playbook-v2.md`): a stated output, stages in order, separate work and review chats, a structured prompt per stage, shared gates and rules, and a version number.
- **Prompt standard:** every workflow prompt (the saved prompts in a playbook, used by copy and paste or later in a harness) must score 3 on all five criteria of the Modern AI Prompt Evaluation Rubric (`reference/Prompt-Evaluation-Rubric.md`): context separated from instructions with tags, goals instead of step-by-step scripts, explicit positive limits and a rule for missing data, a strict output format, and no filler or personas. The rubric is the tool for creating and updating those prompts. It does not apply to the conversational practice prompts in AI Basics.
- Playbooks are **shared**: people copy them and paste the prompts into the chatbot, until the workflows can be built into a tool such as SkyChat.
- AI Basics stays tool-agnostic principles. It is the foundation the workflows build on.

---

## AI Basics
- **Audience:** anyone interested, "from the tech to the exec": office workers, technicians, non-technical staff, engineers, leaders.
- **Length:** 90 min, break at 45.
- **Purpose:** dispel fear and myth by lifting the curtain on how LLMs work, and give everyone enough basic skill to start using AI and see for themselves what it is and isn't.
- **Key ideas** *(draft — refine)*:
  - What an LLM actually is, demystified
  - What it's good at, what it's bad at, and why
  - Job fears are answered by tone, not by a slide: teach the tool, show its shortcomings, and keep the person in charge. The trainer makes no promises about jobs and presents no research on the subject: this is a training, not a lecture.
  - The engine-vs-car analogy is optional: use it in a line where it explains something people can act on (why AI needs the source, why most AI use will happen inside tools). Value add, not preaching.
  - Hands-on: first productive uses with Copilot
- **Hands off to the advanced courses:** a shared vocabulary, basic prompting, a healthy skepticism of outputs, and the habit of keeping your own judgment.

## AI for Troubleshooting
- **Audience:** engineers and equipment technicians.
- **Length:** 90 min, break at 45.
- **Purpose:** use AI to investigate tool downs and speed up difficult investigations.
- **Key ideas** (agreed 2026-11-14): one workflow, the full 8D run as a loop with AI in every discipline (frame, update the causes with data, documents and technician results, signed check plans, fix, qual, prevent, close), taught through a tool-down case; each step lands a principle tagged H (when the human steps in), R (reviewing AI work, and building reviews with AI) or O (owning and communicating what you produce). One slide notes the same loop for process troubleshooting.
- **Synthetic data:** tool-down logs, alarm histories, maintenance records, an 8D template, plus mocked interview answers and technician findings (troubleshooting-kit, worked example).

## AI for Process Development
- **Audience:** process engineers. Equipment engineers generally don't need it.
- **Length:** 90 min, break at 45.
- **Purpose:** use AI to improve DOEs, process experimental data, and draw insights from experiments without giving up judgment and expertise.
- **Key ideas** *(draft — refine)*: DOE design support, data analysis and interpretation, and checking AI-generated insights against process knowledge.
- **Synthetic data needed:** DOE datasets and experiment results.

## AI for Leaders
- **Audience:** managers and executives. Should attend AI Basics first.
- **Length:** **50 min.**
- **Purpose:** leaders mostly analyze, collect and interrogate information rather than produce it. The course teaches them to:
  - Notice when material is AI-generated
  - Check AI-generated material for common pitfalls
  - Use AI to interrogate business plans and strategy, not to defer to it
  - Run leader workflows, starting with meetings: record the meeting, give the transcript to AI with a saved prompt, and get decisions, owners and open questions
  - Think about where to add or invest in AI to reach their larger strategic goals
- **Must not repeat AI Basics.** It covers how a leader's use of AI differs from an individual contributor's.
- **Synthetic data needed:** sample AI-generated reports or plans with planted flaws to find.

---

## Open items
- [ ] Hands-on exercises for each course
- [ ] Synthetic data packages
- [ ] Confirm SkyChat features before it appears in any exercise
