# Nonprofit Proposal Go/No-Go Engine

[![CI](https://github.com/vassiliylakhonin/nonprofit-rbm-skill-for-claw-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/vassiliylakhonin/nonprofit-rbm-skill-for-claw-hub/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Decision-focused skill for turning incomplete nonprofit project inputs into a donor-aligned proposal package and a defensible submission verdict: **Go / Conditional Go / No-Go**.

## What this skill does

- Structures rough inputs into Concept, LOI, Full Proposal, Review, Donor-Fit, or Express outputs
- Enforces evidence discipline (facts vs assumptions vs hypotheses vs unknowns)
- Builds RBM / Theory of Change and measurement logic
- Stress-tests risk, safeguarding, and budget integrity
- Produces a transparent verification plan and readiness gate

## Install (OpenClaw)

```bash
clawhub install nonprofit-rbm-logic-model
```

## Codex variant

Use `codex/SKILL.md` for the same methodology in Codex skill workflows.

## Example prompts

- "Review this near-final proposal and give me a Go / Conditional Go / No-Go verdict."
- "Adapt this project to the UNICEF call and show donor-fit gaps."
- "Build an LOI from these rough notes with explicit evidence gaps."

## Output contract

1. Decision Summary
2. Facts / Assumptions / Hypotheses / Unknowns
3. Core Proposal Artifacts
4. Donor-Fit Matrix
5. Evidence and Traceability
6. Submission Readiness Checklist

## Repository structure

- `SKILL.md` — canonical OpenClaw skill specification
- `codex/SKILL.md` — Codex-ready skill variant
- `README.md` — overview and usage
- `.github/` — CI and contribution templates

## License

MIT
