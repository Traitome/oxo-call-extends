---
name: dpcstruct
category: metagenomics
description: "Unsupervised clustering algorithm for identifying and classifying protein domains based on structural similarity."
tags: [dpcstruct, metagenomics, protein-domains, structural-clustering]
author: oxo-call-community
source_url: "https://github.com/RitAreaSciencePark/DPCstruct"
---

## Concepts

- **Tool Overview**: DPCstruct is an unsupervised clustering algorithm for identifying and classifying protein domains based on structural similarity.
- **Core Function**: Groups protein sequences into structurally similar clusters without prior annotation.
- **Input/Output**: Input: Protein sequences (FASTA). Output: Cluster assignments, structural similarity matrices.
- **Algorithm**: Uses dynamic programming and structural alignment for clustering.
- **Key Features**: Unsupervised learning, structural similarity metrics, hierarchical clustering, visualization support.
- **Installation**: `conda install -c bioconda dpcstruct`

## Pitfalls

- **Sequence Length**: Very short sequences may not contain enough structural information.
- **Computational Complexity**: Large datasets can be computationally intensive.
- **Structural Noise**: Low-quality structures can affect clustering accuracy.
- **Parameter Sensitivity**: Clustering results may vary with different distance thresholds.
- **Memory Requirements**: Large alignments may require significant memory.

## Examples

### Basic clustering
**Args:** `--input proteins.fasta --output clusters.txt`
**Explanation:** Clusters protein sequences based on structural similarity.

### Generate similarity matrix
**Args:** `--input proteins.fasta --output matrix.txt --matrix`
**Explanation:** Computes and outputs pairwise structural similarity matrix.

### Hierarchical clustering
**Args:** `--input proteins.fasta --output clusters.txt --hierarchical`
**Explanation:** Performs hierarchical clustering of protein domains.

### Visualization
**Args:** `--input proteins.fasta --output clusters.txt --plot dendrogram.png`
**Explanation:** Generates a dendrogram visualization of clustering results.

### Custom distance threshold
**Args:** `--input proteins.fasta --output clusters.txt --threshold 0.7`
**Explanation:** Sets custom similarity threshold (0.7) for cluster formation.