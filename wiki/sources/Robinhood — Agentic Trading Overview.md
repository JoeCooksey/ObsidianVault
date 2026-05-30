---
type: source
source_type: official-documentation
title: "Robinhood — Agentic Trading Overview"
author: Robinhood Markets
date_published: 2026-05-27
url: https://robinhood.com/us/en/support/articles/agentic-trading-overview/
confidence: high
created: 2026-05-29
updated: 2026-05-29
tags:
  - source
  - finance
  - robinhood
  - agentic-ai
  - mcp
related:
  - "[[Agentic Trading (Robinhood)]]"
  - "[[Robinhood]]"
  - "[[MCP Tools for Agent Stacks]]"
key_claims:
  - "Agentic Trading connects a user's own AI agent to a dedicated Robinhood account via the Robinhood Trading MCP."
  - "Agents trade only within a separate pre-funded Agentic account; they cannot touch the user's other accounts."
  - "The user is ultimately responsible for every trade the agent places; Robinhood disclaims losses from agent decisions."
---

# Robinhood — Agentic Trading Overview

Robinhood's official support article for **Agentic Trading**, the beta feature (announced 2026-05-27) that lets users connect an external AI agent to trade on their behalf.

## What it contributes

The authoritative, first-party description of how the feature works — used to anchor the [[Agentic Trading (Robinhood)]] concept page against press summaries.

### Setup (from the doc)
1. Choose an MCP-capable AI platform (Claude Code, Claude Desktop, ChatGPT, Cursor, others).
2. Connect the **Robinhood Trading MCP** endpoint: `https://agent.robinhood.com/mcp/trading`.
3. Authenticate the agent and complete onboarding for a **dedicated Agentic account**.
4. Account creation and authentication must be done on a **desktop device**.

### Account model
- The Agentic account is "a type of self-directed, individual investing account."
- Requires an existing primary individual account in good standing.
- Up to 10 self-directed individual accounts total (incl. the Agentic one).
- Agents execute **only** within the dedicated account — no access to other accounts.

### Agent capabilities
- Query portfolio value, buying power, account info (read-only to account numbers, positions, balances, full order history).
- Place orders (various order types), build portfolios, automate conditional strategies, rebalance, analyze risk and market data.

### Control & responsibility
- Some trades show a **preview requiring approval**; agents can be pre-authorized to trade without confirmation.
- "You are ultimately responsible for the trades your AI agent places."
- Stated risk: "AI agents can make errors, misinterpret instructions, act on incomplete or outdated information." Robinhood "is not responsible for losses resulting from agent-generated decisions."

### Scope / eligibility
- Beta, **stocks only** at launch; options, crypto, futures, event/prediction markets planned.
- Rolling out gradually — access requires an email notification from Robinhood.

> [!note] Primary source. First-party documentation; mechanics are high-confidence. Forward-looking asset-class plans are company statements, not yet shipped.
