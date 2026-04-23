---
name: cutefc
category: variant-calling
description: Regenotyping structural variants through an accurate and efficient force-calling method
tags: [cutefc, variant-calling]
author: oxo-call-community
source_url: "https://github.com/Meltpinkg/cuteFC"
---

## Concepts

- **Tool Overview**: cutefc (v1.0.2) - Regenotyping structural variants through an accurate and efficient force-calling method
- **Core Function**: Regenotyping structural variants through an accurate and efficient force-calling method
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cutefc`

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
