---
name: cellxgene
category: expression
description: Web application for exploration of large scale scRNA-seq datasets
tags: [cellxgene, expression]
author: oxo-call-community
source_url: "https://github.com/chanzuckerberg/cellxgene"
---

## Concepts

- **Tool Overview**: cellxgene (v1.3.0) - Web application for exploration of large scale scRNA-seq datasets
- **Core Function**: Web application for exploration of large scale scRNA-seq datasets
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cellxgene`

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
