---
name: ucsc-bigmaftomaf
category: utility
description: UCSC bigMafToMaf - Tool for converting bigMaf to MAF format.
tags: [ucsc-bigmaftomaf, ucsc, format-conversion, bigmaf, maf]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigMafToMaf - A tool for converting bigMaf format to MAF format.
- **Core Function**: Converts indexed bigMaf files to plain MAF format.
- **Input**: bigMaf file.
- **Output**: MAF format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment analysis, data sharing.

## Pitfalls

- **File Size**: Output may be significantly larger.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to MAF
**Args:** `bigMafToMaf input.bigmaf output.maf`
**Explanation:** Convert bigMaf to MAF format.

### With region
**Args:** `bigMafToMaf -chrom=chr1 -start=1 -end=1000000 input.bigmaf output.maf`
**Explanation:** Extract specific region from bigMaf.
