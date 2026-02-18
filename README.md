# Nonprofit RBM Skill for ClawHub

A practical OpenClaw skill for nonprofit and NGO teams that need donor-ready Results-Based Management (RBM) logic models.

## What this skill does

- Builds a 5-level results chain: Inputs -> Activities -> Outputs -> Outcomes -> Impact
- Adds a Theory of Change (if/then pathway + key assumptions)
- Proposes SMART outcome indicators
- Maps outcomes to relevant SDG goals/targets
- Recommends a monitoring and data collection plan

## Who this is for

- Nonprofit program managers
- M&E / MEAL specialists
- Grant writers
- NGO consultants
- Social impact startups preparing donor-facing plans

## Install

From ClawHub:

```bash
clawhub install nonprofit-rbm-logic-model
```

Optional pinned version:

```bash
clawhub install nonprofit-rbm-logic-model --version 1.0.2
```

## Use in OpenClaw

Prompt with the skill name:

```text
Use $nonprofit-rbm-logic-model to design an RBM logic model for [program], including Theory of Change, SMART indicators, SDG mapping, and a monitoring plan.
```

## Output format

1. Theory of Change (if/then statement plus causal pathway and key assumptions)
2. Executive Summary (2-3 sentences)
3. Logic Model Table (Inputs to Impact)
4. Outcome Indicators (group by outcome)
5. SDG Alignment (goal and target references)
6. Data Collection Plan (method, frequency, owner)
7. Assumptions and Risks (recommended when uncertainty exists)

## Repository structure

```text
skills/.experimental/nonprofit-rbm-logic-model/
  LICENSE.txt
  SKILL.md
  agents/openai.yaml
  references/rbm-framework.md
```

## License

MIT. See `skills/.experimental/nonprofit-rbm-logic-model/LICENSE.txt`.
