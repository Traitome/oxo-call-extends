---
name: primers
category: assembly
description: This is a small, straightforward tool for creating PCR primers. Its target use-case is DNA assembly.
tags: ["primers", "assembly"]
author: oxo-call-community
source_url: "https://github.com/Lattice-Automation/primers"
---

## Concepts

- **Tool Overview**: This is a small, straightforward tool for creating PCR primers. Its target use-case is DNA assembly. (version 0.5.10)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda primers`

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

