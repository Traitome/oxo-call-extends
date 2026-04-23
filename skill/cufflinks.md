---
name: cufflinks
category: expression
description: Transcriptome assembly and differential expression analysis for RNA-Seq.
tags: [cufflinks, expression]
author: oxo-call-community
source_url: "http://cole-trapnell-lab.github.io/cufflinks/"
---

## Concepts

- **Tool Overview**: cufflinks (v2.2.1) - Transcriptome assembly and differential expression analysis for RNA-Seq.
- **Core Function**: Transcriptome assembly and differential expression analysis for RNA-Seq.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cufflinks`

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
