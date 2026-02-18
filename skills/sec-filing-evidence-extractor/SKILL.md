---
name: sec-filing-evidence-extractor
description: Extract structured forensic evidence from SEC filings (10-K, 10-Q, 8-K, S-1 proxy appendices) for accounting-quality analysis. Use when a user asks to review filings, gather red flags, or prepare inputs for Shenanigans classification.
---
# SEC Filing Evidence Extractor

Extract evidence before drawing conclusions. Favor traceable, section-anchored facts over narrative summaries.

## Workflow

1. Identify filing set and periods.
1. Prefer at least 8 quarters plus latest annual filing when available.
1. Extract facts into a normalized evidence table.
1. Keep every row tied to a filing, period, and location anchor.
1. Flag uncertain interpretation explicitly instead of forcing classification.

## Evidence Table Schema

Use this schema in Markdown or CSV.

- `evidence_id`: stable id (for example `EV-001`)
- `filing`: form + date (for example `10-Q 2025-11-03`)
- `period`: fiscal period covered
- `location`: section/footnote anchor
- `topic`: revenue, receivables, reserves, CFFO, non-GAAP, acquisitions, etc.
- `fact`: concise paraphrase of disclosure
- `numbers`: raw numbers with units and sign
- `trend`: increase/decrease/flat/volatile/one-off
- `initial_tags`: optional candidate tags (`EM4`, `CF2`, `AA1`, etc.)
- `confidence`: `high|medium|low` for extraction accuracy only

## Extraction Priorities

Prioritize sections most likely to contain manipulative reporting clues.

1. Revenue recognition policy and contract assets/liabilities notes
1. Accounts receivable, allowance, DSO-related disclosures
1. Capitalized costs, deferred costs, useful lives, impairment
1. Restructuring, contingencies, reserves, and releases
1. Statement of cash flows plus supplemental cash disclosures
1. Non-GAAP reconciliations and KPI definition changes
1. Acquisition accounting, purchase price allocation, pro forma metrics

## Quality Rules

- Separate disclosure facts from interpretation.
- Keep quote snippets short; prefer paraphrase with exact numbers.
- Normalize sign conventions for cash flow and expenses.
- Capture definition changes in KPIs as separate evidence rows.
- If wording is ambiguous, add a `low` extraction confidence row and continue.

## Output Handoff

Return:

1. Evidence table
1. Missing-data list (what was unavailable)
1. Ready-for-classification package keyed by `evidence_id`

For section anchors and filing hotspots, read `references/sec-filing-hotspots.md`.
