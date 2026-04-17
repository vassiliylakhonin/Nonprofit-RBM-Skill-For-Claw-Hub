# Nonprofit Proposal Decision Engine (OpenClaw Skill)

[![ClawHub](https://img.shields.io/badge/ClawHub-nonprofit--rbm--logic--model-2bc6a4)](https://clawhub.ai/vassiliylakhonin/nonprofit-rbm-logic-model)
[![CI](https://github.com/vassiliylakhonin/Nonprofit-RBM-Skill-For-Claw-Hub/actions/workflows/ci.yml/badge.svg)](https://github.com/vassiliylakhonin/Nonprofit-RBM-Skill-For-Claw-Hub/actions/workflows/ci.yml)
[![GitHub release](https://img.shields.io/github/v/release/vassiliylakhonin/Nonprofit-RBM-Skill-For-Claw-Hub)](https://github.com/vassiliylakhonin/Nonprofit-RBM-Skill-For-Claw-Hub/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

`nonprofit-proposal-decision-engine` helps NGO teams and grant writers turn messy project inputs into donor-ready proposal artifacts and a hard submission verdict (`Go / Conditional Go / No-Go`).

**ClawHub page:** https://clawhub.ai/vassiliylakhonin/nonprofit-rbm-logic-model

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
