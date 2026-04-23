---
name: deploid
category: variant-calling
description: A software that deconvolutes mixed genomes with unknown proportions.
tags: [deploid, variant-calling, deconvolution, mixed-infection, malaria]
author: oxo-call-community
source_url: "http://deploid.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Tool Overview**: DEploid v0.5 - Tool for deconvoluting mixed genome samples with unknown proportions, commonly used for malaria parasite infections.
- **Core Function**: Infers individual strain haplotypes and proportions from mixed sequencing data.
- **Input/Output**: Expects VCF files; outputs strain haplotypes and proportions.
- **Installation**: `conda install -c bioconda deploid`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires VCF with sufficient SNP coverage for strain separation.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deploid --vcf sample.vcf --ref ref.fa --output results/`
**Explanation:** Deconvolutes mixed genome sample into component strains.
