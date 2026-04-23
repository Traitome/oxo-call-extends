---
name: chexalign
category: alignment
description: ChExAlign is used for alignment and quantification of ChIP-exo crosslinking patterns.
tags: [chexalign, alignment]
author: oxo-call-community
source_url: "https://github.com/seqcode/chexalign"
---

## Concepts

- **Tool Overview**: chexalign (v0.12) - ChExAlign is used for alignment and quantification of ChIP-exo crosslinking patterns.
- **Core Function**: ChExAlign is a computational framework that aligns ChIP-exo crosslinking patterns from multiple proteins across a set of regulatory regions, and which detects and quantifies protein-DNA crosslinking e...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda chexalign`

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
