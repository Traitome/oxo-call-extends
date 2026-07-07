---
name: ucsc-fafilter
category: utility
description: UCSC faFilter - Tool for filtering FASTA sequences.
tags: [ucsc-fafilter, ucsc, fasta, sequence-filtering, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faFilter - A tool for filtering FASTA sequences.
- **Core Function**: Filters sequences based on various criteria.
- **Input**: FASTA file.
- **Output**: Filtered FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence filtering, quality control, data preparation.

## Pitfalls

- **Filter Criteria**: Requires appropriate filter parameters.
- **Memory**: May require significant memory for large sequences.

## Examples

### Filter sequences
**Args:** `faFilter -minSize=1000 input.fa > filtered.fa`
**Explanation:** Filter sequences by minimum size.

### With multiple filters
**Args:** `faFilter -minSize=1000 -maxN=0.1 input.fa > filtered.fa`
**Explanation:** Filter by size and N content.
