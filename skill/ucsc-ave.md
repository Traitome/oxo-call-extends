---
name: ucsc-ave
category: analysis
description: UCSC ave - Tool for calculating statistics across multiple files.
tags: [ucsc-ave, ucsc, statistics, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC ave - A tool for calculating statistics across multiple data files.
- **Core Function**: Computes averages, sums, and other statistics across files.
- **Input**: Multiple tab-delimited files with corresponding columns.
- **Output**: Statistical summaries across files.
- **Installation**: Part of UCSC utilities
- **Use Case**: Comparative analysis, data aggregation, statistics.

## Pitfalls

- **File Matching**: Requires matching columns across files.
- **Data Consistency**: Requires consistent data formats.

## Examples

### Average across files
**Args:** `ave file1.txt file2.txt file3.txt > averages.txt`
**Explanation:** Calculate averages across multiple files.

### Sum across files
**Args:** `ave -sum file*.txt > sums.txt`
**Explanation:** Calculate sums across files.
