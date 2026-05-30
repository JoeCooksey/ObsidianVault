import app

r = app.build_report("AAPL")
print("keys:", list(r.keys()))
print("error:", r.get("error"))
h = r.get("header", {})
print("name:", h.get("name"), "| price:", h.get("price"), "| chg%:", h.get("change_pct"))
print("mktcap:", h.get("market_cap"))
f = r.get("fundamentals", {})
print("n fundamental flags:", len(f.get("flags", [])))
for m in f.get("metrics", [])[:6]:
    print("   ", m["label"], "=", m["value"])
tc = r.get("technicals")
if tc:
    print("tech: rsi", tc["rsi"], "sma50", tc["sma50"], "sma200", tc["sma200"], "cross", tc["cross"])
    print("n tech flags:", len(tc["flags"]))
m = r.get("margin_of_safety")
if m:
    print("MoS%:", m["margin_of_safety_pct"], "target_mean:", m["target_mean"], "rec:", m["recommendation"])
print("OK")
