# Annotation Guidelines

## Objective
Evaluate AI-generated responses consistently for quality, factual accuracy, relevance, and instruction following.

## Labels
- **Pass**: Response satisfies the request and contains no material quality issue.
- **Fail**: Response contains a material factual, calculation, classification, relevance, or instruction-following issue.

## Dimensions
1. **Relevance** — Does the response directly address the user's request?
2. **Clarity** — Is it understandable, concise, and well structured?
3. **Factual accuracy** — Are factual claims correct and supported by the supplied context?
4. **Instruction following** — Does the response follow explicit constraints such as number of items, format, tone, or source-only requirements?

## Issue types
- No issue
- Factual error
- Calculation error
- Classification error
- Unsupported claim
- Instruction-following error
- Irrelevant/off-topic
- Incomplete answer

## Annotation principles
- Do not reward confident wording when the underlying claim is incorrect.
- If a source is explicitly provided, do not assume information that is absent from that source.
- Follow explicit user constraints over stylistic preferences.
- When uncertain, document the reason and use the evidence available in the prompt/source.
