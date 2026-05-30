const fmtMoney = v => v == null ? '—' : '$' + v.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
const fmtPct = v => v == null ? '—' : (v >= 0 ? '+' : '') + v.toFixed(2) + '%';
const cls = v => v == null ? '' : (v >= 0 ? 'up' : 'down');
const COLORS = ['#58a6ff','#3fb950','#d29922','#f85149','#bc8cff','#39c5cf','#ff9e64','#7ee787'];

async function init() {
  const r = await fetch('/api/portfolio');
  const d = await r.json();

  document.getElementById('updated').textContent = 'Updated ' + (d.updated || '');
  document.getElementById('stale-banner').classList.toggle('hidden', !d.stale);
  document.getElementById('empty-state').classList.toggle('hidden', !d.empty);
  if (d.empty) return;

  document.getElementById('totals').innerHTML = `
    <div class="stat"><div class="label">Total Value</div><div class="big">${fmtMoney(d.total_value)}</div></div>
    <div class="stat"><div class="label">Today</div><div class="big ${cls(d.day_change)}">${fmtMoney(d.day_change)} <small>${fmtPct(d.day_change_pct)}</small></div></div>
    <div class="stat"><div class="label">Unrealized Gain</div><div class="big ${cls(d.total_gain)}">${fmtMoney(d.total_gain)} <small>${fmtPct(d.total_gain_pct)}</small></div></div>`;

  donut('chart-ticker', d.allocation.by_ticker);
  donut('chart-sector', d.allocation.by_sector);
  donut('chart-account', d.allocation.by_account);

  document.getElementById('accounts').innerHTML = d.accounts.map(renderAccount).join('');
}

function renderAccount(a) {
  const rows = a.holdings.map(h => h.error
    ? `<tr><td>${h.ticker}</td><td colspan="5" class="down">⚠️ ${h.error}</td></tr>`
    : `<tr>
        <td><a href="/ticker/${h.ticker}">${h.ticker}</a> <span style="color:var(--muted)">${h.name ?? ''}</span></td>
        <td>${h.shares}</td><td>${fmtMoney(h.price)}</td><td>${fmtMoney(h.value)}</td>
        <td class="${cls(h.gain)}">${fmtMoney(h.gain)}</td><td class="${cls(h.gain_pct)}">${fmtPct(h.gain_pct)}</td>
      </tr>`).join('');
  return `<div class="account-card">
    <div class="head"><h2>${a.name}${a.broker ? ' · ' + a.broker : ''}</h2>
      <div>${fmtMoney(a.value)} <span class="${cls(a.gain)}">${fmtPct(a.gain_pct)}</span></div></div>
    <table class="holdings">
      <thead><tr><th>Holding</th><th>Shares</th><th>Price</th><th>Value</th><th>Gain</th><th>Gain %</th></tr></thead>
      <tbody>${rows}</tbody></table></div>`;
}

function donut(id, data) {
  new Chart(document.getElementById(id), {
    type: 'doughnut',
    data: { labels: data.map(x => x.label),
      datasets: [{ data: data.map(x => x.value), backgroundColor: COLORS, borderWidth: 0 }] },
    options: { plugins: { legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 11 } } } } }
  });
}

init();
