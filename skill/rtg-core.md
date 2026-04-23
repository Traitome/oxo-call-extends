---
name: rtg-core
category: alignment
description: RealTimeGenomics Core -- Software for alignment and analysis of next-gen sequencing data.
tags: ["rtg-core", "alignment"]
author: oxo-call-community
source_url: "https://realtimegenomics.github.io/rtg-core/index.html"
---

## Concepts

- **Tool Overview**: RealTimeGenomics Core -- Software for alignment and analysis of next-gen sequencing data. (version 3.13)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rtg-core`

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

