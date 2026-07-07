---
name: ucsc-genepredtofakepsl
category: utility
description: UCSC genePredToFakePsl - Tool for converting gene predictions to fake PSL.
tags: [ucsc-genepredtofakepsl, ucsc, gene-prediction, psl, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC genePredToFakePsl - A tool for creating fake PSL from gene predictions.
- **Core Function**: Generates PSL-like format from gene predictions.
- **Input**: Gene prediction file.
- **Output**: Fake PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, compatibility, visualization.

## Pitfalls

- **Fake PSL**: Not a true alignment, just PSL-like format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to fake PSL
**Args:** `genePredToFakePsl genes.txt > genes.psl`
**Explanation:** Create fake PSL from gene predictions.

### With options
**Args:** `genePredToFakePsl -name=gene genes.txt > genes.psl`
**Explanation:** Add name prefix.
