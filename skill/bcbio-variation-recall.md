---
name: bcbio-variation-recall
category: variant-calling
description: Parallel merging, squaring off and ensemble calling for genomic variants
tags: [bcbio-variation-recall, variant-calling]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbio.variation.recall"
---

## Concepts

- **Tool Overview**: bcbio-variation-recall (v0.2.6) - Parallel merging, squaring off and ensemble calling for genomic variants
- **Core Function**: Parallel merging, squaring off and ensemble calling for genomic variants
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda bcbio-variation-recall`

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
