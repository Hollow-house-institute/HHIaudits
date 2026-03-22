# LOCK STATE

## Package
GROK_HHI_AUDIT_30DAY

## Current State
Working / Governance-Controlled

## Lock Rules
- Human authority is final
- Terminology must remain aligned to canonical HHI terms
- Audit notes must remain distinguishable from model outputs
- Evidence must be preserved in chronological order where possible
- Checksums are generated after mutation, not before

## Mutation Policy
Allowed:
- Add new day files
- Add comparison notes
- Add summaries
- Refresh manifest when structure changes
- Regenerate checksums after updates

Not Allowed:
- Silent rewriting of historical outputs
- Mixing evaluator notes into model prompts during testing
- Replacing canonical authority references with ad hoc phrasing
