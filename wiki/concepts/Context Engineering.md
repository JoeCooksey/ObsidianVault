---
type: concept
title: "Context Engineering"
created: 2026-06-04
updated: 2026-06-04
tags:
  - concept
  - ai
  - agents
  - llm
  - skill
status: developing
related:
  - "[[Research - Most Useful Topics to Learn Now (for Joe)]]"
  - "[[Persistent Agent Memory]]"
  - "[[MCP Tools for Agent Stacks]]"
  - "[[Multi-Agent Development Team]]"
  - "[[Vibe Coding]]"
---
# Context Engineering

**Context engineering** is the discipline of designing *everything the model knows when it answers* — tools, memory, retrieval, state, and the assembled prompt — as opposed to **prompt engineering**, which optimizes only the text you send. (Source: [[Context Engineering Field Guide (Taskade)]])

> "Prompt engineering is deciding **what and how to ask**. Context engineering is deciding **what the model knows when it answers**." (Source: [[Context Engineering Field Guide (Taskade)]])

## Why It's *The* 2026 AI Skill

- Gartner named context engineering the **breakout AI capability of 2026**. (confidence: medium)
- **82%** of IT/data leaders say prompt engineering alone is no longer sufficient to power AI at scale (2026 State of Context Management Report). (Source: search synthesis, confidence: medium)
- The field literature: *"If you're building agents in 2026, you are a data engineer — an architect of context."*

## What It Actually Covers

1. **Retrieval (RAG)** — what documents/knowledge to inject, and how to rank them.
2. **Memory** — short-term (conversation) + long-term (cross-session) — see [[Persistent Agent Memory]].
3. **Tools** — which capabilities the model can call (see [[MCP Tools for Agent Stacks]]).
4. **State** — what the agent carries between steps.
5. **Context window budgeting** — what to keep, compress, or drop as context fills.

## Relationship to Prompt Engineering

They are **complementary, not replacements**: prompt engineering controls the conversation; context engineering gives the model the memory and knowledge to make that conversation meaningful. The strongest 2026 results come from doing both well. (Source: [[Context Engineering Field Guide (Taskade)]])

## Why This Matters For Joe

Joe already runs agent stacks ([[Multi-Agent Development Team]], [[Hermes Agent]], this very wiki) — context engineering is the **named skill** behind making them reliable. It is the difference between a demo and a system that works on the 50th run. It directly upgrades his [[Vibe Coding]] and [[Profitable Micro-SaaS Playbook|micro-SaaS]] work, and it's a portable, in-demand skill outside any single tool.

## See Also

- [[Persistent Agent Memory]] · [[MCP Tools for Agent Stacks]] — the building blocks
- [[Programming Skills AI Cannot Replace]] — judgment that frames good context
