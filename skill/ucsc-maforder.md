---
name: ucsc-maforder
category: utility
description: UCSC mafOrder - Tool for ordering MAF alignments.
tags: [ucsc-maforder, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafOrder - A tool for ordering MAF alignments.
- **Core Function**: Reorders sequences in MAF alignments.
- **Input**: MAF file.
- **Output**: Ordered MAF file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment processing, reordering, visualization.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Order MAF alignments
**Args:** `mafOrder input.maf > output.maf`
**Explanation:** Order sequences in MAF alignment.

### With options
**Args:** `mafOrder -speciesOrder=hg38,panTro4 input.maf > output.maf`
**Explanation:** Specify species order.
