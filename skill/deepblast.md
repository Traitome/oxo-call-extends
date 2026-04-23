---
name: deepblast
category: alignment
description: Neural Networks for Protein Sequence Alignment.
tags: [deepblast, alignment]
author: oxo-call-community
source_url: "https://github.com/flatironinstitute/deepblast"
---

## Concepts

- **Tool Overview**: deepblast (v1.0.2) - Neural Networks for Protein Sequence Alignment.
- **Core Function**: Neural Networks for Protein Sequence Alignment.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda deepblast`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
