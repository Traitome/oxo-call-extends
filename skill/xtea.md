---
name: xtea
category: bioinformatics
description: XTEA - RNA-seq analysis tool.
tags: [xtea, rna-seq, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/yangcao77/XTEA"
---

## Concepts

- **Tool Overview**: XTEA - Alternative splicing detection tool.
- **Core Function**: Detects alternative splicing events.
- **Input**: RNA-seq data.
- **Output**: Splicing events.
- **Installation**: Install via pip or conda
- **Use Case**: RNA-seq analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Detect splicing
**Args:** `xtea -i input.bam -o splicing.txt`
**Explanation:** Detect alternative splicing.

### With options
**Args:** `xtea -i input.bam -o splicing.txt -t 8`
**Explanation:** Use 8 threads.
