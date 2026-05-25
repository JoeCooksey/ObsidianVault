---
type: concept
title: "Agent Orchestration Frameworks"
status: developing
created: 2026-05-25
updated: 2026-05-25
tags:
  - AI
  - agents
  - frameworks
  - CrewAI
  - LangGraph
  - AutoGen
  - MetaGPT
---

# Agent Orchestration Frameworks

Frameworks that manage multiple AI agents working together toward a shared goal. As of 2026, three are production-ready for software development pipelines.

## Framework Comparison

| Framework | Model | Strengths | Weaknesses | Best Use |
|---|---|---|---|---|
| **CrewAI** | Role-based crew | Fastest to ship, intuitive abstraction, YAML config, enterprise observability (2026) | Less control than graph approach | Prototyping, role-clear teams |
| **LangGraph** | Directed graph (state machine) | Maximum control, checkpointed state, resumable, conditional routing | Steeper learning curve | Production, complex dependencies |
| **Claude Code Agent Teams** | Orchestrator + subagents | Native in Claude Code, parallel init, isolated contexts, shared codebase | Claude-only ecosystem | Claude-native development |
| **MetaGPT** | Sequential assembly line | Software-company abstraction, structured artifacts (PRD → spec → code) | Less flexible than custom pipelines | Full software company simulation |
| **AutoGen** (maintenance) | Conversation / group chat | Mature code execution sandbox | No new features, deprecated | Legacy only; use Microsoft Agent Framework for new |

## CrewAI

**Core abstractions**: `Agent` (role + goal + backstory + tools), `Task` (description + expected output + agent), `Crew` (agents + tasks + process).

**Process types**:
- `Process.sequential` — tasks run in order, each can access prior outputs
- `Process.hierarchical` — manager agent auto-delegates tasks to best-fit worker

**Key 2026 updates**: enterprise-grade observability dashboard, scheduling for multi-agent coordination, YAML-first task definition (recommended), `@before_kickoff` / `@after_kickoff` hooks.

## LangGraph

**Core abstractions**: `State` (TypedDict shared across all nodes), `Node` (agent function that reads/writes state), `Edge` (routing logic between nodes).

**Key patterns**:
- `interrupt_before` on a node = human-in-the-loop gate
- `add_conditional_edges` = dynamic routing based on state
- Sub-graphs = nested agents, independently testable
- Checkpointing = persist state to SQLite/Redis for resume

**Key 2026 updates**: LangGraph Cloud (hosted execution + monitoring), better LangSmith integration, improved multi-agent spawning.

## Claude Code Agent Teams

**Core abstractions**: subagent YAML files in `.claude/agents/`, each with `name`, `model`, `system`, `tools`.

**Orchestration modes**:
1. **Agent View** — independent parallel tasks (fix bug in A, review PR in B, check logs in C)
2. **Subagents** — repeatable defined workflows with locked model + system prompt
3. **Agent Teams** — dependent tasks where orchestrator sequences work and passes context

**Key 2026 updates**: Released with Claude Opus 4.6 (Feb 2026), supports 2–16 agents, parallel init since April 2026, subagents initialize MCP connections simultaneously cutting startup time.

## MetaGPT

**Philosophy**: `Code = SOP(Team)` — Standard Operating Procedures applied to LLM teams.

**Five canonical roles**: Product Manager → Architect → Project Manager → Engineer → QA Engineer

**Output artifacts**:
- PRD (Product Requirements Document)
- Technical specification
- Task list
- Implementation code
- Test cases

MetaGPT is the **reference architecture** for agent software teams — any custom pipeline should at minimum replicate its 5-role structure and artifact handoff pattern.

## Selection Rule

- **Need to ship fast?** → CrewAI
- **Complex dependencies, need control?** → LangGraph
- **Already using Claude Code?** → Claude Code Agent Teams
- **Want the full software-company experience?** → MetaGPT
- **Inheriting existing AutoGen system?** → Keep for now, migrate to Microsoft Agent Framework

## Related

- [[Multi-Agent Development Team]] — the standard 5-role team built on these frameworks
- [[MCP Tools for Agent Stacks]] — tools that plug into all frameworks via MCP
- [[Research - Full Agent Stack Team Guide]] — full code examples for CrewAI and LangGraph
