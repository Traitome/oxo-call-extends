---
name: ldhelmet
category: population-genomics
description: Inference of fine-scale crossover recombination rates from population genetic data
tags: [ldhelmet, population-genomics, recombination, LD, population-genetics]
author: oxo-call-community
source_url: "https://github.com/grenaud/ldhelmet"
---

## Concepts

- **Recombination Rate**: Estimates fine-scale crossover recombination rates
- **Population Genetics**: Analyzes population genetic data
- **Linkage Disequilibrium**: Uses LD patterns to infer recombination
- **Statistical Inference**: Bayesian inference framework
- **Fine-scale Analysis**: Resolves recombination hotspots at fine scale
- **Coalescent Model**: Uses coalescent-based statistical model

## Pitfalls

- **Sample Size**: Large sample sizes required for reliable inference
- **Population Structure**: Population structure affects LD patterns
- **Genotyping Errors**: Errors affect recombination rate estimation
- **Missing Data**: Missing genotypes reduce power
- **Computational Time**: Large datasets require significant computation
- **Mutation Rate**: Assumed mutation rate affects results

## Examples

### Estimate recombination rates
**Args:** `ldhelmet rjmcmc --num_threads 4 -o rates.txt`
**Explanation:** Runs MCMC to estimate recombination rates.

### Prepare input
**Args:** `ldhelmet table_gen --num_threads 4 -o lookup_tables.bin`
**Explanation:** Generates lookup tables for analysis.

### Post-process
**Args:** `ldhelmet post_process -i posterior_samples.txt -o rates.txt`
**Explanation:** Processes posterior samples.

### Set burn-in
**Args:** `ldhelmet rjmcmc --burn_in 10000 -o rates.txt`
**Explanation:** Sets burn-in period for MCMC.

### Specify region
**Args:** `ldhelmet rjmcmc --region chr1:1000000-2000000 -o rates.txt`
**Explanation:** Analyzes specific genomic region.

### Export hotspots
**Args:** `ldhelmet hotspots -i rates.txt -o hotspots.bed`
**Explanation:** Identifies recombination hotspots.