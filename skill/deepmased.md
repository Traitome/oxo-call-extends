---
name: deepmased
category: qc
description: DeepMAsED - deep learning for metagenome assembly error detection.
tags: [deepmased, qc, metagenomics, deep-learning, assembly]
author: oxo-call-community
source_url: "https://github.com/leylabmpi/DeepMAsED"
---

## Concepts

- **Tool Overview**: deepmased (v0.3.1+) is a deep learning-based tool for detecting errors in metagenome assemblies. It identifies misassembled contigs and helps improve assembly quality.
- **Core Function**: Uses deep learning to analyze assembled contigs and read mappings to identify misassemblies, chimeras, and other assembly errors.
- **Input/Output**: Input: Assembled contigs (FASTA), read alignment (BAM). Output: Error predictions per contig, quality scores, visualization.
- **Algorithm**: Uses convolutional neural networks to learn patterns associated with assembly errors from read coverage and mapping information.
- **Key Features**: High accuracy, supports metagenomic data, integrates with assembly pipelines, provides confidence scores, visualization tools.
- **Installation**: `conda install -c bioconda deepmased`

## Pitfalls

- **Input Requirements**: Requires both assembly and read alignment data.
- **Contig Length**: Short contigs may produce unreliable predictions.
- **Mapping Quality**: Poor mapping quality affects accuracy.
- **Computational Resources**: Requires significant computational resources.
- **Training Data**: Performance depends on training dataset diversity.

## Examples

### Predict assembly errors
**Args:** `deepmased predict --assembly contigs.fa --bam alignment.bam --output results/`
**Explanation:** Predicts assembly errors from contigs and read mappings.

### With visualization
**Args:** `deepmased predict --assembly contigs.fa --bam alignment.bam --output results/ --visualize`
**Explanation:** Generate visualization of error predictions.

### Filter contigs by quality
**Args:** `deepmased filter --assembly contigs.fa --bam alignment.bam --output filtered.fa`
**Explanation:** Filter out misassembled contigs based on error predictions.