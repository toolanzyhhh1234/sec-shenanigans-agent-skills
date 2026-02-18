# Shenanigans Taxonomy for SEC Analysis

This reference is based on the Summary List and supported by chapter themes in Financial Shenanigans (4th ed.).

## Earnings Manipulation (EM)

- `EM1` Recording revenue too soon
  - Cues: earlier recognition policy, shipment timing games, acceptance risk ignored, extended terms with rising receivables.
- `EM2` Recording bogus revenue
  - Cues: related-party sales lacking substance, round-trips/barter, non-revenue cash presented as revenue.
- `EM3` Boosting income using one-time or unsustainable activities
  - Cues: gains and reclassifications mixed into recurring performance, serial “special” benefits.
- `EM4` Shifting current expenses to later periods
  - Cues: unusual capitalization, longer useful lives, slow amortization, weak impairment discipline.
- `EM5` Employing other techniques to hide expenses or losses
  - Cues: under-accruals, aggressive assumptions, reserve releases supporting earnings.
- `EM6` Shifting current income to later periods
  - Cues: cookie-jar reserve builds and smoothing behavior.
- `EM7` Shifting future expenses to current period
  - Cues: oversized current write-offs/restructuring to create easier future comps.

## Cash Flow (CF)

- `CF1` Shifting financing cash inflows to Operating
  - Cues: borrowings or receivable monetization presented as CFFO-like strength.
  - Behavioral detail: factoring or securitization programs that convert receivables to cash without organic collection; supply-chain financing where a bank pays the company early and collects from customers later; proceeds from sale-leaseback or insurance classified within operating; credit facility draws routed through working-capital accounts so that debt proceeds appear as reduced payables or increased collections.
  - Filing anchors: supplemental cash flow disclosures, liquidity footnotes, off-balance-sheet arrangements note, related-party transaction note (for captive financing).
- `CF2` Moving operating cash outflows to other sections
  - Cues: operating costs reclassified as investing/financing cash uses.
  - Behavioral detail: newly capitalizing costs that were previously expensed (software, content, contract fulfillment) so cash outflows shift from operating to investing; structuring vendor payments as financing arrangements; classifying implementation or integration costs as CapEx; lease restructuring that converts operating lease payments to financing lease payments.
  - Filing anchors: investing section of cash flow statement, capitalization policy note, software/content cost footnotes, lease obligation note, segment CapEx disclosures.
- `CF3` Boosting operating cash flow using unsustainable activities
  - Cues: temporary working-capital maneuvers, pulled-forward collections.
  - Behavioral detail: stretching payables (days payable outstanding increasing while vendor relationships are stable), pulling forward customer collections through early-pay discounts or quarter-end sweeps, timing of tax payments or insurance settlements, one-time beneficial working-capital swings from restructuring (e.g., inventory liquidation).
  - Filing anchors: working-capital components in cash flow statement, payables aging discussion in MD&A, customer concentration disclosures, quarterly DSO/DPO trends.

## Key Metrics (KM)

- `KM1` Showcasing misleading metrics that overstate performance
  - Cues: custom metrics without stable definition, selective exclusions, pro forma emphasis over GAAP.
- `KM2` Distorting Balance Sheet metrics to avoid showing deterioration
  - Cues: manipulated reserve/allowance/quality indicators hiding stress.

## Acquisition Accounting (AA)

- `AA1` Artificially boosting revenue and earnings
  - Cues: post-deal policy changes that accelerate revenue or suppress expense.
  - Behavioral detail: adopting the acquirer's more aggressive revenue recognition policy for the target's contracts; recording deferred revenue at fair value (haircut) so that future periods recognize "new" revenue from pre-existing contracts; reducing acquired warranty or return reserves to boost post-close margins; accelerating cost synergies into the purchase-accounting measurement period to inflate first reported combined earnings.
  - Filing anchors: purchase price allocation footnote, revenue recognition policy changes post-close, pro forma adjustments in the acquisition note, deferred revenue fair value adjustment disclosure.
- `AA2` Inflating reported cash flow
  - Cues: deal-structure or classification effects creating misleading operating cash optics.
  - Behavioral detail: structuring earnout payments as financing rather than operating outflows; pre-close settlement of target's payables funded by acquisition financing (removing a future operating outflow); classifying integration costs as investing activity; seller-financed deals where payments are structured as debt rather than operating expense.
  - Filing anchors: cash flow statement investing/financing sections in quarters around close, supplemental cash flow disclosures, earnout/contingent consideration footnote, integration cost disclosure.
- `AA3` Manipulating key metrics
  - Cues: acquisition-adjusted KPIs that mask organic weakness or integration costs.
  - Behavioral detail: introducing "organic growth" metrics that exclude the target's pre-acquisition baseline in a way that inflates apparent growth rate; reporting "adjusted EBITDA" that strips integration costs while including acquired revenue; changing cohort definitions, customer count methodology, or same-store metrics to absorb the target favorably; dropping or redefining pre-acquisition KPIs that would show deterioration in the legacy business.
  - Filing anchors: non-GAAP reconciliation tables, MD&A organic growth discussion, segment reporting changes, investor presentation KPI definitions vs. prior period definitions.

## SEC-Focused Distinction Rules

- Prefer `AA*` when deal timing is central to the signal.
- Prefer `KM*` when the core issue is metric design/definition rather than GAAP line items.
- Pair `EM4` with `CF2` when capitalization both lifts earnings and shifts cash presentation.
