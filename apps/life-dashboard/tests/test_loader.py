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
