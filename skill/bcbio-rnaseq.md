---
name: bcbio-rnaseq
category: expression
description: Report generation for bcbio-nextgen RNA-seq runs
tags: [bcbio-rnaseq, expression]
author: oxo-call-community
source_url: "https://github.com/roryk/bcbio.rnaseq"
---

## Concepts

- **Tool Overview**: bcbio-rnaseq (v1.2.0) - Report generation for bcbio-nextgen RNA-seq runs
- **Core Function**: Report generation for bcbio-nextgen RNA-seq runs
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda bcbio-rnaseq`

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
