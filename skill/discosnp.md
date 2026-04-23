---
name: discosnp
category: variant-calling
description: DiscoSnp - SNP discovery from read sets without reference genome.
tags: [discosnp, variant-calling, snp, reference-free, de-bruijn]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DiscoSnp - Reference-free SNP discovery tool using de Bruijn graph approach.
- **Core Function**: Discovers SNPs directly from read sets without requiring a reference genome.
- **Input/Output**: Expects FASTQ read files; outputs SNP predictions.
- **Installation**: `conda install -c bioconda discosnp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires multiple read sets for comparative SNP discovery.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `discosnp run --reads sample1.fq sample2.fq --output snps.vcf`
**Explanation:** Discovers SNPs between read sets without reference.
