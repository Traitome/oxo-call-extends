---
name: ucsc-rmfadups
category: utility
description: UCSC rmFaDups - Tool for removing duplicate sequences.
tags: [ucsc-rmfadups, ucsc, fasta, duplicates, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC rmFaDups - A tool for removing duplicate FASTA sequences.
- **Core Function**: Removes duplicate sequences from FASTA files.
- **Input**: FASTA file.
- **Output**: Deduplicated FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence deduplication, data cleaning, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper FASTA format.

## Examples

### Remove duplicate sequences
**Args:** `rmFaDups input.fa > unique.fa`
**Explanation:** Remove duplicate sequences.

### With options
**Args:** `rmFaDups -verbose input.fa > unique.fa`
**Explanation:** Remove with verbose output.
