# Life Dashboard — Portfolio Module (v1)

**Date:** 2026-05-30
**Owner:** Joe
**Status:** Approved design, ready for implementation plan

## Context

Joe wants a personal "life dashboard" that eventually tracks health (Apple Watch,
Eight Sleep), a stock portfolio, and uploaded health records (blood tests), with a
polished UI and Obsidian integration. That scope is four independent subsystems of
very different difficulty, so it is being built one slice at a time.

**This spec covers the first slice only: the Portfolio module**, built as the shell
that the other modules will later plug into.

Decisions already made during brainstorming:

- **Build order:** Stocks first.
- **Data source:** Portfolio data lives as Markdown notes in the vault (Obsidian-native,
  plain text, version-controlled by the existing git backup).
- **Features:** total net worth + per-account breakdown; gain/loss vs cost basis;
  today's change + allocation breakdown; click-through to a single-ticker deep-dive.
- **Obsidian link:** both a live web app **and** an auto-written snapshot note in the vault.
- **Look:** polished dark theme, builder's discretion (no mockup comparison needed).

There is an existing `apps/stock-dashboard/` Flask app that produces a single-ticker
report (fundamentals / technicals / margin-of-safety) using `yfinance`. Its analysis
logic is reused.

## Goals

- A running local web app showing Joe's whole portfolio across multiple accounts.
- Holdings authored and edited as Markdown notes in the vault — no separate DB.
- Live(ish) prices, totals, gain/loss, today's move, and allocation breakdowns.
- Click any holding to open the existing single-ticker deep-dive.
- A snapshot Markdown note written back into the vault on each successful refresh.
- A shell with navigation stubs for future Health / Labs modules.

## Non-Goals (v1)

- Health metrics, Eight Sleep, Apple Watch, blood-test ingestion (future slices).
- Real-time streaming quotes, intraday tick data, or brokerage API auth.
- Realized gains, tax lots, dividends reinvestment, multi-currency conversion.
- Authentication / multi-user. This is a single-user local app.
- Editing holdings *from* the web app — editing happens in Obsidian. The app reads.

## Architecture

New app at `apps/life-dashboard/`. Built as the shell for the whole life dashboard;
Portfolio is the first and only active module in v1. Health / Labs appear in the nav
as disabled "coming soon" stubs so the structure is ready.

```
apps/life-dashboard/
├── app.py                  # Flask app: routes + shell wiring
├── config.py               # vault paths (accounts dir, snapshot note, cache dir)
├── portfolio/
│   ├── __init__.py
│   ├── loader.py           # parse account .md notes -> list[Holding] / Account
│   ├── compute.py          # totals, gain/loss, allocation, day-change
│   └── snapshot.py         # render + write "Portfolio Dashboard.md" to the vault
├── providers/
│   ├── __init__.py
│   ├── prices.py           # batch live price/prev-close/sector via yfinance + disk cache
│   └── stocks.py           # ported single-ticker deep-dive report (from stock-dashboard)
├── templates/
│   ├── base.html           # shell: sidebar nav (Portfolio active; Health/Labs stubbed)
│   ├── portfolio.html      # main portfolio view
│   └── ticker.html         # single-ticker deep-dive
├── static/
│   ├── css/dashboard.css
│   └── js/portfolio.js
├── tests/
│   ├── fixtures/           # sample account .md notes
│   ├── test_loader.py
│   ├── test_compute.py
│   ├── test_snapshot.py
│   └── test_routes.py
├── requirements.txt
├── run.bat
└── README.md
```

The existing `apps/stock-dashboard/` is left untouched in v1. Once the new app is
confirmed to fully replace it, it can be deleted (separate follow-up, with Joe's OK).

## Data Model

### Account notes (input) — `Finance/Accounts/*.md`

One note per account. Frontmatter identifies the account; a single Markdown table
lists holdings.

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

Parsing rules:

- `account` (frontmatter) — display name. Falls back to the filename if absent.
- `broker` (frontmatter) — optional label.
- The first Markdown table in the body is the holdings table.
- Required columns: `ticker`, `shares`. Optional: `cost_basis`.
- Column matching is case-insensitive and tolerant of surrounding whitespace.
- `shares` and `cost_basis` parse as floats; blank `cost_basis` -> `None`.
- A row with a blank/missing `ticker` or unparseable `shares` is skipped with a warning.
- Only notes with `type: investment-account` in frontmatter are treated as accounts.

### Internal types

- `Holding`: `ticker`, `shares`, `cost_basis | None`, `account` (name).
- `Account`: `name`, `broker | None`, `holdings: list[Holding]`.
- `PricedHolding`: a `Holding` plus `price`, `prev_close`, `sector`, `name`,
  `value`, `cost`, `gain`, `gain_pct`, `day_change`, `error | None`, `spark: list[float]`.

### Snapshot note (output) — `Finance/Portfolio Dashboard.md`

Auto-generated, **overwritten on each successful refresh**. Obsidian-flavored:
frontmatter with an `updated` timestamp, a totals callout, per-account sections with
holdings tables (value + gain/loss), and a note that it is machine-generated. Never
written on a failed/stale refresh.

## Data Flow

1. `loader` scans `Finance/Accounts/*.md`, parses accounts + holdings.
2. `prices.get_quotes(tickers)` batch-fetches price, previous close, sector, and long
   name for each unique ticker via `yfinance`, with an on-disk cache (~10 min TTL) to
   avoid Yahoo rate-limiting. On a fetch failure it falls back to the last cached value.
3. `compute` joins holdings with quotes and produces:
   - per holding: value, cost (if cost_basis), gain $/%, today's $ change, sparkline;
   - per account: summed value, cost, gain, day change;
   - portfolio: total value, total cost, total gain $/%, total day change $/%;
   - allocation breakdowns: by ticker, by sector, by account (value-weighted).
4. The web app renders the live view; `snapshot.write()` rewrites the vault note.
5. Clicking a holding hits `/ticker/<symbol>` → `providers/stocks.py` deep-dive report.

## Routes

- `GET /` — portfolio view (`portfolio.html`).
- `GET /api/portfolio` — JSON: accounts, priced holdings, totals, allocations, `stale` flag.
- `GET /ticker/<symbol>` — deep-dive page (`ticker.html`).
- `GET /api/stock/<symbol>` — JSON single-ticker report (ported from existing app).

On `GET /api/portfolio`, after a successful price fetch, the snapshot note is written
as a side effect.

## UI / Look

- Dark theme, card-based, system font stack; green for gains, red for losses, muted
  grey for neutral / missing data.
- **Top bar:** total net worth (large), today's $/% change, total unrealized gain/loss $/%.
- **Allocation:** three donut charts (by stock, by sector, by account) via Chart.js (CDN).
- **Account cards:** account name + broker, account subtotal and gain/loss, then a row
  per holding: ticker, name, shares, price, value, gain/loss %, 120-day sparkline.
- **Sidebar nav:** Portfolio (active), Health (disabled "soon"), Labs (disabled "soon").
- A "stale data" banner appears when prices are served from cache after a fetch failure.
- A timestamp shows when prices were last refreshed.

## Error Handling

- **Bad / unknown ticker:** the holding's card row is flagged with an error and excluded
  from all totals and allocations. Does not crash the page.
- **Missing `cost_basis`:** the row shows current value but `—` for gain/loss; it is
  excluded from cost and gain totals (value still counts toward net worth and allocation).
- **Price-fetch / network failure:** serve the last good cached prices and show a stale
  banner; do **not** overwrite the snapshot note on a stale refresh.
- **Malformed account note:** skip the bad row/note, surface a warning in the API payload
  and a small notice in the UI; other accounts still render.
- **No account notes found:** render an empty state explaining where to create them.

## Testing

`pytest`, network mocked throughout so tests are fast and deterministic:

- `test_loader.py` — parses fixture account notes: frontmatter, holdings table, optional
  cost_basis, case-insensitive columns, skips malformed rows, ignores non-account notes.
- `test_compute.py` — totals, gain/loss (with and without cost_basis), day-change, and
  the three allocation breakdowns against a fixed mocked price set; bad-ticker exclusion.
- `test_snapshot.py` — the snapshot renderer produces expected Markdown (totals callout,
  per-account tables, timestamp) for a known input.
- `test_routes.py` — smoke test that `/`, `/api/portfolio`, and `/ticker/<symbol>` return
  200 with `prices` mocked.

## Configuration

`config.py` resolves vault-relative paths (computed from the app location, so it works
regardless of where the repo is checked out):

- `ACCOUNTS_DIR = <vault>/Finance/Accounts`
- `SNAPSHOT_NOTE = <vault>/Finance/Portfolio Dashboard.md`
- `CACHE_DIR = apps/life-dashboard/.cache`
- `PRICE_TTL_SECONDS = 600`
- Flask dev port: `5058` (distinct from the old app's `5057`).

## Open Questions / Defaults Chosen

- Accounts folder defaulted to `Finance/Accounts/` and snapshot to
  `Finance/Portfolio Dashboard.md`. Joe can override before implementation.
- Sector data comes from `yfinance` `.info` (heavier); cached aggressively. If a sector
  is unavailable it is bucketed as "Unknown" in the sector allocation.

## Future Slices (out of scope, noted for shell design)

- **Health metrics** (Eight Sleep API; Apple Watch via an iPhone→export pipeline).
- **Blood tests / health records** (upload, store, trend).
- These will become additional modules + nav entries in the same shell.
