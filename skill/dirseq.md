---
name: dirseq
category: expression
description: Work out whether RNAseq reads agree with the direction of the gene predicted.
tags: [dirseq, expression, rna-seq, strand, gene-direction]
author: oxo-call-community
source_url: "https://github.com/wwood/dirseq"
---

## Concepts

- **Tool Overview**: dirseq v0.4.3 - Tool for checking if RNA-seq reads agree with predicted gene direction.
- **Core Function**: Verifies strand specificity of RNA-seq data by comparing read orientation with gene annotations.
- **Input/Output**: Expects BAM files and GFF annotations; outputs direction agreement statistics.
- **Installation**: `conda install -c bioconda dirseq`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires aligned BAM and gene annotation files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dirseq --bam sample.bam --gff genes.gff --output dir_stats.tsv`
**Explanation:** Checks read direction agreement with gene predictions.
