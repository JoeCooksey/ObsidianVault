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
