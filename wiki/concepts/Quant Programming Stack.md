---
type: concept
title: "Quant Programming Stack"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - programming
  - python
  - cpp
  - backtesting
  - finance
---

# Quant Programming Stack

The implementation layer of quantitative finance. Python dominates research; C++ dominates production at high-frequency firms.

## Python: The Primary Research Language

Python is the universal quant research language at hedge funds, investment banks, and prop trading firms. Every quant role requires Python fluency.

### Core Data Science Stack (all quants need this)

| Library | Purpose | Key Operations |
|---------|---------|----------------|
| **NumPy** | Array math, linear algebra | Matrix multiply, broadcasting, random sampling, vectorized ops |
| **Pandas** | Time series + tabular data | groupby, resample, rolling, merge, pivot_table, reindex |
| **SciPy** | Scientific computing | Optimization (minimize), statistics (distributions), integration |
| **Matplotlib** | Static visualization | Equity curves, histograms, scatter plots, heatmaps |
| **Plotly** | Interactive visualization | Interactive dashboards, 3D surface plots |
| **Statsmodels** | Econometrics | OLS, ARIMA, GARCH, cointegration tests, ACF/PACF |
| **Scikit-learn** | Machine learning | Regression, classification, PCA, cross-validation, pipelines |

### Quant-Specific Libraries

| Library | Purpose | Where Used |
|---------|---------|-----------|
| **QuantLib** (Python binding) | Derivatives pricing, term structure | Pricing exotic options, yield curve bootstrapping |
| **PyPortfolioOpt** | Portfolio optimization | Markowitz, Black-Litterman, hierarchical risk parity |
| **alphalens** | Factor signal analysis | Factor IC, factor returns, turnover analysis |
| **VectorBT** | Fast vectorized backtesting | GPU-accelerated; tests thousands of param sets |
| **Backtrader** | Event-driven backtesting | Portfolio simulation with commissions + slippage |
| **Zipline (Reloaded)** | Research-grade backtesting | Quant research platform; data bundles |
| **yfinance / OpenBB** | Free market data | Yahoo Finance; Bloomberg alternative |
| **TA-Lib** | Technical indicators | 200+ indicators (RSI, MACD, Bollinger Bands) |
| **PyMC** | Bayesian inference | Bayesian factor models, regime detection |

### Python Learning Path for Quants

1. **Python basics** (2–4 weeks): syntax, data structures (list, dict, set), OOP (classes, inheritance), file I/O
2. **NumPy fluency** (2–3 weeks): array creation, broadcasting, vectorized operations, random module
3. **Pandas fluency** (4–6 weeks — this is where most time is correctly spent): Series/DataFrame, indexing, time series operations (resample, rolling, shift), groupby, merge
4. **Data visualization** (1 week): matplotlib + seaborn for standard quant charts
5. **Statsmodels** (2–3 weeks): OLS regression, ARIMA, cointegration tests, GARCH
6. **Scikit-learn** (3–4 weeks): model API, cross-validation, regularized regression, PCA
7. **Backtesting** (ongoing): build a simple backtest from scratch before using a framework

**Best Resources**:
- *Python for Finance* by Yves Hilpisch (O'Reilly; finance-specific Python; the standard reference)
- PyQuant News (pyquantnews.com) — free newsletter + tutorials on NumPy/Pandas/finance
- QuantStart Python articles (quantstart.com/articles) — free, finance-specific Python guides
- Kaggle Python course + financial dataset competitions (free practice environment)

---

## C++: The Production Language

Quant Developers and competitive Quant Traders at high-frequency firms need C++. Reasons:
- Python prototypes get rewritten in C++ for microsecond-level latency
- Production order management systems, execution engines, risk engines are C++
- QuantLib is written in C++ at its core
- HFT firms (Citadel Securities, Virtu, HRT, Optiver, IMC) run C++ execution stacks

### C++ Topics for Quants

| Topic | Why It Matters |
|-------|---------------|
| STL containers (vector, map, unordered_map, deque) | Fast data structures for order books, price caches |
| Move semantics + smart pointers (unique_ptr, shared_ptr) | Memory-safe production code; no raw new/delete |
| Templates and generic programming | Generic pricing engines; policy-based design |
| Concurrency (std::thread, std::mutex, std::atomic) | Parallel backtesting; real-time data feed processing |
| Lambda expressions + functional patterns | Modern C++17/20 idioms used at quant firms |
| CRTP (Curiously Recurring Template Pattern) | Zero-overhead abstractions in performance-critical code |
| Lock-free data structures | Ultra-low-latency order book implementations |

### C++ Learning Path

1. *C++ Primer* by Lippman, Lajoie, Moo (comprehensive; the standard intro text)
2. *Effective Modern C++* by Scott Meyers (idioms, move semantics, modern patterns)
3. *C++ Design Patterns and Derivatives Pricing* by Joshi (quant-specific C++; most relevant)
4. Study QuantLib source code (real-world quant C++ at production quality)
5. Build a simple fixed-income pricer or option engine in pure C++

---

## SQL: The Universal Requirement

Every quant role requires SQL. Market data lives in relational databases. Time series data lives in columnar stores.

**Key SQL skills for quants**:
- SELECT, WHERE, GROUP BY, ORDER BY, HAVING
- JOINs (INNER, LEFT, RIGHT) for combining price and fundamental data
- Window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER) — critical for time series
- CTEs (Common Table Expressions) for readable complex queries
- Date/time operations (DATEADD, DATEDIFF, EXTRACT)

**Databases encountered in quant roles**:
- PostgreSQL / MySQL (relational, general purpose)
- ClickHouse / DuckDB (columnar; fast for time series analytics)
- KDB+ / Q (specialist quant finance time series database; used at Bloomberg, top banks, prop firms)
- Arctic (MongoDB-based Python time series store by Man Group)

---

## Other Languages (Awareness Level)

| Language | Context | Priority |
|----------|---------|----------|
| R | Academic research, econometrics; CRAN packages | Low — Python dominates industry; know it exists |
| MATLAB | Legacy bank pricing code; academic labs | Low — declining; some banks still use it |
| Julia | High-performance research; speed of C++, syntax of Python | Medium — emerging in quant research; worth watching |
| KDB+/Q | Time series database query language | Medium — if targeting market data infrastructure roles |

---

## Portfolio Project List

Build these to demonstrate quant programming competency:

| Project | Skills Demonstrated | Difficulty |
|---------|--------------------|-----------| 
| **Options Pricer** | Black-Scholes, binomial tree, all Greeks; Python | Easy |
| **Backtest Engine** | Momentum strategy from scratch; transaction costs; Sharpe ratio | Medium |
| **Factor Model** | Fama-French 3-factor replication; OLS; Kenneth French data (free) | Medium |
| **Pairs Trading System** | Cointegration test; z-score entry/exit; equity curve | Medium |
| **Monte Carlo VaR** | Historical simulation vs. parametric VaR; portfolio context | Medium |
| **GARCH Volatility Forecaster** | GARCH(1,1) fit; vol forecast; compare to realized vol | Hard |
| **ML Factor Alpha** | Gradient boosting; cross-sectional stock return prediction; walk-forward | Hard |
| **Options Risk Dashboard** | Real-time Greeks via QuantLib; Plotly dash visualization | Hard |

---

## The Backtest Engine Build (Most Important Project)

Building a simple backtest engine from scratch (before using Backtrader or VectorBT) forces you to understand:
- How to correctly handle look-ahead bias (using only data available at time t)
- Transaction cost modeling (bid-ask spread, market impact)
- Portfolio rebalancing mechanics
- Performance analytics (Sharpe, Sortino, max drawdown, Calmar ratio)

**Minimum viable backtest engine** (~500 lines of Python):
```
BacktestEngine
├── DataLoader (load OHLCV data, compute returns)
├── SignalGenerator (momentum, z-score, etc.)
├── PortfolioConstructor (equal weight, volatility parity)
├── ExecutionSimulator (apply transaction costs, fill prices)
└── PerformanceAnalyzer (Sharpe, drawdown, turnover)
```

## See Also
- [[Quantitative Finance Career Guide]]
- [[Quant Math Foundations]]
- [[Systematic Trading Strategies]]
- [[Machine Learning in Quantitative Finance]]
