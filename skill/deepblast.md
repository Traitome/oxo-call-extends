---
name: deepblast
category: alignment
description: DeepBLAST - neural network based protein sequence alignment.
tags: [deepblast, alignment, protein-alignment, deep-learning, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/flatironinstitute/deepblast"
---

## Concepts

- **Tool Overview**: deepblast (v1.0.2+) is a deep learning-based tool for protein sequence alignment that uses neural networks to improve alignment accuracy and speed.
- **Core Function**: Aligns protein sequences using deep learning models that capture complex evolutionary relationships and sequence patterns.
- **Input/Output**: Input: Protein sequences (FASTA). Output: Alignments, similarity scores, evolutionary distance estimates.
- **Algorithm**: Uses transformer-based neural networks to model sequence relationships and predict accurate alignments.
- **Key Features**: Deep learning-based alignment, improved accuracy for remote homologs, fast inference, supports multiple sequence alignment.
- **Installation**: `conda install -c bioconda deepblast`

## Pitfalls

- **Computational Resources**: Requires GPU for optimal performance.
- **Training Data**: Performance depends on training dataset diversity.
- **Sequence Length**: May struggle with very long sequences.
- **Gap Penalties**: Default parameters may need adjustment.
- **Homology Detection**: May miss very distant homologs.

## Examples

### Align two proteins
**Args:** `deepblast -i query.fasta -d target.fasta -o alignment.txt`
**Explanation:** Align query protein against target database.

### Multiple sequence alignment
**Args:** `deepblast msa -i sequences.fasta -o msa.fasta`
**Explanation:** Perform multiple sequence alignment.

### With custom model
**Args:** `deepblast -i query.fasta -d target.fasta -m custom_model.pt -o alignment.txt`
**Explanation:** Use custom trained model for alignment.