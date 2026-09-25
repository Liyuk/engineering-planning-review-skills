# Decision and review contract

This contract captures shared behavior for planning, technical review, and reporting skills. It is a source of truth for future skill revisions; each skill should apply only the parts relevant to its task.

## Evidence states

Use these states when the distinction affects a decision or a reported claim:

- **User-provided** — supplied by the user or their source material; not independently verified.
- **Sourced** — supported by a cited external source; retain source and publication/access date when relevant.
- **Measured** — observed in a named test, benchmark, or operational dataset; preserve method, scope, and time window.
- **Estimated** — calculated from explicit assumptions or ranges; show the inputs and formula.
- **Inferred** — reasoned from available evidence; state the evidence and material alternative explanations.
- **Assumed** — temporarily accepted to proceed; say what changes if it is false.
- **Unknown / to confirm** — required input is unavailable or conflicting.

Do not turn an estimate, inference, or unknown into a confirmed fact during handoff or reporting. If a metric cannot be calculated, provide its definition, formula, and missing inputs instead of inventing a value.

## Evidence-to-judgment sequence

1. Define the question, audience, scope, and time window.
2. Gather facts and state their evidence status.
3. Describe relevant changes over time.
4. Identify prior art, competitors, alternatives, and the strongest obvious counter-explanation.
5. Compare options against shared dimensions and actual constraints.
6. Record benefits, costs, failure modes, and who bears each trade-off.
7. Challenge the provisional conclusion with counterexamples and missing evidence.
8. State only the bounded conclusion the evidence supports, including its conditions and limits.

This is a working sequence, not a mandatory visible section list. Skip steps that do not apply and say when missing information blocks a judgment.

## Review finding format

Each material finding should include:

```text
Finding: concise statement of the issue
Evidence: source, quote, metric, or missing input
Impact: consequence if left unresolved
Priority: blocker / important / recommendation / accepted risk
Action or decision: what should happen next, and who must decide when known
Status: open / resolved / accepted / not substantiated
```

Do not manufacture a minimum number of questions or findings. A review may conclude that no blocking issue is supported by the available evidence. Distinguish a missing decision from a defect and a preference.

## Shared handoff fields

When moving from planning to review or reporting, preserve the relevant fields:

- decision question and audience;
- objective, baseline, target, scope, and time window;
- evidence and its state, source, method, and metric definition;
- options considered and trade-offs;
- assumptions, unknowns, and unresolved conflicts;
- cost, owners, dependencies, risks, and fallback/rollback;
- milestones and acceptance criteria;
- decisions needed and current status.

Final output format remains task- and audience-specific. This contract preserves information state; it does not require every response to include every field.
