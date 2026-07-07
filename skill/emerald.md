---
name: emerald
category: alignment
description: "Unlocking the suboptimal pairwise alignment space for protein sequences"
tags: [emerald, alignment, protein-sequences, suboptimal-alignment, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/algbio/emerald"
---

## Concepts

- **Tool Overview**: Emerald is a bioinformatics tool for exploring suboptimal pairwise alignments of protein sequences, providing insights into alternative alignment solutions.
- **Core Function**: Identifies and analyzes multiple suboptimal alignments between protein sequences, revealing biologically meaningful alternative alignment paths.
- **Input/Output**: Input: Protein sequences (FASTA). Output: Multiple suboptimal alignments, alignment scores, visualization of alignment space.
- **Algorithm**: Uses dynamic programming with gap penalty optimization to explore the alignment landscape beyond the single optimal solution.
- **Key Features**: Suboptimal alignment discovery, alignment space visualization, scoring metrics, biological relevance assessment, comparative analysis.
- **Installation**: `conda install -c bioconda emerald`

## Pitfalls

- **Computation Time**: Exploring suboptimal alignments can be computationally intensive.
- **Result Interpretation**: Multiple solutions require careful biological interpretation.
- **Parameter Tuning**: Gap penalties and scoring matrices significantly affect results.
- **Memory Usage**: Large sequences may require substantial memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic suboptimal alignment
**Args:** `emerald -i seq1.fasta seq2.fasta -o alignments.txt`
**Explanation:** Finds suboptimal alignments between two protein sequences.

### With specific number of solutions
**Args:** `emerald -i seq1.fasta seq2.fasta -n 10 -o alignments.txt`
**Explanation:** Returns top 10 suboptimal alignments.

### Output alignment scores
**Args:** `emerald -i seq1.fasta seq2.fasta -s -o scores.txt`
**Explanation:** Outputs alignment scores for all discovered solutions.

### Visualize alignment space
**Args:** `emerald -i seq1.fasta seq2.fasta -v -o alignment_plot.pdf`
**Explanation:** Generates visualization of alignment space.

### Compare multiple sequences
**Args:** `emerald -i sequences.fasta -o multi_alignments.txt`
**Explanation:** Performs pairwise suboptimal alignment for multiple sequences.