# Life Dashboard — Portfolio Module Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local web app that reads a stock portfolio authored as Markdown notes in the vault, shows live totals / gain-loss / allocation with click-through to a single-ticker deep-dive, and writes a snapshot note back into Obsidian.

**Architecture:** A new Flask app at `apps/life-dashboard/` acting as the shell for the broader life dashboard (Portfolio active; Health/Labs stubbed). Pure-Python modules (`portfolio/loader`, `providers/prices`, `portfolio/compute`, `portfolio/snapshot`) are independently unit-tested with prices mocked; Flask only wires them to routes and templates. The single-ticker deep-dive logic is ported from the existing `apps/stock-dashboard/app.py`.

**Tech Stack:** Python 3.10, Flask, yfinance, pandas, numpy, pytest. Chart.js via CDN on the frontend.

---

## File Structure

```
apps/life-dashboard/
├── app.py                  # Flask routes + shell wiring
├── config.py               # vault-relative paths + constants
├── portfolio/
│   ├── __init__.py
│   ├── models.py           # Holding, Account, PricedHolding dataclasses
│   ├── loader.py           # parse account .md notes
│   ├── compute.py          # totals, gain/loss, allocation, day-change
│   └── snapshot.py         # render + write Portfolio Dashboard.md
├── providers/
│   ├── __init__.py
│   ├── prices.py           # batch quotes via yfinance + disk cache
│   └── stocks.py           # ported single-ticker deep-dive report
├── templates/
│   ├── base.html           # shell + sidebar nav
│   ├── portfolio.html      # portfolio view
│   └── ticker.html         # deep-dive view
├── static/
│   ├── css/dashboard.css
│   └── js/portfolio.js
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── fixtures/Roth-IRA.md
│   ├── fixtures/Taxable.md
│   ├── fixtures/not-an-account.md
│   ├── test_loader.py
│   ├── test_compute.py
│   ├── test_snapshot.py
│   └── test_routes.py
├── requirements.txt
├── run.bat
└── README.md
```

Vault data paths (created at runtime / by the user, not part of the app folder):
- `Finance/Accounts/*.md` — account notes (input)
- `Finance/Portfolio Dashboard.md` — snapshot (output)

---

## Task 1: Scaffold app skeleton, config, deps

**Files:**
- Create: `apps/life-dashboard/requirements.txt`
- Create: `apps/life-dashboard/config.py`
- Create: `apps/life-dashboard/portfolio/__init__.py` (empty)
- Create: `apps/life-dashboard/providers/__init__.py` (empty)
- Create: `apps/life-dashboard/tests/__init__.py` (empty)
- Create: `apps/life-dashboard/.gitignore`

- [ ] **Step 1: Create requirements.txt**

```
flask>=3.0
yfinance>=0.2.40
pandas>=2.0
numpy>=1.26
pytest>=8.0
```

- [ ] **Step 2: Create .gitignore**

```
.venv/
.cache/
__pycache__/
*.pyc
```

- [ ] **Step 3: Create config.py**

```python
"""Paths and constants for the life dashboard. Paths resolve relative to this
file so the app works regardless of where the repo is checked out."""
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent          # apps/life-dashboard
VAULT_ROOT = APP_DIR.parent.parent                 # Joe_Vault

ACCOUNTS_DIR = VAULT_ROOT / "Finance" / "Accounts"
SNAPSHOT_NOTE = VAULT_ROOT / "Finance" / "Portfolio Dashboard.md"
CACHE_DIR = APP_DIR / ".cache"

PRICE_TTL_SECONDS = 600
PORT = 5058
```

- [ ] **Step 4: Create the three empty `__init__.py` files**

Each is an empty file. Create `portfolio/__init__.py`, `providers/__init__.py`, `tests/__init__.py`.

- [ ] **Step 5: Verify config imports**

Run: `cd apps/life-dashboard && python -c "import config; print(config.PORT, config.ACCOUNTS_DIR)"`
Expected: `5058 ...\Finance\Accounts`

- [ ] **Step 6: Commit**

```bash
git add apps/life-dashboard/requirements.txt apps/life-dashboard/.gitignore apps/life-dashboard/config.py apps/life-dashboard/portfolio/__init__.py apps/life-dashboard/providers/__init__.py apps/life-dashboard/tests/__init__.py
git commit -m "chore: scaffold life-dashboard app skeleton + config"
```

---

## Task 2: Data models

**Files:**
- Create: `apps/life-dashboard/portfolio/models.py`

- [ ] **Step 1: Create models.py**

```python
"""Plain dataclasses passed between loader, prices, compute, and snapshot."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Holding:
    ticker: str
    shares: float
    cost_basis: float | None  # per-share; None when not recorded
    account: str              # owning account name


@dataclass
class Account:
    name: str
    broker: str | None
    holdings: list[Holding] = field(default_factory=list)


@dataclass
class Quote:
    price: float | None
    prev_close: float | None
    sector: str | None
    name: str | None
    spark: list[float] = field(default_factory=list)  # recent closes for sparkline
    error: str | None = None


@dataclass
class PricedHolding:
    ticker: str
    name: str | None
    account: str
    shares: float
    cost_basis: float | None
    price: float | None
    prev_close: float | None
    sector: str | None
    spark: list[float]
    error: str | None

    @property
    def value(self) -> float | None:
        if self.price is None:
            return None
        return self.shares * self.price

    @property
    def cost(self) -> float | None:
        if self.cost_basis is None:
            return None
        return self.shares * self.cost_basis

    @property
    def gain(self) -> float | None:
        if self.value is None or self.cost is None:
            return None
        return self.value - self.cost

    @property
    def gain_pct(self) -> float | None:
        if self.gain is None or not self.cost:
            return None
        return self.gain / self.cost * 100

    @property
    def day_change(self) -> float | None:
        if self.price is None or self.prev_close is None:
            return None
        return self.shares * (self.price - self.prev_close)
```

- [ ] **Step 2: Verify it imports**

Run: `cd apps/life-dashboard && python -c "from portfolio.models import Holding, Account, Quote, PricedHolding; print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add apps/life-dashboard/portfolio/models.py
git commit -m "feat: portfolio data models"
```

---

## Task 3: Account-note loader

**Files:**
- Create: `apps/life-dashboard/portfolio/loader.py`
- Create: `apps/life-dashboard/tests/fixtures/Roth-IRA.md`
- Create: `apps/life-dashboard/tests/fixtures/Taxable.md`
- Create: `apps/life-dashboard/tests/fixtures/not-an-account.md`
- Create: `apps/life-dashboard/tests/test_loader.py`

- [ ] **Step 1: Create the three fixture notes**

`tests/fixtures/Roth-IRA.md`:

```markdown
---
type: investment-account
account: Roth IRA
broker: Fidelity
---

| ticker | shares | cost_basis |
|--------|--------|------------|
| AAPL   | 40     | 150.20     |
| MSFT   | 15     | 310.00     |
| VTI    | 22     |            |
```

`tests/fixtures/Taxable.md` (tests case-insensitive headers, extra whitespace, a malformed row):

```markdown
---
type: investment-account
account: Taxable Brokerage
---

| Ticker | Shares | Cost_Basis |
|--------|--------|------------|
|  NVDA  |  10    |  90.0      |
|        |  5     |  1.0       |
| GOOG   | 7      |            |
```

`tests/fixtures/not-an-account.md` (must be ignored — no investment-account type):

```markdown
---
type: note
---

| ticker | shares |
|--------|--------|
| SPY    | 100    |
```

- [ ] **Step 2: Write the failing test**

`tests/test_loader.py`:

```python
from pathlib import Path

from portfolio.loader import load_accounts, parse_account_file

FIXTURES = Path(__file__).parent / "fixtures"


def test_parses_frontmatter_and_holdings():
    acct = parse_account_file(FIXTURES / "Roth-IRA.md")
    assert acct.name == "Roth IRA"
    assert acct.broker == "Fidelity"
    assert len(acct.holdings) == 3
    aapl = acct.holdings[0]
    assert aapl.ticker == "AAPL"
    assert aapl.shares == 40
    assert aapl.cost_basis == 150.20
    assert aapl.account == "Roth IRA"


def test_optional_cost_basis_is_none_when_blank():
    acct = parse_account_file(FIXTURES / "Roth-IRA.md")
    vti = [h for h in acct.holdings if h.ticker == "VTI"][0]
    assert vti.cost_basis is None


def test_case_insensitive_headers_and_skips_malformed_rows():
    acct = parse_account_file(FIXTURES / "Taxable.md")
    tickers = [h.ticker for h in acct.holdings]
    assert tickers == ["NVDA", "GOOG"]  # blank-ticker row dropped
    assert acct.broker is None


def test_load_accounts_ignores_non_account_notes(tmp_path):
    # copy the three fixtures into a temp dir
    import shutil
    for name in ("Roth-IRA.md", "Taxable.md", "not-an-account.md"):
        shutil.copy(FIXTURES / name, tmp_path / name)
    accounts = load_accounts(tmp_path)
    names = sorted(a.name for a in accounts)
    assert names == ["Roth IRA", "Taxable Brokerage"]
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `cd apps/life-dashboard && python -m pytest tests/test_loader.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'portfolio.loader'`

- [ ] **Step 4: Implement loader.py**

```python
"""Parse investment-account Markdown notes into Account/Holding objects.

An account note has YAML frontmatter with `type: investment-account` and a
single Markdown holdings table with `ticker`, `shares`, and optional `cost_basis`.
"""
from __future__ import annotations

import re
from pathlib import Path

from portfolio.models import Account, Holding


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Minimal YAML: flat `key: value` pairs."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip("\n")
    body = text[end + 4:]
    fm: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm, body


def _parse_first_table(body: str) -> list[dict[str, str]]:
    """Parse the first GitHub-style Markdown table into a list of row dicts."""
    rows = [ln for ln in body.splitlines() if ln.strip().startswith("|")]
    if len(rows) < 2:
        return []

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    headers = [h.lower() for h in cells(rows[0])]
    # rows[1] is the separator (---). Data starts at rows[2].
    out: list[dict[str, str]] = []
    for line in rows[2:]:
        values = cells(line)
        if len(values) != len(headers):
            continue
        out.append(dict(zip(headers, values)))
    return out


def _to_float(raw: str) -> float | None:
    raw = (raw or "").strip().replace(",", "")
    if not raw:
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def parse_account_file(path: Path) -> Account | None:
    text = Path(path).read_text(encoding="utf-8")
    fm, body = _parse_frontmatter(text)
    if fm.get("type") != "investment-account":
        return None

    name = fm.get("account") or Path(path).stem
    broker = fm.get("broker") or None

    holdings: list[Holding] = []
    for row in _parse_first_table(body):
        ticker = (row.get("ticker") or "").strip().upper()
        shares = _to_float(row.get("shares", ""))
        if not ticker or shares is None:
            continue
        holdings.append(
            Holding(
                ticker=ticker,
                shares=shares,
                cost_basis=_to_float(row.get("cost_basis", "")),
                account=name,
            )
        )
    return Account(name=name, broker=broker, holdings=holdings)


def load_accounts(accounts_dir: Path) -> list[Account]:
    accounts_dir = Path(accounts_dir)
    if not accounts_dir.exists():
        return []
    accounts: list[Account] = []
    for path in sorted(accounts_dir.glob("*.md")):
        acct = parse_account_file(path)
        if acct is not None:
            accounts.append(acct)
    return accounts
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `cd apps/life-dashboard && python -m pytest tests/test_loader.py -v`
Expected: 4 passed

- [ ] **Step 6: Commit**

```bash
git add apps/life-dashboard/portfolio/loader.py apps/life-dashboard/tests/test_loader.py apps/life-dashboard/tests/fixtures
git commit -m "feat: account-note loader with tests"
```

---

## Task 4: Prices provider (batch quotes + disk cache)

**Files:**
- Create: `apps/life-dashboard/providers/prices.py`
- Create: `apps/life-dashboard/tests/conftest.py`
- Create: `apps/life-dashboard/tests/test_prices.py`

The provider exposes `get_quotes(tickers, *, cache_dir, ttl, fetcher=None) -> dict[str, Quote]`.
The `fetcher` seam lets tests inject fake network data; production passes the default
yfinance fetcher.

- [ ] **Step 1: Create conftest.py (shared fake fetcher)**

`tests/conftest.py`:

```python
import pytest

from portfolio.models import Quote


@pytest.fixture
def fake_quotes():
    """Deterministic quotes keyed by ticker for compute/snapshot/route tests."""
    return {
        "AAPL": Quote(price=200.0, prev_close=190.0, sector="Technology",
                      name="Apple Inc.", spark=[180.0, 190.0, 200.0]),
        "MSFT": Quote(price=400.0, prev_close=400.0, sector="Technology",
                      name="Microsoft Corp.", spark=[390.0, 395.0, 400.0]),
        "VTI": Quote(price=250.0, prev_close=248.0, sector="ETF",
                     name="Vanguard Total Stock Market", spark=[245.0, 247.0, 250.0]),
        "NVDA": Quote(price=120.0, prev_close=110.0, sector="Technology",
                      name="NVIDIA Corp.", spark=[100.0, 110.0, 120.0]),
        "GOOG": Quote(price=150.0, prev_close=151.0, sector="Communication Services",
                      name="Alphabet Inc.", spark=[148.0, 149.0, 150.0]),
        "BADX": Quote(price=None, prev_close=None, sector=None, name=None,
                      spark=[], error="No data found for 'BADX'."),
    }
```

- [ ] **Step 2: Write the failing test**

`tests/test_prices.py`:

```python
from portfolio.models import Quote
from providers import prices


def test_get_quotes_uses_fetcher_and_caches(tmp_path):
    calls = []

    def fetcher(tickers):
        calls.append(tuple(sorted(tickers)))
        return {t: Quote(price=10.0, prev_close=9.0, sector="X", name=t) for t in tickers}

    q1 = prices.get_quotes(["AAPL", "MSFT"], cache_dir=tmp_path, ttl=600, fetcher=fetcher)
    assert q1["AAPL"].price == 10.0
    # Second call within TTL must hit the cache, not the fetcher again.
    q2 = prices.get_quotes(["AAPL", "MSFT"], cache_dir=tmp_path, ttl=600, fetcher=fetcher)
    assert q2["MSFT"].price == 10.0
    assert len(calls) == 1  # fetcher called only once


def test_get_quotes_falls_back_to_cache_on_fetch_failure(tmp_path):
    def good(tickers):
        return {t: Quote(price=5.0, prev_close=5.0, sector="X", name=t) for t in tickers}

    prices.get_quotes(["AAPL"], cache_dir=tmp_path, ttl=0, fetcher=good)

    def boom(tickers):
        raise RuntimeError("network down")

    # ttl=0 forces a refetch attempt; failure should fall back to cached value.
    out = prices.get_quotes(["AAPL"], cache_dir=tmp_path, ttl=0, fetcher=boom)
    assert out["AAPL"].price == 5.0
    assert out.stale is True
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `cd apps/life-dashboard && python -m pytest tests/test_prices.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'providers.prices'`

- [ ] **Step 4: Implement prices.py**

```python
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
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `cd apps/life-dashboard && python -m pytest tests/test_prices.py -v`
Expected: 2 passed

- [ ] **Step 6: Commit**

```bash
git add apps/life-dashboard/providers/prices.py apps/life-dashboard/tests/conftest.py apps/life-dashboard/tests/test_prices.py
git commit -m "feat: batch price provider with disk cache + stale fallback"
```

---

## Task 5: Compute (totals, gain/loss, allocation, day-change)

**Files:**
- Create: `apps/life-dashboard/portfolio/compute.py`
- Create: `apps/life-dashboard/tests/test_compute.py`

- [ ] **Step 1: Write the failing test**

`tests/test_compute.py`:

```python
from portfolio.compute import build_portfolio
from portfolio.models import Account, Holding


def _accounts():
    return [
        Account(name="Roth IRA", broker="Fidelity", holdings=[
            Holding("AAPL", 40, 150.20, "Roth IRA"),
            Holding("VTI", 22, None, "Roth IRA"),     # no cost basis
        ]),
        Account(name="Taxable", broker=None, holdings=[
            Holding("NVDA", 10, 90.0, "Taxable"),
            Holding("BADX", 5, 1.0, "Taxable"),         # bad ticker -> excluded
        ]),
    ]


def test_totals_and_gain(fake_quotes):
    p = build_portfolio(_accounts(), fake_quotes)
    # values: AAPL 40*200=8000, VTI 22*250=5500, NVDA 10*120=1200 ; BADX excluded
    assert p["total_value"] == 8000 + 5500 + 1200
    # cost only where cost_basis present: AAPL 40*150.20=6008, NVDA 10*90=900
    assert round(p["total_cost"], 2) == 6908.0
    assert round(p["total_gain"], 2) == round((8000 - 6008) + (1200 - 900), 2)


def test_day_change(fake_quotes):
    p = build_portfolio(_accounts(), fake_quotes)
    # AAPL 40*(200-190)=400, VTI 22*(250-248)=44, NVDA 10*(120-110)=100
    assert round(p["day_change"], 2) == 544.0


def test_allocation_by_sector_excludes_bad_ticker(fake_quotes):
    p = build_portfolio(_accounts(), fake_quotes)
    by_sector = {a["label"]: a["value"] for a in p["allocation"]["by_sector"]}
    assert by_sector["Technology"] == 8000 + 1200   # AAPL + NVDA
    assert by_sector["ETF"] == 5500                  # VTI
    assert "BADX" not in [h["ticker"] for acc in p["accounts"] for h in acc["holdings"] if h["error"] is None]


def test_bad_ticker_flagged_but_present(fake_quotes):
    p = build_portfolio(_accounts(), fake_quotes)
    badx = [h for acc in p["accounts"] for h in acc["holdings"] if h["ticker"] == "BADX"][0]
    assert badx["error"] is not None
    assert badx["value"] is None
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd apps/life-dashboard && python -m pytest tests/test_compute.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'portfolio.compute'`

- [ ] **Step 3: Implement compute.py**

```python
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
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `cd apps/life-dashboard && python -m pytest tests/test_compute.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add apps/life-dashboard/portfolio/compute.py apps/life-dashboard/tests/test_compute.py
git commit -m "feat: portfolio compute — totals, gain/loss, allocation, day-change"
```

---

## Task 6: Snapshot note writer

**Files:**
- Create: `apps/life-dashboard/portfolio/snapshot.py`
- Create: `apps/life-dashboard/tests/test_snapshot.py`

- [ ] **Step 1: Write the failing test**

`tests/test_snapshot.py`:

```python
from portfolio.compute import build_portfolio
from portfolio.models import Account, Holding
from portfolio.snapshot import render_snapshot, write_snapshot


def _portfolio(fake_quotes):
    accounts = [Account("Roth IRA", "Fidelity", [
        Holding("AAPL", 40, 150.20, "Roth IRA"),
        Holding("VTI", 22, None, "Roth IRA"),
    ])]
    return build_portfolio(accounts, fake_quotes)


def test_render_contains_totals_and_tables(fake_quotes):
    md = render_snapshot(_portfolio(fake_quotes), updated="2026-05-30 14:00")
    assert "type: portfolio-snapshot" in md
    assert "Roth IRA" in md
    assert "AAPL" in md
    assert "| AAPL |" in md          # holdings table row
    assert "Total value" in md
    assert "2026-05-30 14:00" in md
    assert "machine-generated" in md.lower()


def test_write_snapshot_creates_file(tmp_path, fake_quotes):
    out = tmp_path / "sub" / "Portfolio Dashboard.md"
    write_snapshot(_portfolio(fake_quotes), out, updated="2026-05-30 14:00")
    assert out.exists()
    assert "AAPL" in out.read_text(encoding="utf-8")
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd apps/life-dashboard && python -m pytest tests/test_snapshot.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'portfolio.snapshot'`

- [ ] **Step 3: Implement snapshot.py**

```python
"""Render the portfolio summary as an Obsidian-flavored Markdown note and write
it to the vault. Only ever called on a successful (non-stale) refresh."""
from __future__ import annotations

from pathlib import Path


def _money(v) -> str:
    return "—" if v is None else f"${v:,.2f}"


def _pct(v) -> str:
    return "—" if v is None else f"{v:+.2f}%"


def render_snapshot(p: dict, *, updated: str) -> str:
    lines: list[str] = []
    lines.append("---")
    lines.append("type: portfolio-snapshot")
    lines.append(f"updated: {updated}")
    lines.append("tags: [finance, portfolio, dashboard]")
    lines.append("---")
    lines.append("")
    lines.append("# Portfolio Dashboard")
    lines.append("")
    lines.append("> [!info] Totals")
    lines.append(f"> **Total value:** {_money(p['total_value'])}  ")
    lines.append(f"> **Today:** {_money(p['day_change'])} ({_pct(p.get('day_change_pct'))})  ")
    lines.append(f"> **Unrealized gain:** {_money(p['total_gain'])} ({_pct(p.get('total_gain_pct'))})")
    lines.append("")

    for acct in p["accounts"]:
        broker = f" · {acct['broker']}" if acct["broker"] else ""
        lines.append(f"## {acct['name']}{broker}")
        lines.append("")
        lines.append(f"Value {_money(acct['value'])} · Gain {_money(acct['gain'])} ({_pct(acct.get('gain_pct'))})")
        lines.append("")
        lines.append("| Ticker | Shares | Price | Value | Gain | Gain % |")
        lines.append("|--------|-------:|------:|------:|-----:|-------:|")
        for h in acct["holdings"]:
            if h["error"]:
                lines.append(f"| {h['ticker']} | {h['shares']:g} | ⚠️ | — | — | — |")
            else:
                lines.append(
                    f"| {h['ticker']} | {h['shares']:g} | {_money(h['price'])} | "
                    f"{_money(h['value'])} | {_money(h['gain'])} | {_pct(h['gain_pct'])} |"
                )
        lines.append("")

    lines.append("---")
    lines.append(f"*Machine-generated by life-dashboard on {updated}. Do not edit by hand.*")
    lines.append("")
    return "\n".join(lines)


def write_snapshot(p: dict, path, *, updated: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_snapshot(p, updated=updated), encoding="utf-8")
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `cd apps/life-dashboard && python -m pytest tests/test_snapshot.py -v`
Expected: 2 passed

- [ ] **Step 5: Commit**

```bash
git add apps/life-dashboard/portfolio/snapshot.py apps/life-dashboard/tests/test_snapshot.py
git commit -m "feat: portfolio snapshot note writer"
```

---

## Task 7: Port single-ticker deep-dive into providers/stocks.py

**Files:**
- Create: `apps/life-dashboard/providers/stocks.py`
- Reference (read-only): `apps/stock-dashboard/app.py:30-353`

- [ ] **Step 1: Create providers/stocks.py by porting the existing report logic**

Copy these functions verbatim from `apps/stock-dashboard/app.py` into `providers/stocks.py`:
`_num`, `_pct`, `flag`, `rsi`, `macd`, `build_technicals`, `build_fundamentals`,
`build_margin_of_safety`, and `build_report` (lines 30–353). Then make these edits:

- Add at the top of the new file (replace the original module docstring/imports block):

```python
"""Single-ticker deep-dive report (fundamentals / technicals / margin-of-safety).
Ported from apps/stock-dashboard/app.py — the Flask app and routes are dropped;
this module exposes build_report(ticker) only."""
from __future__ import annotations

import math
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf
```

- Do **not** copy the Flask bits from the original: the `from flask import ...` line,
  `app = Flask(__name__)`, any `@app.route(...)` functions, and the
  `if __name__ == "__main__":` block. Only the pure functions move over.

- [ ] **Step 2: Verify the report builds for a known ticker**

Run: `cd apps/life-dashboard && python -c "from providers.stocks import build_report; r = build_report('AAPL'); print('error' if 'error' in r else r['header']['ticker'])"`
Expected: `AAPL` (requires network; if offline, expect an `error` key instead — acceptable, the import working is the gate)

- [ ] **Step 3: Commit**

```bash
git add apps/life-dashboard/providers/stocks.py
git commit -m "feat: port single-ticker deep-dive report into providers/stocks"
```

---

## Task 8: Flask app — routes + service wiring

**Files:**
- Create: `apps/life-dashboard/app.py`
- Create: `apps/life-dashboard/tests/test_routes.py`

- [ ] **Step 1: Write the failing test**

`tests/test_routes.py`:

```python
import pytest

import app as app_module
from portfolio.models import Account, Holding


@pytest.fixture
def client(monkeypatch, tmp_path, fake_quotes):
    # Point the app at fixture accounts and a temp snapshot, and mock prices.
    accounts = [Account("Roth IRA", "Fidelity", [
        Holding("AAPL", 40, 150.20, "Roth IRA"),
        Holding("VTI", 22, None, "Roth IRA"),
    ])]
    monkeypatch.setattr(app_module, "load_accounts", lambda _dir: accounts)
    monkeypatch.setattr(app_module, "get_quotes",
                        lambda tickers, **kw: _stub_qmap(fake_quotes))
    monkeypatch.setattr(app_module.config, "SNAPSHOT_NOTE", tmp_path / "snap.md")
    app_module.app.config.update(TESTING=True)
    return app_module.app.test_client()


def _stub_qmap(fake_quotes):
    from providers.prices import QuoteMap
    qm = QuoteMap(fake_quotes)
    qm.stale = False
    return qm


def test_index_ok(client):
    assert client.get("/").status_code == 200


def test_api_portfolio_ok(client, tmp_path):
    r = client.get("/api/portfolio")
    assert r.status_code == 200
    data = r.get_json()
    assert data["total_value"] == 8000 + 5500
    assert data["stale"] is False


def test_ticker_page_ok(client, monkeypatch):
    monkeypatch.setattr(app_module, "build_report",
                        lambda t: {"header": {"ticker": t, "name": t, "price": 1,
                                              "as_of": "now"}, "fundamentals": None,
                                   "technicals": None, "margin_of_safety": None})
    assert client.get("/ticker/AAPL").status_code == 200
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd apps/life-dashboard && python -m pytest tests/test_routes.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'app'`

- [ ] **Step 3: Implement app.py**

```python
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
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `cd apps/life-dashboard && python -m pytest tests/test_routes.py -v`
Expected: 3 passed (templates must exist; if Task 9 not yet done, create empty `templates/portfolio.html` and `templates/ticker.html` placeholders first, then refine in Task 9)

- [ ] **Step 5: Run the full suite**

Run: `cd apps/life-dashboard && python -m pytest -v`
Expected: all tests pass

- [ ] **Step 6: Commit**

```bash
git add apps/life-dashboard/app.py apps/life-dashboard/tests/test_routes.py
git commit -m "feat: flask routes + portfolio service wiring with tests"
```

---

## Task 9: Templates, CSS, JS (the polished UI)

**Files:**
- Create: `apps/life-dashboard/templates/base.html`
- Create: `apps/life-dashboard/templates/portfolio.html`
- Create: `apps/life-dashboard/templates/ticker.html`
- Create: `apps/life-dashboard/static/css/dashboard.css`
- Create: `apps/life-dashboard/static/js/portfolio.js`

Reuse the existing dark palette from `apps/stock-dashboard/templates/index.html:8-12`
(`--bg #0d1117`, `--panel #161b22`, `--good #3fb950`, `--bad #f85149`, `--accent #58a6ff`).

- [ ] **Step 1: Create base.html (shell + sidebar nav)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{% block title %}Life Dashboard{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}" />
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
</head>
<body>
  <aside class="sidebar">
    <div class="brand">◆ Life</div>
    <nav>
      <a href="/" class="{{ 'active' if active == 'portfolio' else '' }}">📈 Portfolio</a>
      <span class="navstub">❤️ Health <em>soon</em></span>
      <span class="navstub">🧪 Labs <em>soon</em></span>
    </nav>
  </aside>
  <main class="content">
    {% block content %}{% endblock %}
  </main>
  {% block scripts %}{% endblock %}
</body>
</html>
```

- [ ] **Step 2: Create portfolio.html**

```html
{% extends "base.html" %}
{% block title %}Portfolio — Life Dashboard{% endblock %}
{% block content %}
<header class="page-head">
  <h1>Portfolio</h1>
  <div class="updated" id="updated"></div>
</header>

<div id="stale-banner" class="banner hidden">⚠️ Showing cached prices — live fetch failed.</div>
<div id="empty-state" class="empty hidden">
  No accounts yet. Create notes in <code>Finance/Accounts/</code> with
  <code>type: investment-account</code> frontmatter and a holdings table.
</div>

<section class="totals" id="totals"></section>

<section class="alloc-grid">
  <div class="panel"><h3>By Stock</h3><canvas id="chart-ticker"></canvas></div>
  <div class="panel"><h3>By Sector</h3><canvas id="chart-sector"></canvas></div>
  <div class="panel"><h3>By Account</h3><canvas id="chart-account"></canvas></div>
</section>

<section id="accounts"></section>

<script src="{{ url_for('static', filename='js/portfolio.js') }}"></script>
{% endblock %}
```

- [ ] **Step 3: Create ticker.html (deep-dive, reuses /api/stock)**

```html
{% extends "base.html" %}
{% block title %}{{ symbol }} — Life Dashboard{% endblock %}
{% block content %}
<header class="page-head">
  <a href="/" class="back">← Portfolio</a>
  <h1 id="dd-title">{{ symbol }}</h1>
</header>
<div id="report" data-symbol="{{ symbol }}">Loading {{ symbol }}…</div>
<script>
async function load() {
  const sym = document.getElementById('report').dataset.symbol;
  const r = await fetch(`/api/stock/${sym}`);
  const d = await r.json();
  const el = document.getElementById('report');
  if (d.error) { el.innerHTML = `<div class="banner">${d.error}</div>`; return; }
  const h = d.header;
  el.innerHTML = `
    <div class="price-head">
      <span class="px">$${h.price?.toFixed(2) ?? '—'}</span>
      <span class="sub">${h.name} · ${h.sector ?? ''}</span>
    </div>
    <div class="dd-flags">${renderFlags(d.fundamentals)}${renderFlags(d.technicals)}${renderFlags(d.margin_of_safety)}</div>
    <p class="summary">${h.summary ?? ''}</p>`;
}
function renderFlags(section) {
  if (!section || !section.flags) return '';
  return section.flags.map(f => `<div class="flag ${f.level}">${f.text}</div>`).join('');
}
load();
</script>
{% endblock %}
```

- [ ] **Step 4: Create static/css/dashboard.css**

```css
:root {
  --bg: #0d1117; --panel: #161b22; --panel2: #1c2230; --border: #2a3140;
  --text: #e6edf3; --muted: #8b949e; --accent: #58a6ff;
  --good: #3fb950; --bad: #f85149; --warn: #d29922;
}
* { box-sizing: border-box; }
body { margin: 0; display: flex; background: var(--bg); color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.sidebar { width: 210px; min-height: 100vh; background: #0a0e14;
  border-right: 1px solid var(--border); padding: 20px 14px; position: sticky; top: 0; }
.brand { font-size: 18px; font-weight: 700; margin-bottom: 24px; color: var(--accent); }
.sidebar nav { display: flex; flex-direction: column; gap: 4px; }
.sidebar nav a, .navstub { padding: 9px 12px; border-radius: 8px; color: var(--text);
  text-decoration: none; font-size: 14px; }
.sidebar nav a.active { background: var(--panel2); color: var(--accent); }
.sidebar nav a:hover { background: var(--panel); }
.navstub { color: var(--muted); cursor: default; }
.navstub em { font-size: 10px; text-transform: uppercase; opacity: .6; margin-left: 4px; }
.content { flex: 1; padding: 26px 34px 80px; max-width: 1200px; }
.page-head { display: flex; align-items: baseline; justify-content: space-between; }
.page-head h1 { margin: 0; font-size: 22px; }
.back { color: var(--muted); text-decoration: none; font-size: 13px; }
.updated { color: var(--muted); font-size: 12px; }
.banner { background: rgba(210,153,34,.12); border: 1px solid var(--warn);
  color: var(--warn); padding: 10px 14px; border-radius: 10px; margin: 14px 0; }
.empty { background: var(--panel); border: 1px solid var(--border);
  padding: 18px; border-radius: 12px; margin: 16px 0; color: var(--muted); }
.hidden { display: none; }
.totals { display: flex; gap: 18px; flex-wrap: wrap; margin: 20px 0; }
.totals .stat { background: var(--panel); border: 1px solid var(--border);
  border-radius: 14px; padding: 16px 22px; min-width: 200px; }
.totals .stat .label { color: var(--muted); font-size: 12px; }
.totals .stat .big { font-size: 30px; font-weight: 700; margin-top: 4px; }
.up { color: var(--good); } .down { color: var(--bad); }
.alloc-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin: 8px 0 24px; }
@media (max-width: 900px) { .alloc-grid { grid-template-columns: 1fr; } }
.panel { background: var(--panel); border: 1px solid var(--border);
  border-radius: 14px; padding: 16px 18px; }
.panel h3 { margin: 0 0 10px; font-size: 13px; color: var(--muted); font-weight: 600; }
.account-card { background: var(--panel); border: 1px solid var(--border);
  border-radius: 14px; padding: 16px 20px; margin-bottom: 16px; }
.account-card .head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px; }
.account-card h2 { margin: 0; font-size: 16px; }
table.holdings { width: 100%; border-collapse: collapse; font-size: 13px; }
table.holdings th { text-align: right; color: var(--muted); font-weight: 500;
  padding: 6px 8px; border-bottom: 1px solid var(--border); }
table.holdings th:first-child, table.holdings td:first-child { text-align: left; }
table.holdings td { padding: 7px 8px; border-bottom: 1px solid rgba(42,49,64,.5); }
table.holdings tr:hover { background: var(--panel2); }
table.holdings a { color: var(--accent); text-decoration: none; }
.flag { padding: 7px 10px; border-radius: 8px; margin: 5px 0; font-size: 13px;
  border-left: 3px solid var(--muted); background: var(--panel2); }
.flag.good { border-color: var(--good); } .flag.bad { border-color: var(--bad); }
.flag.warn { border-color: var(--warn); } .flag.info { border-color: var(--accent); }
.price-head .px { font-size: 34px; font-weight: 700; }
.price-head .sub { color: var(--muted); margin-left: 12px; }
.summary { color: var(--muted); max-width: 70ch; line-height: 1.6; }
```

- [ ] **Step 5: Create static/js/portfolio.js**

```javascript
const fmtMoney = v => v == null ? '—' : '$' + v.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
const fmtPct = v => v == null ? '—' : (v >= 0 ? '+' : '') + v.toFixed(2) + '%';
const cls = v => v == null ? '' : (v >= 0 ? 'up' : 'down');
const COLORS = ['#58a6ff','#3fb950','#d29922','#f85149','#bc8cff','#39c5cf','#ff9e64','#7ee787'];

async function init() {
  const r = await fetch('/api/portfolio');
  const d = await r.json();

  document.getElementById('updated').textContent = 'Updated ' + (d.updated || '');
  document.getElementById('stale-banner').classList.toggle('hidden', !d.stale);
  document.getElementById('empty-state').classList.toggle('hidden', !d.empty);
  if (d.empty) return;

  document.getElementById('totals').innerHTML = `
    <div class="stat"><div class="label">Total Value</div><div class="big">${fmtMoney(d.total_value)}</div></div>
    <div class="stat"><div class="label">Today</div><div class="big ${cls(d.day_change)}">${fmtMoney(d.day_change)} <small>${fmtPct(d.day_change_pct)}</small></div></div>
    <div class="stat"><div class="label">Unrealized Gain</div><div class="big ${cls(d.total_gain)}">${fmtMoney(d.total_gain)} <small>${fmtPct(d.total_gain_pct)}</small></div></div>`;

  donut('chart-ticker', d.allocation.by_ticker);
  donut('chart-sector', d.allocation.by_sector);
  donut('chart-account', d.allocation.by_account);

  document.getElementById('accounts').innerHTML = d.accounts.map(renderAccount).join('');
}

function renderAccount(a) {
  const rows = a.holdings.map(h => h.error
    ? `<tr><td>${h.ticker}</td><td colspan="5" class="down">⚠️ ${h.error}</td></tr>`
    : `<tr>
        <td><a href="/ticker/${h.ticker}">${h.ticker}</a> <span style="color:var(--muted)">${h.name ?? ''}</span></td>
        <td>${h.shares}</td><td>${fmtMoney(h.price)}</td><td>${fmtMoney(h.value)}</td>
        <td class="${cls(h.gain)}">${fmtMoney(h.gain)}</td><td class="${cls(h.gain_pct)}">${fmtPct(h.gain_pct)}</td>
      </tr>`).join('');
  return `<div class="account-card">
    <div class="head"><h2>${a.name}${a.broker ? ' · ' + a.broker : ''}</h2>
      <div>${fmtMoney(a.value)} <span class="${cls(a.gain)}">${fmtPct(a.gain_pct)}</span></div></div>
    <table class="holdings">
      <thead><tr><th>Holding</th><th>Shares</th><th>Price</th><th>Value</th><th>Gain</th><th>Gain %</th></tr></thead>
      <tbody>${rows}</tbody></table></div>`;
}

function donut(id, data) {
  new Chart(document.getElementById(id), {
    type: 'doughnut',
    data: { labels: data.map(x => x.label),
      datasets: [{ data: data.map(x => x.value), backgroundColor: COLORS, borderWidth: 0 }] },
    options: { plugins: { legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 11 } } } } }
  });
}

init();
```

- [ ] **Step 6: Re-run route tests (templates now real)**

Run: `cd apps/life-dashboard && python -m pytest tests/test_routes.py -v`
Expected: 3 passed

- [ ] **Step 7: Commit**

```bash
git add apps/life-dashboard/templates apps/life-dashboard/static
git commit -m "feat: portfolio UI — shell, dark theme, donuts, account cards, deep-dive"
```

---

## Task 10: Launcher, seed account, README, manual run

**Files:**
- Create: `apps/life-dashboard/run.bat`
- Create: `apps/life-dashboard/README.md`
- Create: `Finance/Accounts/Example Account.md` (seed so first run isn't empty)

- [ ] **Step 1: Create run.bat**

```bat
@echo off
REM Life Dashboard launcher
cd /d "%~dp0"
if not exist ".venv" (
  echo Creating virtual environment...
  python -m venv .venv
  call .venv\Scripts\activate.bat
  echo Installing dependencies...
  pip install -r requirements.txt
) else (
  call .venv\Scripts\activate.bat
)
echo.
echo Starting Life Dashboard at http://127.0.0.1:5058
start "" http://127.0.0.1:5058
python app.py
```

- [ ] **Step 2: Create the seed account note**

`Finance/Accounts/Example Account.md`:

```markdown
---
type: investment-account
account: Example Account
broker: Example Broker
---

Replace these with your real holdings. `cost_basis` (per-share) is optional.

| ticker | shares | cost_basis |
|--------|--------|------------|
| AAPL   | 10     | 150.00     |
| MSFT   | 5      | 300.00     |
| VTI    | 8      |            |
```

- [ ] **Step 3: Create README.md**

```markdown
# 🧭 Life Dashboard

Local web app that tracks your stock portfolio from Markdown notes in the vault,
shows live totals / gain-loss / allocation, and writes a snapshot note back into
Obsidian. Built as the shell for future Health and Labs modules.

## Add your accounts

Create one note per account in `Finance/Accounts/`:

\`\`\`markdown
---
type: investment-account
account: Roth IRA
broker: Fidelity
---

| ticker | shares | cost_basis |
|--------|--------|------------|
| AAPL   | 40     | 150.20     |
| VTI    | 22     |            |
\`\`\`

`cost_basis` is per-share and optional (blank = no gain/loss shown for that row).

## Run it

Double-click **`run.bat`**, or:

\`\`\`powershell
cd apps\life-dashboard
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
\`\`\`

Then open <http://127.0.0.1:5058>. A `Finance/Portfolio Dashboard.md` snapshot is
rewritten in the vault on each successful refresh.

## Tests

\`\`\`powershell
cd apps\life-dashboard
.\.venv\Scripts\Activate.ps1
python -m pytest -v
\`\`\`

## Caveats

Prices come from **yfinance** (Yahoo, ~15-min delayed, scraped) — directional, not
audited. Cached ~10 min to avoid rate-limits.
```

- [ ] **Step 4: Manual smoke run**

Run: `cd apps/life-dashboard && python -m venv .venv && .venv\Scripts\python.exe -m pip install -r requirements.txt && .venv\Scripts\python.exe -m pytest -v`
Expected: full suite passes.

Then run `.venv\Scripts\python.exe app.py`, open http://127.0.0.1:5058, confirm the
Example Account renders with live prices and donut charts, click a ticker to confirm
the deep-dive loads, and confirm `Finance/Portfolio Dashboard.md` was created.

- [ ] **Step 5: Commit**

```bash
git add apps/life-dashboard/run.bat apps/life-dashboard/README.md "Finance/Accounts/Example Account.md"
git commit -m "feat: launcher, seed account note, README"
```

---

## Self-Review Notes

- **Spec coverage:** accounts-as-markdown (Task 3), live prices + cache + stale fallback
  (Task 4), totals/gain-loss/day-change/allocation (Task 5), snapshot note (Task 6),
  deep-dive reuse (Task 7), routes (Task 8), polished dark UI + shell stubs (Task 9),
  launcher/README/seed (Task 10). All spec sections map to a task.
- **Error handling:** bad ticker excluded but flagged (Task 5 tests), missing cost_basis
  → `—` (Task 5/6), stale fallback + no-overwrite (Task 4/8), empty state (Task 9).
- **Type consistency:** `Quote`, `Holding`, `Account`, `PricedHolding`, `QuoteMap`,
  `build_portfolio`, `get_quotes`, `load_accounts`, `build_report`, `render_snapshot`,
  `write_snapshot` are used with consistent signatures across tasks.
- **Note on Task 8/9 ordering:** route tests in Task 8 require the two templates to
  exist; Step 4 of Task 8 calls for placeholder templates if Task 9 hasn't run, then
  Task 9 replaces them. The full UI commit lands in Task 9.
```
