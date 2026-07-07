---
name: theta2
category: analysis
description: Theta2 - Population genetics statistics calculator for measuring genetic diversity.
tags: [theta2, population-genetics, theta, genetic-diversity, coalescent, snp]
author: oxo-call-community
source_url: "https://github.com/compbio/theta2"
---

## Concepts

- **Tool Overview**: Theta2 - A tool for estimating population genetics statistics including theta (θ) from genetic data.
- **Core Function**: Calculates theta estimators (θW, θπ, θL) and other population genetics parameters from SNP data.
- **Input**: VCF files or aligned sequences, population information.
- **Output**: Population genetics statistics, theta estimates, diversity metrics.
- **Installation**: `pip install theta2` or `conda install -c bioconda theta2`
- **Use Case**: Population genetics studies, genetic diversity assessment, demographic inference.

## Pitfalls

- **Sample Size**: Requires sufficient samples for accurate theta estimation.
- **Recombination**: ThetaL assumes no recombination - use appropriate model.

## Examples

### Calculate theta
**Args:** `theta2 -i snp_data.vcf -o theta_results.txt`
**Explanation:** Calculate theta statistics from SNP data.

### With population info
**Args:** `theta2 -v variants.vcf -p population_file.txt -o results/`
**Explanation:** Calculate population-specific theta values.
