---
name: salmid
category: alignment
description: Rapid tool to check taxonomic ID of single isolate samples. Currently only IDs Salmonella species and subspecies, and some common contaminants (Listeria, Escherichia).
tags: ["salmid", "alignment", "sam"]
author: oxo-call-community
source_url: "https://github.com/hcdenbakker/SalmID"
---

## Concepts

- **Tool Overview**: Rapid tool to check taxonomic ID of single isolate samples. Currently only IDs Salmonella species and subspecies, and some common contaminants (Listeria, Escherichia). (version 0.1.23)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda salmid`

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

