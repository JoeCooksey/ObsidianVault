"""Life Dashboard — Flask shell. Portfolio module active; Health/Labs stubbed."""
from __future__ import annotations

from datetime import datetime

from flask import Flask, jsonify, render_template

import config
from portfolio.compute import build_portfolio
from portfolio.loader import load_accounts
from portfolio.snapshot import write_snapshot
from providers.prices import get_quotes
from providers.stocks import build_report

app = Flask(__name__)


def _portfolio_payload() -> dict:
    accounts = load_accounts(config.ACCOUNTS_DIR)
    tickers = [h.ticker for a in accounts for h in a.holdings]
    quotes = get_quotes(tickers, cache_dir=config.CACHE_DIR, ttl=config.PRICE_TTL_SECONDS)
    payload = build_portfolio(accounts, quotes)
    payload["stale"] = bool(getattr(quotes, "stale", False))
    payload["updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload["empty"] = len(accounts) == 0
    # Only write the snapshot on a successful (non-stale) refresh.
    if not payload["stale"] and accounts:
        write_snapshot(payload, config.SNAPSHOT_NOTE, updated=payload["updated"])
    return payload


@app.route("/")
def index():
    return render_template("portfolio.html", active="portfolio")


@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(_portfolio_payload())


@app.route("/ticker/<symbol>")
def ticker(symbol):
    return render_template("ticker.html", active="portfolio", symbol=symbol.upper())


@app.route("/api/stock/<symbol>")
def api_stock(symbol):
    try:
        return jsonify(build_report(symbol))
    except Exception as e:  # noqa: BLE001
        return jsonify({"error": f"{type(e).__name__}: {e}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=config.PORT)
