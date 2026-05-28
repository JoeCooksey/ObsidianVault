---
type: synthesis
title: "Research: Stock Buy/Sell Factors and Quant Finance"
created: 2026-05-28
updated: 2026-05-28
status: developing
tags:
  - research
  - finance
  - investing
  - quant
related:
  - "[[Fundamental Analysis Valuation Metrics]]"
  - "[[Technical Analysis Indicators]]"
  - "[[Position Sizing and Risk Management]]"
  - "[[Sell Discipline (When to Sell a Stock)]]"
  - "[[Statistical Arbitrage]]"
  - "[[Quantitative Trading]]"
  - "[[Jim Simons]]"
  - "[[Renaissance Technologies]]"
  - "[[Ed Thorp]]"
  - "[[D.E. Shaw]]"
  - "[[Index Fund Investing]]"
  - "[[Margin of Safety (Finance)]]"
sources:
  - "[[Renaissance Technologies — Wikipedia]]"
  - "[[Edward O. Thorp — Wikipedia]]"
  - "[[2024 Hedge Fund Returns Reporting]]"
  - "[[SPIVA Scorecard — Active vs Index]]"
---

# Research: Stock Buy/Sell Factors and Quant Finance

## Overview

Two questions, one answer. **(1) What factors should drive buying/selling a stock?** They fall into four layers: *what* to own (fundamentals), *when* to act (technicals/timing), *how much* to risk (position sizing), and *when to exit* (sell discipline). **(2) Do quant geniuses actually win?** A tiny handful do, spectacularly and durably — but their edges are secret, capacity-constrained, and decay over time, while ~90% of all active managers lose to a plain index fund. The honest synthesis: **the discipline of the great quants is transferable to you; their secret signals are not.**

## Part 1 — Factors That Should Influence Buying & Selling

### A. Fundamentals — *what* to own and at what price → [[Fundamental Analysis Valuation Metrics]]
- **Valuation ratios**: P/E (vs. own history, peers, market), PEG (<1 cheap-for-growth), P/B (asset-heavy firms), P/S, free-cash-flow yield. No single ratio in isolation — P/E is distorted by buybacks, debt, one-offs, and the cycle. (Source: [[Fundamental Analysis Valuation Metrics]])
- **Business quality**: earnings growth & quality, competitive moat, balance-sheet/debt, management capital allocation.
- **Margin of safety**: buy meaningfully below estimated fair value → [[Margin of Safety (Finance)]].

### B. Technicals & macro — *when* to act → [[Technical Analysis Indicators]]
- Moving averages (50/200-day trend), RSI (overbought/oversold), MACD (trend + momentum), support/resistance, volume confirmation.
- Macro overlay: interest rates, sector cycle, regulation. Technicals are a **timing/discipline tool, weakly supported as a standalone edge** after costs.

### C. Position sizing & risk — *how much* → [[Position Sizing and Risk Management]]
- **Risk 1–2% of capital per trade**; pre-set stop-loss; loss limits; diversify across assets/sectors. A 50% loss needs a 100% gain to recover — avoiding ruin compounds better than chasing gains.

### D. Sell discipline — *when to exit* → [[Sell Discipline (When to Sell a Stock)]]
- Sell when: **thesis breaks**, **target price hit**, **rebalancing**, **defensive weakening**, or **personal cash/risk need**.
- The **worst** (and most common) reason to sell: "the price dropped." Panic selling locks losses and misses rebounds — missing the 10 best S&P days (2000–2020) cut returns from ~6% to ~2.4%.

## Part 2 — Quant Finance: People, Algorithms, Reality

| Person/Firm | Algorithm | Track Record | Real? |
|-------------|-----------|--------------|-------|
| **[[Ed Thorp]]** | Invented [[Statistical Arbitrage]]; convertible/warrant arb; Kelly sizing | PNP **~20% net, 2 decades, no down quarter** | Yes — and quit Ridgeline in 2002 when the edge crowded out |
| **[[Jim Simons]] / [[Renaissance Technologies]]** | Mean-reversion + stat-arb signals on petabyte data; thousands of tiny market-neutral bets | Medallion **~39% net since 1988**; +98% in 2008, +76% in 2020 | Yes — best ever, but **closed since 1993**, capped small |
| **[[D.E. Shaw]]** | Computational stat-arb + multi-strategy | ~22%/yr 1988–2000; **2024 #1 with $11.1B**, Oculus +36% | Yes — top platform quant, but ~15–18% net |
| **Citadel / Millennium** | Multi-strategy "pod" platforms | ~15% in 2024 | Yes — strong, institutional-only |

### How the algorithms actually work
Find a **repeating statistical anomaly** → trade it **market-neutral** so you bet on the relationship not the market → **repeat at massive scale** so the law of large numbers turns a thin per-trade edge into consistent profit. See [[Quantitative Trading]] and [[Statistical Arbitrage]].

### Are they actually successful? — the two-sided truth
- **The winners are real**: Medallion and PNP are not luck; the returns and consistency are too extreme over too long.
- **But the base rate is brutal**: per [[SPIVA Scorecard — Active vs Index]], **~90% of active managers underperform the index over 15 years**; in 2024, 65% of large-cap active funds lost to the S&P 500.
- **And edges decay**: Thorp shut Ridgeline because competition arbitraged his edge away. A known strategy is a dying strategy — which is why RenTech operates in extreme secrecy and keeps Medallion tiny.

## Key Findings

1. Stock decisions decompose into four separable factors — **fundamentals (what), timing (when), sizing (how much), sell rules (exit)** — and most retail failures are sizing/sell-discipline failures, not bad stock picks. (Source: [[Position Sizing and Risk Management]], [[Sell Discipline (When to Sell a Stock)]])
2. **No single valuation ratio is reliable alone**; P/E is routinely distorted. (Source: [[Fundamental Analysis Valuation Metrics]])
3. **Renaissance's Medallion (~39% net since 1988) is the best track record in finance** — but closed since 1993 and deliberately capacity-capped; its public RIEF fund trails by ~17–19%. (Source: [[Renaissance Technologies — Wikipedia]])
4. **Ed Thorp invented statistical arbitrage** and earned ~20% net for two decades with no losing quarter — then quit when the edge crowded out, proving edges decay. (Source: [[Edward O. Thorp — Wikipedia]])
5. **2024 platform quants** (D.E. Shaw +18%, Citadel +15.1%, Millennium +15%) are excellent but an order of magnitude below Medallion and institution-only. (Source: [[2024 Hedge Fund Returns Reporting]])
6. **~90% of active managers underperform the index over 15 years** — the winning quants are the rare exception. (Source: [[SPIVA Scorecard — Active vs Index]])
7. **You can't copy the algorithms** (data, costs, leverage, talent are moats) — but you *can* copy the discipline: rules-based, unemotional, well-sized, with a written sell plan. For most people that resolves to [[Index Fund Investing]] + sizing + sell rules.

## Contradictions

- **"Active management works" vs. "active management loses to the index."** Both true at different scales: a handful of elite, secretive quants genuinely beat the market for decades, while the *median* active manager loses. The glamour cases are survivorship-biased; SPIVA is the unbiased base rate. SPIVA is more credible for the *typical* investor's expectation.
- **Hedge-fund return figures** are self-reported and survivorship-biased (failed funds vanish from averages) — treat the 2024 numbers as directional, not audited.

## Open Questions

- What *exactly* are Medallion's signals? Unknown by design — proprietary and never disclosed. (Open by construction.)
- Two Sigma and AQR specific 2023–2024 figures and factor-model details were not fetched this session.
- How much of factor investing (value/momentum/quality premia) survives after fees and crowding in 2026? Not researched here.
- Quantitative detail on options/derivatives as buy-sell instruments (Greeks, hedging) — out of scope this session.

## Sources

- [[Renaissance Technologies — Wikipedia]] — Medallion returns, fees, history, IRS settlement
- [[Edward O. Thorp — Wikipedia]] — origin of stat arb, PNP/Ridgeline record
- [[2024 Hedge Fund Returns Reporting]] — Fortune/P&I/Institutional Investor, Jan 2025
- [[SPIVA Scorecard — Active vs Index]] — S&P Dow Jones Indices, 2025
- Supporting searches: Schwab/Fidelity/Bankrate (valuation), Wealthsimple/Fidelity (technicals), Lime/QuantifiedStrategies (sizing), Cabot/Motley Fool/Kiplinger (sell discipline)
