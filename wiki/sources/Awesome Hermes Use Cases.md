---
type: source
source_type: documentation
title: "Hermes Agent User Stories + Awesome Use-Case Repos"
author: "Nous Research + community (aliaihub, 0xNyk)"
date_published: 2026
url: "https://hermes-agent.nousresearch.com/docs/user-stories"
created: 2026-06-02
updated: 2026-06-02
confidence: high
tags:
  - source
  - ai
  - agents
  - use-cases
status: developing
related:
  - "[[Hermes Agent]]"
  - "[[Research - Hermes Agent (What It's For, Setup, POCs)]]"
key_claims:
  - "Official user-stories page + curated awesome-list catalog dozens of real POCs"
  - "Spans personal assistants, dev workflows, content pipelines, trading, smart home"
  - "Includes the autonomous 79k-word novel+audiobook pipeline"
---

# Awesome Hermes Use Cases

Combines the **official user-stories doc** (`/docs/user-stories`) with community-curated repos (`aliaihub/awesome-hermes-usecases`, `0xNyk/awesome-hermes-agent`) and `hermesatlas.com`. The official doc is primary-source (**high confidence**); community repos are curated but include anecdotal metrics.

## Standout proof-of-concept projects

**Content / media**
- **Autonovel (House of Bells)** — end-to-end pipeline that produced a **19-chapter, 79,456-word novel + audiobook + website** autonomously. *(Most-cited flagship demo.)*
- Screen recording → finished HeyGen tutorial video with AI avatar; ComfyUI Stable-Diffusion pipelines; HTML/GSAP → MP4 with TTS narration.
- "Iris" on a spare laptop **builds a RenPy visual novel autonomously** — discovers ComfyUI locally, generates images, installs RenPy.

**Dev / multi-agent**
- Nous runs **12 Hermes instances in parallel to build Hermes itself**.
- 3-role pipeline: planner (GPT-5.4) → coder (MiniMax M2.7) → QA (local Qwen 35B) that tests, fails, and repairs until shipping.
- Event-driven **GitHub PR review** via cron or signed webhooks; Matt Pocock skills + parallel vertical-slice sub-agents.

**Smart home / device**
- Conversational **Home Assistant** control; **Android** remote control (36 tools: taps/swipes/screenshots); self-hosted **iPhone companion** with HealthKit/sensors; OnStar EV battery + remote start.

**Trading / finance** *(anecdotal — low confidence)*
- Weather-trading bot on Polymarket; reported figures vary wildly across sources ($100→$216 in 48h vs $300→$123K in 3 months).

**Knowledge / second brain** *(directly relevant to this vault)*
- **Self-improving LLM Wiki second brain on a Hetzner VPS via Telegram, using Karpathy's LLM Wiki pattern.**
- Obsidian vault as long-term memory; agent writes structured markdown notes into a synced vault.

**Other**: Minecraft companion (HermesCraft), autonomous Kali pen-testing with approval gates, voice-first fitness coach, meal planner, Ethereum onchain attestations, Tidal playlist curation.

> [!gap] Community trading/ROI numbers are self-reported and inconsistent — treat as low confidence. Official user stories are credible but are *user reports*, not audited benchmarks.
