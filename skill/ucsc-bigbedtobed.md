---
name: ucsc-bigbedtobed
category: utility
description: UCSC bigBedToBed - Tool for converting BigBed to BED format.
tags: [ucsc-bigbedtobed, ucsc, format-conversion, bigbed, bed]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigBedToBed - A tool for converting BigBed format to BED format.
- **Core Function**: Converts indexed BigBed files to plain BED format.
- **Input**: BigBed file.
- **Output**: BED format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, data extraction, analysis.

## Pitfalls

- **File Size**: Output may be significantly larger than input.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to BED
**Args:** `bigBedToBed input.bb output.bed`
**Explanation:** Convert BigBed to BED format.

### With region
**Args:** `bigBedToBed -chrom=chr1 -start=1 -end=1000000 input.bb output.bed`
**Explanation:** Extract specific region from BigBed.
