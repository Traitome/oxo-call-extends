---
name: fitter
category: utility
description: "Fitter is a Python tool that fits data to 30+ probability distributions and identifies the best fitting distribution using AIC or cross-validation."
tags: [fitter, utility, statistics, distribution-fitting, probability, python, data-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cokelaer/fitter"
---

## Concepts
- **Tool Overview**: Fitter fits data to 30+ common probability distributions and identifies the best fitting one using goodness-of-fit statistics. Useful for determining underlying probability models in data analysis.
- **Core Function**: Takes a dataset and fits multiple distribution families (Normal, Exponential, Gamma, Weibull, Lognormal, etc.), then ranks by Akaike Information Criterion (AIC) or sum of squared errors (SSE).
- **Distribution Library**: Supports 35+ distributions including: norm, expon, gamma, weibull_min, lognorm, beta, chi2, f, t, pareto, gumbel_r, gumbel_l, and many more.
- **Summary Statistics**: Automatically computes mean, median, std, variance, skewness, kurtosis for input data to help narrow candidate distributions.
- **Confidence Intervals**: Can bootstrap confidence intervals for fitted parameters to assess estimate reliability.
- **Visualization**: Generates plots comparing fitted distributions to data histogram, Q-Q plots, and CDF comparisons.
- **Installation**: `conda install -c bioconda fitter` or `pip install fitter`. Requires Python 3.x, scipy, matplotlib, pandas.

## Pitfalls
- **Large Datasets**: Fitting 35+ distributions to very large data (>100k points) is computationally expensive. Consider subsampling for initial exploration.
- **Convergence Failures**: Some distributions may fail to converge for certain datasets. Fitter reports failed fits but continues with others.
- **AIC vs SSE Ranking**: Different ranking criteria may produce different "best" distributions. Use AIC for model selection theory, SSE for empirical fit quality.
- **Continuous vs Discrete**: Fitter is designed for continuous distributions. Discrete data (counts) may show poor fits regardless of distribution.
- **Parameter Interpretation**: Different distributions may have same parameters with different meanings (e.g., shape/scale vs mean/variance). Understand parameterization before interpreting.
- **Multimodal Data**: Fitter assumes unimodal distributions. Multimodal data will show poor fits for all single distributions.

## Examples
### Basic fit to find best distribution
**Args:** `fitter data.txt --output fit_results.csv`
**Explanation:** Reads data from file, fits all distributions, saves ranked results to CSV. Top distribution in list is best fit by AIC.

### Specify distributions to test
**Args:** `fitter data.txt --distributions norm,gamma,expon,weibull_min`
**Explanation:** Only tests specified distributions instead of all 35+. Faster and useful when candidate distributions are known.

### Set number of bootstrap samples
**Args:** `fitter data.txt --n_bootstrap 1000 --output results.csv`
**Explanation:** Uses 1000 bootstrap iterations for confidence intervals. More bootstrap samples = narrower, more reliable intervals but slower.

### Generate visualization
**Args:** `fitter data.txt --plot --plot_dir ./plots`
**Explanation:** Creates PNG plots comparing fitted distributions to data. Includes histogram, PDF overlay, and goodness-of-fit statistics.

### Use in Python interactively
**Args:** `python -c "from fitter import Fitter; f = Fitter(data, distributions=['norm','gamma']); f.fit(); print(f.summary())"`
**Explanation:** Programmatic use in Python. More control over fitting process and access to individual parameter estimates.

### Get fitted parameters
**Args:** `fitter data.txt --get_params norm`
**Explanation:** Returns fitted parameters for normal distribution specifically. Useful when comparing specific distributions across multiple datasets.

### Set timeout per distribution
**Args:** `fitter data.txt --timeout 10`
**Explanation:** Sets 10-second timeout per distribution fit. Prevents hanging on difficult fits. Distributions exceeding timeout are marked as failed.

### Filter results by AIC threshold
**Args:** `fitter data.txt --output results.csv && awk 'NR==1 || $3 < 100' results.csv`
**Explanation:** Shows only distributions with AIC < 100. Filters out poorly fitting distributions from output.

### Fit to generated data
**Args:** `python -c "import numpy as np; from fitter import Fitter; f = Fitter(np.random.normal(0,1,1000)); f.fit(); print(f.summary())"`
**Explanation:** Demonstrates programmatic use with generated data. Normal distribution should rank highly for normally distributed input.
