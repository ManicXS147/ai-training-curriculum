# Fact-check: AI Basics speaker notes, "The four-part question, built" through "Questions: Asking and checking" (source lines 55-107)

Verdict scale: Supported / Partly supported (with exact correction) / Unsupported / Outdated. Every URL below was opened (fetched) unless marked "search listing only".

## Does each named number match the source exactly?

### Takeaway
The two named numbers that come from research are accurate: Laban et al. 2025 does report an average 39% drop, and verbalized-confidence research does find models mostly say 80-100%. The deck's wording around them needs small fixes. "1.33 is a common minimum Cpk" is standard industry practice, but I could not confirm it in the primary source I opened (NIST uses 1.0 as its target). "0.8 is not capable" holds under either threshold.

### Cited Findings

**Claim (line 74): "A 2025 study found answers got about 39% worse when details came out over several turns instead of all at once (Laban et al.)." Verdict: Supported, with a wording tweak.**
- The paper is "LLMs Get Lost In Multi-Turn Conversation" by Laban, Hayashi, Zhou and Neville, arXiv 2505.06120, submitted May 9, 2025. The abstract reports "an average drop of 39% across six generation tasks" between multi-turn and single-turn conversations. — [arXiv abstract](https://arxiv.org/abs/2505.06120)
- In the body: "every model sees its performance degrade on every task when comparing Full and Sharded performance, with an average degradation of -39%." The study covered 15 LLMs from eight model families and more than 200,000 simulated conversations. — [arXiv HTML](https://arxiv.org/html/2505.06120)
- The abstract breaks the drop into "a minor loss in aptitude and a significant increase in unreliability." It also says: "when LLMs take a wrong turn in a conversation, they get lost and do not recover." — [arXiv abstract](https://arxiv.org/abs/2505.06120)
- When the same information is given in one turn ("Concat"), models average 95.1% of their full single-prompt score. The loss comes from the information arriving piece by piece, not from rewording. — [arXiv HTML](https://arxiv.org/html/2505.06120)
- Suggested wording: "A 2025 study of 15 models found performance dropped by an average of 39% when the details of a task came out over several turns instead of all at once (Laban et al., 2025). Mostly the answers became less consistent: once a chat took a wrong turn, it rarely recovered."

**Claim (line 104): "Cpk measures how well a process fits inside its spec limits; 1.33 is a common minimum, so 0.8 is not capable." Verdict: Partly supported.**
- NIST defines Cpk as min(Cpl, Cpu), so it accounts for both spread and centering against the spec limits. In its worked example NIST says "We would like to have Cpk at least 1.0," and it calls a process with Cpk of about 0.67 "not a good process." — [NIST/SEMATECH e-Handbook 6.1.6](https://itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)
- NIST does not name 1.33 as a minimum Cpk. On that page, 1.33 appears only in the Cp table. — [NIST/SEMATECH e-Handbook 6.1.6](https://itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)
- Suggested wording: "Cpk measures how well a process fits inside its spec limits, allowing for both spread and centering. Many customers and industries require at least 1.33, and even the textbook floor is 1.0, so 0.8 is not capable."

**Claim (line 74): "it will almost always say it is highly confident." Verdict: Partly supported.** The number checks out. The conclusion is covered in the third key question below.
- Xiong et al. (arXiv 2306.13063, ICLR 2024) report that verbalized confidences "appear as multiples of 5 and with most values ranging between the 80% to 100% range" (Section 5.1). — [arXiv HTML v2](https://arxiv.org/html/2306.13063v2)

### Inferences
- The Laban paper tested mid-2025 models (GPT-4o-class and similar). Whether the 39% figure holds for late-2026 models is not established. Presenting it as "a 2025 study found" is accurate. Presenting it as a current constant would not be.

### Gaps
- I did not open a primary industry standard (for example AIAG SPC or PPAP manuals) that states 1.33. Those manuals are paywalled. A Wikipedia "Process capability index" page appeared in search results but I did not open it.
- "Most of these take seconds" (line 104, about the planted-error checks) is a claim about the classroom game. No external evidence applies.

## For advice with no cited source, is there credible research or vendor guidance backing it?

### Takeaway
Most moves have vendor guidance (Anthropic docs) or peer-reviewed or preprint research behind them. The weakest is Move 4, "have it ask you first." It has research showing clarification helps on ambiguous requests, but no vendor prompting guidance that I found. The persona claims (Zheng 2024; Wharton Dec 2025) check out, but Anthropic's own docs still recommend role prompting for tone. The deck should not imply that roles are useless.

### Cited Findings

**Line 56: "research (Zheng et al. 2024; Wharton, December 2025) finds expert personas don't make answers more accurate." Verdict: Supported.**
- Zheng, Pei, Logeswaran, Lee and Jurgens, "When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models" (arXiv 2311.10054, v2 dated 7 Oct 2024). They find that "adding personas in system prompts does not improve model performance across a range of questions" compared with no persona. — [arXiv](https://arxiv.org/abs/2311.10054v2). A search listing also shows an EMNLP 2024 Findings entry; I did not open it.
- Wharton Generative AI Labs, "Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy" (Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke; arXiv 2512.05858, December 2025). The report tested six models on GPQA Diamond and MMLU-Pro and concludes: "assigning an expert persona is not a reliable way to improve accuracy." It also says: "When persona prompts do matter, they are more likely to reduce accuracy than to increase it." There were small exceptions; for example, Gemini 2.0 Flash gained about 9 points with an engineering persona on MMLU-Pro. — [arXiv PDF](https://arxiv.org/pdf/2512.05858v1)
- Nuance: Anthropic's current guide says "Setting a role in the system prompt focuses Claude's behavior and tone for your use case. Even a single sentence makes a difference." — [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

**Line 56: "saying who will read the answer does shape its tone and level." Verdict: Supported by vendor guidance. I found no controlled study.**
- Anthropic: "Providing context or motivation behind your instructions … can give Claude more information about your goals and help it deliver more targeted responses." — [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Suggested wording: "Expert personas don't make answers more accurate (Zheng et al. 2024; Wharton, December 2025). Telling it who will read the answer is the more useful part, because it shapes the tone and the level of detail."

**Line 56: "Thirty seconds of setup saves about ten minutes of back and forth." Verdict: Unsupported, but already labelled honestly** ("a rule of thumb, not a measured result"). Keep the label.

**Move 1 (line 62): give it the source, "This fixes 'confident and wrong.'" Verdict: Partly supported. "Fixes" is too strong.**
- Anthropic's hallucination guide recommends grounding the answer in a provided document and says these techniques "significantly reduce hallucinations" but "don't eliminate them entirely. Always validate critical information, especially for high-stakes decisions." — [Anthropic: Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- Suggested wording: "This cuts down 'confident and wrong'. It doesn't remove it, which is why section 03 exists."

**Move 2 (line 65): make it quote the line and section. Verdict: Supported by vendor guidance.**
- Anthropic: "Use direct quotes for factual grounding … ask Claude to extract word-for-word quotes first," and "Verify with citations … If it can't find a quote, it must retract the claim." — [Anthropic: Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- Anthropic also advises: "For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task." — [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- "This fixes 'makes up sources'" is too strong, and a model can misquote. Suggested wording: "You can check the quote in ten seconds, and a quote that isn't in the document is a red flag."

**Move 3 (line 68): open rather than leading questions reduce agreement or sycophancy. Verdict: Supported (evidence is indirect).**
- Sharma et al. (Anthropic), "Towards Understanding Sycophancy in Language Models" (ICLR 2024), tested prompts such as "I think the answer is [incorrect answer], but I'm really not sure." They found "The user suggesting an incorrect answer can reduce accuracy by up to 27% (LLaMA 2)." The trend was consistent across all assistants tested, and GPT-4 was the most robust. Assistants also gave "more positive feedback about arguments that the user likes." — [arXiv HTML v4](https://arxiv.org/html/2310.13548v4)
- The study shows that a hinted answer pulls the model's answer toward it. That an open question avoids this follows from the study; it was not tested directly. "There is no hint to pull the answer" is a fair summary. "This fixes" is too strong; "This removes the hint" is accurate.

**Move 4 (line 71): have it ask you clarifying questions first. Verdict: Partly supported.** There is research evidence. I found no vendor prompting guidance.
- Zhang, Knox and Choi, "Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions" (arXiv 2410.13788, revised Mar 2025): "State-of-the-art LLMs often do not ask clarifying questions when presented with an ambiguous request, and instead respond directly by assuming the user's intent." Their training method gave about a 5% F1 improvement. This was a training intervention, not a user prompt. — [arXiv HTML v2](https://arxiv.org/html/2410.13788v2)
- Anthropic's best-practices page gives no general advice to have the model ask clarifying questions. — [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- The Laban et al. results also back the idea: giving everything up front (Concat, 95.1% of the full single-prompt score) beats details trickling in, and asking first is one way to get everything up front. — [arXiv HTML](https://arxiv.org/html/2505.06120)
- Suggested wording: "Models usually guess what you meant instead of asking, so tell it to ask first. It finds the gaps in your question, which saves rounds of back and forth." Present it as good practice, not a measured result.

**Line 74: "Show what good looks like … You get your format the first time." Verdict: Partly supported.**
- Anthropic: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure. A few well-crafted examples … improve accuracy and consistency." The page recommends 3-5 varied examples. — [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- "First time" is a promise. One example is fewer than the guide recommends and can be copied too literally. Suggested wording: "Paste one good pass-down and ask for the same shape. An example is one of the most reliable ways to get your format."

**Line 74: "If it drifts, ask it to sum up everything you've told it, then paste that summary into a new chat." Verdict: Supported. The cited paper itself makes this recommendation.**
- Laban et al.: "starting a new conversation that repeats the same information might yield significantly better outcomes than continuing an ongoing conversation." They suggest asking the model to consolidate what you've told it ("Please consolidate everything I've told you so far") and reusing that in a new chat. — [arXiv HTML](https://arxiv.org/html/2505.06120)
- Restating details inside the same chat helps less. "Recap" recovered about 16-18 points and "Snowball" about 6-11 points, versus a 30-plus point loss, and both "still lag behind Full or Concat." — [arXiv HTML](https://arxiv.org/html/2505.06120)

**Line 74: "Permission to say 'I don't know' cuts confident errors, since training long rewarded guessing." Verdict: Partly supported.** The vendor guidance and the explanation both check out. I found no measured effect for a user's prompt.
- Anthropic: "Explicitly give Claude permission to admit uncertainty. This technique can drastically reduce false information." No figures are given. — [Anthropic: Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- OpenAI, "Why language models hallucinate" (5 Sep 2025): "standard training and evaluation procedures reward guessing over acknowledging uncertainty." On SimpleQA, gpt-5-thinking-mini abstained 52% of the time with a 26% error rate. o4-mini abstained 1% of the time with a 75% error rate, at similar accuracy (22% vs 24%). — [OpenAI](https://openai.com/index/why-language-models-hallucinate/)
- The OpenAI result concerns how models are trained and scored, not what a user types in a prompt. It explains why the advice makes sense but does not measure it.
- Suggested wording: "Give it permission to say 'I don't know.' Training long rewarded guessing, and model makers recommend this to cut confident errors."

**Check 3 (line 92): re-ask in a new chat; "An answer that changes from one try to the next is a strong sign it is making that part up. Agreement is not proof…" Verdict: Supported.** The caveat in the notes is correct.
- Anthropic, "Best-of-N verification": "Run Claude through the same prompt multiple times and compare the outputs. Inconsistencies across outputs could indicate hallucinations." — [Anthropic: Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- Farquhar et al., Nature (June 2024), "Detecting hallucinations in large language models using semantic entropy." Several answers are sampled and grouped by meaning, and high disagreement flags confabulations. The method misses errors the model repeats consistently, such as wrong facts learned in training. — [Oxford OATML blog on the Nature paper](https://oatml.cs.ox.ac.uk/blog/2024/06/19/detecting_hallucinations_2024.html). The PMC copy was blocked by a CAPTCHA.
- Suggested wording: "…is a strong warning sign that it's guessing on that part." "Making that part up" is acceptable. Answers can also differ because the question was ambiguous, so "guessing" is the more precise word.

**Checks 1, 2 and 4, and "Check harder when the stakes are higher" (lines 86-98).** These are practice advice, not evidence claims. Anthropic's closing note backs the general principle: "Always validate critical information, especially for high-stakes decisions." — [Anthropic: Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). The office examples ($1.2M vs $120K, the warranty years) are illustrations.

### Inferences
- "Iterate on small fixes in the same chat" (line 74) does not conflict with Laban et al. That paper studied task details arriving piece by piece, not edits to a draft that already exists. Still, it is consistent with the paper to say "if it drifts, restart with a summary."
- Anthropic recommends role prompts for tone, so the deck should say personas don't add accuracy, not that they do nothing.

### Gaps
- I found no controlled study that measures the effect of a user adding "If the document doesn't say, tell me" in a chat prompt. The support is vendor guidance only.
- I found no vendor guide (Anthropic, OpenAI, Microsoft) that recommends "ask me clarifying questions first". I did not open the OpenAI or Microsoft prompting guides because of the tool-call budget.
- "It points you straight to the parts worth checking" (the ambiguity question, line 74): I found no source either way.

## Is anything stated more strongly than the evidence allows?

### Takeaway
Yes, in four places. The verb "fixes" in Moves 1-3. The flat "asking how confident it is doesn't help." "You get your format the first time." And "Permission … cuts confident errors" presented as a measured effect. Each needs a one-word or one-clause softening.

### Cited Findings
- **"Asking how confident it is doesn't help, because it will almost always say it is highly confident." Verdict: Partly supported. "Doesn't help" goes beyond the evidence.**
  - Xiong et al. support overconfidence: "LLMs, when verbalizing their confidence, tend to be overconfident," with most values at 80-100%. — [arXiv abstract](https://arxiv.org/abs/2306.13063); [arXiv HTML v2, §5.1](https://arxiv.org/html/2306.13063v2)
  - The same paper also finds "As model capability scales up, both calibration and failure prediction performance improve." It adds that consistency across multiple responses "can help mitigate this overconfidence." — [arXiv abstract](https://arxiv.org/abs/2306.13063)
  - The models tested date from 2023-24, so the finding may be partly outdated for 2026 models.
  - Suggested wording: "Don't rely on asking how confident it is: models tend to say 80-100% confident even when they're wrong. Comparing two fresh answers (check 3) tells you more."
- **"This fixes …" (Moves 1-3, and line 59 "each fix one weak spot").** Anthropic says these techniques reduce hallucinations but "don't eliminate them entirely." — [Anthropic: Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). Use "cuts down" or "guards against."
- **"You get your format the first time."** The vendor wording is "one of the most reliable ways," not a guarantee. — [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- **"Answers got about 39% worse."** The figure matches the source. "Performance dropped" is closer to the paper's metric (task scores) than "answers got worse." — [arXiv](https://arxiv.org/abs/2505.06120)
- **Check 3, "strong sign it is making that part up."** Acceptable. Semantic entropy is designed to catch exactly this kind of guessing (confabulation). — [OATML](https://oatml.cs.ox.ac.uk/blog/2024/06/19/detecting_hallucinations_2024.html)

### Inferences
- None of the claims in lines 55-107 are wrong enough to remove. The fixes are wording changes. The one exception is the Cpk line, which should drop the implied single industry standard or name the threshold as a customer or industry requirement.

### Gaps
- Calibration of the newest (2026) models when asked for verbalized confidence: I did not find a 2025-2026 replication within the budget.
