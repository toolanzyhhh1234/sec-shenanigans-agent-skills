---
name: sec-shenanigans-classifier
description: Classify SEC filing evidence using Financial Shenanigans taxonomy (EM1-7, CF1-3, KM1-2, AA1-3) and produce confidence-scored risk calls. Use when users ask to detect accounting tricks, map red flags to categories, or assess manipulation risk.
---
# SEC Shenanigans Classifier

Classify only after evidence extraction. Produce falsifiable, evidence-linked calls.

## Workflow

1. Load evidence rows and preserve `evidence_id` lineage.
1. Map each row to candidate categories from taxonomy.
1. Require corroboration before high-confidence calls.
1. Distinguish aggressive-but-allowed accounting from probable manipulation.
1. Produce a risk register with confidence and rebuttal conditions.

## Corroboration Standard

Use these confidence gates.

- `high`: at least 2 independent indicators, one numeric trend and one disclosure/definition signal.
- `medium`: one strong indicator with incomplete corroboration.
- `low`: weak or ambiguous signal; keep as watchlist.

Do not mark `high` if the signal can be explained by disclosed business model changes without contradiction.

## Classification Output Schema

- `risk_id`
- `category`: one of `EM1..EM7`, `CF1..CF3`, `KM1..KM2`, `AA1..AA3`
- `claim`: precise manipulation hypothesis
- `supporting_evidence_ids`: list
- `counter_evidence_ids`: list or empty
- `confidence`: `high|medium|low`
- `potential_impact`: earnings/cash flow/valuation/multiple
- `next_checks`: concrete follow-up tests

## Judgment Rules

- Prefer specific category call over generic “aggressive accounting.”
- Allow multi-tagging when one action affects earnings and cash flow.
- Treat KPI definition changes as potential `KM1` until reconciled.
- Treat post-acquisition accounting policy shifts as potential `AA1`/`AA3` by default.
- Escalate to watchlist instead of forcing conviction.

Read taxonomy details in `references/shenanigans-taxonomy.md`.
