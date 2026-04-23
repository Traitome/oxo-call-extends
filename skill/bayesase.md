---
name: bayesase
category: variant-calling
description: Bayesian analysis of allele specific expression
tags: [bayesase, variant-calling, SAM, BED]
author: oxo-call-community
source_url: "https://github.com/McIntyre-Lab/BayesASE"
---

## Concepts

- **Tool Overview**: bayesase (v21.1.13.1) - Bayesian analysis of allele specific expression
- **Core Function**: Allelic imbalance (AI) indicates the presence of functional variation in cis regulatory regions. Detecting cis regulatory differences using AI is widespread, yet there is no formal statistical methodo...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda bayesase`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
