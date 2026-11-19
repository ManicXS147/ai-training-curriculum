# Plan an Experiment: Worked Example (course kit, v0.5)

SYNTHETIC TRAINING DATA. This example uses the course project (a faster cap nitride on PECVD-03). No real tool, lot, product or person.

Use it with `Process-Playbook-Plan-an-Experiment-v0.5.md`. It gives you:

1. **Your messages for Thread 1**, ready to paste, so the interview moves fast.
2. **Your answers to the sort and the menus.**
3. **Restart points:** a reference Experiment Brief and Design Decision Record. If you fall behind, start the next hands-on from these.
4. **What good output looks like** at each step, so you know what to check.

The restart points are reference versions written from the kit files. They are not AI output. Your AI's versions will word things differently; check them against the standard, not against these words.

---

## 1. Thread 1: your messages

Paste the Discovery Interview prompt first. Then paste M1. After that, the AI asks its own questions; answer from M2 to M6, whichever fits what it asked. Paste a message more than once if it asks about the same thing again. Upload the files when it asks for them.

**M1 (talk it through)**

> My manager wants the cap nitride step on PECVD-03 about 20 percent faster, because that tool is the bottleneck for the new product ramp. Right now it's 60 seconds of deposition per wafer at about 3100 angstroms a minute. We usually run these experiments on chamber A. The last time anyone tried this was a 2021 DOE on the sister tool, 8 wafers, which felt about right. I'm worried about uniformity at high power, and integration got burned once when a silane-rich nitride changed the HF etch rate. I have 25 wafers and two weeks.

**M2 (responses and specs)**

> The specs are in project_brief.txt: rate at least 3700 A/min, uniformity at most 2.0 percent one sigma on the 49-point map, stress -250 to -50 MPa, RI 1.98 to 2.02, and HF wet etch rate within 10 percent of today's. Cpk at least 1.33 for uniformity, stress and RI, checked for each chamber separately. Thickness and RI come off the step 39 ellipsometer map. I don't know the gauge repeatability numbers offhand.

**M3 (factors and limits)**

> I can change RF power, pressure, silane flow and spacing. The limits are in tool_limits.csv. NH3 and heater temperature are fixed and out of scope. Deposition time just gets set to hit 3000 A. All four knobs can change from run to run without a problem.

**M4 (mechanism and prior learning)**

> From the 2021 report, power and silane drive rate, and tighter spacing helps too. Uniformity got worse at high power, but they couldn't tell if pressure fixes that because the interaction was confounded. The 2023 report says more silane drops the HF etch rate. Past reports are in past_reports.txt.

**M5 (budget, scope, groups, safety)**

> 25 wafers, two weeks. The recipe has to pass on both chambers, A and B. Chamber B's heater was replaced in 2025 and its uniformity is higher and noisier, so B needs checking on its own. Don't go below 3.5 Torr, the plasma goes unstable. And there's a particle check needed if spacing goes below 350 mil.

**M6 (success and non-goals)**

> Success is a recipe that meets every spec on both chambers and is at least 20 percent faster, and an experiment that finally answers whether lower pressure fixes uniformity at high power. Not in scope: NH3, heater temperature, or retuning any downstream step in this experiment.

**M7 (your answer to the sort table)**

> Chamber A is an example: the ask covers both chambers. The 8 wafers in 2021 is background: my budget is 25. The 2021 and 2023 reports are binding where they set a limit or a measurement, otherwise background.

**M8 (after the draft)**

> Confirmed.

---

## 2. Your answers to the menus

**Design Decision Menu (Thread 2).** The option letters will vary. Pick the option in each category that matches:

- Design family: full 2-level factorial in the four factors with center points (20 wafers), because it can estimate power x pressure.
- Replication and noise: center points give the noise estimate; no full replicate.
- Groups that differ physically: run the experiment on one chamber and qualify the other separately; the chamber held constant is A.
- Spares and run order: keep 5 spares; randomize with a stated seed.

Dispositions: accept the recommended disposition for every open item.

**Risk Decision Menu (Thread 3).** Take the recommended default in every category unless it spends spares before the experiment is complete.

**Assumption sign-off:** confirm any assumption that comes straight from a kit file; leave every metrology repeatability assumption Pending.

---

## 3. Restart point: Experiment Brief v1.0

Paste this into R0 for Hands-on 2, or into Thread 2 if you skip ahead.

```markdown
# Experiment Brief v1.0

## 1. Objective and Decision
- EB-1.1 The result selects a new step 38 cap nitride recipe for both PECVD-03 chambers. [M1]
- EB-1.2 Deposition time per wafer drops at least 20 percent versus the process of record (60 s). [M1, project_brief.txt]
- EB-1.3 Done is a recommended recipe backed by the experiment, ready for confirmation runs on both chambers. [project_brief.txt]

## 2. Responses, Specs and Measurement
- EB-2.1 Deposition rate: mean at or above 3700 A/min. [project_brief.txt]
- EB-2.2 Thickness nonuniformity: at or below 2.0 % (1 sigma, 49-point map); Cpk at or above 1.33 per chamber. [project_brief.txt, M2]
- EB-2.3 Film stress: between -250 MPa and -50 MPa; Cpk at or above 1.33 per chamber. [project_brief.txt]
- EB-2.4 Refractive index at 633 nm: between 1.98 and 2.02; Cpk at or above 1.33 per chamber. [project_brief.txt]
- EB-2.5 HF wet etch rate (100:1 HF): mean within 10 % of the process of record. [project_brief.txt, TR-2023-007]
- EB-2.6 Thickness and RI are measured on the step 39 ellipsometer, 49-point map. [M2, process_flow.txt]
- EB-2.7 Wafer-to-wafer nonuniformity on the process of record: sd 0.046 % on chamber A, 0.100 % on chamber B. [spc_baseline.csv]
- EB-2.8 Later steps that depend on this film: 39, 41, 44, 47, 52, 60 and 61. [process_flow.txt]

## 3. Factors and Limits
- EB-3.1 RF power: between 300 W and 600 W (hardware limit). [tool_limits.csv]
- EB-3.2 Chamber pressure: between 3.5 Torr and 5.0 Torr; plasma unstable below 3.5 Torr. [tool_limits.csv, TR-2021-014, M5]
- EB-3.3 SiH4 flow: between 100 sccm and 300 sccm. [tool_limits.csv]
- EB-3.4 Electrode spacing: between 300 mil and 500 mil. [tool_limits.csv]
- EB-3.5 Deposition time is set per run to reach 3000 A. [tool_limits.csv, M3]
- EB-3.6 All four factors can change between consecutive runs. [M3]

## 4. Mechanism, Prior Learning, Examples and Background
- EB-4.1 Higher power and higher SiH4 flow raise deposition rate; tighter spacing raises it too. [TR-2021-014, M4]
- EB-4.2 Nonuniformity rises at high power; whether lower pressure offsets it is unknown, because the earlier design aliased power x pressure. [TR-2021-014, M4]
- EB-4.3 Higher SiH4 flow lowers HF wet etch rate and raises RI. [TR-2023-007, M4]
- EB-4.4 Example: experiments are often run on one chamber of a tool. [M1, M7]
- EB-4.5 Background: an earlier screening experiment on a sister tool used 8 wafers. [M1, M7]

## 5. Budget, Scope, Groups and Safety
- EB-5.1 Budget: at or below 25 wafers. [project_brief.txt, M1]
- EB-5.2 Time: two weeks. [project_brief.txt, M1]
- EB-5.3 Equipment in scope: PECVD-03 chambers A and B. [project_brief.txt, M5]
- EB-5.4 Chamber B nonuniformity runs higher and noisier than chamber A since its heater replacement; each chamber is judged separately. [TR-2025-003, M5]
- EB-5.5 Any run with spacing below 350 mil needs a particle check. [TR-2022-031, M5]
- EB-5.6 NH3 flow (2000 sccm) and heater temperature (400 C) stay fixed. [tool_limits.csv, M3]

## 6. Success Criteria and Non-Goals
- EB-6.1 The experiment estimates the power x pressure interaction on nonuniformity. [M6, TR-2021-014]
- EB-6.2 The recommended recipe meets every spec in section 2 on both chambers at a deposition time at least 20 % shorter. [M6]
- EB-6.3 Non-goal: changing NH3 flow or heater temperature. [M6]
- EB-6.4 Non-goal: retuning any later step within this experiment. [M6]

## 7. Open Items
- OPEN-1 Measurement repeatability of the 49-point thickness map; needed to set the smallest detectable effect. [M2]
- OPEN-2 Measurement method and repeatability for stress, and for HF wet etch rate. [M2]
- OPEN-3 Which chamber or chambers run the experiment, given EB-5.4. [M5]

## 8. Change Log
| Version | Date | Change | Items affected |
| --- | --- | --- | --- |
| 1.0 | 2026-11-14 | First confirmed version. | All |
```

---

## 4. Restart point: Design Decision Record v1.0

Paste this with the brief into a new Thread 3 for Hands-on 3.

```markdown
# Design Decision Record v1.0

## 1. Question Trace
| Question (EB-*) | Effect to estimate | Smallest effect worth detecting | Measurement repeatability (EB-* or ASM-*) |
| --- | --- | --- | --- |
| EB-6.1 | Power x pressure on nonuniformity | 0.2 % (ASM-1) | EB-2.7, ASM-2 |
| EB-2.1 | Main effects of power, SiH4, spacing on rate | 100 A/min (ASM-1) | ASM-2 |
| EB-2.5 | SiH4 effect on HF wet etch rate | 1 A/min (ASM-1) | ASM-3 |

## 2. Selections
| DM ID | Category | Option chosen, stated in full | Units used | Can estimate | Aliased with |
| --- | --- | --- | --- | --- | --- |
| DM-1B | Design family | 2-level full factorial in power, pressure, SiH4 and spacing, plus 4 center points | 20 | All main effects and all two-factor interactions; curvature check | None among two-factor interactions |
| DM-2A | Replication and noise | Center points give the noise estimate; no full replicate | 0 extra | Pure error from 4 centers | n/a |
| DM-3A | Groups | Run every experiment wafer on chamber A; chamber B is judged separately in confirmation runs | 0 extra | Effects on chamber A | Chamber held constant |
| DM-4A | Spares and run order | 5 spares; run order randomized with a stated seed | 5 | Protects against one lost run | n/a |

## 3. Open Item Dispositions
| OPEN-* | Disposition | Working assumption or reason to defer |
| --- | --- | --- |
| OPEN-1 | Assume | ASM-2 |
| OPEN-2 | Assume | ASM-3 |
| OPEN-3 | Closed by DM-3A | Chamber A runs the experiment; chamber B qualifies separately |

## 4. Assumptions
| ASM ID | Assumption | Affected IDs | Consequence if wrong | Sign-off (Pending) |
| --- | --- | --- | --- | --- |
| ASM-1 | Smallest effects worth detecting as listed in the question trace | Question trace | The design may be too small or too large for the real need | Pending |
| ASM-2 | 49-point map repeatability is small next to the wafer-to-wafer sd in EB-2.7 | EB-2.2, EB-6.1 | Real effects hide in measurement noise | Pending |
| ASM-3 | Stress and HF wet etch rate are measured on the standard monitor methods, repeatability under 2 % | EB-2.3, EB-2.5 | A WER shift near the 10 % limit is missed | Pending |
```

---

## 5. What good output looks like

**Interview (Thread 1).**
- Round 1 marks at least responses or constraints Fuzzy, and asks about measurement repeatability.
- The sort table lists chamber A and the 8-wafer DOE, and does not treat either as binding before you answer M7.
- The draft cites a message or a file on every item, and puts open questions in section 7 instead of guessing.

**Brief Lint and Review (R0).**
- The lint shows its code before the report.
- The review quotes your messages for every finding, and writes NO SUPPORT where nothing you said backs an item.
- A good review flags any design choice in the brief, any limit that doesn't match the file it cites, and any spec from the brief file that is missing.

**Design Decision Menu (Thread 2) and Review (R1).**
- At least one option is blind to power x pressure (an 8-run fraction), and the menu says so.
- No option uses a level outside tool_limits.csv.
- The recommended default can estimate power x pressure.

**Run Sheet (Thread 3) and Lint (R2).**
- 20 runs plus 5 spares, factor levels 450/600 W, 3.5/4.5 Torr, 180/260 sccm, 350/450 mil, centers at 525 W, 4.0 Torr, 220 sccm, 400 mil.
- Runs at 350 mil carry the particle check.
- The analysis plan states the run exclusion rule (for example, an incomplete metrology map) before any data exists.
- The lint reports L1 to L7 from executed code and gives the L8 counts.

**Your review.** Walk the run sheet. If you notice that no run measures HF wet etch rate, that is a requirement the run sheet missed (EB-2.5): fix it in Thread 3. If you want a response the brief never named, that is a Brief Change.

**Risk and release.** The risk ledger names at least one measurement failure (an incomplete map), the chamber B difference, and the later steps in process_flow.txt once you give it that file. The release review lists every Pending assumption with an owner, or OWNER NEEDED.
