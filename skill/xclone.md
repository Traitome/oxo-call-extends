---
name: xclone
category: bioinformatics
description: xclone - Single-cell copy number analysis.
tags: [xclone, single-cell, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/single-cell-genetics/XClone"
---

## Concepts

- **Tool Overview**: xclone - Single-cell copy number analysis tool.
- **Core Function**: Analyzes copy number variations in single cells.
- **Input**: Single-cell sequencing data.
- **Output**: Copy number profiles.
- **Installation**: Install via pip
- **Use Case**: Single-cell analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Analyze single-cell CNV
**Args:** `xclone analyze -i input.h5ad -o cnv.txt`
**Explanation:** Analyze copy number variations.

### With options
**Args:** `xclone analyze -i input.h5ad -o cnv.txt -t 8`
**Explanation:** Use 8 threads.
