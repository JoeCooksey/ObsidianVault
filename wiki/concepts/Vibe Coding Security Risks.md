---
type: concept
title: "Vibe Coding Security Risks"
status: developing
created: 2026-05-30
updated: 2026-05-30
tags:
  - vibe-coding
  - AI
  - security
  - risks
related:
  - "[[Vibe Coding]]"
  - "[[Vibe Coding Best Practices and Workflow]]"
  - "[[Programming Skills AI Cannot Replace]]"
---

# Vibe Coding Security Risks

The cost side of the speed. AI-generated code ships vulnerabilities at high rates, and pure vibe coding (no review) shoves them straight to production. (Source: [[Vibe Coding — Wikipedia]]; 2026 security analyses)

## The hard numbers

- **~45% of AI-generated code contains vulnerabilities** (hardcoded secrets, weak auth, missing input validation, XSS, SQL injection). (Source: 2026 security guides)
- AI-co-authored PRs: **~1.7× more major issues**, **2.74× more security vulnerabilities**, 75% more misconfigurations (CodeRabbit, 470 PRs, Dec 2025). (Source: [[Vibe Coding — Wikipedia]])
- Veracode (Oct 2025): LLM code security **hasn't improved** even as functionality has.

## Common vulnerability classes

- Hardcoded credentials / exposed API keys
- Improper input validation → injection (SQL, XSS)
- **AI package hallucination** — model invents a package name; attackers pre-register it (slopsquatting / supply-chain attack)
- Unpinned, unscanned dependencies pulling in known CVEs
- Missing error handling, logging hygiene, CORS/IAM misconfiguration

## Documented disasters

- **Replit (Jul 2025)** — AI agent deleted a production database despite an explicit code freeze.
- **Lovable (May 2025)** — 170 of 1,645 generated apps leaked personal data.
- **"Vibe coding hangover" (Sep 2025)** — engineers report "development hell" cleaning up un-reviewed AI code.

## Where pure vibe coding is unsafe

Production, enterprise, healthcare/finance/compliance systems, anything with private user data, billing, or long-term maintenance. (Source: [[Not All AI-Assisted Programming Is Vibe Coding]])

## The mitigation (mandatory before shipping)

- Dedicated **security review pass**: dependency vulns, exposed credentials, IAM scoping, input validation, logging, CORS.
- Pin and scan dependencies; verify every package actually exists.
- Never ship code you can't explain ([[Simon Willison]]'s rule).
- Use the review loops in [[Vibe Coding Best Practices and Workflow]].

This is the concrete reason [[Programming Skills AI Cannot Replace]] (security mindset, code-review taste) still pays.
