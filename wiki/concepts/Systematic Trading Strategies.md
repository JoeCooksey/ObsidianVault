---
type: concept
title: "Systematic Trading Strategies"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - trading
  - strategies
  - momentum
  - mean-reversion
  - factor-models
  - backtesting
---

# Systematic Trading Strategies

The strategy synthesis layer of quantitative finance. Built on math + programming + financial theory.

## Strategy Taxonomy

```
Systematic Strategies
├── Momentum / Trend Following
│   ├── Time-series momentum (asset vs. own history)
│   └── Cross-sectional momentum (rank assets vs. each other)
├── Mean Reversion
│   ├── Pairs trading (cointegration-based)
│   └── Statistical arbitrage (many pairs simultaneously)
├── Factor Investing
│   ├── Value, Size, Momentum, Quality, Low Vol (classic)
│   └── ML-constructed factors (modern)
├── Market Making
│   ├── Bid-ask spread capture
│   └── Inventory management via quote skewing
└── Volatility Strategies
    ├── Variance swaps / volatility surface trading
    └── Gamma scalping / delta hedging
```

---

## 1. Momentum / Trend Following

**Core idea**: Assets that have recently outperformed continue to outperform over medium horizons (1–12 months). Conversely, recent losers continue to lose.

**Why it works**: Behavioral finance explains momentum. Investors underreact to news (anchoring), institutions are slow to rebalance, herding creates price trends. Jegadeesh & Titman (1993) is the foundational paper.

**Variants**:

| Type | Description | Holding Period |
|------|------------|----------------|
| Cross-sectional momentum | Rank all stocks by past N-month return; long top quintile, short bottom quintile | 1–3 months |
| Time-series momentum | Buy if asset is above its own N-month average; sell if below | 1–12 months |
| Trend following (CTAs) | Apply time-series momentum to futures across asset classes | 1–12 months |

**Key parameters**: lookback window (1–12 months), skip period (avoid 1-month reversal effect), rebalancing frequency (monthly standard)

**Momentum crash risk**: Momentum portfolios can crash catastrophically during sharp reversals (Jan 2009, March 2020). The losers being shorted are often severely distressed stocks with short-squeeze potential. Must size positions carefully and use stop-losses.

**Implementation**:
```python
# Cross-sectional momentum: monthly rebalance
lookback = 252  # 12-month lookback (252 trading days)
skip = 21       # skip last month (1-month reversal effect)
signal = returns.rolling(lookback).sum().shift(skip)
# Long top 20%, short bottom 20%
long_mask = signal.rank(axis=1, pct=True) > 0.8
short_mask = signal.rank(axis=1, pct=True) < 0.2
```

---

## 2. Mean Reversion / Pairs Trading

**Core idea**: Related assets (or spreads between assets) revert to a long-run equilibrium. Temporary divergences are tradeable.

**Why it works**: Co-integrated pairs have a long-run economic relationship (e.g., Coca-Cola/Pepsi compete for the same dollars; Gold/Silver have historically similar supply/demand curves). Temporary divergences are mispricings that get arbitraged away.

### Statistical Foundation: Cointegration
Two series X and Y are **cointegrated** if a linear combination Z = X − β·Y is stationary (has a constant mean it reverts to). This is stronger than correlation — two random walks can be uncorrelated but cointegrated.

**Step 1: Find cointegrated pairs**
```python
from statsmodels.tsa.stattools import coint
score, pvalue, _ = coint(price_series_1, price_series_2)
if pvalue < 0.05:
    print("Pair is cointegrated at 95% confidence")
```

**Step 2: Estimate hedge ratio**
```python
from sklearn.linear_model import LinearRegression
β = LinearRegression().fit(X.reshape(-1,1), Y).coef_[0]
spread = Y - β * X
```

**Step 3: Trade on z-score**
```python
z = (spread - spread.rolling(60).mean()) / spread.rolling(60).std()
long_entry  = z < -2.0   # buy spread (Y cheap relative to X)
short_entry = z >  2.0   # sell spread (Y expensive relative to X)
exit_signal = abs(z) < 0.5  # exit when spread reverts
```

**Risk**: pairs can diverge permanently (regime change, M&A, fundamental shift in one company). Must set hard stop-losses, track cointegration stability.

---

## 3. Factor Investing

**Core idea**: Systematic exposure to quantifiable risk factors earns long-run risk premia. A factor is a characteristic of a stock that predicts its future return.

### Classic Factors (Fama-French)

| Factor | Construction | Economic Rationale |
|--------|-------------|-------------------|
| **Market (β)** | Long stocks, short T-bills | Equity risk premium for holding market risk |
| **Size (SMB)** | Long small-cap, short large-cap | Small-cap illiquidity + higher risk premium |
| **Value (HML)** | Long high book/price, short low book/price | Mean reversion of fundamentals; cheap vs. expensive |
| **Momentum (WML)** | Long past 12-month winners, short losers | Behavioral underreaction to information |
| **Profitability (RMW)** | Long high profitability, short low profitability | Quality premium; productive firms outperform |
| **Investment (CMA)** | Long low asset growth, short high asset growth | Conservative firms outperform aggressive investors |

### How to Build a Factor

1. Define a stock characteristic (e.g., book-to-market ratio)
2. At end of each month, rank all stocks by that characteristic
3. Long top quintile, short bottom quintile (zero-cost long-short portfolio)
4. Track monthly return of this portfolio → the **factor return**
5. Risk-adjust by regressing on known factors (is this "alpha" or just market risk?)
6. Measure IC (Information Coefficient = correlation of signal with next-period return)

**Alpha decay**: As a factor becomes widely known and published, its returns get arbitraged away. Research alpha typically decays from publication. The edge lies in early discovery and proprietary signal construction.

### Portfolio Construction from Factors

- **Equal weight factors**: simple but ignores factor correlations
- **Risk parity**: weight factors by inverse of volatility; equalizes risk contribution
- **Mean-variance optimization**: Markowitz on factor returns; requires estimating factor covariance matrix
- **Hierarchical Risk Parity (HRP)**: graph-based clustering; more robust than Markowitz

---

## 4. Statistical Arbitrage (StatArb)

**Core idea**: Simultaneously buy underpriced securities and sell overpriced securities, earning the convergence when prices normalize.

**Difference from pairs trading**: StatArb operates across many pairs simultaneously (50–500 positions), relies on diversification to control risk, typically shorter holding periods (days to weeks).

**Common forms**:

| Type | Description |
|------|------------|
| **ETF arbitrage** | ETF price vs. NAV of underlying basket; market makers arbitrage intraday |
| **Index rebalancing** | Stocks added to S&P 500 must be bought by all index funds → anticipate demand |
| **Dual-listed stocks** | Same company on two exchanges; identical claims must converge |
| **Convertible bond arb** | Exploit mispricings between convertible bonds and the underlying equity |

---

## 5. Market Making

**Core idea**: Post bid and ask quotes simultaneously. Earn the bid-ask spread from uninformed order flow. Manage inventory risk from directional price moves.

**P&L decomposition**:
```
P&L = (spread earned × volume) − (adverse selection losses) − (inventory risk costs)
```

**Key concepts**:
- **Adverse selection**: informed traders (who know where the price is going) will always trade against you when your quote is stale or wrong. This is the main risk.
- **Inventory management**: if you accumulate too much long or short inventory, your risk grows. Skew your quotes to attract inventory-reducing trades.
- **Order book dynamics**: queue priority, level 2 depth, order flow toxicity (how much flow is informed vs. uninformed)
- **Avellaneda-Stoikov model**: the optimal market-making model; provides closed-form bid/ask quote policies as a function of inventory and time

**Who does this**: Jane Street, Optiver, IMC, Virtu, HRT, Citadel Securities. Market making is the most profitable quant strategy per capital deployed — but requires exchange memberships, capital, and ultra-low-latency infrastructure.

---

## Backtesting: The Most Critical Skill

A strategy is only as good as the rigor of its backtest. Most quant strategies fail in live trading because of backtesting errors.

### The Seven Deadly Sins of Backtesting

| Sin | Description | Fix |
|-----|------------|-----|
| **Look-ahead bias** | Using data at time t that wasn't available until t+k | Always shift signals by at least 1 period |
| **Survivorship bias** | Testing only on stocks that still exist | Use databases including delisted stocks |
| **Transaction cost neglect** | Ignoring bid-ask spreads, market impact | Add realistic costs; kills most "profitable" retail strategies |
| **Overfitting** | Too many parameters tuned on historical data | Out-of-sample test set; keep strategy simple |
| **Data snooping** | Testing many strategies on same data | Multiple testing correction (Bonferroni / FDR) |
| **Regime ignorance** | Strategy trained in one market regime fails in another | Test across multiple market regimes |
| **Capacity blindness** | Strategy profitable at $1M but kills itself at $100M | Measure market impact; test at realistic AUM |

### Walk-Forward Validation (the correct approach)
- Train on 60% of data → validate on 20% (tune parameters) → test on final 20% (never touch until final evaluation)
- Walk-forward: expand training window forward in time; re-validate monthly
- Never look at the test set until the strategy is completely final

### Key Performance Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Sharpe Ratio** | (mean_return − rf) / std × √252 | >1.0 acceptable; >2.0 excellent |
| **Sortino Ratio** | (mean_return − rf) / downside_std × √252 | Higher = better; penalizes only downside risk |
| **Max Drawdown** | Peak-to-trough % loss | <20% for most institutional strategies |
| **Calmar Ratio** | Annualized return / Max Drawdown | >1.0 acceptable |
| **Information Coefficient** | Corr(signal, next-period return) | >0.05 is meaningful alpha |
| **t-statistic** | mean_IC / std_IC × √N | >2.0 for 95% significance |

---

## Key Books

| Book | Focus | Level |
|------|-------|-------|
| *Algorithmic Trading* — Ernest Chan | Practical Python backtesting; momentum + mean reversion | Beginner–Intermediate |
| *Quantitative Trading* — Ernest Chan | Strategy selection, position sizing, execution | Beginner–Intermediate |
| *Active Portfolio Management* — Grinold & Kahn | Factor investing bible; IC, IR, the Fundamental Law | Intermediate–Advanced |
| *Trading Evolved* — Andreas Clenow | Trend following implementation; Python; CTAs | Intermediate |
| *Advances in Financial Machine Learning* — López de Prado | Backtesting pitfalls, ML signals, PurgedKFold | Advanced |
| *Pairs Trading* — Ganapathy Vidyamurthy | Statistical arbitrage theory and implementation | Intermediate |

## See Also
- [[Quantitative Finance Career Guide]]
- [[Quant Math Foundations]]
- [[Machine Learning in Quantitative Finance]]
- [[Quant Programming Stack]]
- [[Derivatives Pricing and Financial Theory]]
