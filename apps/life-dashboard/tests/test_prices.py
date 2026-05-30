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
