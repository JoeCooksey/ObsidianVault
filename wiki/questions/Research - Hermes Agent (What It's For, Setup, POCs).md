---
type: synthesis
title: "Research - Hermes Agent (What It's For, Setup, POCs)"
created: 2026-06-02
updated: 2026-06-02
tags:
  - research
  - ai
  - agents
  - hermes
status: developing
related:
  - "[[Hermes Agent]]"
  - "[[Nous Research]]"
  - "[[Self-Improving Agent Loop]]"
  - "[[Persistent Agent Memory]]"
  - "[[Hermes Agent vs Claude Code vs OpenClaw]]"
  - "[[Awesome Hermes Use Cases]]"
  - "[[Andrej Karpathy]]"
sources:
  - "[[Hermes Agent — Official Site and GitHub]]"
  - "[[NVIDIA — Hermes Self-Improving Agents]]"
  - "[[Hermes Agent vs Claude Code vs OpenClaw]]"
  - "[[Awesome Hermes Use Cases]]"
---

# Research: Hermes Agent — What It's For, Should Joe Set It Up, and Cool POCs

## Overview

[[Hermes Agent]] is [[Nous Research]]'s open-source (MIT), self-hosted autonomous agent, released Feb 2026. It turns any OpenAI-compatible LLM into a **24/7 personal assistant that learns** — auto-generating reusable skills ([[Self-Improving Agent Loop]]) and remembering every past session ([[Persistent Agent Memory]]). It is the agent-runtime sibling of the Hermes LLM models, not a model itself.

## 1. What is it best suited for?

A persistent, always-on agent whose value **compounds over time**. Sweet spots:

- **Always-on personal assistant with memory** — daily briefings, inbox triage, monitoring, reminders delivered to Telegram/Discord/Slack while you're away from the keyboard. *(This is its single biggest differentiator.)*
- **Scheduled / background automation** — natural-language cron that survives restarts and resumes from checkpoints.
- **Multi-agent orchestration** — spawns isolated sub-agents for parallel workstreams.
- **Self-hosted, model-agnostic deployment** — runs on a $5 VPS, a Raspberry Pi, a Mac Mini, or a GPU box; swap models with `hermes model`.

**Not** best for desk-bound deep coding — Claude Code wins that. The honest framing: Claude Code for ~90% of keyboard knowledge-work; Hermes for the ~10% that should run in the background. They're complements ([[Hermes Agent vs Claude Code vs OpenClaw]]).

## 2. Should Joe set it up?

**Probably yes — as a complement to Claude Code, not a replacement — and the fit is unusually strong.**

- Nous's **official user stories literally include Joe's exact setup**: a *self-improving LLM Wiki second brain on a Hetzner VPS via a Telegram bot, using [[Andrej Karpathy|Karpathy]]'s LLM Wiki pattern* — which is precisely this vault's autoresearch + wiki loop. Hermes Agent is a productized, always-on version of what Joe already does manually.
- Joe is the target user: technically confident, already invested in a [[Persistent Agent Memory|persistent-memory]] workflow, comfortable in a Linux terminal.
- **Concrete payoff**: an always-on Hermes could run `/autoresearch`-style briefings on a schedule, ingest sources into the Obsidian vault automatically, and monitor his stock watchlist or EE news — delivered to Telegram.

**Caveats before committing:**
- Setup cost ~20–30 min; minimum ~1 vCPU / 2GB VPS + a model API key. Value only compounds if used continuously for weeks.
- The install is a piped remote script (`curl ... | bash`) — read it first.
- Keep Claude Code for desk coding.

> [!gap] "Best model" advice is volatile. For local/self-hosted, current candidates are Llama 4 Maverick (tool calling) or Qwen3.5-9b on small boxes; for quality, route to Claude/GPT via OpenRouter. Benchmark before locking in.

## 3. Cool proof-of-concepts people have built

- 🏆 **Autonovel (House of Bells)** — autonomous **79,456-word, 19-chapter novel + audiobook + website**.
- **Builds Hermes with Hermes** — Nous runs **12 instances in parallel** to develop the project itself; a planner→coder→QA trio that self-repairs until shipping.
- **Autonomous RenPy visual novel** — "Iris" discovers ComfyUI locally, generates art, installs RenPy, ships a game.
- **Event-driven GitHub PR review** — cron or signed-webhook code review with human-in-the-loop gates.
- **Smart home + phones** — Home Assistant control; Android remote control via 36 tools; iPhone companion with HealthKit context.
- **Autonomous Kali pen-testing** with scope/approval gates.
- **LLM-Wiki second brain on a VPS via Telegram** (Karpathy pattern) — *the one to copy.*
- **Polymarket weather-trading bot** *(fun but unverified — ROI claims vary wildly, low confidence).*

Full catalog: [[Awesome Hermes Use Cases]].

## Key Findings

- Hermes Agent = **self-hosted, MIT, model-agnostic agent runtime** built around a learning loop + persistent memory (Source: [[Hermes Agent — Official Site and GitHub]]).
- Its differentiator is **compounding value**: skills + session memory make an older instance beat a fresh one (Source: [[Hermes Agent vs Claude Code vs OpenClaw]]).
- **40+ tools**, 6 execution backends, 14+ messaging gateways; v0.15.2; ~177k stars (Source: [[Hermes Agent — Official Site and GitHub]]).
- It complements rather than replaces Claude Code.

## Key Entities
- [[Nous Research]] — builder; also makes Hermes LLMs + the function-calling standard.
- [[Hermes Agent]] — the product.

## Key Concepts
- [[Self-Improving Agent Loop]] — experience → reusable, self-refining skills.
- [[Persistent Agent Memory]] — FTS5 session search + `MEMORY.md`/`USER.md` + Honcho user model.

## Contradictions
- **License**: official site + GitHub say **MIT**; one SEO blog claimed Apache 2.0 → primary source wins, **MIT**.
- **Trading ROI**: $100→$216/48h vs $300→$123K/3mo — irreconcilable, self-reported, **low confidence**.

## Open Questions
- Which model gives the best cost/quality for Joe's wiki-automation use case specifically? (Needs hands-on testing.)
- How well does the learning loop actually generalize vs. overfit to recent sessions? (One tester noted it "cheats" by reading yesterday's session.)
- Real total cost of running it 24/7 for Joe's workload (API token spend dominates, not hosting).
- Skipped due to scope: deep dive on the Hermes 4.x models and the function-calling standard themselves.

## Sources
- [[Hermes Agent — Official Site and GitHub]] — Nous Research (primary, high confidence)
- [[Awesome Hermes Use Cases]] — official user stories + community repos (high/medium)
- [[NVIDIA — Hermes Self-Improving Agents]] — NVIDIA blog (medium)
- [[Hermes Agent vs Claude Code vs OpenClaw]] — 2026 comparison blogs (medium)
