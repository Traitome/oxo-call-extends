---
name: ucsc-avecols
category: utility
description: UCSC aveCols - Tool for averaging columns in tab-delimited files.
tags: [ucsc-avecols, ucsc, data-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC aveCols - A tool for calculating averages across columns in tab-delimited files.
- **Core Function**: Computes average values for specified columns.
- **Input**: Tab-delimited file with numeric columns.
- **Output**: File with averaged columns.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data analysis, statistics, genomics data processing.

## Pitfalls

- **Numeric Data**: Requires numeric column data.
- **Missing Values**: May handle missing values differently.

## Examples

### Average columns
**Args:** `aveCols -cols=2-5 input.txt > output.txt`
**Explanation:** Calculate average of columns 2-5.

### Weighted average
**Args:** `aveCols -cols=3 -weights=weights.txt input.txt > result.txt`
**Explanation:** Calculate weighted average of column 3.
