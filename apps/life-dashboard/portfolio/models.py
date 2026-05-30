"""Plain dataclasses passed between loader, prices, compute, and snapshot."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Holding:
    ticker: str
    shares: float
    cost_basis: float | None  # per-share; None when not recorded
    account: str              # owning account name


@dataclass
class Account:
    name: str
    broker: str | None
    holdings: list[Holding] = field(default_factory=list)


@dataclass
class Quote:
    price: float | None
    prev_close: float | None
    sector: str | None
    name: str | None
    spark: list[float] = field(default_factory=list)  # recent closes for sparkline
    error: str | None = None


@dataclass
class PricedHolding:
    ticker: str
    name: str | None
    account: str
    shares: float
    cost_basis: float | None
    price: float | None
    prev_close: float | None
    sector: str | None
    spark: list[float]
    error: str | None

    @property
    def value(self) -> float | None:
        if self.price is None:
            return None
        return self.shares * self.price

    @property
    def cost(self) -> float | None:
        if self.cost_basis is None:
            return None
        return self.shares * self.cost_basis

    @property
    def gain(self) -> float | None:
        if self.value is None or self.cost is None:
            return None
        return self.value - self.cost

    @property
    def gain_pct(self) -> float | None:
        if self.gain is None or not self.cost:
            return None
        return self.gain / self.cost * 100

    @property
    def day_change(self) -> float | None:
        if self.price is None or self.prev_close is None:
            return None
        return self.shares * (self.price - self.prev_close)
