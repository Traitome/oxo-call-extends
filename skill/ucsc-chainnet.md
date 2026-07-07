---
name: ucsc-chainnet
category: utility
description: UCSC chainNet - Tool for creating net alignments from chains.
tags: [ucsc-chainnet, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainNet - A tool for creating net alignments from chain alignments.
- **Core Function**: Creates hierarchical net alignments from chain files.
- **Input**: Chain alignment file.
- **Output**: Net alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome alignment, synteny analysis, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Computation Time**: May be slow for large genomes.

## Examples

### Create net alignment
**Args:** `chainNet target.chain query.chain > output.net`
**Explanation:** Create net alignment from chains.

### With gap limit
**Args:** `chainNet -minGap=1000 target.chain query.chain > output.net`
**Explanation:** Create net with minimum gap size.
