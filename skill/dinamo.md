---
name: dinamo
category: utility
description: Motif discovery tool for nucleotide sequences.
tags: [dinamo, utility, motif-discovery, nucleotide]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DINAMO - Motif discovery tool for finding conserved patterns in nucleotide sequences.
- **Core Function**: Discovers over-represented sequence motifs in sets of nucleotide sequences.
- **Input/Output**: Expects FASTA sequences; outputs discovered motifs with position weight matrices.
- **Installation**: `conda install -c bioconda dinamo`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires nucleotide sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dinamo --input sequences.fa --output motifs/`
**Explanation:** Discovers sequence motifs in nucleotide data.
