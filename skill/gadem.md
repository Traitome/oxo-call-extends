---
name: gadem
category: formatting
description: A Genetic Algorithm Guided Formation of Spaced Dyads Coupled with an EM Algorithm for Motif Discovery.
tags: [gadem, motif discovery, genetic algorithm, transcription factor]
author: oxo-call-community
source_url: "https://www.niehs.nih.gov/research/resources/software/biostatistics/gadem/index.cfm"
---

## Concepts
- **Motif Discovery**: Identifies transcription factor binding motifs.
- **Genetic Algorithm**: Uses genetic algorithms for motif search.
- **EM Algorithm**: Employs expectation-maximization for optimization.
- **Spaced Dyads**: Detects spaced dyad patterns in sequences.
- **Statistical Scoring**: Uses statistical models for motif scoring.

## Pitfalls
- **Computational Complexity**: High computational requirements.
- **Parameter Sensitivity**: Results depend heavily on parameter settings.
- **Sequence Length**: May struggle with very long sequences.
- **Background Model**: Requires appropriate background model selection.
- **Multiple Testing**: Requires correction for multiple testing.

## Examples
### Discover motifs
**Args:** `gadem -i sequences.fasta -o motifs.txt`
**Explanation:** Discovers motifs in input sequences.

### With custom background
**Args:** `gadem -i sequences.fasta -b background.fasta -o motifs.txt`
**Explanation:** Uses custom background for motif discovery.

### Set motif length
**Args:** `gadem -i sequences.fasta -l 8-12 -o motifs.txt`
**Explanation:** Searches for motifs of length 8-12bp.

### Iterative search
**Args:** `gadem -i sequences.fasta -iter 3 -o motifs.txt`
**Explanation:** Runs 3 iterations of motif search.

### Output alignment
**Args:** `gadem -i sequences.fasta -align -o alignment.txt`
**Explanation:** Outputs motif alignment.