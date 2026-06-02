---
type: source
source_type: documentation
title: "Hermes Agent — Official Site and GitHub"
author: "Nous Research"
date_published: 2026
url: "https://github.com/nousresearch/hermes-agent"
created: 2026-06-02
updated: 2026-06-02
confidence: high
tags:
  - source
  - ai
  - agents
status: developing
related:
  - "[[Hermes Agent]]"
  - "[[Nous Research]]"
key_claims:
  - "Hermes Agent is MIT-licensed, latest v0.15.2 (May 29 2026), ~177k GitHub stars"
  - "Built-in learning loop + FTS5 session search + Honcho user modeling"
  - "40+ tools, 6 execution backends, BYO OpenAI-compatible LLM"
---

# Hermes Agent — Official Site and GitHub

Primary sources: the official site `hermes-agent.nousresearch.com`, its `/docs/`, and the `github.com/nousresearch/hermes-agent` repo. Highest-confidence reference for what Hermes Agent *is* and how to run it.

## What it contributes

The canonical, vendor-authored definition of [[Hermes Agent]]: an autonomous, self-hosted agent with a closed [[Self-Improving Agent Loop|learning loop]] and [[Persistent Agent Memory|persistent memory]].

## Key claims (high confidence — primary source)

- **License**: MIT. **Latest**: v0.15.2 (May 29, 2026). **Stars**: ~177k / ~30k forks.
- **Architecture**: autonomous skill creation after complex tasks; FTS5 session search with LLM summarization; skills self-improve during use; agent-curated memory with periodic nudges; Honcho dialectic user modeling; `agentskills.io`-compatible.
- **Models**: switch with `hermes model` — Nous Portal, OpenRouter (200+), NovitaAI, NVIDIA NIM, OpenAI, Hugging Face, custom; local via Ollama/vLLM/MLX with auto-detection.
- **Tools/backends**: 40+ tools; local, Docker, SSH, Singularity, Modal, Daytona; web search, browser automation, vision, image gen, TTS.
- **Gateway**: Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI (+ Matrix, Mattermost, SMS, DingTalk, Feishu, WeCom, BlueBubbles/iMessage, Home Assistant).

## Installation

```bash
# Linux / macOS / WSL2
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```
```powershell
# Windows (PowerShell) — bundles Python 3.11, Node.js, ripgrep, ffmpeg, portable Git Bash
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)
```
One command to install, one to start. Docs at `hermes-agent.nousresearch.com/docs/`.

> [!gap] Verify the install command and license against the live repo before running — fetched numbers are a 2026-06 snapshot, and piping a remote script to bash/PowerShell warrants reading it first.
