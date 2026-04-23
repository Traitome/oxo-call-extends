---
name: derip2
category: annotation
description: Predict ancestral sequence of fungal repeat elements by correcting for RIP-like mutations.
tags: [derip2, annotation, repeat-elements, fungal, rip]
author: oxo-call-community
source_url: "https://github.com/Adamtaranto/deRIP2"
---

## Concepts

- **Tool Overview**: deRIP2 v0.4.1 - Tool for correcting RIP-like mutations in fungal repeat elements to predict ancestral sequences.
- **Core Function**: Reverses Repeat-Induced Point (RIP) mutations in multi-sequence alignments to reconstruct ancestral repeat element sequences.
- **Input/Output**: Expects multiple sequence alignments (FASTA); outputs corrected/ancestral sequences.
- **Installation**: `conda install -c bioconda derip2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires aligned sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `derip2 --input repeats_aln.fa --output ancestral.fa`
**Explanation:** Corrects RIP mutations to predict ancestral repeat sequences.
