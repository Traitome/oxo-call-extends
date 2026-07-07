---
name: ucsc-maffilter
category: utility
description: UCSC mafFilter - Tool for filtering MAF alignments.
tags: [ucsc-maffilter, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafFilter - A tool for filtering MAF alignments.
- **Core Function**: Filters MAF alignments based on various criteria.
- **Input**: MAF file.
- **Output**: Filtered MAF file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment filtering, quality control, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Filter Criteria**: Requires proper filter specification.

## Examples

### Filter MAF alignments
**Args:** `mafFilter input.maf > filtered.maf`
**Explanation:** Filter MAF alignments.

### With options
**Args:** `mafFilter -minScore=100 input.maf > filtered.maf`
**Explanation:** Minimum alignment score filter.
