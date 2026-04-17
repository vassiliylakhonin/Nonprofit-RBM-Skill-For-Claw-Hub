# Nonprofit Proposal Decision Engine (OpenClaw Skill)

`nonprofit-proposal-decision-engine` helps NGO teams and grant writers turn messy project inputs into donor-ready proposal artifacts and a hard submission verdict (`Go / Conditional Go / No-Go`).

## What this skill does

- Drafts concept notes, LOIs, and full proposal structures
- Builds RBM/ToC logic and logframe-ready outputs
- Produces MEAL, risk, safeguarding, and donor-fit matrices
- Enforces evidence discipline (no fabricated citations or certainty)
- Adds decision gating and submission readiness checks

## Install

```bash
clawhub install nonprofit-rbm-logic-model
```

## Quick usage patterns

```text
mode=concept [project brief]
mode=donor-fit [project brief + donor call]
mode=review [proposal draft]
mode=express [fast turnaround brief]
```

## Output contract (always)

1. Decision Summary
2. Facts / Assumptions / Hypotheses / Unknowns
3. Core Proposal Artifacts
4. Donor-Fit Matrix
5. Evidence and Traceability (or Evidence Needed)
6. Submission Readiness Checklist

## Repository structure

```text
.
├── SKILL.md
├── README.md
└── LICENSE
```

## License

MIT
