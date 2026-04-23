---
name: leviosam2
category: alignment
description: Fast and accurate coordinate conversion between assemblies.
tags: [leviosam2, alignment]
author: oxo-call-community
source_url: "https://github.com/milkschen/leviosam2"
---

## Concepts

- **Tool Overview**: leviosam2 v0.5.0 - Fast and accurate coordinate conversion between assemblies..
- **Core Function**: Fast and accurate coordinate conversion between assemblies.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda leviosam2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Lift over alignments
**Args:** `leviosam2 lift -a aln.bam -c chain.txt -o lifted.bam`
**Explanation:** Lifts over BAM alignments using a chain file.

