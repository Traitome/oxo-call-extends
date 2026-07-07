---
name: bbmix
category: utility
description: BBMix - Inference of beta-binomial mixture model for allele-specific expression
tags: [bbmix, utility, beta-binomial, mixture-model, ASE]
author: oxo-call-community
source_url: "https://github.com/statbiomed/betabinmix"
---

## Concepts

- **Tool Overview**: BBMix (v0.2.2) performs inference of beta-binomial mixture models, primarily used for allele-specific expression analysis in RNA-seq data.
- **Core Function**: Fits beta-binomial mixture models to identify allele-specific expression patterns.
- **Mixture Model**: Uses finite mixture models to detect distinct expression states.
- **Beta-Binomial Distribution**: Models overdispersed count data common in sequencing experiments.
- **Allele-Specific Expression**: Identifies loci with differential expression between alleles.
- **Input/Output**: Accepts allele count data; outputs mixture model parameters and posterior probabilities.
- **Installation**: `conda install -c bioconda bbmix`.

## Pitfalls

- **Model Selection**: Number of mixture components affects results; need model comparison.
- **Convergence**: MCMC or EM algorithms require proper convergence checks.
- **Small Counts**: May struggle with low-coverage loci.
- **Prior Specification**: Results sensitive to prior choices.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic inference
**Args:** `bbmix -i allele_counts.txt -o results.txt`
**Explanation:** Runs beta-binomial mixture model inference on allele count data.

### Specify components
**Args:** `bbmix -i allele_counts.txt -k 3 -o results.txt`
**Explanation:** Fits mixture model with 3 components.

### EM algorithm
**Args:** `bbmix -i allele_counts.txt --em -o results.txt`
**Explanation:** Uses EM algorithm for parameter estimation.

### MCMC inference
**Args:** `bbmix -i allele_counts.txt --mcmc -n 10000 -o results.txt`
**Explanation:** Uses MCMC with 10000 iterations for Bayesian inference.

### Output posteriors
**Args:** `bbmix -i allele_counts.txt --posterior -o results.txt`
**Explanation:** Outputs posterior probabilities for each component.

### Include covariates
**Args:** `bbmix -i allele_counts.txt -c covariates.txt -o results.txt`
**Explanation:** Includes covariate information in the model.

### Display help
**Args:** `bbmix --help`
**Explanation:** Shows all available command-line options and usage information.