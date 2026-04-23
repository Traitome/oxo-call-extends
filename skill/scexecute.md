---
name: scexecute
category: alignment
description: SCExecute generates cell-barcode specific BAM files from aligned, aggregate single-cell sequencing data, executing a user-provided command on each barcode-stratified BAM file.
tags: ["scexecute", "alignment", "bam", "bam"]
author: oxo-call-community
source_url: "https://horvathlab.github.io/NGS/SCExecute"
---

## Concepts

- **Tool Overview**: SCExecute generates cell-barcode specific BAM files from aligned, aggregate single-cell sequencing data, executing a user-provided command on each barcode-stratified BAM file. (version 1.3.3)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda scexecute`

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

