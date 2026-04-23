---
name: sciphi
category: variant-calling
description: Single-cell mutation identification via phylogenetic inference
tags: ["sciphi", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/SCIPhI"
---

## Concepts

- **Tool Overview**: Single-cell mutation identification via phylogenetic inference (version 0.1.7)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sciphi`

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

