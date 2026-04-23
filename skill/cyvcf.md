---
name: cyvcf
category: variant-calling
description: A cython wrapper around htslib built for fast parsing of Variant Call Format (VCF) files
tags: [cyvcf, variant-calling, VCF]
author: oxo-call-community
source_url: "https://github.com/brentp/cyvcf2"
---

## Concepts

- **Tool Overview**: cyvcf (v0.8.0) - A cython wrapper around htslib built for fast parsing of Variant Call Format (VCF) files
- **Core Function**: A cython wrapper around htslib built for fast parsing of Variant Call Format (VCF) files
- **Input/Output**: VCF variant input/output
- **Installation**: `conda install -c bioconda cyvcf`

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
