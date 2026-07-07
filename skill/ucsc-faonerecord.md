---
name: ucsc-faonerecord
category: utility
description: UCSC faOneRecord - Tool for extracting single FASTA record.
tags: [ucsc-faonerecord, ucsc, fasta, sequence-extraction, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faOneRecord - A tool for extracting a single record from FASTA.
- **Core Function**: Extracts one sequence by name from multi-record FASTA.
- **Input**: FASTA file, sequence name.
- **Output**: Single FASTA record.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence extraction, single record analysis.

## Pitfalls

- **Sequence Name**: Requires exact sequence name match.
- **Memory**: May require significant memory for large files.

## Examples

### Extract record
**Args:** `faOneRecord genome.fa chr1 > chr1.fa`
**Explanation:** Extract single chromosome.

### From stdin
**Args:** `cat genome.fa | faOneRecord stdin chr1 > chr1.fa`
**Explanation:** Extract from piped input.
