---
name: bis-snp-utils
category: variant-calling
description: bis-snp-utils are support tools for Bis-SNP
tags: [bis-snp-utils, variant-calling]
author: oxo-call-community
source_url: "http://people.csail.mit.edu/dnaase/bissnp2011/"
---

## Concepts

- **Tool Overview**: bis-snp-utils (v0.0.1) - bis-snp-utils are support tools for Bis-SNP
- **Core Function**: bis-snp-utils are support tools for Bis-SNP
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda bis-snp-utils`

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
