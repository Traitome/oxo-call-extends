---
name: ucsc-axtchain
category: alignment
description: UCSC axtChain - Tool for aligning two genomes using chain format.
tags: [ucsc-axtchain, ucsc, genome-alignment, chain-format, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC axtChain - A tool for creating pairwise genome alignments in chain format.
- **Core Function**: Aligns two genomes and outputs alignments in chain format.
- **Input**: Two genome sequences (FASTA), optional alignment hints.
- **Output**: Chain format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome alignment, comparative genomics, synteny analysis.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Alignment Time**: May be slow for large genomes.

## Examples

### Align genomes
**Args:** `axtChain -linearGap=medium target.fa query.fa output.chain`
**Explanation:** Create chain alignment between two genomes.

### With netting
**Args:** `axtChain -preNet target.fa query.fa chain.raw chain.net`
**Explanation:** Create alignment with pre-netting.
