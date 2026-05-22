---
type: concept
title: "Quantitative Finance Career Guide"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - finance
  - career
  - mathematics
  - programming
---

# Quantitative Finance Career Guide

Master hub for becoming a quantitative analyst (quant). Every section links to a dedicated deep-dive page.

## The Three Quant Roles

| Role | Primary Focus | Math | Code | Finance |
|------|--------------|------|------|---------|
| **Quant Researcher** | Finding alpha signals, building models | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| **Quant Developer** | Building trading systems and infrastructure | ★★★☆☆ | ★★★★★ | ★★☆☆☆ |
| **Quant Trader** | Deploying capital, managing risk in real time | ★★★★☆ | ★★★☆☆ | ★★★★★ |

**Researcher**: Develops pricing models, backtests strategies, generates alpha. PhD common at top firms. Pure math + statistics + ML focus. Hands strategy prototypes to Developers.

**Developer**: Builds execution systems, data pipelines, risk engines. Rewrites Python research prototypes in C++ for production. Strong CS + software engineering. The quant software engineer.

**Trader**: Manages live positions, reacts to markets, handles real-time risk. Requires strong probability intuition + market microstructure + composure under pressure. Most visible role; highest PnL variability.

## The Skill Dependency Map

All quant roles share a common foundation. The layers build on each other — skipping ahead fails.

```
MATHEMATICS (the irreducible foundation)
├── Calculus → options pricing (PDEs), gradient descent in ML
├── Linear Algebra → portfolio optimization, factor models, PCA, neural network weights
├── Probability Theory → every model, every interview question
├── Mathematical Statistics → regression, time series, backtesting validity
└── Stochastic Calculus → derivatives pricing, SDEs, Ito's lemma [the summit]
         ↓
FINANCIAL THEORY (applied math layer)
├── Markets & Instruments → vocabulary: equities, bonds, futures, options, swaps
├── Portfolio Theory → Markowitz, CAPM, factor models
├── Derivatives Pricing → Black-Scholes, Monte Carlo, risk-neutral pricing
└── Risk Management → Greeks, VaR, CVaR, stress testing
         ↓
PROGRAMMING (implementation layer)
├── Python → research, prototyping, backtesting (everyone needs this)
├── C++ → production systems, low-latency execution (Developers + HFT)
└── SQL → data engineering (universal requirement)
         ↓
STRATEGIES (synthesis layer)
├── Momentum / Trend Following
├── Mean Reversion / Pairs Trading
├── Statistical Arbitrage
├── Factor Investing
└── Market Making
         ↓
ML FOR QUANT (frontier layer)
├── Classical ML (gradient boosting, regularized regression)
├── Time Series ML (LSTM, Transformers)
├── Alternative Data feature engineering
└── Overfitting prevention (PurgedKFold, walk-forward)
         ↓
INTERVIEW PREP (final gate)
├── Mental Math
├── Probability Puzzles and Expected Value
├── Brainteasers and Logic
└── Market-Making Trading Games
```

## Self-Study Phase Plan

| Phase | Duration | Content | Output |
|-------|---------|---------|--------|
| 1: Math | 18–24 months | [[Quant Math Foundations]] — 5-layer curriculum | Comfort with stochastic calculus |
| 2: Finance | 4–6 months | [[Derivatives Pricing and Financial Theory]] | Can price an option, compute Greeks |
| 3: Programming | Parallel | [[Quant Programming Stack]] — Python data stack | Working backtest engine in Python |
| 4: Strategies | 3–6 months | [[Systematic Trading Strategies]] | Live-coded momentum + pairs strategy |
| 5: ML | 3–6 months | [[Machine Learning in Quantitative Finance]] | ML factor model on real data |
| 6: Interview | 2–3 months | [[Quant Interview Prep Guide]] | 12-week structured prep plan |

## Top Firms Tier List (2026)

| Tier | Firms | Profile |
|------|-------|---------|
| **S — Legendary** | Renaissance Technologies | Never publicly recruits; highest returns in history; PhD physicists/mathematicians |
| **S — Elite** | Jane Street, D.E. Shaw, Two Sigma | Values mathematical creativity over finance background; recruits undergrads from top math/CS programs |
| **A — Top Quant** | Citadel / Citadel Securities, Optiver, IMC, Virtu, HRT, SIG | World-class infrastructure; market-making + quant research; aggressive undergrad recruiting |
| **A — Top HF** | Millennium, Point72, Bridgewater, Balyasny | More discretionary-quant hybrids; longer holding periods |
| **B — Systematic** | AQR, Winton, Man AHL, Acadian | Factor investing + systematic macro; more academic culture |

**Jane Street** specifically: values how you think when you don't know the answer — calibration, probabilistic reasoning, communicating uncertainty. No finance background needed.

**Optiver**: famous for a mental math pre-screen (80 questions in 8 minutes). Speed + accuracy under pressure.

## Education Paths

| Role | Minimum | Competitive | Ideal |
|------|---------|-------------|-------|
| Quant Researcher | MS in Math/Stats/CS | PhD in Math, Physics, CS | PhD from top-10 program |
| Quant Developer | BS in CS/Math/Eng | MS in CS or Comp Finance | BS from target school + strong projects |
| Quant Trader | BS in Math/CS/Eng | Strong undergrad + math competitions | Putnam, USAMO, IOI background |

**Alternative paths**:
- **MFE (Master of Financial Engineering)**: MIT, Columbia, Berkeley, Carnegie Mellon; 1-year; industry-ready faster than PhD
- **WorldQuant University**: 100% free, accredited MSc in Financial Engineering; fully online; 2 years; 115 countries of students

## Salary Benchmarks (2026)

| Role | Base Range | Total Comp at Top Firms |
|------|-----------|------------------------|
| Junior Quant Analyst | $69k–$147k | $150k–$250k |
| Quant Researcher (hedge fund) | $150k–$300k | $200k–$500k+ |
| Quant Developer (top firm) | $150k–$250k | $200k–$350k |
| Quant Trader (top prop firm) | $150k–$300k | $300k–$1M+ in good years |
| First-year Jane Street / Optiver | $150k–$200k base | $250k–$400k total reported |

## See Also
- [[Quant Math Foundations]]
- [[Quant Programming Stack]]
- [[Derivatives Pricing and Financial Theory]]
- [[Systematic Trading Strategies]]
- [[Machine Learning in Quantitative Finance]]
- [[Quant Interview Prep Guide]]
