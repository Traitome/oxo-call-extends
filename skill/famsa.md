---
name: famsa
category: alignment
description: "Algorithm for large-scale multiple sequence alignments."
tags: [famsa, alignment, multiple-sequence-alignment, bioinformatics, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/FAMSA"
---

## Concepts

- **Tool Overview**: FAMSA is a fast and accurate algorithm for large-scale multiple sequence alignments.
- **Core Function**: Aligns large sets of sequences efficiently, suitable for thousands of sequences.
- **Input/Output**: Input: Sequences (FASTA). Output: Multiple sequence alignment (FASTA/Clustal).
- **Algorithm**: Uses a progressive alignment approach with efficient heuristics for large datasets.
- **Key Features**: Scalable to thousands of sequences, high accuracy, fast performance, multiple output formats, support for protein and DNA sequences.
- **Installation**: `conda install -c bioconda famsa`

## Pitfalls

- **Memory Usage**: Large alignments may require significant memory.
- **Sequence Diversity**: Highly divergent sequences may affect alignment quality.
- **Computation Time**: Very large datasets may require substantial processing time.
- **Format Compatibility**: Requires standard FASTA format.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic multiple sequence alignment
**Args:** `famsa input.fasta output.fasta`
**Explanation:** Aligns sequences in input file.

### Protein alignment
**Args:** `famsa --protein proteins.fasta aligned.fasta`
**Explanation:** Performs protein sequence alignment.

### DNA alignment
**Args:** `famsa --dna dna.fasta aligned.fasta`
**Explanation:** Performs DNA sequence alignment.

### Fast mode
**Args:** `famsa --fast input.fasta output.fasta`
**Explanation:** Uses fast mode for large datasets.

### Output in Clustal format
**Args:** `famsa --clustal input.fasta output.clustal`
**Explanation:** Outputs alignment in Clustal format.