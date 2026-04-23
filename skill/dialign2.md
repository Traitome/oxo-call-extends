---
name: dialign2
category: alignment
description: DIALIGN multiple sequence alignment using various sources of external information.
tags: [dialign2, alignment, multiple-sequence, external-information]
author: oxo-call-community
source_url: "http://dialign.gobics.de"
---

## Concepts

- **Tool Overview**: DIALIGN2 v2.2.1 - Multiple sequence alignment program that can incorporate external information.
- **Core Function**: Creates multiple sequence alignments using segment-based approach with support for external constraints.
- **Input/Output**: Expects FASTA sequences; outputs multiple sequence alignments.
- **Installation**: `conda install -c bioconda dialign2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dialign2 -fa input.fa -out aligned.fa`
**Explanation:** Performs multiple sequence alignment with external information.
