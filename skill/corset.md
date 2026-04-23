---
name: corset
category: expression
description: Software for clustering de novo assembled transcripts and counting overlapping reads.
tags: [corset, expression]
author: oxo-call-community
source_url: "https://github.com/Oshlack/Corset/wiki"
---

## Concepts

- **Tool Overview**: corset (v1.09) - Software for clustering de novo assembled transcripts and counting overlapping reads.
- **Core Function**: Software for clustering de novo assembled transcripts and counting overlapping reads.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda corset`

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
