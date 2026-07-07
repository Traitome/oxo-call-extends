---
name: mira-moods
category: utility
description: "MOODS: Motif Occurrence Detection Suite"
tags: [mira-moods, utility, motif]
author: oxo-call-community
source_url: "https://www.cs.helsinki.fi/group/pssmfind/"
---
## Concepts

- **Tool Overview**: MIRA-MOODS v1.9.4.2 detects motif occurrences in sequences.
- **Core Function**: Identifies transcription factor binding sites and motifs.
- **Motif Detection**: Searches for sequence motifs in DNA/RNA sequences.
- **PSSM Scanning**: Uses position-specific scoring matrices for motif matching.
- **Input/Output**: Accepts sequence data; outputs motif locations.
- **Regulatory Analysis**: Supports gene regulatory element analysis.

## Pitfalls

- **Motif Specific**: Designed for motif analysis.
- **Computational Resources**: Scanning large genomes may require significant resources.
- **Memory Requirements**: Memory usage depends on sequence size.
- **Parameter Tuning**: May require parameter adjustment for optimal detection.
- **Data Quality**: Results depend on input sequence quality.
- **Motif Database**: Requires appropriate motif database.

## Examples

### Scan for motifs
**Args:** `mira-moods -i genome.fasta -m motifs.pwm -o hits.txt`
**Explanation:** Scans genome for motif occurrences.

### With custom threshold
**Args:** `mira-moods -i genome.fasta -m motifs.pwm -o hits.txt -t 0.8`
**Explanation:** Uses 0.8 threshold for motif matching.

### Multiple motifs
**Args:** `mira-moods -i genome.fasta -m motifs/ -o hits.txt`
**Explanation:** Scans with multiple motif files.

### Batch processing
**Args:** `mira-moods -i fasta/ -m motifs.pwm -o hits/`
**Explanation:** Processes multiple FASTA files.

### Generate statistics
**Args:** `mira-moods -i genome.fasta -m motifs.pwm -o hits.txt -s stats.txt`
**Explanation:** Generates motif detection statistics.