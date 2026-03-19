---
name: nonprofit-impact-orchestra
description: Generate donor-ready nonprofit project packages for grants, concept notes, logframes, MEAL plans, budgets, safeguarding reviews, and funder adaptation. Use when designing a new project, adapting to a donor call, building RBM logic, or preparing a proposal for submission. Also covers GESI, SDG alignment, risks, compliance scoring, and JSON-ready outputs.
homepage: https://clawhub.ai/u/vassiliylakhonin
user-invocable: true
metadata: {"openclaw":{"emoji":"🎼","os":["linux","darwin","win32"]}}
---

# Nonprofit Impact Orchestra

Turn rough nonprofit ideas, donor calls, or messy draft proposals into
clear, donor-ready project packages.

Use this skill to go from:
- idea → concept note
- concept → logframe and MEAL plan
- draft → donor-adapted proposal
- proposal → peer review and compliance check

## Quick Start

Install:

```bash
clawhub install nonprofit-impact-orchestra
Start with a rough project idea:

text
orchestra Youth-led reconstruction and green skills training in war-affected regions of Ukraine, €180k, 18 months, partners: local civil society and EU-linked actors
Start with a donor call:

text
orchestra --cfp [paste funding call text]
Review a draft before submission:

text
orchestra --peer-review [paste proposal text]
Best For
This skill is especially useful for:

NGO program designers

grant writers

nonprofit consultants

fundraising teams

program managers preparing donor submissions

teams that need one workflow for concept, budget, compliance, and narrative

Quick Reference
If you need...	Use...
A full project package from a rough idea	orchestra [project description]
A fast first draft	orchestra --express [description]
A concept note only	orchestra --concept [description]
An LOI / EOI	orchestra --loi [description]
Donor adaptation from a real call	orchestra --cfp [paste donor call]
A review of an existing proposal	orchestra --review [paste draft]
A donor-style scoring simulation	orchestra --peer-review [paste draft]
A donor comparison	orchestra --compare donor [A] vs [B] for [project]
A structured export	orchestra --json [description]
What You Get
Depending on the request, this skill can produce:

Elevator pitch

Executive summary

Concept note

Problem statement

Strategic context

Stakeholder map

RBM chain

Theory of Change

Logframe matrix

SMART indicators

MEAL plan

GESI analysis

SDG alignment

Safeguarding / Do No Harm checklist

Budget breakdown

Co-financing summary

Sustainability and exit strategy

Partnership structure

Donor adaptation notes

Risk matrix and scenarios

Human impact narrative

Compliance score

Confidence report

JSON export block

When to Use
Use this skill when the user needs:

A grant proposal from scratch

A concept note, LOI, or EOI

A logframe or Theory of Change

A MEAL plan

A donor-ready budget

GESI integration

Safeguarding review

A funder-adapted narrative

A submission-readiness check

Modes
text
orchestra [project description]
orchestra --express [description]
orchestra --cfp [paste donor call text]
orchestra --concept [description]
orchestra --loi [description]
orchestra --review [paste proposal text]
orchestra --peer-review [paste proposal text]
orchestra --compare [project A] vs [project B]
orchestra --compare donor [Funder A] vs [Funder B] for [project]
orchestra --from=context
orchestra --from=logic
orchestra --from=budget
orchestra --from=donor-adapt
orchestra --from=final
orchestra [description] --audience=donor
orchestra [description] --audience=board
orchestra [description] --audience=community
orchestra [description] --lang=fr
orchestra --json [description]
orchestra --excel-ready [description]
orchestra --donor-fit [description]
Intake Template
text
Project name:     |
Location/country: |
Target group:     |
Problem:          |
Goal/impact:      |
Budget:           |
Duration:         |
Partners:         |
Donor/funder:     | (name, CFP link, or "unknown")
Audience:         | (donor / board / community)
Language:         | (default: English)
Need now:         | (full package / concept note / budget / review / donor adaptation)
Free-form input also works. Ask follow-up questions only if missing
details would block a useful result.

Core Rules
text
1. Be donor-ready, but do not fake certainty.
2. Preserve realism over grandiosity.
3. Flag weak or unverifiable claims clearly.
4. Ask only the minimum number of blocking questions.
5. Prefer structured outputs over long prose.
6. Keep language natural and human.
7. Build for implementation, not only for approval.
8. Never fabricate baselines, evidence, partner commitments, or donor fit.
Confidence Labels
text
[HIGH]       — verified or widely supported
[MEDIUM]     — plausible but incomplete
[UNVERIFIED] — manual check required before submission
Use these labels whenever evidence is uncertain.

Workflow
Step 1 — Parse and Scope

Extract:

text
- project name
- location
- target group
- problem
- intended impact
- budget and duration
- partners
- donor or funder
- audience and language
- required output type
Depth by budget:

text
< $50k       → lighter package
$50k–$500k   → full standard package
> $500k      → add procurement, audit trail, and financial risk logic
Step 2 — Strategic Context

Produce:

text
- problem framing
- stakeholder mapping
- key drivers
- assumptions
- initial risks
- short PESTLE if useful
If --cfp is used, extract:

text
- donor priorities
- eligibility signals
- required structure
- compliance expectations
- red flags and likely gaps
Step 3 — Program Logic

Build:

text
- RBM chain
- Theory of Change narrative
- logframe matrix
- SMART indicators
- assumptions
- baselines and targets where possible
Use a simple ToC diagram when useful:

text
graph LR
  Inputs --> Activities --> Outputs --> Outcomes --> Impact
Step 4 — MEAL, GESI, SDG

Generate:

text
- MEAL plan
- accountability and feedback logic
- learning loop
- GESI analysis
- SDG alignment
At minimum, GESI should consider:

text
- women and girls
- youth
- people with disabilities
- minorities or excluded groups
Step 5 — Safeguarding and Do No Harm

Output:

text
Area | Status | Recommended Action
Review at minimum:

text
- environmental screening
- PSEA / safeguarding
- conflict sensitivity / Do No Harm
- data protection and privacy
- community consent and feedback
Status values:

text
✅ Clear | ⚠️ Review needed | ❌ Missing
Step 6 — Budget and Delivery Logic

If budget detail is requested, provide:

text
- personnel
- travel
- equipment
- training
- operations/admin
- contingency
- co-financing if relevant
Useful formulas when needed:

text
=SUM(B2:B10)
=IF(admin/total>0.15,"FLAG","OK")
=B2*exchange_rate
Flag:

text
- high admin share
- weak co-financing
- missing procurement logic
- missing audit trail for larger budgets
Step 7 — Draft and Adapt

Draft:

text
- problem statement
- objectives
- key activities
- implementation logic
- sustainability / exit strategy
- partnership structure
If a donor is named, adapt:

text
- framing
- vocabulary
- emphasis
- structure
- likely compliance expectations
Use labels:

text
[Known guidelines]
[Inferred from public sources]
Step 8 — Final Readiness Check

Produce:

text
- risk matrix
- mitigation actions
- 4 scenarios
- early warning indicators
- 200–300 word human impact narrative
- compliance score
- confidence report
- final delivery package
Default Delivery Package
text
00. Elevator Pitch
01. Executive Summary
02. Concept Note (if requested)
03. Strategic Context
04. Stakeholder Mapping
05. GESI Analysis
06. Safeguarding / Do No Harm Checklist
07. RBM Chain
08. Theory of Change
09. Theory of Change Diagram
10. Logframe Matrix
11. MEAL Plan
12. SDG Alignment
13. Budget Table
14. Co-financing Summary
15. Sustainability / Exit Strategy
16. Partnership Structure
17. Donor Adaptation Notes
18. Risk Matrix and Scenarios
19. Human Impact Narrative
20. Compliance Score
21. Confidence Report
22. Sources / Traceability Notes
23. JSON Export Block
Compliance Score
End with a readiness check like:

text
Compliance Score: XX/100

✅ GESI indicators present
✅ SDG alignment mapped
✅ Safeguarding covered
⚠️ Admin cap needs review
⚠️ Sustainability section needs strengthening
❌ Partner MoU missing
Output Style
text
donor      → formal, evidence-based, results-oriented
board      → concise, strategic, impact-focused
community  → plain-language, accessible, human
Final polish should:

text
- remove repetitive AI phrasing
- improve readability
- preserve meaning
- keep the tone credible and practical
JSON Output
json
{
  "project": {},
  "elevator_pitch": "",
  "executive_summary": "",
  "concept_note": "",
  "strategic_context": {},
  "stakeholders": [],
  "rbm_chain": {},
  "theory_of_change": {},
  "logframe": [],
  "meal_plan": [],
  "gesi_analysis": {},
  "safeguarding": {},
  "budget": {},
  "co_financing": {},
  "sustainability": {},
  "partnerships": {},
  "donor_adaptation": {},
  "risks": [],
  "scenarios": [],
  "sdg_alignment": [],
  "narrative": "",
  "compliance_score": {},
  "confidence_report": {},
  "sources": []
}
Limits
This skill does not:

guarantee donor approval

replace legal or financial review

verify external statistics automatically

justify fabricated baselines or impact claims

If information is weak, flag it clearly instead of overclaiming.

Quick Tips
Use --cfp whenever the real donor call is available.

Run --peer-review before submission.

Use --donor-fit when deciding whether to pursue a specific funder.

Use --excel-ready when the next step is budget editing.

Verify every [UNVERIFIED] claim before submission.

Keep sustainability as strong as the problem statement.

Do not skip GESI, safeguarding, or accountability sections.

Author
Vassiliy Lakhonin