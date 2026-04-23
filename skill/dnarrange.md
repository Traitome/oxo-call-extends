---
name: dnarrange
category: utility
description: DNArrange - Tool for rearranging DNA sequences.
tags: [dnarrange, utility, dna, rearrangement]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DNArrange - Tool for rearranging and reorganizing DNA sequences.
- **Core Function**: Rearranges DNA sequences according to specified patterns.
- **Input/Output**: Expects DNA sequences; outputs rearranged sequences.
- **Installation**: `conda install -c bioconda dnarrange`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires DNA sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dnarrange --input sequences.fa --pattern rearrangement.txt --output rearranged.fa`
**Explanation:** Rearranges DNA sequences according to pattern.
