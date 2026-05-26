---
type: concept
title: "EE Data Science Skills Roadmap"
created: 2026-05-26
updated: 2026-05-26
tags:
  - data-science
  - electrical-engineering
  - roadmap
  - skills
  - career
status: developing
---

# EE Data Science Skills Roadmap

## Who This Is For
An EE student (or early-career engineer) who already has Python basics and wants to add data science skills for high-value EE roles — specifically in power systems, BMS, renewable energy, or industrial analytics. See [[Data Science in Electrical Engineering]] for the application context.

## Skill Gaps to Fill (EE → DS)
Things not taught in a standard EE curriculum:
- **pandas** — the most important single tool; 80% of DS work is data cleaning and reshaping
- **SQL** — EE data lives in historian databases (OSIsoft PI, InfluxDB, PostgreSQL)
- **ML workflow** — train/test split, cross-validation, evaluation metrics (ROC-AUC, precision/recall), leakage prevention
- **Feature engineering** — rolling windows, lag features, Fourier features for time-series
- **Statistical hypothesis testing** — t-test, chi-square, ANOVA, confidence intervals
- **Stakeholder visualization** — communicating findings to non-engineers via plotly dashboards

## The Learning Sequence

### Phase 1 — Python Foundation (already done or 1-2 weeks)
- `automatetheboringstuff.com` or Kaggle Python course
- If Python basics are solid, skip to Phase 2

### Phase 2 — pandas + SQL (2-4 weeks)
- **Kaggle Pandas course** (free, 5 hours) — the single highest-leverage resource here
- Learn: `read_csv`, `groupby`, `merge`, `resample`, `rolling`, `pivot_table`, handling missing data
- **SQL**: mode.com/sql-tutorial (free) or SQLite built into Python — learn joins, aggregations, window functions
- Goal: clean a real EE dataset (vibration CSV, meter data, LTSpice output) entirely in pandas

### Phase 3 — ML Fundamentals (4-6 weeks)
Kaggle course sequence (hands-on first, free):
1. Intro to Machine Learning
2. Intermediate Machine Learning (feature engineering, pipelines)
3. Data Cleaning
4. Feature Engineering (especially cross-validation and lag features for time-series)
5. ML Explainability
- Reference book: *Hands-On Machine Learning* (Aurélien Géron, O'Reilly)
- Core algorithms to know: Random Forest, Gradient Boosting (XGBoost), Logistic Regression, SVM, Isolation Forest, k-means clustering

### Phase 4 — Time-Series and Signal Processing (4-6 weeks)
EEs have a natural advantage here — the math is already familiar.
- **statsmodels**: ARIMA, STL decomposition, seasonal decomposition — `pip install statsmodels`
- **SciPy.signal**: FFT feature extraction from waveform data, Welch PSD, spectrogram — already in EE Python stack
- DataCamp's *Data Scientist's Guide to Signal Processing* — free
- Key concept: **feature engineering from waveforms** = FFT bins + rolling statistics + lag features as inputs to sklearn models

### Phase 5 — Deep Learning for Sequences (4-8 weeks)
- PyTorch LSTM for time-series prediction (SOC estimation, demand forecasting, anomaly detection)
- Fast.ai Part 1 (free, fastai.com) — best intro to practical deep learning for engineers
- Target: build one LSTM model on real or synthetic sensor data end-to-end (train → evaluate → visualize predictions)

### Phase 6 — EE-Specific DS Projects (ongoing)
See the 7-project ladder in [[Research - Data Science in Electrical Engineering]]:
1. Motor Vibration FFT Analyzer (pandas + SciPy.signal)
2. Transformer Fault Predictor (Random Forest on temperature logs)
3. Smart Meter Load Forecaster (ARIMA + XGBoost)
4. Battery SOC Estimator (LSTM vs Kalman)
5. Power Quality Anomaly Detector (Isolation Forest + LSTM autoencoder)
6. LTSpice Surrogate Model (PyLTSpice → pandas → sklearn)
7. SCADA Dashboard (Streamlit or Plotly Dash)

Project 6 is the bridge between [[Python EE Project Ladder]] and data science — it uses tools Joe already has.

## Parallel Path: Domain Specialization

### Track A — Battery/BMS DS
BMS Data Scientist = highest EE×DS salary ceiling ($130-220k).
- Add: PyTorch LSTM for SOC/SOH
- Study: electrochemical impedance spectroscopy (EIS) data formats, cycle aging models
- Target companies: Tesla, Rivian, Lucid, QuantumScape, CATL, Panasonic EV
- Differentiator: combine EE device physics knowledge with ML time-series → rare combination

### Track B — Power Systems / Grid Analytics
Energy Analytics Engineer ($100-145k), growing as renewable penetration increases.
- Add: statsmodels (ARIMA/STL), XGBoost, SQL for InfluxDB/OSIsoft PI
- Learn: PMU data format, SCADA data schemas, smart meter interval data structure
- Target companies: PG&E, Southern California Edison, CAISO, Enel, NextEra
- Differentiator: Python + power system domain knowledge is scarce in pure DS hires

### Track C — Industrial/Manufacturing ML
Predictive maintenance ($90-135k), largest single market for DS in EE.
- Add: scikit-learn (Isolation Forest, Random Forest), SciPy.signal (MCSA)
- Learn: vibration signature databases, bearing fault frequency formulas
- Target companies: Siemens, ABB, Rockwell Automation, GE Vernova, Emerson

## Joe's Specific Action Stack
Joe's [[Python EE Project Ladder]] already covers NumPy, SciPy, and matplotlib. The incremental steps:
1. **This week**: Kaggle Pandas course (5 hrs, free) — adds the missing piece
2. **Month 4-5** (alongside Python EE Phase 1): Add `pd.read_csv`, `resample`, `rolling` to existing workflows
3. **Month 5-6**: Kaggle ML sequence (run in parallel with EE sim projects)
4. **Month 6**: Project 6 — LTSpice surrogate model — the natural bridge project
5. **Month 7-8**: MCSA vibration analysis project (highest EE+DS signal to a hiring manager)
6. **Month 9+**: Choose Track A (BMS, highest ceiling) or Track B (grid, more openings)

## Key Resources
| Resource | Cost | Priority |
|----------|------|----------|
| Kaggle Pandas course | Free | S-tier, do first |
| Kaggle ML sequence (7 courses) | Free | S-tier |
| mode.com/sql-tutorial | Free | A-tier |
| fast.ai Part 1 | Free | A-tier (Phase 5) |
| *Hands-On Machine Learning* (Géron) | ~$60 / free library | A-tier reference |
| DataCamp Signal Processing guide | Free | A-tier |
| Towards Data Science (Medium) | Free | B-tier ongoing |

## Related Pages
- [[Data Science in Electrical Engineering]] — application domain overview
- [[AI Skills Roadmap for Electrical Engineers]] — broader AI/ML roadmap (Phase 3-4)
- [[Python EE Project Ladder]] — foundational Python project sequence (Projects 1-19)
- [[Python in Electrical Engineering]] — PyVISA, python-control, PyLTSpice
- [[Research - Data Science in Electrical Engineering]] — full source with 8 findings
