# EE Pipeline Visualizer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `apps/ee-pipeline.html` — a single self-contained interactive study app visualizing the math/physics → EE pipeline with four canvas simulations.

**Architecture:** One HTML file, zero dependencies. Internally sectioned: CSS → HTML skeleton (SVG graph sidebar + sim panel) → JS utilities (RK4, Gaussian elimination, Plot) → four sim modules sharing a slider/animation framework → a `CONNECTIONS` data array driving both the clickable graph and the router. A `?test=1` query param runs console self-tests comparing sims to closed-form solutions.

**Tech Stack:** Vanilla JS, SVG (graph), Canvas 2D (sims), CSS. Verified via Playwright MCP browser.

**Spec:** `docs/superpowers/specs/2026-06-10-ee-pipeline-visualizer-design.md`

---

### Task 1: Skeleton — layout, theme, router shell

**Files:**
- Create: `apps/ee-pipeline.html`

- [ ] **Step 1: Write the HTML/CSS skeleton**

Dark theme study-app aesthetic. Structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>EE Pipeline — Math & Physics → Electrical Engineering</title>
<style>
  :root{
    --bg:#0e1116; --panel:#161b24; --ink:#dbe2ec; --muted:#8b97a8;
    --math:#5aa9ff; --phys:#ffb454; --ee:#7ce38b; --accent:#ff6e9c;
    --grid:#222a36;
  }
  *{box-sizing:border-box} body{margin:0;font:15px/1.5 system-ui;background:var(--bg);color:var(--ink);display:flex;height:100vh}
  #sidebar{width:340px;min-width:300px;border-right:1px solid var(--grid);overflow-y:auto;padding:12px}
  #main{flex:1;overflow-y:auto;padding:20px 28px}
  /* slider rows, readout chips, .eq equation blocks, .why explanation card */
</style>
</head>
<body>
  <nav id="sidebar"><h1>The Pipeline</h1><svg id="graph"></svg></nav>
  <main id="main"><div id="sim-root"></div></main>
<script>
"use strict";
// ===== 1. utils ===== (Task 2)
// ===== 2. data: CONNECTIONS ===== (Task 3)
// ===== 3. graph render ===== (Task 3)
// ===== 4. sims ===== (Tasks 4-7)
// ===== 5. router + boot ===== (Task 3)
</script>
</body>
</html>
```

- [ ] **Step 2: Verify it renders**

Open `file:///C:/Users/joe43/Documents/Joe_Vault/apps/ee-pipeline.html` via Playwright `browser_navigate`, snapshot. Expected: dark two-pane layout, sidebar title visible, no console errors (`browser_console_messages`).

- [ ] **Step 3: Commit**

```bash
git add apps/ee-pipeline.html && git commit -m "feat: EE pipeline app skeleton"
```

### Task 2: Core math utilities + self-tests

**Files:**
- Modify: `apps/ee-pipeline.html` (utils section)

- [ ] **Step 1: Implement RK4, Gaussian elimination, Plot**

```js
// rk4Step: y' = f(t,y), y is Float64Array-like array. Returns new array.
function rk4Step(f, t, y, h){
  const k1=f(t,y), k2=f(t+h/2, y.map((v,i)=>v+h/2*k1[i]));
  const k3=f(t+h/2, y.map((v,i)=>v+h/2*k2[i]));
  const k4=f(t+h,   y.map((v,i)=>v+h*k3[i]));
  return y.map((v,i)=>v + h/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]));
}
// gaussSolve: solves Ax=b with partial pivoting. A: array of rows, b: array. Returns x.
function gaussSolve(A,b){
  const n=b.length, M=A.map((r,i)=>[...r,b[i]]);
  for(let c=0;c<n;c++){
    let p=c; for(let r=c+1;r<n;r++) if(Math.abs(M[r][c])>Math.abs(M[p][c])) p=r;
    [M[c],M[p]]=[M[p],M[c]];
    for(let r=c+1;r<n;r++){ const f=M[r][c]/M[c][c]; for(let k=c;k<=n;k++) M[r][k]-=f*M[c][k]; }
  }
  const x=new Array(n).fill(0);
  for(let r=n-1;r>=0;r--){ let s=M[r][n]; for(let k=r+1;k<n;k++) s-=M[r][k]*x[k]; x[r]=s/M[r][r]; }
  return x;
}
// Plot: lightweight canvas line plotter with axes, multiple traces, auto/fixed y-range.
class Plot { constructor(canvas, opts){...} draw(traces){...} } // axes, gridlines, labels, legend
```

- [ ] **Step 2: Add self-test harness**

`runSelfTests()` invoked when `location.search` includes `test=1`; logs `SELFTEST PASS/FAIL <name>`:
1. RK4 on v' = (1−v)/τ (RC, τ=1) from 0 to 1τ, h=0.001 → |v(τ) − (1−e⁻¹)| < 1e−6.
2. RK4 on undamped LC: energy drift < 1e−6 over 10 cycles.
3. gaussSolve([[2,1],[1,3]],[5,10]) → x ≈ [1,3].

- [ ] **Step 3: Verify**

Navigate with `?test=1`, read console. Expected: 3× `SELFTEST PASS`, zero FAIL.

- [ ] **Step 4: Commit** — `git commit -m "feat: RK4, gauss solver, plotter + self-tests"`

### Task 3: Dependency graph + CONNECTIONS + router

**Files:**
- Modify: `apps/ee-pipeline.html` (data + graph + router sections)

- [ ] **Step 1: Define CONNECTIONS data**

```js
const SIMS = { rlc:{...}, analogy:{...}, nodal:{...}, fields:{...} }; // registered by Tasks 4-7: {title, mount(el)}
const NODES = [
  // {id, label, track:'math'|'phys'|'ee', x, y, sim, blurb}
  {id:'calc1', label:'Calc 1', track:'math', sim:'rlc'},
  {id:'calc2', label:'Calc 2', track:'math', sim:'rlc'},
  {id:'calc3', label:'Calc 3 (vector)', track:'math', sim:'fields'},
  {id:'diffeq', label:'Diff Eq', track:'math', sim:'rlc'},
  {id:'linalg', label:'Linear Algebra', track:'math', sim:'nodal'},
  {id:'phys1', label:'Phys 1: Mechanics', track:'phys', sim:'analogy'},
  {id:'phys2', label:'Phys 2: E&M', track:'phys', sim:'fields'},
  {id:'phys3', label:'Phys 3: Modern', track:'phys', sim:null},
  {id:'eee202',label:'Circuits 202', track:'ee', sim:'nodal'}, // → 350 → 352 → 334 → 340 → 480
];
const EDGES = [ {from:'calc1',to:'phys1',sim:'analogy'}, {from:'diffeq',to:'eee202',sim:'rlc'}, ... ];
```

Each sim entry carries a `why` HTML string distilled from the wiki page, naming the wiki pages it draws on (e.g. "[[Classical Mechanics in Electrical Engineering]]") as plain styled text.

- [ ] **Step 2: Render the SVG graph**

Build nodes (rounded rects, track-colored) and edges (paths with arrowheads) into `#graph` from NODES/EDGES; vertical layout: math column + physics column, arrows converging into the EE chain running down the bottom. Click node/edge → `show(simId)`; active element gets a glow class. Phys 3 (no sim) shows an info card instead.

- [ ] **Step 3: Router**

`show(simId)` clears `#sim-root`, renders title + `why` card + calls `SIMS[simId].mount(root)`. Default route: `analogy`.

- [ ] **Step 4: Verify** — Playwright: click 3 different nodes, snapshot each, panel title changes, no console errors.

- [ ] **Step 5: Commit** — `git commit -m "feat: dependency graph, connections data, router"`

### Task 4: RC/RLC transients sim

**Files:** Modify `apps/ee-pipeline.html` (sims section)

- [ ] **Step 1: Implement**

Mode toggle RC|RLC. Sliders (log-scale where natural): R 10Ω–10kΩ, L 1mH–1H, C 0.1µF–1mF, source 5V step.
State: series RLC, y=[v_C, i_L]; `f = (t,[v,i]) => [ i/C, (Vs − v − R*i)/L ]`; RC mode: `v' = (Vs−v)/(R*C)`.
Readouts: RC → τ=RC chip; RLC → ω₀=1/√(LC), ζ=(R/2)√(C/L), classification chip (underdamped ζ<1 / critical ≈1 / overdamped >1).
Equation block shows the ODE with live slider values substituted. Plot v_C(t) and i(t) traces; time window auto-scales to ~6τ or ~8/(ζω₀). Reset button. Re-simulate on any input (full re-integration, h = window/2000 — cheap).

- [ ] **Step 2: Self-test** — add SELFTEST: RLC with R chosen for ζ=1 reports "critically damped"; RC sim at t=τ within 1e−4 of 0.632·Vs.

- [ ] **Step 3: Verify** — Playwright: move R slider extremes, snapshot underdamped ringing vs overdamped creep; `?test=1` all PASS.

- [ ] **Step 4: Commit** — `git commit -m "feat: RC/RLC transient sim"`

### Task 5: Mass-spring ↔ RLC analogy sim

**Files:** Modify `apps/ee-pipeline.html`

- [ ] **Step 1: Implement**

Two canvases side by side + one shared plot below.
Left: animated mass on spring with damper (wall, coil spring drawn as zigzag whose length tracks x(t), mass block, dashpot). Right: series RLC schematic with charge-dot animation whose speed/direction tracks i(t).
Mapped slider pairs (one slider moves both systems): m↔L (0.1–5), b↔R (0–10), k↔1/C (1–50). Initial displacement release (x₀=1, q₀ analog).
Integrate BOTH systems separately with RK4 from their own equations (m x″ = −kx − bx′ and L q″ = −q/C − R q′ with mapped values); plot x(t) and q(t) on one axis — they coincide, which is the point. Equation block shows both ODEs aligned term-over-term with arrows (force↔voltage, mass↔inductance, damping↔resistance, spring↔1/C).

- [ ] **Step 2: Self-test** — SELFTEST: max|x(t)−q(t)| over the window < 1e−9 with mapped parameters.

- [ ] **Step 3: Verify** — Playwright snapshot: both animations move, traces overlap as one curve; drag damping slider → both decay faster.

- [ ] **Step 4: Commit** — `git commit -m "feat: mass-spring/RLC analogy sim"`

### Task 6: Nodal analysis Ax=b sim

**Files:** Modify `apps/ee-pipeline.html`

- [ ] **Step 1: Implement**

Fixed topology: 3 non-ground nodes. Vs=10V via R1 to node1; R2 node1–node2; R3 node2–gnd; R4 node2–node3; R5 node3–gnd. Source converted via Norton (Is=Vs/R1) so pure conductance form works.
Sliders R1–R5 (10Ω–10kΩ, log). Build G (3×3) and b live; render the matrix equation as an HTML grid `[G][v]=[b]` with numeric entries updating as sliders move; solve with `gaussSolve`; show x=[v1,v2,v3]. SVG schematic with node voltage labels colored by magnitude. Caption: "This is what SPICE does on every step."

- [ ] **Step 2: Self-test** — SELFTEST: KCL residual |G·v − b| < 1e−9; with all R equal, v1>v2>v3>0.

- [ ] **Step 3: Verify** — Playwright: drag R3 → matrix entries and node voltages update live; snapshot.

- [ ] **Step 4: Commit** — `git commit -m "feat: nodal analysis Ax=b sim"`

### Task 7: Fields & waves sim

**Files:** Modify `apps/ee-pipeline.html`

- [ ] **Step 1: Implement**

Canvas with draggable point charges (start: +1 and −1 dipole). E-field vector grid (~24×16 arrows, length ∝ log|E|, capped) recomputed per frame via Coulomb superposition; field lines traced from positive charges (Euler steps along Ê, stop at negative charge/border). Buttons: add +, add −, clear; double-click charge toggles sign; drag to move. Equation block: Coulomb's law + superposition note tying to Maxwell/Gauss.

- [ ] **Step 2: Self-test** — SELFTEST: field at midpoint of equal + + pair has |E| < 1e−12 (symmetry cancellation).

- [ ] **Step 3: Verify** — Playwright: snapshot dipole field, drag a charge (browser_drag), snapshot again — pattern follows.

- [ ] **Step 4: Commit** — `git commit -m "feat: E-field visualizer sim"`

### Task 8: Vault integration + final verification

**Files:**
- Modify: `wiki/questions/Research - Math and Physics Pipeline to Electrical Engineering.md` (add Companion App line under Overview)
- Modify: `wiki/log.md` (new entry at TOP — append-only convention)

- [ ] **Step 1: Add wiki link + log entry**

Wiki page, after the Overview paragraph: `> 🎛 **Companion app:** [ee-pipeline.html](../../apps/ee-pipeline.html) — interactive simulations of these connections.`
Log entry at top of `wiki/log.md` following its existing entry format, dated 2026-06-10.

- [ ] **Step 2: Full verification pass**

Playwright: load with `?test=1` → ALL self-tests PASS, zero console errors; click through every node/edge; screenshot each of the 4 sims.

- [ ] **Step 3: Commit** — `git commit -m "feat: EE pipeline visualizer — vault links + final pass"`

---

## Self-Review Notes

- Spec coverage: layout ✓ (T1/T3), 4 sims ✓ (T4–T7), CONNECTIONS routing ✓ (T3), numerical safety ✓ (clamped log sliders, fixed-h RK4, self-tests vs analytic), vault integration ✓ (T8), Playwright testing ✓ (every task).
- Phys 3 has no sim per spec scope — handled as info card (T3 Step 2), not a dangling route.
- Type consistency: `rk4Step(f,t,y,h)`, `gaussSolve(A,b)`, `SIMS[id].mount(el)`, `show(simId)` used uniformly.
