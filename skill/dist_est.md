---
name: dist_est
category: population-genomics
description: Estimation of Rates-Across-Sites Distributions in Phylogenetic Substitution Models.
tags: [dist_est, population-genomics, phylogenetics, rates-across-sites]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: dist_est v1.1 - Tool for estimating rates-across-sites distributions in phylogenetic models.
- **Core Function**: Estimates the distribution of substitution rates across sites in phylogenetic analyses.
- **Input/Output**: Expects multiple sequence alignments; outputs rate distribution parameters.
- **Installation**: `conda install -c bioconda dist_est`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires aligned sequences.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dist_est --alignment sequences.fa --output rates.txt`
**Explanation:** Estimates rate distribution across sites.
