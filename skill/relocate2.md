---
name: relocate2
category: alignment
description: a high resolution transposable element insertion sites mapping tool for population resequencing
tags: ["relocate2", "alignment"]
author: oxo-call-community
source_url: "https://github.com/stajichlab/RelocaTE2"
---

## Concepts

- **Tool Overview**: a high resolution transposable element insertion sites mapping tool for population resequencing (version 2.0.1)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda relocate2`

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

