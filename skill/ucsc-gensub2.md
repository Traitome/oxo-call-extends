---
name: ucsc-gensub2
category: utility
description: UCSC genSub2 - Tool for generating sequence subsets.
tags: [ucsc-gensub2, ucsc, sequence-extraction, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC genSub2 - A tool for generating sequence subsets from genome.
- **Core Function**: Extracts sequence regions based on coordinates.
- **Input**: Genome FASTA, region coordinates.
- **Output**: Sequence subset.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence extraction, primer design, region analysis.

## Pitfalls

- **Coordinate Format**: Requires proper coordinate specification.
- **Memory**: May require significant memory for large genomes.

## Examples

### Extract subset
**Args:** `genSub2 genome.fa chr1:1000-2000 > region.fa`
**Explanation:** Extract sequence region.

### With options
**Args:** `genSub2 -mask genome.fa chr1:1000-2000 > region.fa`
**Explanation:** Extract with soft masking.
