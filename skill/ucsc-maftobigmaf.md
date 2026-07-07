---
name: ucsc-maftobigmaf
category: utility
description: UCSC mafToBigMaf - Tool for converting MAF to bigMaf.
tags: [ucsc-maftobigmaf, ucsc, maf, bigmaf, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafToBigMaf - A tool for converting MAF to bigMaf format.
- **Core Function**: Converts MAF alignments to binary bigMaf format.
- **Input**: MAF file, chrom.sizes file.
- **Output**: bigMaf binary file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser tracks, data compression.

## Pitfalls

- **Chromosome Sizes**: Requires chrom.sizes file.
- **Memory**: May require significant memory for large files.

## Examples

### Convert MAF to bigMaf
**Args:** `mafToBigMaf input.maf chrom.sizes > output.bb`
**Explanation:** Convert MAF to bigMaf format.

### With options
**Args:** `mafToBigMaf -name=alignments input.maf chrom.sizes > output.bb`
**Explanation:** Add track name.
