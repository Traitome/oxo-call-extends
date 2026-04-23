---
name: pyeasyfuse
category: alignment
description: EasyFuse is a pipeline to detect fusion transcripts from RNA-seq data with high accuracy. The current version of EasyFuse uses two fusion gene detection tools, STAR-Fusion and Fusioncatcher along with a powerful read filtering strategy, stringent re-quantification of supporting reads and machine learning for highly accurate predictions.
tags: ["pyeasyfuse", "alignment"]
author: oxo-call-community
source_url: "https://github.com/TRON-Bioinformatics/EasyFuse"
---

## Concepts

- **Tool Overview**: EasyFuse is a pipeline to detect fusion transcripts from RNA-seq data with high accuracy. The current version of EasyFuse uses two fusion gene detection tools, STAR-Fusion and Fusioncatcher along with a powerful read filtering strategy, stringent re-quantification of supporting reads and machine learning for highly accurate predictions. (version 2.0.3)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pyeasyfuse`

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

