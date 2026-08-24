# Prompt Adherence Benchmark

## Purpose

This benchmark evaluates whether a generated image follows the explicit requirements stated in a visual generation prompt.

The evaluation focuses on observable evidence rather than subjective artistic preference.

## Evaluation Criteria

Each generated image is evaluated across five dimensions:

| Criterion | Description | Score |
|-----------|-------------|------:|
| Subject adherence | Required subjects are present | 0–2 |
| Attribute adherence | Required attributes are correct | 0–2 |
| Composition adherence | Required arrangement is respected | 0–2 |
| Style adherence | Requested visual style is followed | 0–2 |
| Overall adherence | Overall prompt compliance | 0–2 |

### Scoring

- `2` = Clearly satisfies the requirement
- `1` = Partially satisfies the requirement
- `0` = Does not satisfy the requirement

Maximum score: **10**

---

# Evaluation Case 001 — Stylized Faces

## Prompt

Create a contemporary abstract figurative artwork containing multiple stylized faces arranged vertically, using a vibrant and varied color palette with embossed texture.

## Required Attributes

- Multiple stylized faces
- Vertical arrangement
- Vibrant color palette
- Embossed texture
- Contemporary abstract figurative style

## Evaluation

| Criterion | Score | Evidence |
|-----------|------:|----------|
| Subject adherence | 2 | Multiple stylized faces are clearly visible. |
| Attribute adherence | 2 | The artwork uses multiple vivid colors and visible facial features. |
| Composition adherence | 2 | Faces are arranged across the vertical composition. |
| Style adherence | 2 | The image has a contemporary abstract figurative appearance. |
| Overall adherence | 2 | The major prompt requirements are satisfied. |

**Total Score: 10/10**

**Verdict: PASS**

---

# Evaluation Case 002 — Samurai Android

## Prompt

Create a futuristic samurai android wearing glossy black segmented puffer-style armor, with a metallic helmet and a strong red background.

## Required Attributes

- Samurai-inspired character
- Android / humanoid character
- Glossy black puffer-style armor
- Metallic helmet
- Red background

## Evaluation

| Criterion | Score | Evidence |
|-----------|------:|----------|
| Subject adherence | 2 | A humanoid futuristic character is clearly visible. |
| Attribute adherence | 2 | Black glossy segmented armor and metallic helmet are visible. |
| Composition adherence | 2 | Character is centered prominently in the image. |
| Style adherence | 2 | Futuristic samurai aesthetic is clearly represented. |
| Overall adherence | 2 | The required visual elements are present. |

**Total Score: 10/10**

**Verdict: PASS**

---

# Evaluation Case 003 — Movie Poster

## Prompt

Create a cinematic movie poster with a cool color palette, pink headline text, turquoise/cyan hair, and a person shown in profile.

## Required Attributes

- Movie poster composition
- Pink headline text
- Turquoise/cyan hair
- Profile view
- Cool color palette

## Evaluation

| Criterion | Score | Evidence |
|-----------|------:|----------|
| Subject adherence | 2 | A person is clearly shown in profile. |
| Attribute adherence | 2 | Cyan/turquoise hair and pink typography are visible. |
| Composition adherence | 2 | The image follows a recognizable movie-poster layout. |
| Style adherence | 2 | The overall visual treatment is cinematic and cool-toned. |
| Overall adherence | 2 | The major prompt requirements are satisfied. |

**Total Score: 10/10**

**Verdict: PASS**

---

# Evaluation Case 004 — Ambiguous Requirement

## Prompt

Create an image containing a person and a laptop.

## Evaluation Scenario

The generated image contains a person and a laptop, but the laptop is partially obscured.

| Criterion | Score | Evidence |
|-----------|------:|----------|
| Subject adherence | 2 | A person is clearly visible. |
| Attribute adherence | 1 | The laptop is visible but partially obscured. |
| Composition adherence | 1 | Both subjects are present but the laptop is not fully visible. |
| Style adherence | 2 | No style conflict is observed. |
| Overall adherence | 1 | The prompt is mostly satisfied but visibility is limited. |

**Total Score: 7/10**

**Verdict: REVIEW**

## Reason

The required object is present, but the visual evidence is insufficient for a fully confident pass.

This case demonstrates ambiguity handling and conservative evaluation.

---

# Reviewer Rules

A reviewer should:

1. Read the prompt before judging the image.
2. Identify explicit requirements.
3. Evaluate only observable visual evidence.
4. Avoid rewarding details that were not requested.
5. Avoid penalizing artistic choices that do not violate the prompt.
6. Separate objective prompt adherence from subjective image quality.
7. Flag ambiguous cases for additional review.
8. Use conservative scoring when evidence is unclear.

## Final Decision

Suggested decision thresholds:

- `9–10` → PASS
- `7–8` → REVIEW
- `0–6` → FAIL

The final decision should always consider whether any critical requirement was completely missed.
