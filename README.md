# Nonprofit Impact Orchestra (OpenClaw Skill)

`nonprofit-impact-orchestra` helps NGO and nonprofit teams turn rough ideas, donor calls, or draft proposals into donor-ready project packages.

## What this skill does

- Builds concept notes, LOI/EOI drafts, and full proposal packages
- Produces RBM chain, Theory of Change, and logframe matrix
- Generates MEAL plan, GESI analysis, SDG alignment, and safeguarding checks
- Drafts budget structure, co-financing summary, and delivery logic
- Runs donor adaptation and peer-review style readiness scoring

## Install

```bash
clawhub install nonprofit-impact-orchestra
```

## Quick usage

```text
orchestra Youth-led reconstruction and green skills training in war-affected regions of Ukraine, €180k, 18 months, partners: local civil society and EU-linked actors
```

```text
orchestra --cfp [paste donor call text]
```

```text
orchestra --peer-review [paste proposal draft]
```

## Common modes

- `orchestra [description]` — full package
- `orchestra --express [description]` — fast first draft
- `orchestra --concept [description]` — concept note only
- `orchestra --loi [description]` — LOI/EOI draft
- `orchestra --review [draft]` — proposal quality review
- `orchestra --peer-review [draft]` — donor-style scoring simulation
- `orchestra --json [description]` — structured JSON output

## Typical outputs

1. Elevator pitch + executive summary
2. Strategic context + stakeholder mapping
3. RBM chain + Theory of Change + logframe
4. Indicator set + MEAL plan
5. GESI + safeguarding / Do No Harm checks
6. SDG alignment
7. Budget table + co-financing summary
8. Risk matrix, scenarios, compliance score, and confidence report

## Repository structure

```text
.
├── SKILL.md
├── README.md
└── LICENSE
```

## License

MIT
