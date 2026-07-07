---
name: velocyto.py
category: bioinformatics
description: velocyto.py - RNA velocity analysis.
tags: [velocyto.py, single-cell, rna-velocity, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/velocyto-team/velocyto.py"
---

## Concepts

- **Tool Overview**: velocyto.py - RNA velocity analysis tool.
- **Core Function**: Analyzes RNA velocity from single-cell RNA-seq data.
- **Input**: BAM file, annotation.
- **Output**: Velocity estimates.
- **Installation**: Install via pip or conda
- **Use Case**: Single-cell RNA-seq analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Run velocity analysis
**Args:** `velocyto run10x -b sample.bam -o output/ -g genes.gtf`
**Explanation:** Run velocity analysis.

### With options
**Args:** `velocyto run10x -b sample.bam -o output/ -g genes.gtf -@ 8`
**Explanation:** Use 8 threads.
