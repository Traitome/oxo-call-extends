---
name: domclust
category: utility
description: DomClust - Orthologous grouping tool for multiple genomes using domain architecture.
tags: [domclust, utility, orthology, domain-architecture, comparative-genomics]
author: oxo-call-community
source_url: "https://mbgd.nibb.ac.jp/domclust"
---

## Concepts

- **Tool Overview**: DomClust is a tool for clustering orthologous genes across multiple genomes.
- **Core Function**: Groups genes into orthologous clusters based on domain architecture similarity.
- **Input/Output**: Input: Protein sequences from multiple genomes. Output: Orthologous cluster assignments.
- **Algorithm**: Uses domain architecture comparison for orthology prediction.
- **Key Features**: Orthologous clustering, domain-based analysis, multi-genome comparison, visualization.
- **Installation**: `conda install -c bioconda domclust`

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence files for each genome.
- **Sequence Quality**: Poor quality sequences affect clustering accuracy.
- **Genome Completeness**: Incomplete genomes may produce incomplete clusters.
- **Memory Usage**: Analyzing many genomes simultaneously requires significant RAM.
- **Computation Time**: Large-scale analysis can be computationally intensive.
- **Output Interpretation**: Clusters require manual curation for biological validation.

## Examples

### Cluster orthologs
**Args:** `domclust --input genomes.txt --output clusters.tsv`
**Explanation:** Clusters orthologous genes across multiple genomes.

### With domain filtering
**Args:** `domclust --input genomes.txt --output clusters.tsv --min-domains 2`
**Explanation:** Only includes proteins with at least 2 domains.

### Output FASTA clusters
**Args:** `domclust --input genomes.txt --output clusters/ --fasta`
**Explanation:** Outputs each cluster as a separate FASTA file.

### Include statistics
**Args:** `domclust --input genomes.txt --output clusters.tsv --stats stats.txt`
**Explanation:** Generates statistics about cluster sizes and composition.

### Visualize clusters
**Args:** `domclust --input genomes.txt --output plot.png --visualize`
**Explanation:** Generates a visualization of orthologous clusters.

### Custom similarity threshold
**Args:** `domclust --input genomes.txt --output clusters.tsv --threshold 0.7`
**Explanation:** Sets a custom similarity threshold for clustering.