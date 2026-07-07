---
name: ucsc-bedpileups
category: analysis
description: UCSC bedPileups - Tool for generating pileups from BED files.
tags: [ucsc-bedpileups, ucsc, pileup-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedPileups - A tool for generating pileup information from BED files.
- **Core Function**: Creates pileup tracks from aligned reads in BED format.
- **Input**: BED file with alignment information.
- **Output**: Pileup data.
- **Installation**: Part of UCSC utilities
- **Use Case**: Read depth analysis, coverage visualization, variant calling.

## Pitfalls

- **Format Requirements**: Requires specific BED format with read information.
- **Memory**: May require significant memory for large datasets.

## Examples

### Generate pileup
**Args:** `bedPileups -i alignments.bed > pileup.txt`
**Explanation:** Generate pileup from aligned reads.

### With quality filter
**Args:** `bedPileups -minQ 30 -i alignments.bed > pileup.txt`
**Explanation:** Generate pileup with quality filter.
