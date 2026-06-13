---
type: concept
title: "ML Surrogate Modeling — Week 1 Daily Plan (Physical EE)"
created: 2026-06-13
updated: 2026-06-13
tags:
  - machine-learning
  - electrical-engineering
  - surrogate-modeling
  - gaussian-processes
  - bayesian-optimization
  - pyspice
  - roadmap
  - hands-on
status: developing
related:
  - "[[AI Skills Roadmap for Electrical Engineers]]"
  - "[[AI Applications in Electrical Engineering]]"
  - "[[EE Data Science Skills Roadmap]]"
  - "[[Python Self-Teaching Roadmap for EE]]"
  - "[[LTSpice Complete Skills Guide]]"
---
# ML Surrogate Modeling — Week 1 Daily Plan (Physical EE)

A concrete, ~1-hour-a-day, five-day plan to start building machine-learning skills aimed at the **physical/hardware side of EE** (power, RF/EM, semiconductors, analog, sensors) rather than the comms/DSP side. The week builds the full physical-EE ML loop on a circuit you already understand: **generate your own data → model it → use the model to design backwards.**

This is Week 1 of the broader [[AI Skills Roadmap for Electrical Engineers]]. The framing reflects the key reframe for hardware EE: ML here is mostly **[[Surrogate Modeling]]** (a fast model that replaces a slow simulator), **inverse design** (target behavior → design), **physics-informed learning**, and **edge inference on real hardware** — not classification on clean datasets.

## Core insight: lean on physics, not data volume

On the physical side, datasets are usually small — each sample is one expensive simulation or bench measurement. So **classical ML matters more than deep learning**: [[Gaussian Processes]] (small data + built-in uncertainty), random forests, and [[Bayesian Optimization]] are the bread and butter. You also have an unfair advantage: by scripting your own simulator you can *generate* training data on demand, sidestepping the "no dataset" problem.

## The daily shape

Every session: **15 min learn → 40 min build → 5 min log.** Always train on data from a system you understand — when the model is wrong, your physics intuition tells you why, which teaches ML far faster than someone else's MNIST notebook.

## One-time setup

```bash
python -m venv ml-ee && source ml-ee/bin/activate   # Windows: ml-ee\Scripts\activate
pip install numpy pandas matplotlib scikit-learn jupyter
pip install PySpice                                  # then: pyspice-post-installation --install-ngspice-dll
pip install gpytorch torch                           # for Thursday
```

[[PySpice]] needs the ngspice shared library. Every script below has a pure-Python analytical fallback so a failed simulator install never blocks the day.

## Week project: surrogate model of an RC low-pass filter

### Day 1 — Generate your own dataset

Learn: AC analysis & the −3 dB cutoff. Ground truth for an RC low-pass is `f_c = 1/(2πRC)` — use it to sanity-check the simulator. Build: sweep R and C, record cutoff, save to CSV.

```python
import numpy as np, pandas as pd

def rc_cutoff_spice(R, C):
    from PySpice.Spice.Netlist import Circuit
    from PySpice.Unit import u_V, u_Ohm, u_F, u_Hz, u_MHz
    c = Circuit('RC lowpass')
    c.SinusoidalVoltageSource('in', 'vin', c.gnd, amplitude=1@u_V)
    c.R(1, 'vin', 'vout', R@u_Ohm)
    c.C(1, 'vout', c.gnd, C@u_F)
    sim = c.simulator(temperature=25, nominal_temperature=25)
    an = sim.ac(start_frequency=1@u_Hz, stop_frequency=1@u_MHz,
                number_of_points=200, variation='dec')
    gain = np.abs(np.array(an['vout']))
    freq = np.array(an.frequency)
    return freq[np.argmin(np.abs(gain - 1/np.sqrt(2)))]   # -3 dB crossing

def rc_cutoff_analytic(R, C):
    return 1.0 / (2*np.pi*R*C)                            # fallback / ground truth

USE_SPICE = True
rng = np.random.default_rng(0)
R = 10**rng.uniform(2, 5, 200)      # 100 Ω … 100 kΩ
C = 10**rng.uniform(-9, -6, 200)    # 1 nF … 1 µF

rows = []
for r, cap in zip(R, C):
    try:
        fc = rc_cutoff_spice(r, cap) if USE_SPICE else rc_cutoff_analytic(r, cap)
    except Exception:
        fc = rc_cutoff_analytic(r, cap)
    rows.append((r, cap, fc))

pd.DataFrame(rows, columns=['R', 'C', 'fc']).to_csv('rc_data.csv', index=False)
```

Done when `rc_data.csv` has 200 rows. Log: did SPICE match `1/(2πRC)`, and by how much?

### Day 2 — Explore & prep

Learn: why feature scaling matters; R, C, and f_c each span orders of magnitude → **log-transform** them. Build: load, plot log-log, save prepped features.

```python
import pandas as pd, numpy as np, matplotlib.pyplot as plt

df = pd.read_csv('rc_data.csv')
fig, ax = plt.subplots(1, 2, figsize=(10,4))
ax[0].scatter(df.R, df.fc, s=8); ax[0].set(xscale='log', yscale='log', xlabel='R', ylabel='fc')
ax[1].scatter(df.C, df.fc, s=8); ax[1].set(xscale='log', yscale='log', xlabel='C', ylabel='fc')
plt.tight_layout(); plt.show()

df['logR'], df['logC'], df['logfc'] = np.log10(df.R), np.log10(df.C), np.log10(df.fc)
df.to_csv('rc_data_prepped.csv', index=False)
```

Done when the log-log scatter shows clean straight lines (the physics is multiplicative). Log: what slope vs. R and vs. C, and why?

### Day 3 — Baseline models

Learn: train/test split, MAE vs. R², why you always need a dumb baseline first. Build:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv('rc_data_prepped.csv')
X, y = df[['logR','logC']].values, df['logfc'].values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)

for name, model in [("Linear", LinearRegression()),
                    ("Forest", RandomForestRegressor(n_estimators=200, random_state=0))]:
    model.fit(Xtr, ytr); p = model.predict(Xte)
    print(f"{name:7s}  MAE={mean_absolute_error(yte,p):.4f}  R2={r2_score(yte,p):.4f}")
```

Done when linear regression nearly nails it (R² ≈ 1.0). Key lesson: linear *beats* the random forest because in log-space the relationship is exactly linear — **match the model to the physics.**

### Day 4 — Gaussian Process with uncertainty

Learn: a [[Gaussian Processes|GP]] predicts a *distribution* — mean **and** error bars. That uncertainty is why GPs dominate expensive-simulation modeling. Build:

```python
import torch, gpytorch, pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('rc_data_prepped.csv')
X = torch.tensor(df[['logR','logC']].values, dtype=torch.float32)
y = torch.tensor(df['logfc'].values, dtype=torch.float32)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)

class GP(gpytorch.models.ExactGP):
    def __init__(self, Xtr, ytr, lik):
        super().__init__(Xtr, ytr, lik)
        self.mean = gpytorch.means.ConstantMean()
        self.cov  = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel(ard_num_dims=2))
    def forward(self, x):
        return gpytorch.distributions.MultivariateNormal(self.mean(x), self.cov(x))

lik = gpytorch.likelihoods.GaussianLikelihood()
model = GP(Xtr, ytr, lik)
model.train(); lik.train()
opt = torch.optim.Adam(model.parameters(), lr=0.1)
mll = gpytorch.mlls.ExactMarginalLogLikelihood(lik, model)
for i in range(100):
    opt.zero_grad(); loss = -mll(model(Xtr), ytr); loss.backward(); opt.step()

model.eval(); lik.eval()
with torch.no_grad(), gpytorch.settings.fast_pred_var():
    pred = lik(model(Xte))
    print(f"GP  MAE={(pred.mean - yte).abs().mean():.4f}  mean σ={pred.stddev.mean():.4f}")
```

Done when GP MAE is comparable to linear and you can print a σ per prediction. Log: where is σ largest — and does it match sparse regions of training data? (It should.)

### Day 5 — Inverse design

Learn: forward model = design → behavior; inverse design = target behavior → design. Build: invert the surrogate to find (R, C) for a desired cutoff. The reliable path is optimizing over the trained surrogate with SciPy ([[Bayesian Optimization]] via BoTorch/Ax is the "proper" route for expensive black boxes, but its API churns — SciPy gets a correct answer today).

```python
import numpy as np, torch
from scipy.optimize import minimize

TARGET_FC = 1_000.0
target_log = np.log10(TARGET_FC)

def predict_logfc(logR, logC):
    x = torch.tensor([[logR, logC]], dtype=torch.float32)
    with torch.no_grad(), gpytorch.settings.fast_pred_var():
        return lik(model(x)).mean.item()

fixed_logC = -7.0                                  # pin C = 100 nF, solve for R
obj = lambda v: (predict_logfc(v[0], fixed_logC) - target_log)**2
res = minimize(obj, x0=[3.0], method='Nelder-Mead')

R_found, C_found = 10**res.x[0], 10**fixed_logC
print(f"Design: R={R_found:.0f} Ω, C={C_found*1e9:.0f} nF")
print(f"Analytic check: fc = {1/(2*np.pi*R_found*C_found):.0f} Hz (target {TARGET_FC:.0f})")
```

Done when the analytic check lands near 1 kHz. You've closed the loop: generated data → modeled it → used the model to design backwards.

## Weekend wrap

Combine the five scripts into one notebook: **problem → data → baselines → GP → inverse design**. That notebook is the first portfolio piece and the template for every future week — swap the RC filter for a transistor I-V curve, an antenna resonance, or a thermal model.

## Pitfalls specific to the physical side

- **Don't reach for deep learning first.** With 50–500 expensive samples, a GP or random forest beats a neural net.
- **Respect units & scaling.** Physical features span many orders of magnitude — normalize (log-transform), or training breaks.
- **Validate against physics, not just held-out error.** A model that violates conservation laws is wrong even if RMSE looks good.
- **Watch extrapolation.** Surrogates are only trustworthy inside their training domain.

## Starter "daily project" ideas (pick one per week)

- Predict a transistor's drain current from bias + W/L (SPICE sweeps).
- Predict antenna resonant frequency from patch dimensions (EM sim, or analytic to start).
- Classify motor health from vibration/current waveforms (public predictive-maintenance dataset).
- Build a physics-informed NN that solves the 1D heat equation and check against the analytical solution.
