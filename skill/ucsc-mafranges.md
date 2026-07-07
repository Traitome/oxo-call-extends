---
name: ucsc-mafranges
category: utility
description: UCSC mafRanges - Tool for extracting ranges from MAF.
tags: [ucsc-mafranges, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafRanges - A tool for extracting ranges from MAF alignments.
- **Core Function**: Extracts specific ranges from MAF alignments.
- **Input**: MAF file, range file.
- **Output**: Extracted ranges.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment extraction, region analysis, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Extract ranges from MAF
**Args:** `mafRanges ranges.txt input.maf > output.maf`
**Explanation:** Extract specified ranges from MAF.

### With options
**Args:** `mafRanges -verbose ranges.txt input.maf > output.maf`
**Explanation:** Extract with verbose output.
