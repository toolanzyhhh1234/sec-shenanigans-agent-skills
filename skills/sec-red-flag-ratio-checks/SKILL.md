---
name: sec-red-flag-ratio-checks
description: Run forensic ratio and trend checks from SEC filing data to validate or challenge Shenanigans hypotheses. Use when users ask for quantitative red-flag checks, earnings quality diagnostics, or quarter-over-quarter anomaly detection.
---
# SEC Red-Flag Ratio Checks

Use quick numeric diagnostics to support or refute classification claims.

## Workflow

1. Build a period-aligned dataset from filing evidence.
1. Compute core diagnostic ratios and deltas.
1. Compare directionality against management narrative.
1. Map anomalies to candidate Shenanigans categories.
1. Output findings with thresholds and caveats.

## Minimum Input Fields

- Revenue, gross profit, operating income, net income
- CFO/CFFO, CapEx, free cash flow proxy
- Accounts receivable, allowances, inventory, payables
- Capitalized costs, amortization/depreciation, impairments
- Acquisition-related adjustments and non-GAAP addbacks

## Output Format

- `metric`
- `formula`
- `period_values`
- `anomaly_flag` (`yes|no`)
- `linked_categories` (for example `EM1`, `EM4`, `CF3`)
- `interpretation`
- `confidence`

## Rules

- Emphasize trend breaks and divergence over single-point thresholds.
- Require at least 4 quarters for directional claims when possible.
- Report data quality issues explicitly.
- Avoid precision theater; round and focus on signal.

Read metric definitions in `references/forensic-metric-library.md`.
