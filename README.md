# SEC Shenanigans Agent Skills

Reusable skills for SEC filing forensic analysis, based on the Shenanigans taxonomy:

- Earnings Manipulation (`EM1-EM7`)
- Cash Flow (`CF1-CF3`)
- Key Metric (`KM1-KM2`)
- Acquisition Accounting (`AA1-AA3`)

This repository follows the `vercel-labs/skills` repository format (`skills/<skill-name>/SKILL.md`) so it can be installed across multiple agent harnesses.

## Included Skills

- `sec-filing-evidence-extractor`
- `sec-shenanigans-classifier`
- `sec-red-flag-ratio-checks`
- `sec-shenanigans-memo-writer`
- `sec-shenanigans-orchestrator`

## Install with Skills CLI

From a published GitHub repo:

```bash
npx skills add <owner>/sec-shenanigans-agent-skills --skill '*'
```

From local path:

```bash
npx skills add ./sec-shenanigans-agent-skills --skill '*'
```

Install to specific harnesses only:

```bash
npx skills add <owner>/sec-shenanigans-agent-skills --skill '*' -a codex -a claude-code
```

Install globally:

```bash
npx skills add <owner>/sec-shenanigans-agent-skills --skill '*' -g
```

List skills before install:

```bash
npx skills add <owner>/sec-shenanigans-agent-skills --list
```

## Recommended Usage Order

1. `sec-filing-evidence-extractor`
2. `sec-shenanigans-classifier`
3. `sec-red-flag-ratio-checks`
4. `sec-shenanigans-memo-writer`

Or run end-to-end with:

- `sec-shenanigans-orchestrator`

## Repository Structure

```text
sec-shenanigans-agent-skills/
  skills/
    sec-filing-evidence-extractor/
    sec-shenanigans-classifier/
    sec-red-flag-ratio-checks/
    sec-shenanigans-memo-writer/
    sec-shenanigans-orchestrator/
```
