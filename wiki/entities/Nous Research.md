---
type: entity
entity_type: organization
title: "Nous Research"
created: 2026-06-02
updated: 2026-06-02
tags:
  - entity
  - ai
  - open-source
  - organization
status: developing
related:
  - "[[Hermes Agent]]"
  - "[[Self-Improving Agent Loop]]"
---

# Nous Research

**Nous Research** is an open-source AI lab best known for the **Hermes** family of open-weight LLMs and, since February 2026, the [[Hermes Agent]] autonomous agent runtime. It releases models, datasets, and tooling under permissive licenses (Hermes Agent is MIT). (Source: [[Hermes Agent — Official Site and GitHub]])

## What it ships

- **Hermes LLMs** — open-weight chat/agentic models. Hermes 2 Pro introduced strong function calling; Hermes 3 widened the lead; the line continues through Hermes 4.x (e.g., Hermes-4.3-36B). Hermes 3 can plan, use external data, and call tools out-of-the-box. (Source: [[Hermes Agent — Official Site and GitHub]])
- **Hermes Function Calling standard** — tool definitions in `<tools>`, invocations in `<tool_call>`, responses in `<tool_response>`; backed by the open `hermes-function-calling-v1` dataset. Hermes 2 Pro hit ~90% function-calling accuracy vs. 60–70% for general models (vendor-reported).
- **[[Hermes Agent]]** — the self-improving agent harness that runs those (or any OpenAI-compatible) models.
- **Honcho** — a service for "dialectic user modeling" that Hermes Agent integrates for deepening per-user models.

> [!gap] Benchmark figures (90% vs 60–70%) are vendor-reported; per program rules, treat LLM leaderboard/accuracy claims as low confidence until independently verified.

## Significance

Nous occupies the "fully open, self-hostable, no-lock-in" corner of the agent landscape — the philosophical opposite of closed copilots. Hermes Agent's ~177k GitHub stars within months of release signal unusually fast community adoption. See [[Hermes Agent vs Claude Code vs OpenClaw]].
