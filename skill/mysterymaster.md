---
name: mysterymaster
category: utility
description: Graphical Oxford Nanopore read demultiplexer
tags: [mysterymaster, utility, nanopore, demultiplexing, barcoding]
author: oxo-call-community
source_url: "https://bitbucket.org/NPC239/mysterymaster/src/main/"
---

## Concepts

- **Tool Overview**: MysteryMaster v0.0.8 - graphical Oxford Nanopore read demultiplexer.
- **Core Function**: Demultiplexes Oxford Nanopore reads by barcode with a graphical interface.
- **Input/Output**: Takes FASTQ files from Nanopore runs; outputs demultiplexed reads by barcode.
- **Installation**: `conda install -c bioconda mysterymaster`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure reads contain barcode information.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir`
**Explanation:** Demultiplexes Nanopore reads by barcode.
