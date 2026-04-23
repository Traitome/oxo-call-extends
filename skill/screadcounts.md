---
name: screadcounts
category: expression
description: SCReadCounts is a computational tool for a cell-level assessment of the read counts bearing a particular nucleotide at genomic positions of interest from single cell RNA sequencing (scRNA-seq) data.
tags: [screadcounts, expression]
author: oxo-call-community
source_url: "https://horvathlab.github.io/NGS/SCReadCounts"
---

## Concepts

- **Tool Overview**: screadcounts (v1.4.2) - SCReadCounts is a computational tool for a cell-level assessment of the read counts bearing a particular nucleotide at genomic positions of interest from single cell RNA sequencing (scRNA-seq) data.
- **Core Function**: SCReadCounts is a computational tool for a cell-level assessment of the read counts bearing a particular nucleotide at genomic positions of interest from single cell RNA sequencing (scRNA-seq) data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda screadcounts`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `screadcounts -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run screadcounts with typical input and output options.
