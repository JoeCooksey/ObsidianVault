---
type: concept
title: "Machine Learning in Quantitative Finance"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - machine-learning
  - factor-models
  - alternative-data
  - deep-learning
  - overfitting
---

# Machine Learning in Quantitative Finance

The frontier layer of systematic investing. ML is now ubiquitous at Two Sigma, D.E. Shaw, Citadel, WorldQuant, and all major quant hedge funds.

## How ML Fits in the Quant Stack

ML extends traditional quant — it does not replace it:

```
Traditional Quant:
  Hypothesis → Signal → Backtest → Deploy

ML Quant:
  Data (large, messy) → Feature Engineering → Model → Signal → Validation → Deploy
```

The bottleneck shifts from "finding signals" to "validating signal quality" and "preventing overfitting at every stage."

**Prerequisite**: solid [[Quant Math Foundations]] (statistics + linear algebra) before diving into ML for finance. ML without statistics = a machine for generating false discoveries.

---

## 1. Classical ML for Finance (Start Here)

| Method | Primary Quant Application | When to Use |
|--------|--------------------------|-------------|
| **Linear Regression (OLS)** | Factor signal estimation; OLS factor model | When relationship is linear; interpretability matters |
| **Ridge Regression (L2)** | Regularized factor models; many correlated predictors | Many features; multicollinearity between signals |
| **Lasso Regression (L1)** | Sparse factor models; automatic feature selection | Want to select only the most predictive signals |
| **Logistic Regression** | Binary signal (up/down classification) | Simple, interpretable; baseline model |
| **Random Forests** | Non-linear factor combination; feature importance | Many features; want non-linear interactions |
| **Gradient Boosting (XGBoost/LightGBM)** | Cross-sectional return prediction at scale | Best general-purpose signal; currently dominant in competitions |
| **k-NN** | Nearest-neighbor historical pattern matching | Regime identification; analogous period detection |
| **Gaussian Process** | Bayesian prediction with confidence intervals | When uncertainty quantification matters |

**Start here**: Scikit-learn + *Introduction to Statistical Learning* (ISLR, free) covers everything in this table.

---

## 2. Feature Engineering — The Most Important Skill

Raw market data → meaningful features → model input. The quality of features determines the quality of the signal far more than the choice of ML model.

### Price-Based Features

| Feature | Computation | Economic Intuition |
|---------|------------|-------------------|
| Cross-sectional rank of N-day return | Rank stocks by past return | Momentum signal |
| Volatility-scaled return | Return / rolling standard deviation | Normalize signal across different vol regimes |
| Rolling Sharpe | Rolling mean return / rolling std | Risk-adjusted momentum |
| RSI (Relative Strength Index) | Ratio of up-days to down-days, scaled | Overbought/oversold |
| Bollinger Band z-score | (Price − MA) / rolling std | Mean-reversion signal |
| VWAP deviation | (Price − VWAP) / VWAP | Intraday order flow signal |

### Fundamental/Accounting Features

| Feature | Ratio | Factor |
|---------|-------|--------|
| Book-to-Market | Book value / Market cap | Value factor |
| Earnings Yield | Earnings / Market cap | Value factor |
| ROE (Return on Equity) | Net income / Book equity | Quality factor |
| Gross Profit Margin | Gross profit / Revenue | Quality/profitability |
| Asset Growth | Change in total assets | Investment factor (negative predictor) |
| Operating Accruals | Operating income − operating cash flow | Quality; accruals are negative predictor |

### Alternative Data Features (frontier)

| Data Source | Signal Type | Edge |
|------------|------------|------|
| Credit card transactions | Consumer spending by merchant category | GDP/retail nowcasting ahead of releases |
| Satellite imagery | Parking lot occupancy, oil tank levels, shipping | Physical activity before financial data |
| Job postings (LinkedIn, Indeed) | Hiring rate by company/role | Growth/contraction indicator |
| Web traffic (SimilarWeb) | App downloads, website visitors | Revenue proxy for consumer tech |
| News sentiment NLP | Tone of earnings calls, SEC filings | Unusual language → information signal |
| Patent filings | USPTO new patents by company | R&D investment; future pipeline |
| Social sentiment (Reddit/Twitter) | Unusual mention volume + sentiment | Crowded; mostly noise, some signal |

**Key challenge**: Alternative data is expensive (6-figure annual contracts), quickly arbitraged when widely known, and legally complex (material non-public information rules apply).

---

## 3. The Factor Zoo and ML's Role

Over 400 "factors" have been published in academic literature. Most are:
- Statistical noise (result of data mining)
- Correlated proxies for the same underlying risk
- Already arbitraged away by the time of publication

**ML's contribution**: combine 100+ characteristics simultaneously, with non-linear interactions, to construct a single prediction for next-month stock returns — the "ML mega-factor."

**Key paper**: "Empirical Asset Pricing via Machine Learning" (Gu, Kelly, Xiu 2020):
- Tested 94 characteristics across all US stocks 1957–2016
- Gradient boosted trees and neural networks outperformed all linear factor models in Sharpe ratio
- Interpreted results: interaction effects between factors are large; non-linearity matters
- Most important predictors: momentum, short-term reversal, and volatility

---

## 4. Time Series ML for Finance

### Why Financial Time Series Is Hard

| Challenge | Description | Why It Matters |
|-----------|------------|----------------|
| **Non-stationarity** | Statistical properties change over time (regime shifts) | A model trained in 2010–2015 fails in 2020 |
| **Low signal-to-noise** | A Sharpe of 0.5 is "good" signal in finance | Models appear to learn noise |
| **Short effective sample** | 1 market regime ≈ 5 years; 30 years = 6 regimes | Not enough data for complex models |
| **Autocorrelation in labels** | Monthly returns overlap (past 12 months includes past 11) | Standard cross-validation gives misleading results |

### Recurrent Models (LSTM, GRU)
- Handle sequential dependencies in time series
- Used for pattern recognition across time periods
- Still prone to overfitting on financial data; treat results skeptically
- More useful for execution / nowcasting than alpha generation

### Transformer Models for Finance (2024–2026)
- **Temporal Fusion Transformer (TFT)**: strong multi-horizon forecasting; handles covariates
- **TimesFM** (Google, 2024): foundation model for time series; zero-shot forecasting
- **Chronos** (Amazon, 2024): pre-trained time series foundation model
- **PatchTST**: treats time series as patches (like ViT for images); handles long sequences
- Status: very promising in benchmark tests; overfitting risk is still high in finance applications

---

## 5. Reinforcement Learning in Finance

**What it is**: An agent learns to trade by maximizing a cumulative reward signal (P&L, Sharpe ratio) through interactions with a simulated market environment.

**Applications**:

| Application | Status | Firms Using |
|------------|--------|-------------|
| Optimal execution | Production-deployed | All major quant firms |
| Market making | Production-deployed | Jane Street, Optiver, Virtu |
| Portfolio rebalancing | Research/production | Two Sigma, D.E. Shaw |
| Options hedging (RL-based delta) | Research-stage | Academic + some hedge funds |
| Alpha generation | Research-stage; very difficult | Mostly academic |

**Optimal execution with RL**: The classic problem — you need to sell 1M shares of AAPL without moving the price. RL learns to slice the order optimally based on current market state. This is the most mature RL application in finance.

**Frameworks**: OpenAI Gym (environment), Stable Baselines 3 (PPO, SAC, TD3 algorithms), FinRL (finance-specific RL library)

---

## 6. The Overfitting Problem — The #1 Enemy

**Why overfitting is worse in finance than any other ML domain**:
- Financial return labels are extremely noisy (Sharpe 0.5 = "good signal")
- Small effective sample: 30 years of monthly data = 360 points
- Multiple testing: testing 1000 signals → ~50 appear significant by chance even if all are noise
- Overfitting is catastrophic: it means deploying a strategy that looks profitable but isn't

### Correct Validation: PurgedKFold (López de Prado Method)
Standard k-fold cross-validation creates **data leakage** in time series:
- Training set at time t may include information that influenced the test set at t+k (overlapping return windows)
- **PurgedKFold** removes a "purge" buffer between train and test folds, eliminating this leakage
- Essential for monthly return prediction (returns overlap by 11 months in a 12-month lookback)

```python
from mlfinlab.cross_validation import PurgedKFold
cv = PurgedKFold(n_splits=5, n_jobs=1, embargo_pct=0.01)
# embargo_pct removes a gap between train/test
```

### Walk-Forward Validation
- Expand training window monthly → always test on out-of-sample future data
- Simulates real-world conditions: you can only use data available at time of prediction
- The gold standard for testing systematic strategies

### Multiple Testing Correction
If you test N strategies/signals:
- **Bonferroni**: require t-stat > 3.0 (not 2.0) to account for multiple tests
- **False Discovery Rate (Benjamini-Hochberg)**: controls the expected fraction of false discoveries
- **Bailey-López de Prado Theorem**: probability that minimum backtest Sharpe is a false discovery, as a function of number of trials

---

## 7. Key Books and Resources

| Resource | Focus | Level |
|---------|-------|-------|
| *Advances in Financial Machine Learning* — Marcos López de Prado | Backtesting pitfalls, feature engineering, PurgedKFold, meta-labeling | Advanced (read this first) |
| *Machine Learning for Asset Managers* — López de Prado | More concise; clustering, denoising, signal testing | Intermediate |
| *Machine Learning for Algorithmic Trading* — Stefan Jansen | Python-focused; most practical; end-to-end projects | Intermediate |
| *Empirical Asset Pricing via Machine Learning* — Gu, Kelly, Xiu | The foundational academic paper; free on SSRN | Advanced |
| *Introduction to Statistical Learning* (ISLR) — James et al. | Classical ML methods; free PDF | Beginner–Intermediate |
| Kaggle financial competitions | Practice feature engineering + model building | All levels |
| WorldQuant BRAIN platform | Simulate factor research on real data | Intermediate |

---

## Learning Path

1. Scikit-learn fundamentals + ISLR (2 months) — regression, classification, cross-validation basics
2. Feature engineering with Pandas (1 month) — momentum signals, accounting ratios, data cleaning
3. *Advances in Financial Machine Learning* by López de Prado (2 months — the serious text)
4. Implement: OLS factor model → add gradient boosting layer → PurgedKFold validation → compare Sharpe
5. Kaggle: Jane Street Market Prediction competition (historical; great for feature engineering practice)
6. WorldQuant BRAIN: simulate alpha factors on US equities data (free access for students)

## See Also
- [[Quantitative Finance Career Guide]]
- [[Systematic Trading Strategies]]
- [[Quant Math Foundations]]
- [[Quant Programming Stack]]
