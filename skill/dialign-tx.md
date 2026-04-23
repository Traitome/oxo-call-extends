---
name: dialign-tx
category: alignment
description: DIALIGN-TX - greedy and progressive approaches for segment-based multiple sequence alignment.
tags: [dialign-tx, alignment, multiple-sequence, segment-based]
author: oxo-call-community
source_url: "https://dialign.gobics.de"
---

## Concepts

- **Tool Overview**: DIALIGN-TX v1.0.2 - Segment-based multiple sequence alignment tool using greedy and progressive approaches.
- **Core Function**: Aligns sequences based on segment-to-segment comparisons rather than single residues.
- **Input/Output**: Expects FASTA sequences; outputs multiple sequence alignments.
- **Installation**: `conda install -c bioconda dialign-tx`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dialign-tx -fa input.fa -out aligned.fa`
**Explanation:** Performs segment-based multiple sequence alignment.
