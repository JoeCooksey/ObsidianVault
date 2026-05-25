---
type: concept
title: "Derivatives Pricing and Financial Theory"
status: complete
created: 2026-05-22
updated: 2026-05-22
tags:
  - quant
  - derivatives
  - options
  - risk-management
  - black-scholes
  - portfolio-theory
---

# Derivatives Pricing and Financial Theory

The applied financial theory layer of quantitative finance. Built on [[Quant Math Foundations]]. Learn in the sequence below.

## 1. Markets and Instruments (Learn First — Vocabulary)

Before modeling anything, you need the vocabulary of financial markets.

| Instrument | What It Is | Key Quant Concepts |
|-----------|-----------|-------------------|
| **Equity (stocks)** | Ownership stake in a company | Price processes, dividends, total return |
| **Fixed Income (bonds)** | Debt instrument with coupon payments | Yield curves, duration, convexity, credit risk |
| **Futures** | Obligation to buy/sell an asset at a fixed future price | Cost of carry, mark-to-market, basis |
| **Options (calls/puts)** | Right (not obligation) to buy/sell at strike K | Non-linear payoffs, implied volatility, Greeks |
| **Swaps** | Exchange of two cash flow streams | Interest rate risk, LIBOR transition to SOFR |
| **Credit Derivatives** | Exposure to credit events (default) | CDS pricing, CDOs, credit risk modeling |

**Best starting resource**: *Options, Futures and Other Derivatives* by John C. Hull — the industry-standard textbook; used in every MFE program worldwide; Chapters 1–20 are core.

---

## 2. Portfolio Theory

**Why it matters**: Foundation for systematic investing, factor models, risk management, and portfolio construction.

### Markowitz Mean-Variance Optimization
- Choose portfolio weights w to maximize expected return μᵀw for a given variance wᵀΣw
- The **efficient frontier** = the set of portfolios that maximize return for each level of risk
- The **minimum variance portfolio** = lowest-risk fully-invested portfolio
- Math required: quadratic programming with linear constraints (calculus + linear algebra)

**Key formula**: Portfolio variance = wᵀΣw, where Σ is the covariance matrix of returns

**Limitation**: Markowitz is extremely sensitive to estimated expected returns (the "estimation error maximizer" problem); practical applications use robust estimation or Black-Litterman

### CAPM (Capital Asset Pricing Model)
- **Formula**: E[r] = rf + β × (E[rm] − rf)
- β (beta) = Cov(ri, rm) / Var(rm) = sensitivity to market movement
- **Alpha** = actual return − CAPM predicted return = excess return unexplained by market beta
- **Limitation**: single factor; empirically, many other factors also predict returns (size, value, momentum)

### Factor Models
- **Fama-French 3-Factor**: market β + size (SMB) + value (HML); explains ~95% of portfolio variance
- **Fama-French 5-Factor**: adds profitability (RMW) + investment (CMA)
- **Barra Risk Models**: commercial multi-factor models with 50+ risk factors used by most institutional investors
- Factor models decompose risk into: factor risk (rewarded + unrewarded) + idiosyncratic risk

---

## 3. Options Pricing — The Core of Derivatives

### Step 1: Binomial Tree (Start Here)
- Stock can go up (u) or down (d) in each step → risk-neutral probability p
- Risk-neutral pricing: V = e^{-rΔt} [p × Vu + (1−p) × Vd]
- No calculus required; builds deep intuition for risk-neutral pricing
- Converges to Black-Scholes as number of steps → ∞
- **Key insight**: the real-world probability of up/down doesn't matter for pricing — only the risk-neutral probability p

### Step 2: Black-Scholes Model
**Assumptions**:
- Stock price follows Geometric Brownian Motion: dS = μS dt + σS dW
- Constant volatility σ (unrealistic; the biggest assumption)
- No dividends, no transaction costs
- Continuous trading possible, risk-free rate constant

**Derivation (sketch)**:
1. Apply Ito's Lemma to V(S,t) → get the SDE for V
2. Construct a delta-hedged portfolio: Π = V − Δ·S (eliminates randomness)
3. Arbitrage-free → portfolio earns risk-free rate → **Black-Scholes PDE**
4. Solve PDE with terminal condition → closed-form formula

**Black-Scholes Formula (European call)**:
```
C = S·N(d₁) − K·e^{-rT}·N(d₂)

d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d₂ = d₁ − σ√T

P = K·e^{-rT}·N(−d₂) − S·N(−d₁)   [European put]
```
Where N(·) = standard normal CDF, S = spot, K = strike, T = time to expiry, r = risk-free, σ = volatility.

**Put-Call Parity**: C − P = S − K·e^{-rT} (must hold by arbitrage)

### Step 3: Beyond Black-Scholes
Black-Scholes assumes constant volatility σ — but markets imply different σ for different strikes and maturities:

- **Volatility smile**: implied volatility is higher for OTM puts and calls than ATM → Black-Scholes underprices tails
- **Local volatility models**: σ = σ(S,t) — Dupire's equation gives a unique local vol surface matching all market prices
- **Stochastic volatility models**: vol itself follows an SDE; **Heston model** (vol follows CIR process) is the most widely used; SABR model for rates
- **Monte Carlo pricing**: when no closed form exists; simulate thousands of paths → average discounted payoff

---

## 4. The Options Greeks — Risk Decomposition

Greeks are partial derivatives of the option price. Every options trading desk uses Greeks for real-time risk management and P&L attribution.

| Greek | Symbol | Definition | Sign (long call) | Intuition |
|-------|--------|-----------|---------|-----------|
| **Delta** | Δ | ∂V/∂S | +0 to +1 | Moves $Δ per $1 in S |
| **Gamma** | Γ | ∂²V/∂S² | + | Rate of change of Δ; convexity |
| **Theta** | Θ | ∂V/∂t | − | Time decay; option loses value daily |
| **Vega** | ν | ∂V/∂σ | + | Gains $ν per 1% increase in vol |
| **Rho** | ρ | ∂V/∂r | + (call) | Sensitivity to interest rate |

**The P&L decomposition** (fundamental to options trading):
```
ΔP ≈ Δ·ΔS + ½Γ·(ΔS)² + Θ·Δt + ν·Δσ
```
This equation explains exactly where your P&L comes from each day.

**Delta hedging**: Hold −Δ shares per long call to be delta-neutral → first-order neutral to stock price moves. Gamma tells you how fast Δ changes, so how often you must rebalance.

**Vega risk**: long options are long volatility (you benefit if vol rises); short options are short volatility (you benefit if vol falls). Vol trading = buying and selling vega.

---

## 5. Risk Management

### Value-at-Risk (VaR)
- **Definition**: VaR(α, T) = the loss level exceeded with probability (1−α) over horizon T
- **95% 1-day VaR**: only 5% of days should have losses exceeding this number
- **Methods**:
  - *Historical simulation*: use actual historical returns; no distribution assumption; handles fat tails
  - *Parametric*: assume returns are normal; fast; underestimates fat-tail risk
  - *Monte Carlo*: simulate many scenarios; most flexible; computationally expensive
- **Key limitation**: VaR says nothing about how bad losses are when you exceed the threshold (just that you do)

### CVaR / Expected Shortfall (ES)
- **Definition**: Expected loss in the worst (1−α)% of scenarios
- **CVaR = average of losses beyond VaR** — more informative and "coherent"
- Preferred by Basel III / FRTB regulations over VaR; all major banks now report ES

### Greeks-Based Risk (for options books)
- **Delta neutral**: first-order insensitive to stock price
- **Gamma neutral**: second-order insensitive to stock price (large moves hedged)
- **Vega neutral**: insensitive to volatility moves
- **Theta**: unavoidable for long options positions; time decay is a cost of optionality

### Stress Testing
- Apply extreme historical scenarios (2008 GFC, 2020 COVID crash, 1987 Black Monday)
- Test whether the portfolio survives tail events, not just normal markets

---

## Reading Sequence

1. **Hull** (*Options, Futures and Other Derivatives*) — Chapters 1–20 cover everything here; start here
2. **Joshi** (*The Concepts and Practice of Mathematical Finance*) — bridges theory to practice; shows how models are implemented and used
3. **Shreve Vol I** (*Stochastic Calculus for Finance I*) — discrete-time risk-neutral pricing; martingales; rigorous foundation
4. **Shreve Vol II** (*Stochastic Calculus for Finance II*) — continuous-time; Brownian motion; Ito; Black-Scholes from first principles

## Key Formulas to Memorize

| Formula | Context |
|---------|---------|
| C = S·N(d₁) − K·e^{-rT}·N(d₂) | Black-Scholes call price |
| d₁ = [ln(S/K) + (r+σ²/2)T] / σ√T | Black-Scholes d₁ |
| C − P = S − K·e^{-rT} | Put-call parity |
| E[r] = rf + β(E[rm]−rf) | CAPM |
| Var(portfolio) = wᵀΣw | Markowitz portfolio variance |
| ΔP ≈ Δ·ΔS + ½Γ·(ΔS)² + Θ·Δt | P&L attribution |

## See Also
- [[Quant Math Foundations]]
- [[Quantitative Finance Career Guide]]
- [[Systematic Trading Strategies]]
- [[Quant Interview Prep Guide]]
