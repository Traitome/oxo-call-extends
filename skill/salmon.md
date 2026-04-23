---
name: salmon
category: alignment
description: Highly-accurate & wicked fast transcript-level quantification from RNA-seq reads using selective alignment.
tags: ["salmon", "alignment"]
author: oxo-call-community
source_url: "https://combine-lab.github.io/salmon"
---

## Concepts

- **Tool Overview**: Highly-accurate & wicked fast transcript-level quantification from RNA-seq reads using selective alignment. (version 1.11.4)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda salmon`

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

