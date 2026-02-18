# Forensic Metric Library

Use these checks as directional evidence, not standalone proof. Thresholds below are indicative ranges drawn from forensic accounting practice; always weigh them against industry context and the company's own history.

## Revenue and Receivables

- `DSO` = AR / Revenue * days
  - Rising DSO with stable growth can support `EM1` or `EM2`.
  - Threshold guidance: DSO increase >5 days QoQ or >15 days YoY without a disclosed business-model change is a moderate signal. A >10-day QoQ jump is a strong signal.
- `AR growth - Revenue growth` (spread)
  - Persistent positive spread suggests collection-quality issues.
  - Threshold guidance: spread >5pp for 2+ consecutive quarters is a moderate signal. Spread >10pp in any single quarter is a strong signal. Negative spread (AR shrinking faster than revenue) may indicate aggressive write-offs worth investigating for `EM5`.

## Earnings Quality

- `CFO / Net Income` (cash conversion ratio)
  - Sustained low conversion can support `EM3`, `EM4`, `EM5`.
  - Threshold guidance: ratio below 0.8x for 3+ consecutive quarters is a moderate signal. Below 0.5x in any quarter is a strong signal. Negative CFO with positive net income for 2+ quarters is a critical signal.
- `Accrual intensity` = (Net Income - CFO) / Total Assets
  - Rising accrual intensity supports deeper review.
  - Threshold guidance: absolute value >5% is elevated. Increase of >3pp YoY is a moderate signal. Values >10% or sustained increases over 3+ quarters are strong signals.

## Expense Deferral and Asset Quality

- `Capitalized costs / Revenue`
  - Step-ups may support `EM4`.
  - Threshold guidance: ratio increase >2pp YoY without a corresponding change in business mix is a moderate signal. Ratio exceeding industry median by >50% is a strong signal.
- `Amortization pace` = Amortization / Capitalized balance
  - Falling pace can indicate slower expense recognition (`EM4`).
  - Threshold guidance: pace decline >20% relative YoY is a moderate signal. Implied useful life increasing by >2 years without disclosed rationale is a strong signal.
- `Impairment timeliness`
  - Deteriorating business with low impairments can support `EM4`.
  - Threshold guidance: revenue or margin declines for 3+ quarters with zero impairment charges when capitalized intangibles/goodwill exceed 20% of total assets is a strong signal.

## Reserve Quality

- `Allowance coverage` = Allowance / AR (or NPL base)
  - Falling coverage during stress can support `EM5` or `KM2`.
  - Threshold guidance: coverage ratio decline >50bps QoQ during a period of rising delinquencies or macro stress is a moderate signal. Coverage hitting a 3-year low is a strong signal.
- `Warranty or restructuring reserve release vs earnings benefit`
  - Large releases may support `EM5`.
  - Threshold guidance: reserve release contributing >10% of pre-tax income in a quarter is a moderate signal. Release coinciding with an earnings-beat quarter where operating trends are weak is a strong signal.

## Cash Flow Presentation

- `CFO lift from working capital`
  - One-off working-capital boosts can support `CF3`.
  - Threshold guidance: working-capital contribution to CFO >30% of total CFO in a quarter is a moderate signal. Payables increase >20% QoQ without a matching revenue ramp, or receivables monetization/factoring appearing for the first time, is a strong signal.
- `Factoring / receivables monetization` = disclosed factoring volume / total AR
  - New or growing factoring programs can inflate CFFO by converting AR to cash without organic collection improvement.
  - Threshold guidance: factoring volume >10% of AR is a moderate signal for `CF1`. YoY increase in factoring volume >50% is a strong signal. Undisclosed or footnote-only mention of factoring when CFO is improving is a critical signal.
- `Operating outflow reclassification checks`
  - Cash costs moved to investing/financing can support `CF2`.
  - Threshold guidance: CapEx/Revenue ratio increasing >3pp YoY when the company is not in a disclosed investment cycle is a moderate signal for reclassification. Newly capitalized categories (e.g., implementation costs, content costs) appearing in investing that were historically in operating is a strong signal.
- `Borrowing-to-CFO proximity` = new borrowings or credit facility draws / reported CFO
  - When new debt proceeds approximate the period's CFO improvement, it can indicate financing inflows supporting operating cash optics.
  - Threshold guidance: ratio >0.5x in a quarter where CFO improved significantly is a moderate signal for `CF1`. Debt proceeds routed through working-capital accounts (e.g., paying down payables then re-drawing) is a strong signal.

## Acquisition Lens

- `Post-deal margin jump without matching cash conversion`
  - Can support `AA1` or `AA2`.
  - Threshold guidance: gross or operating margin improvement >3pp in the first 2 quarters post-close without a comparable CFO/Net Income improvement is a moderate signal. Margin improvement driven primarily by reduced amortization of acquired intangibles or purchase-accounting fair value adjustments is a strong signal.
- `Adjusted KPI outperformance vs weak GAAP trend`
  - Can support `AA3` and `KM1`.
  - Threshold guidance: adjusted metric growth exceeding GAAP equivalent by >10pp for 2+ quarters post-acquisition is a moderate signal. Introduction of new "pro forma" or "organic" metrics coinciding with acquisition close is a strong signal.
