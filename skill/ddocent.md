---
name: ddocent
category: variant-calling
description: dDocent is an interactive bash wrapper to QC, assemble, map, and call SNPs from all types of RAD data
tags: [ddocent, variant-calling]
author: oxo-call-community
source_url: "https://www.ddocent.com/UserGuide/"
---

## Concepts

- **Tool Overview**: ddocent (v2.9.8) - dDocent is an interactive bash wrapper to QC, assemble, map, and call SNPs from all types of RAD data
- **Core Function**: dDocent is an interactive bash wrapper to QC, assemble, map, and call SNPs from all types of RAD data
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ddocent`

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
