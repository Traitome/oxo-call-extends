---
name: pypgatk
category: variant-calling
description: The Pypgatk framework and library provides a set of tools to perform ProteoGenomics Analysis.
tags: ["pypgatk", "variant-calling"]
author: oxo-call-community
source_url: "https://pgatk.readthedocs.io/en/latest/pypgatk.html"
---

## Concepts

- **Tool Overview**: The Pypgatk framework and library provides a set of tools to perform ProteoGenomics Analysis. (version 0.0.24)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pypgatk`

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

