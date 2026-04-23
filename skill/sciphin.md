---
name: sciphin
category: variant-calling
description: Single-Cell mutation Identification via finite-sites Phylogenetic Inference
tags: ["sciphin", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/SCIPhI"
---

## Concepts

- **Tool Overview**: Single-Cell mutation Identification via finite-sites Phylogenetic Inference (version 1.0.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sciphin`

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

