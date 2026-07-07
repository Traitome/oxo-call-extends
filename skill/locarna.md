---
name: locarna
category: alignment
description: LocARNA - Multiple alignment of RNA sequences
tags: [locarna, alignment, RNA, multiple-alignment, structural-alignment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/s-will/LocARNA"
---

## Concepts

- **RNA Alignment**: Multiple alignment of RNA sequences
- **Structural Alignment**: Considers RNA secondary structure
- **Sequence Comparison**: Compares RNA sequences
- **Homology Detection**: Detects homologous RNA sequences
- **Secondary Structure**: Incorporates RNA secondary structure information
- **Multiple Sequences**: Aligns multiple RNA sequences

## Pitfalls

- **Sequence Quality**: Poor quality sequences affect alignment
- **Structure Prediction**: Requires accurate secondary structure prediction
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Memory Usage**: Memory-intensive for large datasets
- **Alignment Accuracy**: May produce suboptimal alignments

## Examples

### Align RNA sequences
**Args:** `locarna -i rna_sequences.fasta -o alignment.sto`
**Explanation:** Aligns multiple RNA sequences.

### Structural alignment
**Args:** `locarna -i rna_sequences.fasta -o alignment.sto -s`
**Explanation:** Performs structural alignment considering secondary structure.

### Threads
**Args:** `locarna -i rna_sequences.fasta -o alignment.sto -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `locarna -i rna_sequences.fasta -o alignment.clustal -f clustal`
**Explanation:** Outputs alignment in Clustal format.

### Consensus structure
**Args:** `locarna -i rna_sequences.fasta -o alignment.sto -c`
**Explanation:** Computes consensus secondary structure.

### Verbose output
**Args:** `locarna -i rna_sequences.fasta -o alignment.sto -v`
**Explanation:** Provides detailed output.