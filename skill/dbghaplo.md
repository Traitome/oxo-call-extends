---
name: dbghaplo
category: variant-calling
description: Haplotyping small sequences from heterogeneous long-read sequencing samples with a SNP-encoded positional de Bruijn Graph.
tags: [dbghaplo, variant-calling, SAM]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/dbghaplo"
---

## Concepts

- **Tool Overview**: dbghaplo (v0.0.2) - Haplotyping small sequences from heterogeneous long-read sequencing samples with a SNP-encoded positional de Bruijn Graph.
- **Core Function**: Haplotyping small sequences from heterogeneous long-read sequencing samples with a SNP-encoded positional de Bruijn Graph.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda dbghaplo`

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
