---
type: concept
title: "Vibe Coding Best Practices and Workflow"
status: developing
created: 2026-05-30
updated: 2026-05-30
tags:
  - vibe-coding
  - AI
  - best-practices
  - workflow
  - methodology
related:
  - "[[Vibe Coding]]"
  - "[[Spec-Driven Development]]"
  - "[[Vibe Coding Security Risks]]"
  - "[[Multi-Agent Development Team]]"
---

# Vibe Coding Best Practices and Workflow

How to get production-grade results from AI coding agents and avoid the failure modes. (Source: Product Talk; 2026 best-practices guides)

## The Doom Loop (the failure to avoid)

The **doom loop** is when an agent repeatedly fails to fix the same bug. It happens when the three layers — **data, controller, view** — drift out of alignment, usually from unclear specs, frequent requirement changes leaving vestigial code, or mid-stream tech switches. (Source: Product Talk)

## Two core principles

1. **Plan for clarity** — the clearer the spec, the better the output. Iterate on requirements in **markdown**, not in code. → see [[Spec-Driven Development]].
2. **Manage the agent's mistakes** — agents err; your job is a systematic review process, not blind acceptance.

## The recommended loop: Plan-Review-Fix → Implement-Review-Fix

**Plan-Review-Fix**
1. Draft a detailed spec in markdown with one agent.
2. Have a **second agent review the plan** fresh, hunting gaps and logic flaws.
3. Iterate until aligned. (A lightweight version of [[Multi-Agent Development Team]].)

**Implement-Review-Fix**
1. Implement in a **fresh conversation** (clean context).
2. A **code-reviewer agent** checks the implementation against the plan.
3. Focus the review on three areas: **error handling, test coverage, security**.
4. Share *findings, not fixes* with the coding agent for collaborative repair.

## Concrete tactics

- **Start fresh conversations often** to avoid context rot.
- **Separate diagnosis from fixing**: tell the agent "diagnose and report back, don't fix" — only authorize changes after a confident root cause.
- **Use two agents on the same bug** and check they converge.
- **Wireframe first** (Figma/Whimsical/Miro) and feed screenshots to the builder.
- **Build incrementally** — treat outputs as drafts; never ask for the whole app at once.
- **Ask the agent to explain** unfamiliar concepts (turns coding into learning — ties to [[AI-Assisted Programming Learning Roadmap]]).

## The non-negotiable

Apply [[Simon Willison]]'s rule before anything ships: *don't commit code you can't explain.* Security review is mandatory — see [[Vibe Coding Security Risks]].
