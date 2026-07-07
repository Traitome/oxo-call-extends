---
name: ucsc-pslscore
category: utility
description: UCSC pslScore - Tool for scoring PSL alignments.
tags: [ucsc-pslscore, ucsc, psl, scoring, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslScore - A tool for scoring PSL alignments.
- **Core Function**: Calculates alignment scores.
- **Input**: PSL file.
- **Output**: Scored PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment scoring, quality assessment, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Score PSL alignments
**Args:** `pslScore input.psl > scored.psl`
**Explanation:** Calculate alignment scores.

### With options
**Args:** `pslScore -verbose input.psl > scored.psl`
**Explanation:** Score with verbose output.
