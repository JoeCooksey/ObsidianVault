---
type: source
title: "PySDR: Filters Guide — Python DSP Reference"
source_type: educational_website
author: PySDR.org
date_published: 2025
url: https://pysdr.org/content/filters.html
confidence: high
key_claims:
  - "scipy.signal.firwin() is the primary FIR filter design function"
  - "101 taps is a good starting point for FIR design"
  - "scipy.signal.lfilter() applies filter; lfilter_zi() manages stateful filtering"
  - "Complex-tap filters can pass asymmetric frequency ranges (not possible with real-tap FIR)"
  - "Hamming window is the standard choice for FIR — balances passband and stopband ripple"
tags:
  - python
  - signal-processing
  - DSP
  - filter-design
  - source
---

# PySDR: Filters — Python DSP Reference

Open-source educational resource on SDR (Software Defined Radio) and DSP using Python. The filters chapter is the definitive Python FIR/IIR filter design reference.

## Core Functions Covered

**FIR Design:**
- `scipy.signal.firwin(numtaps, cutoff, fs=fs)` — Hamming-windowed linear-phase FIR
- `scipy.signal.firwin2(numtaps, freqs, gains)` — arbitrary frequency response design
- `scipy.signal.freqz(taps, worN=8000)` — compute frequency response of any filter

**Convolution / Application:**
- `np.convolve(signal, taps)` — basic filter application
- `scipy.signal.fftconvolve()` — faster for long signals
- `scipy.signal.lfilter()` — stateful filtering (for streaming data)
- `scipy.signal.lfilter_zi()` — initial conditions (eliminates transients)

**FFT Operations:**
- `np.fft.fft()` / `ifft()` — full spectrum
- `np.fft.fftshift()` — center DC in plot

## Contribution to Research

Validates the FIR/IIR filter design approach in Projects 9–10. The PySDR site is the best free Python DSP reference for EE students — it covers SDR/RF engineering with Python, relevant for RF track in Year 3+.
