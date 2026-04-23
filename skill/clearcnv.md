---
name: clearcnv
category: variant-calling
description: CNV calling package
tags: [clearcnv, variant-calling]
author: oxo-call-community
source_url: "https://github.com/bihealth/clear-cnv"
---

## Concepts

- **Tool Overview**: clearcnv (v0.306) - CNV calling package
- **Core Function**: CNV calling package
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda clearcnv`

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
