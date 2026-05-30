# 🧭 Life Dashboard

Local web app that tracks your stock portfolio from Markdown notes in the vault,
shows live totals / gain-loss / allocation, and writes a snapshot note back into
Obsidian. Built as the shell for future Health and Labs modules.

## Add your accounts

Create one note per account in `Finance/Accounts/`:

```markdown
---
type: investment-account
account: Roth IRA
broker: Fidelity
---

| ticker | shares | cost_basis |
|--------|--------|------------|
| AAPL   | 40     | 150.20     |
| VTI    | 22     |            |
```

`cost_basis` is per-share and optional (blank = no gain/loss shown for that row).

## Run it

Double-click **`run.bat`**, or:

```powershell
cd apps\life-dashboard
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5058>. A `Finance/Portfolio Dashboard.md` snapshot is
rewritten in the vault on each successful refresh.

## Tests

```powershell
cd apps\life-dashboard
.\.venv\Scripts\Activate.ps1
python -m pytest -v
```

## Caveats

Prices come from **yfinance** (Yahoo, ~15-min delayed, scraped) — directional, not
audited. Cached ~10 min to avoid rate-limits.

## Roadmap

This is the shell for the broader life dashboard. Planned modules (see
`docs/superpowers/specs/`): **Health** (Eight Sleep + Apple Watch via an
iPhone→export pipeline) and **Labs** (blood-test upload, storage, trends).
