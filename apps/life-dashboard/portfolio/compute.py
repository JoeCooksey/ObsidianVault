"""Join accounts with quotes and produce the portfolio summary dict the web app
and snapshot writer consume. Bad-ticker holdings are kept (flagged) but excluded
from every total and allocation."""
from __future__ import annotations

from collections import defaultdict

from portfolio.models import Account, PricedHolding, Quote


def _price_holding(h, quotes: dict[str, Quote]) -> PricedHolding:
    q = quotes.get(h.ticker, Quote(None, None, None, None, [], error="No quote."))
    return PricedHolding(
        ticker=h.ticker, name=q.name, account=h.account, shares=h.shares,
        cost_basis=h.cost_basis, price=q.price, prev_close=q.prev_close,
        sector=q.sector, spark=q.spark, error=q.error,
    )


def _holding_dict(ph: PricedHolding) -> dict:
    return {
        "ticker": ph.ticker, "name": ph.name, "shares": ph.shares,
        "cost_basis": ph.cost_basis, "price": ph.price,
        "value": ph.value, "cost": ph.cost, "gain": ph.gain,
        "gain_pct": ph.gain_pct, "day_change": ph.day_change,
        "sector": ph.sector, "spark": ph.spark, "error": ph.error,
    }


def build_portfolio(accounts: list[Account], quotes: dict[str, Quote]) -> dict:
    total_value = 0.0
    total_cost = 0.0
    total_gain = 0.0
    day_change = 0.0
    by_ticker: dict[str, float] = defaultdict(float)
    by_sector: dict[str, float] = defaultdict(float)
    by_account: dict[str, float] = defaultdict(float)

    out_accounts = []
    for acct in accounts:
        a_value = a_cost = a_gain = a_day = 0.0
        holdings = []
        for h in acct.holdings:
            ph = _price_holding(h, quotes)
            holdings.append(_holding_dict(ph))
            if ph.error or ph.value is None:
                continue
            total_value += ph.value
            a_value += ph.value
            by_ticker[ph.ticker] += ph.value
            by_sector[ph.sector or "Unknown"] += ph.value
            by_account[acct.name] += ph.value
            if ph.cost is not None:
                total_cost += ph.cost
                a_cost += ph.cost
            if ph.gain is not None:
                total_gain += ph.gain
                a_gain += ph.gain
            if ph.day_change is not None:
                day_change += ph.day_change
                a_day += ph.day_change
        out_accounts.append({
            "name": acct.name, "broker": acct.broker, "holdings": holdings,
            "value": a_value, "cost": a_cost, "gain": a_gain, "day_change": a_day,
            "gain_pct": (a_gain / a_cost * 100) if a_cost else None,
        })

    def alloc(mapping):
        return [{"label": k, "value": round(v, 2)}
                for k, v in sorted(mapping.items(), key=lambda kv: -kv[1])]

    prev_total = total_value - day_change
    return {
        "accounts": out_accounts,
        "total_value": round(total_value, 2),
        "total_cost": round(total_cost, 2),
        "total_gain": round(total_gain, 2),
        "total_gain_pct": round(total_gain / total_cost * 100, 2) if total_cost else None,
        "day_change": round(day_change, 2),
        "day_change_pct": round(day_change / prev_total * 100, 2) if prev_total else None,
        "allocation": {
            "by_ticker": alloc(by_ticker),
            "by_sector": alloc(by_sector),
            "by_account": alloc(by_account),
        },
    }
