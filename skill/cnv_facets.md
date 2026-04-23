---
name: cnv_facets
category: variant-calling
description: Detect somatic copy number variants (CNV) in tumour-normal samples using next generation sequencing data
tags: [cnv_facets, variant-calling, SAM]
author: oxo-call-community
source_url: "https://github.com/dariober/cnv_facets"
---

## Concepts

- **Tool Overview**: cnv_facets (v0.16.1) - Detect somatic copy number variants (CNV) in tumour-normal samples using next generation sequencing data
- **Core Function**: Detect somatic copy number variants (CNV) in tumour-normal samples using next generation sequencing data
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda cnv_facets`

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
