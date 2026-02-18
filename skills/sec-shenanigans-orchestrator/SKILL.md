---
name: sec-shenanigans-orchestrator
description: Orchestrate end-to-end SEC forensic analysis by chaining evidence extraction, Shenanigans classification, ratio diagnostics, and memo generation. Use when users ask for a full pipeline run, complete diligence workflow, or one-command analysis.
---
# SEC Shenanigans Orchestrator

Coordinate the full analysis pipeline across the four component skills.

## Pipeline Order

1. Run `sec-filing-evidence-extractor` to build evidence table.
1. Run `sec-shenanigans-classifier` on extracted evidence.
1. Run `sec-red-flag-ratio-checks` for quantitative corroboration.
1. Run `sec-shenanigans-memo-writer` to produce final memo.

## Inputs

- Filing set (10-K/10-Q/8-K and optional earnings release exhibits)
- Analysis window (recommended: latest 8 quarters + latest annual)
- Optional focus areas (`revenue`, `cash flow`, `acquisition`, `non-GAAP`)
- Output depth (`quick`, `standard`, `deep`)

## Execution Contract

Use these handoff artifacts between stages.

- Stage 1 output: evidence table keyed by `evidence_id`
- Stage 2 output: risk register keyed by `risk_id` and linked `evidence_id`
- Stage 3 output: metric anomalies with linked categories and periods
- Stage 4 output: final memo with confidence and diligence questions

## Decision Rules

- If extraction confidence is mostly low, stop and request better filing inputs.
- If classification has only low-confidence risks, still produce watchlist memo.
- If metrics contradict high-confidence classifications, downgrade confidence and explain.
- If acquisition activity is material, prioritize `AA*` and `KM*` checks.

## Output Bundle

Return all artifacts in this order:

1. `evidence-table.md`
1. `risk-register.md`
1. `ratio-diagnostics.md`
1. `shenanigans-memo.md`
1. `open-questions.md`

For run profiles and stop conditions, read `references/pipeline-profiles.md`.
