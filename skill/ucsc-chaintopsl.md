---
name: ucsc-chaintopsl
category: utility
description: UCSC chainToPsl - Tool for converting chains to PSL format.
tags: [ucsc-chaintopsl, ucsc, format-conversion, chain, psl]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainToPsl - A tool for converting chain alignments to PSL format.
- **Core Function**: Converts chain format alignments to full PSL format.
- **Input**: Chain alignment file, FASTA sequences.
- **Output**: PSL format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment visualization, genome browser.

## Pitfalls

- **FASTA Requirement**: Requires FASTA sequence files.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to PSL
**Args:** `chainToPsl input.chain target.fa query.fa > output.psl`
**Explanation:** Convert chain to PSL format.

### With output file
**Args:** `chainToPsl -output output.psl input.chain target.fa query.fa`
**Explanation:** Convert with specified output file.
