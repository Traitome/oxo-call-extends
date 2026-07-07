---
name: magus-msa
category: alignment
description: Multiple Sequence Alignment using Graph Clustering
tags: [magus-msa, alignment, multiple-sequence-alignment, graph-clustering]
author: oxo-call-community
source_url: "https://github.com/vlasmirnov/MAGUS"
---

## Concepts

- **Tool Overview**: magus-msa v0.2.0 - MAGUS (Multiple Alignment using Graph Clustering) is a multiple sequence alignment tool that uses graph-based clustering for improved accuracy.
- **Core Function**: Constructs alignments using graph clustering of sequences to handle large datasets efficiently.
- **Input/Output**: Input: FASTA sequence files; Output: Aligned sequences in various formats.
- **Installation**: `conda install -c bioconda magus-msa`
- **Graph-based Approach**: Uses graph clustering to group similar sequences before alignment.
- **Scalability**: Designed to handle large sequence datasets efficiently.

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **Time Complexity**: Graph construction can be computationally intensive.
- **Parameter Tuning**: Incorrect clustering parameters affect alignment quality.
- **Sequence Diversity**: Highly divergent sequences may not cluster well.
- **Output Format**: Limited output format options compared to other aligners.
- **Reference Sequence**: Requires appropriate reference sequences for alignment.

## Examples

### Basic alignment
**Args:** `magus -i input.fasta -o aligned.fasta`
**Explanation:** Performs multiple sequence alignment.

### With guide tree
**Args:** `magus -i input.fasta -o aligned.fasta -t tree.newick`
**Explanation:** Uses custom guide tree for alignment.

### Fast mode
**Args:** `magus -i input.fasta -o aligned.fasta --fast`
**Explanation:** Runs in fast mode for large datasets.

### Output in Clustal format
**Args:** `magus -i input.fasta -o aligned.clustal -f clustal`
**Explanation:** Outputs alignment in Clustal format.

### With custom k-mer size
**Args:** `magus -i input.fasta -o aligned.fasta -k 15`
**Explanation:** Uses k-mer size of 15 for clustering.

### Verbose mode
**Args:** `magus -i input.fasta -o aligned.fasta -v`
**Explanation:** Provides detailed logging during alignment.