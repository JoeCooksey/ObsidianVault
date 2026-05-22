---
type: concept
title: "Quant Math Foundations"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - mathematics
  - stochastic-calculus
  - linear-algebra
  - probability
  - statistics
---

# Quant Math Foundations

The mathematical backbone of quantitative finance. Five layers, strictly ordered. Cannot skip ahead. Total self-study time from scratch: 18–30 months.

## Layer 1: Calculus
**Prerequisite**: High school math
**Time**: 4–6 months (from scratch), 1–2 months (if already comfortable)

**Why it matters**: Black-Scholes is a partial differential equation (PDE) — a heat equation in disguise. Portfolio optimization is constrained calculus. Gradient descent in ML is calculus. Ito's Lemma (stochastic calculus) is an extension of the chain rule.

**Key topics**:
- Single-variable: limits, derivatives, chain rule, integration by parts
- Multivariable: partial derivatives, Jacobians, Hessians, gradient
- Optimization: unconstrained minima, Lagrange multipliers, convex functions
- Ordinary and partial differential equations (ODEs / PDEs): separation of variables, heat equation

**Resources**:
- *Calculus* by Stewart (undergrad standard; Chapters 1–15 cover everything needed)
- MIT OCW 18.01 + 18.02 (free lecture videos + problem sets)
- *Mathematics for Finance* by Capinski & Zastawniak (finance-focused bridge; calculus + probability)

**Connection map**:
- Black-Scholes PDE = heat equation (calculus)
- Markowitz optimization = Lagrangian constrained optimization (calculus)
- Gradient descent in ML = partial derivatives (calculus)

---

## Layer 2: Linear Algebra
**Prerequisite**: Calculus (basic)
**Time**: 3–4 months

**Why it matters**: Portfolio variance = wᵀΣw (quadratic form in the covariance matrix). PCA for factor decomposition = eigendecomposition of Σ. Factor models (Fama-French, Barra) are systems of linear equations. Neural network forward passes are matrix multiplications.

**Key topics**:
- Vectors, matrices, matrix multiplication
- Systems of linear equations; Gaussian elimination
- Matrix inversion, determinants
- **Eigenvalues and eigenvectors** (the most important topic for quant applications)
- **Singular Value Decomposition (SVD)** — generalization of eigendecomposition; used for dimensionality reduction
- Positive definite matrices (covariance matrices must be positive semi-definite)
- Least squares regression — normal equation: β = (XᵀX)⁻¹Xᵀy

**Resources**:
- **MIT 18.06 (Prof. Gilbert Strang, free on OCW)** — THE standard; same course serves EE + ML + quant simultaneously
- 3Blue1Brown "Essence of Linear Algebra" (visual intuition first; watch before lectures)
- *Introduction to Linear Algebra* by Strang (textbook companion)

**Connection map**:
- Covariance matrix decomposition → eigenvectors = principal components (risk factors)
- Portfolio optimization → minimize wᵀΣw subject to wᵀμ = target return (quadratic programming)
- Regression → normal equation; regularized regression → ridge/lasso
- Neural networks → matrix multiplications at each layer

---

## Layer 3: Probability Theory
**Prerequisite**: Calculus + Linear Algebra
**Time**: 4–6 months

**Why it matters**: Every financial model is a probability model. Quant interviews are 50%+ probability problems. Option pricing = discounted expected payoff under risk-neutral measure. Risk management = tails of probability distributions.

**Key topics**:
- Probability spaces, sample spaces, events, axioms
- Conditional probability, independence, Bayes' theorem
- Discrete distributions: Bernoulli, Binomial, Geometric, Poisson, Hypergeometric
- Continuous distributions: Uniform, Normal, Log-Normal, Exponential, Gamma
- Expectation, variance, covariance, correlation
- Law of Large Numbers (LLN) + Central Limit Theorem (CLT) — the foundations of backtesting
- Moment generating functions, characteristic functions
- **Martingales** — the mathematical definition of a "fair game"; prerequisite for stochastic calculus
- **Markov chains** — memoryless processes; used in transition probability models

**Resources**:
- *A First Course in Probability* by Sheldon Ross (the gold standard; highly recommended)
- MIT OCW 18.600 (Probability, free)
- *Probability and Statistics for Engineers and Scientists* by Walpole (applied; good for intuition)

**Connection map**:
- Risk-neutral pricing: V(t) = e^{-r(T-t)} Eᴼ[payoff | Fₜ] — discounted expectation
- CLT → justifies normal approximations in risk models (and shows their limits)
- Bayes' theorem → signal updating, Bayesian portfolio construction, Kalman filter
- Martingales → underpins risk-neutral measure, no-arbitrage arguments

---

## Layer 4: Mathematical Statistics
**Prerequisite**: Probability Theory
**Time**: 4–6 months

**Why it matters**: Factor signal construction is regression. Backtesting validity requires hypothesis testing. Financial returns are a time series. ML is applied statistics with large datasets.

**Key topics**:
- Point estimation: Maximum Likelihood (MLE), method of moments
- Confidence intervals, hypothesis testing, p-values
- Type I and Type II errors; statistical power
- **Multiple testing correction** — Bonferroni, FDR (Benjamini-Hochberg); critical for backtesting (testing 1000 strategies → ~50 appear significant by chance)
- **Linear regression** (OLS, GLS, Ridge, Lasso, Elastic Net)
- **Time series analysis**: AR, MA, ARMA, ARIMA; stationarity (ADF test); autocorrelation (ACF/PACF)
- GARCH models for volatility clustering (financial returns have fat tails + clustered volatility)
- Principal Component Analysis (PCA) — connect to LA Layer 2
- Cointegration — key for pairs trading; Engle-Granger and Johansen tests

**Resources**:
- *Statistics* by Freedman, Pisani & Purves (intuition-first; best first read)
- *Introduction to Statistical Learning* (ISLR, free PDF at statlearning.com) — bridges stats and ML
- *Analysis of Financial Time Series* by Ruey Tsay (applied financial time series)
- MIT OCW 18.650 (Statistics, free)

**Connection map**:
- OLS regression → factor signal construction; Fama-French factor estimation
- Multiple testing → the reason most backtests are false positives
- GARCH → volatility forecasting for risk management and options pricing
- Cointegration → statistical foundation of pairs trading
- PCA → factor decomposition in multi-factor risk models

---

## Layer 5: Stochastic Calculus
**Prerequisite**: All four layers above
**Time**: 6–12 months

**Why it matters**: This is the core mathematics of derivatives pricing. Black-Scholes is derived from Ito's Lemma applied to a Geometric Brownian Motion model. Every exotic option, interest rate model, and credit derivative is built on this foundation.

**Key topics**:
- **Brownian Motion (Wiener Process)**: continuous-time random walk; properties (independent increments, normal increments, continuous paths)
- Filtrations and information: the mathematical framework for "information revealed over time"
- **Martingales** in continuous time: the fair-game property; why risk-neutral prices are martingales
- **Ito's Lemma** (the stochastic chain rule): if X follows an SDE, what does f(X) follow? This is how you derive the BS PDE.
- **Stochastic Differential Equations (SDEs)**:
  - Geometric Brownian Motion: dS = μS dt + σS dW (stock price model under Black-Scholes)
  - Ornstein-Uhlenbeck: mean-reverting SDE (used in pairs trading, rates models)
  - Cox-Ingersoll-Ross (CIR): positive mean-reverting SDE (interest rate model)
- **Change of measure (Girsanov's theorem)**: the mathematical tool that converts real-world measure P to risk-neutral measure Q; the key to no-arbitrage pricing
- **Black-Scholes PDE derivation**: construct a hedged portfolio → eliminate randomness → derive the PDE → solve for option price
- Feynman-Kac theorem: connects PDEs (Black-Scholes) to expected values under risk-neutral measure

**Resources**:
- **Shreve Vol I** (*Stochastic Calculus for Finance I* — Binomial tree model; discrete-time foundation; read first)
- **Shreve Vol II** (*Stochastic Calculus for Finance II* — Brownian motion, Ito calculus, Black-Scholes from first principles; the graduate-level bible)
- *Financial Calculus* by Baxter & Rennie (more intuitive, shorter; good before Shreve)
- *Introduction to Mathematical Finance* by Pliska (more concise alternative to Shreve)

**Connection map**:
- Ito's Lemma + GBM → Black-Scholes PDE → option pricing formula
- Girsanov → risk-neutral pricing of any derivative
- OU process → pairs trading (mean-reversion speed estimation)
- CIR model → interest rate derivatives, credit models

---

## The Complete Dependency Graph

```
High School Math
    ↓
Layer 1: Calculus (4–6 months)
    ↓                ↓
Layer 2: Linear Algebra    (parallel)
(3–4 months)
    ↓
Layer 3: Probability Theory (4–6 months)
    ↓
Layer 4: Mathematical Statistics (4–6 months, start during Layer 3)
    ↓
Layer 5: Stochastic Calculus (6–12 months — the summit)
```

## Critical Concept Cross-Reference

| Math Concept | Quant Finance Application |
|-------------|--------------------------|
| Eigenvalues / SVD | Covariance decomposition, PCA, factor models |
| Least squares (OLS) | Factor signal construction, regression |
| CLT | Justification for normal approximation in risk models |
| Bayes' theorem | Signal updating, Kalman filter, Bayesian portfolio |
| Martingale | Risk-neutral pricing, no-arbitrage arguments |
| Ito's Lemma | Black-Scholes PDE, any derivative pricing |
| GARCH | Volatility modeling and forecasting |
| Cointegration | Pairs trading, stat arb strategy construction |
| Multiple testing | Why most backtests are false; Bonferroni correction |
| OU Process | Pairs trading mean-reversion speed; short rates |

## See Also
- [[Quantitative Finance Career Guide]]
- [[Derivatives Pricing and Financial Theory]]
- [[Systematic Trading Strategies]]
- [[Quant Interview Prep Guide]]
