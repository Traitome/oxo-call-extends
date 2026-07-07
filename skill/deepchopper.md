---
name: deepchopper
category: metagenomics
description: DeepChopper - genomic language model for chimera artifact detection in Nanopore Direct RNA sequencing.
tags: [deepchopper, metagenomics, chimera-detection, nanopore, RNA-seq]
author: oxo-call-community
source_url: "https://github.com/ylab-hi/DeepChopper"
---

## Concepts

- **Tool Overview**: deepchopper (v1.2.9+) is a genomic language model designed to detect chimera artifacts in Nanopore Direct RNA sequencing data using deep learning.
- **Core Function**: Identifies artificial chimeric sequences that arise during library preparation or sequencing.
- **Input/Output**: Input: FASTQ reads, optionally FASTA reference. Output: Chimera predictions, filtered reads, visualization.
- **Algorithm**: Uses transformer architecture trained on known chimeric and non-chimeric sequences to classify reads.
- **Key Features**: Genomic language model, chimera detection, supports Direct RNA sequencing, high accuracy, interpretable results.
- **Installation**: `conda install -c bioconda deepchopper`

## Pitfalls

- **RNA-specific**: Optimized for RNA sequencing data.
- **Computational Resources**: Requires significant computational resources.
- **Model Size**: Large models may require GPU memory.
- **Training Data**: Performance depends on training dataset diversity.
- **False Positives**: May incorrectly classify some sequences.

## Examples

### Basic chimera detection
**Args:** `deepchopper predict -i reads.fastq -o predictions.csv`
**Explanation:** Predict chimeric sequences in reads.

### Filter reads
**Args:** `deepchopper filter -i reads.fastq -o clean_reads.fastq`
**Explanation:** Filter out chimeric sequences from reads.

### Train custom model
**Args:** `deepchopper train -i training_data/ -o custom_model/`
**Explanation:** Train custom chimera detection model.