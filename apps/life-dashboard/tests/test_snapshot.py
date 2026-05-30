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
