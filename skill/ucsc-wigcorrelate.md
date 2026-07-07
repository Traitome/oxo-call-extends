---
name: ucsc-wigcorrelate
category: utility
description: UCSC wigCorrelate - Tool for computing WIG correlations.
tags: [ucsc-wigcorrelate, ucsc, wig, correlation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC wigCorrelate - A tool for computing correlations between WIG files.
- **Core Function**: Calculates correlation coefficients between genomic signals.
- **Input**: WIG files.
- **Output**: Correlation matrix.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data analysis, comparative genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large WIG files.
- **Format Requirements**: Requires proper WIG format.

## Examples

### Compute WIG correlation
**Args:** `wigCorrelate input1.wig input2.wig`
**Explanation:** Compute correlation between two WIG files.

### With options
**Args:** `wigCorrelate -verbose input1.wig input2.wig`
**Explanation:** Compute with verbose output.
