---
name: progressivemauve
category: alignment
description: progressiveMauve computes multiple genome alignment with gene gain, loss and rearrangement
tags: ["progressivemauve", "alignment"]
author: oxo-call-community
source_url: "http://darlinglab.org/mauve/user-guide/progressivemauve.html"
---

## Concepts

- **Tool Overview**: progressiveMauve computes multiple genome alignment with gene gain, loss and rearrangement (version snapshot_2015_02_13)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda progressivemauve`

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

