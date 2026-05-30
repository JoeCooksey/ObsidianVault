---
type: concept
title: "Technical Analysis Indicators"
status: developing
created: 2026-05-28
updated: 2026-05-28
tags:
  - finance
  - investing
  - trading
  - technical-analysis
related:
  - "[[Fundamental Analysis Valuation Metrics]]"
  - "[[Quantitative Trading]]"
---

# Technical Analysis Indicators

> The "what is the price doing?" layer. Technical analysis ignores the business and studies price and volume patterns to time entries and exits. It tells you *when*, not *what* to own.

## Premise & Caveat

Technical analysis assumes price action reflects all information and that patterns recur because human behavior recurs. It is **widely used for timing but weakly supported as a standalone edge** — most academic tests find it does not reliably beat buy-and-hold after costs. Treat it as a discipline tool, not a crystal ball. (confidence: medium)

## Core Indicators

| Indicator | Type | How it's read |
|-----------|------|---------------|
| **Moving Average (SMA/EMA)** | Trend | Price above a rising 200-day SMA = long-term uptrend; 50-day for intermediate trend. "Golden cross" (50 over 200) is bullish; "death cross" bearish. |
| **RSI** (Relative Strength Index) | Momentum oscillator | 0–100 scale. > 70 = overbought (possible pullback); < 30 = oversold (possible bounce). Created to measure speed of price moves. |
| **MACD** (Moving Avg Convergence/Divergence) | Trend + momentum | Difference of 12- and 26-day EMAs vs. a signal line. Crossovers flag shifts in trend direction and strength. Gerald Appel, late 1970s. |
| **Support / Resistance** | Price levels | Prices where buying (support) or selling (resistance) has historically clustered; breaks of these levels are watched as signals. |
| **Volume** | Confirmation | A move on high volume is considered more reliable than the same move on thin volume. |

(Source: Wealthsimple, Fidelity, Investing.com)

## How Practitioners Combine Them

No single indicator is used alone. A common pairing: **MACD identifies the trend direction/strength, RSI (or a stochastic oscillator) times the entry/exit** by spotting overbought/oversold extremes within that trend. (confidence: medium)

## Relationship to Fundamentals

- **Fundamentals** answer *what* to own and at what price ([[Fundamental Analysis Valuation Metrics]]).
- **Technicals** answer *when* to act.
- Many disciplined investors use fundamentals to build a watchlist and technicals only to time the entry — or ignore technicals entirely and dollar-cost average.

> [!gap] Beware curve-fitting: any indicator can be tuned to look great on past data ("backtest") and fail live. This is the same crowding/decay trap that ended Ed Thorp's Ridgeline fund — see [[Statistical Arbitrage]].

## See Also
- [[Fundamental Analysis Valuation Metrics]]
- [[Quantitative Trading]]
- [[Position Sizing and Risk Management]]
