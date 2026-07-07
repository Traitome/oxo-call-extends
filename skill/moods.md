---
name: moods
category: utility
description: "MOODS: Motif Occurrence Detection Suite"
tags: [moods, utility, motif]
author: oxo-call-community
source_url: "https://www.cs.helsinki.fi/group/pssmfind"
---
## Concepts

- **Tool Overview**: MOODS v1.9.4.2 detects motif occurrences in DNA sequences.
- **Core Function**: Searches for sequence motifs using position-specific scoring matrices.
- **Motif Detection**: Identifies transcription factor binding sites.
- **PSSM-based**: Uses position-specific scoring matrices for searching.
- **Multiple Motifs**: Supports simultaneous search for multiple motifs.
- **Input/Output**: Accepts FASTA sequences; outputs motif positions.

## Pitfalls

- **Motif Specific**: Designed for motif search.
- **Memory Requirements**: Memory usage depends on sequence length.
- **Parameter Tuning**: May require threshold adjustment for sensitivity.
- **Data Quality**: Results depend on sequence quality.
- **False Positives**: May produce false positive matches.
- **Computational Resources**: Large sequences may require significant resources.

## Examples

### Search for motifs
**Args:** `moods search -i sequence.fasta -m motifs.pwm -o results.txt`
**Explanation:** Searches for motif occurrences.

### With custom threshold
**Args:** `moods search -i sequence.fasta -m motifs.pwm -t 0.9 -o results.txt`
**Explanation:** Uses custom score threshold.

### Scan genome
**Args:** `moods scan -i genome.fasta -m motifs.pwm -o results.txt`
**Explanation:** Scans entire genome for motifs.

### Batch processing
**Args:** `moods search -i fasta/ -m motifs.pwm -o results/`
**Explanation:** Processes multiple sequence files.

### Generate PSSM
**Args:** `moods pssm -i aligned_sequences.fasta -o motif.pwm`
**Explanation:** Creates position-specific scoring matrix.