"""Parse investment-account Markdown notes into Account/Holding objects.

An account note has YAML frontmatter with `type: investment-account` and a
single Markdown holdings table with `ticker`, `shares`, and optional `cost_basis`.
"""
from __future__ import annotations

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
