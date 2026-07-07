---
name: ucsc-pslcat
category: utility
description: UCSC pslCat - Tool for concatenating PSL files.
tags: [ucsc-pslcat, ucsc, psl, concatenation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslCat - A tool for concatenating PSL files.
- **Core Function**: Combines multiple PSL files into one.
- **Input**: Multiple PSL files.
- **Output**: Combined PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data merging, alignment processing, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Concatenate PSL files
**Args:** `pslCat input1.psl input2.psl > combined.psl`
**Explanation:** Combine multiple PSL files.

### With options
**Args:** `pslCat -verbose input1.psl input2.psl > combined.psl`
**Explanation:** Concatenate with verbose output.
