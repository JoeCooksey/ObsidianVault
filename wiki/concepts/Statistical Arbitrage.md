---
type: concept
title: "Statistical Arbitrage"
status: developing
created: 2026-05-28
updated: 2026-05-28
tags:
  - finance
  - quant
  - trading
  - strategy
related:
  - "[[Quantitative Trading]]"
  - "[[Ed Thorp]]"
  - "[[Jim Simons]]"
  - "[[Renaissance Technologies]]"
---

# Statistical Arbitrage

> Profit from tiny, temporary mispricings between related securities, repeated thousands of times. No single trade is confident; the *aggregate* is — it's a casino running the house edge, not a gambler.

## How It Works

1. **Find a statistical relationship** — e.g., two correlated stocks (pairs trading), or a basket whose prices historically revert to a mean.
2. **Trade the divergence** — when the spread widens beyond its normal range, short the relatively expensive leg and buy the cheap one, betting on reversion ([[mean reversion]]).
3. **Stay market-neutral** — long and short legs cancel broad market moves, so the bet is on the *relationship*, not market direction.
4. **Repeat at scale** — any single trade has a thin edge and is often a coin-flip; profit comes from the **law of large numbers** over thousands of small, weakly-correlated bets.

(Source: [[Edward O. Thorp — Wikipedia]], [[Renaissance Technologies — Wikipedia]])

## Who Built It

- **Ed Thorp invented and first implemented stat arb** (and convertible/warrant arbitrage before it) — see [[Ed Thorp]].
- **Jim Simons / Renaissance** industrialized it with petabyte-scale data and machine learning into the [[Medallion Fund]]'s ~39% net annual returns — see [[Jim Simons]].

## The Edge Decays

The defining lesson: **statistical arbitrage edges erode as more players discover them.** Thorp wound down his Ridgeline fund in 2002 specifically because the strategy had become crowded and opportunities shrank. (confidence: high) This is why quant firms guard their signals in extreme secrecy and constantly research new ones — a known edge is a dying edge.

## Why Retail Can't Replicate It

Stat arb requires: massive clean datasets, ultra-low transaction costs, sophisticated execution, leverage, and PhD-level modeling. The per-trade edge is so thin that retail commissions and slippage erase it. This is a structural moat, not a skill you can self-teach into.

## See Also
- [[Quantitative Trading]]
- [[Ed Thorp]]
- [[Jim Simons]]
- [[Technical Analysis Indicators]]
