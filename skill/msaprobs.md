---
name: msaprobs
category: alignment
description: State-of-the-art multiple sequence alignment algorithm for protein sequences.
tags: [msaprobs, alignment, phylogenetics]
author: oxo-call-community
source_url: "https://msaprobs.sourceforge.net/homepage.htm#latest"
---

## Concepts

- **Tool Overview**: MSAProbs v0.9.7 performs accurate protein sequence alignment.
- **Core Function**: Aligns protein sequences using probabilistic models.
- **Stochastic Algorithms**: Uses stochastic optimization methods.
- **High Accuracy**: Known for state-of-the-art alignment accuracy.
- **Protein Sequences**: Specialized for protein alignment.
- **Input/Output**: Accepts protein sequences; outputs alignments.

## Pitfalls

- **Protein Only**: Designed for protein sequences only.
- **Memory Requirements**: Memory usage depends on sequence count.
- **Computational Time**: Accurate alignment can be slow for large datasets.
- **Parameter Tuning**: May require parameter adjustment for optimization.
- **Sequence Similarity**: Performance varies with sequence similarity.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Align protein sequences
**Args:** `msaprobs -i proteins.fasta -o alignment.fasta`
**Explanation:** Performs protein sequence alignment.

### With multiple iterations
**Args:** `msaprobs -i proteins.fasta -i 5 -o alignment.fasta`
**Explanation:** Uses 5 optimization iterations.

### Output in CLUSTAL format
**Args:** `msaprobs -i proteins.fasta -o alignment.aln -f clustal`
**Explanation:** Outputs in CLUSTAL format.

### With CPU threads
**Args:** `msaprobs -i proteins.fasta -t 8 -o alignment.fasta`
**Explanation:** Uses 8 CPU threads.

### Batch processing
**Args:** `msaprobs -i fasta/ -o alignments/`
**Explanation:** Processes multiple sequence files.