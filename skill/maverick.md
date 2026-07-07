---
name: maverick
category: population-genomics
description: Bayesian clustering for genetic data to infer population structure.
tags: [maverick, population-structure, Bayesian-clustering]
author: oxo-call-community
source_url: "https://github.com/bobverity/MavericK"
---

## Concepts

- **Tool Overview**: MavericK performs Bayesian clustering of population-genetic data.
- **Core Function**: Infers population structure from genetic markers.
- **Bayesian Inference**: Uses MCMC for posterior inference.
- **Admixture Modeling**: Supports admixture between populations.
- **Input/Output**: Accepts VCF or genotype files, produces clustering results.
- **Installation**: `conda install -c bioconda maverick`

## Pitfalls

- **Computation Time**: MCMC sampling can be slow for large datasets.
- **Convergence**: Requires proper convergence diagnostics.
- **K Selection**: Choosing number of populations (K) is challenging.
- **Prior Sensitivity**: Results may depend on prior specifications.
- **Memory Requirements**: High memory for large genotype matrices.
- **Missing Data**: Handles missing data but may affect accuracy.

## Examples

### Run Bayesian clustering
**Args:** `maverick -i genotypes.vcf -o results/`
**Explanation:** Performs Bayesian clustering on VCF data.

### With K populations
**Args:** `maverick -i genotypes.vcf -k 3 -o results/`
**Explanation:** Infers 3 populations from data.

### Admixture model
**Args:** `maverick -i genotypes.vcf -a -o results/`
**Explanation:** Runs admixture model.

### MCMC settings
**Args:** `maverick -i genotypes.vcf --iter 100000 --burnin 10000 -o results/`
**Explanation:** Sets MCMC iterations and burn-in.

### Plot results
**Args:** `maverick -i genotypes.vcf -o results/ --plot`
**Explanation:** Generates visualization of clustering results.

### Help documentation
**Args:** `maverick --help`
**Explanation:** Displays available commands and options.
