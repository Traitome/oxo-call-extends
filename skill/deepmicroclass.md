---
name: deepmicroclass
category: metagenomics
description: DeepMicroClass - deep learning based contig classification tool (CPU version).
tags: [deepmicroclass, metagenomics, classification, deep-learning, contig]
author: oxo-call-community
source_url: "https://github.com/chengsly/DeepMicroClass"
---

## Concepts

- **Tool Overview**: deepmicroclass (v1.0.3+) is a deep learning-based tool for classifying metagenomic contigs by their origin (prokaryote, eukaryote, virus, etc.). It runs efficiently on CPU.
- **Core Function**: Classifies metagenomic contigs into taxonomic or functional categories using deep learning models.
- **Input/Output**: Input: FASTA contigs. Output: Classification results per contig, confidence scores, taxonomic assignments.
- **Algorithm**: Uses deep neural networks trained on known sequences to classify contigs based on sequence composition and patterns.
- **Key Features**: CPU optimized, supports multiple taxonomic levels, high accuracy, batch processing, confidence scoring.
- **Installation**: `conda install -c bioconda deepmicroclass`

## Pitfalls

- **Contig Length**: Short contigs may produce unreliable classifications.
- **Training Data**: Performance depends on training dataset diversity.
- **Computational Time**: CPU-only processing may be slow for large datasets.
- **Novel Sequences**: May struggle with completely novel sequences.
- **Memory Usage**: May require significant memory for large inputs.

## Examples

### Classify metagenomic contigs
**Args:** `deepmicroclass predict --input contigs.fa --output classifications.tsv`
**Explanation:** Classifies metagenomic contigs by their likely origin.

### With confidence threshold
**Args:** `deepmicroclass predict --input contigs.fa --output classifications.tsv --confidence 0.9`
**Explanation:** Filter results to only include high-confidence classifications.

### Batch processing
**Args:** `deepmicroclass predict --input contigs_dir/ --output classifications/`
**Explanation:** Process multiple FASTA files in batch.