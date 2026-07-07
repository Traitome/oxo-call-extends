---
name: ucsc-bigpsltopsl
category: utility
description: UCSC bigPslToPsl - Tool for extracting PSL from bigPsl format.
tags: [ucsc-bigpsltopsl, ucsc, format-conversion, bigpsl, psl]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigPslToPsl - A tool for extracting PSL alignments from bigPsl format.
- **Core Function**: Converts bigPsl files to plain PSL format.
- **Input**: bigPsl file.
- **Output**: PSL format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment analysis, genome browser.

## Pitfalls

- **File Size**: Output may be significantly larger.
- **Index Requirement**: Requires indexed bigPsl file.

## Examples

### Convert to PSL
**Args:** `bigPslToPsl input.bigpsl output.psl`
**Explanation:** Convert bigPsl to PSL format.

### With region
**Args:** `bigPslToPsl -chrom=chr1 input.bigpsl output.psl`
**Explanation:** Extract alignments from specific chromosome.
