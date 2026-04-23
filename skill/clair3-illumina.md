---
name: clair3-illumina
category: variant-calling
description: Clair3 with libraries to support variant calling using Illumina short-reads. Version in sync with Clair3.
tags: [clair3-illumina, variant-calling]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/Clair3"
---

## Concepts

- **Tool Overview**: clair3-illumina (v2.0.0) - Clair3 with libraries to support variant calling using Illumina short-reads. Version in sync with Clair3.
- **Core Function**: Clair3 with libraries to support variant calling using Illumina short-reads. Version in sync with Clair3.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda clair3-illumina`

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
