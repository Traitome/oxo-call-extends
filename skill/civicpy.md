---
name: civicpy
category: variant-calling
description: CIViC variant knowledgebase analysis toolkit.
tags: [civicpy, variant-calling]
author: oxo-call-community
source_url: "https://docs.civicpy.org/en/latest"
---

## Concepts

- **Tool Overview**: civicpy (v5.3.0) - CIViC variant knowledgebase analysis toolkit.
- **Core Function**: CIViC variant knowledgebase analysis toolkit.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda civicpy`

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
