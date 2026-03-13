#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_KEYS = [
    "theory_of_change",
    "executive_summary",
    "logic_model",
    "outcome_indicators",
    "sdg_alignment",
    "monitoring_plan",
    "assumptions_risks_mitigations",
]


def load(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def evaluate(doc: dict) -> dict:
    missing = [k for k in REQUIRED_KEYS if k not in doc]

    lm = doc.get("logic_model", {}) or {}
    levels = ["inputs", "activities", "outputs", "outcomes", "impact"]
    missing_levels = [lvl for lvl in levels if lvl not in lm]

    inds = doc.get("outcome_indicators", []) or []
    indicator_count = 0
    if isinstance(inds, list):
        for x in inds:
            if isinstance(x, dict) and isinstance(x.get("indicators"), list):
                indicator_count += len(x["indicators"])

    score = 100
    score -= min(40, len(missing) * 6)
    score -= min(20, len(missing_levels) * 4)
    if indicator_count < 3:
        score -= 20
    if indicator_count < 1:
        score -= 20
    score = max(0, score)

    if score >= 85 and not missing and not missing_levels and indicator_count >= 3:
        verdict = "Pass"
    elif score >= 65:
        verdict = "Conditional Pass"
    else:
        verdict = "Fail"

    return {
        "score": score,
        "verdict": verdict,
        "missing_sections": missing,
        "missing_logic_model_levels": missing_levels,
        "indicator_count": indicator_count,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic RBM quality gate")
    ap.add_argument("--input", required=True, help="Path to RBM JSON output")
    ap.add_argument("--out", default="", help="Optional output file")
    args = ap.parse_args()

    result = evaluate(load(args.input))
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
