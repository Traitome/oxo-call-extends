---
name: rnacode
category: alignment
description: RNAcode - Analyze the protein coding potential in multiple sequence alignments RNAcode relies on evolutionary signatures including synonymous/conservative mutations and conservation of the reading frame. It does not use any species specific sequence characteristics whatsoever and does not use any machine learning techniques.
tags: ["rnacode", "alignment"]
author: oxo-call-community
source_url: "https://viennarna.github.io/RNAcode"
---

## Concepts

- **Tool Overview**: RNAcode - Analyze the protein coding potential in multiple sequence alignments RNAcode relies on evolutionary signatures including synonymous/conservative mutations and conservation of the reading frame. It does not use any species specific sequence characteristics whatsoever and does not use any machine learning techniques. (version 0.3.1)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rnacode`

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

