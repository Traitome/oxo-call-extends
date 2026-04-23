---
name: astalavista
category: expression
description: AStalavista is a computer program to extract alternative splicing (AS) events from a given genomic annotation of exon-intron gene coordinates. By comparing all given transcripts, AStalavista detects the variations in their splicing structure and identify all AS events (like exon skipping, alternate donor, etc) by assigning to each of them an AS code.
tags: [astalavista, expression]
author: oxo-call-community
source_url: "http://sammeth.net/confluence/display/ASTA/Home"
---

## Concepts

- **Tool Overview**: astalavista (v4.0) - AStalavista is a computer program to extract alternative splicing (AS) events from a given genomic annotation of exon-intron gene coordinates. By comparing all given transcripts, AStalavista detects the variations in their splicing structure and identify all AS events (like exon skipping, alternate donor, etc) by assigning to each of them an AS code.
- **Core Function**: AStalavista is a computer program to extract alternative splicing (AS) events from a given genomic annotation of exon-intron gene coordinates. By comparing all given transcripts, AStalavista detects the variations in their splicing structure and identify all AS events (like exon skipping, alternate donor, etc) by assigning to each of them an AS code.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda astalavista`

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
