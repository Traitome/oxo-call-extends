---
name: core-snp-filter
category: alignment
description: Filtering sites (i.e. columns) in a FASTA-format whole-genome pseudo-alignment.
tags: [core-snp-filter, alignment, FASTA]
author: oxo-call-community
source_url: "https://github.com/rrwick/Core-SNP-filter"
---

## Concepts

- **Tool Overview**: core-snp-filter (v0.2.0) - Filtering sites (i.e. columns) in a FASTA-format whole-genome pseudo-alignment.
- **Core Function**: Filtering sites (i.e. columns) in a FASTA-format whole-genome pseudo-alignment.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda core-snp-filter`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
