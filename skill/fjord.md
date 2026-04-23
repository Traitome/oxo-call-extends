---
name: fjord
category: hpc
description: ONT amplicon sequencing pipeline for bacterial identification
tags: [fjord, hpc]
author: oxo-call-community
source_url: "https://github.com/adnsvrtsn/fjord"
---

## Concepts
- **Tool Overview**: FJORD (Flexible Joint Operational pipeline for Reference-based Diagnostics) is an amplicon sequencing pipeline for bacterial identification from Oxford Nanopore Technologies long-read data. It maps reads to a GTDB-formatted reference database, generates consensus sequences, clusters similar sequences with IUPAC-aware consolidation, and assigns taxonomy via BLAST.
- **Core Function**: ONT amplicon sequencing pipeline for bacterial identification
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda fjord`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
