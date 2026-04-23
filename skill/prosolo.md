---
name: prosolo
category: variant-calling
description: A highly sensitive and accurate Bayesian caller for variants in single cell sequencing data.
tags: ["prosolo", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/prosolo/prosolo/tree/v0.6.1"
---

## Concepts

- **Tool Overview**: A highly sensitive and accurate Bayesian caller for variants in single cell sequencing data. (version 0.6.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda prosolo`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Call variants
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Identifies variants from aligned reads.

