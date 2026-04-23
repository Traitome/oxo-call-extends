---
name: ldsc
category: population-genomics
description: ldsc is a tool for estimating heritability and genetic correlation from GWAS summary statistics. It also computes LD Scores.
tags: [ldsc, population-genomics]
author: oxo-call-community
source_url: "https://github.com/bulik/ldsc/"
---

## Concepts

- **Tool Overview**: ldsc v1.0.1 - ldsc is a tool for estimating heritability and genetic correlation from GWAS summary statistics. It also computes LD Scores..
- **Core Function**: ldsc is a tool for estimating heritability and genetic correlation from GWAS summary statistics. It also computes LD Scores.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda ldsc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Calculate LD scores
**Args:** `ldsc.py --l2 --bfile reference --ld-wind-cm 1 --out ld_scores`
**Explanation:** Calculates LD scores from reference panel.

