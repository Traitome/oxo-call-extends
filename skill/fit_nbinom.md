---
name: fit_nbinom
category: utility
description: "fit_nbinom is a Python script for fitting negative binomial distributions to count data via maximum likelihood estimation, commonly used for RNA-seq and NGS count modeling."
tags: [fit_nbinom, utility, statistics, negative-binomial, distribution, ngs, rna-seq, count-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/joachimwolff/fit_nbinom/"
---

## Concepts
- **Tool Overview**: fit_nbinom fits negative binomial distributions to count data using maximum likelihood estimation (MLE). Particularly useful for modeling overdispersed count data from RNA-seq and other NGS experiments.
- **Core Function**: Estimates the two parameters of the negative binomial distribution (size r and probability p) that best fit the observed count data by maximizing the likelihood function.
- **Negative Binomial in Genomics**: The negative binomial distribution is the standard model for RNA-seq counts where variance exceeds mean (overdispersion). Parameters are used for differential expression testing.
- **MLE Algorithm**: Uses numerical optimization (typically Newton-Raphson or similar) to find parameter values that maximize the probability of observing the given counts.
- **Input Format**: Accepts a text file with count values (one per line or space-separated) or directly via command line arguments.
- **Output**: Returns estimated r and p parameters, log-likelihood value, and optionally confidence intervals. Can output in JSON format for programmatic parsing.
- **Installation**: `conda install -c bioconda fit_nbinom` or `pip install fit_nbinom`. Requires Python 2.7+ or 3.x and scipy/numpy.

## Pitfalls
- **Count Data Only**: fit_nbinom is designed for non-negative integer count data. Fractional values or negative numbers produce undefined results.
- **Insufficient Data**: Small sample sizes (<20 observations) may lead to unreliable parameter estimates with wide confidence intervals.
- **Zero Inflation**: If data contains excess zeros beyond NB expectations, the simple NB fit may be poor. Consider zero-inflated models for such data.
- **Convergence Issues**: Numerical optimization may fail to converge for extreme dispersion values. Check log-likelihood of final fit.
- **Outlier Sensitivity**: Extreme outliers can distort parameter estimates. Consider removing extreme counts or using robust methods.
- **Overdispersion Parameter**: The estimated r parameter (size) is inversely related to dispersion. Small r indicates high overdispersion common in RNA-seq.

## Examples
### Fit from file with counts
**Args:** `fit_nbinom --input counts.txt --output results.txt`
**Explanation:** Reads count values from input file (one count per line) and writes parameter estimates to output file.

### Fit from command line values
**Args:** `fit_nbinom 10 15 12 18 14 20 11 13 16 17`
**Explanation:** Directly provides count values as command line arguments. Returns estimated NB parameters to stdout.

### JSON output format
**Args:** `fit_nbinom --input counts.txt --json`
**Explanation:** Returns parameters in JSON format: {"size": r, "prob": p, "loglik": value, "ci_lower": ..., "ci_upper": ...}. Useful for pipeline integration.

### Specify confidence level
**Args:** `fit_nbinom --input counts.txt --confidence 0.99 --output results.txt`
**Explanation:** Calculates 99% confidence intervals instead of default 95%. Use when more conservative interval estimate is needed.

### Verbose output with diagnostics
**Args:** `fit_nbinom --input counts.txt --verbose`
**Explanation:** Shows iteration history of optimization, convergence status, and goodness-of-fit statistics. Useful for troubleshooting convergence issues.

### Save fitted distribution plot
**Args:** `fit_nbinom --input counts.txt --plot fitted_distribution.png`
**Explanation:** Generates histogram of input data with fitted NB curve overlaid. Visual diagnostic for goodness of fit.

### Batch fit multiple genes
**Args:** `while read gene counts; do echo "$gene $(fit_nbinom $counts)"; done < gene_counts.txt`
**Explanation:** Processes multiple genes from file, fitting NB distribution to each gene's count vector. Common for RNA-seq gene-wise dispersion estimation.

### Use in Python script
**Args:** `python -c "from fit_nbinom import fit; r, p = fit([10,15,12,18]); print(f'r={r}, p={p}')"`
**Explanation:** Imports fit function directly in Python for programmatic use. Returns tuple of (size, prob) parameters.
