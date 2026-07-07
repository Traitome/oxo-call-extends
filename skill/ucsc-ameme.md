---
name: ucsc-ameme
category: analysis
description: UCSC aMeme - Tool for discovering motifs in DNA sequences.
tags: [ucsc-ameme, motif-discovery, dna-motifs, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC aMeme - A tool for discovering sequence motifs in DNA sequences.
- **Core Function**: Identifies statistically significant motifs in sequence datasets.
- **Input**: Sequence files (FASTA), optional background sequences.
- **Output**: Motif predictions, position weight matrices, motif logos.
- **Installation**: Part of UCSC utilities
- **Use Case**: Motif discovery, transcription factor binding sites, sequence analysis.

## Pitfalls

- **Motif Size**: Requires appropriate motif size selection.
- **Background Model**: Results depend on background sequence selection.

## Examples

### Discover motifs
**Args:** `aMeme -sequence input.fasta -output motifs.txt`
**Explanation:** Discover motifs in sequence file.

### With background
**Args:** `aMeme -sequence targets.fasta -bg background.fasta -o results/`
**Explanation:** Discover motifs with background sequences.
