---
name: graphclust-wrappers
category: bioinformatics
description: graphclust-wrappers provides individual Perl wrappers extracted from the GraphClust pipeline for RNA family analysis.
tags: [graphclust-wrappers, RNA-analysis, bioinformatics]
author: oxo-call-community
source_url: "http://www.bioinf.uni-freiburg.de/Software/GraphClust/"
---

## Concepts

- **RNA Family Analysis**: graphclust-wrappers tools analyze and cluster non-coding RNA sequences into families.

- **Graph-Based Clustering**: Uses graph-based approaches to identify structurally similar RNA sequences.

- **Multiple Sequence Alignment**: Generates alignments of RNA sequences within each cluster.

- **Consensus Structure Prediction**: Predicts consensus secondary structures for RNA families.

- **Annotation Integration**: Integrates with RNA annotation databases for functional analysis.

- **Quality Control**: Provides metrics for assessing clustering quality and confidence.

## Pitfalls

- **Sequence Quality**: Low-quality sequences can produce incorrect clustering results.

- **Parameter Tuning**: Adjust parameters based on RNA type and dataset characteristics.

- **Computational Resources**: Processing large RNA datasets may require significant memory.

- **Database Compatibility**: Ensure compatibility with reference databases used by GraphClust.

- **Output Interpretation**: Clustering results require careful biological interpretation.

## Examples

### Cluster RNA sequences
**Args:** `graphclust-cluster -i rna_sequences.fasta -o clusters/`
**Explanation:** Clusters RNA sequences into families using graph-based approach.

### Generate multiple sequence alignment
**Args:** `graphclust-align -i cluster.fasta -o alignment.sto`
**Explanation:** Generates multiple sequence alignment for a cluster of RNA sequences.

### Predict consensus structure
**Args:** `graphclust-structure -i alignment.sto -o consensus.structure`
**Explanation:** Predicts consensus secondary structure for aligned RNA sequences.

### Annotate clusters
**Args:** `graphclust-annotate -i clusters/ -d rfam -o annotations.txt`
**Explanation:** Annotates clusters using the Rfam database.

### Generate report
**Args:** `graphclust-report -i clusters/ -o report.html`
**Explanation:** Generates a comprehensive HTML report with clustering statistics.

### Batch processing
**Args:** `graphclust-batch -d datasets/ -o results/`
**Explanation:** Processes multiple RNA sequence files in a directory.

### Adjust clustering sensitivity
**Args:** `graphclust-cluster -i rna_sequences.fasta -s 0.8 -o clusters/`
**Explanation:** Sets sensitivity threshold for clustering.