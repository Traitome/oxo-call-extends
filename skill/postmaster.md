---
name: postmaster
category: alignment
description: Postmaster is a tool for annotating transcriptome alignments with posterior alignment probabilities derived from salmon quantifications.
tags: ["postmaster", "alignment"]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/postmaster"
---

## Concepts

- **Tool Overview**: Postmaster is a tool for annotating transcriptome alignments with posterior alignment probabilities derived from salmon quantifications. (version 0.1.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda postmaster`

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

