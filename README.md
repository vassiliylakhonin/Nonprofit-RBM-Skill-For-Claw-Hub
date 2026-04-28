# Nonprofit Proposal Go/No-Go Engine

[![ClawHub](https://img.shields.io/badge/ClawHub-nonprofit--rbm--logic--model-2bc6a4)](https://clawhub.ai/vassiliylakhonin/nonprofit-rbm-logic-model)
[![CI](https://github.com/vassiliylakhonin/nonprofit-rbm-skill-for-claw-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/vassiliylakhonin/nonprofit-rbm-skill-for-claw-hub/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Decision-grade nonprofit proposal engine for OpenClaw and Codex: donor-fit, RBM/Theory of Change, logframe, MEAL, safeguarding, evidence traceability, and Go / Conditional Go / No-Go submission gating.**

This skill turns messy nonprofit project inputs into a donor-aligned proposal package and a defensible submission decision. It is built for proposal teams that need stronger logic, clearer evidence gaps, and a realistic readiness verdict before spending scarce time on a weak submission.

## Why this skill exists

Nonprofit proposals often fail for avoidable reasons: weak donor fit, vague problem logic, unsupported targets, missing evidence, unclear MEAL, budget-risk mismatch, or polished language hiding structural gaps.

This skill enforces submission discipline:

- define the submission decision before drafting;
- separate **facts**, **assumptions**, **hypotheses**, **unknowns**, and **verdicts**;
- build RBM / Theory of Change logic before prose;
- show donor-fit gaps instead of pretending alignment;
- stress-test safeguarding, feasibility, budget logic, and evidence quality;
- end with a clear **Go / Conditional Go / No-Go** gate.

## Best for

- concept notes from rough project inputs;
- LOIs and first-stage donor submissions;
- full proposal skeletons and core sections;
- donor-call adaptation and fit analysis;
- RBM / Theory of Change / logframe / MEAL logic;
- near-final proposal reviews;
- safeguarding, risk, and budget-integrity stress tests;
- evidence and verification plans before submission.

## Not for

- inventing donor requirements, citations, baselines, targets, partners, or budget figures;
- making a weak proposal sound stronger than it is;
- legal, accounting, or compliance sign-off;
- funding-probability guarantees;
- generic copy-editing when the real problem is wording only.

## Output modes

| Mode | Use when you need | Typical output |
|---|---|---|
| **A — Concept** | Early-stage project idea | Concept note draft, proposal risks, evidence gaps, continue/stop recommendation |
| **B — LOI** | Short first-stage donor narrative | LOI-ready narrative, budget summary, feasibility and donor-fit flags |
| **C — Full Proposal** | Fuller submission package | Core sections, RBM/ToC, logframe, MEAL mini-plan, risks, verdict |
| **D — Review** | Existing draft needs a hard read | Diagnostic review, weaknesses, fix plan, Go / Conditional Go / No-Go |
| **E — Donor-Fit** | Adapt to a donor call | Alignment matrix, gaps against criteria, adaptation edits, evidence needs |
| **F — Express** | Severe time or information limits | Lean package, minimum logic chain, blockers, verification plan |

## What the skill always makes explicit

| Standard | How it appears |
|---|---|
| Submission framing | `Submission`, `Decision`, `Donor / Call`, `Audience`, `Geography / Population`, `Mode`, `Evidence mode` |
| Evidence discipline | `Fact`, `Assumption`, `Hypothesis`, `Unknown`, `Verdict` labels |
| Donor fit | Requirements, alignment, gaps, and unsupported claims |
| Logic quality | Problem → Activities → Outputs → Outcomes → Impact |
| Measurement | Indicators, baselines, targets, means of verification, cadence, owner — only where support exists |
| Readiness gate | **Go**, **Conditional Go**, or **No-Go** with reasons and required fixes |

## Installation

From ClawHub:

```bash
clawhub install nonprofit-rbm-logic-model
```

If installing directly from GitHub in OpenClaw:

```bash
openclaw skills install vassiliylakhonin/nonprofit-rbm-skill-for-claw-hub
```

## Codex usage

A Codex-ready variant is included at:

```text
codex/SKILL.md
```

Use that file in Codex skill workflows when you want the same proposal-review and submission-gating discipline outside OpenClaw.

## Example prompts

### Review a near-final proposal

```text
Use Nonprofit Proposal Go/No-Go Engine.
Review this near-final proposal and give me a Go / Conditional Go / No-Go verdict.
Focus on donor fit, evidence gaps, MEAL, safeguarding, budget logic, and blockers before submission.
```

### Adapt a project to a donor call

```text
Adapt this project to the UNICEF call.
Show donor-fit gaps, missing evidence, required changes, and whether we should proceed.
```

### Build an LOI from rough notes

```text
Build an LOI from these rough notes.
Mark assumptions and unknowns explicitly, and give me the minimum verification plan before submission.
```

### Stress-test proposal readiness

```text
Stress-test this proposal for logic, targets, safeguarding, implementation feasibility, and budget-risk mismatch.
End with a Conditional Go / No-Go gate.
```

## Recommended prompt shape

For best results, include the submission context:

```text
Use Nonprofit Proposal Go/No-Go Engine.
Donor / call: ...
Geography: ...
Target group: ...
Problem statement: ...
Intervention scope: ...
Budget envelope: ...
Timeline: ...
Implementing partners: ...
Requested mode: Concept / LOI / Full Proposal / Review / Donor-Fit / Express
Evidence mode: source-backed / reasoning-only / mixed
```

If two or more critical fields are missing, the skill should not produce a polished proposal. It should return blocking questions and an interim skeleton instead.

## Repository structure

```text
.
├── SKILL.md              # OpenClaw skill
├── codex/SKILL.md        # Codex-ready variant
├── README.md             # Public documentation
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
└── .github/              # CI and contribution templates
```

## Trust and safety posture

This skill is intentionally conservative. It should not invent citations, donor criteria, partner commitments, baselines, targets, compliance status, or budget figures. Unsupported claims are marked as evidence needs, not smoothed over with persuasive prose.

It is a proposal decision-support tool, not legal, accounting, compliance, or fundraising-success advice.

## License

MIT — see [LICENSE](LICENSE).
