---
name: ucsc-expmatrixtobarchartbed
category: utility
description: UCSC expMatrixToBarChartBed - Tool for converting expression matrix to BED.
tags: [ucsc-expmatrixtobarchartbed, ucsc, expression, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC expMatrixToBarChartBed - A tool for converting expression matrices to BED format.
- **Core Function**: Transforms gene expression data into BED format for visualization.
- **Input**: Expression matrix file.
- **Output**: BED file for bar chart display.
- **Installation**: Part of UCSC utilities
- **Use Case**: Expression visualization, genome browser tracks.

## Pitfalls

- **Matrix Format**: Requires proper matrix format.
- **Gene Names**: Requires matching gene identifiers.

## Examples

### Convert expression matrix
**Args:** `expMatrixToBarChartBed matrix.txt > output.bed`
**Explanation:** Convert expression matrix to BED.

### With options
**Args:** `expMatrixToBarChartBed -normalize matrix.txt > output.bed`
**Explanation:** Convert with normalization.
