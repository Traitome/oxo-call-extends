---
name: ucsc-clustergenes
category: analysis
description: UCSC clusterGenes - Tool for clustering genes.
tags: [ucsc-clustergenes, ucsc, gene-clustering, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC clusterGenes - A tool for clustering gene annotations.
- **Core Function**: Groups genes into clusters based on overlap or proximity.
- **Input**: Gene annotation file.
- **Output**: Clustered gene file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Gene analysis, functional annotation, comparative genomics.

## Pitfalls

- **Cluster Parameters**: Requires appropriate clustering thresholds.
- **Memory**: May require significant memory for large datasets.

## Examples

### Cluster genes
**Args:** `clusterGenes genes.bed > clusters.bed`
**Explanation:** Cluster genes based on overlap.

### With distance
**Args:** `clusterGenes -maxDistance=1000 genes.bed > clusters.bed`
**Explanation:** Cluster with maximum distance threshold.
