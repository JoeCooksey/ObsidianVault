---
type: entity
entity_type: product
title: "Hermes Agent"
created: 2026-06-02
updated: 2026-06-02
tags:
  - entity
  - ai
  - agents
  - open-source
status: developing
related:
  - "[[Nous Research]]"
  - "[[Self-Improving Agent Loop]]"
  - "[[Persistent Agent Memory]]"
  - "[[Agent Orchestration Frameworks]]"
  - "[[MCP Tools for Agent Stacks]]"
  - "[[Andrej Karpathy]]"
  - "[[Research - Hermes Agent (What It's For, Setup, POCs)]]"
---

# Hermes Agent

**Hermes Agent** is an open-source, self-hosted autonomous AI agent built by [[Nous Research]], released February 2026. Tagline: *"The agent that grows with you."* It turns any OpenAI-compatible LLM into a 24/7 personal assistant with a [[Persistent Agent Memory|persistent memory]], an auto-generated skills library, a cron scheduler, and a multi-platform messaging gateway. (Source: [[Hermes Agent — Official Site and GitHub]])

It is **not** the same thing as the Hermes *LLM models* (Hermes 3, Hermes 4) or the *Hermes Function Calling standard*, though all three come from Nous Research. Hermes Agent is the **harness/runtime**; the models are interchangeable backends.

## What it actually is

A Python agent harness that:
- Receives a natural-language goal, decomposes it into steps, selects from **40+ built-in tools**, and iterates until done or until it determines it cannot finish. (Source: [[Hermes Agent — Official Site and GitHub]])
- **Learns**: writes a structured record after each task and auto-generates reusable *skills* (markdown files), improving them on reuse. See [[Self-Improving Agent Loop]].
- **Remembers**: SQLite + FTS5 full-text search over every past session, plus `MEMORY.md`/`USER.md` durable facts and a deepening user model. See [[Persistent Agent Memory]].
- **Runs unattended**: natural-language cron scheduling persists across restarts (SQLite state DB; resumes pipelines from the last checkpoint). (Source: [[Awesome Hermes Use Cases]])
- **Parallelizes**: spawns isolated, short-lived sub-agents with focused context and tools.

## Key facts

| Field | Value |
|---|---|
| Builder | [[Nous Research]] |
| Released | February 2026 |
| License | **MIT** (one SEO blog claims Apache 2.0 — incorrect) |
| Latest version | v0.15.2 (May 29, 2026) |
| GitHub stars | ~177,000 (≈30k forks) |
| Language | Python |
| Cost | Free to run; bring-your-own LLM API key |

> [!gap] Star count (~177k) and version come from one fetch of the GitHub page; treat exact numbers as a 2026-06 snapshot.

## LLM backends (no lock-in)

Switch with `hermes model` — no code changes. Supports **Nous Portal, OpenRouter (200+ models), OpenAI, NVIDIA NIM, NovitaAI, Hugging Face, and custom endpoints**, plus local models via **Ollama / vLLM / MLX**. Local-model auto-detection: pull a model and Hermes finds it. (Source: [[Hermes Agent — Official Site and GitHub]])

> [!gap] "Best open-source model" advice is fast-moving: one April 2026 source named Llama 4 Maverick best-in-class for tool calling; another reports Qwen3.5-9b works "VERY good" on a 16GB Mac Mini. Verify against current benchmarks before committing.

## Integrations

**Messaging gateway** (single process): Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, BlueBubbles (iMessage), Home Assistant — Telegram-first UX.

**Execution backends**: local, Docker, SSH, Singularity, Modal, Daytona (container-hardened sandboxing).

**Protocols**: MCP integration ([[MCP Tools for Agent Stacks]]); compatible with the `agentskills.io` open skills standard.

## Best suited for

- An **always-on personal assistant with memory** that compounds over weeks (its core differentiator vs. session-scoped tools).
- **Background / scheduled automation** delivered to chat apps (briefings, monitoring, triage) while you're away from the keyboard.
- **Multi-agent / sub-agent orchestration** for parallel workstreams.
- **Self-hostable** on anything from a $5 VPS or Raspberry Pi to a GPU cluster.

It is **not** the best tool for keyboard-driven, deep agentic software engineering — Claude Code wins that lane. The two are complements, not competitors. See [[Hermes Agent vs Claude Code vs OpenClaw]].

## Relevance to Joe

Nous Research's **official user-stories page lists Joe's exact pattern**: *"maintains a self-improving LLM Wiki second brain on a Hetzner VPS via a Telegram bot, using [[Andrej Karpathy|Karpathy]]'s LLM Wiki pattern."* Hermes Agent is, in effect, a productized, always-on version of this very vault's autoresearch + wiki loop. (Source: [[Hermes Agent — Official Site and GitHub]])
