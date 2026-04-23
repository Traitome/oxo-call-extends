---
name: aquilasv
category: variant-calling
description: A region-based diploid assembly and variants calling tool
tags: [aquilasv, variant-calling]
author: oxo-call-community
source_url: "https://github.com/maiziezhoulab/AquilaSV"
---

## Concepts

- **Tool Overview**: aquilasv (v1.5) - A region-based diploid assembly and variants calling tool
- **Core Function**: A region-based diploid assembly and variants calling tool
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda aquilasv`

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
