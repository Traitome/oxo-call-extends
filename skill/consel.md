---
name: consel
category: utility
description: Assess confidence in model selection using p-values
tags: [consel, statistical-testing, model-selection, p-value, bioinformatics]
author: oxo-call-community
source_url: "https://stat.sys.i.kyoto-u.ac.jp/prog/consel"
---

## Concepts

- **Tool Overview**: CONSEL is a statistical tool for calculating p-values to assess confidence in model selection problems, commonly used in phylogenetic tree selection.
- **Core Function**: Computes approximately unbiased (AU) p-values and other confidence measures for comparing competing models or hypotheses.
- **Algorithm**: Uses multiscale bootstrap resampling to compute AU p-values, bootstrap probabilities, and other confidence measures.
- **Input**: Log-likelihood values for competing models across multiple datasets or sites.
- **Output**: P-values (AU, BP, NP), confidence intervals, and selection probabilities.
- **Application**: Phylogenetic tree selection, model comparison, and hypothesis testing.
- **Installation**: Install via bioconda: `conda install -c bioconda consel`

## Pitfalls

- **Sample Size**: Requires sufficient bootstrap replicates for accurate p-values.
- **Model Number**: Too many models increase multiple testing burden.
- **Likelihood Quality**: Results depend on accurate log-likelihood calculations.
- **Interpretation**: AU p-values differ from standard bootstrap probabilities.
- **Computational Cost**: Bootstrap resampling can be computationally intensive.

## Examples

### Calculate p-values from likelihoods
**Args:** `consel likelihood.txt`
**Explanation:** Calculates p-values from site-wise log-likelihoods.

### Run bootstrap analysis
**Args:** `catpv bootstrap.txt > results.txt`
**Explanation:** Processes bootstrap replicates to generate p-values.

### Generate confidence summary
**Args:** `makermt input.txt > output.rmt && consel output.rmt`
**Explanation:** Creates RMT file and runs CONSEL analysis.

### Display help
**Args:** `consel --help`
**Explanation:** Shows all available options and usage information.