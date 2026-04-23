---
name: bactopia-variants
category: variant-calling
description: Methods used by Bactopia for SNP and InDel analysis
tags: [bactopia-variants, variant-calling]
author: oxo-call-community
source_url: "https://bactopia.github.io/"
---

## Concepts

- **Tool Overview**: bactopia-variants (v1.0.4) - Methods used by Bactopia for SNP and InDel analysis
- **Core Function**: Methods used by Bactopia for SNP and InDel analysis
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda bactopia-variants`

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
