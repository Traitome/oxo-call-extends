---
name: dnp-mapping
category: utility
description: DNPattern tools - Mapping nucleosome positions using dinucleotide patterns.
tags: [dnp-mapping, utility, nucleosome, dinucleotide, mapping]
author: oxo-call-community
source_url: "https://github.com/erinijapranckeviciene/mapping_CC"
---

## Concepts

- **Tool Overview**: dnp-mapping - Tool for mapping nucleosome positions using dinucleotide pattern analysis.
- **Core Function**: Maps nucleosome positions in sequences based on dinucleotide periodicity patterns.
- **Input/Output**: Expects FASTA sequences; outputs predicted nucleosome positions.
- **Installation**: `conda install -c bioconda dnp-mapping`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires DNA sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dnp-mapping --input sequences.fa --output nucleosomes.bed`
**Explanation:** Maps nucleosome positions using dinucleotide patterns.
