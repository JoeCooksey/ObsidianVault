---
type: concept
title: "Efficient Market Hypothesis"
status: developing
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - finance
  - quant
  - investing
related:
  - "[[Quantitative Trading]]"
  - "[[Index Fund Investing]]"
  - "[[Statistical Arbitrage]]"
  - "[[Renaissance Technologies]]"
aliases:
  - "EMH"
---

# Efficient Market Hypothesis

The EMH (Eugene Fama) holds that asset prices reflect available information, so consistently earning **risk-adjusted excess returns** is very hard. Three forms: **weak** (prices embed past prices → technicals don't beat), **semi-strong** (prices embed all public info → fundamental analysis on public data doesn't reliably beat), **strong** (prices embed even private info → nobody beats).

## What the evidence actually says (2025)
- **Markets aren't perfectly efficient** — Buffett, Renaissance, Thorp prove durable mispricings exist. So strict/strong EMH is false.
- **But beating it is hard and self-defeating** — any tradable signal, once exploited, gets **priced away**. Renaissance's edge is profitable only for minutes; trading on it *makes the market more efficient* ([[Renaissance Technologies]], [[Statistical Arbitrage]]).
- **ML doesn't break it for retail** — academic 2024–2025 work finds ML "wins" are mostly **overfitting** that dies out-of-sample; results stay broadly consistent with EMH ([[ML vs Efficient Markets — Academic Reassessment]]).
- **SPIVA confirms the practical upshot** — after fees, ~80%+ of equity funds trail their index over 10 years ([[SPIVA Scorecard — Active vs Index]]).

## The takeaway
Markets are **adaptively efficient**: not perfect, but efficient *enough* that the average participant — especially a retail one without a data/latency/cost moat — should expect to underperform the index after costs. The rational response is [[Index Fund Investing]], not a "market-beating" bot. See [[Research - Robinhood Agentic Trading and Beating the Market]].
