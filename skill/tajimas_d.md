---
name: tajimas_d
category: population-genetics
description: Computes Tajima's D, Pi, and Watterson's estimator for population genetics analysis.
tags: [tajimas_d, population-genetics, statistics, dna-sequences]
author: oxo-call-community
source_url: "https://github.com/not-a-feature/tajimas_d/blob/v2.0.4/README.md"
---

## Concepts

- **Tool Overview**: tajimas_d (v2.0.4) computes population genetics statistics.
- **Core Function**: Calculates Tajima's D, Pi, and Watterson's estimator.
- **Algorithm**: Implements standard population genetics formulas.
- **Input/Output**: Input: FASTA/FASTQ files; Output: Statistical values.
- **Applications**: Population genetics, evolutionary biology, SNP analysis.
- **Installation**: `conda install -c bioconda tajimas_d` or download from GitHub.

## Pitfalls

- **Sequence Quality**: Requires high-quality sequences.
- **Sample Size**: Results depend on sample size.
- **Population Model**: Assumes specific population models.
- **Recombination**: Ignores recombination events.
- **Selection**: Assumes neutral evolution.
- **Missing Data**: Missing sites affect calculations.

## Examples

### Display help
**Args:** `tajimas_d --help`
**Explanation:** Shows available options and usage information.

### Basic Tajima's D calculation
**Args:** `tajimas_d -i sequences.fasta -o results.txt`
**Explanation:** Calculate Tajima's D from aligned sequences.

### Calculate Pi
**Args:** `tajimas_d -i sequences.fasta -o results.txt -m pi`
**Explanation:** Calculate nucleotide diversity (Pi).

### Verbose mode
**Args:** `tajimas_d -i sequences.fasta -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tajimas_d -i sequences.fasta -o results.txt --stats`
**Explanation:** Generate comprehensive statistics.

### Batch processing
**Args:** `for f in fasta/*.fasta; do tajimas_d -i $f -o results/${f%.fasta}_stats.txt; done`
**Explanation:** Process multiple sequence files.

### Include Watterson's estimator
**Args:** `tajimas_d -i sequences.fasta -o results.txt -m all`
**Explanation:** Calculate all statistics (Tajima's D, Pi, Watterson).

### Filter by quality
**Args:** `tajimas_d -i sequences.fasta -o results.txt -q 20`
**Explanation:** Filter low-quality sites.

### Generate report
**Args:** `tajimas_d -i sequences.fasta -o results.txt --report`
**Explanation:** Generate comprehensive analysis report.
