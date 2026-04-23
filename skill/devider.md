---
name: devider
category: variant-calling
description: Haplotyping small sequences from heterogeneous long-read sequencing samples with SNP-encoded positional de Bruijn graphs.
tags: [devider, variant-calling, haplotyping, long-read, de-bruijn]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/devider"
---

## Concepts

- **Tool Overview**: devider v0.0.1 - Haplotyping tool for heterogeneous samples using SNP-encoded positional de Bruijn graphs.
- **Core Function**: Reconstructs haplotypes from mixed long-read sequencing data using positional de Bruijn graph approach.
- **Input/Output**: Expects long reads and variant sites; outputs haplotype-resolved sequences.
- **Installation**: `conda install -c bioconda devider`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires long reads with sufficient coverage for haplotype resolution.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `devider --reads reads.fq --variants variants.vcf --output haplotypes/`
**Explanation:** Reconstructs haplotypes from heterogeneous long-read data.
