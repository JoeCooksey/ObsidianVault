"""
Stock Dashboard — real-time stock report built around Joe's Vault framework.

Decision layers (from the vault):
  1. Fundamentals       — WHAT to own   (Fundamental Analysis Valuation Metrics)
  2. Technicals         — WHEN to act   (Technical Analysis Indicators)
  3. Position Sizing    — HOW MUCH      (Position Sizing and Risk Management)
  4. Sell Discipline    — WHEN to exit  (Sell Discipline / Margin of Safety)

Data source: yfinance (free, no API key). Numbers are delayed ~15 min and
scraped from Yahoo — treat as directional, not audited.
"""

from __future__ import annotations

import math
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _num(x):
    """Return a clean float or None (NaN/inf/None all collapse to None)."""
    if x is None:
        return None
    try:
        f = float(x)
    except (TypeError, ValueError):
        return None
    if math.isnan(f) or math.isinf(f):
        return None
    return f


def _pct(x):
    v = _num(x)
    return None if v is None else round(v * 100, 2)


def flag(level, text):
    """level: 'good' | 'warn' | 'bad' | 'info'."""
    return {"level": level, "text": text}


# --------------------------------------------------------------------------- #
# Technical indicators (computed from price history)
# --------------------------------------------------------------------------- #
def rsi(series: pd.Series, period: int = 14):
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gain / loss
    out = 100 - (100 / (1 + rs))
    return out


def macd(series: pd.Series, fast=12, slow=26, signal=9):
    ema_fast = series.ewm(span=fast, adjust=False).mean()
    ema_slow = series.ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    hist = macd_line - signal_line
    return macd_line, signal_line, hist


def build_technicals(hist: pd.DataFrame):
    if hist is None or hist.empty or len(hist) < 30:
        return None

    close = hist["Close"].dropna()
    price = float(close.iloc[-1])

    sma50 = float(close.rolling(50).mean().iloc[-1]) if len(close) >= 50 else None
    sma200 = float(close.rolling(200).mean().iloc[-1]) if len(close) >= 200 else None

    rsi_series = rsi(close)
    rsi_val = _num(rsi_series.iloc[-1])

    macd_line, signal_line, hist_line = macd(close)
    macd_val = _num(macd_line.iloc[-1])
    signal_val = _num(signal_line.iloc[-1])
    macd_hist = _num(hist_line.iloc[-1])

    # Golden / death cross: did the 50 cross the 200 in the last ~10 sessions?
    cross = None
    if len(close) >= 205:
        s50 = close.rolling(50).mean()
        s200 = close.rolling(200).mean()
        diff = (s50 - s200).dropna()
        recent = diff.iloc[-10:]
        if (recent.iloc[0] < 0) and (recent.iloc[-1] > 0):
            cross = "golden"
        elif (recent.iloc[0] > 0) and (recent.iloc[-1] < 0):
            cross = "death"

    # Support / resistance from recent swing low/high (last ~60 sessions)
    window = close.iloc[-60:]
    support = float(window.min())
    resistance = float(window.max())

    # Volume confirmation
    vol = hist["Volume"].dropna()
    last_vol = float(vol.iloc[-1]) if len(vol) else None
    avg_vol = float(vol.rolling(20).mean().iloc[-1]) if len(vol) >= 20 else None
    vol_ratio = (last_vol / avg_vol) if (last_vol and avg_vol) else None

    flags = []
    # Trend vs 200-day
    if sma200:
        if price > sma200:
            flags.append(flag("good", f"Price is above the 200-day SMA (${sma200:,.2f}) — long-term uptrend."))
        else:
            flags.append(flag("bad", f"Price is below the 200-day SMA (${sma200:,.2f}) — long-term downtrend."))
    # Cross events
    if cross == "golden":
        flags.append(flag("good", "Golden cross — 50-day crossed above 200-day (bullish)."))
    elif cross == "death":
        flags.append(flag("bad", "Death cross — 50-day crossed below 200-day (bearish)."))
    # RSI
    if rsi_val is not None:
        if rsi_val > 70:
            flags.append(flag("warn", f"RSI {rsi_val:.0f} — overbought (>70), possible pullback."))
        elif rsi_val < 30:
            flags.append(flag("warn", f"RSI {rsi_val:.0f} — oversold (<30), possible bounce."))
        else:
            flags.append(flag("info", f"RSI {rsi_val:.0f} — neutral (30–70)."))
    # MACD
    if macd_val is not None and signal_val is not None:
        if macd_val > signal_val:
            flags.append(flag("good", "MACD above its signal line — momentum positive."))
        else:
            flags.append(flag("warn", "MACD below its signal line — momentum negative."))
    # Volume
    if vol_ratio is not None and vol_ratio > 1.5:
        flags.append(flag("info", f"Volume {vol_ratio:.1f}× the 20-day average — moves more reliable on high volume."))

    return {
        "price": round(price, 2),
        "sma50": round(sma50, 2) if sma50 else None,
        "sma200": round(sma200, 2) if sma200 else None,
        "rsi": round(rsi_val, 1) if rsi_val is not None else None,
        "macd": round(macd_val, 3) if macd_val is not None else None,
        "macd_signal": round(signal_val, 3) if signal_val is not None else None,
        "macd_hist": round(macd_hist, 3) if macd_hist is not None else None,
        "cross": cross,
        "support": round(support, 2),
        "resistance": round(resistance, 2),
        "vol_ratio": round(vol_ratio, 2) if vol_ratio else None,
        "flags": flags,
        "spark": [round(float(x), 2) for x in close.iloc[-120:].tolist()],
    }


# --------------------------------------------------------------------------- #
# Fundamentals
# --------------------------------------------------------------------------- #
def build_fundamentals(info: dict):
    market_cap = _num(info.get("marketCap"))
    fcf = _num(info.get("freeCashflow"))
    fcf_yield = _pct(fcf / market_cap) if (fcf and market_cap) else None

    trailing_pe = _num(info.get("trailingPE"))
    forward_pe = _num(info.get("forwardPE"))
    peg = _num(info.get("trailingPegRatio")) or _num(info.get("pegRatio"))
    pb = _num(info.get("priceToBook"))
    ps = _num(info.get("priceToSalesTrailing12Months"))

    debt_to_equity = _num(info.get("debtToEquity"))
    roe = _pct(info.get("returnOnEquity"))
    profit_margin = _pct(info.get("profitMargins"))
    gross_margin = _pct(info.get("grossMargins"))
    op_margin = _pct(info.get("operatingMargins"))
    earnings_growth = _pct(info.get("earningsGrowth"))
    revenue_growth = _pct(info.get("revenueGrowth"))
    current_ratio = _num(info.get("currentRatio"))

    flags = []
    # PEG (vault rule: <1 cheap-for-growth, >2 over-optimistic)
    if peg is not None:
        if peg < 1:
            flags.append(flag("good", f"PEG {peg:.2f} (<1) — potentially undervalued for its growth."))
        elif peg > 2:
            flags.append(flag("warn", f"PEG {peg:.2f} (>2) — may be over-optimistic / priced for perfection."))
        else:
            flags.append(flag("info", f"PEG {peg:.2f} — growth roughly fairly priced."))
    # FCF yield (real cash, hard to fake)
    if fcf_yield is not None:
        if fcf_yield >= 5:
            flags.append(flag("good", f"FCF yield {fcf_yield:.1f}% — strong real cash generation vs price."))
        elif fcf_yield < 0:
            flags.append(flag("bad", f"FCF yield {fcf_yield:.1f}% — burning cash."))
        else:
            flags.append(flag("info", f"FCF yield {fcf_yield:.1f}%."))
    # Moat proxy: ROE + margins
    if roe is not None and roe >= 15:
        flags.append(flag("good", f"ROE {roe:.0f}% — high return on equity, possible competitive moat."))
    elif roe is not None and roe < 0:
        flags.append(flag("bad", f"ROE {roe:.0f}% — destroying shareholder equity."))
    if gross_margin is not None and gross_margin >= 40:
        flags.append(flag("good", f"Gross margin {gross_margin:.0f}% — pricing power."))
    # Balance sheet / leverage
    if debt_to_equity is not None:
        # yfinance reports D/E as a percentage-like number (e.g. 150 = 1.5x)
        de_x = debt_to_equity / 100 if debt_to_equity > 5 else debt_to_equity
        if de_x > 2:
            flags.append(flag("bad", f"Debt-to-equity {de_x:.2f}× — heavy leverage amplifies bankruptcy risk."))
        elif de_x > 1:
            flags.append(flag("warn", f"Debt-to-equity {de_x:.2f}× — meaningful leverage."))
        else:
            flags.append(flag("good", f"Debt-to-equity {de_x:.2f}× — conservative balance sheet."))
    # Growth
    if earnings_growth is not None:
        if earnings_growth > 0:
            flags.append(flag("good", f"Earnings growth {earnings_growth:.0f}% YoY."))
        else:
            flags.append(flag("warn", f"Earnings growth {earnings_growth:.0f}% YoY — shrinking profits."))

    return {
        "metrics": [
            {"label": "Trailing P/E", "value": trailing_pe, "fmt": "x",
             "hint": "$ paid per $1 of annual profit. Compare to own history, peers, market."},
            {"label": "Forward P/E", "value": forward_pe, "fmt": "x",
             "hint": "P/E on next-year expected earnings."},
            {"label": "PEG", "value": peg, "fmt": "x",
             "hint": "P/E adjusted for growth. <1 cheap-for-growth, >2 over-optimistic."},
            {"label": "P/B", "value": pb, "fmt": "x",
             "hint": "Price vs net asset value. Best for banks/insurers/REITs."},
            {"label": "P/S", "value": ps, "fmt": "x",
             "hint": "Price vs revenue. Used when earnings are negative/volatile."},
            {"label": "FCF yield", "value": fcf_yield, "fmt": "%",
             "hint": "Free cash flow ÷ market cap. Harder to manipulate than earnings."},
            {"label": "ROE", "value": roe, "fmt": "%",
             "hint": "Return on equity — moat / capital-allocation proxy."},
            {"label": "Gross margin", "value": gross_margin, "fmt": "%",
             "hint": "Pricing power proxy."},
            {"label": "Operating margin", "value": op_margin, "fmt": "%", "hint": ""},
            {"label": "Profit margin", "value": profit_margin, "fmt": "%", "hint": ""},
            {"label": "Debt / Equity", "value": debt_to_equity, "fmt": "raw",
             "hint": "Leverage. >100 (=1x) is meaningful; >200 (=2x) is heavy."},
            {"label": "Current ratio", "value": current_ratio, "fmt": "x",
             "hint": "Short-term liquidity. >1 covers current liabilities."},
            {"label": "Earnings growth", "value": earnings_growth, "fmt": "%", "hint": "YoY"},
            {"label": "Revenue growth", "value": revenue_growth, "fmt": "%", "hint": "YoY"},
        ],
        "flags": flags,
    }


# --------------------------------------------------------------------------- #
# Margin of safety vs analyst fair value
# --------------------------------------------------------------------------- #
def build_margin_of_safety(info: dict, price: float):
    target_mean = _num(info.get("targetMeanPrice"))
    target_low = _num(info.get("targetLowPrice"))
    target_high = _num(info.get("targetHighPrice"))
    recommendation = info.get("recommendationKey")
    n_analysts = _num(info.get("numberOfAnalystOpinions"))

    mos = None
    if target_mean and price:
        mos = round((target_mean - price) / target_mean * 100, 1)

    flags = []
    if mos is not None:
        if mos >= 20:
            flags.append(flag("good", f"Trading {mos:.0f}% below mean analyst target — wide margin of safety (analyst-based)."))
        elif mos >= 0:
            flags.append(flag("info", f"Trading {mos:.0f}% below mean analyst target — thin margin."))
        else:
            flags.append(flag("warn", f"Trading {abs(mos):.0f}% ABOVE mean analyst target — no margin of safety."))
    flags.append(flag("info", "Analyst targets are opinions, not truth. Valuation is judgment, not arithmetic — your own fair-value estimate is what counts."))

    return {
        "target_low": target_low,
        "target_mean": target_mean,
        "target_high": target_high,
        "recommendation": recommendation,
        "n_analysts": int(n_analysts) if n_analysts else None,
        "margin_of_safety_pct": mos,
        "flags": flags,
    }


# --------------------------------------------------------------------------- #
# Main report
# --------------------------------------------------------------------------- #
def build_report(ticker: str):
    ticker = ticker.strip().upper()
    t = yf.Ticker(ticker)

    try:
        info = t.info or {}
    except Exception:
        info = {}

    if not info or not (info.get("regularMarketPrice") or info.get("currentPrice")):
        # try fast_info as a fallback
        try:
            fi = t.fast_info
            if not fi or not fi.get("lastPrice"):
                return {"error": f"No data found for '{ticker}'. Check the symbol."}
        except Exception:
            return {"error": f"No data found for '{ticker}'. Check the symbol."}

    hist = t.history(period="1y", auto_adjust=False)
    tech = build_technicals(hist)

    price = (
        _num(info.get("currentPrice"))
        or _num(info.get("regularMarketPrice"))
        or (tech["price"] if tech else None)
    )

    prev_close = _num(info.get("regularMarketPreviousClose")) or _num(info.get("previousClose"))
    change = None
    change_pct = None
    if price and prev_close:
        change = round(price - prev_close, 2)
        change_pct = round((price - prev_close) / prev_close * 100, 2)

    header = {
        "ticker": ticker,
        "name": info.get("longName") or info.get("shortName") or ticker,
        "exchange": info.get("fullExchangeName") or info.get("exchange"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "currency": info.get("currency", "USD"),
        "price": price,
        "change": change,
        "change_pct": change_pct,
        "market_cap": _num(info.get("marketCap")),
        "fifty_two_high": _num(info.get("fiftyTwoWeekHigh")),
        "fifty_two_low": _num(info.get("fiftyTwoWeekLow")),
        "beta": _num(info.get("beta")),
        "dividend_yield": _pct(info.get("dividendYield")) if info.get("dividendYield") and info.get("dividendYield") < 1 else _num(info.get("dividendYield")),
        "summary": info.get("longBusinessSummary"),
        "as_of": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    return {
        "header": header,
        "fundamentals": build_fundamentals(info),
        "technicals": tech,
        "margin_of_safety": build_margin_of_safety(info, price) if price else None,
    }


# --------------------------------------------------------------------------- #
# Routes
# --------------------------------------------------------------------------- #
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/stock/<ticker>")
def api_stock(ticker):
    try:
        return jsonify(build_report(ticker))
    except Exception as e:  # noqa: BLE001
        return jsonify({"error": f"{type(e).__name__}: {e}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5057)
