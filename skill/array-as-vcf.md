---
name: array-as-vcf
category: variant-calling
description: Convert SNP array to VCF
tags: [array-as-vcf, variant-calling, VCF]
author: oxo-call-community
source_url: "https://github.com/LUMC/array-as-vcf"
---

## Concepts

- **Tool Overview**: array-as-vcf (v1.1.0) - Convert SNP array to VCF
- **Core Function**: Convert SNP array to VCF
- **Input/Output**: VCF variant input/output
- **Installation**: `conda install -c bioconda array-as-vcf`

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
