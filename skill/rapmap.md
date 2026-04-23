---
name: rapmap
category: alignment
description: Rapid sensitive and accurate read mapping via quasi-mapping
tags: ["rapmap", "alignment"]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/RapMap"
---

## Concepts

- **Tool Overview**: Rapid sensitive and accurate read mapping via quasi-mapping (version 0.6.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rapmap`

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

