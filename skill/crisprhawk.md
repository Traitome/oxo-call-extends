---
name: crisprhawk
category: variant-calling
description: CRISPR-HAWK: Haplotype and vAriant-aWare guide design toolKit
tags: [crisprhawk, variant-calling]
author: oxo-call-community
source_url: "https://github.com/pinellolab/CRISPR-HAWK"
---

## Concepts

- **Tool Overview**: crisprhawk (v0.1.2) - CRISPR-HAWK: Haplotype and vAriant-aWare guide design toolKit
- **Core Function**: CRISPR-HAWK: Haplotype and vAriant-aWare guide design toolKit
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda crisprhawk`

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
