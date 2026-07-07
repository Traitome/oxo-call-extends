---
name: ucsc-netfilter
category: utility
description: UCSC netFilter - Tool for filtering net alignments.
tags: [ucsc-netfilter, ucsc, net, filtering, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC netFilter - A tool for filtering net alignments.
- **Core Function**: Filters net alignments based on criteria.
- **Input**: Net file.
- **Output**: Filtered net file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment filtering, quality control, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Filter Criteria**: Requires proper filter specification.

## Examples

### Filter net alignments
**Args:** `netFilter input.net > filtered.net`
**Explanation:** Filter net alignments.

### With options
**Args:** `netFilter -minScore=100 input.net > filtered.net`
**Explanation:** Minimum alignment score filter.
