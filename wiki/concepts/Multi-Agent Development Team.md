---
type: concept
title: "Multi-Agent Development Team"
status: developing
created: 2026-05-25
updated: 2026-05-25
tags:
  - AI
  - agents
  - software-development
  - orchestration
---

# Multi-Agent Development Team

A **multi-agent development team** is a system of specialized AI agents that mirrors a real software company's org chart — each agent has a single role, isolated context, and defined inputs/outputs. Together they take a natural-language prompt and deliver a complete project.

## The 5-Role Standard Team

| # | Role | Input | Output | Best Model |
|---|---|---|---|---|
| 1 | **Product Manager** | User prompt | PRD (user stories, AC, scope) | Opus 4.7 |
| 2 | **Architect** | PRD | Tech spec, system diagram, API contracts | Opus 4.7 |
| 3 | **Engineer** | Arch spec + tasks | Working code in `/src/` | Sonnet 4.6 |
| 4 | **QA Engineer** | Code + acceptance criteria | Tests, coverage report, bug list | Sonnet 4.6 |
| 5 | **Reviewer** | Code + tests + AC | Review report, inline fixes, PR | Opus 4.7 |

An optional **Project Manager agent** sits between Architect and Engineer to decompose the tech spec into discrete tasks and assign them to engineer sub-agents.

## Three Human-in-the-Loop Gates

1. **PRD approval** — human confirms scope before architecture work begins
2. **Architecture approval** — human confirms design before code is written
3. **Final review** — human reviews output before merge/deploy

Skipping gates risks hallucinated scope (Gate 1) and irreversible structural mistakes (Gate 2).

## Orchestration Patterns

- **Sequential pipeline** — fixed handoff order, each agent waits for prior output; simplest, best for well-scoped projects ([[CrewAI]] `Process.sequential`)
- **Supervisor pattern** — an orchestrator agent dynamically delegates to workers; best for variable or parallel workloads ([[LangGraph]] supervisor)
- **Role-based crew** — agents self-assign tasks from a shared pool based on role + goal match; best for open-ended work ([[CrewAI]] `Process.hierarchical`)

## Artifact Convention

Each agent writes to a named file in `/artifacts/`:
- `prd.md` — Product Manager output
- `architecture.md` — Architect output
- `tasks.md` — Project Manager breakdown
- `review.md` — Reviewer findings

Code goes in `/src/`, tests in `/tests/`. This makes inter-agent handoffs explicit and creates an audit trail.

## Related

- [[Agent Orchestration Frameworks]] — CrewAI vs LangGraph vs Claude Code Agent Teams
- [[Agent Roles Software Development]] — detailed role definitions
- [[MCP Tools for Agent Stacks]] — tools each agent needs
- [[Research - Full Agent Stack Team Guide]] — full synthesis with code examples
