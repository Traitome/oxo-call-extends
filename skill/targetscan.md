---
name: targetscan
category: ncrna-analysis
description: Predicted microRNA targets in mammals.
tags: [targetscan, mirna, microrna, mammals]
author: oxo-call-community
source_url: "https://www.targetscan.org/vert_80/"
---

## Concepts

- **Tool Overview**: targetscan (v7.0) predicts microRNA targets in mammals.
- **Core Function**: Identifies conserved miRNA target sites.
- **Algorithm**: Uses context++ scores and seed matching.
- **Input/Output**: Input: miRNA and mRNA sequences; Output: Predicted targets.
- **Applications**: miRNA research, gene regulation, cancer studies.
- **Installation**: `conda install -c bioconda targetscan` or download from website.

## Pitfalls

- **Conservation Filter**: Requires conserved target sites.
- **Context Scores**: Incorrect context parameters affect ranking.
- **Species Specificity**: Optimized for mammalian species.
- **Multiple Isoforms**: May predict targets for multiple isoforms.
- **False Positives**: May include non-functional targets.
- **Database Updates**: Requires updated seed matches.

## Examples

### Display help
**Args:** `targetscan --help`
**Explanation:** Shows available options and usage information.

### Basic target prediction
**Args:** `targetscan -i mirnas.fasta -t 3utrs.fasta -o targets.txt`
**Explanation:** Predict miRNA targets from 3' UTRs.

### With context scores
**Args:** `targetscan -i mirnas.fasta -t 3utrs.fasta -o targets.txt -c`
**Explanation:** Include context++ scores.

### Verbose mode
**Args:** `targetscan -i mirnas.fasta -t 3utrs.fasta -o targets.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `targetscan -i mirnas.fasta -t 3utrs.fasta -o targets.txt --stats`
**Explanation:** Generate statistics about predictions.

### Batch processing
**Args:** `for f in mirna/*.fasta; do targetscan -i $f -t 3utrs.fasta -o results/${f%.fasta}_targets.txt; done`
**Explanation:** Process multiple miRNA files.

### Filter by score
**Args:** `targetscan -i mirnas.fasta -t 3utrs.fasta -o targets.txt -s 90`
**Explanation:** Minimum cumulative weighted context++ score.

### Conservation analysis
**Args:** `targetscan -i mirnas.fasta -t 3utrs.fasta -o targets.txt --conserved`
**Explanation:** Only conserved targets.

### Generate report
**Args:** `targetscan -i mirnas.fasta -t 3utrs.fasta -o targets.txt --report`
**Explanation:** Generate comprehensive target report.
