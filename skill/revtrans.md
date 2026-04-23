---
name: revtrans
category: alignment
description: revtrans - performs a reverse translation of a peptide alignment.
tags: ["revtrans", "alignment"]
author: oxo-call-community
source_url: "http://www.cbs.dtu.dk/services/RevTrans-2.0/web/download.php"
---

## Concepts

- **Tool Overview**: revtrans - performs a reverse translation of a peptide alignment. (version 1.4)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda revtrans`

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

