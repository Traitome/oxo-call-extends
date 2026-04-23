---
name: nanocall
category: utility
description: An Oxford Nanopore Basecaller
tags: [nanocall, utility, nanopore, basecalling, signal]
author: oxo-call-community
source_url: "https://github.com/mateidavid/nanocall"
---

## Concepts

- **Tool Overview**: NanoCall v0.7.4 - Oxford Nanopore basecaller.
- **Core Function**: Basecalls Oxford Nanopore raw signal data to produce nucleotide sequences.
- **Input/Output**: Takes FAST5 signal files; outputs FASTQ basecalled reads.
- **Installation**: `conda install -c bioconda nanocall`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FAST5 files from Nanopore runs.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i fast5_dir -o output.fastq`
**Explanation:** Basecalls Nanopore FAST5 files to FASTQ.
