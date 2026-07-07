---
name: ucsc-facmp
category: utility
description: UCSC faCmp - Tool for comparing FASTA sequences.
tags: [ucsc-facmp, ucsc, fasta, sequence-comparison, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faCmp - A tool for comparing FASTA sequences.
- **Core Function**: Compares two FASTA files for differences.
- **Input**: Two FASTA files.
- **Output**: Comparison report.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence comparison, validation, quality control.

## Pitfalls

- **Sequence Names**: Requires matching sequence names.
- **Memory**: May require significant memory for large sequences.

## Examples

### Compare FASTA files
**Args:** `faCmp ref.fa query.fa > diff.txt`
**Explanation:** Compare two FASTA files.

### With options
**Args:** `faCmp -verbose ref.fa query.fa > diff.txt`
**Explanation:** Compare with verbose output.
