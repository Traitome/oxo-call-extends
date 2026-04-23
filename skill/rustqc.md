---
name: rustqc
category: alignment
description: RNA-seq quality control suite: dupRadar, featureCounts, RSeQC, preseq, samtools stats, and Qualimap in one pass
tags: ["rustqc", "alignment", "sam"]
author: oxo-call-community
source_url: "https://seqeralabs.github.io/RustQC/"
---

## Concepts

- **Tool Overview**: RNA-seq quality control suite: dupRadar, featureCounts, RSeQC, preseq, samtools stats, and Qualimap in one pass (version 0.2.1)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rustqc`

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

