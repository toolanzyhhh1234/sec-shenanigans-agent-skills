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

## Few-Shot Example

The following abbreviated evidence table shows correctly extracted rows from a hypothetical 10-Q. Use this as an anchor for format, granularity, and tone.

| evidence_id | filing | period | location | topic | fact | numbers | trend | initial_tags | confidence |
|---|---|---|---|---|---|---|---|---|---|
| EV-001 | 10-Q 2025-11-03 | Q3 FY2025 | Note 3 – Revenue Recognition | revenue | Company changed from point-in-time to over-time recognition for professional services contracts starting Q3 | n/a | one-off | EM1 | high |
| EV-002 | 10-Q 2025-11-03 | Q3 FY2025 | Balance Sheet, Note 5 | receivables | Gross AR rose 34% YoY while revenue grew 12%; allowance for doubtful accounts held flat at $4.2M (1.8% of AR vs 2.6% prior year) | AR $233M vs $174M; allowance $4.2M vs $4.5M | increase | EM1, EM5 | high |
| EV-003 | 10-Q 2025-11-03 | Q3 FY2025 | Cash Flow Statement | CFFO | CFO declined to $18M from $47M YoY; $22M increase in AR was the largest working-capital drag | CFO $18M vs $47M; AR drag -$22M | decrease | CF3 | medium |

Key points illustrated:
- Each row captures one disclosure fact, not a conclusion.
- Numbers are exact with units and comparative context.
- Tags are candidates only; classification happens downstream.
- The revenue-recognition policy change (EV-001) and the AR buildup (EV-002) are separate rows despite being related, preserving granularity.

## Output Handoff

Return:

1. Evidence table
1. Missing-data list (what was unavailable)
1. Ready-for-classification package keyed by `evidence_id`

For section anchors and filing hotspots, read `references/sec-filing-hotspots.md`.
