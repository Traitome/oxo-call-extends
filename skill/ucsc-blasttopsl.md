---
name: ucsc-blasttopsl
category: utility
description: UCSC blastToPsl - Tool for converting BLAST output to PSL format.
tags: [ucsc-blasttopsl, ucsc, format-conversion, blast, psl]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC blastToPsl - A tool for converting BLAST alignments to PSL format.
- **Core Function**: Converts BLAST output to PSL format for visualization.
- **Input**: BLAST output file.
- **Output**: PSL format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment visualization, genome browser.

## Pitfalls

- **Format Requirements**: Requires specific BLAST output format.
- **Alignment Quality**: Results depend on BLAST alignment quality.

## Examples

### Convert BLAST to PSL
**Args:** `blastToPsl input.blast output.psl`
**Explanation:** Convert BLAST output to PSL format.

### With query sequence
**Args:** `blastToPsl -query=query.fa input.blast output.psl`
**Explanation:** Convert with query sequence information.
