---
name: danpos3
category: utility
description: DANPOS - Dynamic Analysis of Nucleosome Positioning and Occupancy by Sequencing
tags: [danpos3, utility, nucleosome, ChIP-seq, MNase-seq]
author: oxo-call-community
source_url: "https://github.com/boenc28-cmyk/DANPOS"
---

## Concepts

- **Tool Overview**: danpos3 (v3.2.3+) is a toolkit for dynamic analysis of nucleosome positioning and occupancy from sequencing data.
- **Core Function**: Identifies and analyzes nucleosome positions and occupancy levels from MNase-seq, ChIP-seq, or ATAC-seq data.
- **Input/Output**: Input: BAM alignments, genome. Output: Nucleosome positions, occupancy scores, visualization.
- **Algorithm**: Uses peak-calling and smoothing algorithms to identify nucleosome dyads.
- **Key Features**: Dynamic analysis, handles multiple sequencing protocols, differential occupancy detection.
- **Installation**: `conda install -c bioconda danpos3`

## Pitfalls

- **Fragment Size**: Requires appropriate fragment size selection for nucleosome analysis.
- **Background Normalization**: Proper background estimation is critical.
- **Sequencing Depth**: Adequate coverage needed for accurate nucleosome detection.
- **Peak Calling**: Results depend on peak-calling parameters.
- **Cross-platform**: May behave differently across sequencing platforms.

## Examples

### Identify nucleosome positions
**Args:** `danpos3 dpeak -i aligned.bam -r genome.fasta -o nucleosome_results/`
**Explanation:** Identify nucleosome positions from aligned reads.

### Calculate occupancy
**Args:** `danpos3 occupancy -i treatment.bam -c control.bam -o occupancy.tsv`
**Explanation:** Calculate nucleosome occupancy with background normalization.

### Differential analysis
**Args:** `danpos3 compare -i sample1.bam sample2.bam -o comparison/`
**Explanation:** Compare nucleosome positioning between samples.
