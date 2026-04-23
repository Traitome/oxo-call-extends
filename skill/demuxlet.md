---
name: demuxlet
category: expression
description: Genetic multiplexing of barcoded single cell RNA-seq.
tags: [demuxlet, expression, single-cell, demultiplexing, rna-seq]
author: oxo-call-community
source_url: "https://github.com/statgen/demuxlet"
---

## Concepts

- **Tool Overview**: demuxlet v1.0 - Tool for genetically demultiplexing pooled single-cell RNA-seq samples using natural genetic variation.
- **Core Function**: Assigns single cells to individual donors in pooled scRNA-seq experiments using SNP genotypes.
- **Input/Output**: Expects BAM/VCF from scRNA-seq and donor genotype VCF; outputs cell-to-donor assignments.
- **Installation**: `conda install -c bioconda demuxlet`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires both scRNA-seq data and donor genotype information.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `demuxlet --plink genotypes --vcf pool.vcf --out assignments`
**Explanation:** Demultiplexes pooled scRNA-seq using genetic variation.
