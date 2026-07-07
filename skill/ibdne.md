---
name: ibdne
category: population-genomics
description: IBDNe estimates historical effective population size from Identity-by-Descent segments.
tags: [ibdne, population-genomics, effective-population-size, IBD, demography]
author: oxo-call-community
source_url: "http://faculty.washington.edu/browning/ibdne.html"
---

## Concepts

- **Tool Overview**: IBDNe (v04Sep15.e78) is a program for estimating historical effective population size (Ne) using IBD segments, developed by the Browning lab at University of Washington.
- **Effective Population Size**: Ne represents the size of an idealized population that would experience the same level of genetic drift as the actual population.
- **IBD-based Inference**: Uses long shared IBD segments to estimate Ne from approximately 4 to 200+ generations ago.
- **Non-parametric Method**: Does not assume a specific demographic model, allowing flexible estimation of population size changes over time.
- **Input Requirements**: Takes IBD segment calls (typically from IBDseq or hap-ibd) as input.
- **Installation**: `conda install -c bioconda ibdne`

## Pitfalls

- **Sample Size Sensitivity**: Requires at least ~100 individuals for reliable estimates; smaller samples may produce unstable results.
- **IBD Call Quality**: Dependent on accurate IBD detection; false positives/negatives affect Ne estimation.
- **Recent vs Ancient**: Best for recent history (last 100 generations); less accurate for deeper time scales.
- **Population Homogeneity**: Assumes a homogeneous population; admixture can bias results.
- **Recombination Rate**: Local recombination rates affect segment detection; regions with low recombination may show inflated Ne estimates.
- **Linkage Disequilibrium**: High LD can lead to overestimation of IBD segment sharing.

## Examples

### Basic Ne estimation from IBD segments
**Args:** `ibdne input_ibd.txt out_prefix`
**Explanation:** Estimates historical effective population size from IBD segment file.

### With confidence intervals
**Args:** `ibdne input_ibd.txt out_prefix -seed 12345 -nboot 100`
**Explanation:** Runs 100 bootstrap replicates to generate confidence intervals for Ne estimates.

### Specify generation time
**Args:** `ibdne input_ibd.txt out_prefix -g 25`
**Explanation:** Sets generation time to 25 years for converting genetic distance to time.

### Filter by segment length
**Args:** `ibdne input_ibd.txt out_prefix -mincm 1.5`
**Explanation:** Only uses IBD segments longer than 1.5 cM to reduce noise from short segments.

### Output detailed statistics
**Args:** `ibdne input_ibd.txt out_prefix -verbose`
**Explanation:** Produces additional output including per-segment statistics and convergence information.