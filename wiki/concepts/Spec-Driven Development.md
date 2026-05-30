---
type: concept
title: "Spec-Driven Development"
status: developing
created: 2026-05-30
updated: 2026-05-30
tags:
  - AI
  - programming
  - methodology
  - spec-driven
  - claude-code
related:
  - "[[Vibe Coding]]"
  - "[[Vibe Coding Best Practices and Workflow]]"
  - "[[Multi-Agent Development Team]]"
---

# Spec-Driven Development

**Spec-Driven Development (SDD)** is the disciplined, production-grade end of the [[Vibe Coding]] spectrum: instead of prompting straight into code, you write the spec first and have the AI build against it, with a human review between every step. (Source: 2026 Claude Code / Towards Data Science guides)

## The three-document workflow

SDD is a methodology, not a tool. It runs on three artifacts, in order, with review between each:

1. **What** — a document stating what the change should do (the PRD / requirements).
2. **Plan** — the steps to get there.
3. **Code** — written against the plan.

Human review sits between each pair. This is the structured cure for the **doom loop** (see [[Vibe Coding Best Practices and Workflow]]).

## Why it beats pure vibe coding for real projects

- Clear specs → far better output and far less rework.
- The spec becomes durable documentation.
- It enforces [[Simon Willison]]'s rule (you understand what ships).

## Claude Code's native SDD support (2026)

The tool this vault runs on absorbs most SDD tooling natively: (Source: 2026 guides)

- **CLAUDE.md** — the "project constitution"; encodes conventions, standards, and PRD constraints so the agent follows them without constant reminders.
- **Subagents** — parallel research and review from fresh perspectives.
- **Ask-user-question / interview pattern** — refines requirements before coding.
- **Tasks system** — delegates implementation with dependency ordering and atomic commits.
- Large context windows let it ingest multi-layered architecture without losing the thread ("context engineering").

## For Joe

This is how to take a vibe-coded prototype and make it sellable. Pair it with [[Multi-Agent Development Team]] (PM → Architect → Engineer → QA → Reviewer) for bigger builds. The slogan: **vibe to validate, spec to ship.**
