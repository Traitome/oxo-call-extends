---
name: dinf
category: population-genomics
description: dinf - Demographic inference from population genomic data.
tags: [dinf, population-genomics, demographic-inference, simulation]
author: oxo-call-community
source_url: "https://github.com/popgenmethods/dinf"
---

## Concepts

- **Tool Overview**: dinf is a tool for demographic inference from population genomic data using simulation-based approaches.
- **Core Function**: Infers demographic parameters such as population size changes, divergence times, and migration rates from population genomic data.
- **Input/Output**: Input: VCF files with population variants, FASTA sequences. Output: Inferred demographic parameters, model fits, visualization.
- **Algorithm**: Uses approximate Bayesian computation (ABC) or likelihood-based methods to fit demographic models to data.
- **Key Features**: Demographic model fitting, population size inference, divergence time estimation, migration rate estimation, visualization.
- **Installation**: `conda install -c bioconda dinf`

## Pitfalls

- **Input Requirements**: Requires high-quality population genomic variant data.
- **Model Complexity**: Choosing appropriate demographic model complexity is critical.
- **Computational Resources**: May require significant computational resources for complex models.
- **Sample Size**: Requires sufficient sample size for reliable inference.
- **Data Quality**: Poor quality variants can bias demographic inference.

## Examples

### Infer demographic parameters
**Args:** `dinf --vcf population.vcf --model demography.yaml --output params.tsv`
**Explanation:** Infers demographic parameters from population variant data using specified model.

### With prior specification
**Args:** `dinf --vcf population.vcf --model demography.yaml --priors priors.tsv --output params.tsv`
**Explanation:** Use custom prior distributions for demographic parameters.

### Generate model visualization
**Args:** `dinf --vcf population.vcf --model demography.yaml --output params.tsv --plot model.png`
**Explanation:** Generate visualization of inferred demographic model.

### Run multiple models
**Args:** `dinf --vcf population.vcf --model-dir models/ --output results/`
**Explanation:** Compare multiple demographic models and select best fit.

### Simulate data for validation
**Args:** `dinf --simulate --model demography.yaml --output simulated.vcf`
**Explanation:** Simulate population genomic data from demographic model for validation.