---
name: nanomod
category: epigenomics
description: A computational method for Nanopore signal analysis and modification detection.
tags: [nanomod, epigenomics, nanopore, modification, signal]
author: oxo-call-community
source_url: "https://github.com/WGLab/NanoMod"
---

## Concepts

- **Tool Overview**: NanoMod v0.2.2 - Nanopore signal analysis for modification detection.
- **Core Function**: Detects DNA/RNA modifications by analyzing Nanopore raw signal data.
- **Input/Output**: Takes FAST5 files and alignments; outputs modification sites.
- **Installation**: `conda install -c bioconda nanomod`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FAST5 signal files and alignment data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-f fast5_dir -b aligned.bam -r reference.fasta -o output_dir`
**Explanation:** Detects modifications from Nanopore signal data.
