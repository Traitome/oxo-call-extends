---
name: influx_si
category: metabolomics
description: Metabolic flux and concentration estimation based on stable isotope labeling
tags: [influx_si, metabolic-flux, stable-isotope, metabolomics]
author: oxo-call-community
source_url: "https://influx-si.readthedocs.io/"
---

## Concepts

- **Tool Overview**: influx_si (v7.4.3) is a software suite for estimating metabolic fluxes and metabolite concentrations using stable isotope labeling data.
- **Core Components**: Includes influx_s (stationary labeling) and influx_i (instationary labeling) for different experimental designs.
- **Algorithm**: Uses NLSIC optimization algorithm for reliable convergence and high numerical precision.
- **Input/Output**: Accepts metabolic network definitions, labeling measurements (.miso files), and outputs flux distributions with confidence intervals.
- **Features**: Supports cumomer and EMU frameworks, parallel experiments, metabolite pool confusion handling, and chi2 goodness-of-fit testing.

## Pitfalls

- **Network Definition**: Metabolic network must be properly defined with correct stoichiometry.
- **Labeling Data Quality**: Results depend heavily on the quality and completeness of labeling measurements.
- **Computational Resources**: Complex networks may require significant computational resources.
- **Parameter Tuning**: Optimization parameters may need adjustment for specific experimental setups.
- **Convergence Issues**: Ill-conditioned systems may require multiple optimization runs with different starting points.

## Examples

### Run stationary flux analysis
**Args:** `influx_s -n network.net -m measurements.miso -o results/`
**Explanation:** Performs stationary metabolic flux analysis using network and measurement files.

### Run instationary flux analysis
**Args:** `influx_i -n network.net -m time_series.miso -o dynamic_results/`
**Explanation:** Analyzes instationary labeling data with time-series measurements.

### Parallel processing
**Args:** `influx_s -n network.net -m measurements.miso -p 8 -o results/`
**Explanation:** Uses 8 parallel processes for faster computation.

### Specify initial fluxes
**Args:** `influx_s -n network.net -m measurements.miso -i initial_fluxes.txt -o results/`
**Explanation:** Provides initial flux estimates for optimization.

### Include metabolite concentration estimation
**Args:** `influx_s -n network.net -m measurements.miso -c -o results/`
**Explanation:** Estimates both fluxes and metabolite concentrations.

### Generate visualization
**Args:** `influx_s -n network.net -m measurements.miso -o results/ --plot`
**Explanation:** Generates graphical output of flux distribution.