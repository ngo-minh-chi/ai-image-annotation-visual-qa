# Annotation Quality Control

## 1. Purpose

This document defines the quality-control process used to review image annotations and visual question-answering data.

The main goals are:

- Maintain annotation accuracy.
- Ensure answers are supported by visible evidence.
- Detect ambiguous or misleading annotations.
- Keep labels and terminology consistent.
- Identify errors before final submission.

---

## 2. Quality Checks

Each annotation should be reviewed using the following checks:

### A. Object and Attribute Accuracy

Verify that:

- Objects described in the annotation are actually visible.
- Object counts are correct.
- Labels accurately represent the visible objects.
- Visual attributes such as color and lighting are supported by the image.

### B. Question and Answer Consistency

Verify that:

- The answer directly addresses the question.
- The answer is supported by visible evidence.
- No information is inferred without visual support.
- Yes/no questions contain an unambiguous answer.

### C. Evidence Quality

Evidence should:

- Describe observable visual information.
- Be concise and specific.
- Explain why the selected answer is correct.
- Avoid assumptions about information that cannot be seen.

### D. Confidence Review

Confidence should reflect the certainty of the annotation.

Suggested interpretation:

- 0.90–1.00: High confidence
- 0.75–0.89: Moderate confidence
- Below 0.75: Requires additional review

---

## 3. Ambiguity Handling

If an image or question is ambiguous:

1. Inspect the entire image.
2. Identify the relevant visual evidence.
3. Avoid unsupported assumptions.
4. Lower the confidence score when appropriate.
5. Flag the annotation for review if the ambiguity could affect the answer.

When the evidence is insufficient, the annotation should not be marked as fully verified.

---

## 4. Common Annotation Errors

The following errors should be checked during review:

- Incorrect object count.
- Incorrect object label.
- Missing visible objects.
- Incorrect color description.
- Unsupported visual attributes.
- Answers that do not match the question.
- Evidence that does not support the answer.
- Overconfident annotations.
- Confusing illustrations with photographs.
- Ignoring visible text in posters or images.

---

## 5. Review Workflow

For each annotation:

1. Inspect the complete image.
2. Read the question carefully.
3. Verify the relevant object or attribute.
4. Check the answer against visible evidence.
5. Review the confidence score.
6. Identify possible ambiguity.
7. Correct any detected issue.
8. Mark the annotation as verified only after review.

---

## 6. Annotation Status

The project uses the following annotation statuses:

- `verified` — Annotation has been reviewed and is supported by visual evidence.
- `needs_review` — Annotation contains uncertainty or a potential issue.
- `rejected` — Annotation contains a significant error and should not be used.

---

## 7. Final Quality Rule

An annotation should only be considered high quality when the label, answer, evidence, and confidence level are consistent with the visible content of the image.
