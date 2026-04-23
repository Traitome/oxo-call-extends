---
name: chewbbaca
category: variant-calling
description: A complete suite for gene-by-gene schema creation and strain identification.
tags: [chewbbaca, variant-calling]
author: oxo-call-community
source_url: "https://chewbbaca.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Tool Overview**: chewbbaca (v3.5.3) - A complete suite for gene-by-gene schema creation and strain identification.
- **Core Function**: chewBBACA is a comprehensive pipeline including a set of functions for the creation and validation of whole genome and core genome MultiLocus Sequence Typing (wg/cgMLST) schemas, providing an allele c...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda chewbbaca`

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
