---
name: dnp-corrprofile
category: utility
description: DNPattern tools - Correlation profile analysis of dinucleotide frequency patterns.
tags: [dnp-corrprofile, utility, dinucleotide, correlation-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/erinijapranckeviciene/dnpatterntools"
---

## Concepts

- **Tool Overview**: dnp-corrprofile computes correlation profiles of dinucleotide frequency patterns.
- **Core Function**: Calculates correlations between dinucleotide frequencies on forward and reverse strands.
- **Input/Output**: Input: FASTA DNA sequences. Output: Correlation matrices, profile statistics.
- **Algorithm**: Uses statistical methods to measure correlation between dinucleotide patterns.
- **Key Features**: Strand correlation analysis, statistical profiling, pattern comparison, visualization-ready output.
- **Installation**: `conda install -c bioconda dnp-corrprofile`

## Pitfalls

- **Input Requirements**: Requires DNA sequences in FASTA format.
- **Sequence Quality**: Poor quality sequences with many Ns affect correlation calculations.
- **Strand Bias**: Natural strand biases may affect correlation measurements.
- **Output Interpretation**: Correlation values require careful interpretation.
- **Computation Time**: Large genomes may require significant processing time.
- **Memory Usage**: Correlation matrices for large datasets can be memory-intensive.

## Examples

### Compute correlation profiles
**Args:** `dnp-corrprofile --input sequences.fa --output correlations.tsv`
**Explanation:** Calculates dinucleotide frequency correlations between strands.

### With window analysis
**Args:** `dnp-corrprofile --input sequences.fa --output correlations.tsv --window 1000`
**Explanation:** Computes correlations in sliding windows of 1000bp.

### Compare multiple sequences
**Args:** `dnp-corrprofile --input seq1.fa seq2.fa seq3.fa --output comparison.tsv`
**Explanation:** Compares correlation profiles across multiple sequences.

### Output matrix format
**Args:** `dnp-corrprofile --input sequences.fa --output matrix.tsv --matrix`
**Explanation:** Outputs full correlation matrix instead of summary statistics.

### Include p-values
**Args:** `dnp-corrprofile --input sequences.fa --output correlations.tsv --pvalues`
**Explanation:** Includes statistical significance values in the output.

### Generate heatmap data
**Args:** `dnp-corrprofile --input sequences.fa --output heatmap.tsv --heatmap`
**Explanation:** Generates data suitable for correlation heatmap visualization.