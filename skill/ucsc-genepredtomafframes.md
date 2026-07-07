---
name: ucsc-genepredtomafframes
category: utility
description: UCSC genePredToMafFrames - Tool for converting gene predictions to MAF frames.
tags: [ucsc-genepredtomafframes, ucsc, gene-prediction, maf, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC genePredToMafFrames - A tool for converting gene predictions to MAF frame coordinates.
- **Core Function**: Converts gene predictions to MAF alignment coordinates.
- **Input**: Gene prediction file, MAF file.
- **Output**: MAF frame coordinates.
- **Installation**: Part of UCSC utilities
- **Use Case**: Comparative genomics, alignment analysis, gene prediction.

## Pitfalls

- **MAF Requirement**: Requires MAF alignment file.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to MAF frames
**Args:** `genePredToMafFrames genes.txt alignment.maf > frames.txt`
**Explanation:** Convert gene predictions to MAF frames.

### With options
**Args:** `genePredToMafFrames -species=hg38 genes.txt alignment.maf > frames.txt`
**Explanation:** Specify species.
