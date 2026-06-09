---
type: concept
title: "University Physics 3 in Electrical Engineering"
status: developing
created: 2026-06-09
updated: 2026-06-09
tags:
  - physics
  - thermodynamics
  - optics
  - quantum
  - semiconductors
  - electrical-engineering
related:
  - "[[Electromagnetism Foundations for EE]]"
  - "[[Semiconductor Device Fundamentals]]"
  - "[[Wide Bandgap Semiconductors]]"
---

# University Physics 3 in Electrical Engineering

Physics 3 (ASU **PHY 241**: thermodynamics, kinetic theory, physical/wave optics, relativity, photons, matter waves, atomic physics) looks like a grab-bag — but it is the **gateway to everything below the circuit level**: semiconductor devices, photonics, and thermal design. Mechanics and E&M explain how circuits *behave*; Physics 3 explains why the components *exist*. (Source: [[ASU PHY 241 Course Description]], confidence: high)

---

## Thermodynamics + Kinetic Theory → Thermal Management

Every watt a chip dissipates must go somewhere. Thermo is the physics of that "somewhere":

- **Heat conduction** through die → solder → substrate → heatsink is a thermal-resistance chain, directly analogous to a resistor ladder ($\theta_{JA}$ in every datasheet). Junction temperature math IS thermodynamics.
- **Carnot/efficiency limits** govern heat engines, thermoelectric coolers (Peltier), and why converter efficiency matters at all.
- **Kinetic theory** underlies carrier thermal velocity, Johnson-Nyquist thermal noise ($v_n^2 = 4kTR\Delta f$), and temperature-dependent device parameters.
- For Joe's track this is load-bearing: [[WBG Thermal Management]] (junction temps, cooling strategies) and [[Silver Sintering Die-Attach]] / [[Power Module Ceramic Substrates]] are all applied thermodynamics. (confidence: high)

---

## Wave + Physical Optics → Photonics, Fiber, Lithography

Geometric optics (refraction, lenses) plus interference and diffraction:

- **Total internal reflection** = how optical fiber guides light; numerical aperture and modal dispersion are optics calculations.
- **Interference** = thin-film coatings, interferometers, laser cavities, and the operating principle of [[Thin-Film LiNbO₃ Electro-Optic Modulators|electro-optic modulators]] and silicon photonics.
- **Diffraction limits** set the resolution of photolithography — the entire reason EUV exists (13.5 nm light to print smaller features) traces to the diffraction limit $\sim \lambda/\text{NA}$. (confidence: high)
- Gratings → optical phased arrays, WDM demultiplexers, spectrometers.

---

## Photons, Matter Waves, Atomic Physics → Semiconductor Devices

The modern-physics third is the most important for EE:

- **Photoelectric effect / photons (E = hf)** → photodiodes, solar cells, image sensors, LEDs (bandgap sets emission color: $\lambda = hc/E_g$).
- **Matter waves + quantization** → electrons in a periodic crystal can only occupy allowed **energy bands**. Band theory is derived from quantum mechanical wave functions in a periodic lattice, and it is the foundation of understanding all solid-state devices — transistors, diodes, solar cells. Classical physics cannot explain why semiconductors conduct only under specific conditions, or how flash memory and LEDs work at all. (Source: [[Quantum Mechanics in Semiconductor Devices (overview)]], confidence: high)
- **The bandgap** ($E_g$): the single number behind Joe's whole specialization — Si 1.1 eV vs SiC 3.3 eV vs GaN 3.4 eV vs Ga₂O₃ ~4.8 eV. "Wide bandgap" is a quantum mechanics term. [[Wide Bandgap Semiconductors]] starts here.
- **Quantum tunneling** → flash memory programming, Zener breakdown, gate leakage at small nodes, and tunnel FETs.
- **Stimulated emission** (atomic physics) → lasers, the light source of all fiber-optic communication.
- **Relativity**: minor for most EE, but GPS clock correction and magnetism-as-relativistic-electrostatics are the classic touchpoints. (confidence: medium)

---

## Summary Table

| Physics 3 Topic | EE Application | Where It Lands |
|---|---|---|
| Thermodynamics / heat transfer | Junction temp, heatsinks, θJA, thermal noise | Power electronics, packaging |
| Kinetic theory | Thermal noise, carrier statistics | Analog design, devices |
| Geometric optics | Fiber optics, imaging, lens systems | Photonics, sensors |
| Interference/diffraction | Photolithography (EUV), modulators, gratings | Semiconductor manufacturing, photonics |
| Photons | LEDs, photodiodes, solar cells, lasers | Optoelectronics |
| Matter waves / quantization | **Band theory → all semiconductor devices** | EEE 352, device physics |
| Tunneling | Flash memory, Zener, leakage | Memory, scaling limits |

---

## The One-Sentence Version

> Mechanics and E&M explain the circuit; Physics 3 explains the **components** — why a diode rectifies, why an LED glows, why SiC beats silicon, and where the heat goes.

---

## Related
- [[Semiconductor Device Fundamentals]] — the EE course this physics unlocks
- [[Wide Bandgap Semiconductors]] — bandgap physics as career track
- [[WBG Thermal Management]] — applied thermodynamics
- [[Research - Math and Physics Pipeline to Electrical Engineering]]
