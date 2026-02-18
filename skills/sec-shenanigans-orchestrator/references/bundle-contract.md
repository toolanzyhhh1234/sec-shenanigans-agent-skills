# Bundle Contract

Use these exact filenames and required fields so all skills interoperate.

## 1) `evidence-table.md`

Producer: `sec-filing-evidence-extractor`

Required columns:

- `evidence_id`
- `filing`
- `period`
- `location`
- `topic`
- `fact`
- `numbers`
- `trend`
- `initial_tags`
- `confidence`

## 2) `risk-register.md`

Producer: `sec-shenanigans-classifier`

Required columns:

- `risk_id`
- `category`
- `claim`
- `supporting_evidence_ids`
- `counter_evidence_ids`
- `confidence`
- `potential_impact`
- `next_checks`

## 3) `ratio-diagnostics.md`

Producer: `sec-red-flag-ratio-checks`

Required columns:

- `metric_id`
- `metric`
- `formula`
- `period_values`
- `anomaly_flag`
- `linked_risk_ids`
- `linked_categories`
- `interpretation`
- `confidence`

## 4) `shenanigans-memo.md`

Producer: `sec-shenanigans-memo-writer`

Required sections:

- `Executive Summary`
- `Risk Register Summary`
- `Evidence Highlights`
- `Ratio Diagnostics Summary`
- `Confidence and Uncertainty`
- `Diligence Priorities`

## 5) `open-questions.md`

Producer: `sec-shenanigans-memo-writer`

Required columns:

- `question_id`
- `question`
- `why_it_matters`
- `linked_risk_ids`
- `priority`
- `owner`

## Failure Rules

- If an input artifact is missing, stop and report the missing filename.
- If required fields are missing, produce a schema-gap list before proceeding.
