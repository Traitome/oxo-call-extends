---
name: ucsc-chaintoaxt
category: utility
description: UCSC chainToAxt - Tool for converting chains to axt format.
tags: [ucsc-chaintoaxt, ucsc, format-conversion, chain, axt]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainToAxt - A tool for converting chain alignments to axt format.
- **Core Function**: Converts chain format alignments to axt format.
- **Input**: Chain alignment file, FASTA sequences.
- **Output**: Axt format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment visualization, genome browser.

## Pitfalls

- **FASTA Requirement**: Requires FASTA sequence files.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to axt
**Args:** `chainToAxt input.chain target.fa query.fa > output.axt`
**Explanation:** Convert chain to axt format.

### With output directory
**Args:** `chainToAxt -outputDir=axt_dir input.chain target.fa query.fa`
**Explanation:** Convert with output to directory.
