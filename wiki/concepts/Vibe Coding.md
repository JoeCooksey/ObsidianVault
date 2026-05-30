---
type: concept
title: "Vibe Coding"
status: developing
created: 2026-05-30
updated: 2026-05-30
tags:
  - vibe-coding
  - AI
  - programming
  - methodology
related:
  - "[[Andrej Karpathy]]"
  - "[[Simon Willison]]"
  - "[[Spec-Driven Development]]"
  - "[[Vibe Coding Tool Landscape 2026]]"
  - "[[Vibe Coding Best Practices and Workflow]]"
  - "[[Vibe Coding Security Risks]]"
  - "[[AI-Assisted Programming Learning Roadmap]]"
---

# Vibe Coding

**Vibe coding** is AI-assisted development where you describe what you want in natural language and an LLM generates the code — in its purest form, accepting that code with minimal review and steering by results and follow-up prompts rather than by reading every line. Coined by [[Andrej Karpathy]] in February 2025. (Source: [[Vibe Coding — Wikipedia]])

> Karpathy: "fully give in to the vibes, embrace exponentials, and forget that the code even exists."

## The spectrum (this is the key mental model)

Vibe coding sits at one end of a spectrum. [[Simon Willison]] drew the line: (Source: [[Not All AI-Assisted Programming Is Vibe Coding]])

| | **Pure vibe coding** | **AI-assisted engineering** |
|---|---|---|
| Review the code? | No | Yes |
| Can you explain it? | Don't care | Required |
| Good for | toys, prototypes, learning | production, anything you sell |
| Risk | high if shipped | managed |

Willison's rule: *if you reviewed, tested, and can explain it, that's not vibe coding — it's software development.* The disciplined version of "vibe coding for real projects" is actually [[Spec-Driven Development]].

## When pure vibe coding is appropriate

Low-stakes, throwaway, sandboxed, or learning contexts. **Not** for production, security/keys, private data, or billing. (Source: [[Not All AI-Assisted Programming Is Vibe Coding]])

## Why it matters now

- Collins **Word of the Year 2025**; **25% of YC Winter 2025 startups** had 95% AI-generated codebases. (Source: [[Vibe Coding — Wikipedia]])
- Lowers the floor: beginners ship working things; experts move faster on scaffolding.
- But AI-co-authored code shows **~1.7× more major issues** — speed is not free. See [[Vibe Coding Security Risks]].

## For Joe specifically

Use pure vibe coding to **learn fast and prototype**; graduate anything real to [[Spec-Driven Development]] with review. This is the practical edge of [[Permissionless Leverage]] (code leverage) and the engine behind [[Profitable Micro-SaaS Playbook]]. Builds on [[AI-Assisted Programming Learning Roadmap]] and the cautions in [[Programming Skills AI Cannot Replace]].
