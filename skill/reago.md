---
name: reago
category: assembly
description: An assembly tool for 16S ribosomal RNA recovery from metagenomic data
tags: ["reago", "assembly"]
author: oxo-call-community
source_url: "https://github.com/chengyuan/reago-1.1"
---

## Concepts

- **Tool Overview**: An assembly tool for 16S ribosomal RNA recovery from metagenomic data (version 1.1)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda reago`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Run assembly
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assembles reads into contigs/scaffolds.

