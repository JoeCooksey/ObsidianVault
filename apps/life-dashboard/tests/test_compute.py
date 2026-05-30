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
