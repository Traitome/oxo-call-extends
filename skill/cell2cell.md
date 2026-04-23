---
name: cell2cell
category: expression
description: Inferring cell-cell interactions from transcriptomes with cell2cell.
tags: [cell2cell, expression]
author: oxo-call-community
source_url: "https://github.com/earmingol/cell2cell"
---

## Concepts

- **Tool Overview**: cell2cell (v0.8.4) - Inferring cell-cell interactions from transcriptomes with cell2cell.
- **Core Function**: Inferring cell-cell interactions from transcriptomes with cell2cell.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cell2cell`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
