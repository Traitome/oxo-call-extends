---
name: ucsc-genepredtogtf
category: utility
description: UCSC genePredToGtf - Tool for converting gene predictions to GTF format.
tags: [ucsc-genepredtogtf, ucsc, gene-prediction, gtf, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC genePredToGtf - A tool for converting gene predictions to GTF format.
- **Core Function**: Converts genePred format to GTF format.
- **Input**: Gene prediction file.
- **Output**: GTF format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome annotation, RNA-seq analysis.

## Pitfalls

- **Format Requirements**: Requires proper genePred format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to GTF
**Args:** `genePredToGtf genes.txt > genes.gtf`
**Explanation:** Convert gene predictions to GTF.

### With source
**Args:** `genePredToGtf -source=GENCODE genes.txt > genes.gtf`
**Explanation:** Add source attribute.
