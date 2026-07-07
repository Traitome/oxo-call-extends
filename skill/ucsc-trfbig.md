---
name: ucsc-trfbig
category: utility
description: UCSC trfBig - Tool for tandem repeat finder on big files.
tags: [ucsc-trfbig, ucsc, trf, tandem-repeat, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC trfBig - A tool for finding tandem repeats in big files.
- **Core Function**: Identifies tandem repeat sequences.
- **Input**: Sequence file.
- **Output**: Tandem repeat annotations.
- **Installation**: Part of UCSC utilities
- **Use Case**: Repeat analysis, genome annotation, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **Performance**: May be slow for large inputs.

## Examples

### Find tandem repeats
**Args:** `trfBig input.fa > repeats.txt`
**Explanation:** Find tandem repeats.

### With options
**Args:** `trfBig -minScore=50 input.fa > repeats.txt`
**Explanation:** Minimum score threshold.
