---
name: ucsc-bedtogenepred
category: utility
description: UCSC bedToGenePred - Tool for converting BED to GenePred format.
tags: [ucsc-bedtogenepred, ucsc, format-conversion, bed, genepred]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedToGenePred - A tool for converting BED format to GenePred format.
- **Core Function**: Converts BED12 gene annotations to GenePred format.
- **Input**: BED12 format file.
- **Output**: GenePred format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Gene annotation conversion, genome browser compatibility.

## Pitfalls

- **Format Requirements**: Requires BED12 format.
- **Gene Structure**: Requires proper gene structure in input.

## Examples

### Convert to GenePred
**Args:** `bedToGenePred input.bed output.genepred`
**Explanation:** Convert BED12 to GenePred format.

### With name
**Args:** `bedToGenePred -geneNameAsName2 input.bed output.genepred`
**Explanation:** Convert using gene name as name2 field.
