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
