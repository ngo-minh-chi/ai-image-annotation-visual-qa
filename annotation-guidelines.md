# Image Annotation & Visual QA Guidelines

## 1. Purpose

This project demonstrates a structured workflow for image annotation and visual quality evaluation.

Annotators should answer questions based only on information that is visibly present in the image.

---

## 2. Core Principles

### 2.1 Use visible evidence only

Do not infer information that cannot be directly observed.

Example:

If an image shows a person wearing a dark shirt, do not assume the shirt is black unless the color is clearly identifiable.

### 2.2 Do not use outside knowledge

Annotations should be based on the image itself rather than external information.

### 2.3 Maintain consistent labels

Use the same terminology for similar objects, colors, and attributes throughout the dataset.

### 2.4 Handle ambiguity explicitly

If an image does not provide enough evidence to determine the answer confidently, mark the annotation as uncertain.

### 2.5 Prioritize accuracy over guessing

When evidence is unclear, it is better to mark an item as uncertain than to provide an unsupported answer.

---

# 3. Annotation Fields

Each annotation contains:

- Image ID
- Question
- Answer
- Confidence
- Evidence
- Issue
- Issue Severity

---

# 4. Confidence Levels

## High

The answer is directly visible and unambiguous.

## Medium

The answer is visible but there is some minor ambiguity.

## Low

The image does not provide enough reliable evidence.

---

# 5. Issue Types

## None

No issue is present.

## Ambiguous

The image is unclear or does not provide enough evidence.

## Occluded

The relevant object is partially blocked.

## Low Quality

The image is too blurry, dark, distorted, or otherwise difficult to inspect.

## Inconsistent

The annotation does not follow the project labeling rules.

---

# 6. Severity

## Major

The issue causes the annotation to be incorrect or unusable.

Examples:

- Wrong object
- Wrong answer
- Hallucinated object
- Major misunderstanding of the image

## Minor

The annotation is mostly correct but contains a small issue.

Examples:

- Slightly inconsistent terminology
- Minor formatting issue
- Incomplete description

---

# 7. Annotation Procedure

For each image:

1. Inspect the entire image.
2. Identify the relevant object or attribute.
3. Read the question carefully.
4. Answer using visible evidence only.
5. Assign a confidence level.
6. Record supporting visual evidence.
7. Identify any potential issue.
8. Assign severity when necessary.
9. Review the annotation before submission.

---

# 8. Quality Rule

Never guess when the visual evidence is insufficient.

A correct "uncertain" label is preferable to an unsupported answer.
