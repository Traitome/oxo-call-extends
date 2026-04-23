---
name: dinf
category: population-genomics
description: Dinf - demographic inference from population genomic data.
tags: [dinf, population-genomics, demographic-inference, simulation]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: dinf - Tool for demographic inference from population genomic data using simulation-based approaches.
- **Core Function**: Infers demographic parameters from population genomic data using generative models.
- **Input/Output**: Expects VCF/FASTA population data; outputs inferred demographic parameters.
- **Installation**: `conda install -c bioconda dinf`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires population genomic variant data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dinf --vcf population.vcf --model demography.yaml --output params.tsv`
**Explanation:** Infers demographic parameters from population data.
