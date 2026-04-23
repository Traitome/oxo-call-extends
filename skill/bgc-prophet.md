---
name: bgc-prophet
category: annotation
description: Deep learning tool for identifying and classifying Biosynthetic Gene Clusters
tags: [bgc, biosynthetic-gene-cluster, deep-learning, secondary-metabolites]
author: oxo-call-community
source_url: "https://github.com/HUST-NingKang-Lab/BGC-Prophet"
---

## Concepts
- **Tool Overview**: BGC-Prophet is a deep learning tool for identifying and classifying Biosynthetic Gene Clusters (BGCs) using language processing neural networks. BGCs are gene clusters that encode biosynthetic pathways for secondary metabolites.
- **Deep Learning**: Uses neural network models trained on known BGC sequences to predict novel BGCs in genomic data.
- **Classification**: Categorizes predicted BGCs into known classes (NRPS, PKS, RiPP, terpene, etc.) based on biosynthetic pathway type.
- **Applications**: Drug discovery, natural product research, microbiome analysis.

## Pitfalls
- **Model Requirements**: Requires pre-trained models for prediction.
- **Input Format**: Expects properly formatted genomic sequences or gene annotations.
- **False Positives**: Deep learning predictions may include false positives requiring experimental validation.

## Examples
### Predict BGCs from genome
**Args:** `bgc-prophet predict -i genome.fasta -o predictions.tsv`
**Explanation:** Predicts biosynthetic gene clusters in a genomic sequence.

### Classify BGC types
**Args:** `bgc-prophet classify -i bgc_regions.fasta -o classifications.tsv`
**Explanation:** Classifies predicted BGCs into biosynthetic pathway types.
