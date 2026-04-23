---
name: nanoraw
category: epigenomics
description: Analysis of nanopore sequencing data.
tags: [nanoraw, epigenomics, nanopore, signal, analysis]
author: oxo-call-community
source_url: "https://github.com/marcus1487/nanoraw"
---

## Concepts

- **Tool Overview**: NanoRaw v0.5 - analysis tool for Nanopore sequencing data.
- **Core Function**: Analyzes raw Nanopore signal data for modification detection and other analyses.
- **Input/Output**: Takes FAST5 and alignment data; outputs analysis results.
- **Installation**: `conda install -c bioconda nanoraw`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FAST5 signal files and alignment data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-f fast5_dir -b aligned.bam -r reference.fasta -o output_dir`
**Explanation:** Analyzes Nanopore raw signal data.
