---
name: rnaalishapes
category: alignment
description: RNAalishapes is a tool for secondary structure prediction, using shape abstraction. Input is a multiple sequence alignment. Pseudoknots are not considered at all.
tags: ["rnaalishapes", "alignment"]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/rnaalishapes"
---

## Concepts

- **Tool Overview**: RNAalishapes is a tool for secondary structure prediction, using shape abstraction. Input is a multiple sequence alignment. Pseudoknots are not considered at all. (version 2.5.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rnaalishapes`

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

