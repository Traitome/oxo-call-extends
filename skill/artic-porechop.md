---
name: artic-porechop
category: qc
description: Adapter removal and demultiplexing of Oxford Nanopore reads (fork of rrwick/Porechop)
tags: [artic-porechop, qc]
author: oxo-call-community
source_url: "https://github.com/artic-network/Porechop"
---

## Concepts

- **Tool Overview**: artic-porechop (v0.3.2pre) - Adapter removal and demultiplexing of Oxford Nanopore reads (fork of rrwick/Porechop)
- **Core Function**: Adapter removal and demultiplexing of Oxford Nanopore reads (fork of rrwick/Porechop)
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda artic-porechop`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
