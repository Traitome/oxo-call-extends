---
name: aquila_sv
category: variant-calling
description: Diploid assembly and variants calling tool
tags: [aquila_sv, variant-calling]
author: oxo-call-community
source_url: "https://github.com/maiziezhoulab/AquilaSV"
---

## Concepts

- **Tool Overview**: aquila_sv (v1.0) - Diploid assembly and variants calling tool
- **Core Function**: Diploid assembly and variants calling tool
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda aquila_sv`

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
