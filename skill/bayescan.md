---
name: bayescan
category: population-genomics
description: BayeScan - Population genomics FST outlier detection using Bayesian methods
tags: [outlier-detection, selection, fst, population-genomics, bayesian]
author: oxo-call-community
source_url: "https://cmpg.unibe.ch/software/BayeScan"
---

## Concepts

- **Tool Overview**: BayeScan identifies FST outliers (loci under selection) using Bayesian methods, distinguishing selection from demographic effects.

- **Bayesian Decomposition**: Decomposes population differentiation into population-specific and locus-specific components.

- **Selection Detection**: Identifies loci under positive or balancing selection.

- **False Discovery Control**: Controls for multiple testing using FDR (False Discovery Rate).

- **Multiple Populations**: Handles multiple populations simultaneously.

## Pitfalls

- **Sample Size**: Requires sufficient sample size per population (typically ≥10 individuals).

- **Population Structure**: Results affected by population structure. Interpret carefully.

- **Prior Odds**: Default prior odds may need adjustment for specific datasets.

- **Convergence**: MCMC must converge. Check convergence diagnostics.

## Examples

### Basic outlier detection
**Args:** `bayescan input.txt -out results -n 5000 -thin 10 -nbp 20 -pilot 5000`
**Explanation:** Runs BayeScan with 5000 MCMC iterations, thinning every 10 steps.

### Adjust prior odds
**Args:** `bayescan input.txt -out results -prior_odds 10`
**Explanation:** Uses prior odds of 10 for more stringent outlier detection.

### Set FDR threshold
**Args:** `bayescan input.txt -out results -fst_offset 0.05`
**Explanation:** Sets FST offset threshold to 0.05 for outlier calling.

### Multiple threads
**Args:** `bayescan input.txt -out results -threads 8`
**Explanation:** Uses 8 threads for parallel computation.

### Different output format
**Args:** `bayescan input.txt -out results -bayes factor`
**Explanation:** Outputs Bayes factors instead of default q-values for outlier identification.
