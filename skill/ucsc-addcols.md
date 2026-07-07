---
name: ucsc-addcols
category: utility
description: UCSC addCols - Tool for adding columns to tab-delimited files.
tags: [ucsc-addcols, ucsc, table-manipulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC addCols - A utility for adding columns to tab-delimited data files.
- **Core Function**: Adds columns from one file to another based on matching keys.
- **Input**: Tab-delimited files, key columns.
- **Output**: Merged tab-delimited file with added columns.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data merging, table manipulation, genomics data processing.

## Pitfalls

- **Key Column**: Requires matching key columns in both files.
- **File Format**: Requires proper tab-delimited format.

## Examples

### Add columns
**Args:** `addCols -keys=1 -col=5 file1.txt file2.txt > output.txt`
**Explanation:** Add column 5 from file2 to file1 based on key column 1.

### Multiple keys
**Args:** `addCols -keys=1,2 -col=3,4 fileA.txt fileB.txt > merged.txt`
**Explanation:** Merge files using multiple key columns.
