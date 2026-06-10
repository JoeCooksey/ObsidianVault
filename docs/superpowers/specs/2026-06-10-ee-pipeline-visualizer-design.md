# EE Pipeline Visualizer — Design Spec

Date: 2026-06-10
Status: Approved by Joe (design review 2026-06-10)
Source material: `wiki/questions/Research - Math and Physics Pipeline to Electrical Engineering.md`

## Purpose

A personal study aid for Joe's ASU EE coursework that visualizes how the six
"weed-out" math/physics courses feed electrical engineering, with interactive
simulations for the key connections. Depth and correct math matter more than
polish.

## Deliverable

One self-contained file: `apps/ee-pipeline.html` in the vault root.

- Zero dependencies: no build step, no CDN, no npm. Works offline, opens from
  Explorer or Obsidian.
- SVG for the dependency graph, `<canvas>` for simulations, vanilla JS.
- Equations rendered with styled HTML/Unicode (no KaTeX).

## Layout

Split view:

- **Left sidebar** — the dependency graph from the wiki page: math track
  (Calc 1, Calc 2, Calc 3, Diff Eq, Linear Algebra) and physics track
  (Physics 1 Mechanics, Physics 2 E&M, Physics 3 thermo/optics/quantum)
  converging into the EE course chain (Circuits EEE 202 → Signals 350 →
  Devices 352 → Electronics 334 → EM 340 → Control 480). Edges and nodes are
  clickable; the active connection highlights.
- **Right panel** — the selected simulation, its live equation readout, and a
  "why this connects" explanation distilled from the wiki page, naming the
  linked courses/wiki pages.

## Simulations

Shared infrastructure: fixed-timestep RK4 integrator, slider component,
requestAnimationFrame render loop, reset button per sim.

1. **RC/RLC transients** — toggle first-order RC vs second-order RLC; sliders
   for R, L, C; step input; live v(t)/i(t) plot. Readouts: τ for RC; ζ, ω₀,
   and over/under/critically-damped classification for RLC. The ODE displays
   with current slider values substituted in.
   *Connection: Calculus (i = C dv/dt) + Differential Equations.*
2. **Mass-spring ↔ RLC analogy** — side-by-side animated mass-on-spring and
   series RLC driven by the same second-order ODE. Mapped slider pairs
   (m↔L, b↔R, k↔1/C); both response traces plot on one axis to show they
   coincide exactly.
   *Connection: Physics 1 Mechanics as the template for circuit transients.*
3. **Nodal analysis Ax=b** — fixed 3-node resistor network with a source;
   adjust resistor values and watch the conductance matrix G and vector b
   rebuild and re-solve live (Gaussian elimination), node voltages displayed
   on the schematic. Framing: "this is what SPICE does."
   *Connection: Linear Algebra.*
4. **Fields & waves** — draggable point charges on a canvas with a live
   E-field vector grid and field lines (Coulomb superposition), charge-sign
   toggling.
   *Connection: Physics 2 E&M → EM course / components.*

## Data flow

A single `CONNECTIONS` array maps each graph edge/node to a sim config plus
explanation text. Clicking a graph element routes the right panel. No state
persistence.

## Numerical safety

- Slider ranges clamped to numerically stable values.
- Fixed-timestep RK4.
- Physics sanity-checked against analytic solutions during development
  (e.g., RC charging vs 1 − e^(−t/τ)).

## Vault integration

- Add a "Companion app" link line to the pipeline wiki page.
- Add a log entry at the top of `wiki/log.md`.

## Testing

Open the file in a browser via Playwright, exercise each simulation,
screenshot-verify rendering and interaction, and compare simulation outputs
to closed-form solutions.

## Out of scope

- Probability/statistics, complex analysis, numerical-methods content
  (flagged as open questions on the wiki page).
- Mobile layout, deployment, persistence, sharing polish.
