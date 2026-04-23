---
name: dnp-corrprofile
category: utility
description: DNPattern tools - Correlation profile of dinucleotide frequency patterns.
tags: [dnp-corrprofile, utility, dinucleotide, correlation, pattern]
author: oxo-call-community
source_url: "https://github.com/erinijapranckeviciene/dnpatterntools"
---

## Concepts

- **Tool Overview**: dnp-corrprofile - Tool for computing correlation profiles of dinucleotide frequency patterns.
- **Core Function**: Calculates correlations between dinucleotide frequency patterns on forward and reverse strands.
- **Input/Output**: Expects FASTA sequences; outputs correlation profiles.
- **Installation**: `conda install -c bioconda dnp-corrprofile`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires DNA sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dnp-corrprofile --input sequences.fa --output correlations.tsv`
**Explanation:** Computes dinucleotide frequency correlation profiles.
