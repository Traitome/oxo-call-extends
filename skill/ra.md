---
name: ra
category: alignment
description: Ra is short for RNA Assembler and it is a C++ implementation of an overlap-layout-consensus transcriptome assembler.
tags: ["ra", "alignment"]
author: oxo-call-community
source_url: "https://github.com/mariokostelac/ra"
---

## Concepts

- **Tool Overview**: Ra is short for RNA Assembler and it is a C++ implementation of an overlap-layout-consensus transcriptome assembler. (version 0.9)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ra`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

