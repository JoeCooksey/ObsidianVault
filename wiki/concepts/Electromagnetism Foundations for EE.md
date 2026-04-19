---
type: concept
title: "Electromagnetism Foundations for EE"
status: developing
created: 2026-04-19
updated: 2026-04-19
tags:
  - physics
  - electromagnetism
  - electrical-engineering
  - maxwell
  - circuits
---

# Electromagnetism Foundations for EE

E&M (PHY 122 / PHY 132) is the direct physics parent of all circuit theory, electromagnetics, and RF engineering. Every passive component — resistor, capacitor, inductor — is understood from first-principles E&M. Every wire, trace, and antenna is an E&M problem.

---

## Coulomb's Law → Capacitance

Coulomb's law: $F = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r^2}$

This gives rise to the electric field $\mathbf{E}$ from a charge distribution. For a parallel-plate capacitor:
- Use Gauss's law to find $E = \sigma/\varepsilon_0 = Q/(\varepsilon_0 A)$ between the plates
- Integrate $E$ over the gap: $V = Ed$
- Derive capacitance from first principles: $$C = \frac{Q}{V} = \frac{\varepsilon_0 A}{d}$$

Real capacitors add a dielectric ($\varepsilon_r$): $C = \varepsilon_r \varepsilon_0 A/d$. Choosing a dielectric is a materials + E&M problem.

**PCB application**: trace-to-trace capacitance (parasitic capacitance) on a PCB is calculated exactly this way. At high frequencies (>100 MHz) it causes signal coupling and crosstalk.

---

## Electric Potential → Circuit Voltage

The electric potential $V$ is defined as the work per unit charge to move a test charge:
$$V = -\int \mathbf{E} \cdot d\mathbf{l}$$

**This is the origin of the word "voltage."** KVL (sum of voltages around a loop = 0) is a direct consequence of the conservative nature of the electric field ($\nabla \times \mathbf{E} = 0$ in static case).

Poisson's equation: $\nabla^2 V = -\rho/\varepsilon_0$ is used in semiconductor device simulation (MOSFET, BJT) to find the potential distribution inside the device.

---

## Biot-Savart and Ampere's Law → Inductance

The magnetic field from a current element: $d\mathbf{B} = \frac{\mu_0 I}{4\pi}\frac{d\mathbf{l}\times\hat{r}}{r^2}$

For a long straight wire: $B = \mu_0 I/(2\pi r)$. For a solenoid: $B = \mu_0 n I$.

Self-inductance is defined via magnetic flux linkage: $L = N\Phi/I$

**Toroid inductor** (used in power converters): use Ampere's law ($\oint \mathbf{H}\cdot d\mathbf{l} = NI$) to find $H$ inside the core, then $B = \mu_r \mu_0 H$, then $L = \mu_r \mu_0 N^2 A / l$. This is how transformer and inductor design works in power electronics — directly Ampere's law.

**PCB trace inductance**: every trace is a wire. At high frequency, trace inductance limits slew rate and causes overshoot on switching waveforms. A 1 cm PCB trace has ~10 nH of inductance — enough to cause significant ringing in a GaN gate driver.

---

## Faraday's Law → Transformers and Generators

$$\mathcal{E} = -\frac{d\Phi_B}{dt} = -N\frac{d\Phi}{dt}$$

This is the entire operating principle of:

### Transformers
Changing current in the primary winding creates a changing $B$ field in the core, inducing EMF in the secondary. Turns ratio: $V_2/V_1 = N_2/N_1$.

Every power supply has a transformer or a switched transformer (flyback, forward, LLC converter). Transformer design requires knowing Faraday's law to calculate the number of turns needed at a given switching frequency without saturating the core:
$$N = \frac{V \cdot t}{\Delta B \cdot A_c}$$

### Electric Generators
A rotating coil in a magnetic field: $\mathcal{E} = NBA\omega\sin(\omega t)$ — this is how AC power is generated. Every generator (wind, hydro, nuclear) works on this principle.

### Inductors as Energy Storage
$v = L\,di/dt$ is Faraday's law applied to a coil. The inductor stores energy in the magnetic field: $W = \frac{1}{2}LI^2$. This is how a buck converter stores energy — the inductor's magnetic field is the energy reservoir.

---

## Lorentz Force → Motors and Hall Sensors

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

The $q\mathbf{v}\times\mathbf{B}$ term (magnetic force on moving charge) is the fundamental principle behind:

### DC Motors
Force on a current-carrying conductor in a field: $\mathbf{F} = I\mathbf{L}\times\mathbf{B}$. For an $N$-turn coil: $\tau = NIAB\sin\theta$. This torque drives the rotor.

### Hall Effect Sensors
A current $I$ flows through a conductor in magnetic field $B$. The Lorentz force separates charges transversely, creating a Hall voltage:
$$V_H = \frac{IB}{nqt}$$
Used in: brushless motor commutation (every EV and drone motor uses Hall sensors to sense rotor position), current sensing (Hall-effect current sensors in power supplies), magnetic field measurement.

### Cyclotron Motion (vacuum tubes, particle accelerators)
$qvB = mv^2/r$ → $r = mv/(qB)$. Used in magnetrons (microwave ovens), mass spectrometers.

---

## Ampere-Maxwell Law → Displacement Current → Radiation

The full Ampere's law includes Maxwell's displacement current term:
$$\nabla\times\mathbf{H} = \mathbf{J} + \varepsilon\frac{\partial\mathbf{E}}{\partial t}$$

The $\varepsilon\,\partial\mathbf{E}/\partial t$ term is crucial:
- It makes Maxwell's equations predict wave solutions
- It means a capacitor (no conduction current through the dielectric) still "conducts" — the changing $E$ field acts like a current
- **This is why capacitors pass AC but block DC**

At high frequencies, the displacement current dominates, and a capacitor becomes a near-short. This is why bypass capacitors are placed at every IC power pin — they provide a low-impedance AC path to ground for switching transients.

---

## Maxwell's Equations — The Full Picture

In integral form (how you use them in PHY 122 / EEE 340):

| Law | Equation | EE Meaning |
|---|---|---|
| Gauss (E) | $\oint \mathbf{E}\cdot d\mathbf{A} = Q_\text{enc}/\varepsilon_0$ | Capacitance from geometry |
| Gauss (B) | $\oint \mathbf{B}\cdot d\mathbf{A} = 0$ | No magnetic monopoles; flux is conserved |
| Faraday | $\oint \mathbf{E}\cdot d\mathbf{l} = -d\Phi_B/dt$ | Transformer action; KVL origin |
| Ampere-Maxwell | $\oint \mathbf{B}\cdot d\mathbf{l} = \mu_0(I + \varepsilon_0 d\Phi_E/dt)$ | Inductance; displacement current; radiation |

Combining Faraday and Ampere-Maxwell gives the wave equation:
$$\nabla^2\mathbf{E} = \mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}, \quad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = 3\times10^8 \text{ m/s}$$

**This predicts light as an EM wave** — and it means every wire radiates at high enough frequency.

---

## Electromagnetic Compatibility (EMC)

At high frequencies, everything is an antenna. EMC engineering (required for FCC certification) uses E&M directly:
- **Common mode current** creates radiation (EMC failure); uses Faraday's and Ampere's law to model
- **Skin effect**: at high $f$, current crowds to conductor surface; effective resistance increases as $\sqrt{f}$. Power loss in PCB traces at 100 MHz vs 1 MHz is dramatically higher.
- **Shielding**: a Faraday cage redirects induced currents to cancel interior fields. Shielding effectiveness is an E&M boundary-condition problem.

---

## Semiconductor Physics — E&M at Microscale

- **p-n junction built-in potential**: formed by charge diffusion until the E field (drift) balances diffusion — a Poisson equation problem
- **MOSFET inversion layer**: gate voltage creates a surface electric field that inverts the semiconductor below the oxide; channel charge $Q_\text{ch} = C_\text{ox}(V_{GS}-V_{th})$
- **Depletion region width**: $W \propto \sqrt{V/N_D}$ — derived from Poisson's equation with doping profile

---

## E&M Concepts Mapped to EE Courses

| E&M Concept | Core Result | EE Application | Course |
|---|---|---|---|
| Gauss's law | $C = \varepsilon A/d$ | Capacitor design; PCB parasitics | EEE 202, EEE 340 |
| Electric potential | KVL origin | All circuit analysis | EEE 202 |
| Biot-Savart / Ampere | $L = \mu N^2 A/l$ | Inductor/transformer design | EEE 202, EEE 340 |
| Faraday's law | $v = L\,di/dt$; transformer turns ratio | All switching power supplies | EEE 202, EEE 340 |
| Lorentz force | Motor torque; Hall voltage | Motor control; current sensing | EEE 480, EEE 488 |
| Displacement current | Capacitors pass AC | Bypass cap design; filter theory | EEE 202 |
| Wave equation | $c = 1/\sqrt{\mu\varepsilon}$ | Transmission lines; antennas; RF | EEE 340, EEE 476 |
| Poisson's equation | $\nabla^2 V = -\rho/\varepsilon_0$ | MOSFET/BJT device physics | EEE 334 |
| Skin effect | AC resistance ∝ √f | PCB trace loss; EMC | EEE 340, EMC |
| Boundary conditions | Field continuity at interfaces | PCB stackup; waveguide design | EEE 340, EEE 476 |

---

## Related
- [[Calculus in Electrical Engineering]]
- [[Differential Equations in Electrical Engineering]]
- [[Classical Mechanics in Electrical Engineering]]
- [[Wide Bandgap Semiconductors]]
- [[Silicon Carbide Power Electronics]]
- [[EV Fast Charging Topologies]]
