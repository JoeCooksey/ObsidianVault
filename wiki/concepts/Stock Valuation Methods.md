---
type: concept
title: "Stock Valuation Methods"
created: 2026-05-24
updated: 2026-05-24
tags:
  - investing
  - finance
  - valuation
  - DCF
  - stocks
status: complete
---

# Stock Valuation Methods

Valuation answers one question: **Am I paying a fair price?** A great company bought at too high a price will underperform. Two approaches: intrinsic value (what it's worth in absolute terms) and relative value (what similar companies are trading at).

**Buffett Rule:** It is far better to buy a wonderful company at a fair price than a fair company at a wonderful price.

---

## Approach 1: Intrinsic Valuation — Discounted Cash Flow (DCF)

**Theory:** A company's value equals the present value of all future cash flows it will generate, discounted at the appropriate rate.

**Formula:**
```
Intrinsic Value = Sum of (FCF_t / (1 + WACC)^t) + Terminal Value
```

Where:
- FCF_t = Free Cash Flow in year t
- WACC = Weighted Average Cost of Capital (discount rate)
- Terminal Value = value after the explicit forecast period

### Step-by-Step DCF

**Step 1: Forecast Free Cash Flow (typically 5–10 years)**
- Start from current FCF
- Apply expected annual growth rate (be conservative — use two scenarios)
- FCF = Operating Cash Flow − Capex

**Step 2: Choose a Discount Rate (WACC)**
- Typical range: 8–12% for US companies
- Higher risk = higher discount rate = lower valuation
- WACC = (E/V × Re) + (D/V × Rd × (1−Tax))

**Step 3: Calculate Terminal Value**
- Represents all cash flows beyond your forecast window
- Two methods: Gordon Growth Model (FCF × (1+g) / (WACC−g)) or Exit Multiple
- Terminal value often represents 60–80% of total DCF value — be careful here

**Step 4: Discount Back and Sum**
- Add all discounted FCFs + discounted terminal value
- = Intrinsic Enterprise Value
- Subtract net debt, divide by shares = intrinsic value per share

### DCF Pros and Cons
| Pros | Cons |
|---|---|
| Theoretically correct | Extremely sensitive to WACC and growth assumptions |
| Forces you to think about fundamentals | Garbage in = garbage out |
| Captures long-term value | Terminal value can overwhelm the model |
| Flexible for any business | Hard to verify assumptions |

**Rule:** The DCF is a sanity check, not a precise answer. A DCF that says "$47.38 intrinsic value" is false precision. Use ranges: bull/base/bear case. If all three cases suggest the stock is cheap, that's meaningful.

---

## Approach 2: Relative Valuation — Multiples

Compare the company to similar businesses using standardized ratios. Most practiced by professionals because it anchors to current market reality.

### The 6 Core Multiples

#### P/E Ratio (Price-to-Earnings)
**Formula:** Stock Price / Earnings Per Share (EPS)
- Most widely used ratio
- Tells you how much investors are paying per dollar of profit
- **High P/E** = market expects high future growth OR stock is overvalued
- **Low P/E** = slow growth expected, distressed, or undervalued
- Limitation: can be manipulated via accounting; doesn't account for debt

| P/E Range | Typical Interpretation |
|---|---|
| <10 | Value/distressed territory; check why |
| 10–20 | Fair value for stable businesses |
| 20–35 | Growth premium; needs sustained high growth |
| >40 | High growth expected; no room for error |

Compare to: (1) historical average for this stock, (2) industry average, (3) S&P 500 average (~18–22× historically)

#### Forward P/E
- P/E using next 12 months' expected earnings (consensus estimates)
- More relevant than trailing P/E for growth companies

#### EV/EBITDA (Enterprise Value to EBITDA)
**Formula:** (Market Cap + Net Debt) / EBITDA

Most preferred multiple among professional analysts — better than P/E because:
- Capital structure neutral (accounts for debt)
- Removes accounting differences (taxes, depreciation)
- Makes cross-industry comparison easier

**EBITDA** = Earnings Before Interest, Taxes, Depreciation & Amortization

| EV/EBITDA | Interpretation |
|---|---|
| <6× | Potentially cheap |
| 6–12× | Normal for mature companies |
| 12–20× | Growth premium |
| >20× | High growth / aggressive pricing |

Rule: Use EV/EBITDA when comparing companies with different debt levels (e.g., comparing a leveraged buyout target vs. a debt-free tech company).

#### Price-to-Sales (P/S)
**Formula:** Market Cap / Annual Revenue
- Best for unprofitable or early-stage growth companies
- Not useful for profitable mature companies
- "Rule of thumb" for SaaS: P/S should roughly equal growth rate (e.g., 30% growth → ~10× P/S is fair)

#### Price-to-Book (P/B)
**Formula:** Market Cap / Book Value (Shareholders' Equity)
- Best for financial companies (banks, insurance) where assets = the business
- P/B < 1 = stock trading below asset value (potential deep value)
- Less useful for asset-light tech/services companies

#### FCF Yield
**Formula:** Free Cash Flow / Market Cap
- Conceptual inverse of P/FCF
- FCF yield > 5% = company is generating significant cash relative to price
- FCF yield > 8–10% = potentially undervalued, especially for stable businesses

---

## Sector-Specific Multiples

| Sector | Preferred Multiple | Why |
|---|---|---|
| Technology (SaaS) | EV/Revenue, EV/ARR | Often unprofitable; revenue is the metric |
| Banks / Financials | P/B, P/E | Assets = business; book value matters |
| Real Estate (REITs) | P/FFO, Dividend Yield | REIT cash flow is funds from operations, not EPS |
| Mining / Oil & Gas | EV/EBITDA, P/NAV | Commodity cycles distort earnings |
| Pharma | P/E, P/R&D pipeline | Patent cliff and pipeline value dominate |
| Utilities | P/E, Dividend Yield | Regulated, stable, income-oriented |

---

## Applying Both Approaches Together

**Best practice:**
1. Use DCF to anchor your estimate of intrinsic value (use base/bull/bear cases)
2. Use multiples to check whether the market agrees or disagrees — and why
3. Look for "double confirmation" — stock cheap on DCF AND trades at discount to peers → highest conviction
4. If multiples say cheap but DCF says expensive (or vice versa), investigate why

### The Margin of Safety (Benjamin Graham)
Buy at a meaningful discount to your estimated intrinsic value. If you estimate fair value at $100/share, consider buying only below $70–80. This margin protects against:
- Your estimate being wrong
- Short-term price volatility
- Black swan events

**Graham's original rule:** Buy stocks trading at a 33% or greater discount to intrinsic value.

---

## Quick Valuation Checklist

Before buying, answer:
- [ ] What P/E is this company trading at vs. historical average and industry peers?
- [ ] What EV/EBITDA vs. peers?
- [ ] What does the DCF base case say? (rough 3-scenario range)
- [ ] What is the FCF yield? Is it above 5%?
- [ ] What growth rate does the current price imply? Is that realistic?
- [ ] What is the bear case — if growth slows, how bad does the stock fall?
- [ ] Do I have a margin of safety?

## Related Pages
- [[Company Investment Due Diligence Master Guide]]
- [[Financial Statement Analysis for Investors]]
- [[Key Financial Ratios for Investors]]
- [[Derivatives Pricing and Financial Theory]]
- [[Quantitative Finance Career Guide]]
