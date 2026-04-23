---
name: raiss
category: variant-calling
description: SNP summary statistics imputation package
tags: ["raiss", "variant-calling"]
author: oxo-call-community
source_url: "http://statistical-genetics.pages.pasteur.fr/raiss/"
---

## Concepts

- **Tool Overview**: SNP summary statistics imputation package (version 4.0.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda raiss`

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

