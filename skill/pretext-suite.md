---
name: pretext-suite
category: alignment
description: Meta-package for Pretext Hi-C contact map tools.
tags: ["pretext-suite", "alignment"]
author: oxo-call-community
source_url: "https://github.com/wtsi-hpag/"
---

## Concepts

- **Tool Overview**: Meta-package for Pretext Hi-C contact map tools. (version 0.0.2)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pretext-suite`

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

