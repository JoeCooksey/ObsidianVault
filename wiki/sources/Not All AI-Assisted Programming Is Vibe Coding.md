---
type: source
source_type: blog
title: "Not All AI-Assisted Programming Is Vibe Coding"
author: "Simon Willison"
date_published: 2025-03-19
url: "https://simonwillison.net/2025/Mar/19/vibe-coding/"
confidence: high
created: 2026-05-30
updated: 2026-05-30
tags:
  - source
  - vibe-coding
  - AI
  - best-practices
status: stable
key_claims:
  - "Vibe coding = building with an LLM WITHOUT reviewing the code"
  - "Reviewed + tested + explainable code is software development, not vibe coding"
  - "Golden rule: don't commit code you can't explain to someone else"
related:
  - "[[Simon Willison]]"
  - "[[Vibe Coding]]"
  - "[[Vibe Coding Best Practices and Workflow]]"
---

# Not All AI-Assisted Programming Is Vibe Coding

The essay that fixed the precise meaning of "vibe coding" and separated it from professional AI-assisted engineering.

## What it contributes

**The narrow definition**: vibe coding is "building software with an LLM without reviewing the code it writes." Reviewing, testing, and being able to explain the code makes it *software development* — not vibe coding.

**When vibe coding is fine** (low stakes):
1. Low-harm projects (a bug costs little)
2. Throwaway weekend prototypes
3. Personal experiments to learn LLM capabilities
4. Sandboxed environments (e.g. Claude Artifacts) with no external access

**When to avoid it**:
- Production code others must understand
- Anything touching security, API keys, or private user data
- Anything with financial/billing exposure
- Tools given to non-experts without review

**Golden rule**: *"I won't commit any code to my repository if I couldn't explain exactly what it does to somebody else."*

**Upside**: democratizes programming for beginners; gives experts a risk-free lab to probe model limits.

## Confidence

High — primary-source opinion from a widely respected practitioner; the definition is now the de-facto industry standard (echoed by Wikipedia).
