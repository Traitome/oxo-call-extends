---
name: summarize-ranges
category: utility
description: Summarize contiguous ranges of integers found on standard input.
tags: [summarize-ranges, interval-analysis, bioinformatics-utility]
author: oxo-call-community
source_url: "https://github.com/terrycojones/summarize-ranges"
---

## Concepts

- **Tool Overview**: summarize-ranges (v0.1.1) summarizes contiguous ranges of integers from input.
- **Core Function**: Merges overlapping or contiguous integer ranges into concise summaries.
- **Algorithm**: Uses interval merging to summarize integer ranges efficiently.
- **Input/Output**: Input: Integer values; Output: Summarized range notation.
- **Applications**: Genomics interval analysis, data summarization, coordinate processing.
- **Installation**: `conda install -c bioconda summarize-ranges` or download from GitHub.

## Pitfalls

- **Input Format**: Requires sorted integer input.
- **Memory Requirements**: Large input may require significant memory.
- **Duplicate Values**: Duplicates may affect results.
- **Performance**: Very large inputs can be slow.
- **Output Format**: Requires understanding of range notation.
- **Edge Cases**: Empty input or single values require special handling.

## Examples

### Display help
**Args:** `summarize-ranges --help`
**Explanation:** Shows available options and usage information.

### Basic range summarization
**Args:** `echo "1 2 3 5 6 7" | summarize-ranges`
**Explanation:** Summarize integer ranges from standard input.

### From file
**Args:** `summarize-ranges -i positions.txt`
**Explanation:** Read integers from file.

### Verbose mode
**Args:** `echo "1 2 3 5 6 7" | summarize-ranges -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `echo "1 2 3 5 6 7" | summarize-ranges --stats`
**Explanation:** Generate statistics about ranges.

### Batch processing
**Args:** `summarize-ranges -i positions/*.txt -o results/`
**Explanation:** Process multiple position files together.

### Filter by size
**Args:** `echo "1 2 3 5 6 7" | summarize-ranges -m 2`
**Explanation:** Minimum range size of 2.

### Include gaps
**Args:** `echo "1 2 3 5 6 7" | summarize-ranges --gaps`
**Explanation:** Include gap information in output.

### Generate report
**Args:** `echo "1 2 3 5 6 7" | summarize-ranges --report`
**Explanation:** Generate comprehensive HTML report.
