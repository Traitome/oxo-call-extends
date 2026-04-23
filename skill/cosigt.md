---
name: cosigt
category: variant-calling
description: Cosigt (COsine SImilarity-based GenoTyper)
tags: [cosigt, variant-calling]
author: oxo-call-community
source_url: "https://github.com/davidebolo1993/cosigt"
---

## Concepts

- **Tool Overview**: cosigt (v0.1.7) - Cosigt (COsine SImilarity-based GenoTyper)
- **Core Function**: Cosigt (COsine SImilarity-based GenoTyper)
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cosigt`

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
