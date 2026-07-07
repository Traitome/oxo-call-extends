---
name: ucsc-bedtobigbed
category: utility
description: UCSC bedToBigBed - Tool for converting BED to BigBed format.
tags: [ucsc-bedtobigbed, ucsc, format-conversion, bed, bigbed]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedToBigBed - A tool for converting BED format to BigBed format.
- **Core Function**: Converts BED files to indexed BigBed format for efficient access.
- **Input**: BED file, chromosome sizes file.
- **Output**: BigBed format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser visualization, data sharing, efficient random access.

## Pitfalls

- **Sorted Input**: Requires sorted BED input.
- **Chromosome Names**: Requires matching chromosome names.

## Examples

### Convert to BigBed
**Args:** `bedToBigBed input.bed chrom.sizes output.bb`
**Explanation:** Convert BED to BigBed format.

### With autoSql
**Args:** `bedToBigBed -as=schema.as input.bed chrom.sizes output.bb`
**Explanation:** Convert with autoSql schema.
