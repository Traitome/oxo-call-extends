---
name: lastz
category: alignment
description: LASTZ is a program for aligning DNA sequences, a pairwise aligner.
tags: [lastz, alignment]
author: oxo-call-community
source_url: "https://www.bx.psu.edu/~rsharris/lastz"
---

## Concepts

- **Tool Overview**: lastz v1.04.52 - LASTZ is a program for aligning DNA sequences, a pairwise aligner..
- **Core Function**: LASTZ is a program for aligning DNA sequences, a pairwise aligner.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda lastz`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Align sequences
**Args:** `target.fasta query.fasta --output=alignments.maf`
**Explanation:** Aligns query to target sequences outputting MAF format.

