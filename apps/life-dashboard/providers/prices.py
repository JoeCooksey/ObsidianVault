"""Batch quote provider with an on-disk cache and a pluggable fetcher.

`get_quotes` returns a QuoteMap (dict subclass) with a `.stale` flag set True
when any ticker had to fall back to a cached value after a fetch failure.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

from portfolio.models import Quote


class QuoteMap(dict):
    stale: bool = False


def _cache_path(cache_dir: Path) -> Path:
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir / "quotes.json"


def _load_cache(cache_dir: Path) -> dict:
    path = _cache_path(cache_dir)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def _save_cache(cache_dir: Path, data: dict) -> None:
    _cache_path(cache_dir).write_text(json.dumps(data), encoding="utf-8")


def _quote_to_dict(q: Quote) -> dict:
    return {
        "price": q.price, "prev_close": q.prev_close, "sector": q.sector,
        "name": q.name, "spark": q.spark, "error": q.error,
    }


def _quote_from_dict(d: dict) -> Quote:
    return Quote(price=d.get("price"), prev_close=d.get("prev_close"),
                 sector=d.get("sector"), name=d.get("name"),
                 spark=d.get("spark") or [], error=d.get("error"))


def _default_fetcher(tickers: list[str]) -> dict[str, Quote]:
    import yfinance as yf

    out: dict[str, Quote] = {}
    for ticker in tickers:
        try:
            t = yf.Ticker(ticker)
            info = {}
            try:
                info = t.info or {}
            except Exception:
                info = {}
            hist = t.history(period="6mo", auto_adjust=False)
            closes = [round(float(x), 2) for x in hist["Close"].dropna().tolist()] if not hist.empty else []
            price = info.get("currentPrice") or info.get("regularMarketPrice") or (closes[-1] if closes else None)
            prev = info.get("regularMarketPreviousClose") or info.get("previousClose")
            if price is None and not closes:
                out[ticker] = Quote(None, None, None, None, [], error=f"No data found for '{ticker}'.")
                continue
            out[ticker] = Quote(
                price=float(price) if price is not None else None,
                prev_close=float(prev) if prev is not None else None,
                sector=info.get("sector") or ("ETF" if info.get("quoteType") == "ETF" else None),
                name=info.get("longName") or info.get("shortName") or ticker,
                spark=closes[-120:],
            )
        except Exception as e:  # noqa: BLE001
            out[ticker] = Quote(None, None, None, None, [], error=f"{type(e).__name__}: {e}")
    return out


def get_quotes(tickers, *, cache_dir, ttl, fetcher=None) -> QuoteMap:
    fetcher = fetcher or _default_fetcher
    tickers = sorted({t.upper() for t in tickers})
    now = time.time()
    cache = _load_cache(cache_dir)

    fresh = [t for t in tickers
             if t not in cache or (now - cache[t].get("_ts", 0)) >= ttl]

    result = QuoteMap()
    if fresh:
        try:
            fetched = fetcher(fresh)
            for t, q in fetched.items():
                cache[t] = {**_quote_to_dict(q), "_ts": now}
            _save_cache(cache_dir, cache)
        except Exception:  # noqa: BLE001 — fetch failed: serve cache, mark stale
            result.stale = True

    for t in tickers:
        if t in cache:
            result[t] = _quote_from_dict(cache[t])
        else:
            result[t] = Quote(None, None, None, None, [], error="No quote available.")
            result.stale = True
    return result
