---
name: ucsc-gff3togenepred
category: utility
description: UCSC gff3ToGenePred - Tool for converting GFF3 to genePred.
tags: [ucsc-gff3togenepred, ucsc, gff3, gene-prediction, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC gff3ToGenePred - A tool for converting GFF3 to genePred format.
- **Core Function**: Converts GFF3 annotations to genePred format.
- **Input**: GFF3 file.
- **Output**: genePred format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome annotation, gene prediction.

## Pitfalls

- **Format Requirements**: Requires proper GFF3 format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert GFF3 to genePred
**Args:** `gff3ToGenePred input.gff3 > genes.txt`
**Explanation:** Convert GFF3 to genePred format.

### With options
**Args:** `gff3ToGenePred -geneNameAsName2 input.gff3 > genes.txt`
**Explanation:** Use gene name as name2 field.
