---
name: ucsc-pslsplitontarget
category: utility
description: UCSC pslSplitOnTarget - Tool for splitting PSL on target.
tags: [ucsc-pslsplitontarget, ucsc, psl, splitting, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslSplitOnTarget - A tool for splitting PSL alignments on target.
- **Core Function**: Splits alignments based on target regions.
- **Input**: PSL file, target regions.
- **Output**: Split PSL files.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data partitioning, target-based splitting, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Split PSL on target
**Args:** `pslSplitOnTarget targets.bed input.psl`
**Explanation:** Split alignments by target regions.

### With options
**Args:** `pslSplitOnTarget -verbose targets.bed input.psl`
**Explanation:** Split with verbose output.
