---
name: hlafreq
category: immunology
description: Download and combine HLA allele frequency data from multiple studies.
tags: [hlafreq, HLA, immunology, frequency, population genetics]
author: oxo-call-community
source_url: "https://github.com/BarinthusBio/HLAfreq"
---

## Concepts

- **HLA Frequency Data Integration**: hlafreq (v0.0.6) enables automated downloading and combining of HLA allele frequencies from multiple datasets, including data from allelefrequencies.net.
- **Dirichlet Distribution Modeling**: Combines allele frequency estimates using Dirichlet distribution, with default weighting of 2x sample size (accounting for two alleles per person).
- **Population Diversity Analysis**: Useful for studying regional diversity in immune genes and estimating population's ability to mount immune responses to specific epitopes.
- **Installation via Conda**: Recommended installation through bioconda with `conda create -n hlafreq bioconda::hlafreq`.
- **pymc Dependency**: Uses pymc for estimating credible intervals, requiring proper channel configuration for successful installation.

## Pitfalls

- **Installation Challenges**: pymc dependency may cause installation issues; ensure conda channel priority is set correctly.
- **g++ Compilation Warning**: Missing g++ compiler may cause performance degradation; install cxx-compiler via conda if needed.
- **Memory Requirements**: Estimating confidence intervals can be memory-intensive for large datasets.
- **Windows Multiprocessing**: On Windows, scripts need `if __name__ == "__main__":` guard for multiprocessing support.
- **Data Source Reliance**: Dependent on external data sources like allelefrequencies.net; network issues may affect downloads.

## Examples

### Download HLA frequency data from allelefrequencies.net
**Args:** `hlafreq download --population EUR --output frequencies.csv`
**Explanation:** Downloads HLA frequency data for the European population and saves to CSV file.

### Combine multiple frequency datasets
**Args:** `hlafreq combine --inputs freq1.csv freq2.csv --output combined.csv --weight-by samplesize`
**Explanation:** Combines multiple frequency datasets using sample size weighting and outputs the merged result.

### Calculate confidence intervals
**Args:** `hlafreq ci --input frequencies.csv --output ci_results.csv`
**Explanation:** Estimates credible intervals for allele frequencies using pymc.

### Generate population comparison report
**Args:** `hlafreq compare --populations EUR ASN AFR --output comparison.pdf`
**Explanation:** Compares HLA allele frequencies across multiple populations and generates a PDF report.

### Custom weighting scheme
**Args:** `hlafreq combine --inputs freq1.csv freq2.csv --output weighted.csv --weight-column population_size`
**Explanation:** Combines datasets using a custom weighting column instead of the default sample size.