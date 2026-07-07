---
name: deepbgc
category: hpc
description: DeepBGC - Biosynthetic Gene Cluster detection and classification using deep learning.
tags: [deepbgc, hpc, BGC-detection, biosynthetic-gene-cluster, natural-products]
author: oxo-call-community
source_url: "https://github.com/Merck/DeepBGC"
---

## Concepts

- **Tool Overview**: deepbgc (v0.1.31+) is a deep learning-based tool for detecting and classifying Biosynthetic Gene Clusters (BGCs) in microbial genomes. It identifies clusters responsible for producing secondary metabolites.
- **Core Function**: Identifies and classifies BGCs in genomic sequences, enabling discovery of novel natural products with potential pharmaceutical applications.
- **Input/Output**: Input: Genomic sequences (FASTA), annotated genomes (GenBank). Output: BGC predictions, cluster boundaries, product class predictions, visualization.
- **Algorithm**: Uses deep neural networks to recognize patterns in gene clusters that indicate biosynthetic potential, including domain organization and sequence signatures.
- **Key Features**: High sensitivity, multiple BGC classes, boundary prediction, visualization tools, integrates with antiSMASH.
- **Installation**: `conda install -c bioconda deepbgc`

## Pitfalls

- **Novel Clusters**: May miss completely novel BGC architectures.
- **Genome Quality**: Requires high-quality genome assemblies.
- **False Positives**: May predict BGCs in non-biosynthetic regions.
- **Training Data**: Performance depends on diversity of training BGCs.
- **Computational Resources**: May require significant memory for large genomes.

## Examples

### Detect BGCs in genome
**Args:** `deepbgc predict -i genome.fasta -o bgc_predictions.gff`
**Explanation:** Detect and classify biosynthetic gene clusters in a genome.

### With visualization
**Args:** `deepbgc predict -i genome.fasta -o bgc_predictions.gff --visualize`
**Explanation:** Generate visualization of detected BGCs.

### Compare with antiSMASH
**Args:** `deepbgc compare -i bgc_predictions.gff -a antismash_results.gbk`
**Explanation:** Compare DeepBGC predictions with antiSMASH results.