---
name: nanocount
category: expression
description: Transcript abundance estimation from Nanopore direct-RNA sequencing datasets
tags: [nanocount, expression, nanopore, transcript-abundance, direct-rna]
author: oxo-call-community
source_url: "https://github.com/a-slide/NanoCount/"
---

## Concepts

- **Tool Overview**: NanoCount v1.0.0 - transcript abundance estimation from Nanopore direct-RNA sequencing.
- **Core Function**: Estimates transcript abundance using expectation-maximization approach for multi-mapping reads.
- **Input/Output**: Takes aligned BAM from direct RNA-Seq; outputs transcript abundance estimates.
- **Installation**: `conda install -c bioconda nanocount`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires BAM aligned to transcriptome.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -o abundance.tsv`
**Explanation:** Estimates transcript abundance from direct RNA-Seq alignments.
