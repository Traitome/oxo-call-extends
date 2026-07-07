---
name: ucsc-chainfilter
category: utility
description: UCSC chainFilter - Tool for filtering chain alignments.
tags: [ucsc-chainfilter, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainFilter - A tool for filtering chain alignments based on various criteria.
- **Core Function**: Filters chain alignments by score, size, or other properties.
- **Input**: Chain alignment file.
- **Output**: Filtered chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment filtering, quality control, genome comparison.

## Pitfalls

- **Filter Criteria**: Requires appropriate filter parameters.
- **Memory**: May require significant memory for large files.

## Examples

### Filter chains
**Args:** `chainFilter input.chain > filtered.chain`
**Explanation:** Filter chain alignments.

### With score filter
**Args:** `chainFilter -minScore=5000 input.chain > filtered.chain`
**Explanation:** Filter chains by minimum score.
