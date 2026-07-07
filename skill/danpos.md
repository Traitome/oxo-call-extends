---
name: danpos
category: utility
description: DANPOS - Dynamic Analysis of Nucleosome and Protein Occupancy by Sequencing v2
tags: [danpos, utility, nucleosome, ChIP-seq, protein-occupancy]
author: oxo-call-community
source_url: "https://sites.google.com/site/danposdoc/"
---

## Concepts

- **Tool Overview**: danpos (v2.2.2+) is a toolkit for dynamic analysis of nucleosome and protein occupancy from sequencing data.
- **Core Function**: Analyzes nucleosome positioning and protein binding from ChIP-seq, MNase-seq, and related protocols.
- **Input/Output**: Input: BAM alignments, genome sequence. Output: Position files, occupancy scores, statistics.
- **Algorithm**: Uses smoothed signal extraction and statistical testing for nucleosome/protein detection.
- **Key Features**: Handles multiple assay types, identifies binding positions, calculates occupancy.
- **Installation**: `conda install -c bioconda danpos`

## Pitfalls

- **Fragment Size**: Accurate fragment size estimation is critical for occupancy calculation.
- **Background Correction**: Proper background normalization required for accurate results.
- **Input Format**: Requires properly formatted BAM files and genome sequences.
- **Parameter Selection**: Peak-calling parameters affect detection sensitivity.
- **Multiple Testing**: Statistical correction needed for large-scale comparisons.

## Examples

### Identify nucleosome positions
**Args:** `danpos dpeak -i aligned.bam -r genome.fasta -o results/`
**Explanation:** Identify nucleosome positions from aligned sequencing data.

### Calculate protein occupancy
**Args:** `danpos occupancy -i chip.bam -c input.bam -o occupancy.txt`
**Explanation:** Calculate protein binding occupancy with input control normalization.

### Differential analysis
**Args:** `danpos compare -s sample1.bam -s sample2.bam -o diff_results/`
**Explanation:** Compare nucleosome or protein occupancy between samples.
