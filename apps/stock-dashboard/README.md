# 📈 Stock Dashboard

A local web app that pulls real-time(ish) stock data and lays out **all the
information that matters** — organized by the four decision layers from the
vault's investing notes.

| Layer | Question | Vault source |
|-------|----------|--------------|
| ① Fundamentals | *What* to own, at what price? | [[Fundamental Analysis Valuation Metrics]] |
| ② Technicals | *When* to act? | [[Technical Analysis Indicators]] |
| ③ Position Sizing | *How much* to risk? | [[Position Sizing and Risk Management]] |
| ④ Sell Discipline / Margin of Safety | *When* to exit? | [[Sell Discipline (When to Sell a Stock)]], [[Margin of Safety (Finance)]] |

## What it shows

- **Live header** — price, change, market cap, 52-week range, beta, dividend yield, business summary.
- **Fundamentals** — P/E, forward P/E, PEG, P/B, P/S, FCF yield, ROE, margins,
  debt/equity, current ratio, earnings & revenue growth — each with the vault's
  rule-of-thumb flags (e.g. PEG < 1 = cheap-for-growth, > 2 = over-optimistic).
- **Technicals** — 50/200-day SMA, golden/death cross detection, RSI(14),
  MACD vs signal, 60-day support/resistance, volume vs average, 120-day sparkline.
- **Position-sizing calculator** — enter capital, risk %, entry, stop → max shares
  (1–2% risk rule) with concentration warnings.
- **Margin of safety** — price vs analyst target range + the 5-point sell-rule checklist.

## Run it

Double-click **`run.bat`** (first run creates a venv and installs deps), or manually:

```powershell
cd apps\stock-dashboard
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5057>.

## Caveats (from the vault)

- Data is via **yfinance** (Yahoo, ~15-min delayed, scraped) — directional, not audited.
- **No single ratio is reliable alone**; P/E is distorted by buybacks, debt, one-offs, the cycle.
- A "cheap" stock can be a **value trap**. Analyst targets are opinions.
- **Valuation is judgment, not arithmetic** — for most people, index funds + sizing +
  a written sell rule beats stock-picking (~90% of active managers lose to the index).
