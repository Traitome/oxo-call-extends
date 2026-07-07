---
name: ucsc-chaincleaner
category: utility
description: UCSC chainCleaner - Tool for cleaning chain alignments.
tags: [ucsc-chaincleaner, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainCleaner - A tool for cleaning and filtering chain alignments.
- **Core Function**: Removes low-quality or problematic alignments.
- **Input**: Chain alignment file.
- **Output**: Cleaned chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment quality control, filtering, genome comparison.

## Pitfalls

- **Quality Threshold**: Requires appropriate quality thresholds.
- **Memory**: May require significant memory for large files.

## Examples

### Clean chains
**Args:** `chainCleaner input.chain > cleaned.chain`
**Explanation:** Clean and filter chain alignments.

### With quality filter
**Args:** `chainCleaner -minScore=1000 input.chain > cleaned.chain`
**Explanation:** Filter chains by minimum score.
