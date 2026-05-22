---
type: research
title: "Research - Quant Finance Complete Guide"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - research
  - synthesis
  - career
---

# Research: Quant Finance Complete Guide

**Topic**: Full guide to becoming a quant — all topics to master, how they are related, and how to build each skill.
**Searches run**: 8
**Pages created**: 7

---

## Key Findings

### Finding 1: Three Distinct Roles with Different Skill Weightings
The quant world has three primary roles — Researcher, Developer, and Trader — with very different skill compositions. Researchers need the deepest math and ML. Developers need the strongest programming (especially C++). Traders need probability intuition + market structure knowledge. Understanding which role you're targeting should shape your study priorities. Most aspiring quants conflate all three.

### Finding 2: Mathematics Is the True Barrier
The hard prerequisite for any top quant role is stochastic calculus — the summit of a 5-layer mathematical curriculum (Calculus → Linear Algebra → Probability → Statistics → Stochastic Calculus). This takes 18–30 months of dedicated self-study from scratch. There is no shortcut. Top firms (Jane Street, Citadel, D.E. Shaw) hire physicists and mathematicians with no finance background specifically because the math is harder to acquire than the finance.

### Finding 3: Python First, C++ Second, SQL Always
Python (NumPy + Pandas + scipy + statsmodels + QuantLib) is the universal research language. C++ is required for Quant Developer roles and high-frequency trading infrastructure. SQL is universally required — market data lives in databases. The correct learning order: Python fluency first, SQL competence in parallel, C++ only when targeting Developer or HFT roles.

### Finding 4: The Skill Dependency Graph Is Strict
Financial theory (Black-Scholes, portfolio theory) requires probability + calculus as prerequisites. Backtesting validity requires statistics. ML for quant requires statistics + linear algebra + Python. Strategy development requires both financial theory and backtesting skill. The map cannot be skipped — attempting stochastic calculus before probability is like attempting calculus before algebra.

### Finding 5: Top Firms Value Mathematical Creativity Over Finance Knowledge
Jane Street, Optiver, and IMC actively recruit from math/physics/CS backgrounds with zero finance background and teach finance internally. They explicitly value how candidates reason under uncertainty and communicate calibrated uncertainty. Finance knowledge can be learned in months; mathematical maturity takes years.

### Finding 6: Interview Prep Is a Separate Skill Domain
Quant interviews (probability puzzles, mental math, brainteasers, market-making trading games) require dedicated practice that is distinct from your math and programming skill. Optiver's pre-screen is 80 mental arithmetic problems in 8 minutes. Jane Street runs multi-round trading games. The Green Book (Xinfeng Zhou) + tradermath.org + mock trading sessions is the standard preparation stack. 12 weeks of dedicated interview prep is the minimum.

### Finding 7: Overfitting Is the #1 Failure Mode in ML Quant
Financial data has very low signal-to-noise (Sharpe 0.5 = "good signal"). Multiple testing is catastrophic — 1000 strategies tested → ~50 appear significant by chance. PurgedKFold cross-validation and walk-forward testing are mandatory; standard k-fold creates data leakage across time. Marcos López de Prado's *Advances in Financial Machine Learning* is required reading before deploying any ML strategy in production.

### Finding 8: Free Paths to Quant Exist
WorldQuant University's MSc in Financial Engineering is 100% tuition-free, accredited, and fully online. MIT OCW provides Probability (18.600), Statistics (18.650), and Linear Algebra (18.06) for free. The ISLR textbook (machine learning) is free as a PDF. QuantStart, PyQuant News, and QuantLib documentation provide the rest. A motivated self-studier with no formal program can build a competitive quant skill set entirely with free resources.

---

## Pages Created

| Page | Contents |
|------|---------|
| [[Quantitative Finance Career Guide]] | Master hub: 3 roles, skill dependency map, phase plan, firm tier list (Jane Street → Renaissance), salary benchmarks, education paths |
| [[Quant Math Foundations]] | 5-layer math curriculum with dependency graph, time estimates, resources, and quant application for every concept |
| [[Quant Programming Stack]] | Python library stack, C++ requirements, SQL, other languages, 8 portfolio projects, backtest engine build guide |
| [[Derivatives Pricing and Financial Theory]] | Markets vocabulary, Markowitz + CAPM + factor models, Black-Scholes derivation + formula, all 5 Greeks, VaR + CVaR + stress testing |
| [[Systematic Trading Strategies]] | Momentum, mean reversion, pairs trading (code), factor investing (6 classic factors), market making (Avellaneda-Stoikov), 7 backtesting errors, Sharpe and Sortino formulas |
| [[Machine Learning in Quantitative Finance]] | Classical ML table, feature engineering (price + fundamental + alt data), factor zoo, time series ML, RL for execution, overfitting problem + PurgedKFold, learning path |
| [[Quant Interview Prep Guide]] | Firm-specific formats, mental math tricks, probability distributions + classic problems, 5-step brainteasers approach, market-making game mechanics, 12-week schedule |

---

## Sources

- QuantStart (quantstart.com) — self-study plans, reading lists, Python articles
- Quant Blueprint (quantblueprint.com) — top firm tier list, role definitions
- Quant Vero / Quantt — How to Become a Quant 2026 guides
- Mergers & Inquisitions — quant fund career guide
- DataCamp — quantitative analyst career guide 2026
- WorldQuant University (wqu.edu) — free MSc Financial Engineering
- PyQuant News (pyquantnews.com) — Python libraries for quant finance
- QuantNet forums — interview preparation discussions, math prerequisites
- tradermath.org — quant interview question bank + mental math drills
- openquant.co — free online quant practice platform
- Quant Finance Institute — stochastic calculus explainer
- eFinancialCareers — quant developer vs. researcher comparison
- Wall Street Oasis forums — compensation data, role comparisons
- arXiv: Gu/Kelly/Xiu 2020 (ML asset pricing), López de Prado papers
- eFrontier / Stony Brook AMS — quantitative finance curriculum structure
