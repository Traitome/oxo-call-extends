---
name: ucsc-bigwigsummary
category: analysis
description: UCSC bigWigSummary - Tool for generating summaries from BigWig files.
tags: [ucsc-bigwigsummary, ucsc, bigwig, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigSummary - A tool for generating statistical summaries from BigWig files.
- **Core Function**: Computes statistics over genomic regions in BigWig format.
- **Input**: BigWig file, BED regions.
- **Output**: Statistical summaries.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data summarization, quality control, statistical analysis.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Region Format**: Requires proper BED format for regions.

## Examples

### Generate summary
**Args:** `bigWigSummary input.bw regions.bed > summary.txt`
**Explanation:** Generate summary over specified regions.

### With statistics
**Args:** `bigWigSummary -stats input.bw regions.bed > summary.txt`
**Explanation:** Generate detailed statistics.
