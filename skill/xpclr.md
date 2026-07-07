---
name: xpclr
category: bioinformatics
description: XPCLR - Population genetic analysis.
tags: [xpclr, population-genetics, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/hardingnj/xpclr"
---

## Concepts

- **Tool Overview**: XPCLR - Cross-population composite likelihood ratio.
- **Core Function**: Detects positive selection.
- **Input**: Genotype data.
- **Output**: Selection scores.
- **Installation**: Install via pip or conda
- **Use Case**: Population genetics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Detect selection
**Args:** `xpclr -i genotypes.txt -o selection.txt`
**Explanation:** Detect positive selection.

### With options
**Args:** `xpclr -i genotypes.txt -o selection.txt -w 100`
**Explanation:** Use window size 100.
