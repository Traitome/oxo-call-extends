---
name: reviewer
category: alignment
description: A tool for visualizing alignments of reads in regions containing tandem repeats
tags: ["reviewer", "alignment"]
author: oxo-call-community
source_url: "https://github.com/Illumina/REViewer"
---

## Concepts

- **Tool Overview**: A tool for visualizing alignments of reads in regions containing tandem repeats (version 0.2.7)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda reviewer`

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

