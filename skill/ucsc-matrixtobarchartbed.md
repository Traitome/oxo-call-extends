---
name: ucsc-matrixtobarchartbed
category: utility
description: UCSC matrixToBarChartBed - Tool for converting matrix to bar chart BED.
tags: [ucsc-matrixtobarchartbed, ucsc, matrix, bed, visualization]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC matrixToBarChartBed - A tool for converting matrix to bar chart BED.
- **Core Function**: Converts matrix data to bar chart BED format.
- **Input**: Matrix file.
- **Output**: Bar chart BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Visualization, genome browser tracks.

## Pitfalls

- **Memory**: May require significant memory for large matrices.
- **Format Requirements**: Requires proper matrix format.

## Examples

### Convert matrix to bar chart BED
**Args:** `matrixToBarChartBed input.txt > output.bed`
**Explanation:** Convert matrix to bar chart BED.

### With options
**Args:** `matrixToBarChartBed -name=signal input.txt > output.bed`
**Explanation:** Add track name.
