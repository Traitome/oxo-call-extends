---
name: ucsc-mafsplitpos
category: utility
description: UCSC mafSplitPos - Tool for splitting MAF at specific positions.
tags: [ucsc-mafsplitpos, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafSplitPos - A tool for splitting MAF at specific positions.
- **Core Function**: Splits MAF alignments at specified positions.
- **Input**: MAF file, position file.
- **Output**: Split MAF alignments.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment splitting, region analysis, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper position format.

## Examples

### Split MAF at positions
**Args:** `mafSplitPos positions.txt input.maf > output.maf`
**Explanation:** Split MAF at specified positions.

### With options
**Args:** `mafSplitPos -verbose positions.txt input.maf > output.maf`
**Explanation:** Split with verbose output.
