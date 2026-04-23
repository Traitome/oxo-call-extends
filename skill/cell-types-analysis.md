---
name: cell-types-analysis
category: expression
description: A suite of scripts for analysis of scRNA-seq cell type classification tools outputs.
tags: [cell-types-analysis, expression]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/cell-types-analysis"
---

## Concepts

- **Tool Overview**: cell-types-analysis (v0.1.11) - A suite of scripts for analysis of scRNA-seq cell type classification tools outputs.
- **Core Function**: A suite of scripts for analysis of scRNA-seq cell type classification tools outputs.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cell-types-analysis`

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
