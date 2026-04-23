---
name: nanoplexer
category: utility
description: Tool for demultiplexing Nanopore barcode sequence data
tags: [nanoplexer, utility, nanopore, demultiplexing, barcoding]
author: oxo-call-community
source_url: "https://github.com/hanyue36/nanoplexer"
---

## Concepts

- **Tool Overview**: NanoPlexer v0.1.2 - demultiplexing tool for Nanopore barcode data.
- **Core Function**: Separates Nanopore reads by barcode sequences for multiplexed runs.
- **Input/Output**: Takes FASTQ files; outputs demultiplexed FASTQ files by barcode.
- **Installation**: `conda install -c bioconda nanoplexer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires barcoded Nanopore reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir`
**Explanation:** Demultiplexes Nanopore reads by barcode.
