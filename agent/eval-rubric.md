# Shared Skill Evaluation Rubric

Score each skill response against its case from 0 to 2 on each dimension. Judge the behavior, not whether the model repeats the expected wording.

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Fact restraint | Presents unknowns, estimates, or unsupported causal claims as facts | Signals uncertainty but leaves a material overclaim or provenance gap | Preserves source and evidence status; bounds conclusions and identifies material unknowns |
| Task match | Solves a different task or misses the requested audience/artifact | Partly matches but misses an important need or boundary | Fits the user's task, audience, scope, and requested output |
| Actionability | Gives no useful next step or invents precision | Gives broad advice with unclear verification or ownership | Names a practical next action and the evidence/decision needed to move forward |
| Format | Hard to scan or omits essential information | Mostly usable with notable structural gaps | Clear, appropriately concise, and fit for the deliverable |
| Tone calibration | Blaming, theatrical, or falsely certain | Uneven, overcautious, or too forceful for context | Direct and candid, proportionate to evidence and audience |

Maximum: 10. A case passes at 8 or above only when **Fact restraint = 2** and no unsupported claim remains. Record the observed failure and evidence for each score. Run at least one missing-information case, one conflicting-information case, and one normal case per skill. Static repository validation does not substitute for this behavioral review.

## Scoring calibration example

Use this scenario: “Instrumentation coverage and metric definitions were checked; the metric fell after a product change; no experiment or segment analysis has been done.” Score the whole answer against the requested task, not isolated keywords.

| Dimension | 0-point signal | 1-point signal | 2-point signal |
| --- | --- | --- | --- |
| Fact restraint | Says the product change caused the fall | Says causality is uncertain but treats the fall as fully comparable without explaining evidence status | Separates the user-reported observed fall from the unproven causal explanation, and names material remaining unknowns |
| Task match | Gives generic analytics advice without answering whether cause is known | Answers causality but misses the requested next step | Directly answers what can be concluded and gives the requested decision-relevant next step |
| Actionability | Gives no way to investigate | Says “analyze more” or “run an experiment” without specifying what it should distinguish | Names a feasible comparison or segmentation, what evidence would support/reject the hypothesis, and a review condition |
| Format | Buries the conclusion in an unstructured discussion | Mostly readable but separates findings from actions poorly | Makes conclusion, evidence/unknowns, and next action easy to find at a detail level suited to the request |
| Tone calibration | Accusatory, theatrical, or categorical beyond evidence | Hedged or overly forceful in places | Direct, proportionate, and clear about what is known versus unresolved |

This is a calibration aid, not a keyword checklist. A concise answer can earn full marks; an answer should not receive credit merely for saying “uncertain” if it does not help the user decide what to do next.
