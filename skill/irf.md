---
name: irf
category: sequence-analysis
description: Inverted Repeats Finder - Detects approximate inverted repeats in DNA sequences
tags: [irf, sequence-analysis, repeats, palindromes, inverted-repeats]
author: oxo-call-community
source_url: "https://github.com/Benson-Genomics-Lab/IRF"
---

## Concepts

- **Tool Overview**: IRF (Inverted Repeats Finder) is a program for detecting approximate inverted repeats in DNA sequences.
- **Core Function**: Uses Smith-Waterman style local alignment with customizable scoring parameters to identify inverted repeats.
- **Input/Output**: Accepts FASTA format sequence files. Outputs repeat table and alignment files with detailed statistics.
- **Installation**: Download precompiled binaries from official website or build from source
- **Parameters**: Requires alignment scoring parameters (match, mismatch, indel) and probability thresholds for detection.
- **Biological Roles**: Inverted repeats form cruciform structures involved in DNA replication, transcription regulation, and genome stability.

## Pitfalls

- **Memory Usage**: Large MaxLength or MaxLoop parameters can consume significant memory resources.
- **Parameter Sensitivity**: Alignment scoring parameters significantly affect detection sensitivity and specificity.
- **False Positives**: Low MinScore thresholds may produce many false positive results requiring filtering.
- **Sequence Complexity**: Low-complexity regions or repetitive sequences can confound repeat detection.
- **Computation Time**: Detailed alignment options (-a3, -a4) significantly increase processing time.
- **Output File Size**: Large genomes can generate substantial output files requiring careful management.

## Examples

### Basic inverted repeat detection
**Args:** `irf genome.fasta 2 3 5 80 10 40 100000 500000`
**Explanation:** Detects inverted repeats with match=2, mismatch=3, indel=5, PM=80, PI=10, minScore=40, maxLength=100000, maxLoop=500000.

### Generate data file output
**Args:** `irf sequence.fasta 2 7 7 80 10 50 50000 200000 -d`
**Explanation:** Runs IRF with standard parameters and generates a detailed data file for downstream analysis.

### Allow GT pairing (RNA stem-loops)
**Args:** `irf rna_sequence.fasta 2 3 5 80 10 40 100000 500000 -gt`
**Explanation:** Enables GT base pairing for detecting RNA stem-loop structures in addition to standard Watson-Crick pairs.

### Detect mirror repeats
**Args:** `irf genome.fasta 2 3 5 80 10 40 100000 500000 -mr`
**Explanation:** Targets mirror repeats (inverted but not complemented sequences) for statistical background analysis.

### Stricter alignment parameters
**Args:** `irf sequence.fasta 2 7 7 80 10 60 100000 300000`
**Explanation:** Uses stricter mismatch and indel penalties (7 each) and higher minScore (60) for more stringent detection.

### Suppress HTML output
**Args:** `irf genome.fasta 2 3 5 80 10 40 100000 500000 -h`
**Explanation:** Runs IRF without generating HTML output, only producing the data file and alignment files.