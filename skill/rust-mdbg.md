---
name: rust-mdbg
category: assembly
description: An ultra-fast minimizer-space de Bruijn graph (mdBG) implementation, geared towards the assembly of long and accurate reads.
tags: ["rust-mdbg", "assembly"]
author: oxo-call-community
source_url: "https://github.com/ekimb/rust-mdbg"
---

## Concepts

- **Tool Overview**: An ultra-fast minimizer-space de Bruijn graph (mdBG) implementation, geared towards the assembly of long and accurate reads. (version 1.0.1)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rust-mdbg`

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

