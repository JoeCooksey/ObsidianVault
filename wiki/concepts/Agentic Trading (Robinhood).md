---
type: concept
title: "Agentic Trading (Robinhood)"
status: developing
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - finance
  - robinhood
  - agentic-ai
  - mcp
related:
  - "[[Robinhood]]"
  - "[[Robinhood Cortex]]"
  - "[[MCP Tools for Agent Stacks]]"
  - "[[Efficient Market Hypothesis]]"
  - "[[Position Sizing and Risk Management]]"
sources:
  - "[[Robinhood — Agentic Trading Overview]]"
  - "[[TechCrunch — Robinhood Lets AI Agents Trade Stocks]]"
---

# Agentic Trading (Robinhood)

Beta feature (launched **2026-05-27**) that lets a Robinhood user connect their **own external AI agent** to place trades, instead of an in-house bot. The agent connects through the **Robinhood Trading [[MCP Tools for Agent Stacks|MCP]]** endpoint. Stocks only at launch.

## How to use it (verbatim from the official doc)

1. **Have a primary account** — an existing individual investing account in good standing is required.
2. **Pick an MCP-capable AI app** — Claude Code, Claude Desktop, ChatGPT, Cursor, or any MCP client.
3. **Connect the Robinhood Trading MCP** — endpoint `https://agent.robinhood.com/mcp/trading`.
4. **Authenticate the agent on a desktop** — account creation/auth is desktop-only (on mobile, copy the onboarding URL to a desktop browser).
5. **Open the dedicated Agentic account** — a separate self-directed account (you can hold up to 10 individual accounts total). **Pre-fund it**: the agent can only spend the balance loaded into this wallet — it cannot reach your other accounts.
6. **Set the approval mode** — some trades show a preview you must approve; you may pre-authorize the agent to trade without confirmation.

## What the agent can / can't do
- **Can**: read portfolio value, buying power, positions, full order history; place orders (multiple order types); build/rebalance portfolios; run conditional strategies (e.g. *"buy $100 of ROAR each time it drops ≥2% in a day"*); analyze concentration risk, sector exposure, analyst notes.
- **Can't**: touch any account other than the dedicated Agentic one; trade asset classes beyond stocks (yet — options/crypto/futures/prediction markets are announced, not shipped).

## The control surface that actually matters
- Trade **notifications** for every order.
- **Preview-approval** for some orders; pre-authorization possible (use sparingly).
- Robinhood **fraud review** of suspicious trades.
- **You bear full responsibility.** Robinhood disclaims losses from "agent-generated decisions"; agents "can make errors, misinterpret instructions, act on incomplete or outdated information."

## How to use it *safely* (vault take)
The dedicated pre-funded wallet is the real safety primitive — treat its balance as the **maximum you are willing to lose**, sized via [[Position Sizing and Risk Management]] (≤1–2% of net worth, not your emergency fund). Keep preview-approval **on**; never blanket-authorize an autonomous loop with real money until you've watched it on a tiny balance. The feature lowers the *friction* of trading — and friction was one of the few things protecting retail accounts from overtrading. See [[Research - Robinhood Agentic Trading and Beating the Market]].
