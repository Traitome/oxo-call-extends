---
name: ucsc-chainscore
category: analysis
description: UCSC chainScore - Tool for scoring chain alignments.
tags: [ucsc-chainscore, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainScore - A tool for scoring chain alignments.
- **Core Function**: Calculates quality scores for chain alignments.
- **Input**: Chain alignment file.
- **Output**: Scored chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment quality assessment, scoring, filtering.

## Pitfalls

- **Scoring Parameters**: Requires appropriate scoring parameters.
- **Memory**: May require significant memory for large files.

## Examples

### Score chains
**Args:** `chainScore input.chain > scored.chain`
**Explanation:** Score chain alignments.

### With matrix
**Args:** `chainScore -matrix=matrix.txt input.chain > scored.chain`
**Explanation:** Score using custom scoring matrix.
