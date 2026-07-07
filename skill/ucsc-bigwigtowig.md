---
name: ucsc-bigwigtowig
category: utility
description: UCSC bigWigToWig - Tool for converting BigWig to Wig format.
tags: [ucsc-bigwigtowig, ucsc, format-conversion, bigwig, wig]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigToWig - A tool for converting BigWig format to Wig format.
- **Core Function**: Converts indexed BigWig files to plain Wig format.
- **Input**: BigWig file.
- **Output**: Wig format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, data extraction, analysis.

## Pitfalls

- **File Size**: Output may be significantly larger than input.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to Wig
**Args:** `bigWigToWig input.bw output.wig`
**Explanation:** Convert BigWig to Wig format.

### With region
**Args:** `bigWigToWig -chrom=chr1 -start=1 -end=1000000 input.bw output.wig`
**Explanation:** Extract specific region from BigWig.
