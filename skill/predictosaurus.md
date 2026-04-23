---
name: predictosaurus
category: variant-calling
description: Predictosaurus is a command-line tool designed for uncertainty-aware haplotype-based genomic variant effect prediction.
tags: ["predictosaurus", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/fxwiegand/predictosaurus/blob/v0.10.2/README.md"
---

## Concepts

- **Tool Overview**: Predictosaurus is a command-line tool designed for uncertainty-aware haplotype-based genomic variant effect prediction. (version 0.10.2)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda predictosaurus`

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

