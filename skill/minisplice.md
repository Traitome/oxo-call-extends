---
name: minisplice
category: alignment
description: minisplice is a command-line tool to estimate the odds-ratio score of canonical donor (GT) and acceptor (AG) splice sites. It is intended to be used with miniprot or minimap2 for improving alignment accuracy especially for distant homologs.
tags: [minisplice, alignment, splicing]
author: oxo-call-community
source_url: "https://github.com/lh3/minisplice"
---

## Concepts

- **Tool Overview**: MiniSplice v0.4 scores canonical splice sites.
- **Core Function**: Estimates odds-ratio scores for splice sites.
- **Splice Site Prediction**: Identifies donor (GT) and acceptor (AG) sites.
- **Odds-ratio Scoring**: Assigns statistical scores to splice sites.
- **Input/Output**: Accepts sequence data; outputs splice site scores.
- **Alignment Improvement**: Enhances alignment accuracy for distant homologs.

## Pitfalls

- **Splice Site Specific**: Designed for splice site analysis.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on input size.
- **Parameter Tuning**: May require parameter adjustment for optimal scoring.
- **Data Quality**: Results depend on input sequence quality.
- **Canonical Sites**: Focuses on GT-AG splice sites.

## Examples

### Score splice sites
**Args:** `minisplice -i genome.fasta -o scores.txt`
**Explanation:** Scores splice sites in genome sequence.

### With custom model
**Args:** `minisplice -i genome.fasta -o scores.txt -m model.txt`
**Explanation:** Uses custom splice site model.

### Output probabilities
**Args:** `minisplice -i genome.fasta -o scores.txt -p`
**Explanation:** Outputs probability scores.

### Batch processing
**Args:** `minisplice -i fasta/ -o scores/`
**Explanation:** Processes multiple FASTA files.

### Filter by score
**Args:** `minisplice -i genome.fasta -o scores.txt -t 0.7`
**Explanation:** Filters results by score threshold.