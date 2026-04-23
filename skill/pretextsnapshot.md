---
name: pretextsnapshot
category: alignment
description: Commandline image generator for Pretext Hi-C genome contact maps.
tags: ["pretextsnapshot", "alignment"]
author: oxo-call-community
source_url: "https://github.com/wtsi-hpag/PretextSnapshot"
---

## Concepts

- **Tool Overview**: Commandline image generator for Pretext Hi-C genome contact maps. (version 0.0.7)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pretextsnapshot`

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

