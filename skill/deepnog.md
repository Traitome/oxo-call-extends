---
name: deepnog
category: annotation
description: deepNOG - deep learning tool for protein orthologous group assignment.
tags: [deepnog, annotation, orthologs, deep-learning, eggNOG]
author: oxo-call-community
source_url: "https://github.com/univieCUBE/deepnog"
---

## Concepts

- **Tool Overview**: deepnog (v1.2.4+) is a deep learning-based tool for fast protein orthologous group assignment using the eggNOG database. It provides faster classification than traditional HMM approaches.
- **Core Function**: Assigns protein sequences to orthologous groups in eggNOG using deep neural networks, enabling functional annotation and evolutionary analysis.
- **Input/Output**: Input: Protein FASTA files. Output: Orthologous group assignments, functional annotations, confidence scores.
- **Algorithm**: Uses deep neural networks to classify proteins into eggNOG orthologous groups based on sequence features.
- **Key Features**: Fast inference, high accuracy, supports multiple taxonomic levels, integrates with eggNOG database, batch processing.
- **Installation**: `conda install -c bioconda deepnog`

## Pitfalls

- **Sequence Quality**: Requires good quality protein sequences.
- **Database Compatibility**: Must use compatible eggNOG database version.
- **Novel Sequences**: May struggle with completely novel sequences.
- **Computational Resources**: Requires GPU for optimal performance.
- **Memory Usage**: May require significant memory for large inputs.

## Examples

### Classify proteins into orthologous groups
**Args:** `deepnog classify --input proteins.fa --output assignments.tsv`
**Explanation:** Assigns protein sequences to eggNOG orthologous groups.

### With confidence threshold
**Args:** `deepnog classify --input proteins.fa --output assignments.tsv --confidence 0.9`
**Explanation:** Filter results to only include high-confidence assignments.

### Batch processing
**Args:** `deepnog classify --input proteins_dir/ --output assignments/`
**Explanation:** Process multiple FASTA files in batch.