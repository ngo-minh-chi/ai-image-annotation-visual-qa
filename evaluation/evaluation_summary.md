# Evaluation Summary

## Review Dataset

This evaluation set contains four annotation review cases covering common quality issues.

| Case | Issue | Severity | Action | Status |
|---|---|---|---|---|
| review_001 | Incorrect object count | Major | Correct | Rejected |
| review_002 | Unsupported answer | Major | Revise answer | Rejected |
| review_003 | Low confidence | Minor | Adjust confidence | Needs review |
| review_004 | Correct annotation | None | Accept | Approved |

## Review Criteria

Annotations are evaluated based on:

- Object accuracy
- Object counting
- Evidence support
- Confidence calibration
- Consistency between annotation and visible content

## Quality Decision

Major issues require correction before acceptance.

Minor issues require review or adjustment.

Annotations that satisfy all quality criteria can be approved.
